import argparse
import sqlite3
import sys
from pathlib import Path

from build_search_index import (
    DEFAULT_DB_PATH,
    fts_candidates,
    index_uses_fts5,
    keyword_score,
    like_candidates,
    open_index,
    rel,
    resolve_repo_path,
    row_to_record,
    text_value,
    tokenize,
)


DEFAULT_LIMIT = 5


def markdown_list(values) -> str:
    if not values:
        return "none"
    if not isinstance(values, list):
        values = [values]
    return ", ".join(f"`{value}`" for value in values)


def source_variants(source_path: str) -> list[str]:
    variants = {
        source_path,
        source_path.replace("/", "\\"),
        source_path.replace("\\", "/"),
    }
    return sorted(value for value in variants if value)


def search_chunks(conn: sqlite3.Connection, query: str, limit: int) -> list[dict]:
    terms = tokenize(query)
    if not terms:
        raise ValueError("Search query must include at least one alphanumeric term.")

    candidate_limit = max(250, limit * 40)
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
    return results[:limit]


def retrieve_source(conn: sqlite3.Connection, source_path: str, limit: int) -> list[dict]:
    variants = source_variants(source_path)
    clauses = " OR ".join(["source_path = ? COLLATE NOCASE" for _ in variants])
    rows = conn.execute(
        f"""
        SELECT *
        FROM chunks
        WHERE {clauses}
        ORDER BY id
        LIMIT ?
        """,
        [*variants, limit],
    ).fetchall()

    return [
        {"score": "direct source match", "record": row_to_record(row)}
        for row in rows
    ]


def render_markdown(
    results: list[dict],
    db_path: Path,
    query: str | None = None,
    source_path: str | None = None,
    fts5_enabled: bool = False,
) -> str:
    lines = [
        "# Retrieved Manual Context",
        "",
    ]

    if query:
        lines.append(f"- Query: {query}")
    if source_path:
        lines.append(f"- Source query: `{source_path}`")

    lines.extend(
        [
            f"- Database: `{rel(db_path)}`",
            f"- FTS5 enabled: `{str(fts5_enabled).lower()}`",
            f"- Chunks returned: `{len(results)}`",
            "",
        ]
    )

    if not results:
        lines.extend(["No matching chunks were found.", "", "## Sources Used", "", "None.", ""])
        return "\n".join(lines)

    sources_used = []
    seen_sources = set()

    for rank, result in enumerate(results, start=1):
        record = result["record"]
        source = str(record.get("source_path", ""))
        if source and source not in seen_sources:
            sources_used.append(source)
            seen_sources.add(source)

        lines.extend(
            [
                f"## Result {rank}: {record.get('title', '')}",
                "",
                f"- Rank: {rank}",
                f"- Score: {result['score']}",
                f"- Title: {record.get('title', '')}",
                f"- Source path: `{source}`",
                f"- Chunk ID: `{record.get('chunk_id', '')}`",
                f"- Images: {markdown_list(record.get('images'))}",
                f"- Duplicate sources: {markdown_list(record.get('duplicate_sources'))}",
                "",
                "### Chunk Text",
                "",
                "```text",
                text_value(record.get("text")),
                "```",
                "",
            ]
        )

    lines.extend(["## Sources Used", ""])
    for source in sources_used:
        lines.append(f"- `{source}`")
    lines.append("")

    return "\n".join(lines)


def write_or_print(markdown: str, output_path: Path | None) -> None:
    if output_path is None:
        sys.stdout.buffer.write(markdown.encode("utf-8", errors="replace"))
        sys.stdout.buffer.write(b"\n")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    print(f"Wrote retrieved context: {rel(output_path)}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Retrieve paste-ready Markdown context from the local GPT corpus SQLite index."
    )
    parser.add_argument("query", nargs="?", help="User question or search query")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="Number of chunks to return")
    parser.add_argument("--source", help="Retrieve chunks for a specific source_path")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH), help="SQLite GPT corpus database path")
    parser.add_argument("--output", help="Optional Markdown file to write")
    args = parser.parse_args()

    if not args.query and not args.source:
        parser.error("provide a query or --source")

    db_path = resolve_repo_path(args.db)
    output_path = resolve_repo_path(args.output) if args.output else None
    limit = max(1, args.limit)

    conn = open_index(db_path)
    try:
        if args.source:
            results = retrieve_source(conn, args.source, limit)
        else:
            results = search_chunks(conn, args.query, limit)

        markdown = render_markdown(
            results=results,
            db_path=db_path,
            query=args.query,
            source_path=args.source,
            fts5_enabled=index_uses_fts5(conn),
        )
        write_or_print(markdown, output_path)
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
