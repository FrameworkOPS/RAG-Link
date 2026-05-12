"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { MessageSquare, Upload, GitBranch, Activity } from "lucide-react";
import clsx from "clsx";

const nav = [
  { href: "/chat",      label: "Chat",       icon: MessageSquare },
  { href: "/ingestion", label: "Ingestion",  icon: Upload },
  { href: "/repos",     label: "Repos",      icon: GitBranch },
  { href: "/",          label: "Overview",   icon: Activity },
];

export function Sidebar() {
  const path = usePathname();
  return (
    <aside className="w-56 shrink-0 flex flex-col bg-gray-900 border-r border-gray-800">
      <div className="px-5 py-5 border-b border-gray-800">
        <span className="text-brand-500 font-bold text-lg tracking-tight">
          RAG-Link
        </span>
        <p className="text-gray-500 text-xs mt-0.5">Framework OPS</p>
      </div>

      <nav className="flex-1 px-3 py-4 space-y-1">
        {nav.map(({ href, label, icon: Icon }) => {
          const active = path === href || (href !== "/" && path.startsWith(href));
          return (
            <Link
              key={href}
              href={href}
              className={clsx(
                "flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors",
                active
                  ? "bg-brand-500/15 text-brand-400"
                  : "text-gray-400 hover:text-gray-100 hover:bg-gray-800"
              )}
            >
              <Icon size={16} />
              {label}
            </Link>
          );
        })}
      </nav>

      <div className="px-5 py-4 border-t border-gray-800 text-xs text-gray-600">
        v1.0.0
      </div>
    </aside>
  );
}
