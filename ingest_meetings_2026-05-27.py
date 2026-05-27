#!/usr/bin/env python3
"""
One-shot ingest for 2026-05-27 Fathom meetings:
  - Impromptu Ops Review (recording_id: 149923467)
  - Weekly Leadership Meeting - Skyright (recording_id: 149909615)

Run from Terminal:
  cd ~/Documents/Framework-OPS
  pip3 install supabase httpx python-dotenv "httpx[socks]" --break-system-packages -q
  python3 ingest_meetings_2026-05-27.py
"""

import httpx, time, os, json
from datetime import datetime, timezone
from supabase import create_client
from dotenv import load_dotenv

load_dotenv("fieldy/.env")  # has SUPABASE_URL, SUPABASE_KEY, VOYAGE_API_KEY

SUPABASE_URL  = os.environ["SUPABASE_URL"]
SUPABASE_KEY  = os.environ["SUPABASE_KEY"]
VOYAGE_API_KEY = os.environ["VOYAGE_API_KEY"]
FATHOM_API_KEY = "bX-C0doej7Tg0FBXdgVVbw.MoZes9Xdz95UqbsMS_VMeeikkk5XcTWE5-KiAm0VVdo"

VOYAGE_URL   = "https://api.voyageai.com/v1/embeddings"
VOYAGE_MODEL = "voyage-code-2"
FATHOM_BASE  = "https://api.fathom.ai/external/v1"

supa = create_client(SUPABASE_URL, SUPABASE_KEY)

def embed(text: str) -> list[float]:
    resp = httpx.post(
        VOYAGE_URL,
        headers={"Authorization": f"Bearer {VOYAGE_API_KEY}", "Content-Type": "application/json"},
        json={"model": VOYAGE_MODEL, "input": [text], "input_type": "document"},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["data"][0]["embedding"]

def fathom_get(path: str, params: dict = None) -> dict:
    r = httpx.get(
        f"{FATHOM_BASE}{path}",
        headers={"X-Api-Key": FATHOM_API_KEY},
        params=params,
        timeout=60,
    )
    r.raise_for_status()
    return r.json()

def already_ingested(recording_id: int) -> bool:
    res = supa.table("documents").select("id").eq(
        "metadata->>recording_id", str(recording_id)
    ).limit(1).execute()
    return len(res.data) > 0

def chunk_text(text: str, max_chars: int = 1400) -> list[str]:
    """Split on double-newlines, then merge short chunks."""
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, buf = [], ""
    for p in paras:
        if len(buf) + len(p) + 2 > max_chars and buf:
            chunks.append(buf)
            buf = p
        else:
            buf = (buf + "\n\n" + p).strip() if buf else p
    if buf:
        chunks.append(buf)
    return chunks

def ingest_meeting(recording_id: int, label: str):
    print(f"\n── {label} (recording_id={recording_id}) ──")

    if already_ingested(recording_id):
        print("  Already ingested — skipping.")
        return

    # Fetch from Fathom
    data = fathom_get(f"/meetings/{recording_id}", {
        "include_transcript": "true",
        "include_summary": "true",
        "include_action_items": "true",
    })

    title     = data.get("title", "Untitled")
    url       = data.get("url", "")
    summary   = data.get("summary", "") or ""
    action_items = data.get("action_items", "") or ""
    transcript   = data.get("transcript", "") or ""
    date_str  = (data.get("created_at") or datetime.now(timezone.utc).isoformat())[:10]

    base_meta = {
        "recording_id": str(recording_id),
        "date": date_str,
        "meeting_type": "fathom",
        "source": "fathom",
    }

    docs = []

    # Chunk 1: overview
    overview = f"# {title}\n\nDate: {date_str}\nURL: {url}\n\n## Summary\n\n{summary}"
    docs.append(("overview", overview))

    # Chunk 2: action items
    if action_items:
        docs.append(("action_items", f"# {title} — Action Items\n\n{action_items}"))

    # Transcript chunks
    if transcript:
        for i, chunk in enumerate(chunk_text(transcript)):
            docs.append((f"transcript_{i+1}", f"# {title} — Transcript Part {i+1}\n\n{chunk}"))

    total = len(docs)
    base_meta["total_chunks"] = total
    print(f"  Chunks to ingest: {total}")

    for idx, (chunk_type, content) in enumerate(docs):
        print(f"  [{idx+1}/{total}] {chunk_type} — embedding...", end=" ", flush=True)
        vec = embed(content)
        meta = {**base_meta, "chunk_type": chunk_type, "chunk_index": idx}
        supa.table("documents").insert({
            "repo": "framework-ops/fathom-meetings",
            "source_type": "meeting",
            "path": f"fathom/{recording_id}/{chunk_type}",
            "title": f"{title} — {chunk_type}",
            "url": url,
            "content": content,
            "metadata": meta,
            "embedding": vec,
        }).execute()
        print("✓")
        if idx < total - 1:
            time.sleep(1.5)  # light rate-limit buffer

    print(f"  ✓ Ingested {total} chunks for '{title}'")


if __name__ == "__main__":
    ingest_meeting(149923467, "Impromptu Ops Review")
    ingest_meeting(149909615, "Weekly Leadership Meeting - Skyright")
    print("\nDone.")
