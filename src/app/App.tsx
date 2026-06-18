import { useEffect, useMemo, useRef, useState } from "react";
import { AnimatePresence, motion } from "motion/react";
import { AlertCircle } from "lucide-react";
import { AppShell } from "../components/AppShell";
import { EmptyState } from "../components/EmptyState";
import { ExamMode } from "../features/exam/ExamMode";
import {
  FavoritesPage,
  type FavoriteEntry,
  type FavoriteTag,
} from "../features/favorites/FavoritesPage";
import { FlashcardMode } from "../features/flashcards/FlashcardMode";
import {
  MistakeNotebookPage,
  type MistakeEntry,
} from "../features/mistakes/MistakeNotebookPage";
import { StickyNotesPage } from "../features/notes/StickyNotesPage";
import { useExamProgress } from "../hooks/useExamProgress";
import { useLocalStorage } from "../hooks/useLocalStorage";
import { useMarkedItems } from "../hooks/useMarkedItems";
import { loadExamData, loadManifest } from "../lib/loadExamData";
import { storageKeys } from "../lib/storageKeys";
import { isAcceptedAnswer } from "../lib/text";
import { buildSearchForPage, readPageFromSearch, type AppPage } from "./routes";
import type { AnswerState, ExamDataset, ExamManifest, Mode } from "../types/exam";
import type { StickyNoteItem } from "../types/stickyNote";

type LoadState =
  | { status: "loading" }
  | { status: "ready"; manifest: ExamManifest; dataset: ExamDataset }
  | { status: "error"; message: string };

