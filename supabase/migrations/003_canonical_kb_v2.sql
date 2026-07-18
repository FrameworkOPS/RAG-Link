-- Canonical Voyage-3 knowledge base for all Framework OPS agents.

alter table public.kb_documents
  add column if not exists embedding_model text;

update public.kb_documents
set embedding_model = 'voyage-3'
where embedding is not null
  and embedding_model is null;

alter table public.kb_documents enable row level security;
alter table public.kb_documents force row level security;

create or replace function public.match_kb_documents_v2(
  query_embedding vector(1024),
  filter_tenant_id text default 'skyright',
  filter_sources text[] default null,
  match_threshold double precision default 0.4,
  result_limit integer default 10
)
returns table (
  id uuid,
  title text,
  content text,
  url text,
  source text,
  source_id text,
  tenant_id text,
  metadata jsonb,
  embedding_model text,
  similarity double precision
)
language sql
stable
security definer
set search_path = public
as $$
  select
    documents.id,
    documents.title,
    documents.content,
    documents.url,
    documents.source,
    documents.source_id,
    documents.tenant_id,
    coalesce(documents.metadata, '{}'::jsonb),
    documents.embedding_model,
    1 - (documents.embedding <=> query_embedding) as similarity
  from public.kb_documents as documents
  where documents.embedding is not null
    and documents.tenant_id = filter_tenant_id
    and (filter_sources is null or documents.source = any(filter_sources))
    and 1 - (documents.embedding <=> query_embedding) >= match_threshold
  order by documents.embedding <=> query_embedding
  limit least(greatest(result_limit, 1), 50);
$$;

revoke all on function public.match_kb_documents_v2(
  vector, text, text[], double precision, integer
) from public, anon, authenticated;
grant execute on function public.match_kb_documents_v2(
  vector, text, text[], double precision, integer
) to service_role;

create or replace function public.kb_source_counts_v2(
  filter_tenant_id text default 'skyright'
)
returns table (
  source text,
  document_count bigint,
  embedded_count bigint,
  missing_embedding_count bigint
)
language sql
stable
security definer
set search_path = public
as $$
  select
    documents.source,
    count(*) as document_count,
    count(documents.embedding) as embedded_count,
    count(*) filter (where documents.embedding is null) as missing_embedding_count
  from public.kb_documents as documents
  where documents.tenant_id = filter_tenant_id
  group by documents.source
  order by documents.source;
$$;

revoke all on function public.kb_source_counts_v2(text)
  from public, anon, authenticated;
grant execute on function public.kb_source_counts_v2(text)
  to service_role;

