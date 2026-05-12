"""GitHub API client — fetches repos, code, issues, PRs, wikis."""

import base64
import logging
from dataclasses import dataclass, field
from typing import Any

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

GITHUB_API = "https://api.github.com"

# Extensions we'll index; everything else is skipped
INDEXABLE_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx",
    ".go", ".rs", ".java", ".rb", ".php",
    ".c", ".cpp", ".h", ".cs", ".swift",
    ".md", ".mdx", ".txt", ".yaml", ".yml",
    ".json", ".toml", ".sh", ".dockerfile",
    ".sql", ".graphql",
}

MAX_FILE_BYTES = 200_000  # skip files larger than 200 KB


@dataclass
class RawDocument:
    source_type: str   # code | issue | pr | readme | wiki
    repo: str          # owner/name
    path: str | None
    title: str | None
    url: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)


class GitHubClient:
    def __init__(self, token: str):
        self._headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=1, min=2, max=30))
    async def _get(self, client: httpx.AsyncClient, path: str, **params) -> Any:
        resp = await client.get(
            f"{GITHUB_API}{path}",
            headers=self._headers,
            params=params,
        )
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.json()

    async def _paginate(
        self, client: httpx.AsyncClient, path: str, per_page: int = 100, **params
    ) -> list[Any]:
        results: list[Any] = []
        page = 1
        while True:
            data = await self._get(client, path, page=page, per_page=per_page, **params)
            if not data:
                break
            results.extend(data)
            if len(data) < per_page:
                break
            page += 1
        return results

    # ------------------------------------------------------------------
    # Public fetch methods
    # ------------------------------------------------------------------

    async def fetch_repo_tree(
        self, client: httpx.AsyncClient, owner: str, name: str
    ) -> list[dict]:
        """Returns flat list of all blobs in default branch."""
        repo = await self._get(client, f"/repos/{owner}/{name}")
        if not repo:
            return []
        branch = repo.get("default_branch", "main")
        tree = await self._get(
            client,
            f"/repos/{owner}/{name}/git/trees/{branch}",
            recursive="1",
        )
        if not tree:
            return []
        return [item for item in tree.get("tree", []) if item["type"] == "blob"]

    async def fetch_file_content(
        self, client: httpx.AsyncClient, owner: str, name: str, path: str
    ) -> str | None:
        data = await self._get(client, f"/repos/{owner}/{name}/contents/{path}")
        if not data or data.get("encoding") != "base64":
            return None
        if data.get("size", 0) > MAX_FILE_BYTES:
            return None
        try:
            return base64.b64decode(data["content"]).decode("utf-8", errors="replace")
        except Exception:
            return None

    async def fetch_issues(
        self, client: httpx.AsyncClient, owner: str, name: str
    ) -> list[RawDocument]:
        items = await self._paginate(
            client, f"/repos/{owner}/{name}/issues", state="all"
        )
        docs: list[RawDocument] = []
        for issue in items:
            if issue.get("pull_request"):
                continue  # PRs appear in issues endpoint too
            body = issue.get("body") or ""
            content = f"# {issue['title']}\n\n{body}"
            docs.append(
                RawDocument(
                    source_type="issue",
                    repo=f"{owner}/{name}",
                    path=None,
                    title=issue["title"],
                    url=issue["html_url"],
                    content=content,
                    metadata={
                        "number": issue["number"],
                        "state": issue["state"],
                        "labels": [l["name"] for l in issue.get("labels", [])],
                        "author": issue.get("user", {}).get("login"),
                        "created_at": issue.get("created_at"),
                    },
                )
            )
        return docs

    async def fetch_pull_requests(
        self, client: httpx.AsyncClient, owner: str, name: str
    ) -> list[RawDocument]:
        items = await self._paginate(
            client, f"/repos/{owner}/{name}/pulls", state="all"
        )
        docs: list[RawDocument] = []
        for pr in items:
            body = pr.get("body") or ""
            content = f"# PR #{pr['number']}: {pr['title']}\n\n{body}"
            docs.append(
                RawDocument(
                    source_type="pr",
                    repo=f"{owner}/{name}",
                    path=None,
                    title=pr["title"],
                    url=pr["html_url"],
                    content=content,
                    metadata={
                        "number": pr["number"],
                        "state": pr["state"],
                        "merged": pr.get("merged_at") is not None,
                        "base": pr.get("base", {}).get("ref"),
                        "head": pr.get("head", {}).get("ref"),
                        "author": pr.get("user", {}).get("login"),
                        "created_at": pr.get("created_at"),
                    },
                )
            )
        return docs

    async def fetch_code_files(
        self, client: httpx.AsyncClient, owner: str, name: str
    ) -> list[RawDocument]:
        blobs = await self.fetch_repo_tree(client, owner, name)
        docs: list[RawDocument] = []
        for blob in blobs:
            path: str = blob["path"]
            ext = "." + path.rsplit(".", 1)[-1].lower() if "." in path else ""
            if ext not in INDEXABLE_EXTENSIONS:
                continue

            content = await self.fetch_file_content(client, owner, name, path)
            if not content or not content.strip():
                continue

            filename = path.split("/")[-1]
            source_type = "readme" if filename.lower().startswith("readme") else "code"

            docs.append(
                RawDocument(
                    source_type=source_type,
                    repo=f"{owner}/{name}",
                    path=path,
                    title=filename,
                    url=f"https://github.com/{owner}/{name}/blob/HEAD/{path}",
                    content=content,
                    metadata={"size": blob.get("size", 0)},
                )
            )
        return docs

    async def fetch_all(
        self,
        owner: str,
        name: str,
        source_types: list[str],
    ) -> list[RawDocument]:
        async with httpx.AsyncClient(timeout=60.0) as client:
            docs: list[RawDocument] = []
            if "code" in source_types or "readme" in source_types:
                logger.info("Fetching code files for %s/%s", owner, name)
                docs.extend(await self.fetch_code_files(client, owner, name))
            if "issues" in source_types:
                logger.info("Fetching issues for %s/%s", owner, name)
                docs.extend(await self.fetch_issues(client, owner, name))
            if "prs" in source_types:
                logger.info("Fetching PRs for %s/%s", owner, name)
                docs.extend(await self.fetch_pull_requests(client, owner, name))
            return docs
