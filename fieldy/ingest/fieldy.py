#!/usr/bin/env python3
"""
fieldy.py — Ingest Fieldy wearable AI conversations into Supabase pgvector RAG.

Env vars (or set in .env):
    FIELDY_API_KEY     sk-f-...
    SUPABASE_URL       https://xxxx.supabase.co
    SUPABASE_KEY       service_role key
    VOYAGE_API_KEY     pa-...

Usage:
    python fieldy.py                    # last 24 hrs
    python fieldy.py --hours 48
    python fieldy.py --all              # full backfill
    python fieldy.py --dry-run          # no embed, no DB write
"""

import os, sys, time, json, logging, argparse, uuid
from datetime import datetime, timedelta, timezone

import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

FIELDY_API_KEY = os.environ["FIELDY_API_KEY"]
SUPABASE_URL   = os.environ["SUPABASE_URL"]
SUPABASE_KEY   = os.environ["SUPABASE_KEY"]
VOYAGE_API_KEY = os.environ["VOYAGE_API_KEY"]

FIELDY_BASE    = "https://api.fieldy.ai/api/public/v2"
VOYAGE_URL     = "https://api.voyageai.com/v1/embeddings"
VOYAGE_MODEL   = "voyage-code-2"
SUPABASE_TABLE = "documents"
SOURCE_TYPE    = "meeting"

try:
    import certifi
    VERIFY = certifi.where()
except ImportError:
    VERIFY = True

_fsess = requests.Session()
_fsess.headers.update({"Authorization": f"Bearer {FIELDY_API_KEY}"})


# ── Fieldy ───────────────────────────────────────────────────────────────────
def fetch_conversations(start: datetime, end: datetime) -> list[dict]:
    items, cursor, page = [], None, 1
    while True:
        params = {"startTime": start.isoformat(), "endTime": end.isoformat(), "per_page": 50}
        if cursor:
            params["cursor"] = cursor
        log.info(f"Fetching page {page}…")
        for attempt in range(5):
            r = _fsess.get(f"{FIELDY_BASE}/conversations", params=params,
                           verify=VERIFY, timeout=20)
            if r.status_code == 429:
                time.sleep(2 ** (attempt + 1)); continue
            r.raise_for_status(); break
        data   = r.json()
        batch  = data.get("items", [])
        items.extend(batch)
        log.info(f"  {len(batch)} conversations (running total: {len(items)})")
        cursor = data.get("nextCursor")
        if not cursor or not batch:
            break
        page += 1
        time.sleep(0.5)
    return items


# ── Embeddings ───────────────────────────────────────────────────────────────
def embed_batch(texts: list[str]) -> list[list[float]]:
    for attempt in range(5):
        try:
            r = requests.post(
                VOYAGE_URL,
                headers={"Authorization": f"Bearer {VOYAGE_API_KEY}",
                         "Content-Type": "application/json"},
                json={"model": VOYAGE_MODEL, "input": texts, "input_type": "document"},
                verify=VERIFY, timeout=120,
            )
            r.raise_for_status()
            return [item["embedding"] for item in r.json()["data"]]
        except (requests.exceptions.Timeout, requests.exceptions.ReadTimeout) as e:
            wait = 30 * (attempt + 1)
            log.warning(f"Voyage timeout (attempt {attempt+1}/5) — waiting {wait}s: {e}")
            time.sleep(wait)
        except requests.exceptions.HTTPError as e:
            if r.status_code == 429:
                wait = 60 * (attempt + 1)
                log.warning(f"Voyage rate limit — waiting {wait}s")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("Voyage AI failed after 5 attempts")


# ── Supabase ─────────────────────────────────────────────────────────────────
_sbsess = requests.Session()
_sbsess.headers.update({
    "apikey":        SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type":  "application/json",
    "Prefer":        "resolution=ignore-duplicates,return=minimal",
})

def upsert_docs(rows: list[dict]):
    r = _sbsess.post(f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}",
                     json=rows, verify=VERIFY, timeout=30)
    r.raise_for_status()


# ── Document builder ─────────────────────────────────────────────────────────
def conv_to_doc(conv: dict) -> dict | None:
    cid      = conv.get("id", "")
    title    = conv.get("title") or "Untitled"
    body     = conv.get("content") or conv.get("summary") or ""
    kw       = ", ".join(conv.get("keywords") or [])
    loc      = (conv.get("location") or {}).get("address", "")
    speakers = ", ".join(s for s in (conv.get("memorySpeakers") or []) if s != "Unknown")

    parts = [f"# {title}"]
    if body:    parts.append(body)
    if kw:      parts.append(f"Keywords: {kw}")
    if speakers: parts.append(f"Participants: {speakers}")
    if loc:     parts.append(f"Location: {loc}")

    content = "\n\n".join(parts).strip()
    if len(content) < 30:
        return None

    return {
        "id":          str(uuid.uuid5(uuid.NAMESPACE_URL, f"fieldy::conv::{cid}")),
        "content":     content,
        "source_type": SOURCE_TYPE,
        "repo":        "framework-ops/fieldy/conversations",
        "metadata": {
            "fieldy_id":  cid,
            "title":      title,
            "type":       "conversation",
            "source":     "fieldy",
            "start_time": conv.get("startTime", ""),
            "keywords":   conv.get("keywords") or [],
            "speakers":   speakers,
            "location":   loc,
        },
    }


# ── Main ─────────────────────────────────────────────────────────────────────
def run(start: datetime, end: datetime, dry_run: bool = False):
    conversations = fetch_conversations(start, end)
    log.info(f"Total fetched: {len(conversations)}")

    docs = [d for c in conversations if (d := conv_to_doc(c)) is not None]
    skipped = len(conversations) - len(docs)
    log.info(f"Docs to ingest: {len(docs)} (skipped {skipped} empty)")

    if not docs:
        return 0, skipped

    if dry_run:
        for doc in docs:
            log.info(f"  [DRY RUN] {doc['metadata']['title'][:70]}")
        return len(docs), skipped

    BATCH = 6  # smaller batch to stay within Voyage rate limits
    ingested = 0
    for i in range(0, len(docs), BATCH):
        batch = docs[i:i+BATCH]
        log.info(f"Embedding batch {i//BATCH+1}/{(len(docs)+BATCH-1)//BATCH}…")
        embs = embed_batch([d["content"] for d in batch])
        for doc, emb in zip(batch, embs):
            doc["embedding"] = emb
        upsert_docs(batch)
        ingested += len(batch)
        log.info(f"  Upserted {len(batch)} (total: {ingested})")
        if i + BATCH < len(docs):
            time.sleep(3)

    log.info(f"Done. Ingested: {ingested}, Skipped: {skipped}")
    return ingested, skipped


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hours",   type=int, default=24)
    parser.add_argument("--start",   type=str, default=None)
    parser.add_argument("--end",     type=str, default=None)
    parser.add_argument("--all",     action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    if args.all:
        start_dt, end_dt = datetime(2020, 1, 1, tzinfo=timezone.utc), now
    elif args.start:
        start_dt = datetime.fromisoformat(args.start).replace(tzinfo=timezone.utc)
        end_dt   = datetime.fromisoformat(args.end).replace(tzinfo=timezone.utc) if args.end else now
    else:
        start_dt = now - timedelta(hours=args.hours)
        end_dt   = now

    log.info(f"Range: {start_dt.date()} → {end_dt.date()}")
    run(start_dt, end_dt, dry_run=args.dry_run)