export default function App() {
  const [page, setPage] = useState<AppPage>(() =>
    readPageFromSearch(window.location.search),
  );
  const [theme, setTheme] = useLocalStorage<"light" | "dark">(
    storageKeys.theme,
    "light",
  );
  const [mode, setMode] = useLocalStorage<Mode>(storageKeys.activeMode, "exam");
  const [activeExamId, setActiveExamId] = useLocalStorage<string>(
    storageKeys.activeExam,
    "",
  );
  const [state, setState] = useState<LoadState>({ status: "loading" });
  const [isDatasetLoading, setIsDatasetLoading] = useState(false);
  const loadRequestIdRef = useRef(0);
  const [pendingQuestion, setPendingQuestion] = useState<{
    examId: string;
    questionId: string;
  } | null>(null);
  const [allMistakes, setAllMistakes] = useState<MistakeEntry[]>([]);
  const [isMistakesLoading, setIsMistakesLoading] = useState(false);
  const [favorites, setFavorites] = useState<FavoriteEntry[]>([]);
  const [isFavoritesLoading, setIsFavoritesLoading] = useState(false);
  const [mistakePracticeIds, setMistakePracticeIds] = useState<Record<string, string[]>>({});
  const [stickyNotes, setStickyNotes] = useLocalStorage<StickyNoteItem[]>(
    storageKeys.stickyNotes,
    [],
  );

  useEffect(() => {
    document.documentElement.classList.toggle("dark", theme === "dark");
  }, [theme]);

  useEffect(() => {
    const handlePopState = () => {
      setPage(readPageFromSearch(window.location.search));
    };

    window.addEventListener("popstate", handlePopState);
    return () => window.removeEventListener("popstate", handlePopState);
  }, []);

  useEffect(() => {
    let cancelled = false;
    const requestId = ++loadRequestIdRef.current;

    async function load() {
      try {
        setIsDatasetLoading(true);
        setState((current) =>
          current.status === "ready" ? current : { status: "loading" },
        );

        const manifest = await loadManifest();
        const activeExamExists = manifest.exams.some(
          (exam) => exam.id === activeExamId,
        );
        const selected =
          manifest.exams.find((exam) => exam.id === activeExamId) ??
          manifest.exams[0];

        if (!selected) {
          throw new Error("目前找不到任何考卷資料。");
        }

        if ((!activeExamId || !activeExamExists) && selected.id !== activeExamId) {
          setActiveExamId(selected.id);
        }

        const dataset = await loadExamData(selected.path);

        if (!cancelled && requestId === loadRequestIdRef.current) {
          setState({ status: "ready", manifest, dataset });
          setIsDatasetLoading(false);
        }
      } catch (error) {
        if (!cancelled && requestId === loadRequestIdRef.current) {
          setIsDatasetLoading(false);
          setState({
            status: "error",
            message: error instanceof Error ? error.message : "載入考卷時發生錯誤。",
          });
        }
      }
    }

    load();

    return () => {
      cancelled = true;
    };
  }, [activeExamId, setActiveExamId]);

  const readyDataset = state.status === "ready" ? state.dataset : null;
  const examId = readyDataset?.id ?? "pending";
  const { answers, answerQuestion, removeAnswers, resetAnswers } = useExamProgress(
    storageKeys.answers(examId),
  );
  const markedQuestions = useMarkedItems(storageKeys.markedQuestions(examId));
  const markedFlashcards = useMarkedItems(storageKeys.markedFlashcards(examId));
  const [favoriteTags, setFavoriteTags] = useLocalStorage<Record<string, FavoriteTag[]>>(
    storageKeys.favoriteTags(examId),
    {},
  );

  const answeredCount = useMemo(() => Object.keys(answers).length, [answers]);

  useEffect(() => {
    if (state.status !== "ready") return undefined;

    let cancelled = false;
    const manifest = state.manifest;
    const currentDataset = state.dataset;

    async function collectMistakes() {
      setIsMistakesLoading(true);

      const entries: MistakeEntry[] = [];

      for (const exam of manifest.exams) {
        const examAnswers =
          exam.id === examId ? answers : readStoredAnswers(exam.id);

        if (Object.keys(examAnswers).length === 0) {
          continue;
        }

        const dataset =
          currentDataset.id === exam.id
            ? currentDataset
            : await loadExamData(exam.path);

        for (const question of dataset.questions) {
          const selectedAnswer = examAnswers[question.id];

          if (selectedAnswer && !isAcceptedAnswer(selectedAnswer, question)) {
            entries.push({ exam, question, selectedAnswer });
          }
        }
      }

      if (!cancelled) {
        setAllMistakes(entries);
        setIsMistakesLoading(false);
      }
    }

    collectMistakes().catch(() => {
      if (!cancelled) {
        setAllMistakes([]);
        setIsMistakesLoading(false);
      }
    });

    return () => {
      cancelled = true;
    };
  }, [answers, examId, readyDataset, state]);

  useEffect(() => {
    if (state.status !== "ready") return undefined;

    let cancelled = false;
    const manifest = state.manifest;
    const currentDataset = state.dataset;

    async function collectFavorites() {
      setIsFavoritesLoading(true);

      const entries: FavoriteEntry[] = [];

      for (const exam of manifest.exams) {
        const markedQuestionIds =
          exam.id === examId
            ? markedQuestions.marked
            : readStoredStringArray(storageKeys.markedQuestions(exam.id));
        const markedFlashcardIds =
          exam.id === examId
            ? markedFlashcards.marked
            : readStoredStringArray(storageKeys.markedFlashcards(exam.id));
        const examFavoriteTags =
          exam.id === examId
            ? favoriteTags
            : readStoredFavoriteTags(storageKeys.favoriteTags(exam.id));
        const favoriteIds = Array.from(
          new Set([...markedQuestionIds, ...markedFlashcardIds]),
        );

        if (favoriteIds.length === 0) continue;

        const dataset =
          currentDataset.id === exam.id
            ? currentDataset
            : await loadExamData(exam.path);

        for (const question of dataset.questions) {
          if (!favoriteIds.includes(question.id)) continue;

          const inQuestions = markedQuestionIds.includes(question.id);
          const inFlashcards = markedFlashcardIds.includes(question.id);

          entries.push({
            exam,
            question,
            source: inQuestions && inFlashcards ? "both" : inQuestions ? "question" : "flashcard",
            tags: examFavoriteTags[question.id] ?? [],
          });
        }
      }

      if (!cancelled) {
        setFavorites(entries);
        setIsFavoritesLoading(false);
      }
    }

    collectFavorites().catch(() => {
      if (!cancelled) {
        setFavorites([]);
        setIsFavoritesLoading(false);
      }
    });

    return () => {
      cancelled = true;
    };
  }, [examId, favoriteTags, markedFlashcards.marked, markedQuestions.marked, state]);

  useEffect(() => {
    if (page !== "exam" || !pendingQuestion || readyDataset?.id !== pendingQuestion.examId) {
      return undefined;
    }

    const frameId = window.requestAnimationFrame(() => {
      const target = document.getElementById(pendingQuestion.questionId);
      if (target) {
        target.scrollIntoView({ behavior: "smooth", block: "start" });
        window.location.hash = pendingQuestion.questionId;
        setPendingQuestion(null);
      }
    });

    return () => window.cancelAnimationFrame(frameId);
  }, [page, pendingQuestion, readyDataset?.id]);

  const handlePageChange = (nextPage: AppPage) => {
    if (nextPage === page) return;

    const nextSearch = buildSearchForPage(nextPage, window.location.search);
    const nextUrl = `${window.location.pathname}${nextSearch}`;
    window.history.pushState({}, "", nextUrl);
    setPage(nextPage);
  };

  const handleAddNote = (text: string) => {
    setStickyNotes((current) => [
      {
        id: `${Date.now()}-${Math.random().toString(36).slice(2)}`,
        text,
        createdAt: new Date().toISOString(),
      },
      ...current,
    ]);
  };

  const handleRemoveNote = (id: string) => {
    setStickyNotes((current) => current.filter((note) => note.id !== id));
  };

  const handleClearNotes = () => {
    if (!window.confirm("確定要清空全部便利貼嗎？這個動作無法復原。")) return;
    setStickyNotes([]);
  };

  const handleClearAllMistakes = () => {
    if (state.status !== "ready" || allMistakes.length === 0) return;
    if (!window.confirm("確定要清空目前所有錯題紀錄嗎？答錯紀錄會從錯題本移除。")) return;

    const mistakeIdsByExam = new Map<string, string[]>();

    for (const mistake of allMistakes) {
      mistakeIdsByExam.set(mistake.exam.id, [
        ...(mistakeIdsByExam.get(mistake.exam.id) ?? []),
        mistake.question.id,
      ]);
    }

    for (const [targetExamId, questionIds] of mistakeIdsByExam) {
      if (targetExamId === examId) {
        removeAnswers(questionIds);
        continue;
      }

      const storedAnswers = readStoredAnswers(targetExamId);
      for (const questionId of questionIds) {
        delete storedAnswers[questionId];
      }
      writeStoredAnswers(targetExamId, storedAnswers);
    }

    setAllMistakes([]);
    setMistakePracticeIds({});
  };

  const handleClearAllFavorites = () => {
    if (state.status !== "ready" || favorites.length === 0) return;
    if (!window.confirm("確定要清空全部收藏嗎？題目收藏與背卡收藏都會移除。")) return;

    for (const exam of state.manifest.exams) {
      if (exam.id === examId) {
        markedQuestions.clearMarked();
        markedFlashcards.clearMarked();
        setFavoriteTags({});
        continue;
      }

      writeStoredStringArray(storageKeys.markedQuestions(exam.id), []);
      writeStoredStringArray(storageKeys.markedFlashcards(exam.id), []);
      writeStoredFavoriteTags(storageKeys.favoriteTags(exam.id), {});
    }

    setFavorites([]);
  };

  const handleStartMistakePractice = () => {
    if (allMistakes.length === 0) return;

    const idsByExam: Record<string, string[]> = {};
    for (const mistake of allMistakes) {
      idsByExam[mistake.exam.id] = [
        ...(idsByExam[mistake.exam.id] ?? []),
        mistake.question.id,
      ];
    }

    const firstMistake = allMistakes[0];
    setMistakePracticeIds(idsByExam);
    setMode("exam");
    setActiveExamId(firstMistake.exam.id);
    handlePageChange("exam");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleToggleFavoriteTag = (
    targetExamId: string,
    questionId: string,
    tag: FavoriteTag,
  ) => {
    const toggleTags = (current: Record<string, FavoriteTag[]>) => {
      const currentTags = current[questionId] ?? [];
      const nextTags = currentTags.includes(tag)
        ? currentTags.filter((item) => item !== tag)
        : [...currentTags, tag];
      const next = { ...current };

      if (nextTags.length === 0) {
        delete next[questionId];
      } else {
        next[questionId] = nextTags;
      }

      return next;
    };

    if (targetExamId === examId) {
      setFavoriteTags(toggleTags);
    } else {
      writeStoredFavoriteTags(
        storageKeys.favoriteTags(targetExamId),
        toggleTags(readStoredFavoriteTags(storageKeys.favoriteTags(targetExamId))),
      );
    }

    setFavorites((current) =>
      current.map((entry) =>
        entry.exam.id === targetExamId && entry.question.id === questionId
          ? { ...entry, tags: toggleTags({ [questionId]: entry.tags })[questionId] ?? [] }
          : entry,
      ),
    );
  };

  if (state.status === "loading") {
    return (
      <div className="grid min-h-screen place-items-center bg-[#fff8f4] px-6 text-[#4b3b35]">
        <div className="rounded-[1.5rem] border border-white/80 bg-white/72 px-8 py-7 text-center shadow-[0_18px_60px_rgba(181,133,117,0.18)] backdrop-blur-2xl">
          <div className="mx-auto h-12 w-12 animate-spin rounded-full border-2 border-[#f6a9c6] border-t-transparent" />
          <p className="mt-5 text-sm font-semibold tracking-[0.16em] text-[#9c7b70]">
            正在載入考卷資料...
          </p>
        </div>
      </div>
    );
  }

  if (state.status === "error") {
    return (
      <div className="grid min-h-screen place-items-center bg-slate-950 px-6 text-white">
        <div className="max-w-md rounded-lg border border-red-300/30 bg-red-500/10 p-6">
          <AlertCircle className="text-red-200" />
          <h1 className="mt-4 text-xl font-semibold">考卷載入失敗</h1>
          <p className="mt-2 text-sm leading-6 text-red-100/80">
            {state.message}
          </p>
        </div>
      </div>
    );
  }

  const { manifest, dataset } = state;

  return (
    <AppShell
      exams={manifest.exams}
      activeExamId={dataset.id}
      page={page}
      mode={mode}
      theme={theme}
      answeredCount={answeredCount}
      questionCount={dataset.questions.length}
      wrongQuestionCount={allMistakes.length}
      favoriteCount={favorites.length}
      stickyNoteCount={stickyNotes.length}
      onExamChange={setActiveExamId}
      onPageChange={handlePageChange}
      onModeChange={setMode}
      onThemeToggle={() => setTheme(theme === "dark" ? "light" : "dark")}
      onReset={() => {
        if (!window.confirm("確定要清空本卷作答嗎？")) return;
        resetAnswers();
      }}
    >
      <div className="relative">
        <AnimatePresence>
          {isDatasetLoading ? (
            <motion.div
              key="soft-loading"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.28, ease: "easeOut" }}
              className="absolute inset-0 z-30 grid min-h-80 place-items-center rounded-[1.5rem] bg-[#fff8f4]/72 backdrop-blur-sm"
            >
              <div className="rounded-full border border-[#efd9d0] bg-white/86 px-5 py-3 text-sm font-semibold tracking-[0.12em] text-[#9c7b70] shadow-[0_18px_50px_rgba(181,133,117,0.16)]">
                正在切換考卷...
              </div>
            </motion.div>
          ) : null}
        </AnimatePresence>

        <DailyReviewHint
          mistakeCount={allMistakes.length}
          favoriteCount={favorites.length}
          noteCount={stickyNotes.length}
          onGoMistakes={() => handlePageChange("mistakes")}
          onGoFavorites={() => handlePageChange("favorites")}
          onGoNotes={() => handlePageChange("notes")}
        />

        {page === "mistakes" ? (
          <MistakeNotebookPage
            mistakes={allMistakes}
            loading={isMistakesLoading}
            onClearMistakes={handleClearAllMistakes}
            onStartPractice={handleStartMistakePractice}
            onOpenQuestion={(targetExamId, questionId) => {
              setMode("exam");
              setActiveExamId(targetExamId);
              setPendingQuestion({ examId: targetExamId, questionId });
              handlePageChange("exam");
            }}
          />
        ) : page === "favorites" ? (
          <FavoritesPage
            favorites={favorites}
            loading={isFavoritesLoading}
            onClearFavorites={handleClearAllFavorites}
            onToggleTag={handleToggleFavoriteTag}
            onOpenQuestion={(targetExamId, questionId) => {
              setMode("exam");
              setActiveExamId(targetExamId);
              setPendingQuestion({ examId: targetExamId, questionId });
              handlePageChange("exam");
            }}
          />
        ) : page === "notes" ? (
          <StickyNotesPage
            notes={stickyNotes}
            onAddNote={handleAddNote}
            onRemoveNote={handleRemoveNote}
            onClearNotes={handleClearNotes}
          />
        ) : dataset.questions.length === 0 ? (
          <EmptyState
            title="這一卷目前沒有題目"
            description="資料已載入，但目前還沒有可顯示的題目內容。"
          />
        ) : (
          <AnimatePresence mode="wait">
            {mode === "exam" ? (
              <motion.div
                key={`${dataset.id}-exam`}
                initial={{ opacity: 0, y: 18, filter: "blur(8px)" }}
                animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
                exit={{ opacity: 0, y: -12, filter: "blur(8px)" }}
                transition={{ duration: 0.42, ease: [0.22, 1, 0.36, 1] }}
              >
                <ExamMode
                  dataset={dataset}
                  answers={answers}
                  markedQuestions={markedQuestions}
                  onAnswer={answerQuestion}
                  reviewMode={
                    mistakePracticeIds[dataset.id]?.length
                      ? {
                          title: "錯題再練模式",
                          description: `目前只顯示這份題庫中的 ${mistakePracticeIds[dataset.id].length} 題錯題。`,
                          questionIds: mistakePracticeIds[dataset.id],
                          onExit: () => setMistakePracticeIds({}),
                        }
                      : undefined
                  }
                />
              </motion.div>
            ) : (
              <motion.div
                key={`${dataset.id}-flashcards`}
                initial={{ opacity: 0, y: 18, filter: "blur(8px)" }}
                animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
                exit={{ opacity: 0, y: -12, filter: "blur(8px)" }}
                transition={{ duration: 0.42, ease: [0.22, 1, 0.36, 1] }}
              >
                <FlashcardMode
                  dataset={dataset}
                  markedFlashcards={markedFlashcards}
                />
              </motion.div>
            )}
          </AnimatePresence>
        )}
      </div>
    </AppShell>
  );
}

