import argparse
import json
import re
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS_DIR = ROOT / "build_clean" / "chunks_jsonl_parts"
DEFAULT_DB_PATH = ROOT / "build_clean" / "gpt_corpus.sqlite"
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


def tokenize(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", value.casefold())


def text_value(value) -> str:
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    if value is None:
        return ""
    return str(value)


def json_value(value) -> str:
    if value is None:
        value = []
    return json.dumps(value, ensure_ascii=False)


def decode_json_field(value: str):
    if not value:
        return []
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


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


def has_fts5(conn: sqlite3.Connection) -> bool:
    try:
        conn.execute("CREATE VIRTUAL TABLE temp._fts5_check USING fts5(value)")
        conn.execute("DROP TABLE temp._fts5_check")
        return True
    except sqlite3.DatabaseError:
        return False


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


def create_schema(conn: sqlite3.Connection, fts5_enabled: bool) -> None:
    conn.executescript(
        """
        DROP TABLE IF EXISTS chunks_fts;
        DROP TABLE IF EXISTS chunks;
        DROP TABLE IF EXISTS metadata;

        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY,
            chunk_id TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            source_path TEXT NOT NULL,
            vehicle TEXT NOT NULL,
            headings TEXT NOT NULL,
            text TEXT NOT NULL,
            images TEXT NOT NULL,
            links TEXT NOT NULL,
            duplicate_sources TEXT NOT NULL
        );

        CREATE TABLE metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );

        CREATE INDEX idx_chunks_source_path ON chunks(source_path);
        CREATE INDEX idx_chunks_title ON chunks(title);
        """
    )

    if fts5_enabled:
        conn.execute(
            """
            CREATE VIRTUAL TABLE chunks_fts USING fts5(
                chunk_id UNINDEXED,
                title,
                headings,
                text,
                source_path,
                vehicle
            )
            """
        )


def build_index(corpus_dir: Path, db_path: Path) -> dict:
    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)
    try:
        fts5_enabled = has_fts5(conn)
        create_schema(conn, fts5_enabled)

        chunks_inserted = 0
        part_files = len(list(corpus_dir.glob("*.jsonl"))) if corpus_dir.exists() else 0

        with conn:
            for record in load_records(corpus_dir):
                headings = record.get("headings", [])
                images = record.get("images", [])
                links = record.get("links", [])
                duplicate_sources = record.get("duplicate_sources", [])

                cursor = conn.execute(
                    """
                    INSERT INTO chunks (
                        chunk_id,
                        title,
                        source_path,
                        vehicle,
                        headings,
                        text,
                        images,
                        links,
                        duplicate_sources
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        str(record.get("chunk_id", "")),
                        str(record.get("title", "")),
                        str(record.get("source_path", "")),
                        str(record.get("vehicle", "")),
                        json_value(headings),
                        str(record.get("text", "")),
                        json_value(images),
                        json_value(links),
                        json_value(duplicate_sources),
                    ),
                )

                if fts5_enabled:
                    conn.execute(
                        """
                        INSERT INTO chunks_fts (
                            rowid,
                            chunk_id,
                            title,
                            headings,
                            text,
                            source_path,
                            vehicle
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            cursor.lastrowid,
                            str(record.get("chunk_id", "")),
                            str(record.get("title", "")),
                            text_value(headings),
                            str(record.get("text", "")),
                            str(record.get("source_path", "")),
                            str(record.get("vehicle", "")),
                        ),
                    )

                chunks_inserted += 1

            metadata = {
                "corpus_dir": rel(corpus_dir),
                "chunks_indexed": str(chunks_inserted),
                "fts5_enabled": str(fts5_enabled).lower(),
            }
            conn.executemany(
                "INSERT INTO metadata (key, value) VALUES (?, ?)",
                metadata.items(),
            )

        return {
            "db_path": db_path,
            "corpus_dir": corpus_dir,
            "part_files": part_files,
            "chunks_indexed": chunks_inserted,
            "fts5_enabled": fts5_enabled,
        }
    finally:
        conn.close()


def open_index(db_path: Path) -> sqlite3.Connection:
    if not db_path.exists():
        raise FileNotFoundError(f"SQLite index not found: {db_path}")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def index_uses_fts5(conn: sqlite3.Connection) -> bool:
    row = conn.execute("SELECT value FROM metadata WHERE key = 'fts5_enabled'").fetchone()
    return bool(row and row["value"] == "true")


def fts_query(query: str, operator: str = "AND") -> str:
    terms = tokenize(query)
    if not terms:
        raise ValueError("Search query must include at least one alphanumeric term.")
    return f" {operator} ".join(f'"{term}"' for term in terms)


def row_to_record(row: sqlite3.Row) -> dict:
    record = dict(row)
    record["headings"] = decode_json_field(record.get("headings", "[]"))
    record["images"] = decode_json_field(record.get("images", "[]"))
    record["links"] = decode_json_field(record.get("links", "[]"))
    record["duplicate_sources"] = decode_json_field(record.get("duplicate_sources", "[]"))
    return record


