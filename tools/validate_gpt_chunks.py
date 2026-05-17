import argparse
import hashlib
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED_FIELDS = (
    "chunk_id",
    "source_path",
    "title",
    "text",
    "images",
    "links",
    "vehicle",
    "chunk_index",
)

EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}
MIN_TEXT_CHARS = 100
MAX_TEXT_CHARS = 8000

ROOT = Path(__file__).resolve().parents[1]


def resolve_repo_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return ROOT / path


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def normalize_for_display(value) -> str:
    if value is None:
        return ""
    return str(value).replace("\n", "\\n")


def make_ref(part_path: Path, line_number: int, record: dict | None = None) -> dict:
    record = record or {}
    return {
        "part": rel(part_path),
        "line": line_number,
        "chunk_id": normalize_for_display(record.get("chunk_id")),
        "source_path": normalize_for_display(record.get("source_path")),
    }


def format_ref(ref: dict) -> str:
    bits = [f"`{ref['part']}:{ref['line']}`"]
    if ref.get("chunk_id"):
        bits.append(f"chunk_id=`{ref['chunk_id']}`")
    if ref.get("source_path"):
        bits.append(f"source_path=`{ref['source_path']}`")
    return " | ".join(bits)


def is_external_path(value: str) -> bool:
    candidate = value.strip().replace("\\", "/")
    parsed = urlsplit(candidate)
    return parsed.scheme.lower() in EXTERNAL_SCHEMES


def strip_query_fragment(value: str) -> str:
    candidate = value.strip().replace("\\", "/")
    parsed = urlsplit(candidate)
    if parsed.scheme and parsed.scheme.lower() not in EXTERNAL_SCHEMES:
        return unquote(candidate.split("#", 1)[0].split("?", 1)[0])
    path = parsed.path if parsed.scheme or parsed.netloc else candidate
    return unquote(path.split("#", 1)[0].split("?", 1)[0])


def is_within_repo(path: Path) -> bool:
    try:
        path.resolve().relative_to(ROOT.resolve())
        return True
    except ValueError:
        return False


def repo_relative_candidate(value: str) -> Path | None:
    cleaned = strip_query_fragment(value)
    if not cleaned:
        return None

    path = Path(cleaned)
    if path.is_absolute():
        return path
    return ROOT / cleaned.lstrip("/\\")


def repo_path_exists(value: str) -> bool:
    candidate = repo_relative_candidate(value)
    if candidate is None or not is_within_repo(candidate):
        return False
    return candidate.exists()


def local_image_candidates(image_path: str, source_path: str | None) -> list[Path]:
    cleaned = strip_query_fragment(image_path)
    if not cleaned:
        return []

    path = Path(cleaned)
    if path.is_absolute():
        return [path]

    candidates = [ROOT / cleaned.lstrip("/\\")]

    if source_path:
        source_candidate = repo_relative_candidate(source_path)
        if source_candidate is not None:
            candidates.append(source_candidate.parent / cleaned)

    deduped = []
    seen = set()
    for candidate in candidates:
        key = str(candidate)
        if key not in seen:
            deduped.append(candidate)
            seen.add(key)
    return deduped


def local_image_exists(image_path: str, source_path: str | None) -> bool:
    for candidate in local_image_candidates(image_path, source_path):
        if is_within_repo(candidate) and candidate.exists():
            return True
    return False


def text_preview(text: str, max_chars: int = 160) -> str:
    preview = " ".join(text.split())
    if len(preview) > max_chars:
        preview = preview[: max_chars - 3].rstrip() + "..."
    return preview


def load_manifest(manifest_path: Path, issues: dict) -> dict | None:
    if not manifest_path.exists():
        issues["manifest"].append(f"Manifest file is missing: `{rel(manifest_path)}`")
        return None

    try:
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues["manifest"].append(
            f"Manifest is not valid JSON: `{rel(manifest_path)}:{exc.lineno}:{exc.colno}` {exc.msg}"
        )
    except OSError as exc:
        issues["manifest"].append(f"Could not read manifest `{rel(manifest_path)}`: {exc}")
    return None


