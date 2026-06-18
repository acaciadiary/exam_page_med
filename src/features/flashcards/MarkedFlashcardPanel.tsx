import { Trash2 } from "lucide-react";
import { EmptyState } from "../../components/EmptyState";
import { getFlashcardStudyContent } from "../../lib/flashcards";
import { compactText } from "../../lib/text";
import type { ExamQuestion } from "../../types/exam";

type MarkedFlashcardPanelProps = {
  questions: ExamQuestion[];
  markedIds: string[];
  onClearMarked: () => void;
  onNavigate: (question: ExamQuestion) => void;
};

export function MarkedFlashcardPanel({
  questions,
  markedIds,
  onClearMarked,
  onNavigate,
}: MarkedFlashcardPanelProps) {
  const marked = questions.filter((question) => markedIds.includes(question.id));

  return (
    <aside className="rounded-[1.35rem] border border-white/80 bg-white/74 p-4 shadow-[0_18px_60px_rgba(181,133,117,0.16)] backdrop-blur-2xl">
      <div className="mb-4 flex items-start justify-between gap-3">
        <div>
          <p className="text-xs font-bold uppercase tracking-[0.22em] text-[#c4869b]">
            收藏閃卡
          </p>
          <p className="mt-1 text-sm text-[#725b52]">已收藏 {marked.length} 張</p>
        </div>
        {marked.length > 0 && (
          <button
            type="button"
            onClick={() => {
              if (!window.confirm("確定要清空本卷全部背卡收藏嗎？")) return;
              onClearMarked();
            }}
            className="inline-flex shrink-0 items-center gap-1.5 rounded-full border border-[#efd9d0] bg-white/72 px-3 py-2 text-xs font-semibold text-[#8d7167] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
            aria-label="一鍵清空收藏閃卡"
            title="一鍵清空收藏閃卡"
          >
            <Trash2 size={14} />
            一鍵清空
          </button>
        )}
      </div>

      {marked.length === 0 ? (
        <EmptyState
          title="尚未收藏閃卡"
          description="點閃卡右上角的收藏按鈕，即可把重點卡片集中在這裡。"
        />
      ) : (
        <div className="grid gap-2">
          {marked.map((question) => (
            <MarkedFlashcardLink
              key={question.id}
              question={question}
              onNavigate={onNavigate}
            />
          ))}
        </div>
      )}
    </aside>
  );
}

function MarkedFlashcardLink({
  question,
  onNavigate,
}: {
  question: ExamQuestion;
  onNavigate: (question: ExamQuestion) => void;
}) {
  const card = getFlashcardStudyContent(question);

  return (
    <button
      type="button"
      onClick={() => onNavigate(question)}
      className="rounded-[0.9rem] px-3 py-3 text-left text-sm leading-6 text-[#725b52] transition hover:bg-[#fff3f8] hover:text-[#4b3b35]"
    >
      <span className="font-semibold text-[#c4869b]">
        {question.question_number}.
      </span>{" "}
      {compactText(card.front, 70)}
    </button>
  );
}
