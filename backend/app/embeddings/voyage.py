"""Voyage AI embedding client — voyage-code-2 (1536-dim)."""

import logging
from typing import Literal

import httpx
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

logger = logging.getLogger(__name__)

VOYAGE_API_URL = "https://api.voyageai.com/v1/embeddings"


class VoyageClient:
    def __init__(self, api_key: str, model: str = "voyage-code-2"):
        self._api_key = api_key
        self._model = model

    @retry(
        stop=stop_after_attempt(8),
        wait=wait_exponential(multiplier=2, min=5, max=120),
        retry=retry_if_exception_type(httpx.HTTPStatusError),
    )
    async def embed(
        self,
        texts: list[str],
        input_type: Literal["query", "document"] = "document",
    ) -> list[list[float]]:
        if not texts:
            return []

        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(
                VOYAGE_API_URL,
                headers={
                    "Authorization": f"Bearer {self._api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": self._model,
                    "input": texts,
                    "input_type": input_type,
                },
            )
            resp.raise_for_status()
            data = resp.json()

        embeddings = [item["embedding"] for item in data["data"]]
        logger.debug("Embedded %d texts with %s", len(embeddings), self._model)
        return embeddings

    async def embed_query(self, query: str) -> list[float]:
        results = await self.embed([query], input_type="query")
        return results[0]
