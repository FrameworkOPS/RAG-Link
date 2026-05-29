#!/usr/bin/env python3
"""
ingest_wikis.py — Framework OPS Wiki Ingest Pipeline

Reads .md files from Wiki/, chunks them semantically (~500 tokens each),
embeds with Voyage AI (voyage-code-2, 1536 dims), and upserts into Supabase
documents table as source_type='wiki'.

Deduplication: checks existing rows by (repo, metadata.filename, metadata.chunk_index)
before inserting. Safe to re-run — will skip already-ingested chunks.

Usage:
    python3 ingest_wikis.py
    python3 ingest_wikis.py --dry-run      # embed only, don't insert
    python3 ingest_wikis.py --force        # re-insert even if chunk exists
    python3 ingest_wikis.py --file company-profile.md  # single file
"""

import ssl
import certifi
import urllib.request
import json
import os
import re
import time
import argparse
from pathlib import Path
from datetime import datetime

# ── Config ──────────────────────────────────────────────────────────────────

SUPABASE_URL = "https://cnvvvxltuebymowemwpk.supabase.co"
SERVICE_KEY  = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNudnZ2eGx0dWVieW1vd2Vtd3BrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3ODM2ODY2NCwiZXhwIjoyMDkzOTQ0NjY0fQ"
    ".CUtP8KhxDN2PGVcxBxU2xRlqBsGafmhhRvyqw6mPSac"
)
VOYAGE_KEY   = "pa-IFdqEAaZN5f1qqwf7PIOwYJQILE1hsYv1Gpw2E89tIe"
VOYAGE_MODEL = "voyage-code-2"
EMBED_DIMS   = 1536

WIKI_DIR     = Path(__file__).parent.parent / "Wiki"
REPO         = "framework-ops/wiki"
SOURCE_TYPE  = "wiki"

# ~500 tokens ≈ ~375 words ≈ ~2000 chars (conservative estimate for mixed markdown)
CHUNK_TARGET_CHARS = 1800
CHUNK_OVERLAP_CHARS = 200

SSL_CTX = ssl.create_default_context(cafile=certifi.where())

# ── HTTP helpers ─────────────────────────────────────────────────────────────

def _supabase_headers():
    return {
        "apikey": SERVICE_KEY,
        "Authorization": f"Bearer {SERVICE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal",
    }

def supabase_get(path: str) -> list:
    url = SUPABASE_URL + path
    req = urllib.request.Request(url, headers=_supabase_headers())
    with urllib.request.urlopen(req, context=SSL_CTX) as r:
        return json.loads(r.read())

def supabase_post(path: str, data: dict) -> dict:
    url = SUPABASE_URL + path
    body = json.dumps(data).encode()
    req = urllib.request.Request(url, data=body, headers=_supabase_headers(), method="POST")
    with urllib.request.urlopen(req, context=SSL_CTX) as r:
        resp = r.read()
        return json.loads(resp) if resp.strip() else {}

def voyage_embed(texts: list[str]) -> list[list[float]]:
    """Embed a batch of texts. Returns list of 1536-dim vectors."""
    url = "https://api.voyageai.com/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {VOYAGE_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": VOYAGE_MODEL,
        "input": texts,
        "input_type": "document",
    }
    body = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req, context=SSL_CTX) as r:
        result = json.loads(r.read())
    return [item["embedding"] for item in result["data"]]

