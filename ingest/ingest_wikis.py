#!/usr/bin/env python3
"""
Ingest Framework OPS Wiki markdown files into Supabase pgvector RAG.
Reads all .md files from the Wiki folder, chunks, embeds via Voyage AI,
and upserts into the documents table with source_type='wiki'.
"""

import os, ssl, json, time, re, uuid
import urllib.request, urllib.error
from pathlib import Path

SUPABASE_URL   = os.getenv("SUPABASE_URL",   "https://cnvvvxltuebymowemwpk.supabase.co")
SUPABASE_KEY   = os.getenv("SUPABASE_KEY",   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNudnZ2eGx0dWVieW1vd2Vtd3BrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3ODM2ODY2NCwiZXhwIjoyMDkzOTQ0NjY0fQ.CUtP8KhxDN2PGVcxBxU2xRlqBsGafmhhRvyqw6mPSac")
VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY", "pa-IFdqEAaZN5f1qqwf7PIOwYJQILE1hsYv1Gpw2E89tIe")
WIKI_DIR       = Path(__file__).parent.parent / "Wiki"
CHUNK_SIZE     = 500
CHUNK_OVERLAP  = 50
SOURCE_TYPE    = "wiki"

try:
    import certifi
    ssl_ctx = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    ssl_ctx = ssl.create_default_context()

def http_post(url, payload, headers):
    data = json.dumps(payload).encode()
    req  = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, context=ssl_ctx, timeout=30) as r:
        return r.status, json.loads(r.read()) if r.read() else {}

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunks.append(" ".join(words[i:i+chunk_size]))
        i += chunk_size - overlap
    return chunks

def embed(texts):
    _, resp = http_post(
        "https://api.voyageai.com/v1/embeddings",
        {"model": "voyage-code-2", "input": texts, "input_type": "document"},
        {"Authorization": f"Bearer {VOYAGE_API_KEY}", "Content-Type": "application/json"},
    )
    return [item["embedding"] for item in resp["data"]]

def upsert_docs(rows):
    status, _ = http_post(
        f"{SUPABASE_URL}/rest/v1/documents",
        rows,
        {
            "apikey":        SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type":  "application/json",
            "Prefer":        "resolution=ignore-duplicates,return=minimal",
        },
    )
    return status

def parse_frontmatter(text):
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                meta[k.strip()] = v.strip().strip('"')
    return meta

def main():
    wiki_files = sorted(WIKI_DIR.glob("*.md"))
    print(f"Found {len(wiki_files)} wiki files\n")
    total = 0

    for md_file in wiki_files:
        text   = md_file.read_text(encoding="utf-8")
        meta   = parse_frontmatter(text)
        title  = meta.get("title", md_file.stem)
        repo   = f"framework-ops/wiki/{md_file.stem}"
        chunks = chunk_text(text)
        print(f"  {md_file.name} → {len(chunks)} chunks")

        rows = []
        for b in range(0, len(chunks), 8):
            batch = chunks[b:b+8]
            embs  = embed(batch)
            for i, (chunk, emb) in enumerate(zip(batch, embs)):
                ci = b + i
                rows.append({
                    "id":          str(uuid.uuid5(uuid.NAMESPACE_URL, f"{repo}::{ci}")),
                    "content":     chunk,
                    "embedding":   emb,
                    "source_type": SOURCE_TYPE,
                    "repo":        repo,
                    "metadata":    {
                        "title": title, "file": md_file.name,
                        "chunk_index": ci, "type": "wiki",
                        "source": "manual", "date": meta.get("date", "2026-05-27"),
                    },
                })
            time.sleep(0.4)

        status = upsert_docs(rows)
        total += len(rows)
        print(f"    HTTP {status} — {len(rows)} chunks upserted")

    print(f"\nDone. Total: {total} chunks")

if __name__ == "__main__":
    main()
