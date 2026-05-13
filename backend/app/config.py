from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Supabase
    supabase_url: str
    supabase_service_role_key: str

    # Anthropic
    anthropic_api_key: str
    anthropic_model: str = "claude-sonnet-4-6"

    # Voyage AI
    voyage_api_key: str
    voyage_model: str = "voyage-code-2"
    voyage_embedding_dim: int = 1536

    # GitHub
    github_token: str
    github_webhook_secret: str = ""

    # App
    frontend_url: str = "http://localhost:3000"
    max_chunks_per_file: int = 50
    chunk_size: int = 1500        # chars
    chunk_overlap: int = 200      # chars
    retrieval_match_count: int = 8
    retrieval_threshold: float = 0.4

    # MCP
    mcp_auth_token: str = ""


settings = Settings()
