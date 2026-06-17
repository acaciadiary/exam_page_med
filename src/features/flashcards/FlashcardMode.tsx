import { ChevronDown, ChevronUp } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { CategoryFilter } from "../../components/CategoryFilter";
import type { useMarkedItems } from "../../hooks/useMarkedItems";
import {
  ALL_CATEGORIES,
  buildCategoryOptions,
  filterQuestionsByCategory,
  getDerivedQuestionCategory,
} from "../../lib/categoryFilters";
import type { ExamDataset, ExamQuestion } from "../../types/exam";
import { Flashcard } from "./Flashcard";
import { MarkedFlashcardPanel } from "./MarkedFlashcardPanel";

type MarkedApi = ReturnType<typeof useMarkedItems>;

type FlashcardModeProps = {
  dataset: ExamDataset;
  markedFlashcards: MarkedApi;
};

export function FlashcardMode({
  dataset,
  markedFlashcards,
}: FlashcardModeProps) {
  const [activeCategory, setActiveCategory] = useState(ALL_CATEGORIES);
  const [pendingFlashcardId, setPendingFlashcardId] = useState<string | null>(null);
  const categoryOptions = useMemo(() => buildCategoryOptions(dataset), [dataset]);
  const visibleQuestions = useMemo(
    () => filterQuestionsByCategory(dataset, activeCategory),
    [activeCategory, dataset],
  );

  useEffect(() => {
    setActiveCategory(ALL_CATEGORIES);
  }, [dataset.id]);

  useEffect(() => {
    if (!pendingFlashcardId) return;

    const frameId = window.requestAnimationFrame(() => {
      const target = document.getElementById(`flashcard-${pendingFlashcardId}`);
      if (!target) return;

      target.scrollIntoView({ behavior: "smooth", block: "start" });
      window.location.hash = `flashcard-${pendingFlashcardId}`;
      setPendingFlashcardId(null);
    });

    return () => window.cancelAnimationFrame(frameId);
  }, [pendingFlashcardId, visibleQuestions]);

  const handleNavigateToFlashcard = (question: ExamQuestion) => {
    setPendingFlashcardId(question.id);
    setActiveCategory(getDerivedQuestionCategory(dataset, question) || ALL_CATEGORIES);
  };

  return (
    <div className="grid gap-6 lg:grid-cols-[1fr_20rem]">
      <section>
        <div className="mb-6">
          <p className="text-xs font-bold uppercase tracking-[0.24em] text-[#c4869b]">
            [02] Flashcard corner / {dataset.year}
          </p>
          <h2 className="mt-3 text-3xl font-semibold tracking-normal text-[#4b3b35]">
            閃卡速記
          </h2>
          <p className="mt-3 max-w-2xl text-sm leading-7 text-[#725b52]">
            用同一組科目分類練習重點提示。點整張卡片即可翻面，收藏清單也能直接帶你跳回對應分類。
          </p>
        </div>

        <CategoryFilter
          options={categoryOptions}
          activeCategory={activeCategory}
          onChange={setActiveCategory}
        />

        <div className="grid gap-5 md:grid-cols-2">
          {visibleQuestions.map((question) => (
            <div id={`flashcard-${question.id}`} key={question.id}>
              <Flashcard
                question={question}
                marked={markedFlashcards.markedSet.has(question.id)}
                onToggleMarked={() => markedFlashcards.toggleMarked(question.id)}
              />
            </div>
          ))}
        </div>

        <MobileMarkedFlashcards
          questions={dataset.questions}
          markedIds={markedFlashcards.marked}
          onClearMarked={markedFlashcards.clearMarked}
          onNavigate={handleNavigateToFlashcard}
        />
      </section>

      <div className="lg:sticky lg:top-32 lg:self-start">
        <MarkedFlashcardPanel
          questions={dataset.questions}
          markedIds={markedFlashcards.marked}
          onClearMarked={markedFlashcards.clearMarked}
          onNavigate={handleNavigateToFlashcard}
        />
      </div>
    </div>
  );
}

function MobileMarkedFlashcards({
  questions,
  markedIds,
  onClearMarked,
  onNavigate,
}: {
  questions: ExamDataset["questions"];
  markedIds: string[];
  onClearMarked: () => void;
  onNavigate: (question: ExamQuestion) => void;
}) {
  const [open, setOpen] = useState(false);
  const marked = questions.filter((question) => markedIds.includes(question.id));

  return (
    <aside className="mt-6 rounded-[1.2rem] border border-white/80 bg-white/78 p-4 shadow-[0_14px_42px_rgba(181,133,117,0.14)] backdrop-blur-2xl lg:hidden">
      <button
        type="button"
        onClick={() => setOpen((value) => !value)}
        className="flex w-full items-center justify-between gap-3 text-left"
      >
        <div>
          <p className="text-xs font-bold uppercase tracking-[0.22em] text-[#c4869b]">
            收藏閃卡
          </p>
          <p className="mt-1 text-sm text-[#725b52]">已收藏 {marked.length} 張</p>
        </div>
        {open ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
      </button>

      {open && (
        <div className="mt-4 border-t border-[#f0ded6] pt-3">
          {marked.length === 0 ? (
            <div className="rounded-[1rem] border border-dashed border-[#efd9d0] bg-white/58 px-4 py-5 text-sm leading-6 text-[#8a7066]">
              目前還沒有收藏閃卡，點卡片上的收藏按鈕就會出現在這裡。
            </div>
          ) : (
            <>
              <div className="mb-3 flex items-center justify-between gap-3">
                <p className="text-xs font-semibold tracking-[0.12em] text-[#8a7066]">
                  點一下就能切到對應分類
                </p>
                <button
                  type="button"
                  onClick={onClearMarked}
                  className="rounded-full border border-[#efd9d0] bg-white/72 px-3 py-1.5 text-xs font-semibold text-[#8d7167] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
                >
                  清空收藏
                </button>
              </div>
              <div className="grid gap-2">
                {marked.map((question) => (
                  <button
                    key={question.id}
                    type="button"
                    onClick={() => {
                      setOpen(false);
                      onNavigate(question);
                    }}
                    className="rounded-[0.9rem] border border-transparent px-3 py-3 text-left text-sm leading-6 text-[#725b52] transition hover:border-[#f2c9d8] hover:bg-[#fff3f8] hover:text-[#4b3b35]"
                  >
                    <span className="font-semibold text-[#c4869b]">
                      {question.question_number}.
                    </span>{" "}
                    {question.question_text}
                  </button>
                ))}
              </div>
            </>
          )}
        </div>
      )}
    </aside>
  );
}
