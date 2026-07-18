import asyncio

import pytest
from fastapi import HTTPException

from app.api.auth import require_api_key
from app.config import settings
from app.retrieval.kb_store import split_text


def test_split_text_is_deterministic_and_bounded():
    text = ("Framework OPS paragraph.\n\n" * 250).strip()
    first = split_text(text, chunk_size=500, overlap=50)
    second = split_text(text, chunk_size=500, overlap=50)
    assert first == second
    assert len(first) > 1
    assert all(chunk and len(chunk) <= 500 for chunk in first)


def test_api_auth_accepts_bearer_and_rejects_wrong_token(monkeypatch):
    monkeypatch.setattr(settings, "api_key", "canonical-secret")
    asyncio.run(require_api_key(x_api_key=None, authorization="Bearer canonical-secret"))
    with pytest.raises(HTTPException) as caught:
        asyncio.run(require_api_key(x_api_key="wrong", authorization=None))
    assert caught.value.status_code == 401

