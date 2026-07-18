"""Shared API key auth for internal RAG endpoints."""

import hmac

from fastapi import Header, HTTPException, status

from app.config import settings


async def require_api_key(
    x_api_key: str | None = Header(default=None),
    authorization: str | None = Header(default=None),
) -> None:
    if not settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="API key auth is not configured.",
        )
    bearer = authorization[7:] if authorization and authorization.lower().startswith("bearer ") else ""
    incoming = x_api_key or bearer
    if not incoming or not hmac.compare_digest(incoming, settings.api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key.",
        )
