import { ExternalLink } from "lucide-react";
import type { SourceDoc } from "@/lib/api";
import clsx from "clsx";

const TYPE_COLORS: Record<string, string> = {
  code:       "bg-blue-500/15 text-blue-300",
  issue:      "bg-yellow-500/15 text-yellow-300",
  pr:         "bg-purple-500/15 text-purple-300",
  readme:     "bg-green-500/15 text-green-300",
  wiki:       "bg-cyan-500/15 text-cyan-300",
  discussion: "bg-orange-500/15 text-orange-300",
};

export function SourceCard({ doc }: { doc: SourceDoc }) {
  const label = doc.path ?? doc.title ?? doc.source_type;
  const color = TYPE_COLORS[doc.source_type] ?? "bg-gray-500/15 text-gray-300";
  return (
    <a
      href={doc.url}
      target="_blank"
      rel="noopener noreferrer"
      className="flex items-start gap-2 p-2.5 rounded-lg bg-gray-800 hover:bg-gray-750
                 border border-gray-700 hover:border-brand-500/40 transition-all min-w-0"
    >
      <span className={clsx("shrink-0 px-1.5 py-0.5 rounded text-xs font-medium", color)}>
        {doc.source_type}
      </span>
      <span className="text-xs text-gray-300 truncate flex-1">{label}</span>
      <ExternalLink size={11} className="shrink-0 text-gray-600 mt-0.5" />
    </a>
  );
}
