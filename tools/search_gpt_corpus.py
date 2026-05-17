import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = ROOT / "build_clean" / "chunks_jsonl_parts"
DEFAULT_LIMIT = 10
PREVIEW_CHARS = 320
INDEX_SOURCE_PATHS = {"pages\\3.html", "pages/3.html"}
INDEX_SOURCE_PATHS_NORMALIZED = {path.replace("/", "\\").casefold() for path in INDEX_SOURCE_PATHS}
SINGLE_PAGE_TITLE = "repair and diagnosis (single page)"
PROCEDURE_TITLE_WORDS = (
    "replacement",
    "inspection",
    "removal",
    "installation",
    "adjustment",
    "test",
    "troubleshooting",
    "specifications",
)


def tokenize(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)?", value.casefold())


def field_text(record: dict, field: str) -> str:
    value = record.get(field, "")
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return str(value)


def is_index_page(record: dict) -> bool:
    source_path = str(record.get("source_path", "")).replace("/", "\\").casefold()
    title = str(record.get("title", "")).casefold()
    return (
        source_path in INDEX_SOURCE_PATHS_NORMALIZED
        or "single page" in title
        or " index" in title
        or title.endswith("index")
        or title == SINGLE_PAGE_TITLE
    )


def is_video_page(record: dict) -> bool:
    return "- video" in str(record.get("title", "")).casefold()


def normalize_source_path(value: str) -> str:
    return value.replace("/", "\\").casefold().strip()


def normalize_title(value: str) -> str:
    return re.sub(r"\s+", " ", value).casefold().strip()


def load_records(corpus_dir: Path):
    part_paths = sorted(corpus_dir.glob("*.jsonl"))
    if not corpus_dir.exists():
        raise FileNotFoundError(f"Corpus directory not found: {corpus_dir}")
    if not part_paths:
        raise FileNotFoundError(f"No JSONL part files found in: {corpus_dir}")

    for part_path in part_paths:
        with part_path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Invalid JSON in {part_path}:{line_number}: {exc.msg}"
                    ) from exc
                if isinstance(record, dict):
                    yield record


def score_record(
    record: dict,
    query: str,
    terms: list[str],
    include_index: bool = False,
    include_video: bool = False,
) -> int | None:
    if is_index_page(record) and not include_index:
        return None

    weighted_fields = (
        ("title", 12),
        ("headings", 10),
        ("source_path", 6),
        ("vehicle", 4),
        ("text", 1),
    )
    query_folded = query.casefold()
    query_has_video = "video" in terms
    score = 0
    matched_terms = set()
    title = field_text(record, "title").casefold()
    text = field_text(record, "text").casefold()

    if query_folded and query_folded in title:
        score += 900
    if query_folded and query_folded in text:
        score += 500

    title_tokens = tokenize(title)
    unique_terms = set(terms)
    title_term_matches = {term for term in unique_terms if term in title_tokens or term in title}
    if unique_terms and title_term_matches == unique_terms:
        score += 850

    for term in terms:
        if term in title_tokens:
            score += 90
        elif term in title:
            score += 45

    if any(word in title_tokens for word in PROCEDURE_TITLE_WORDS):
        score += 180

    for field, weight in weighted_fields:
        value = field_text(record, field).casefold()
        if not value:
            continue

        if query_folded and query_folded in value:
            score += weight * 12

        field_tokens = tokenize(value)
        token_counts = {}
        for token in field_tokens:
            token_counts[token] = token_counts.get(token, 0) + 1

        for term in terms:
            count = token_counts.get(term, 0)
            if count:
                score += count * weight
                matched_terms.add(term)
            elif term in value:
                score += weight
                matched_terms.add(term)

    if terms and len(matched_terms) == len(set(terms)):
        score += 30

    if is_index_page(record):
        score -= 800
        if str(record.get("source_path", "")).replace("/", "\\").casefold() == "pages\\3.html":
            score -= 700
        if "single page" in title:
            score -= 500
        if " index" in title or title.endswith("index"):
            score -= 700
        if title == SINGLE_PAGE_TITLE:
            score -= 700

    if is_video_page(record) and not include_video and not query_has_video:
        score -= 2000

    return score


