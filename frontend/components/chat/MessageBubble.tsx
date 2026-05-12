import type { SourceDoc } from "@/lib/api";
import { SourceCard } from "./SourceCard";
import clsx from "clsx";

export interface Message {
  role: "user" | "assistant";
  content: string;
  sources?: SourceDoc[];
  streaming?: boolean;
}

function renderMarkdown(text: string): string {
  return text
    .replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) =>
      `<pre class="bg-gray-900 rounded-lg p-4 overflow-x-auto my-3 border border-gray-700"><code class="language-${lang} text-sm text-gray-200">${escapeHtml(code.trimEnd())}</code></pre>`
    )
    .replace(/`([^`]+)`/g, '<code class="bg-gray-800 px-1.5 py-0.5 rounded text-sm text-brand-300">$1</code>')
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2" target="_blank" class="text-brand-400 underline">$1</a>')
    .replace(/^#{1,3} (.+)/gm, '<h3 class="font-semibold text-gray-100 mt-4 mb-1">$1</h3>')
    .replace(/\n/g, "<br/>");
}

function escapeHtml(s: string) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

export function MessageBubble({ msg }: { msg: Message }) {
  if (msg.role === "user") {
    return (
      <div className="flex justify-end">
        <div className="max-w-[75%] px-4 py-3 rounded-2xl bg-brand-500 text-white text-sm leading-relaxed">
          {msg.content}
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-3">
      {msg.sources && msg.sources.length > 0 && (
        <div>
          <p className="text-xs text-gray-500 mb-2">Sources ({msg.sources.length})</p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-1.5">
            {msg.sources.map((s) => (
              <SourceCard key={s.id} doc={s} />
            ))}
          </div>
        </div>
      )}

      <div
        className={clsx(
          "prose-sm max-w-none text-sm text-gray-200 leading-relaxed",
          msg.streaming && "after:content-['▌'] after:animate-pulse after:text-brand-400"
        )}
        dangerouslySetInnerHTML={{ __html: renderMarkdown(msg.content) }}
      />
    </div>
  );
}
