"use client";

import { useEffect, useRef, useState } from "react";
import { Loader2, Play, RefreshCw, CheckCircle, XCircle, Clock } from "lucide-react";
import { triggerIngest, listJobs, getJob, type IngestJob } from "@/lib/api";
import clsx from "clsx";

const SOURCE_OPTIONS = [
  { id: "code",   label: "Code Files" },
  { id: "issues", label: "Issues" },
  { id: "prs",    label: "Pull Requests" },
  { id: "readme", label: "READMEs" },
];

function StatusIcon({ status }: { status: IngestJob["status"] }) {
  if (status === "completed") return <CheckCircle size={14} className="text-green-400" />;
  if (status === "failed")    return <XCircle     size={14} className="text-red-400"   />;
  if (status === "running")   return <Loader2     size={14} className="text-brand-400 animate-spin" />;
  return <Clock size={14} className="text-gray-500" />;
}

function ProgressBar({ job }: { job: IngestJob }) {
  if (!job.total_chunks) return null;
  const pct = Math.round((job.indexed_chunks / job.total_chunks) * 100);
  return (
    <div className="mt-2">
      <div className="flex justify-between text-xs text-gray-500 mb-1">
        <span>{job.indexed_chunks} / {job.total_chunks} chunks</span>
        <span>{pct}%</span>
      </div>
      <div className="h-1.5 bg-gray-700 rounded-full overflow-hidden">
        <div
          className="h-full bg-brand-500 rounded-full transition-all duration-500"
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}

function JobRow({ job, onRefresh }: { job: IngestJob; onRefresh: () => void }) {
  return (
    <div className="p-4 rounded-xl bg-gray-900 border border-gray-800">
      <div className="flex items-center gap-2">
        <StatusIcon status={job.status} />
        <span className="font-medium text-gray-100 text-sm">{job.repo}</span>
        <span className={clsx(
          "ml-auto text-xs px-2 py-0.5 rounded-full",
          job.status === "completed" ? "bg-green-500/15 text-green-300" :
          job.status === "failed"    ? "bg-red-500/15 text-red-300"     :
          job.status === "running"   ? "bg-brand-500/15 text-brand-300" :
                                       "bg-gray-700 text-gray-400"
        )}>
          {job.status}
        </span>
        {(job.status === "running" || job.status === "pending") && (
          <button onClick={onRefresh} className="text-gray-600 hover:text-gray-300">
            <RefreshCw size={13} />
          </button>
        )}
      </div>

      <ProgressBar job={job} />

      {job.error && (
        <p className="mt-2 text-xs text-red-400 font-mono">{job.error}</p>
      )}

      <p className="mt-2 text-xs text-gray-600">
        Started: {job.created_at ? new Date(job.created_at).toLocaleString() : "—"}
        {job.completed_at && ` · Completed: ${new Date(job.completed_at).toLocaleString()}`}
      </p>
    </div>
  );
}

export default function IngestionPage() {
  const [owner, setOwner] = useState("");
  const [name, setName]   = useState("");
  const [types, setTypes] = useState<string[]>(["code", "issues", "prs", "readme"]);
  const [submitting, setSubmitting] = useState(false);
  const [jobs, setJobs] = useState<IngestJob[]>([]);
  const [error, setError] = useState("");
  const pollingRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const fetchJobs = async () => {
    try {
      setJobs(await listJobs());
    } catch {}
  };

  useEffect(() => {
    fetchJobs();
    pollingRef.current = setInterval(fetchJobs, 5000);
    return () => { if (pollingRef.current) clearInterval(pollingRef.current); };
  }, []);

  const toggleType = (id: string) =>
    setTypes((prev) => prev.includes(id) ? prev.filter((t) => t !== id) : [...prev, id]);

  const submit = async () => {
    if (!owner.trim() || !name.trim() || types.length === 0) return;
    setError("");
    setSubmitting(true);
    try {
      await triggerIngest(owner.trim(), name.trim(), types);
      setOwner(""); setName("");
      await fetchJobs();
    } catch (e) {
      setError(String(e));
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="px-6 py-8 max-w-3xl">
      <h1 className="text-2xl font-bold text-gray-100 mb-1">Ingestion</h1>
      <p className="text-gray-500 text-sm mb-8">Index a GitHub repository into the vector store.</p>

      {/* Trigger form */}
      <div className="p-6 rounded-xl bg-gray-900 border border-gray-800 mb-8">
        <h2 className="font-semibold text-gray-200 mb-4">New Indexing Job</h2>
        <div className="grid grid-cols-2 gap-3 mb-4">
          <div>
            <label className="block text-xs text-gray-500 mb-1">Owner</label>
            <input
              value={owner}
              onChange={(e) => setOwner(e.target.value)}
              placeholder="frameworkops"
              className="w-full px-3 py-2 rounded-lg bg-gray-800 border border-gray-700 text-sm
                         text-gray-200 placeholder-gray-600 focus:outline-none focus:border-brand-500"
            />
          </div>
          <div>
            <label className="block text-xs text-gray-500 mb-1">Repository</label>
            <input
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="my-repo"
              className="w-full px-3 py-2 rounded-lg bg-gray-800 border border-gray-700 text-sm
                         text-gray-200 placeholder-gray-600 focus:outline-none focus:border-brand-500"
            />
          </div>
        </div>

        <div className="mb-4">
          <label className="block text-xs text-gray-500 mb-2">Source Types</label>
          <div className="flex flex-wrap gap-2">
            {SOURCE_OPTIONS.map(({ id, label }) => (
              <button
                key={id}
                onClick={() => toggleType(id)}
                className={clsx(
                  "px-3 py-1.5 rounded-lg text-xs font-medium transition-colors border",
                  types.includes(id)
                    ? "bg-brand-500/15 text-brand-300 border-brand-500/40"
                    : "text-gray-500 border-gray-700 hover:border-gray-600"
                )}
              >
                {label}
              </button>
            ))}
          </div>
        </div>

        {error && <p className="text-red-400 text-xs mb-3">{error}</p>}

        <button
          onClick={submit}
          disabled={submitting || !owner.trim() || !name.trim()}
          className="flex items-center gap-2 px-4 py-2 rounded-lg bg-brand-500 hover:bg-brand-600
                     disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium
                     transition-colors"
        >
          {submitting ? <Loader2 size={14} className="animate-spin" /> : <Play size={14} />}
          Start Indexing
        </button>
      </div>

      {/* Jobs list */}
      <div className="flex items-center justify-between mb-4">
        <h2 className="font-semibold text-gray-200">Recent Jobs</h2>
        <button onClick={fetchJobs} className="text-gray-500 hover:text-gray-300 transition-colors">
          <RefreshCw size={14} />
        </button>
      </div>

      {jobs.length === 0 ? (
        <p className="text-gray-600 text-sm">No jobs yet.</p>
      ) : (
        <div className="space-y-3">
          {jobs.map((job) => (
            <JobRow key={job.id} job={job} onRefresh={fetchJobs} />
          ))}
        </div>
      )}
    </div>
  );
}
