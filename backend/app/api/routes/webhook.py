"""GitHub webhook handler — triggers re-indexing on push events."""

import hashlib
import hmac
import logging

from fastapi import APIRouter, BackgroundTasks, Header, HTTPException, Request

from app.config import settings
from app.ingestion.pipeline import create_job, run_ingestion

logger = logging.getLogger(__name__)

router = APIRouter()

DEFAULT_SOURCE_TYPES = ["code", "issues", "prs", "readme"]


def _verify_signature(body: bytes, signature: str) -> bool:
    """Verify GitHub webhook HMAC-SHA256 signature."""
    if not settings.github_webhook_secret:
        return False
    expected = "sha256=" + hmac.new(
        settings.github_webhook_secret.encode(),
        body,
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(expected, signature)


@router.post("/webhook/github")
async def github_webhook(
    request: Request,
    background_tasks: BackgroundTasks,
    x_github_event: str = Header(...),
    x_hub_signature_256: str = Header(default=""),
):
    body = await request.body()

    if not _verify_signature(body, x_hub_signature_256):
        raise HTTPException(403, "Invalid webhook signature")

    if x_github_event not in ("push", "issues", "pull_request"):
        return {"ignored": True, "event": x_github_event}

    payload = await request.json()
    repo_data = payload.get("repository", {})
    owner = repo_data.get("owner", {}).get("login")
    name = repo_data.get("name")

    if not owner or not name:
        raise HTTPException(400, "Could not parse repository from payload")

    job_id = create_job(owner, name, DEFAULT_SOURCE_TYPES)
    background_tasks.add_task(run_ingestion, job_id, owner, name, DEFAULT_SOURCE_TYPES)

    logger.info("Webhook triggered re-index for %s/%s (job %s)", owner, name, job_id)
    return {"job_id": job_id, "repo": f"{owner}/{name}", "event": x_github_event}
