import { ChevronDown, ChevronUp, BookOpenCheck, Layers3 } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import clsx from "clsx";
import { CategoryFilter } from "../../components/CategoryFilter";
import type { useMarkedItems } from "../../hooks/useMarkedItems";
import {
  ALL_CATEGORIES,
  buildCategoryOptions,
  filterQuestionsByCategory,
} from "../../lib/categoryFilters";
import { getExamDisplayTitle } from "../../lib/examMetadata";
import type { AnswerOptionKey, AnswerState, ExamDataset, Mode } from "../../types/exam";
import type { StickyNoteItem } from "../../types/stickyNote";
import type { AppTheme } from "../../components/ThemeToggle";
import { MarkedQuestionSidebar } from "./MarkedQuestionSidebar";
import { QuestionCard } from "./QuestionCard";

type MarkedApi = ReturnType<typeof useMarkedItems>;

type ExamModeProps = {
  dataset: ExamDataset;
  answers: AnswerState;
  markedQuestions: MarkedApi;
  onAnswer: (questionId: string, answer: AnswerOptionKey) => void;
  mode: Mode;
  onModeChange: (mode: Mode) => void;
  theme: AppTheme;
  stickyNotes?: StickyNoteItem[];
  onAddQuestionNote?: (questionId: string, text: string) => void;
  onRemoveNote?: (id: string) => void;
  focusQuestionId?: string | null;
  onFocusComplete?: (questionId: string) => void;
  reviewMode?: {
    title: string;
    description: string;
    questionIds: string[];
    onExit: () => void;
  };
};

