import { BadgeCheck, Lightbulb, Sparkles } from "lucide-react";
import { useMemo } from "react";
import { randomEncouragement } from "../../lib/encouragements";
import type { ExamQuestion } from "../../types/exam";

type ExplanationPanelProps = {
  question: ExamQuestion;
};

export function ExplanationPanel({ question }: ExplanationPanelProps) {
  const explanation =
    question.explanation ||
    "這題尚未匯入詳解。之後可透過 Gemini 手動批次流程產生，並保留人工複查狀態。";
  const keyPoint = question.key_point || "考點提示尚未建立。";
  const summary =
    question.flashcard_summary ||
    "閃卡摘要尚未建立：之後會整理成「關鍵字 -> 選什麼」的一句話。";
  const status = question.review_status || (question.explanation ? "ai_generated" : "empty");
  const encouragement = useMemo(() => randomEncouragement(), [question.id]);
  const statusText =
    status === "reviewed"
      ? "已人工複查"
      : status === "ai_generated"
        ? encouragement
        : "待補詳解";

  return (
    <div className="mt-6 rounded-[1.1rem] border border-[#d8eadf] bg-[#effaf5]/82 p-5 shadow-sm">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-2 text-sm font-semibold text-[#4c806e]">
          <Lightbulb size={17} />
          詳解與考點提示
        </div>
        <span className="inline-flex items-center gap-1.5 rounded-full border border-[#d8eadf] bg-white/70 px-3 py-1 text-xs font-semibold text-[#4c806e]">
          {status === "reviewed" ? <BadgeCheck size={14} /> : <Sparkles size={14} />}
          {statusText}
        </span>
      </div>
      <div className="mt-4 rounded-[0.9rem] border border-[#d8eadf] bg-white/64 px-4 py-3 text-sm font-semibold leading-6 text-[#4c806e]">
        {keyPoint}
      </div>
      <p className="mt-3 whitespace-pre-line text-sm leading-7 text-[#604b43]">{explanation}</p>
      <div className="mt-4 rounded-[0.9rem] border border-[#f2d7a9] bg-[#fff8df] px-4 py-3 text-sm font-semibold text-[#7a6040]">
        {summary}
      </div>
    </div>
  );
}
