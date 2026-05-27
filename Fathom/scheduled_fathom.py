"""
scheduled_fathom.py — Daily Fathom pipeline entry point

Runs both Fathom integrations in sequence:
  1. ingest/fathom_ingest.py      → RAG (Supabase pgvector via Voyage AI)
  2. obsidian/fathom_to_obsidian.py → Obsidian vault notes

One failure does NOT block the other. Exit code:
  0 = all succeeded
  1 = one or more failures

Usage:
    python scheduled_fathom.py              # default: last 24 hrs
    python scheduled_fathom.py --hours 48
    python scheduled_fathom.py --start 2026-05-01 --end 2026-05-26
    python scheduled_fathom.py --dry-run

LaunchAgent (macOS) — see ../launchd/com.frameworkops.fathom.plist
"""

import sys
import logging
import argparse
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger(__name__)


def run_ingest(start_dt, end_dt, dry_run):
    log.info("━━━ STEP 1/2: RAG Ingestion (Supabase / Voyage AI) ━━━")
    try:
        from ingest.fathom_ingest import run
        ingested, skipped, errors = run(start_dt, end_dt, dry_run=dry_run)
        log.info("RAG ingest complete — ingested: %d, skipped: %d, errors: %d",
                 ingested, skipped, errors)
        return errors == 0
    except Exception as exc:
        log.error("RAG ingest FAILED: %s", exc, exc_info=True)
        return False


def run_obsidian(start_dt, end_dt, dry_run):
    log.info("━━━ STEP 2/2: Obsidian Sync ━━━")
    try:
        from obsidian.fathom_to_obsidian import run
        written, skipped, errors = run(start_dt, end_dt, dry_run=dry_run)
        log.info("Obsidian sync complete — written: %d, skipped: %d, errors: %d",
                 written, skipped, errors)
        return errors == 0
    except Exception as exc:
        log.error("Obsidian sync FAILED: %s", exc, exc_info=True)
        return False


def parse_args():
    parser = argparse.ArgumentParser(description="Daily Fathom pipeline runner")
    parser.add_argument("--hours",         type=float, default=24)
    parser.add_argument("--start",         help="YYYY-MM-DD")
    parser.add_argument("--end",           help="YYYY-MM-DD")
    parser.add_argument("--dry-run",       action="store_true")
    parser.add_argument("--skip-ingest",   action="store_true")
    parser.add_argument("--skip-obsidian", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    now = datetime.now(timezone.utc)

    if args.start:
        start_dt = datetime.fromisoformat(args.start).replace(tzinfo=timezone.utc)
        end_dt   = (
            datetime.fromisoformat(args.end).replace(tzinfo=timezone.utc)
            if args.end else now
        )
    else:
        end_dt   = now
        start_dt = end_dt - timedelta(hours=args.hours)

    log.info("Fathom pipeline starting | window: %s → %s | dry_run: %s",
             start_dt.strftime("%Y-%m-%d %H:%M UTC"),
             end_dt.strftime("%Y-%m-%d %H:%M UTC"),
             args.dry_run)

    results = {}

    if not args.skip_ingest:
        results["ingest"]   = run_ingest(start_dt, end_dt, args.dry_run)
    if not args.skip_obsidian:
        results["obsidian"] = run_obsidian(start_dt, end_dt, args.dry_run)

    log.info("━━━ PIPELINE SUMMARY ━━━")
    all_ok = True
    for step, ok in results.items():
        log.info("  %s: %s", step.upper(), "✓ OK" if ok else "✗ FAILED")
        if not ok:
            all_ok = False

    sys.exit(0 if all_ok else 1)
