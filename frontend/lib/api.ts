const API = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export interface SourceDoc {
  id: string;
  repo: string;
  source_type: string;
  path: string | null;
  title: string | null;
  url: string;
  similarity: number;
}

export interface IngestJob {
  id: string;
  repo: string;
  status: "pending" | "running" | "completed" | "failed";
  source_types: string[];
  total_chunks: number;
  indexed_chunks: number;
  error: string | null;
  started_at: string | null;
  completed_at: string | null;
  created_at: string;
}

export interface Repository {
  id: string;
  owner: string;
  name: string;
  full_name: string;
  description: string | null;
  is_active: boolean;
  last_indexed_at: string | null;
  created_at: string;
}

// ── Streaming query ──────────────────────────────────────────────────────────

export interface QueryOptions {
  query: string;
  repo?: string;
  source_types?: string[];
  match_count?: number;
  threshold?: number;
}

export async function* streamQuery(opts: QueryOptions): AsyncGenerator<
  | { type: "sources"; sources: SourceDoc[] }
  | { type: "token"; token: string }
  | { type: "done" }
> {
  const resp = await fetch(`${API}/api/query`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(opts),
  });

  if (!resp.ok) throw new Error(`Query failed: ${resp.status}`);
  if (!resp.body) throw new Error("No response body");

  const reader = resp.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    const events = buffer.split("\n\n");
    buffer = events.pop() ?? "";

    for (const event of events) {
      if (!event.trim()) continue;
      const lines = event.split("\n");
      const eventType = lines.find((l) => l.startsWith("event:"))?.slice(7).trim();
      const dataLine = lines.find((l) => l.startsWith("data:"))?.slice(5).trim();
      if (!eventType || !dataLine) continue;

      const data = JSON.parse(dataLine);
      if (eventType === "sources") yield { type: "sources", sources: data };
      else if (eventType === "token") yield { type: "token", token: data.token };
      else if (eventType === "done") yield { type: "done" };
    }
  }
}

// ── Ingestion ────────────────────────────────────────────────────────────────

export async function triggerIngest(
  owner: string,
  name: string,
  source_types: string[]
): Promise<{ job_id: string; status: string }> {
  const resp = await fetch(`${API}/api/ingest`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ owner, name, source_types }),
  });
  if (!resp.ok) throw new Error(`Ingest failed: ${resp.status}`);
  return resp.json();
}

export async function getJob(jobId: string): Promise<IngestJob> {
  const resp = await fetch(`${API}/api/ingest/${jobId}`);
  if (!resp.ok) throw new Error(`Job fetch failed: ${resp.status}`);
  return resp.json();
}

export async function listJobs(): Promise<IngestJob[]> {
  const resp = await fetch(`${API}/api/ingest`);
  if (!resp.ok) throw new Error("Failed to list jobs");
  return resp.json();
}

export async function listRepos(): Promise<Repository[]> {
  const resp = await fetch(`${API}/api/repos`);
  if (!resp.ok) throw new Error("Failed to list repos");
  return resp.json();
}
