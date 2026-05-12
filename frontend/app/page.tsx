import Link from "next/link";
import { MessageSquare, Upload, GitBranch } from "lucide-react";

const cards = [
  {
    href: "/chat",
    icon: MessageSquare,
    title: "Chat",
    desc: "Ask questions about your codebase, issues, and PRs.",
  },
  {
    href: "/ingestion",
    icon: Upload,
    title: "Ingestion",
    desc: "Trigger indexing runs and monitor job progress.",
  },
  {
    href: "/repos",
    icon: GitBranch,
    title: "Repos",
    desc: "Manage which GitHub repositories are indexed.",
  },
];

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-full px-6 py-16">
      <h1 className="text-4xl font-bold text-gray-100 mb-2">RAG-Link</h1>
      <p className="text-gray-400 mb-12 text-center max-w-md">
        AI-powered knowledge base for Framework OPS — search across code, issues,
        and PRs with natural language.
      </p>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-5 w-full max-w-3xl">
        {cards.map(({ href, icon: Icon, title, desc }) => (
          <Link
            key={href}
            href={href}
            className="group flex flex-col gap-3 p-6 rounded-xl bg-gray-900 border border-gray-800
                       hover:border-brand-500/50 hover:bg-gray-800 transition-all"
          >
            <Icon size={24} className="text-brand-500" />
            <h2 className="font-semibold text-gray-100 group-hover:text-white">{title}</h2>
            <p className="text-sm text-gray-500">{desc}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
