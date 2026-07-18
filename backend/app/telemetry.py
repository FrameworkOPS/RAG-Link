"""Bounded RAG run telemetry. Retrieved content is never persisted here."""

from datetime import UTC, datetime
from time import perf_counter
from typing import Any

from supabase import create_client

from app.config import settings


class RagRun:
    def __init__(
        self,
        *,
        caller_agent: str,
        record_type: str,
        parent_run_id: str | None,
        inputs: dict[str, Any],
    ):
        self.caller_agent = caller_agent
        self.record_type = record_type
        self.parent_run_id = parent_run_id
        self.inputs = inputs
        self.started = perf_counter()
        self.run_id: str | None = None

    def _table(self):
        db = create_client(settings.supabase_url, settings.supabase_service_role_key)
        return db.schema("ops").table("agent_runs")

    async def start(self) -> None:
        row = {
            "agent_name": "rag.agent",
            "caller_agent": self.caller_agent,
            "parent_run_id": self.parent_run_id,
            "record_type": self.record_type,
            "status": "running",
            "inputs": self.inputs,
        }
        response = self._table().insert(row).execute()
        if response.data:
            self.run_id = response.data[0]["id"]

    async def finish(
        self,
        *,
        status: str,
        document_ids: list[str],
        error_message: str | None = None,
    ) -> None:
        elapsed_ms = round((perf_counter() - self.started) * 1000)
        persisted_status = {
            "completed": "success",
            "failed": "error",
            "success": "success",
            "error": "error",
            "skipped": "skipped",
        }.get(status, status)
        update = {
            "status": persisted_status,
            "run_finished_at": datetime.now(UTC).isoformat(),
            "summary": f"{self.record_type} {status} in {elapsed_ms}ms",
            "outputs": {
                "document_ids": document_ids[:50],
                "document_count": len(document_ids),
                "elapsed_ms": elapsed_ms,
            },
            "rows_processed": len(document_ids),
            "error_message": (error_message or "")[:1000] or None,
        }
        table = self._table()
        if self.run_id:
            table.update(update).eq("id", self.run_id).execute()
        else:
            table.insert(
                {
                    "agent_name": "rag.agent",
                    "caller_agent": self.caller_agent,
                    "parent_run_id": self.parent_run_id,
                    "record_type": self.record_type,
                    **update,
                }
            ).execute()
