import asyncio
from contextlib import asynccontextmanager, suppress

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.routes import health, ingest, query, webhook, v1
from app.config import settings
from app.heartbeat import heartbeat_loop
from app.mcp_server import mcp_app


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with mcp_app.lifespan(app):
        heartbeat_task = asyncio.create_task(heartbeat_loop())
        try:
            yield
        finally:
            heartbeat_task.cancel()
            with suppress(asyncio.CancelledError):
                await heartbeat_task


app = FastAPI(
    title="RAG-Link API",
    description="RAG pipeline for Framework OPS — GitHub-sourced knowledge base",
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:3000"],
    allow_origin_regex=r"https://.*\.up\.railway\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def mcp_bearer_auth(request: Request, call_next):
    if request.url.path.startswith("/mcp") and settings.mcp_auth_token:
        header = request.headers.get("authorization", "")
        token = header[7:] if header.lower().startswith("bearer ") else ""
        if token != settings.mcp_auth_token:
            return JSONResponse({"error": "Unauthorized"}, status_code=401)
    return await call_next(request)


app.include_router(health.router, tags=["health"])
app.include_router(query.router, prefix="/api", tags=["query"])
app.include_router(ingest.router, prefix="/api", tags=["ingest"])
app.include_router(webhook.router, prefix="/api", tags=["webhook"])
app.include_router(v1.router, tags=["canonical-rag"])

app.mount("/mcp", mcp_app)
