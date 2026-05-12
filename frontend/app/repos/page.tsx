"use client";

import { useEffect, useState } from "react";
import { GitBranch, ExternalLink, RefreshCw } from "lucide-react";
import { listRepos, type Repository } from "@/lib/api";

function RepoCard({ repo }: { repo: Repository }) {
  const lastIndexed = repo.last_indexed_at
    ? new Date(repo.last_indexed_at).toLocaleString()
    : "Never";
  return (
    <div className="p-5 rounded-xl bg-gray-900 border border-gray-800">
      <div className="flex items-start gap-3">
        <GitBranch size={18} className="text-brand-500 mt-0.5 shrink-0" />
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2">
            <span className="font-medium text-gray-100">{repo.full_name}</span>
            <a
              href={`https://github.com/${repo.full_name}`}
              target="_blank"
              rel="noopener noreferrer"
              className="text-gray-600 hover:text-brand-400 transition-colors"
            >
              <ExternalLink size={13} />
            </a>
          </div>
          {repo.description && (
            <p className="text-sm text-gray-500 mt-0.5 truncate">{repo.description}</p>
          )}
          <p className="text-xs text-gray-600 mt-2">Last indexed: {lastIndexed}</p>
        </div>
        <span
          className={`shrink-0 text-xs px-2 py-0.5 rounded-full ${
            repo.is_active
              ? "bg-green-500/15 text-green-300"
              : "bg-gray-700 text-gray-500"
          }`}
        >
          {repo.is_active ? "active" : "inactive"}
        </span>
      </div>
    </div>
  );
}

export default function ReposPage() {
  const [repos, setRepos] = useState<Repository[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchRepos = async () => {
    setLoading(true);
    try {
      setRepos(await listRepos());
    } catch {}
    setLoading(false);
  };

  useEffect(() => { fetchRepos(); }, []);

  return (
    <div className="px-6 py-8 max-w-3xl">
      <div className="flex items-center justify-between mb-1">
        <h1 className="text-2xl font-bold text-gray-100">Repositories</h1>
        <button onClick={fetchRepos} className="text-gray-500 hover:text-gray-300 transition-colors">
          <RefreshCw size={15} />
        </button>
      </div>
      <p className="text-gray-500 text-sm mb-8">
        Repositories are automatically registered when their first indexing job completes.
      </p>

      {loading ? (
        <p className="text-gray-600 text-sm">Loading…</p>
      ) : repos.length === 0 ? (
        <p className="text-gray-600 text-sm">
          No repositories indexed yet. Go to{" "}
          <a href="/ingestion" className="text-brand-400 hover:underline">Ingestion</a> to add one.
        </p>
      ) : (
        <div className="space-y-3">
          {repos.map((r) => (
            <RepoCard key={r.id} repo={r} />
          ))}
        </div>
      )}
    </div>
  );
}
