"use client";

import { useRef, useState } from "react";
import { Send, Loader2 } from "lucide-react";
import { streamQuery, type SourceDoc } from "@/lib/api";
import { MessageBubble, type Message } from "@/components/chat/MessageBubble";

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [repo, setRepo] = useState("");
  const bottomRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () =>
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });

  const submit = async () => {
    const query = input.trim();
    if (!query || loading) return;

    setInput("");
    setMessages((prev) => [...prev, { role: "user", content: query }]);
    setLoading(true);

    // Placeholder assistant message
    const assistantIdx = messages.length + 1;
    setMessages((prev) => [
      ...prev,
      { role: "assistant", content: "", sources: [], streaming: true },
    ]);

    try {
      for await (const event of streamQuery({ query, repo: repo || undefined })) {
        if (event.type === "sources") {
          setMessages((prev) => {
            const next = [...prev];
            next[assistantIdx] = { ...next[assistantIdx], sources: event.sources };
            return next;
          });
          scrollToBottom();
        } else if (event.type === "token") {
          setMessages((prev) => {
            const next = [...prev];
            next[assistantIdx] = {
              ...next[assistantIdx],
              content: next[assistantIdx].content + event.token,
            };
            return next;
          });
          scrollToBottom();
        } else if (event.type === "done") {
          setMessages((prev) => {
            const next = [...prev];
            next[assistantIdx] = { ...next[assistantIdx], streaming: false };
            return next;
          });
        }
      }
    } catch (err) {
      setMessages((prev) => {
        const next = [...prev];
        next[assistantIdx] = {
          ...next[assistantIdx],
          content: "Error: " + String(err),
          streaming: false,
        };
        return next;
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-full">
      {/* Header */}
      <div className="shrink-0 px-6 py-4 border-b border-gray-800 flex items-center gap-4">
        <h1 className="font-semibold text-gray-100">Chat</h1>
        <input
          type="text"
          value={repo}
          onChange={(e) => setRepo(e.target.value)}
          placeholder="Filter repo (e.g. owner/name)"
          className="ml-auto w-56 px-3 py-1.5 rounded-lg bg-gray-800 border border-gray-700
                     text-sm text-gray-300 placeholder-gray-600 focus:outline-none
                     focus:border-brand-500 transition-colors"
        />
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-6 py-6 space-y-8">
        {messages.length === 0 && (
          <div className="flex items-center justify-center h-full text-gray-600 text-sm">
            Ask anything about your codebase…
          </div>
        )}
        {messages.map((msg, i) => (
          <MessageBubble key={i} msg={msg} />
        ))}
        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div className="shrink-0 px-6 py-4 border-t border-gray-800">
        <div className="flex items-end gap-3 max-w-4xl mx-auto">
          <textarea
            rows={1}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                submit();
              }
            }}
            placeholder="Ask about your code, issues, or PRs… (Enter to send)"
            className="flex-1 resize-none px-4 py-3 rounded-xl bg-gray-800 border border-gray-700
                       text-sm text-gray-100 placeholder-gray-600 focus:outline-none
                       focus:border-brand-500 transition-colors leading-relaxed"
          />
          <button
            onClick={submit}
            disabled={loading || !input.trim()}
            className="shrink-0 p-3 rounded-xl bg-brand-500 hover:bg-brand-600 disabled:opacity-40
                       disabled:cursor-not-allowed transition-colors"
          >
            {loading ? (
              <Loader2 size={18} className="text-white animate-spin" />
            ) : (
              <Send size={18} className="text-white" />
            )}
          </button>
        </div>
      </div>
    </div>
  );
}
