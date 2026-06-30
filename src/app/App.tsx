import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { AnimatePresence, motion } from "motion/react";
import { AlertCircle, ArrowRight, ClipboardCheck, Radar, Sparkles, GitCompare } from "lucide-react";
import { AppShell } from "../components/AppShell";
import { DesktopInstallModal } from "../components/DesktopInstallModal";
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
import {
  StudyOverviewPage,
  type CategoryProgressStat,
  type ExamProgressStat,
  type StudyOverviewSummary,
} from "../features/progress/StudyOverviewPage";
import { StickyNotesPage } from "../features/notes/StickyNotesPage";
import { DiseaseComparePage } from "../features/exam/DiseaseComparePage";
import {
  HomeDashboardPage,
  type ExamPlan,
  type StudyActivityLog,
} from "../features/home/HomeDashboardPage";
import { RadarChart } from "../components/RadarChart";
import { useExamProgress } from "../hooks/useExamProgress";
import { useLocalStorage } from "../hooks/useLocalStorage";
import { useMarkedItems } from "../hooks/useMarkedItems";
import { getExamDisplayTitle, getSubjectLabel, getExamStage } from "../lib/examMetadata";
import { loadExamData, loadManifest } from "../lib/loadExamData";
import { storageKeys } from "../lib/storageKeys";
import { compactText, isAcceptedAnswer } from "../lib/text";
import { getDerivedQuestionCategory } from "../lib/categoryFilters";
import { buildSearchForPage, readPageFromSearch, type AppPage } from "./routes";
import type { AnswerOptionKey, AnswerState, ExamDataset, ExamManifest, Mode } from "../types/exam";
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

type LastPractice = {
  examId: string;
  questionId: string;
  answeredAt: string;
};

type BeforeInstallPromptEvent = Event & {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: "accepted" | "dismissed"; platform: string }>;
};

type InstallAwareNavigator = Navigator & {
  standalone?: boolean;
  getInstalledRelatedApps?: () => Promise<unknown[]>;
};

const siteUrl = "https://acaciadiary.github.io/exam_page_med/";

const pageSeo: Record<AppPage, { title: string; description: string; path: string }> = {
  home: {
    title: "首頁｜Ariel's Med",
    description:
      "Ariel's Med 我的書桌整理今日任務、每日目標、連續練習、考試倒數與個人週報，陪你每天穩定刷題。",
    path: "",
  },
  exam: {
    title: "歷屆試題｜Ariel's Med",
    description:
      "Ariel's Med 收錄台灣醫師國考歷屆試題，提供醫學一至醫學六線上練習、錯題複習、收藏閃卡與重點整理。",
    path: "?page=exam",
  },
  progress: {
    title: "我的進度｜Ariel's Med",
    description:
      "整理所有年度與科目的作答進度、正確率、錯題與弱點分類，快速掌握下一步該補強的範圍。",
    path: "?page=progress",
  },
  diseases: {
    title: "必看區｜Ariel's Med",
    description:
      "整理醫師國考常見疾病鑑別比較，協助考生快速複習高頻考點與容易混淆的臨床重點。",
    path: "?page=diseases",
  },
  mistakes: {
    title: "錯題本｜Ariel's Med",
    description:
      "自動整理醫師國考練習錯題，方便反覆複習弱點、追蹤答題狀態與強化記憶。",
    path: "?page=mistakes",
  },
  favorites: {
    title: "收藏區｜Ariel's Med",
    description:
      "收藏醫師國考歷屆試題與重點閃卡，依標籤整理常考觀念與考前複習清單。",
    path: "?page=favorites",
  },
  notes: {
    title: "便利貼｜Ariel's Med",
    description:
      "在醫師國考練題過程中記錄個人筆記、考點提醒與易錯觀念，方便考前快速回顧。",
    path: "?page=notes",
  },
};

function updateMetaTag(selector: string, attribute: "content" | "href", value: string) {
  const element = document.head.querySelector(selector);
  if (element) element.setAttribute(attribute, value);
}

function isRunningAsInstalledApp() {
  const standaloneNavigator = navigator as InstallAwareNavigator;
  return (
    window.matchMedia("(display-mode: standalone)").matches ||
    window.matchMedia("(display-mode: fullscreen)").matches ||
    window.matchMedia("(display-mode: minimal-ui)").matches ||
    Boolean(standaloneNavigator.standalone) ||
    document.referrer.startsWith("android-app://")
  );
}

