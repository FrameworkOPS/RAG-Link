"""
ingest_meeting_2026-05-26-daniel.py
-----------------------------------
One-shot ingest of the Daniel / William meeting (2026-05-26) into the
Framework OPS Supabase pgvector RAG (documents table).

Embedding model : Voyage AI  voyage-code-2  (1536-dim) — matches backend
Source type     : 'meeting'  (requires migration migrate_add_meeting_source_type.sql
                  to be applied first — adds 'meeting' to the source_type CHECK constraint)

Usage
-----
1. Copy .env.example → .env and fill in real creds, OR export env vars:

    export SUPABASE_URL=https://xxxx.supabase.co
    export SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
    export VOYAGE_API_KEY=pa-...

2. pip install supabase httpx python-dotenv
3. python ingest_meeting_2026-05-26-daniel.py
   OR with --dry-run to preview chunks without writing to DB.
"""

import asyncio
import json
import os
import sys
import time
import argparse
from dotenv import load_dotenv

load_dotenv()

try:
    import httpx
    from supabase import create_client
except ImportError as e:
    sys.exit(f"Missing dependency: {e}\nRun: pip install supabase httpx python-dotenv")

# ── Config ──────────────────────────────────────────────────────────────────
SUPABASE_URL  = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY  = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
VOYAGE_KEY    = os.environ.get("VOYAGE_API_KEY", "")
VOYAGE_MODEL  = "voyage-code-2"
VOYAGE_URL    = "https://api.voyageai.com/v1/embeddings"
TABLE         = "documents"
REPO          = "framework-ops/meetings"
SOURCE_TYPE   = "meeting"         # requires migrate_add_meeting_source_type.sql to be applied first
EMBED_BATCH   = 8
RATE_SLEEP    = 25                # seconds between Voyage batches (free tier ~3 req/min)

MEETING_URL   = "https://fathom.video/calls/688071219"
MEETING_DATE  = "2026-05-26"
MEETING_TITLE = "Daniel / William — Client Acquisition & Automation Review"

# ── Meeting content, pre-chunked ────────────────────────────────────────────
# Each chunk is a semantically coherent section of the meeting note.
# Chunked manually at ~1200 chars to stay well under Voyage's token limit.

CHUNKS_RAW = [
    {
        "title": "Meeting Overview & Key Takeaways",
        "content": """\
# Daniel / William — Client Acquisition & Automation Review
Date: 2026-05-26 | Participants: Chance Peare, Daniel Kalinin
Recording: https://fathom.video/calls/688071219

## Summary
Progress and next-steps review for Daniel's Lead Statement engagement. Two revenue-generating systems are now live — a B2B outreach campaign targeting tax firms, and a daily contractor-license scraper feeding the Close CRM. The Claude copywriting pipeline is functional; the next build is integrating Higgsfield for video ad generation. Client acquisition is the stated #1 priority.

## Key Takeaways
- B2B Outreach launching: Personalized GammaDocs + Loom video targeting tax firms (50+ Google reviews). Metric benchmark: 1 client / 200 outreaches. Tracking: UTM → Calendly → ClickUp GammaDoc ID. Non-responders enter cold email sequence via Smart Lead.
- Home Service Lead Gen live: Daily scraper pulling CA/OR/WA contractor licenses → Close CRM → sales rep. Model: $97/mo, LTV projection 25–40 months. Railway hosting 24/7.
- Claude Copywriting Pipeline functional: Brief → Ideation → QA → Scripting → QA → ClickUp task. Next: integrate Higgsfield for video generation.
- Immediate priorities: Client acquisition, video automation pipeline, Upwork profile update for higher-ticket positioning.\
""",
    },
    {
        "title": "Client Acquisition Strategy — B2B Tax Firm Outreach",
        "content": """\
# Client Acquisition Strategy — B2B Tax Firm Outreach
Meeting: Daniel / William, 2026-05-26

## Goal
Drive immediate cash flow through new client acquisition.

## B2B Outreach — Tax Firms
- Target: Established firms with 50+ Google reviews
- Package price: $6k/quarter
- Method: Personalized GammaDocs + Loom video + 10 ad examples per outreach
- Tracking: UTM parameters linking Calendly bookings to GammaDoc ID in ClickUp
- Follow-up: Non-responders enter cold email sequence via Smart Lead
- Benchmark assumption: 1 client per 200 outreaches (needs validation as data accumulates)

Daniel is responsible for recording and sending ≥50 personalized outreaches as the immediate next step.
Upwork profile update is also required to attract higher-ticket inbound leads.\
""",
    },
    {
        "title": "Home Service Lead Gen System — Contractor License Scraper",
        "content": """\
# Home Service Lead Gen System
Meeting: Daniel / William, 2026-05-26

## Mechanism
Daily scraper pulling new contractor licenses from CA, OR, and WA state databases.
Leads are pushed to Close CRM and handed to a sales rep (Daniel's fiancé's brother).

## Business Model
- Pricing: $97/month
- LTV assumption: 25–40 months (conservative end is more defensible at this stage)
- Upsell potential: high

## Infrastructure
- Hosting: Railway (24/7 uptime)
- Data storage: Supabase
- Status: Live and running

## Next Steps
- Test the Close CRM integration end-to-end
- Call leads from the contractor list to validate scraper accuracy against real contacts\
""",
    },
    {
        "title": "Claude Copywriting & Video Automation Pipeline",
        "content": """\
# Automation & Systems — Claude Copywriting + Video Pipeline
Meeting: Daniel / William, 2026-05-26

## Claude Copywriting Pipeline (Live)
Flow: Brief → Ideation → QA → Scripting → QA → ClickUp task creation
Daniel iterates with repeated feedback to improve model output quality.
Current state: functional; refinement ongoing.

## Video Generation Pipeline (Next Build)
Flow: Claude dissects script into 10-second chunks → Higgsfield generates video → files saved to Google Drive
Open research question: whether Claude can view video output to auto-flag and regenerate out-of-sync clips.
This is the completion milestone for the automation build workstream.

## Infrastructure Stack
- Railway: 24/7 server hosting (lead scraper)
- Supabase: data storage layer
- Claude Remote Routines (Max plan, 15/day): scheduled server-side execution
- Claude Live Artifacts: real-time dashboards\
""",
    },
    {
        "title": "Action Items — Daniel / William 2026-05-26",
        "content": """\
# Action Items — Daniel / William (2026-05-26)
All items are owned by Daniel.

1. Update Upwork profile to attract higher-ticket clients
2. Record and send ≥50 personalized GammaDoc/Loom outreaches to tax firms
3. Test the Close CRM integration for the home service lead-gen project
4. Complete the Claude-to-Higgsfield video automation pipeline
5. Call leads from contractor list to validate scraper accuracy

Next review: track conversion rate on outreaches vs. 1/200 benchmark.
Full recording: https://fathom.video/calls/688071219\
""",
    },
]

