import { BadgeCheck, Lightbulb, Sparkles } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { randomEncouragement } from "../../lib/encouragements";
import { loadDiseaseComparisons } from "../../lib/loadExamData";
import { DiseaseComparison } from "./DiseaseComparison";
import type { ExamQuestion } from "../../types/exam";
import type { DiseaseComparisonGroup } from "../../types/disease";

type ExplanationPanelProps = {
  question: ExamQuestion;
};

export function ExplanationPanel({ question }: ExplanationPanelProps) {
  const [comparisons, setComparisons] = useState<DiseaseComparisonGroup[]>([]);

  useEffect(() => {
    loadDiseaseComparisons()
      .then((data) => {
        setComparisons(data.comparison_groups);
      })
      .catch((err) => {
        console.error("Failed to load disease comparisons", err);
      });
  }, []);

  const matchedGroups = useMemo(() => {
    if (!comparisons.length) return [];

    const matched: DiseaseComparisonGroup[] = [];
    const combinedText = `${question.question_text} ${Object.values(question.options).join(" ")} ${
      question.explanation || ""
    }`.toLowerCase();

    for (const group of comparisons) {
      // 1. Direct match by question ID
      const isDirectMatch = group.related_questions?.some(
        (rq) => rq.question_id === question.id
      );

      if (isDirectMatch) {
        matched.push(group);
        continue;
      }

      // 2. Keyword-based matching
      const hasMatch = group.diseases.some((disease) =>
        disease.aliases.some((alias) => {
          const normalizedAlias = alias.toLowerCase();
          return combinedText.includes(normalizedAlias);
        })
      );

      if (hasMatch) {
        matched.push(group);
      }
    }

    return matched;
  }, [comparisons, question]);

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
    <>
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

      {/* Disease Comparisons */}
      {matchedGroups.map((group) => (
        <DiseaseComparison
          key={group.id}
          group={group}
          currentQuestionId={question.id}
        />
      ))}
    </>
  );
}

