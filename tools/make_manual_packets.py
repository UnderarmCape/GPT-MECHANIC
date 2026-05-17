import argparse
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = ROOT / "build_clean" / "chunks_jsonl_parts"
DEFAULT_OUTPUT_DIR = ROOT / "build_clean" / "packets"
DEFAULT_MAX_CHARS = 750_000


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


def jsonl_part_paths() -> list[Path]:
    if not CORPUS_DIR.exists():
        raise FileNotFoundError(f"Clean JSONL parts directory not found: {CORPUS_DIR}")
    part_paths = sorted(CORPUS_DIR.glob("*.jsonl"))
    if not part_paths:
        raise FileNotFoundError(f"No JSONL part files found in: {CORPUS_DIR}")
    return part_paths


def load_chunks():
    for part_path in jsonl_part_paths():
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


def md_value_list(values) -> str:
    if not values:
        return "none"
    if not isinstance(values, list):
        values = [values]
    return ", ".join(f"`{value}`" for value in values)


def render_chunk(record: dict, chunk_number: int) -> str:
    title = str(record.get("title", ""))
    source_path = str(record.get("source_path", ""))
    chunk_id = str(record.get("chunk_id", ""))
    text = str(record.get("text", ""))

    lines = [
        f"## Chunk {chunk_number}: {title}",
        "",
        f"- Title: {title}",
        f"- Source path: `{source_path}`",
        f"- Chunk ID: `{chunk_id}`",
        f"- Images: {md_value_list(record.get('images'))}",
        f"- Duplicate sources: {md_value_list(record.get('duplicate_sources'))}",
        "",
        "### Full Text",
        "",
        "````text",
        text,
        "````",
        "",
    ]
    return "\n".join(lines)


def suggested_prompt() -> str:
    return (
        "You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. "
        "Use only the manual excerpts in this packet as evidence. When answering, cite "
        "the relevant source_path and chunk_id. If this packet does not contain enough "
        "information, say what is missing and ask for another packet or targeted retrieval."
    )


def packet_sources(sections: list[dict]) -> list[str]:
    sources = []
    seen = set()
    for section in sections:
        source_path = section["source_path"]
        if source_path and source_path not in seen:
            sources.append(source_path)
            seen.add(source_path)
    return sources


def render_packet(packet_number: int, sections: list[dict], max_chars: int) -> str:
    sources = packet_sources(sections)
    first_chunk = sections[0]["chunk_number"] if sections else 0
    last_chunk = sections[-1]["chunk_number"] if sections else 0

    lines = [
        f"# Deep Research Manual Packet {packet_number:04d}",
        "",
        "## Suggested Deep Research Prompt",
        "",
        f"> {suggested_prompt()}",
        "",
        "## Packet Metadata",
        "",
        "- Vehicle: 2016 Honda Civic LX 4D Sedan CVT",
        f"- Packet number: {packet_number:04d}",
        f"- Chunk count: {len(sections)}",
        f"- Chunk range: {first_chunk}-{last_chunk}",
        f"- Source count: {len(sources)}",
        f"- Target maximum characters: {max_chars}",
        "",
        "## Manual Chunks",
        "",
    ]

    lines.extend(section["markdown"] for section in sections)
    lines.extend(["## Sources Used", ""])
    lines.extend(f"- `{source}`" for source in sources)
    lines.append("")
    return "\n".join(lines)


