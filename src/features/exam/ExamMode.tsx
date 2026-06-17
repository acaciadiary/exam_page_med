import { ChevronDown, ChevronUp } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { CategoryFilter } from "../../components/CategoryFilter";
import type { useMarkedItems } from "../../hooks/useMarkedItems";
import {
  ALL_CATEGORIES,
  buildCategoryOptions,
  filterQuestionsByCategory,
} from "../../lib/categoryFilters";
import type { AnswerOptionKey, AnswerState, ExamDataset } from "../../types/exam";
import { MarkedQuestionSidebar } from "./MarkedQuestionSidebar";
import { QuestionCard } from "./QuestionCard";

type MarkedApi = ReturnType<typeof useMarkedItems>;

type ExamModeProps = {
  dataset: ExamDataset;
  answers: AnswerState;
  markedQuestions: MarkedApi;
  onAnswer: (questionId: string, answer: AnswerOptionKey) => void;
};

export function ExamMode({
  dataset,
  answers,
  markedQuestions,
  onAnswer,
}: ExamModeProps) {
  const [activeCategory, setActiveCategory] = useState(ALL_CATEGORIES);
  const categoryOptions = useMemo(() => buildCategoryOptions(dataset), [dataset]);
  const visibleQuestions = useMemo(
    () => filterQuestionsByCategory(dataset, activeCategory),
    [activeCategory, dataset],
  );

  useEffect(() => {
    setActiveCategory(ALL_CATEGORIES);
  }, [dataset.id]);

  return (
    <div className="flex min-w-0 items-start gap-6">
      <section className="min-w-0 flex-1">
        <div className="mb-6">
          <p className="text-xs font-bold uppercase tracking-[0.24em] text-[#c4869b]">
            [01] Exam notes / {dataset.year}
          </p>
          <h2 className="mt-3 text-3xl font-semibold tracking-normal text-[#4b3b35]">
            {dataset.title}
          </h2>
          <p className="mt-3 max-w-2xl text-sm leading-7 text-[#725b52]">
            依科目快速篩題，作答後立即顯示正誤、詳解與考點提示。收藏的題目會自動保存，下次回來繼續複習。
          </p>
        </div>

        <CategoryFilter
          options={categoryOptions}
          activeCategory={activeCategory}
          onChange={setActiveCategory}
        />

        <div className="grid gap-5">
          {visibleQuestions.map((question) => (
            <QuestionCard
              key={question.id}
              question={question}
              selected={answers[question.id]}
              marked={markedQuestions.markedSet.has(question.id)}
              onAnswer={(answer) => onAnswer(question.id, answer)}
              onToggleMarked={() => markedQuestions.toggleMarked(question.id)}
            />
          ))}
        </div>

        <MobileMarkedQuestions
          questions={dataset.questions}
          markedIds={markedQuestions.marked}
          onClearMarked={markedQuestions.clearMarked}
        />
      </section>

      <MarkedQuestionSidebar
        questions={dataset.questions}
        markedIds={markedQuestions.marked}
        onClearMarked={markedQuestions.clearMarked}
      />
    </div>
  );
}

function MobileMarkedQuestions({
  questions,
  markedIds,
  onClearMarked,
}: {
  questions: ExamDataset["questions"];
  markedIds: string[];
  onClearMarked: () => void;
}) {
  const [open, setOpen] = useState(false);
  const marked = questions.filter((question) => markedIds.includes(question.id));

  return (
    <aside className="mt-6 rounded-[1.2rem] border border-white/80 bg-white/78 p-4 shadow-[0_14px_42px_rgba(181,133,117,0.14)] backdrop-blur-2xl lg:hidden">
      <div className="flex items-start justify-between gap-3">
        <button
          type="button"
          onClick={() => setOpen((value) => !value)}
          className="flex min-w-0 flex-1 items-center justify-between gap-3 text-left"
        >
          <div>
            <p className="text-xs font-bold uppercase tracking-[0.22em] text-[#c4869b]">
              收藏題目
            </p>
            <p className="mt-1 text-sm text-[#725b52]">
              目前已收藏 {marked.length} 題
            </p>
          </div>
          {open ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
        </button>
      </div>

      {open && (
        <div className="mt-4 border-t border-[#f0ded6] pt-3">
          {marked.length === 0 ? (
            <div className="rounded-[1rem] border border-dashed border-[#efd9d0] bg-white/58 px-4 py-5 text-sm leading-6 text-[#8a7066]">
              還沒有收藏題目。把想回頭複習的題目標記起來，之後就能快速查看。
            </div>
          ) : (
            <>
              <div className="mb-3 flex items-center justify-between gap-3">
                <p className="text-xs font-semibold tracking-[0.12em] text-[#8a7066]">
                  點題目可回到原本位置
                </p>
                <button
                  type="button"
                  onClick={onClearMarked}
                  className="rounded-full border border-[#efd9d0] bg-white/72 px-3 py-1.5 text-xs font-semibold text-[#8d7167] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
                >
                  清除收藏
                </button>
              </div>
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
                    {question.question_text}
                  </a>
                ))}
              </div>
            </>
          )}
        </div>
      )}
    </aside>
  );
}
