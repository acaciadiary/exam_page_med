import {
  BookmarkCheck,
  PanelRightClose,
  PanelRightOpen,
  Trash2,
} from "lucide-react";
import { useState } from "react";
import clsx from "clsx";
import { EmptyState } from "../../components/EmptyState";
import { compactText } from "../../lib/text";
import type { ExamQuestion } from "../../types/exam";

type MarkedQuestionSidebarProps = {
  questions: ExamQuestion[];
  markedIds: string[];
  onClearMarked: () => void;
};

export function MarkedQuestionSidebar({
  questions,
  markedIds,
  onClearMarked,
}: MarkedQuestionSidebarProps) {
  const [collapsed, setCollapsed] = useState(true);
  const marked = questions.filter((question) => markedIds.includes(question.id));

  return (
    <aside
      className={clsx(
        "sticky top-32 hidden max-h-[calc(100vh-9rem)] shrink-0 overflow-hidden rounded-[1.35rem] border border-white/80 bg-white/74 shadow-[0_18px_60px_rgba(181,133,117,0.16)] backdrop-blur-2xl transition-all lg:block",
        collapsed ? "w-16" : "w-80",
      )}
    >
      <div className="flex items-start justify-between gap-3 border-b border-[#f0ded6] p-4">
        {!collapsed && (
          <div className="font-hand">
            <p className="text-xs font-bold uppercase tracking-[0.22em] text-[#c4869b]">
              收藏題目
            </p>
            <p className="mt-1 text-sm text-[#725b52]">
              目前已收藏 {marked.length} 題
            </p>
          </div>
        )}
        <div className="font-hand flex items-center gap-1">
          {!collapsed && marked.length > 0 && (
            <button
              type="button"
              onClick={() => {
                if (!window.confirm("確定要清除本卷全部題目收藏嗎？")) return;
                onClearMarked();
              }}
              className="inline-flex items-center gap-1.5 rounded-full border border-[#efd9d0] bg-white/72 px-3 py-2 text-xs font-semibold text-[#8d7167] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
              aria-label="清除所有收藏"
              title="清除所有收藏"
            >
              <Trash2 size={14} />
              清除收藏
            </button>
          )}
          <button
            type="button"
            aria-label={collapsed ? "展開收藏欄" : "收合收藏欄"}
            title={collapsed ? "展開收藏欄" : "收合收藏欄"}
            onClick={() => setCollapsed((value) => !value)}
            className="rounded-full p-2 text-[#8d7167] transition hover:bg-[#fff0f6] hover:text-[#9a496b]"
          >
            {collapsed ? <PanelRightOpen size={18} /> : <PanelRightClose size={18} />}
          </button>
        </div>
      </div>

      {collapsed ? (
        <div className="flex justify-center py-5 text-[#c4869b]">
          <BookmarkCheck size={20} />
        </div>
      ) : (
        <div className="max-h-[calc(100vh-13rem)] overflow-y-auto p-3">
          {marked.length === 0 ? (
            <EmptyState
              title="還沒有收藏題目"
              description="點題目右上角的收藏按鈕，即可把想複習的題目集中在這裡。"
            />
          ) : (
            <div className="grid gap-2">
              {marked.map((question) => (
                <a
                  key={question.id}
                  href={`#${question.id}`}
                  className="rounded-[0.9rem] border border-transparent px-3 py-3 text-sm leading-6 text-[#725b52] transition hover:border-[#f2c9d8] hover:bg-[#fff3f8] hover:text-[#4b3b35]"
                >
                  <span className="font-semibold text-[#c4869b]">
                    {question.question_number}.
                  </span>{" "}
                  {compactText(question.question_text, 72)}
                </a>
              ))}
            </div>
          )}
        </div>
      )}
    </aside>
  );
}
