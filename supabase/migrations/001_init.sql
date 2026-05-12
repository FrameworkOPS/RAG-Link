-- Enable pgvector extension
create extension if not exists vector;

-- Documents table: stores chunked content with embeddings
create table if not exists documents (
  id           uuid primary key default gen_random_uuid(),
  repo         text not null,
  source_type  text not null check (source_type in ('code', 'issue', 'pr', 'wiki', 'discussion', 'readme')),
  path         text,
  title        text,
  url          text,
  content      text not null,
  metadata     jsonb not null default '{}',
  embedding    vector(1536) not null,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now()
);

-- Ingestion jobs table
create table if not exists ingestion_jobs (
  id              uuid primary key default gen_random_uuid(),
  repo            text not null,
  status          text not null default 'pending' check (status in ('pending', 'running', 'completed', 'failed')),
  source_types    text[] not null default array['code', 'issues', 'prs', 'readme'],
  total_chunks    int not null default 0,
  indexed_chunks  int not null default 0,
  error           text,
  started_at      timestamptz,
  completed_at    timestamptz,
  created_at      timestamptz not null default now()
);

-- Tracked repositories
create table if not exists repositories (
  id          uuid primary key default gen_random_uuid(),
  owner       text not null,
  name        text not null,
  full_name   text not null generated always as (owner || '/' || name) stored,
  description text,
  is_active   boolean not null default true,
  last_indexed_at timestamptz,
  created_at  timestamptz not null default now(),
  unique (owner, name)
);

-- Index for fast similarity search (cosine distance)
create index if not exists documents_embedding_idx
  on documents using ivfflat (embedding vector_cosine_ops)
  with (lists = 100);

-- Index for filtering by repo
create index if not exists documents_repo_idx on documents (repo);
create index if not exists documents_source_type_idx on documents (source_type);

-- Auto-update updated_at
create or replace function update_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create trigger documents_updated_at
  before update on documents
  for each row execute function update_updated_at();

-- RPC: vector similarity search with metadata filtering
create or replace function match_documents(
  query_embedding vector(1536),
  match_threshold float default 0.5,
  match_count     int default 10,
  filter_repo     text default null,
  filter_types    text[] default null
)
returns table (
  id          uuid,
  repo        text,
  source_type text,
  path        text,
  title       text,
  url         text,
  content     text,
  metadata    jsonb,
  similarity  float
)
language sql stable as $$
  select
    d.id,
    d.repo,
    d.source_type,
    d.path,
    d.title,
    d.url,
    d.content,
    d.metadata,
    1 - (d.embedding <=> query_embedding) as similarity
  from documents d
  where
    (filter_repo is null or d.repo = filter_repo)
    and (filter_types is null or d.source_type = any(filter_types))
    and 1 - (d.embedding <=> query_embedding) > match_threshold
  order by d.embedding <=> query_embedding
  limit match_count;
$$;

-- RPC: delete documents for a repo (used before re-indexing)
create or replace function delete_repo_documents(target_repo text)
returns int
language sql as $$
  with deleted as (
    delete from documents where repo = target_repo returning id
  )
  select count(*)::int from deleted;
$$;
