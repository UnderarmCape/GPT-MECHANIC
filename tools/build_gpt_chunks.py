import argparse
import hashlib
import json
import re
from collections import deque
from pathlib import Path
from urllib.parse import unquote, urldefrag, urlparse

from bs4 import BeautifulSoup


HTML_EXTS = {".html", ".htm"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


def is_external_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "mailto", "tel", "javascript", "data"}


def resolve_local_path(root: Path, current_file: Path, link: str) -> Path | None:
    if not link:
        return None

    link = link.strip()
    if not link or link.startswith("#") or is_external_url(link):
        return None

    link_no_fragment = urldefrag(link)[0]
    link_no_fragment = unquote(link_no_fragment)

    candidate = (current_file.parent / link_no_fragment).resolve()

    try:
        candidate.relative_to(root)
    except ValueError:
        return None

    if candidate.is_dir():
        candidate = candidate / "index.html"

    return candidate


def load_soup(path: Path) -> BeautifulSoup:
    text = path.read_text(encoding="utf-8", errors="replace")
    return BeautifulSoup(text, "lxml")


def extract_title(soup: BeautifulSoup, path: Path) -> str:
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(" ", strip=True)
        if title:
            return title

    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(" ", strip=True)
        if title:
            return title

    return path.stem


def crawl_html_pages(root: Path, start_file: Path):
    queue = deque([start_file])
    seen = set()
    pages = []
    broken_links = []

    while queue:
        current = queue.popleft().resolve()

        if current in seen:
            continue

        if not current.exists() or current.suffix.lower() not in HTML_EXTS:
            continue

        seen.add(current)
        pages.append(current)

        soup = load_soup(current)

        for a in soup.find_all("a", href=True):
            target = resolve_local_path(root, current, a["href"])

            if not target:
                continue

            if target.suffix.lower() in HTML_EXTS:
                if target.exists():
                    if target not in seen:
                        queue.append(target)
                else:
                    broken_links.append({
                        "source": str(current.relative_to(root)),
                        "missing": a["href"],
                        "resolved": str(target)
                    })

    return pages, broken_links


def normalize_text(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def html_to_markdownish_text(soup: BeautifulSoup) -> str:
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    body = soup.body if soup.body else soup

    lines = []

    for element in body.descendants:
        if not getattr(element, "name", None):
            continue

        name = element.name.lower()

        if name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            level = int(name[1])
            text = element.get_text(" ", strip=True)
            if text:
                lines.append("\n" + ("#" * level) + " " + text + "\n")

        elif name == "p":
            text = element.get_text(" ", strip=True)
            if text:
                lines.append(text + "\n")

        elif name == "li":
            text = element.get_text(" ", strip=True)
            if text:
                lines.append("- " + text + "\n")

        elif name == "tr":
            cells = [c.get_text(" ", strip=True) for c in element.find_all(["th", "td"])]
            cells = [c for c in cells if c]
            if cells:
                lines.append(" | ".join(cells) + "\n")

    return normalize_text("\n".join(lines))


def extract_headings(markdownish_text: str):
    headings = []
    for line in markdownish_text.splitlines():
        if line.startswith("#"):
            headings.append(line.lstrip("#").strip())
    return headings


def extract_images(root: Path, path: Path, soup: BeautifulSoup):
    images = []

    body = soup.body if soup.body else soup

    for img in body.find_all("img", src=True):
        target = resolve_local_path(root, path, img["src"])
        if target and target.exists() and target.suffix.lower() in IMAGE_EXTS:
            images.append(str(target.relative_to(root)))
        else:
            images.append(img["src"])

    return sorted(set(images))


def extract_links(root: Path, path: Path, soup: BeautifulSoup):
    links = []

    body = soup.body if soup.body else soup

    for a in body.find_all("a", href=True):
        href = a["href"].strip()

        if not href:
            continue

        target = resolve_local_path(root, path, href)

        if target and target.exists():
            links.append(str(target.relative_to(root)))
        elif is_external_url(href):
            links.append(href)

    return sorted(set(links))


def chunk_text(text: str, max_chars: int, overlap_chars: int):
    if len(text) <= max_chars:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + max_chars

        if end < len(text):
            breakpoints = [
                text.rfind("\n# ", start, end),
                text.rfind("\n## ", start, end),
                text.rfind("\n\n", start, end),
                text.rfind(". ", start, end),
            ]

            best = max(breakpoints)

            if best > start + int(max_chars * 0.5):
                end = best + 1

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start = max(0, end - overlap_chars)

    return chunks


def make_chunk_id(source_path: str, chunk_index: int) -> str:
    raw = f"{source_path}:{chunk_index}"
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]
    return f"chunk_{digest}"


