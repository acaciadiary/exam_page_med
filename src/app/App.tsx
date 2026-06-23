import { useEffect, useMemo, useRef, useState } from "react";
import { AnimatePresence, motion } from "motion/react";
import { AlertCircle, ArrowRight, ClipboardCheck, Radar, Sparkles, GitCompare } from "lucide-react";
import { AppShell } from "../components/AppShell";
import { IosInstallModal } from "../components/IosInstallModal";
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
  type MistakeStatus,
} from "../features/mistakes/MistakeNotebookPage";
import { StickyNotesPage } from "../features/notes/StickyNotesPage";
import { DiseaseComparePage } from "../features/exam/DiseaseComparePage";
import { RadarChart } from "../components/RadarChart";
import { useExamProgress } from "../hooks/useExamProgress";
import { useLocalStorage } from "../hooks/useLocalStorage";
import { useMarkedItems } from "../hooks/useMarkedItems";
import { getExamDisplayTitle, getSubjectLabel, getExamStage } from "../lib/examMetadata";
import { loadExamData, loadManifest } from "../lib/loadExamData";
import { storageKeys } from "../lib/storageKeys";
import { compactText, isAcceptedAnswer } from "../lib/text";
import { buildSearchForPage, readPageFromSearch, type AppPage } from "./routes";
import type { AnswerState, ExamDataset, ExamManifest, Mode } from "../types/exam";
import type { StickyNoteItem } from "../types/stickyNote";
import type { AppTheme } from "../components/ThemeToggle";

type LoadState =
  | { status: "loading" }
  | { status: "ready"; manifest: ExamManifest; dataset: ExamDataset }
  | { status: "error"; message: string };

type PerformanceStat = {
  label: string;
  answered: number;
  correct: number;
  accuracy: number;
};

type BeforeInstallPromptEvent = Event & {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: "accepted" | "dismissed"; platform: string }>;
};

