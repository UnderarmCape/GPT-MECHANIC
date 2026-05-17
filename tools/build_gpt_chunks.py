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
IMPORTANT_KEYWORDS = (
    "WARNING",
    "CAUTION",
    "NOTE",
    "DTC",
    "torque",
    "specification",
    "fluid",
)
DEFAULT_PART_MAX_BYTES = 45 * 1024 * 1024


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


def normalized_text_hash(text: str) -> str:
    normalized = normalize_text(text)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def contains_important_keyword(text: str) -> bool:
    text_folded = text.casefold()
    return any(keyword.casefold() in text_folded for keyword in IMPORTANT_KEYWORDS)


def resolve_output_dir(root: Path, output_dir: str) -> Path:
    path = Path(output_dir)
    if path.is_absolute():
        return path
    return root / path


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

    for optional_field in ["duplicate_sources", "duplicate_count"]:
        if optional_field in record:
            frontmatter[optional_field] = record[optional_field]

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


def write_jsonl_and_parts(records: list[dict], jsonl_path: Path, parts_dir: Path, part_max_bytes: int):
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    parts_dir.mkdir(parents=True, exist_ok=True)

    part_files = []
    part_handle = None
    part_number = 0
    part_bytes = 0

    def open_next_part():
        nonlocal part_handle, part_number, part_bytes
        if part_handle:
            part_handle.close()
        part_number += 1
        part_bytes = 0
        part_path = parts_dir / f"chunks_part_{part_number:04d}.jsonl"
        part_files.append(part_path)
        part_handle = part_path.open("wb")

    try:
        with jsonl_path.open("wb") as jsonl_file:
            for record in records:
                encoded = (json.dumps(record, ensure_ascii=False) + "\n").encode("utf-8")
                jsonl_file.write(encoded)

                if part_handle is None:
                    open_next_part()
                elif part_bytes and part_bytes + len(encoded) > part_max_bytes:
                    open_next_part()

                part_handle.write(encoded)
                part_bytes += len(encoded)
    finally:
        if part_handle:
            part_handle.close()

    return part_files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repo/manual root folder")
    parser.add_argument("--start", default="index.html", help="Starting HTML file")
    parser.add_argument("--vehicle", default="2016 Honda Civic LX 4D Sedan CVT")
    parser.add_argument("--max-chars", type=int, default=4500)
    parser.add_argument("--overlap-chars", type=int, default=800)
    parser.add_argument("--output-dir", default="build", help="Output directory relative to the repo root")
    parser.add_argument("--dedupe-exact", action="store_true", help="Merge chunks with identical normalized text")
    parser.add_argument(
        "--min-chars",
        type=int,
        default=0,
        help="Skip chunks shorter than this unless they contain important service keywords",
    )
    parser.add_argument(
        "--part-max-bytes",
        type=int,
        default=DEFAULT_PART_MAX_BYTES,
        help="Maximum UTF-8 bytes per split JSONL part file",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    start_file = (root / args.start).resolve()
    min_chars = max(0, args.min_chars)
    part_max_bytes = max(1, args.part_max_bytes)

    build_dir = resolve_output_dir(root, args.output_dir)
    md_dir = build_dir / "gpt_chunks"
    parts_dir = build_dir / "chunks_jsonl_parts"
    build_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)

    if not start_file.exists():
        raise FileNotFoundError(f"Start file not found: {start_file}")

    pages, broken_links = crawl_html_pages(root, start_file)

    jsonl_path = build_dir / "chunks.jsonl"
    manifest_path = build_dir / "chunks_manifest.json"

    records = []
    markdown_files = []
    dedupe_index = {}
    duplicate_hashes = set()
    original_chunk_count = 0
    short_chunks_skipped = 0
    short_chunks_kept_for_keywords = 0
    duplicate_chunks_merged = 0

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

        original_chunk_count += len(text_chunks)

        for idx, chunk in enumerate(text_chunks, start=1):
            if min_chars and len(chunk) < min_chars:
                if contains_important_keyword(chunk):
                    short_chunks_kept_for_keywords += 1
                else:
                    short_chunks_skipped += 1
                    continue

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

            if args.dedupe_exact:
                digest = normalized_text_hash(chunk)
                if digest in dedupe_index:
                    kept_record = records[dedupe_index[digest]]
                    duplicate_sources = kept_record.setdefault("duplicate_sources", [])
                    if source_path not in duplicate_sources:
                        duplicate_sources.append(source_path)
                    kept_record["duplicate_count"] = kept_record.get("duplicate_count", 0) + 1
                    duplicate_chunks_merged += 1
                    duplicate_hashes.add(digest)
                    continue

                record["duplicate_sources"] = []
                record["duplicate_count"] = 0
                dedupe_index[digest] = len(records)

            records.append(record)

    part_files = write_jsonl_and_parts(records, jsonl_path, parts_dir, part_max_bytes)

    for chunk_number, record in enumerate(records, start=1):
        md_path = write_markdown_chunk(md_dir, chunk_number, record)
        markdown_files.append(str(md_path.relative_to(root)))

    manifest = {
        "vehicle": args.vehicle,
        "start_file": str(start_file.relative_to(root)),
        "html_pages_found": len(pages),
        "original_chunks_created": original_chunk_count,
        "chunks_created": len(records),
        "clean_chunks_created": len(records),
        "dedupe_exact": args.dedupe_exact,
        "duplicate_text_hashes_merged": len(duplicate_hashes),
        "duplicate_chunks_merged": duplicate_chunks_merged,
        "min_chars": min_chars,
        "important_keywords": list(IMPORTANT_KEYWORDS),
        "short_chunks_skipped": short_chunks_skipped,
        "short_chunks_kept_for_keywords": short_chunks_kept_for_keywords,
        "jsonl_output": str(jsonl_path.relative_to(root)),
        "jsonl_parts_dir": str(parts_dir.relative_to(root)),
        "jsonl_part_files_created": len(part_files),
        "jsonl_part_files": [str(path.relative_to(root)) for path in part_files],
        "jsonl_part_max_bytes": part_max_bytes,
        "markdown_output_dir": str(md_dir.relative_to(root)),
        "markdown_files_created": len(markdown_files),
        "broken_links": broken_links,
        "source_pages": [str(p.relative_to(root)) for p in pages],
    }

    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"HTML pages found: {len(pages)}")
    print(f"Original chunks generated: {original_chunk_count}")
    print(f"Clean chunks created: {len(records)}")
    print(f"Duplicate chunks removed/merged: {duplicate_chunks_merged}")
    print(f"Short chunks skipped: {short_chunks_skipped}")
    print(f"JSONL part files created: {len(part_files)}")
    print(f"Wrote JSONL: {jsonl_path}")
    print(f"Wrote JSONL parts to: {parts_dir}")
    print(f"Wrote Markdown chunks to: {md_dir}")
    print(f"Wrote manifest: {manifest_path}")


if __name__ == "__main__":
    main()