export function ExamMode({
  dataset,
  answers,
  markedQuestions,
  onAnswer,
  mode,
  onModeChange,
  theme,
  stickyNotes = [],
  onAddQuestionNote = () => undefined,
  onRemoveNote = () => undefined,
  focusQuestionId,
  onFocusComplete,
  reviewMode,
}: ExamModeProps) {
  const [activeCategory, setActiveCategory] = useState(ALL_CATEGORIES);
  const [visibleCount, setVisibleCount] = useState(15);
  const categoryOptions = useMemo(() => buildCategoryOptions(dataset), [dataset]);
  const visibleQuestions = useMemo(() => {
    const categoryQuestions = filterQuestionsByCategory(dataset, activeCategory);
    if (!reviewMode) return categoryQuestions;

    const reviewIdSet = new Set(reviewMode.questionIds);
    return categoryQuestions.filter((question) => reviewIdSet.has(question.id));
  }, [activeCategory, dataset, reviewMode]);
  const renderedQuestions = visibleQuestions.slice(0, visibleCount);
  const notesByQuestionId = useMemo(() => {
    const grouped = new Map<string, StickyNoteItem[]>();

    for (const note of stickyNotes) {
      if (!note.questionId || note.examId !== dataset.id) continue;
      grouped.set(note.questionId, [...(grouped.get(note.questionId) ?? []), note]);
    }

    return grouped;
  }, [dataset.id, stickyNotes]);

  const scrollToQuestion = (questionId: string) => {
    window.requestAnimationFrame(() => {
      window.requestAnimationFrame(() => {
        const target = document.getElementById(questionId);
        if (!target) return;

        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
        window.history.replaceState(null, "", `#${questionId}`);
      });
    });
  };

  const navigateToQuestion = (targetIndex: number) => {
    const target = visibleQuestions[targetIndex];
    if (!target) return;

    if (targetIndex >= visibleCount) {
      setVisibleCount(targetIndex + 1);
    }

    scrollToQuestion(target.id);
  };

  useEffect(() => {
    setActiveCategory(ALL_CATEGORIES);
    setVisibleCount(15);
  }, [dataset.id]);

  useEffect(() => {
    if (!focusQuestionId) return;

    const targetExists = dataset.questions.some((question) => question.id === focusQuestionId);
    if (!targetExists) return;

    const targetIndex = visibleQuestions.findIndex((question) => question.id === focusQuestionId);
    if (targetIndex === -1) {
      if (activeCategory !== ALL_CATEGORIES) {
        setActiveCategory(ALL_CATEGORIES);
      }
      return;
    }

    if (targetIndex >= visibleCount) {
      setVisibleCount(targetIndex + 1);
      return;
    }

    let cancelled = false;

    window.requestAnimationFrame(() => {
      window.requestAnimationFrame(() => {
        if (cancelled) return;

        const target = document.getElementById(focusQuestionId);
        if (!target) return;

        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
        window.history.replaceState(null, "", `#${focusQuestionId}`);
        onFocusComplete?.(focusQuestionId);
      });
    });

    return () => {
      cancelled = true;
    };
  }, [
    activeCategory,
    dataset.questions,
    focusQuestionId,
    onFocusComplete,
    visibleCount,
    visibleQuestions,
  ]);

  return (
    <div className="flex min-w-0 items-start gap-6">
      <section className="min-w-0 flex-1">
        <div className="mb-6 flex flex-col justify-between gap-4 sm:flex-row sm:items-end">
          <div>
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-[#c4869b]">
              [01] Exam notes / {dataset.year}
            </p>
            <h2 className="mt-3 text-3xl font-semibold tracking-normal text-[#4b3b35] dark:text-[#f8edf3]">
              {getExamDisplayTitle(dataset)}
            </h2>
            <p className="mt-3 max-w-2xl text-sm leading-7 text-[#725b52] dark:text-[#dccbd3]">
              做題後立即看解析，收藏重要題，錯題會自動整理到錯題本。
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

        {reviewMode && (
          <div className="mb-5 rounded-[1.2rem] border border-[#f2c9d8] bg-[#fff0f6]/88 p-4 shadow-[0_14px_42px_rgba(181,133,117,0.12)]">
            <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <div>
                <p className="text-sm font-semibold text-[#9a496b]">{reviewMode.title}</p>
                <p className="mt-1 text-sm leading-6 text-[#725b52]">{reviewMode.description}</p>
              </div>
              <button
                type="button"
                onClick={reviewMode.onExit}
                className="inline-flex h-10 items-center justify-center rounded-full border border-[#efd9d0] bg-white px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
              >
                離開練習
              </button>
            </div>
          </div>
        )}

        <CategoryFilter options={categoryOptions} activeCategory={activeCategory} onChange={setActiveCategory} />

        <div className="grid gap-5 sm:gap-6">
          {renderedQuestions.map((question, index) => (
            <QuestionCard
              key={question.id}
              question={question}
              selected={answers[question.id]}
              marked={markedQuestions.markedSet.has(question.id)}
              onAnswer={(answer) => onAnswer(question.id, answer)}
              onToggleMarked={() => markedQuestions.toggleMarked(question.id)}
              questionNotes={notesByQuestionId.get(question.id) ?? []}
              onAddNote={(text) => onAddQuestionNote(question.id, text)}
              onRemoveNote={onRemoveNote}
              positionLabel={`${index + 1} / ${visibleQuestions.length}`}
              onGoPrevious={index > 0 ? () => navigateToQuestion(index - 1) : undefined}
              onGoNext={
                index < visibleQuestions.length - 1
                  ? () => navigateToQuestion(index + 1)
                  : undefined
              }
              theme={theme}
            />
          ))}
        </div>

        {visibleQuestions.length > visibleCount && (
          <div className="mt-6 flex justify-center">
            <button
              type="button"
              onClick={() => setVisibleCount((prev) => prev + 15)}
              className="inline-flex h-12 items-center justify-center gap-2 rounded-xl border border-[#efd9d0] bg-white/80 px-6 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b] cursor-pointer shadow-sm font-hand"
            >
              載入更多題目 ({visibleQuestions.length - visibleCount} 待載入)
            </button>
          </div>
        )}

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
            <p className="text-xs font-bold uppercase tracking-[0.22em] text-[#c4869b]">收藏題目</p>
            <p className="mt-1 text-sm text-[#725b52]">目前收藏 {marked.length} 題</p>
          </div>
          {open ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
        </button>
      </div>

      {open && (
        <div className="mt-4 border-t border-[#f0ded6] pt-3">
          {marked.length === 0 ? (
            <div className="rounded-[1rem] border border-dashed border-[#efd9d0] bg-white/58 px-4 py-5 text-sm leading-6 text-[#8a7066]">
              尚未收藏題目。
            </div>
          ) : (
            <>
              <div className="mb-3 flex items-center justify-between gap-3">
                <p className="text-xs font-semibold tracking-[0.12em] text-[#8a7066]">點擊可回到題目</p>
                <button
                  type="button"
                  onClick={() => {
                    if (!window.confirm("確定清空本科收藏題目？")) return;
                    onClearMarked();
                  }}
                  className="rounded-full border border-[#efd9d0] bg-white/72 px-3 py-1.5 text-xs font-semibold text-[#8d7167] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
                >
                  清空
                </button>
              </div>
              <div className="grid gap-2">
                {marked.map((question) => (
                  <a
                    key={question.id}
                    href={`#${question.id}`}
                    className="rounded-[0.9rem] border border-transparent px-3 py-3 text-sm leading-6 text-[#725b52] transition hover:border-[#f2c9d8] hover:bg-[#fff3f8] hover:text-[#4b3b35]"
                  >
                    <span className="font-semibold text-[#c4869b]">{question.question_number}.</span>{" "}
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