def add_section(lines: list[str], title: str, items: list, formatter) -> None:
    lines.append(f"## {title}")
    lines.append("")
    if not items:
        lines.append("No issues found.")
        lines.append("")
        return

    for item in items:
        lines.append(formatter(item))
    lines.append("")


def validate(parts_dir: Path, manifest_path: Path) -> tuple[dict, dict]:
    issues = defaultdict(list)
    stats = {
        "part_files": 0,
        "total_lines": 0,
        "total_chunks": 0,
        "valid_json_lines": 0,
        "local_image_paths_checked": 0,
        "external_image_paths_skipped": 0,
        "manifest_chunks_created": None,
    }
    part_stats = []
    chunk_id_locations = defaultdict(list)
    text_hash_locations = defaultdict(list)
    text_hash_meta = {}
    source_path_cache = {}
    image_path_cache = {}

    manifest = load_manifest(manifest_path, issues)
    if manifest is not None:
        stats["manifest_chunks_created"] = manifest.get("chunks_created")

    part_paths = sorted(parts_dir.glob("*.jsonl"))
    if not parts_dir.exists():
        issues["parts"].append(f"JSONL parts directory is missing: `{rel(parts_dir)}`")
    elif not part_paths:
        issues["parts"].append(f"No JSONL part files found in `{rel(parts_dir)}`")

    for part_path in part_paths:
        stats["part_files"] += 1
        current_part = {
            "part": rel(part_path),
            "lines": 0,
            "valid_json_lines": 0,
            "valid_chunks": 0,
            "invalid_json_lines": 0,
            "non_object_json_lines": 0,
        }

        with part_path.open("r", encoding="utf-8") as handle:
            for line_number, raw_line in enumerate(handle, 1):
                stats["total_lines"] += 1
                current_part["lines"] += 1
                line = raw_line.rstrip("\n")

                if not line.strip():
                    current_part["invalid_json_lines"] += 1
                    issues["json"].append(
                        {
                            "part": rel(part_path),
                            "line": line_number,
                            "error": "blank line is not valid JSON",
                        }
                    )
                    continue

                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    current_part["invalid_json_lines"] += 1
                    issues["json"].append(
                        {
                            "part": rel(part_path),
                            "line": line_number,
                            "error": f"{exc.msg} at column {exc.colno}",
                        }
                    )
                    continue

                stats["valid_json_lines"] += 1
                current_part["valid_json_lines"] += 1

                if not isinstance(record, dict):
                    current_part["non_object_json_lines"] += 1
                    issues["json_objects"].append(
                        {
                            "part": rel(part_path),
                            "line": line_number,
                            "type": type(record).__name__,
                        }
                    )
                    continue

                stats["total_chunks"] += 1
                current_part["valid_chunks"] += 1
                ref = make_ref(part_path, line_number, record)

                missing = [field for field in REQUIRED_FIELDS if field not in record]
                if missing:
                    issues["missing_fields"].append({"ref": ref, "missing": missing})

                chunk_id = record.get("chunk_id")
                if isinstance(chunk_id, str) and chunk_id:
                    chunk_id_locations[chunk_id].append(ref)
                elif "chunk_id" in record:
                    issues["field_types"].append(
                        {"ref": ref, "field": "chunk_id", "expected": "non-empty string"}
                    )

                text = record.get("text")
                if not isinstance(text, str):
                    if "text" in record:
                        issues["field_types"].append(
                            {"ref": ref, "field": "text", "expected": "string"}
                        )
                    text = ""

                text_len = len(text)
                if not text.strip():
                    issues["empty_text"].append({"ref": ref, "length": text_len})
                elif text_len < MIN_TEXT_CHARS:
                    issues["short_text"].append(
                        {"ref": ref, "length": text_len, "preview": text_preview(text)}
                    )
                elif text_len > MAX_TEXT_CHARS:
                    issues["long_text"].append({"ref": ref, "length": text_len})

                text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
                text_hash_locations[text_hash].append(ref)
                text_hash_meta.setdefault(
                    text_hash, {"length": text_len, "preview": text_preview(text)}
                )

                source_path = record.get("source_path")
                if isinstance(source_path, str) and source_path.strip():
                    if source_path not in source_path_cache:
                        source_path_cache[source_path] = repo_path_exists(source_path)
                    if not source_path_cache[source_path]:
                        issues["source_paths"].append({"ref": ref, "path": source_path})
                elif "source_path" in record:
                    issues["field_types"].append(
                        {"ref": ref, "field": "source_path", "expected": "non-empty string"}
                    )

                images = record.get("images")
                if isinstance(images, list):
                    for image in images:
                        if not isinstance(image, str):
                            issues["image_paths"].append(
                                {
                                    "ref": ref,
                                    "image": normalize_for_display(image),
                                    "reason": "image path is not a string",
                                }
                            )
                            continue

                        if not image.strip():
                            issues["image_paths"].append(
                                {"ref": ref, "image": image, "reason": "image path is empty"}
                            )
                            continue

                        if is_external_path(image):
                            stats["external_image_paths_skipped"] += 1
                            continue

                        stats["local_image_paths_checked"] += 1
                        cache_key = (source_path if isinstance(source_path, str) else "", image)
                        if cache_key not in image_path_cache:
                            image_path_cache[cache_key] = local_image_exists(
                                image, source_path if isinstance(source_path, str) else None
                            )
                        if not image_path_cache[cache_key]:
                            issues["image_paths"].append(
                                {
                                    "ref": ref,
                                    "image": image,
                                    "reason": "local image file does not exist",
                                }
                            )
                elif "images" in record:
                    issues["field_types"].append(
                        {"ref": ref, "field": "images", "expected": "list"}
                    )

                links = record.get("links")
                if "links" in record and not isinstance(links, list):
                    issues["field_types"].append(
                        {"ref": ref, "field": "links", "expected": "list"}
                    )

        part_stats.append(current_part)

    duplicate_chunk_ids = {
        chunk_id: locations
        for chunk_id, locations in chunk_id_locations.items()
        if len(locations) > 1
    }
    duplicate_text_hashes = {
        text_hash: locations
        for text_hash, locations in text_hash_locations.items()
        if len(locations) > 1
    }

    for chunk_id, locations in sorted(duplicate_chunk_ids.items()):
        issues["duplicate_chunk_ids"].append({"chunk_id": chunk_id, "locations": locations})

    for text_hash, locations in sorted(duplicate_text_hashes.items()):
        meta = text_hash_meta.get(text_hash, {})
        issues["duplicate_text_hashes"].append(
            {
                "text_hash": text_hash,
                "locations": locations,
                "length": meta.get("length", 0),
                "preview": meta.get("preview", ""),
            }
        )

    if isinstance(stats["manifest_chunks_created"], int):
        if stats["manifest_chunks_created"] != stats["total_chunks"]:
            issues["manifest"].append(
                "Manifest `chunks_created` is "
                f"{stats['manifest_chunks_created']}, but JSONL parts contain "
                f"{stats['total_chunks']} valid chunk records."
            )

    stats["part_stats"] = part_stats
    stats["duplicate_chunk_id_values"] = len(duplicate_chunk_ids)
    stats["duplicate_chunk_id_chunks"] = sum(len(v) for v in duplicate_chunk_ids.values())
    stats["duplicate_text_hash_values"] = len(duplicate_text_hashes)
    stats["duplicate_text_hash_chunks"] = sum(len(v) for v in duplicate_text_hashes.values())

    return stats, issues


