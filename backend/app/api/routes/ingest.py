"""Ingestion endpoints — trigger indexing, poll job status, list repos."""

import asyncio
import logging

from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel, Field

from app.ingestion.pipeline import create_job, run_ingestion
from app.retrieval.vector_store import get_ingestion_jobs, get_job, get_repositories

logger = logging.getLogger(__name__)

router = APIRouter()

VALID_SOURCE_TYPES = {"code", "issues", "prs", "readme"}


class IngestRequest(BaseModel):
    owner: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    source_types: list[str] = Field(
        default=["code", "issues", "prs", "readme"]
    )


@router.post("/ingest", status_code=202)
async def trigger_ingestion(req: IngestRequest, background_tasks: BackgroundTasks):
    invalid = set(req.source_types) - VALID_SOURCE_TYPES
    if invalid:
        raise HTTPException(422, f"Invalid source_types: {invalid}")

    job_id = create_job(req.owner, req.name, req.source_types)

    background_tasks.add_task(
        run_ingestion, job_id, req.owner, req.name, req.source_types
    )

    return {"job_id": job_id, "status": "pending"}


@router.get("/ingest/{job_id}")
async def get_job_status(job_id: str):
    job = await get_job(job_id)
    if not job:
        raise HTTPException(404, "Job not found")
    return job


@router.get("/ingest")
async def list_jobs():
    return await get_ingestion_jobs()


@router.get("/repos")
async def list_repos():
    return await get_repositories()
