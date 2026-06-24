import { ChevronDown, ChevronUp, BookOpenCheck, Layers3 } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import clsx from "clsx";
import { CategoryFilter } from "../../components/CategoryFilter";
import type { useMarkedItems } from "../../hooks/useMarkedItems";
import {
  ALL_CATEGORIES,
  buildCategoryOptions,
  filterQuestionsByCategory,
  getDerivedQuestionCategory,
} from "../../lib/categoryFilters";
import type { ExamDataset, ExamQuestion, Mode } from "../../types/exam";
import type { AppTheme } from "../../components/ThemeToggle";
import { Flashcard } from "./Flashcard";
import { MarkedFlashcardPanel } from "./MarkedFlashcardPanel";

type MarkedApi = ReturnType<typeof useMarkedItems>;

type FlashcardModeProps = {
  dataset: ExamDataset;
  markedFlashcards: MarkedApi;
  mode: Mode;
  onModeChange: (mode: Mode) => void;
  theme: AppTheme;
};

export function FlashcardMode({
  dataset,
  markedFlashcards,
  mode,
  onModeChange,
  theme,
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
    <div className="grid min-w-0 gap-6 lg:grid-cols-[minmax(0,1fr)_20rem]">
      <section className="min-w-0">
        <div className="mb-6 flex flex-col justify-between gap-4 sm:flex-row sm:items-end">
          <div>
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-[#c4869b]">
              [02] Flashcard corner / {dataset.year}
            </p>
            <h2 className="mt-3 text-3xl font-semibold tracking-normal text-[#4b3b35] dark:text-[#f8edf3]">
              閃卡速記
            </h2>
            <p className="mt-3 max-w-2xl text-sm leading-7 text-[#725b52] dark:text-[#dccbd3]">
              用同一組科目分類練習重點提示。點整張卡片即可翻面，收藏清單也能直接帶你跳回對應分類。
            </p>
          </div>

          {/* Mode Switcher */}
          <div className={clsx(
            "inline-flex h-11 rounded-[0.85rem] p-1 border backdrop-blur-xl shrink-0 self-start sm:self-auto",
            theme === "dark"
              ? "bg-[#2b2430]/80 border-white/12"
              : theme === "clinical"
              ? "bg-white/86 border-[#a3bed0]/45"
              : "bg-white/80 border-[#e6d6c9]"
          )}>
            <button
              type="button"
              onClick={() => onModeChange("exam")}
              className={clsx(
                "inline-flex min-h-9 min-w-24 items-center justify-center gap-2 rounded-[0.7rem] px-3 text-sm font-semibold transition cursor-pointer",
                mode === "exam"
                  ? theme === "dark"
                    ? "bg-[#4a2c3a] text-[#f3a6c4] shadow-sm"
                    : theme === "clinical"
                    ? "bg-[#dbeafe] text-[#1f4e79] shadow-sm"
                    : "bg-[#dce8dc] text-[#405d49] shadow-sm"
                  : theme === "dark"
                  ? "text-[#dccbd3] hover:bg-[#2b2430] hover:text-[#f3a6c4]"
                  : theme === "clinical"
                  ? "text-[#26384a] hover:bg-[#e8f2f9] hover:text-[#1f4e79]"
                  : "text-[#806b60] hover:bg-white hover:text-[#3f342d]"
              )}
            >
              <BookOpenCheck size={16} />
              題目模式
            </button>
            <button
              type="button"
              onClick={() => onModeChange("flashcards")}
              className={clsx(
                "inline-flex min-h-9 min-w-24 items-center justify-center gap-2 rounded-[0.7rem] px-3 text-sm font-semibold transition cursor-pointer",
                mode === "flashcards"
                  ? theme === "dark"
                    ? "bg-[#4a2c3a] text-[#f3a6c4] shadow-sm"
                    : theme === "clinical"
                    ? "bg-[#dbeafe] text-[#1f4e79] shadow-sm"
                    : "bg-[#dce8dc] text-[#405d49] shadow-sm"
                  : theme === "dark"
                  ? "text-[#dccbd3] hover:bg-[#2b2430] hover:text-[#f3a6c4]"
                  : theme === "clinical"
                  ? "text-[#26384a] hover:bg-[#e8f2f9] hover:text-[#1f4e79]"
                  : "text-[#806b60] hover:bg-white hover:text-[#3f342d]"
              )}
            >
              <Layers3 size={16} />
              卡片模式
            </button>
          </div>
        </div>

        <CategoryFilter
          options={categoryOptions}
          activeCategory={activeCategory}
          onChange={setActiveCategory}
        />

        <div className="grid min-w-0 gap-5 md:grid-cols-2">
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
                  onClick={() => {
                    if (!window.confirm("確定要清空本卷全部背卡收藏嗎？")) return;
                    onClearMarked();
                  }}
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
