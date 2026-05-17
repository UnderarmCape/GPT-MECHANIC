import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = ROOT / "build_clean" / "chunks_jsonl_parts"
DEFAULT_LIMIT = 10
PREVIEW_CHARS = 320


def tokenize(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)?", value.casefold())


def field_text(record: dict, field: str) -> str:
    value = record.get(field, "")
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return str(value)


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


def score_record(record: dict, query: str, terms: list[str]) -> int:
    weighted_fields = (
        ("title", 12),
        ("headings", 10),
        ("source_path", 6),
        ("vehicle", 4),
        ("text", 1),
    )
    query_folded = query.casefold()
    score = 0
    matched_terms = set()

    for field, weight in weighted_fields:
        value = field_text(record, field).casefold()
        if not value:
            continue

        if query_folded and query_folded in value:
            score += weight * 20

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


def search(query: str, limit: int) -> list[dict]:
    terms = tokenize(query)
    if not terms:
        raise ValueError("Search query must include at least one alphanumeric term.")

    results = []
    for record in load_records(CORPUS_DIR):
        score = score_record(record, query, terms)
        if score:
            results.append({"score": score, "record": record})

    results.sort(
        key=lambda item: (
            -item["score"],
            str(item["record"].get("title", "")),
            str(item["record"].get("source_path", "")),
            str(item["record"].get("chunk_id", "")),
        )
    )
    return results[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search the cleaned GPT corpus in build_clean/chunks_jsonl_parts."
    )
    parser.add_argument("query", help="Search query, for example: \"CVT fluid replacement\"")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="Number of results to show")
    args = parser.parse_args()

    limit = max(1, args.limit)
    terms = tokenize(args.query)
    results = search(args.query, limit)

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