def find_preview(text: str, terms: list[str], width: int = PREVIEW_CHARS) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if not compact:
        return ""

    matches = []
    compact_folded = compact.casefold()
    for term in terms:
        match = re.search(re.escape(term), compact_folded)
        if match:
            matches.append(match.start())

    center = min(matches) if matches else 0
    start = max(0, center - width // 3)
    end = min(len(compact), start + width)
    start = max(0, end - width)

    preview = compact[start:end]
    if start > 0:
        preview = "..." + preview.lstrip()
    if end < len(compact):
        preview = preview.rstrip() + "..."
    return preview


def format_images(images) -> str:
    if not images:
        return "none"
    if not isinstance(images, list):
        return str(images)
    return ", ".join(str(image) for image in images)


def print_result(rank: int, result: dict, terms: list[str]) -> None:
    record = result["record"]
    print(f"{rank}. score: {result['score']}")
    print(f"   title: {record.get('title', '')}")
    print(f"   source_path: {record.get('source_path', '')}")
    print(f"   chunk_id: {record.get('chunk_id', '')}")
    print(f"   images: {format_images(record.get('images'))}")
    print(f"   preview: {find_preview(str(record.get('text', '')), terms)}")
    print()


def dedupe_results(results: list[dict]) -> list[dict]:
    deduped = []
    seen_source_paths = set()
    seen_titles = set()

    for result in results:
        record = result["record"]
        source_path = normalize_source_path(str(record.get("source_path", "")))
        title = normalize_title(str(record.get("title", "")))

        if source_path and source_path in seen_source_paths:
            continue
        if title and title in seen_titles:
            continue

        deduped.append(result)
        if source_path:
            seen_source_paths.add(source_path)
        if title:
            seen_titles.add(title)

    return deduped


def search(
    query: str,
    limit: int,
    include_index: bool = False,
    include_video: bool = False,
    dedupe_displayed_results: bool = True,
) -> list[dict]:
    terms = tokenize(query)
    if not terms:
        raise ValueError("Search query must include at least one alphanumeric term.")

    results = []
    for record in load_records(CORPUS_DIR):
        score = score_record(record, query, terms, include_index, include_video)
        if score is not None and score > 0:
            results.append({"score": score, "record": record})

    results.sort(
        key=lambda item: (
            -item["score"],
            str(item["record"].get("title", "")),
            str(item["record"].get("source_path", "")),
            str(item["record"].get("chunk_id", "")),
        )
    )

    if dedupe_displayed_results:
        results = dedupe_results(results)

    return results[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search the cleaned GPT corpus in build_clean/chunks_jsonl_parts."
    )
    parser.add_argument("query", help="Search query, for example: \"CVT fluid replacement\"")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="Number of results to show")
    parser.add_argument(
        "--include-index",
        action="store_true",
        help="Include index/navigation pages such as pages/3.html in results",
    )
    parser.add_argument(
        "--include-video",
        action="store_true",
        help="Avoid penalizing video pages when the query does not include video",
    )
    parser.add_argument(
        "--no-dedupe-results",
        action="store_true",
        help="Allow repeated chunks from the same source path or exact same title",
    )
    args = parser.parse_args()

    limit = max(1, args.limit)
    terms = tokenize(args.query)
    results = search(
        args.query,
        limit,
        args.include_index,
        args.include_video,
        not args.no_dedupe_results,
    )

    print(f"Query: {args.query}")
    print(f"Corpus: {CORPUS_DIR}")
    print(f"Results: {len(results)}")
    print()

    if not results:
        print("No matches found.")
        return 0

    for rank, result in enumerate(results, start=1):
        print_result(rank, result, terms)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