def issue_count(stats: dict, issues: dict) -> int:
    direct_keys = [
        "parts",
        "json",
        "json_objects",
        "missing_fields",
        "field_types",
        "empty_text",
        "short_text",
        "long_text",
        "source_paths",
        "image_paths",
        "manifest",
    ]
    total = sum(len(issues[key]) for key in direct_keys)
    total += stats["duplicate_chunk_id_chunks"]
    total += stats["duplicate_text_hash_chunks"]
    return total


def render_report(stats: dict, issues: dict, parts_dir: Path, manifest_path: Path) -> str:
    total_issues = issue_count(stats, issues)
    status = "PASS" if total_issues == 0 else "ISSUES FOUND"
    manifest_count = stats["manifest_chunks_created"]
    manifest_display = "not available" if manifest_count is None else str(manifest_count)

    lines = [
        "# GPT Chunk Validation Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Repository: `{ROOT}`",
        f"Corpus: `{rel(parts_dir)}/*.jsonl`",
        f"Manifest: `{rel(manifest_path)}`",
        f"Status: **{status}**",
        "",
        "## Summary",
        "",
        f"- JSONL part files scanned: **{stats['part_files']}**",
        f"- Total lines read: **{stats['total_lines']}**",
        f"- Total valid chunk records: **{stats['total_chunks']}**",
        f"- Manifest `chunks_created`: **{manifest_display}**",
        f"- Total validation issue references: **{total_issues}**",
        "",
        "| Check | Result |",
        "| --- | ---: |",
        f"| Invalid JSON lines | {len(issues['json'])} |",
        f"| Valid JSON lines that are not objects | {len(issues['json_objects'])} |",
        f"| Chunks missing required fields | {len(issues['missing_fields'])} |",
        f"| Field type issues | {len(issues['field_types'])} |",
        f"| Empty text chunks | {len(issues['empty_text'])} |",
        f"| Chunks under {MIN_TEXT_CHARS} characters | {len(issues['short_text'])} |",
        f"| Chunks over {MAX_TEXT_CHARS} characters | {len(issues['long_text'])} |",
        f"| Duplicate `chunk_id` values | {stats['duplicate_chunk_id_values']} |",
        f"| Chunks affected by duplicate `chunk_id` values | {stats['duplicate_chunk_id_chunks']} |",
        f"| Duplicate text hashes | {stats['duplicate_text_hash_values']} |",
        f"| Chunks affected by duplicate text hashes | {stats['duplicate_text_hash_chunks']} |",
        f"| Missing source paths | {len(issues['source_paths'])} |",
        f"| Missing or invalid local image paths | {len(issues['image_paths'])} |",
        f"| Local image path references checked | {stats['local_image_paths_checked']} |",
        f"| External image path references skipped | {stats['external_image_paths_skipped']} |",
        f"| Manifest or parts setup issues | {len(issues['manifest']) + len(issues['parts'])} |",
        "",
        "## Part File Counts",
        "",
        "| Part file | Lines | Valid JSON | Valid chunks | Invalid JSON | Non-object JSON |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]

    for part in stats["part_stats"]:
        lines.append(
            f"| `{part['part']}` | {part['lines']} | {part['valid_json_lines']} | "
            f"{part['valid_chunks']} | {part['invalid_json_lines']} | "
            f"{part['non_object_json_lines']} |"
        )
    lines.append("")

    add_section(
        lines,
        "Parts And Manifest Issues",
        issues["parts"] + issues["manifest"],
        lambda item: f"- {item}",
    )
    add_section(
        lines,
        "Invalid JSON Lines",
        issues["json"],
        lambda item: f"- `{item['part']}:{item['line']}` - {item['error']}",
    )
    add_section(
        lines,
        "Valid JSON Lines That Are Not Objects",
        issues["json_objects"],
        lambda item: f"- `{item['part']}:{item['line']}` - JSON type `{item['type']}`",
    )
    add_section(
        lines,
        "Missing Required Fields",
        issues["missing_fields"],
        lambda item: f"- {format_ref(item['ref'])} | missing: `{', '.join(item['missing'])}`",
    )
    add_section(
        lines,
        "Field Type Issues",
        issues["field_types"],
        lambda item: (
            f"- {format_ref(item['ref'])} | field `{item['field']}` expected "
            f"{item['expected']}"
        ),
    )
    add_section(
        lines,
        "Empty Text Chunks",
        issues["empty_text"],
        lambda item: f"- {format_ref(item['ref'])} | length={item['length']}",
    )
    add_section(
        lines,
        f"Chunks Under {MIN_TEXT_CHARS} Characters",
        issues["short_text"],
        lambda item: (
            f"- {format_ref(item['ref'])} | length={item['length']} | "
            f"preview={json.dumps(item['preview'])}"
        ),
    )
    add_section(
        lines,
        f"Chunks Over {MAX_TEXT_CHARS} Characters",
        issues["long_text"],
        lambda item: f"- {format_ref(item['ref'])} | length={item['length']}",
    )

    lines.append("## Duplicate `chunk_id` Values")
    lines.append("")
    if not issues["duplicate_chunk_ids"]:
        lines.append("No issues found.")
        lines.append("")
    else:
        for item in issues["duplicate_chunk_ids"]:
            lines.append(f"### `{item['chunk_id']}` ({len(item['locations'])} chunks)")
            lines.append("")
            for ref in item["locations"]:
                lines.append(f"- {format_ref(ref)}")
            lines.append("")

    lines.append("## Duplicate Text Hashes")
    lines.append("")
    if not issues["duplicate_text_hashes"]:
        lines.append("No issues found.")
        lines.append("")
    else:
        for item in issues["duplicate_text_hashes"]:
            lines.append(
                f"### `{item['text_hash']}` ({len(item['locations'])} chunks, "
                f"length={item['length']})"
            )
            lines.append("")
            if item["preview"]:
                lines.append(f"Preview: {json.dumps(item['preview'])}")
                lines.append("")
            for ref in item["locations"]:
                lines.append(f"- {format_ref(ref)}")
            lines.append("")

    add_section(
        lines,
        "Missing Source Paths",
        issues["source_paths"],
        lambda item: f"- {format_ref(item['ref'])} | missing path=`{item['path']}`",
    )
    add_section(
        lines,
        "Missing Or Invalid Local Image Paths",
        issues["image_paths"],
        lambda item: (
            f"- {format_ref(item['ref'])} | image=`{item['image']}` | "
            f"{item['reason']}"
        ),
    )

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--build-dir",
        default="build",
        help="Build output directory to validate, relative to the repo root unless absolute",
    )
    parser.add_argument(
        "--report",
        help="Markdown report path. Defaults to <build-dir>/validation_report.md",
    )
    args = parser.parse_args()

    build_dir = resolve_repo_path(args.build_dir)
    parts_dir = build_dir / "chunks_jsonl_parts"
    manifest_path = build_dir / "chunks_manifest.json"
    report_path = resolve_repo_path(args.report) if args.report else build_dir / "validation_report.md"

    stats, issues = validate(parts_dir, manifest_path)
    report = render_report(stats, issues, parts_dir, manifest_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")

    total_issues = issue_count(stats, issues)
    status = "PASS" if total_issues == 0 else "ISSUES FOUND"

    print("GPT chunk validation complete")
    print(f"Status: {status}")
    print(f"Report: {rel(report_path)}")
    print(f"JSONL part files scanned: {stats['part_files']}")
    print(f"Total valid chunk records: {stats['total_chunks']}")
    print(f"Invalid JSON lines: {len(issues['json'])}")
    print(f"Missing required field chunks: {len(issues['missing_fields'])}")
    print(f"Empty text chunks: {len(issues['empty_text'])}")
    print(f"Chunks under {MIN_TEXT_CHARS} chars: {len(issues['short_text'])}")
    print(f"Chunks over {MAX_TEXT_CHARS} chars: {len(issues['long_text'])}")
    print(f"Duplicate chunk_id values: {stats['duplicate_chunk_id_values']}")
    print(f"Duplicate text hashes: {stats['duplicate_text_hash_values']}")
    print(f"Missing source paths: {len(issues['source_paths'])}")
    print(f"Missing/invalid local image paths: {len(issues['image_paths'])}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