export default function App() {
  const [page, setPage] = useState<AppPage>(() =>
    readPageFromSearch(window.location.search),
  );
  const [theme, setTheme] = useLocalStorage<AppTheme>(storageKeys.theme, "light");
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
  const [performanceStats, setPerformanceStats] = useState<PerformanceStat[]>([]);
  const [isMistakesLoading, setIsMistakesLoading] = useState(false);
  const [favorites, setFavorites] = useState<FavoriteEntry[]>([]);
  const [isFavoritesLoading, setIsFavoritesLoading] = useState(false);
  const [mistakePracticeIds, setMistakePracticeIds] = useState<Record<string, string[]>>({});
  const [mistakeStatuses, setMistakeStatuses] = useLocalStorage<Record<string, MistakeStatus>>(
    storageKeys.mistakeStatus,
    {},
  );
  const [stickyNotes, setStickyNotes] = useLocalStorage<StickyNoteItem[]>(
    storageKeys.stickyNotes,
    [],
  );

  const [installEvent, setInstallEvent] = useState<BeforeInstallPromptEvent | null>(null);
  const [showIosInstallModal, setShowIosInstallModal] = useState(false);

  useEffect(() => {
    const handleBeforeInstallPrompt = (e: Event) => {
      e.preventDefault();
      setInstallEvent(e as BeforeInstallPromptEvent);
    };
    window.addEventListener("beforeinstallprompt", handleBeforeInstallPrompt);
    return () => window.removeEventListener("beforeinstallprompt", handleBeforeInstallPrompt);
  }, []);

  const isStandalone = useMemo(() => {
    const standaloneNavigator = navigator as Navigator & { standalone?: boolean };
    return (
      window.matchMedia("(display-mode: standalone)").matches ||
      Boolean(standaloneNavigator.standalone)
    );
  }, []);

  const isIos = useMemo(() => {
    return (
      /iPad|iPhone|iPod/.test(navigator.userAgent) ||
      (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1)
    );
  }, []);

  const isInstallable = !isStandalone && (installEvent !== null || isIos);

  const handleInstall = async () => {
    if (installEvent) {
      await installEvent.prompt();
      const choice = await installEvent.userChoice.catch(() => undefined);
      if (choice && choice.outcome === "accepted") {
        setInstallEvent(null);
      }
    } else if (isIos) {
      setShowIosInstallModal(true);
    }
  };

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
        const activeExamExists = manifest.exams.some((exam) => exam.id === activeExamId);
        const selected =
          manifest.exams.find((exam) => exam.id === activeExamId) ?? manifest.exams[0];

        if (!selected) throw new Error("找不到題庫資料。");

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
            message: error instanceof Error ? error.message : "題庫載入失敗。",
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

  const activeExam = useMemo(() => {
    if (state.status !== "ready") return null;
    return state.manifest.exams.find((e) => e.id === activeExamId);
  }, [state, activeExamId]);

  const activeStage = useMemo(() => {
    return activeExam ? getExamStage(activeExam) : "stage-1";
  }, [activeExam]);

  useEffect(() => {
    if (state.status !== "ready") return undefined;

    let cancelled = false;
    const manifest = state.manifest;
    const currentDataset = state.dataset;

    async function collectMistakesAndStats() {
      setIsMistakesLoading(true);

      const entries: MistakeEntry[] = [];
      const stats = new Map<string, { answered: number; correct: number }>();

      const examsWithAnswers = manifest.exams.filter((exam) => {
        const examAnswers = exam.id === examId ? answers : readStoredAnswers(exam.id);
        return Object.keys(examAnswers).length > 0;
      });

      const loadedDatasets = await Promise.all(
        examsWithAnswers.map(async (exam) => {
          const dataset =
            currentDataset.id === exam.id ? currentDataset : await loadExamData(exam.path);
          return {
            exam,
            dataset,
            examAnswers: exam.id === examId ? answers : readStoredAnswers(exam.id),
          };
        })
      );

      for (const { exam, dataset, examAnswers } of loadedDatasets) {
        const label = getSubjectLabel(exam);

        for (const question of dataset.questions) {
          const selectedAnswer = examAnswers[question.id];
          if (!selectedAnswer) continue;

          const current = stats.get(label) ?? { answered: 0, correct: 0 };
          current.answered += 1;
          if (isAcceptedAnswer(selectedAnswer, question)) current.correct += 1;
          stats.set(label, current);

          if (!isAcceptedAnswer(selectedAnswer, question)) {
            const key = mistakeKey(exam.id, question.id);
            entries.push({
              exam,
              question,
              selectedAnswer,
              status: mistakeStatuses[key] ?? "first",
            });
          }
        }
      }

      if (!cancelled) {
        setAllMistakes(entries);
        setPerformanceStats(
          Array.from(stats.entries())
            .map(([label, stat]) => ({
              label,
              answered: stat.answered,
              correct: stat.correct,
              accuracy: stat.answered === 0 ? 0 : Math.round((stat.correct / stat.answered) * 100),
            }))
            .sort((a, b) => a.accuracy - b.accuracy),
        );
        setIsMistakesLoading(false);
      }
    }

    collectMistakesAndStats().catch(() => {
      if (!cancelled) {
        setAllMistakes([]);
        setPerformanceStats([]);
        setIsMistakesLoading(false);
      }
    });

    return () => {
      cancelled = true;
    };
  }, [answers, examId, mistakeStatuses, readyDataset, state]);

  useEffect(() => {
    if (state.status !== "ready") return undefined;

    let cancelled = false;
    const manifest = state.manifest;
    const currentDataset = state.dataset;

    async function collectFavorites() {
      setIsFavoritesLoading(true);

      const entries: FavoriteEntry[] = [];

      const examsWithFavorites = manifest.exams.map((exam) => {
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
        const favoriteIds = Array.from(new Set([...markedQuestionIds, ...markedFlashcardIds]));

        return {
          exam,
          markedQuestionIds,
          markedFlashcardIds,
          examFavoriteTags,
          favoriteIds,
        };
      }).filter(item => item.favoriteIds.length > 0);

      const loadedDatasets = await Promise.all(
        examsWithFavorites.map(async (item) => {
          const dataset =
            currentDataset.id === item.exam.id ? currentDataset : await loadExamData(item.exam.path);
          return { ...item, dataset };
        })
      );

      for (const { exam, dataset, markedQuestionIds, markedFlashcardIds, examFavoriteTags, favoriteIds } of loadedDatasets) {
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

  const openQuestion = (targetExamId: string, questionId: string) => {
    setMode("exam");
    setActiveExamId(targetExamId);
    setPendingQuestion({ examId: targetExamId, questionId });
    handlePageChange("exam");
  };

  useEffect(() => {
    (window as any).__openQuestion = openQuestion;
    return () => {
      delete (window as any).__openQuestion;
    };
  }, [openQuestion]);


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
    if (!window.confirm("確定清空所有便條？")) return;
    setStickyNotes([]);
  };

  const handleClearAllMistakes = () => {
    if (state.status !== "ready" || allMistakes.length === 0) return;
    if (!window.confirm("確定清空所有錯題紀錄？")) return;

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
      for (const questionId of questionIds) delete storedAnswers[questionId];
      writeStoredAnswers(targetExamId, storedAnswers);
    }

    setAllMistakes([]);
    setMistakePracticeIds({});
  };

  const handleClearAllFavorites = () => {
    if (state.status !== "ready" || favorites.length === 0) return;
    if (!window.confirm("確定清空所有收藏？")) return;

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
      if (mistake.status === "mastered") continue;
      idsByExam[mistake.exam.id] = [
        ...(idsByExam[mistake.exam.id] ?? []),
        mistake.question.id,
      ];
    }

    const firstMistake = allMistakes.find((mistake) => mistake.status !== "mastered") ?? allMistakes[0];
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

      if (nextTags.length === 0) delete next[questionId];
      else next[questionId] = nextTags;

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

  const handleMistakeStatusChange = (
    targetExamId: string,
    questionId: string,
    status: MistakeStatus,
  ) => {
    setMistakeStatuses((current) => ({
      ...current,
      [mistakeKey(targetExamId, questionId)]: status,
    }));
  };

  if (state.status === "loading") {
    return (
      <div className="grid min-h-screen place-items-center bg-[#fff8f4] px-6 text-[#4b3b35]">
        <div className="rounded-[1.5rem] border border-white/80 bg-white/72 px-8 py-7 text-center shadow-[0_18px_60px_rgba(181,133,117,0.18)] backdrop-blur-2xl">
          <div className="mx-auto h-12 w-12 animate-spin rounded-full border-2 border-[#f6a9c6] border-t-transparent" />
          <p className="mt-5 text-sm font-semibold tracking-[0.16em] text-[#9c7b70]">載入題庫中...</p>
        </div>
      </div>
    );
  }

  if (state.status === "error") {
    return (
      <div className="grid min-h-screen place-items-center bg-slate-950 px-6 text-white">
        <div className="max-w-md rounded-lg border border-red-300/30 bg-red-500/10 p-6">
          <AlertCircle className="text-red-200" />
          <h1 className="mt-4 text-xl font-semibold">題庫載入失敗</h1>
          <p className="mt-2 text-sm leading-6 text-red-100/80">{state.message}</p>
        </div>
      </div>
    );
  }

  const { manifest, dataset } = state;

  return (
    <>
    <AppShell
      exams={manifest.exams}
      activeExamId={dataset.id}
      page={page}
      theme={theme}
      answeredCount={answeredCount}
      questionCount={dataset.questions.length}
      wrongQuestionCount={allMistakes.length}
      favoriteCount={favorites.length}
      stickyNoteCount={stickyNotes.length}
      isInstallable={isInstallable}
      onInstall={handleInstall}
      onExamChange={setActiveExamId}
      onPageChange={handlePageChange}
      onThemeChange={setTheme}
      onReset={() => {
        if (!window.confirm("確定重置本科作答？")) return;
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
                正在切換題庫...
              </div>
            </motion.div>
          ) : null}
        </AnimatePresence>

        {page === "exam" && (
          <DailyStudyPanel
            mistakes={allMistakes}
            favorites={favorites}
            stats={performanceStats}
            activeStage={activeStage}
            theme={theme}
            onOpenQuestion={openQuestion}
            onGoMistakes={() => handlePageChange("mistakes")}
            onGoFavorites={() => handlePageChange("favorites")}
          />
        )}

        {page === "mistakes" ? (
          <MistakeNotebookPage
            mistakes={allMistakes}
            loading={isMistakesLoading}
            onClearMistakes={handleClearAllMistakes}
            onStartPractice={handleStartMistakePractice}
            onOpenQuestion={openQuestion}
            onStatusChange={handleMistakeStatusChange}
          />
        ) : page === "favorites" ? (
          <FavoritesPage
            favorites={favorites}
            loading={isFavoritesLoading}
            onClearFavorites={handleClearAllFavorites}
            onToggleTag={handleToggleFavoriteTag}
            onOpenQuestion={openQuestion}
          />
        ) : page === "notes" ? (
          <StickyNotesPage
            notes={stickyNotes}
            onAddNote={handleAddNote}
            onRemoveNote={handleRemoveNote}
            onClearNotes={handleClearNotes}
          />
        ) : page === "diseases" ? (
          <DiseaseComparePage
            stickyNotes={stickyNotes}
            onAddNote={handleAddNote}
            onRemoveNote={handleRemoveNote}
            theme={theme}
          />
        ) : dataset.questions.length === 0 ? (
          <EmptyState title="沒有題目" description="目前這份資料沒有可練習的題目。" />
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
                  mode={mode}
                  onModeChange={setMode}
                  theme={theme}
                  reviewMode={
                    mistakePracticeIds[dataset.id]?.length
                      ? {
                          title: "錯題練習",
                          description: `本次練習 ${mistakePracticeIds[dataset.id].length} 題未掌握錯題。`,
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
                  mode={mode}
                  onModeChange={setMode}
                  theme={theme}
                />
              </motion.div>
            )}
          </AnimatePresence>
        )}
      </div>
    </AppShell>
    <AnimatePresence>
      {showIosInstallModal && (
        <IosInstallModal
          isOpen={showIosInstallModal}
          onClose={() => setShowIosInstallModal(false)}
        />
      )}
    </AnimatePresence>
    </>
  );
}

function DailyStudyPanel({
  mistakes,
  favorites,
  stats,
  activeStage,
  theme,
  onOpenQuestion,
  onGoMistakes,
  onGoFavorites,
}: {
  mistakes: MistakeEntry[];
  favorites: FavoriteEntry[];
  stats: PerformanceStat[];
  activeStage: "stage-1" | "stage-2";
  theme: AppTheme;
  onOpenQuestion: (examId: string, questionId: string) => void;
  onGoMistakes: () => void;
  onGoFavorites: () => void;
}) {
  const activeMistakes = mistakes.filter((mistake) => mistake.status !== "mastered");
  const firstMistake = activeMistakes.find((mistake) => mistake.status === "final") ?? activeMistakes[0];
  const firstFavorite = favorites.find((favorite) => favorite.tags.includes("考前必看")) ?? favorites[0];
  const weakest = stats.find((stat) => stat.answered >= 3) ?? stats[0];

  return (
    <section className="mb-6 grid gap-4 xl:grid-cols-[minmax(0,1.3fr)_minmax(20rem,0.7fr)]">
      <div className="rounded-[1.5rem] border border-white/80 bg-white/80 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl">
        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="flex items-center gap-2 text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
              <ClipboardCheck size={16} />
              今日任務
            </p>
            <h2 className="mt-2 text-2xl font-semibold text-[#3f342d]">10 分鐘，把題庫拉回可掌控</h2>
          </div>
        </div>

        <div className="mt-5 grid gap-3 md:grid-cols-3">
          <TaskCard
            title="錯題回顧"
            description={firstMistake ? compactText(firstMistake.question.question_text, 76) : "目前沒有待複習錯題"}
            action={firstMistake ? "開始" : "查看"}
            onClick={() =>
              firstMistake ? onOpenQuestion(firstMistake.exam.id, firstMistake.question.id) : onGoMistakes()
            }
          />
          <TaskCard
            title="收藏卡片"
            description={firstFavorite ? compactText(firstFavorite.question.flashcard_summary || firstFavorite.question.question_text, 76) : "尚未收藏重點題"}
            action={firstFavorite ? "複習" : "查看"}
            onClick={() =>
              firstFavorite ? onOpenQuestion(firstFavorite.exam.id, firstFavorite.question.id) : onGoFavorites()
            }
          />
          <TaskCard
            title="弱科練習"
            description={weakest ? `${weakest.label} 目前正確率 ${weakest.accuracy}%` : "作答後會自動分析弱點"}
            action="看雷達"
            onClick={onGoMistakes}
          />
        </div>
      </div>

      <div className="rounded-[1.5rem] border border-white/80 bg-white/80 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl flex flex-col justify-between">
        <div>
          <p className="flex items-center gap-2 text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
            <Radar size={16} />
            弱點雷達
          </p>
          <div className="mt-2 flex justify-center">
            {stats.length === 0 ? (
              <div className="py-12 text-center text-sm leading-6 text-[#725b52] font-hand">
                答幾題後，這裡會顯示雷達圖分析。
              </div>
            ) : (
              <RadarChart stats={stats} activeStage={activeStage} theme={theme} />
            )}
          </div>
        </div>

        {stats.length > 0 && (
          <div className="mt-2 border-t border-[#f0ded6]/50 dark:border-white/5 pt-3.5 space-y-2">
            <p className="text-[10px] font-bold uppercase tracking-[0.12em] text-[#8b7666] dark:text-[#a2949e]">
              弱科數據排行 (最需加強)
            </p>
            <div className="grid gap-2 max-h-32 overflow-y-auto pr-1">
              {stats.slice(0, 4).map((stat) => (
                <div key={stat.label} className="flex items-center justify-between text-xs font-semibold text-[#725b52] dark:text-[#dccbd3]">
                  <span>{stat.label}</span>
                  <div className="flex items-center gap-2">
                    <span className="text-[#b36a84] font-extrabold">{stat.accuracy}%</span>
                    <span className="text-[10px] text-[#aa8a7d] dark:text-[#a2949e] font-normal">({stat.correct}/{stat.answered} 題)</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </section>
  );
}

function TaskCard({
  title,
  description,
  action,
  onClick,
}: {
  title: string;
  description: string;
  action: string;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className="group min-h-36 rounded-[1.05rem] border border-[#efd9d0] bg-white/72 p-4 text-left transition hover:-translate-y-0.5 hover:border-[#f1aac8] hover:bg-[#fff7fb]"
    >
      <Sparkles size={17} className="text-[#b36a84]" />
      <p className="mt-3 text-sm font-bold text-[#3f342d]">{title}</p>
      <p className="mt-2 line-clamp-3 text-sm leading-6 text-[#725b52]">{description}</p>
      <span className="mt-3 inline-flex items-center gap-1 text-xs font-bold text-[#9a496b]">
        {action}
        <ArrowRight size={14} />
      </span>
    </button>
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
  const validTags: FavoriteTag[] = ["高頻", "易混淆", "考前必看"];

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
            ? tags.filter((tag): tag is FavoriteTag => validTags.includes(tag as FavoriteTag))
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
    window.localStorage.setItem(storageKeys.answers(examId), JSON.stringify(answers));
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

function mistakeKey(examId: string, questionId: string) {
  return `${examId}:${questionId}`;
}