function readStoredAnswers(examId: string): AnswerState {
  try {
    const stored = window.localStorage.getItem(storageKeys.answers(examId));
    if (!stored) return {};

    const parsed = JSON.parse(stored);
    return parsed && typeof parsed === "object" ? (parsed as AnswerState) : {};
  } catch {
    return {};
  }
}

function readStoredStringArray(key: string): string[] {
  try {
    const stored = window.localStorage.getItem(key);
    if (!stored) return [];

    const parsed = JSON.parse(stored);
    return Array.isArray(parsed)
      ? parsed.filter((item): item is string => typeof item === "string")
      : [];
  } catch {
    return [];
  }
}

function readStoredFavoriteTags(key: string): Record<string, FavoriteTag[]> {
  const validTags: FavoriteTag[] = ["待複習", "很重要", "易混淆"];

  try {
    const stored = window.localStorage.getItem(key);
    if (!stored) return {};

    const parsed = JSON.parse(stored);
    if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) return {};

    return Object.fromEntries(
      Object.entries(parsed)
        .map(([questionId, tags]) => [
          questionId,
          Array.isArray(tags)
            ? tags.filter((tag): tag is FavoriteTag =>
                validTags.includes(tag as FavoriteTag),
              )
            : [],
        ])
        .filter(([, tags]) => tags.length > 0),
    );
  } catch {
    return {};
  }
}

