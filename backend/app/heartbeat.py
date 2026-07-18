"""Truthful 60-second rag.agent heartbeat."""

import asyncio
import logging

import httpx

from app.config import settings

logger = logging.getLogger(__name__)

SKILLS = [
    {"name": "search_kb", "description": "Semantic search over the canonical Framework OPS corpus."},
    {"name": "documents_upsert", "description": "Idempotently chunk, embed, and replace source documents."},
]


async def heartbeat_loop() -> None:
    if not settings.agent_os_control_plane_url or not settings.agent_api_token:
        logger.info("rag.agent heartbeat disabled: control-plane configuration absent")
        return
    endpoint = f"{settings.agent_os_control_plane_url.rstrip('/')}/api/agent-os/heartbeat"
    while True:
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.post(
                    endpoint,
                    headers={"authorization": f"Bearer {settings.agent_api_token}"},
                    json={
                        "agent": "rag.agent",
                        "status": "idle",
                        "version": settings.agent_version,
                        "service_url": settings.agent_service_url or None,
                        "skills": SKILLS,
                    },
                )
                response.raise_for_status()
        except Exception:
            logger.exception("rag.agent heartbeat failed")
        await asyncio.sleep(60)

