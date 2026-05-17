# GPT Corpus Usage

This repository contains two GPT-readable corpus builds for the 2016 Honda Civic LX 4D Sedan CVT static service manual.

## Corpus Directories

- `build_clean/` is the primary GPT corpus. It is deduplicated, filters most very short chunks, and stores duplicate source paths on the kept chunk in `duplicate_sources`.
- `build/` is the raw first-pass corpus. It preserves the original generated chunks before cleanup and deduplication.

## Build The Clean Corpus

```powershell
python tools/build_gpt_chunks.py --dedupe-exact --min-chars 100 --output-dir build_clean
```

This writes:

- `build_clean/chunks.jsonl`
- `build_clean/chunks_jsonl_parts/*.jsonl`
- `build_clean/chunks_manifest.json`

## Validate A Corpus

Validate the clean corpus:

```powershell
python tools/validate_gpt_chunks.py --build-dir build_clean
```

Validate the raw first-pass corpus:

```powershell
python tools/validate_gpt_chunks.py --build-dir build
```

By default, validation writes `<build-dir>/validation_report.md`. To choose a report path:

```powershell
python tools/validate_gpt_chunks.py --build-dir build_clean --report build_clean/custom_report.md
```

## Search The Clean Corpus

Search uses `build_clean/chunks_jsonl_parts/*.jsonl`.

```powershell
python tools/search_gpt_corpus.py "CVT fluid replacement"
```

Limit result count:

```powershell
python tools/search_gpt_corpus.py "brake fluid" --limit 5
```

Index/navigation pages and video pages are downranked by default. To include index pages and avoid the video-page penalty:

```powershell
python tools/search_gpt_corpus.py "CVT fluid" --include-index --include-video
```

Results are deduplicated by source path and exact title by default. To show repeated chunks:

```powershell
python tools/search_gpt_corpus.py "CVT fluid" --no-dedupe-results
```

Each result includes rank, score, title, source path, chunk ID, image paths when present, and a text preview near the matched terms.

## Build A SQLite Search Index

Build a local SQLite database from the clean corpus:

```powershell
python tools/build_search_index.py
```

This writes:

- `build_clean/gpt_corpus.sqlite`

The script uses SQLite FTS5 when the local Python SQLite build supports it. Search the SQLite index:

```powershell
python tools/build_search_index.py --search "CVT fluid"
```

Rebuild before searching:

```powershell
python tools/build_search_index.py --rebuild --search "HCF-2"
```

## Retrieve Paste-Ready Context

Use the SQLite index to retrieve full chunk text as clean Markdown for ChatGPT:

```powershell
python tools/retrieve_context.py "How do I replace the CVT fluid?"
```

Return a different number of chunks:

```powershell
python tools/retrieve_context.py "brake fluid replacement" --limit 3
```

Retrieve chunks directly from a known manual source page:

```powershell
python tools/retrieve_context.py --source pages\12611.html
```

Save the Markdown context to a file:

```powershell
python tools/retrieve_context.py "HCF-2 level check" --output build_clean/retrieved_context.md
```