def keyword_score(record: dict, query: str, terms: list[str]) -> int:
    weighted_fields = (
        ("title", 12),
        ("headings", 10),
        ("source_path", 6),
        ("vehicle", 4),
        ("text", 1),
    )
    query_folded = query.casefold()
    query_has_video = "video" in terms
    title = text_value(record.get("title")).casefold()
    text = text_value(record.get("text")).casefold()
    title_tokens = tokenize(title)
    unique_terms = set(terms)
    matched_terms = set()
    score = 0

    if query_folded and query_folded in title:
        score += 900
    if query_folded and query_folded in text:
        score += 500

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
        value = text_value(record.get(field)).casefold()
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

    if terms and len(matched_terms) == len(unique_terms):
        score += 30

    if is_index_page(record):
        score -= 2700

    if is_video_page(record) and not query_has_video:
        score -= 2000

    return score


def like_candidates(conn: sqlite3.Connection, terms: list[str], candidate_limit: int):
    rows = conn.execute(
        """
        SELECT *
        FROM chunks
        """
    ).fetchall()

    candidates = []
    for row in rows:
        record = row_to_record(row)
        haystack = " ".join(
            [
                text_value(record.get("title")),
                text_value(record.get("headings")),
                text_value(record.get("text")),
                text_value(record.get("source_path")),
                text_value(record.get("vehicle")),
            ]
        ).casefold()
        if all(term in haystack for term in terms):
            candidates.append(record)
            if len(candidates) >= candidate_limit:
                break
    return candidates


def fts_candidates(conn: sqlite3.Connection, query: str, candidate_limit: int):
    rows = []
    for operator in ("AND", "OR"):
        rows = conn.execute(
            """
            SELECT
                c.*,
                bm25(chunks_fts, 12.0, 8.0, 1.0, 4.0, 3.0) AS fts_rank
            FROM chunks_fts
            JOIN chunks AS c ON c.id = chunks_fts.rowid
            WHERE chunks_fts MATCH ?
            ORDER BY fts_rank
            LIMIT ?
            """,
            (fts_query(query, operator), candidate_limit),
        ).fetchall()
        if rows:
            break

    return [row_to_record(row) | {"fts_rank": row["fts_rank"]} for row in rows]


def normalize_source_path(value: str) -> str:
    return value.replace("/", "\\").casefold().strip()


def normalize_title(value: str) -> str:
    return re.sub(r"\s+", " ", value).casefold().strip()


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


def search_index(conn: sqlite3.Connection, query: str, limit: int) -> list[dict]:
    terms = tokenize(query)
    if not terms:
        raise ValueError("Search query must include at least one alphanumeric term.")

    candidate_limit = max(250, limit * 30)
    if index_uses_fts5(conn):
        candidates = fts_candidates(conn, query, candidate_limit)
    else:
        candidates = like_candidates(conn, terms, candidate_limit)

    results = []
    for record in candidates:
        score = keyword_score(record, query, terms)
        if score > 0:
            results.append({"score": score, "record": record})

    results.sort(
        key=lambda item: (
            -item["score"],
            str(item["record"].get("title", "")),
            str(item["record"].get("source_path", "")),
            str(item["record"].get("chunk_id", "")),
        )
    )
    return dedupe_results(results)[:limit]


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


def print_build_summary(stats: dict) -> None:
    print("SQLite GPT corpus index built")
    print(f"Database: {rel(stats['db_path'])}")
    print(f"Corpus: {rel(stats['corpus_dir'])}")
    print(f"JSONL part files scanned: {stats['part_files']}")
    print(f"Chunks indexed: {stats['chunks_indexed']}")
    print(f"FTS5 enabled: {str(stats['fts5_enabled']).lower()}")


def run_search(db_path: Path, query: str, limit: int) -> None:
    conn = open_index(db_path)
    try:
        results = search_index(conn, query, max(1, limit))
        terms = tokenize(query)

        print(f"Query: {query}")
        print(f"Database: {rel(db_path)}")
        print(f"FTS5 enabled: {str(index_uses_fts5(conn)).lower()}")
        print(f"Results: {len(results)}")
        print()

        if not results:
            print("No matches found.")
            return

        for rank, result in enumerate(results, start=1):
            print_result(rank, result, terms)
    finally:
        conn.close()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build and search a SQLite index for the cleaned GPT corpus."
    )
    parser.add_argument(
        "--corpus-dir",
        default=str(DEFAULT_CORPUS_DIR),
        help="Directory containing clean JSONL part files",
    )
    parser.add_argument(
        "--db",
        default=str(DEFAULT_DB_PATH),
        help="SQLite database path to create or search",
    )
    parser.add_argument("--search", help="Search query to run against the SQLite index")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="Number of results to show")
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Rebuild the SQLite index before running --search",
    )
    args = parser.parse_args()

    corpus_dir = resolve_repo_path(args.corpus_dir)
    db_path = resolve_repo_path(args.db)

    if args.search:
        if args.rebuild or not db_path.exists():
            print_build_summary(build_index(corpus_dir, db_path))
            print()
        run_search(db_path, args.search, args.limit)
        return 0

    print_build_summary(build_index(corpus_dir, db_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