def write_markdown_chunk(md_dir: Path, chunk_number: int, record: dict):
    safe_title = re.sub(r"[^a-zA-Z0-9_-]+", "-", record["title"]).strip("-").lower()
    filename = f"{chunk_number:06d}_{safe_title[:60]}.md"
    path = md_dir / filename

    frontmatter = {
        "chunk_id": record["chunk_id"],
        "source_path": record["source_path"],
        "title": record["title"],
        "headings": record["headings"],
        "images": record["images"],
        "links": record["links"],
        "vehicle": record["vehicle"],
        "chunk_index": record["chunk_index"],
    }

    content = [
        "---",
        json.dumps(frontmatter, ensure_ascii=False, indent=2),
        "---",
        "",
        record["text"],
        "",
    ]

    path.write_text("\n".join(content), encoding="utf-8")
    return path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repo/manual root folder")
    parser.add_argument("--start", default="index.html", help="Starting HTML file")
    parser.add_argument("--vehicle", default="2016 Honda Civic LX 4D Sedan CVT")
    parser.add_argument("--max-chars", type=int, default=4500)
    parser.add_argument("--overlap-chars", type=int, default=800)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    start_file = (root / args.start).resolve()

    build_dir = root / "build"
    md_dir = build_dir / "gpt_chunks"
    build_dir.mkdir(exist_ok=True)
    md_dir.mkdir(exist_ok=True)

    if not start_file.exists():
        raise FileNotFoundError(f"Start file not found: {start_file}")

    pages, broken_links = crawl_html_pages(root, start_file)

    jsonl_path = build_dir / "chunks.jsonl"
    manifest_path = build_dir / "chunks_manifest.json"

    records = []
    markdown_files = []
    chunk_number = 1

    with jsonl_path.open("w", encoding="utf-8") as f:
        for page in pages:
            soup = load_soup(page)

            title = extract_title(soup, page)
            source_path = str(page.relative_to(root))
            text = html_to_markdownish_text(soup)

            if not text:
                continue

            headings = extract_headings(text)
            images = extract_images(root, page, soup)
            links = extract_links(root, page, soup)

            text_chunks = chunk_text(
                text=text,
                max_chars=args.max_chars,
                overlap_chars=args.overlap_chars,
            )

            for idx, chunk in enumerate(text_chunks, start=1):
                record = {
                    "chunk_id": make_chunk_id(source_path, idx),
                    "source_path": source_path,
                    "title": title,
                    "headings": headings,
                    "text": chunk,
                    "images": images,
                    "links": links,
                    "vehicle": args.vehicle,
                    "chunk_index": idx,
                    "total_chunks_for_page": len(text_chunks),
                }

                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                records.append(record)

                md_path = write_markdown_chunk(md_dir, chunk_number, record)
                markdown_files.append(str(md_path.relative_to(root)))

                chunk_number += 1

    manifest = {
        "vehicle": args.vehicle,
        "start_file": str(start_file.relative_to(root)),
        "html_pages_found": len(pages),
        "chunks_created": len(records),
        "jsonl_output": str(jsonl_path.relative_to(root)),
        "markdown_output_dir": str(md_dir.relative_to(root)),
        "markdown_files_created": len(markdown_files),
        "broken_links": broken_links,
        "source_pages": [str(p.relative_to(root)) for p in pages],
    }

    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"HTML pages found: {len(pages)}")
    print(f"Chunks created: {len(records)}")
    print(f"Wrote JSONL: {jsonl_path}")
    print(f"Wrote Markdown chunks to: {md_dir}")
    print(f"Wrote manifest: {manifest_path}")


if __name__ == "__main__":
    main()