# ── Voyage embedding ─────────────────────────────────────────────────────────
async def embed_texts(texts: list[str]) -> list[list[float]]:
    if not VOYAGE_KEY:
        raise RuntimeError("VOYAGE_API_KEY is not set")
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            VOYAGE_URL,
            headers={"Authorization": f"Bearer {VOYAGE_KEY}", "Content-Type": "application/json"},
            json={"model": VOYAGE_MODEL, "input": texts, "input_type": "document"},
        )
        resp.raise_for_status()
        data = resp.json()
    return [item["embedding"] for item in data["data"]]


# ── Supabase upsert ──────────────────────────────────────────────────────────
def upsert_rows(rows: list[dict]):
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError("SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY not set")
    db = create_client(SUPABASE_URL, SUPABASE_KEY)
    db.table(TABLE).insert(rows).execute()
    print(f"  ✓ Inserted {len(rows)} row(s) into {TABLE}")


# ── Main ──────────────────────────────────────────────────────────────────────
async def main(dry_run: bool = False):
    total = len(CHUNKS_RAW)
    print(f"\nIngest: {MEETING_TITLE}")
    print(f"Chunks : {total}")
    print(f"Mode   : {'DRY RUN — no DB writes' if dry_run else 'LIVE'}\n")

    rows_to_insert = []

    for i in range(0, total, EMBED_BATCH):
        batch = CHUNKS_RAW[i : i + EMBED_BATCH]
        texts = [c["content"] for c in batch]

        print(f"  Embedding batch {i // EMBED_BATCH + 1} ({len(batch)} chunks)...")

        if not dry_run:
            embeddings = await embed_texts(texts)
        else:
            embeddings = [[0.0] * 1536 for _ in batch]   # placeholder in dry-run

        for j, (chunk, emb) in enumerate(zip(batch, embeddings)):
            idx = i + j
            row = {
                "repo": REPO,
                "source_type": SOURCE_TYPE,
                "path": f"meetings/{MEETING_DATE}-daniel-kalinin.md",
                "title": chunk["title"],
                "url": MEETING_URL,
                "content": chunk["content"],
                "metadata": {
                    "date": MEETING_DATE,
                    "participants": ["Chance Peare", "Daniel Kalinin"],
                    "meeting_type": "client_review",
                    "client": "daniel-lead-statement",
                    "chunk_index": idx,
                    "total_chunks": total,
                    "tags": ["daniel", "lead-statement", "client-acquisition", "automation"],
                },
                "embedding": emb,
            }
            rows_to_insert.append(row)

            if dry_run:
                print(f"    [{idx}] {chunk['title'][:60]} — {len(chunk['content'])} chars")

        if not dry_run and i + EMBED_BATCH < total:
            print(f"  Sleeping {RATE_SLEEP}s (Voyage rate limit)...")
            await asyncio.sleep(RATE_SLEEP)

    if dry_run:
        print("\nDry run complete. No rows written.")
        print("\nSample row (first chunk, embedding omitted):")
        sample = {k: v for k, v in rows_to_insert[0].items() if k != "embedding"}
        print(json.dumps(sample, indent=2))
        return

    upsert_rows(rows_to_insert)
    print(f"\nDone. {total} chunks ingested for '{MEETING_TITLE}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Daniel meeting into Supabase RAG")
    parser.add_argument("--dry-run", action="store_true", help="Preview chunks without writing to DB")
    args = parser.parse_args()

    asyncio.run(main(dry_run=args.dry_run))