function writeStoredAnswers(examId: string, answers: AnswerState) {
  try {
    window.localStorage.setItem(
      storageKeys.answers(examId),
      JSON.stringify(answers),
    );
  } catch {
    // Local storage can be unavailable in private browsing.
  }
}

function writeStoredStringArray(key: string, values: string[]) {
  try {
    window.localStorage.setItem(key, JSON.stringify(values));
  } catch {
    // Local storage can be unavailable in private browsing.
  }
}

function writeStoredFavoriteTags(key: string, values: Record<string, FavoriteTag[]>) {
  try {
    window.localStorage.setItem(key, JSON.stringify(values));
  } catch {
    // Local storage can be unavailable in private browsing.
  }
}

function DailyReviewHint({
  mistakeCount,
  favoriteCount,
  noteCount,
  onGoMistakes,
  onGoFavorites,
  onGoNotes,
}: {
  mistakeCount: number;
  favoriteCount: number;
  noteCount: number;
  onGoMistakes: () => void;
  onGoFavorites: () => void;
  onGoNotes: () => void;
}) {
  const hasMistakes = mistakeCount > 0;
  const hasFavorites = favoriteCount > 0;
  const hasNotes = noteCount > 0;
  const suggestion = hasMistakes
    ? `先把 ${mistakeCount} 題錯題重看一次，再回來寫新題。`
    : hasFavorites
      ? `今天可以從 ${favoriteCount} 題收藏開始暖身。`
      : hasNotes
        ? `先快速翻一下 ${noteCount} 張便利貼，幫記憶熱機。`
        : "今天先挑一份題庫做 10 題，建立手感就好。";

  return (
    <section className="mb-6 rounded-[1.25rem] border border-white/80 bg-white/78 p-4 shadow-[0_14px_42px_rgba(181,133,117,0.12)] backdrop-blur-2xl">
      <div className="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
        <div>
          <p className="text-sm font-semibold text-[#b36a84]">今日建議複習</p>
          <p className="mt-1 text-sm leading-6 text-[#725b52]">{suggestion}</p>
        </div>
        <div className="flex flex-wrap gap-2">
          <button
            type="button"
            onClick={onGoMistakes}
            className="rounded-full border border-[#efd9d0] bg-white px-3 py-2 text-xs font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
          >
            看錯題
          </button>
          <button
            type="button"
            onClick={onGoFavorites}
            className="rounded-full border border-[#efd9d0] bg-white px-3 py-2 text-xs font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
          >
            看收藏
          </button>
          <button
            type="button"
            onClick={onGoNotes}
            className="rounded-full border border-[#efd9d0] bg-white px-3 py-2 text-xs font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
          >
            看便利貼
          </button>
        </div>
      </div>
    </section>
  );
}