# ── Chunking ─────────────────────────────────────────────────────────────────

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Strip YAML frontmatter and return (meta_dict, body_text)."""
    meta = {}
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            fm_block = content[3:end].strip()
            body = content[end + 4:].strip()
            for line in fm_block.splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    k = k.strip()
                    v = v.strip()
                    # parse simple lists like [tag1, tag2]
                    if v.startswith("[") and v.endswith("]"):
                        v = [t.strip() for t in v[1:-1].split(",")]
                    meta[k] = v
            return meta, body
    return meta, content

def split_by_headings(text: str) -> list[str]:
    """Split markdown into sections at H2/H3 headings."""
    pattern = re.compile(r"(?=^#{2,3} )", re.MULTILINE)
    sections = pattern.split(text)
    return [s.strip() for s in sections if s.strip()]

def chunk_section(section: str, target: int = CHUNK_TARGET_CHARS, overlap: int = CHUNK_OVERLAP_CHARS) -> list[str]:
    """If a section is larger than target, split it into overlapping paragraphs."""
    if len(section) <= target:
        return [section]

    chunks = []
    paragraphs = re.split(r"\n{2,}", section)
    current = ""

    for para in paragraphs:
        if len(current) + len(para) + 2 <= target:
            current = (current + "\n\n" + para).strip() if current else para
        else:
            if current:
                chunks.append(current)
            # start new chunk with overlap from end of previous
            if current and overlap > 0:
                overlap_text = current[-overlap:].strip()
                current = overlap_text + "\n\n" + para
            else:
                current = para

    if current:
        chunks.append(current)

    return chunks if chunks else [section]

def chunk_document(filepath: Path) -> list[dict]:
    """
    Read a wiki .md file and return a list of chunk dicts:
    {content, chunk_index, total_chunks, title, tags, filename}
    """
    raw = filepath.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(raw)

    title = fm.get("title", filepath.stem)
    tags  = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]

    sections = split_by_headings(body)
    if not sections:
        sections = [body]

    raw_chunks = []
    for section in sections:
        raw_chunks.extend(chunk_section(section))

    # Prepend title to first chunk for context anchoring
    if raw_chunks:
        raw_chunks[0] = f"# {title}\n\n{raw_chunks[0]}"

    total = len(raw_chunks)
    chunks = []
    for i, text in enumerate(raw_chunks):
        if not text.strip():
            continue
        chunks.append({
            "content": text.strip(),
            "chunk_index": i,
            "total_chunks": total,
            "title": title,
            "tags": tags,
            "filename": filepath.name,
        })

    return chunks

# ── Deduplication ─────────────────────────────────────────────────────────────

def get_existing_keys() -> set[tuple]:
    """
    Return a set of (filename, chunk_index) tuples already in Supabase
    for source_type='wiki' and repo='framework-ops/wiki'.
    """
    existing = set()
    offset = 0
    limit = 1000
    while True:
        path = (
            f"/rest/v1/documents"
            f"?select=metadata"
            f"&source_type=eq.wiki"
            f"&repo=eq.{REPO}"
            f"&limit={limit}&offset={offset}"
        )
        rows = supabase_get(path)
        if not rows:
            break
        for row in rows:
            meta = row.get("metadata") or {}
            fn = meta.get("filename", "")
            ci = meta.get("chunk_index", -1)
            if fn:
                existing.add((fn, ci))
        if len(rows) < limit:
            break
        offset += limit
    return existing

# ── Ingest ────────────────────────────────────────────────────────────────────

def ingest_file(filepath: Path, existing_keys: set, dry_run: bool = False, force: bool = False) -> dict:
    chunks = chunk_document(filepath)
    if not chunks:
        print(f"  ⚠  {filepath.name}: no chunks generated, skipping")
        return {"file": filepath.name, "total": 0, "inserted": 0, "skipped": 0}

    # Filter to chunks not already ingested
    to_insert = []
    skipped = 0
    for ch in chunks:
        key = (ch["filename"], ch["chunk_index"])
        if not force and key in existing_keys:
            skipped += 1
        else:
            to_insert.append(ch)

    if not to_insert:
        print(f"  ✓  {filepath.name}: all {len(chunks)} chunks already ingested, skipping")
        return {"file": filepath.name, "total": len(chunks), "inserted": 0, "skipped": len(chunks)}

    print(f"  →  {filepath.name}: {len(to_insert)} chunks to embed ({skipped} already exist)")

    if dry_run:
        print(f"     [DRY RUN] would embed {len(to_insert)} chunks")
        return {"file": filepath.name, "total": len(chunks), "inserted": 0, "skipped": skipped, "dry_run": len(to_insert)}

    # Embed in batches of 8 (Voyage rate limits)
    BATCH = 8
    all_embeddings = []
    for i in range(0, len(to_insert), BATCH):
        batch_texts = [ch["content"] for ch in to_insert[i:i + BATCH]]
        try:
            embeddings = voyage_embed(batch_texts)
            all_embeddings.extend(embeddings)
            print(f"     Embedded batch {i // BATCH + 1}/{(len(to_insert) + BATCH - 1) // BATCH}")
        except Exception as e:
            print(f"     ✗ Embedding error on batch {i}: {e}")
            raise
        if i + BATCH < len(to_insert):
            time.sleep(0.3)  # gentle rate limiting

    # Insert into Supabase
    inserted = 0
    for ch, embedding in zip(to_insert, all_embeddings):
        doc = {
            "content": ch["content"],
            "embedding": embedding,
            "source_type": SOURCE_TYPE,
            "repo": REPO,
            "metadata": {
                "filename": ch["filename"],
                "title": ch["title"],
                "tags": ch["tags"],
                "chunk_index": ch["chunk_index"],
                "total_chunks": ch["total_chunks"],
                "ingested_at": datetime.utcnow().isoformat() + "Z",
            },
        }
        try:
            supabase_post("/rest/v1/documents", doc)
            inserted += 1
        except Exception as e:
            print(f"     ✗ Insert error on chunk {ch['chunk_index']}: {e}")

    print(f"     ✓ Inserted {inserted}/{len(to_insert)} chunks")
    return {"file": filepath.name, "total": len(chunks), "inserted": inserted, "skipped": skipped}

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Ingest Framework OPS wiki files into Supabase RAG")
    parser.add_argument("--dry-run", action="store_true", help="Embed but don't insert")
    parser.add_argument("--force", action="store_true", help="Re-insert even if chunk exists")
    parser.add_argument("--file", type=str, help="Ingest only this filename (e.g. company-profile.md)")
    args = parser.parse_args()

    print(f"\nFramework OPS Wiki Ingest")
    print(f"{'=' * 50}")
    print(f"Wiki dir:    {WIKI_DIR}")
    print(f"Repo:        {REPO}")
    print(f"Dry run:     {args.dry_run}")
    print(f"Force:       {args.force}")
    print()

    if not WIKI_DIR.exists():
        print(f"✗ Wiki directory not found: {WIKI_DIR}")
        return

    # Find wiki files
    if args.file:
        files = [WIKI_DIR / args.file]
        if not files[0].exists():
            print(f"✗ File not found: {files[0]}")
            return
    else:
        files = sorted(WIKI_DIR.glob("*.md"))

    if not files:
        print("✗ No .md files found in Wiki/")
        return

    print(f"Found {len(files)} wiki file(s)")

    # Load existing keys for dedup
    if not args.force:
        print("Loading existing Supabase records for dedup check...")
        existing_keys = get_existing_keys()
        print(f"  Found {len(existing_keys)} existing wiki chunks in Supabase")
    else:
        existing_keys = set()

    print()

    # Process each file
    results = []
    for f in files:
        print(f"Processing: {f.name}")
        result = ingest_file(f, existing_keys, dry_run=args.dry_run, force=args.force)
        results.append(result)
        print()

    # Summary
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    total_chunks   = sum(r["total"] for r in results)
    total_inserted = sum(r.get("inserted", 0) for r in results)
    total_skipped  = sum(r.get("skipped", 0) for r in results)
    total_dry      = sum(r.get("dry_run", 0) for r in results)

    for r in results:
        status = "DRY" if r.get("dry_run") else ("✓" if r["inserted"] > 0 else "–")
        print(f"  {status}  {r['file']}: {r['total']} chunks, {r.get('inserted',0)} inserted, {r.get('skipped',0)} skipped")

    print()
    print(f"Total chunks:   {total_chunks}")
    print(f"Inserted:       {total_inserted}")
    print(f"Skipped:        {total_skipped}")
    if args.dry_run:
        print(f"Would insert:   {total_dry}")
    print()
    if not args.dry_run:
        print("✓ Ingest complete")
    else:
        print("(Dry run — no data written to Supabase)")

if __name__ == "__main__":
    main()