def render_master_index(packet_infos: list[dict], output_dir: Path, total_chunks: int, max_chars: int) -> str:
    generated = datetime.now().isoformat(timespec="seconds")
    full_manual_dir = output_dir / "full_manual"

    lines = [
        "# GPT Manual Packet Index",
        "",
        f"Generated: {generated}",
        "Vehicle: 2016 Honda Civic LX 4D Sedan CVT",
        f"Corpus: `{rel(CORPUS_DIR)}`",
        f"Packet directory: `{rel(full_manual_dir)}`",
        f"Maximum characters per packet: {max_chars}",
        f"Total chunks processed: {total_chunks}",
        f"Packets created: {len(packet_infos)}",
        "",
        "## Suggested Deep Research Workflow",
        "",
        "Use one or more packets as source documents. Ask Deep Research to cite `source_path` and `chunk_id` from the packet metadata, and request targeted retrieval when a packet does not contain enough evidence.",
        "",
        "## Packet Files",
        "",
        "| Packet | File | Chunks | Sources | Characters | First source | Last source |",
        "| ---: | --- | ---: | ---: | ---: | --- | --- |",
    ]

    for info in packet_infos:
        lines.append(
            f"| {info['packet_number']:04d} | `{rel(info['path'])}` | "
            f"{info['chunk_count']} | {info['source_count']} | {info['char_count']} | "
            f"`{info['first_source']}` | `{info['last_source']}` |"
        )

    lines.append("")
    return "\n".join(lines)


def write_packet(packet_number: int, sections: list[dict], full_manual_dir: Path, max_chars: int) -> dict:
    full_manual_dir.mkdir(parents=True, exist_ok=True)
    packet_path = full_manual_dir / f"packet_{packet_number:04d}.md"
    content = render_packet(packet_number, sections, max_chars)
    packet_path.write_text(content, encoding="utf-8")

    sources = packet_sources(sections)
    return {
        "packet_number": packet_number,
        "path": packet_path,
        "chunk_count": len(sections),
        "source_count": len(sources),
        "char_count": len(content),
        "first_source": sources[0] if sources else "",
        "last_source": sources[-1] if sources else "",
    }


def make_packets(output_dir: Path, max_chars: int) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    full_manual_dir = output_dir / "full_manual"
    full_manual_dir.mkdir(parents=True, exist_ok=True)

    packet_infos = []
    current_sections = []
    packet_number = 1
    total_chunks = 0
    oversize_chunks = []

    for record in load_chunks():
        total_chunks += 1
        section = {
            "chunk_number": total_chunks,
            "source_path": str(record.get("source_path", "")),
            "markdown": render_chunk(record, total_chunks),
        }

        if current_sections:
            candidate = render_packet(packet_number, [*current_sections, section], max_chars)
            if len(candidate) > max_chars:
                packet_infos.append(
                    write_packet(packet_number, current_sections, full_manual_dir, max_chars)
                )
                packet_number += 1
                current_sections = []

        current_sections.append(section)

        if len(render_packet(packet_number, current_sections, max_chars)) > max_chars:
            oversize_chunks.append(total_chunks)
            packet_infos.append(write_packet(packet_number, current_sections, full_manual_dir, max_chars))
            packet_number += 1
            current_sections = []

    if current_sections:
        packet_infos.append(write_packet(packet_number, current_sections, full_manual_dir, max_chars))

    master_index_path = output_dir / "master_manual_index.md"
    master_index = render_master_index(packet_infos, output_dir, total_chunks, max_chars)
    master_index_path.write_text(master_index, encoding="utf-8")

    largest_packet_size = max((info["char_count"] for info in packet_infos), default=0)
    return {
        "total_chunks": total_chunks,
        "packets_created": len(packet_infos),
        "largest_packet_size": largest_packet_size,
        "output_dir": output_dir,
        "master_index": master_index_path,
        "oversize_chunks": oversize_chunks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export the cleaned GPT corpus into Deep Research-ready Markdown packets."
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=DEFAULT_MAX_CHARS,
        help="Maximum characters per packet",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Packet output directory",
    )
    args = parser.parse_args()

    max_chars = max(1, args.max_chars)
    output_dir = resolve_repo_path(args.output_dir)
    stats = make_packets(output_dir, max_chars)

    print("Manual packet export complete")
    print(f"Total chunks processed: {stats['total_chunks']}")
    print(f"Packets created: {stats['packets_created']}")
    print(f"Largest packet size: {stats['largest_packet_size']}")
    print(f"Output directory: {rel(stats['output_dir'])}")
    print(f"Master index: {rel(stats['master_index'])}")
    if stats["oversize_chunks"]:
        print(
            "Warning: some individual chunks exceeded the packet size limit and were "
            f"written alone: {stats['oversize_chunks']}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