export default function App() {
  const [page, setPage] = useState<AppPage>(() =>
    readPageFromSearch(window.location.search),
  );
  const [theme, setTheme] = useLocalStorage<AppTheme>(storageKeys.theme, "light");
  const [readingBold, setReadingBold] = useLocalStorage<boolean>(
    storageKeys.readingBold,
    false,
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
    requestKey: number;
  } | null>(null);
  const [allMistakes, setAllMistakes] = useState<MistakeEntry[]>([]);
  const [performanceStats, setPerformanceStats] = useState<PerformanceStat[]>([]);
  const [examProgressStats, setExamProgressStats] = useState<ExamProgressStat[]>([]);
  const [categoryProgressStats, setCategoryProgressStats] = useState<CategoryProgressStat[]>([]);
  const [studySummary, setStudySummary] = useState<StudyOverviewSummary>({
    totalAnswered: 0,
    totalQuestions: 0,
    totalCorrect: 0,
    totalWrong: 0,
    accuracy: 0,
    completion: 0,
    completedExamCount: 0,
    wrongQuestionCount: 0,
    activeWrongQuestionCount: 0,
    favoriteCount: 0,
    masteredMistakeCount: 0,
  });
  const [isMistakesLoading, setIsMistakesLoading] = useState(false);
  const [favorites, setFavorites] = useState<FavoriteEntry[]>([]);
  const [isFavoritesLoading, setIsFavoritesLoading] = useState(false);
  const [mistakePracticeIds, setMistakePracticeIds] = useState<Record<string, string[]>>({});
  const [mistakeStatuses, setMistakeStatuses] = useLocalStorage<Record<string, MistakeStatus>>(
    storageKeys.mistakeStatus,
    {},
  );
  const [lastPractice, setLastPractice] = useLocalStorage<LastPractice | null>(
    storageKeys.lastPractice,
    null,
  );
  const [dailyGoal, setDailyGoal] = useLocalStorage<number>(storageKeys.dailyGoal, 10);
  const [examPlan, setExamPlan] = useLocalStorage<ExamPlan>(storageKeys.examPlan, {
    targetDate: "",
    targetStage: "stage-2",
    focusExamId: "",
  });
  const [studyActivity, setStudyActivity] = useLocalStorage<StudyActivityLog>(
    storageKeys.studyActivity,
    {},
  );
  const [stickyNotes, setStickyNotes] = useLocalStorage<StickyNoteItem[]>(
    storageKeys.stickyNotes,
    [],
  );
  const [favoritesTrigger, setFavoritesTrigger] = useState(0);

  const [installEvent, setInstallEvent] = useState<BeforeInstallPromptEvent | null>(null);
  const [showIosInstallModal, setShowIosInstallModal] = useState(false);
  const [showDesktopInstallModal, setShowDesktopInstallModal] = useState(false);
  const [isStandalone, setIsStandalone] = useState(() => isRunningAsInstalledApp());
  const [isAppInstalled, setIsAppInstalled] = useLocalStorage<boolean>(
    storageKeys.appInstalled,
    false,
  );
  const [isInstallPromptDismissed, setIsInstallPromptDismissed] = useLocalStorage<boolean>(
    storageKeys.installPromptDismissed,
    false,
  );
  const [isInstallPromptExpired, setIsInstallPromptExpired] = useState(false);

  useEffect(() => {
    const handleBeforeInstallPrompt = (e: Event) => {
      e.preventDefault();
      if (!isRunningAsInstalledApp() && !isAppInstalled) {
        setInstallEvent(e as BeforeInstallPromptEvent);
      }
    };
    window.addEventListener("beforeinstallprompt", handleBeforeInstallPrompt);
    return () => window.removeEventListener("beforeinstallprompt", handleBeforeInstallPrompt);
  }, [isAppInstalled]);

  useEffect(() => {
    const updateInstallState = () => {
      const isInstalledMode = isRunningAsInstalledApp();
      setIsStandalone(isInstalledMode);
      if (isInstalledMode) {
        setIsAppInstalled(true);
        setInstallEvent(null);
      }
    };

    const handleAppInstalled = () => {
      setIsAppInstalled(true);
      setInstallEvent(null);
      setShowIosInstallModal(false);
      setShowDesktopInstallModal(false);
      updateInstallState();
    };

    updateInstallState();
    window.addEventListener("appinstalled", handleAppInstalled);

    const displayModeQueries = [
      window.matchMedia("(display-mode: standalone)"),
      window.matchMedia("(display-mode: fullscreen)"),
      window.matchMedia("(display-mode: minimal-ui)"),
    ];
    displayModeQueries.forEach((query) => {
      query.addEventListener("change", updateInstallState);
    });

    const installAwareNavigator = navigator as InstallAwareNavigator;
    installAwareNavigator
      .getInstalledRelatedApps?.()
      .then((apps) => {
        if (apps.length > 0) {
          setIsAppInstalled(true);
          setInstallEvent(null);
        }
      })
      .catch(() => undefined);

    return () => {
      window.removeEventListener("appinstalled", handleAppInstalled);
      displayModeQueries.forEach((query) => {
        query.removeEventListener("change", updateInstallState);
      });
    };
  }, [setIsAppInstalled]);

  const isIos = useMemo(() => {
    return (
      /iPad|iPhone|iPod/.test(navigator.userAgent) ||
      (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1)
    );
  }, []);

  const canOpenInstallHelp = !isStandalone;
  const isInstallable = !isStandalone && !isAppInstalled && (installEvent !== null || isIos);
  const shouldShowInstallPrompt =
    page === "exam" && isInstallable && !isInstallPromptDismissed && !isInstallPromptExpired;

  useEffect(() => {
    if (!shouldShowInstallPrompt) return undefined;

    const timer = window.setTimeout(() => {
      setIsInstallPromptExpired(true);
    }, 15000);

    return () => window.clearTimeout(timer);
  }, [shouldShowInstallPrompt]);

  const handleInstall = async () => {
    if (installEvent) {
      const choice = await installEvent
        .prompt()
        .then(() => installEvent.userChoice)
        .catch(() => undefined);
      if (choice && choice.outcome === "accepted") {
        setIsAppInstalled(true);
        setInstallEvent(null);
        setShowDesktopInstallModal(false);
      } else if (!choice) {
        setInstallEvent(null);
      }
    } else if (isIos) {
      setShowIosInstallModal(true);
    } else {
      setShowDesktopInstallModal(true);
    }
  };

  const handleDismissInstallPrompt = () => {
    setIsInstallPromptDismissed(true);
    setIsInstallPromptExpired(true);
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
    const seo = pageSeo[page];
    const canonicalUrl = `${siteUrl}${seo.path}`;

    document.title = seo.title;
    updateMetaTag('meta[name="description"]', "content", seo.description);
    updateMetaTag('meta[property="og:title"]', "content", seo.title);
    updateMetaTag('meta[property="og:description"]', "content", seo.description);
    updateMetaTag('meta[property="og:url"]', "content", canonicalUrl);
    updateMetaTag('meta[name="twitter:title"]', "content", seo.title);
    updateMetaTag('meta[name="twitter:description"]', "content", seo.description);
    updateMetaTag('link[rel="canonical"]', "href", canonicalUrl);
  }, [page]);

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

        if (!selected) throw new Error("找不到國考題資料。");

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
            message: error instanceof Error ? error.message : "國考題載入失敗。",
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
    if (state.status !== "ready") return;
    if (examPlan.focusExamId && state.manifest.exams.some((exam) => exam.id === examPlan.focusExamId)) {
      return;
    }

    const fallbackExam =
      state.manifest.exams.find((exam) => getExamStage(exam) === examPlan.targetStage) ??
      state.manifest.exams[0];

    if (fallbackExam) {
      setExamPlan((current) => ({ ...current, focusExamId: fallbackExam.id }));
    }
  }, [examPlan.focusExamId, examPlan.targetStage, setExamPlan, state]);

  useEffect(() => {
    if (state.status !== "ready") return undefined;

    let cancelled = false;
    const manifest = state.manifest;
    const currentDataset = state.dataset;

    async function collectMistakesAndStats() {
      setIsMistakesLoading(true);

      const entries: MistakeEntry[] = [];
      const stats = new Map<string, { answered: number; correct: number }>();
      const examStats = new Map<string, ExamProgressStat>();
      const categoryStats = new Map<string, CategoryProgressStat>();

      const examsWithAnswers = manifest.exams.filter((exam) => {
        const examAnswers = exam.id === examId ? answers : readStoredAnswers(exam.id);
        examStats.set(exam.id, {
          exam,
          answered: Object.keys(examAnswers).length,
          total: exam.question_count,
          correct: 0,
          wrong: 0,
          accuracy: 0,
          completion:
            exam.question_count === 0
              ? 0
              : Math.round((Object.keys(examAnswers).length / exam.question_count) * 100),
        });
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
        const currentExamStat = examStats.get(exam.id);

        for (const question of dataset.questions) {
          const selectedAnswer = examAnswers[question.id];
          if (!selectedAnswer) continue;

          const current = stats.get(label) ?? { answered: 0, correct: 0 };
          current.answered += 1;
          const correct = isAcceptedAnswer(selectedAnswer, question);
          if (correct) current.correct += 1;
          stats.set(label, current);

          if (currentExamStat) {
            if (correct) currentExamStat.correct += 1;
            else currentExamStat.wrong += 1;
          }

          const category = getDerivedQuestionCategory(dataset, question);
          const categoryKey = `${exam.subject}:${category}`;
          const currentCategory = categoryStats.get(categoryKey) ?? {
            key: categoryKey,
            label: category,
            subjectLabel: label,
            answered: 0,
            correct: 0,
            wrong: 0,
            accuracy: 0,
          };
          currentCategory.answered += 1;
          if (correct) currentCategory.correct += 1;
          else currentCategory.wrong += 1;
          categoryStats.set(categoryKey, currentCategory);

          if (!correct) {
            const key = mistakeKey(exam.id, question.id);
            entries.push({
              exam,
              question,
              selectedAnswer,
              status: mistakeStatuses[key] ?? "first",
            });
          }
        }

        if (currentExamStat) {
          currentExamStat.accuracy =
            currentExamStat.answered === 0
              ? 0
              : Math.round((currentExamStat.correct / currentExamStat.answered) * 100);
          examStats.set(exam.id, currentExamStat);
        }
      }

      if (!cancelled) {
        const examProgress = Array.from(examStats.values()).sort((a, b) => {
          const yearCompare = b.exam.year.localeCompare(a.exam.year, "zh-Hant", { numeric: true });
          if (yearCompare !== 0) return yearCompare;
          return a.exam.subject.localeCompare(b.exam.subject, "zh-Hant", { numeric: true });
        });
        const categoryProgress = Array.from(categoryStats.values())
          .map((stat) => ({
            ...stat,
            accuracy: stat.answered === 0 ? 0 : Math.round((stat.correct / stat.answered) * 100),
          }))
          .sort((a, b) => a.accuracy - b.accuracy || b.wrong - a.wrong);
        const totalQuestions = manifest.exams.reduce((sum, exam) => sum + exam.question_count, 0);
        const totalAnswered = examProgress.reduce((sum, stat) => sum + stat.answered, 0);
        const totalCorrect = examProgress.reduce((sum, stat) => sum + stat.correct, 0);
        const totalWrong = examProgress.reduce((sum, stat) => sum + stat.wrong, 0);
        const masteredMistakeCount = entries.filter((entry) => entry.status === "mastered").length;

        setAllMistakes(entries);
        setExamProgressStats(examProgress);
        setCategoryProgressStats(categoryProgress);
        setStudySummary({
          totalAnswered,
          totalQuestions,
          totalCorrect,
          totalWrong,
          accuracy: totalAnswered === 0 ? 0 : Math.round((totalCorrect / totalAnswered) * 100),
          completion:
            totalQuestions === 0 ? 0 : Math.round((totalAnswered / totalQuestions) * 100),
          completedExamCount: examProgress.filter(
            (stat) => stat.total > 0 && stat.answered >= stat.total,
          ).length,
          wrongQuestionCount: entries.length,
          activeWrongQuestionCount: entries.filter((entry) => entry.status !== "mastered").length,
          favoriteCount: favorites.length,
          masteredMistakeCount,
        });
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
        setExamProgressStats([]);
        setCategoryProgressStats([]);
        setStudySummary({
          totalAnswered: 0,
          totalQuestions: 0,
          totalCorrect: 0,
          totalWrong: 0,
          accuracy: 0,
          completion: 0,
          completedExamCount: 0,
          wrongQuestionCount: 0,
          activeWrongQuestionCount: 0,
          favoriteCount: favorites.length,
          masteredMistakeCount: 0,
        });
        setIsMistakesLoading(false);
      }
    });

    return () => {
      cancelled = true;
    };
  }, [answers, examId, favorites.length, mistakeStatuses, readyDataset, state]);

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
  }, [examId, favoriteTags, markedFlashcards.marked, markedQuestions.marked, state, favoritesTrigger]);

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
    setPendingQuestion({ examId: targetExamId, questionId, requestKey: Date.now() });
    handlePageChange("exam");
  };

  const openExam = (targetExamId: string) => {
    setMode("exam");
    setActiveExamId(targetExamId);
    handlePageChange("exam");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleQuestionFocusComplete = useCallback((questionId: string) => {
    setPendingQuestion((current) => {
      if (!current || current.questionId !== questionId) return current;
      return null;
    });
  }, []);

  const handleAnswerQuestion = (questionId: string, answer: AnswerOptionKey) => {
    const isFirstAnswer = !answers[questionId];
    answerQuestion(questionId, answer);

    if (!readyDataset) return;

    const question = readyDataset.questions.find((item) => item.id === questionId);
    if (!question) return;

    const currentExamId = readyDataset.id;
    const correct = isAcceptedAnswer(answer, question);
    const activePracticeIds = mistakePracticeIds[currentExamId] ?? [];

    if (isFirstAnswer) {
      const todayKey = formatLocalDateKey(new Date());
      setStudyActivity((current) => {
        const today = current[todayKey] ?? { answered: 0, correct: 0 };

        return {
          ...current,
          [todayKey]: {
            answered: today.answered + 1,
            correct: today.correct + (correct ? 1 : 0),
          },
        };
      });
    }

    setLastPractice({
      examId: currentExamId,
      questionId,
      answeredAt: new Date().toISOString(),
    });

    if (!activePracticeIds.includes(questionId)) return;

    setMistakeStatuses((current) => {
      const key = mistakeKey(currentExamId, questionId);
      const previous = current[key];

      return {
        ...current,
        [key]: correct ? "mastered" : previous === "repeat" ? "final" : "repeat",
      };
    });

    if (!correct) return;

    setMistakePracticeIds((current) => {
      const remaining = (current[currentExamId] ?? []).filter((id) => id !== questionId);
      const next = { ...current };

      if (remaining.length > 0) next[currentExamId] = remaining;
      else delete next[currentExamId];

      return next;
    });
  };

  useEffect(() => {
    (window as any).__openQuestion = openQuestion;
    return () => {
      delete (window as any).__openQuestion;
    };
  }, [openQuestion]);


  const handleAddNote = (
    text: string,
    source?: Omit<StickyNoteItem, "id" | "text" | "createdAt">,
  ) => {
    setStickyNotes((current) => [
      {
        id: `${Date.now()}-${Math.random().toString(36).slice(2)}`,
        text,
        createdAt: new Date().toISOString(),
        ...source,
      },
      ...current,
    ]);
  };

  const handleAddQuestionNote = (questionId: string, text: string) => {
    if (!readyDataset) return;

    const question = readyDataset.questions.find((item) => item.id === questionId);
    if (!question) return;

    handleAddNote(text, {
      examId: readyDataset.id,
      examTitle: getExamDisplayTitle(readyDataset),
      questionId,
      questionNumber: question.question_number,
      questionText: question.question_text,
    });
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

  const handleRemoveMistake = (targetExamId: string, questionId: string) => {
    if (targetExamId === examId) {
      removeAnswers([questionId]);
    } else {
      const storedAnswers = readStoredAnswers(targetExamId);
      delete storedAnswers[questionId];
      writeStoredAnswers(targetExamId, storedAnswers);
    }

    setMistakeStatuses((current) => {
      const next = { ...current };
      delete next[mistakeKey(targetExamId, questionId)];
      return next;
    });
    setAllMistakes((current) =>
      current.filter(
        (mistake) => mistake.exam.id !== targetExamId || mistake.question.id !== questionId,
      ),
    );
    setMistakePracticeIds((current) => {
      const currentIds = current[targetExamId];
      if (!currentIds) return current;

      const remaining = currentIds.filter((id) => id !== questionId);
      const next = { ...current };
      if (remaining.length > 0) next[targetExamId] = remaining;
      else delete next[targetExamId];
      return next;
    });
  };

  const handleRemoveFavorite = (targetExamId: string, questionId: string) => {
    if (targetExamId === examId) {
      markedQuestions.removeMarked(questionId);
      markedFlashcards.removeMarked(questionId);
      setFavoriteTags((current) => {
        const next = { ...current };
        delete next[questionId];
        return next;
      });
    } else {
      const questionKey = storageKeys.markedQuestions(targetExamId);
      const flashcardKey = storageKeys.markedFlashcards(targetExamId);
      const targetTags = readStoredFavoriteTags(storageKeys.favoriteTags(targetExamId));

      writeStoredStringArray(
        questionKey,
        readStoredStringArray(questionKey).filter((id) => id !== questionId),
      );
      writeStoredStringArray(
        flashcardKey,
        readStoredStringArray(flashcardKey).filter((id) => id !== questionId),
      );
      delete targetTags[questionId];
      writeStoredFavoriteTags(storageKeys.favoriteTags(targetExamId), targetTags);
    }

    setFavorites((current) =>
      current.filter((entry) => entry.exam.id !== targetExamId || entry.question.id !== questionId),
    );
    setFavoritesTrigger((prev) => prev + 1);
  };

  const handleStartMistakePractice = () => {
    if (allMistakes.length === 0) return;

    const idsByExam: Record<string, string[]> = {};
    const pendingMistakes = allMistakes.filter((mistake) => mistake.status !== "mastered");
    if (pendingMistakes.length === 0) return;

    for (const mistake of pendingMistakes) {
      idsByExam[mistake.exam.id] = [
        ...(idsByExam[mistake.exam.id] ?? []),
        mistake.question.id,
      ];
    }

    const firstMistake = pendingMistakes[0];
    setMistakePracticeIds(idsByExam);
    setMode("exam");
    setActiveExamId(firstMistake.exam.id);
    handlePageChange("exam");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleToggleFavorite = (targetExamId: string, questionId: string) => {
    if (targetExamId === examId) {
      markedQuestions.toggleMarked(questionId);
    } else {
      const storedKey = storageKeys.markedQuestions(targetExamId);
      const currentMarked = readStoredStringArray(storedKey);
      const nextMarked = currentMarked.includes(questionId)
        ? currentMarked.filter((id) => id !== questionId)
        : [...currentMarked, questionId];
      writeStoredStringArray(storedKey, nextMarked);
      
      if (currentMarked.includes(questionId)) {
        const targetTags = readStoredFavoriteTags(storageKeys.favoriteTags(targetExamId));
        delete targetTags[questionId];
        writeStoredFavoriteTags(storageKeys.favoriteTags(targetExamId), targetTags);
      }
    }
    setFavoritesTrigger((prev) => prev + 1);
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
          <p className="mt-5 text-sm font-semibold tracking-[0.16em] text-[#9c7b70]">載入國考題中...</p>
        </div>
      </div>
    );
  }

  if (state.status === "error") {
    return (
      <div className="grid min-h-screen place-items-center bg-slate-950 px-6 text-white">
        <div className="max-w-md rounded-lg border border-red-300/30 bg-red-500/10 p-6">
          <AlertCircle className="text-red-200" />
          <h1 className="mt-4 text-xl font-semibold">國考題載入失敗</h1>
          <p className="mt-2 text-sm leading-6 text-red-100/80">{state.message}</p>
        </div>
      </div>
    );
  }

  const { manifest, dataset } = state;
  const fallbackPracticeQuestion =
    dataset.questions.find((question) => !answers[question.id]) ?? dataset.questions[0] ?? null;
  const lastPracticeExamExists = lastPractice
    ? manifest.exams.some((exam) => exam.id === lastPractice.examId)
    : false;
  const continueTarget =
    lastPractice && lastPracticeExamExists
      ? lastPractice
      : fallbackPracticeQuestion
      ? {
          examId: dataset.id,
          questionId: fallbackPracticeQuestion.id,
          answeredAt: "",
        }
      : null;
  const continueQuestion =
    continueTarget?.examId === dataset.id
      ? dataset.questions.find((question) => question.id === continueTarget.questionId) ?? null
      : null;
  const continueExam = continueTarget
    ? manifest.exams.find((exam) => exam.id === continueTarget.examId) ?? null
    : null;
  const overviewSummary = {
    ...studySummary,
    favoriteCount: favorites.length,
  };
  const continueTitle = continueQuestion
    ? `從第 ${continueQuestion.question_number} 題繼續`
    : continueExam
    ? `回到 ${getExamDisplayTitle(continueExam)}`
    : "開始今天的第一題";
  const continueDescription = continueQuestion
    ? compactText(continueQuestion.question_text, 92)
    : continueExam
    ? getExamDisplayTitle(continueExam)
    : "系統會自動帶你到下一題未作答題目。";

  return (
    <>
    <AppShell
      exams={manifest.exams}
      activeExamId={dataset.id}
      page={page}
      theme={theme}
      readingBold={readingBold}
      answeredCount={answeredCount}
      questionCount={dataset.questions.length}
      wrongQuestionCount={allMistakes.length}
      favoriteCount={favorites.length}
      stickyNoteCount={stickyNotes.length}
      isInstallable={shouldShowInstallPrompt}
      canInstallFromSettings={canOpenInstallHelp}
      onInstall={handleInstall}
      onDismissInstallPrompt={handleDismissInstallPrompt}
      onExamChange={setActiveExamId}
      onPageChange={handlePageChange}
      onThemeChange={setTheme}
      onReadingBoldChange={setReadingBold}
      onReset={() => {
        if (!window.confirm("確定重置本科作答？")) return;
        resetAnswers();
        if (lastPractice?.examId === examId) setLastPractice(null);
      }}
      onResetAll={() => {
        if (!window.confirm("⚠️ 確定重置所有作答和筆記？\n\n此操作將清除：\n• 所有科目的作答記錄\n• 所有收藏與標籤\n• 所有錯題狀態\n• 所有便利貼筆記\n\n此操作無法復原！")) return;

        // Clear current exam's in-memory state
        resetAnswers();
        markedQuestions.clearMarked();
        markedFlashcards.clearMarked();
        setFavoriteTags({});

        // Clear all other exams' stored data
        for (const exam of manifest.exams) {
          if (exam.id === examId) continue;
          writeStoredAnswers(exam.id, {});
          writeStoredStringArray(storageKeys.markedQuestions(exam.id), []);
          writeStoredStringArray(storageKeys.markedFlashcards(exam.id), []);
          writeStoredFavoriteTags(storageKeys.favoriteTags(exam.id), {});
        }

        // Clear global state
        setMistakeStatuses({});
        setStickyNotes([]);
        setAllMistakes([]);
        setPerformanceStats([]);
        setFavorites([]);
        setMistakePracticeIds({});
        setLastPractice(null);
        setDailyGoal(10);
        setExamPlan({ targetDate: "", targetStage: "stage-2", focusExamId: manifest.exams[0]?.id ?? "" });
        setStudyActivity({});
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
                正在切換國考題...
              </div>
            </motion.div>
          ) : null}
        </AnimatePresence>

        {page === "home" ? (
          <HomeDashboardPage
            dailyGoal={dailyGoal}
            examPlan={examPlan}
            studyActivity={studyActivity}
            mistakes={allMistakes}
            favorites={favorites}
            stats={performanceStats}
            activeStage={activeStage}
            theme={theme}
            exams={manifest.exams}
            continueTarget={continueTarget}
            continueQuestion={continueQuestion}
            continueExam={continueExam}
            onDailyGoalChange={setDailyGoal}
            onExamPlanChange={setExamPlan}
            onContinuePractice={() => {
              if (!continueTarget) return;
              openQuestion(continueTarget.examId, continueTarget.questionId);
            }}
            onOpenQuestion={openQuestion}
            onOpenExam={openExam}
            onGoMistakes={() => handlePageChange("mistakes")}
            onGoFavorites={() => handlePageChange("favorites")}
            onGoProgress={() => handlePageChange("progress")}
          />
        ) : page === "progress" ? (
          <StudyOverviewPage
            summary={overviewSummary}
            examStats={examProgressStats}
            categoryStats={categoryProgressStats}
            continueTitle={continueTitle}
            continueDescription={continueDescription}
            canContinue={Boolean(continueTarget)}
            onContinuePractice={() => {
              if (!continueTarget) return;
              openQuestion(continueTarget.examId, continueTarget.questionId);
            }}
            onOpenExam={openExam}
            onGoMistakes={() => handlePageChange("mistakes")}
            onGoFavorites={() => handlePageChange("favorites")}
          />
        ) : page === "mistakes" ? (
          <MistakeNotebookPage
            mistakes={allMistakes}
            loading={isMistakesLoading}
            onClearMistakes={handleClearAllMistakes}
            onRemoveMistake={handleRemoveMistake}
            onStartPractice={handleStartMistakePractice}
            onOpenQuestion={openQuestion}
            onStatusChange={handleMistakeStatusChange}
          />
        ) : page === "favorites" ? (
          <FavoritesPage
            favorites={favorites}
            loading={isFavoritesLoading}
            onClearFavorites={handleClearAllFavorites}
            onRemoveFavorite={handleRemoveFavorite}
            onToggleTag={handleToggleFavoriteTag}
            onOpenQuestion={openQuestion}
          />
        ) : page === "notes" ? (
          <StickyNotesPage
            notes={stickyNotes}
            onAddNote={handleAddNote}
            onRemoveNote={handleRemoveNote}
            onClearNotes={handleClearNotes}
            onOpenQuestion={openQuestion}
          />
        ) : page === "diseases" ? (
          <DiseaseComparePage
            stickyNotes={stickyNotes}
            onAddNote={handleAddNote}
            onRemoveNote={handleRemoveNote}
            theme={theme}
            favorites={favorites}
            onToggleFavorite={handleToggleFavorite}
            onToggleFavoriteTag={handleToggleFavoriteTag}
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
                  onAnswer={handleAnswerQuestion}
                  mode={mode}
                  onModeChange={setMode}
                  theme={theme}
                  stickyNotes={stickyNotes}
                  onAddQuestionNote={handleAddQuestionNote}
                  onRemoveNote={handleRemoveNote}
                  focusQuestionId={
                    pendingQuestion?.examId === dataset.id ? pendingQuestion.questionId : null
                  }
                  focusRequestKey={
                    pendingQuestion?.examId === dataset.id ? pendingQuestion.requestKey : null
                  }
                  onFocusComplete={handleQuestionFocusComplete}
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
      {showDesktopInstallModal && (
        <DesktopInstallModal
          isOpen={showDesktopInstallModal}
          onClose={() => setShowDesktopInstallModal(false)}
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
  continueTarget,
  continueQuestion,
  continueExam,
  onContinuePractice,
  onOpenQuestion,
  onGoMistakes,
  onGoFavorites,
}: {
  mistakes: MistakeEntry[];
  favorites: FavoriteEntry[];
  stats: PerformanceStat[];
  activeStage: "stage-1" | "stage-2";
  theme: AppTheme;
  continueTarget: LastPractice | null;
  continueQuestion: ExamDataset["questions"][number] | null;
  continueExam: ExamManifest["exams"][number] | null;
  onContinuePractice: () => void;
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
            <h2 className="mt-2 text-2xl font-semibold text-[#3f342d]">10 分鐘，把國考題拉回可掌控</h2>
          </div>
        </div>

        <button
          type="button"
          onClick={onContinuePractice}
          disabled={!continueTarget}
          className="mt-5 flex w-full flex-col gap-3 rounded-[1.15rem] border border-[#b8e2d4] bg-[#effaf5] p-4 text-left shadow-[0_12px_30px_rgba(123,190,168,0.16)] transition hover:-translate-y-0.5 hover:border-[#8fd5bd] hover:bg-[#e7f8f0] disabled:cursor-not-allowed disabled:opacity-60 sm:flex-row sm:items-center sm:justify-between"
        >
          <div className="min-w-0">
            <p className="text-xs font-bold tracking-[0.16em] text-[#4c806e]">一鍵繼續</p>
            <h3 className="mt-1 text-lg font-semibold text-[#315447]">
              {continueQuestion
                ? `從第 ${continueQuestion.question_number} 題繼續`
                : continueExam
                ? `回到 ${getExamDisplayTitle(continueExam)}`
                : "開始今天的第一題"}
            </h3>
            <p className="mt-1 line-clamp-2 text-sm leading-6 text-[#4f6f65]">
              {continueQuestion
                ? compactText(continueQuestion.question_text, 96)
                : continueExam
                ? getExamDisplayTitle(continueExam)
                : "系統會自動帶你到下一題未作答題目。"}
            </p>
          </div>
          <span className="inline-flex h-11 shrink-0 items-center justify-center gap-2 rounded-full bg-[#b8e2d4] px-4 text-sm font-bold text-[#315447]">
            繼續練習
            <ArrowRight size={16} />
          </span>
        </button>

        <div className="mt-3 grid gap-3 md:grid-cols-3">
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
  const validTags: FavoriteTag[] = ["高頻", "易混淆", "考前必看", "秒殺數字"];

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

function formatLocalDateKey(date: Date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}


