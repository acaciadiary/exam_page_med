import {
  ArrowUp,
  BookOpenCheck,
  ChevronDown,
  Clock3,
  Layers3,
  Pause,
  PencilLine,
  Play,
  RotateCcw,
  StickyNote,
  Trash2,
} from "lucide-react";
import { useEffect, useMemo, useState, type ReactNode } from "react";
import clsx from "clsx";
import { useHorizontalDragScroll } from "../hooks/useHorizontalDragScroll";
import type { ExamManifestItem, Mode } from "../types/exam";
import { useLocalStorage } from "../hooks/useLocalStorage";
import { storageKeys } from "../lib/storageKeys";
import { ThemeToggle } from "./ThemeToggle";

type ExamStage = "stage-1" | "stage-2";

type StickyNoteItem = {
  id: string;
  text: string;
  createdAt: string;
};

type AppShellProps = {
  children: ReactNode;
  exams: ExamManifestItem[];
  activeExamId: string;
  mode: Mode;
  theme: "light" | "dark";
  answeredCount: number;
  questionCount: number;
  onExamChange: (examId: string) => void;
  onModeChange: (mode: Mode) => void;
  onThemeToggle: () => void;
  onReset: () => void;
};

export function AppShell({
  children,
  exams,
  activeExamId,
  mode,
  theme,
  answeredCount,
  questionCount,
  onExamChange,
  onModeChange,
  onThemeToggle,
  onReset,
}: AppShellProps) {
  const dragScrollProps = useHorizontalDragScroll();
  const progress =
    questionCount === 0 ? 0 : Math.round((answeredCount / questionCount) * 100);
  const groupedExams = groupExamsByStage(exams);
  const activeExam = exams.find((exam) => exam.id === activeExamId);
  const activeStage = activeExam ? getExamStage(activeExam) : "stage-1";
  const activeStageExams = groupedExams[activeStage];
  const years = useMemo(() => getAvailableYears(exams), [exams]);
  const activeYear = activeExam?.year ?? years[0] ?? "";

  return (
    <div
      className={clsx(
        "study-journal min-h-screen overflow-hidden bg-[#fff8f4] text-[#4b3b35] transition-colors duration-500",
        theme === "dark" && "theme-dark bg-[#19161e] text-[#f8edf3]",
      )}
    >
      <div
        className={clsx(
          "pointer-events-none fixed inset-0 z-0 bg-[url('/assets/pastel-study-desk.png')] bg-cover bg-top opacity-35 transition-opacity duration-500",
          theme === "dark" && "opacity-10",
        )}
      />
      <div
        className={clsx(
          "pointer-events-none fixed inset-0 z-0 bg-[linear-gradient(180deg,rgba(255,248,244,0.74)_0%,rgba(255,248,244,0.92)_38%,#fff8f4_100%)] transition-opacity duration-500",
          theme === "dark" && "opacity-0",
        )}
      />
      <div
        className={clsx(
          "pointer-events-none fixed inset-0 z-0 bg-[linear-gradient(180deg,rgba(25,22,30,0.68)_0%,rgba(25,22,30,0.9)_42%,#19161e_100%)] transition-opacity duration-500",
          theme === "dark" ? "opacity-100" : "opacity-0",
        )}
      />
      <div className="pointer-events-none fixed inset-0 z-0 journal-paper opacity-70" />

      <header className="sticky top-0 z-40 px-3 pt-3 sm:px-5 sm:pt-5">
        <div className="font-hand mx-auto flex max-w-[92rem] flex-col gap-4 rounded-[1.5rem] border border-white/80 bg-white/72 px-4 py-4 shadow-[0_18px_60px_rgba(181,133,117,0.18)] backdrop-blur-2xl sm:px-6 lg:flex-row lg:items-center lg:justify-between lg:px-8">
          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-[1.1rem] border border-[#f7cddd] bg-[#ffe7ef] text-[#b65f7c] shadow-[0_8px_24px_rgba(118,91,78,0.12)]">
              <PencilLine size={22} />
            </div>
            <div>
              <h1 className="text-xl font-semibold tracking-[0.05em] text-[#3f342d] sm:text-2xl">
                醫師國考複習筆記
              </h1>
              <p className="mt-1 text-xs font-semibold tracking-[0.14em] text-[#8b7666]">
                你的專屬筆記
              </p>
            </div>
          </div>

          <div className="flex flex-col gap-3 lg:items-end">
            {years.length > 0 && (
              <div
                className="inline-flex rounded-[0.75rem] border border-[#e6d6c9] bg-white/70 p-1"
                aria-label="選擇題庫年份"
              >
                {years.map((year) => (
                  <YearButton
                    key={year}
                    active={year === activeYear}
                    onClick={() => {
                      const nextExam = findExamForYear({
                        exams,
                        year,
                        activeExam,
                        activeStage,
                      });
                      if (nextExam) onExamChange(nextExam.id);
                    }}
                  >
                    {year} 年
                  </YearButton>
                ))}
              </div>
            )}

            <div
              className="inline-flex rounded-[0.75rem] border border-[#e6d6c9] bg-white/70 p-1"
              aria-label="選擇考試階段"
            >
              <StageButton
                active={activeStage === "stage-1"}
                onClick={() => {
                  const firstExam =
                    groupedExams["stage-1"].find((exam) => exam.year === activeYear) ??
                    groupedExams["stage-1"][0];
                  if (firstExam) onExamChange(firstExam.id);
                }}
                title="醫師一"
                description="基礎醫學"
              />
              <StageButton
                active={activeStage === "stage-2"}
                onClick={() => {
                  const firstExam =
                    groupedExams["stage-2"].find((exam) => exam.year === activeYear) ??
                    groupedExams["stage-2"][0];
                  if (firstExam) onExamChange(firstExam.id);
                }}
                title="醫師二"
                description="臨床醫學"
              />
            </div>

            <div className="flex flex-col gap-3 sm:flex-row sm:items-center">
              <div
                {...dragScrollProps}
                className="horizontal-drag-scroll flex max-w-full gap-2 rounded-[0.75rem] border border-[#e6d6c9] bg-white/62 p-1"
                aria-label="考科可左右滑動"
              >
                {activeStageExams.map((exam) => (
                  <SubjectButton
                    key={exam.id}
                    active={exam.id === activeExamId}
                    onClick={() => onExamChange(exam.id)}
                  >
                    {getSubjectLabel(exam)}
                  </SubjectButton>
                ))}
              </div>

              <div className="inline-flex h-11 rounded-[0.75rem] border border-[#e6d6c9] bg-white/70 p-1">
                <ModeButton
                  active={mode === "exam"}
                  onClick={() => onModeChange("exam")}
                  icon={<BookOpenCheck size={16} />}
                >
                  考題
                </ModeButton>
                <ModeButton
                  active={mode === "flashcards"}
                  onClick={() => onModeChange("flashcards")}
                  icon={<Layers3 size={16} />}
                >
                  閃卡
                </ModeButton>
              </div>

              <button
                type="button"
                onClick={onReset}
                className="inline-flex h-11 items-center justify-center gap-2 rounded-[0.75rem] border border-[#e6d6c9] bg-white/70 px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#b8c4a7] hover:bg-[#f5f0e8] hover:text-[#3f342d]"
              >
                <RotateCcw size={16} />
                重置
              </button>

              <ThemeToggle theme={theme} onToggle={onThemeToggle} />
            </div>
          </div>
        </div>
      </header>

      <main className="relative z-10 mx-auto max-w-[92rem] px-4 py-8 sm:px-6 lg:px-8">
        <section className="mb-8 grid gap-6 pb-7 lg:grid-cols-[1fr_24rem] lg:items-end">
          <div>
          <p className="font-hand text-xs font-bold tracking-[0.18em] text-[#c4869b]">
            MY STUDY JOURNAL
          </p>
          <div className="mt-4 flex flex-col gap-5">
            <div>
              <h2 className="journal-title text-[clamp(3rem,8vw,6.8rem)] font-semibold leading-[0.9] tracking-normal text-[#3f342d]">
                Study with
                <span className="block text-[#e8a9bd]">Ariel</span>
              </h2>
              <p className="mt-5 max-w-2xl text-base leading-8 text-[#6f5b50]">
                讀一點、貼一點，把想回頭再看的題目輕輕標下來；配著計時與便利貼，慢慢收進自己的考前小本本。
              </p>
            </div>
          </div>
          </div>

            <div className="w-full max-w-md rounded-[1.35rem] border border-white/80 bg-white/72 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.18)] backdrop-blur-2xl">
              <div className="mb-2 flex items-center justify-between text-xs font-semibold tracking-[0.12em] text-[#8b7666]">
                <span>目前進度</span>
                <span>{answeredCount} / {questionCount} 題</span>
              </div>
              <div className="h-2 overflow-hidden rounded-full bg-[#eaded3]">
                <div
                  className="h-full rounded-full bg-gradient-to-r from-[#f6a9c6] via-[#b8e2d4] to-[#b8d8ff] transition-all duration-500"
                  style={{ width: `${progress}%` }}
                />
              </div>
              <p className="mt-3 text-sm leading-6 text-[#7b665b]">
                {activeExam?.title ?? "目前題庫"}，完成 {progress}%。
              </p>
            </div>
        </section>

        {children}
      </main>
      <FloatingStudyTools />
    </div>
  );
}

function YearButton({
  active,
  onClick,
  children,
}: {
  active: boolean;
  onClick: () => void;
  children: ReactNode;
}) {
  return (
    <button
      type="button"
      onPointerDown={(event) => event.stopPropagation()}
      onClick={onClick}
      className={clsx(
        "h-10 shrink-0 rounded-[0.6rem] px-4 text-sm font-semibold transition",
        active
          ? "bg-[#e7ecd8] text-[#4f634b] shadow-[0_8px_20px_rgba(111,128,106,0.16)]"
          : "text-[#806b60] hover:bg-white/80 hover:text-[#3f342d]",
      )}
    >
      {children}
    </button>
  );
}

function StageButton({
  active,
  onClick,
  title,
  description,
}: {
  active: boolean;
  onClick: () => void;
  title: string;
  description: string;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={clsx(
        "flex min-w-32 flex-col items-center justify-center rounded-[0.65rem] px-5 py-2 text-center transition",
        active
          ? "bg-[#f0e5d6] text-[#66513f] shadow-[0_10px_24px_rgba(118,91,78,0.14)]"
          : "text-[#806b60] hover:bg-white/70 hover:text-[#3f342d]",
      )}
    >
      <span className="text-sm font-bold tracking-[0.12em]">{title}</span>
      <span className="mt-0.5 text-[0.68rem] font-semibold tracking-[0.14em] opacity-75">
        {description}
      </span>
    </button>
  );
}

function FloatingStudyTools() {
  const [visible, setVisible] = useState(false);
  const [running, setRunning] = useState(false);
  const [panelOpen, setPanelOpen] = useState(false);
  const [draft, setDraft] = useState("");
  const [seconds, setSeconds] = useLocalStorage(storageKeys.focusSeconds, 0);
  const [notes, setNotes] = useLocalStorage<StickyNoteItem[]>(
    storageKeys.stickyNotes,
    [],
  );

  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > 180);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    if (!running) return undefined;

    const timerId = window.setInterval(() => {
      setSeconds((current) => current + 1);
    }, 1000);

    return () => window.clearInterval(timerId);
  }, [running, setSeconds]);

  const addNote = () => {
    const text = draft.trim();
    if (!text) return;

    setNotes((current) => [
      {
        id: `${Date.now()}-${Math.random().toString(36).slice(2)}`,
        text,
        createdAt: new Date().toISOString(),
      },
      ...current,
    ]);
    setDraft("");
  };

  const removeNote = (id: string) => {
    setNotes((current) => current.filter((note) => note.id !== id));
  };

  return (
    <div
      className={clsx(
        "fixed bottom-5 right-4 z-50 flex flex-col items-end gap-3 transition duration-300 sm:bottom-6 sm:right-6",
        visible
          ? "pointer-events-auto translate-y-0 opacity-100"
          : "pointer-events-none translate-y-4 opacity-0",
      )}
    >
      {panelOpen && (
        <div className="font-hand flex max-h-[calc(100vh-8.5rem)] w-[min(calc(100vw-2rem),24rem)] flex-col overflow-hidden rounded-[1.4rem] border border-white/80 bg-white/86 p-4 text-[#4b3b35] shadow-[0_22px_70px_rgba(181,133,117,0.22)] backdrop-blur-2xl">
          <div className="relative z-10 flex shrink-0 items-start justify-between gap-3">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.2em] text-[#c4869b]">
                Memo notes
              </p>
              <h2 className="mt-1 text-lg font-semibold">我的便利貼</h2>
            </div>
            <button
              type="button"
              aria-label="關閉便利貼"
              title="關閉便利貼"
              onClick={() => setPanelOpen(false)}
              className="rounded-full p-2 text-[#8d7167] transition hover:bg-[#fff0f6] hover:text-[#9a496b]"
            >
              <ChevronDown size={17} />
            </button>
          </div>

          <textarea
            value={draft}
            onChange={(event) => setDraft(event.target.value)}
            placeholder="寫下自己的記憶法、口訣或易錯提醒..."
            rows={4}
            className="mt-4 w-full resize-none rounded-[1rem] border border-[#efd9d0] bg-[#fffaf7]/82 px-4 py-3 text-sm leading-6 text-[#604b43] outline-none transition placeholder:text-[#aa8a7d] focus:border-[#f1aac8] focus:ring-4 focus:ring-[#ffd9e8]/55"
          />
          <div className="mt-3 flex shrink-0 items-center justify-between gap-3">
            <p className="text-xs leading-5 text-[#8a7066]">
              只存在這台裝置，不會公開分享。
            </p>
            <button
              type="button"
              onClick={addNote}
              className="shrink-0 rounded-full bg-[#b8e2d4] px-4 py-2 text-sm font-semibold text-[#355249] shadow-[0_8px_22px_rgba(123,190,168,0.24)] transition hover:-translate-y-0.5"
            >
              貼上
            </button>
          </div>

          <div className="mt-4 min-h-0 flex-1 space-y-3 overflow-y-auto pr-1">
            {notes.length === 0 ? (
              <div className="rounded-[1rem] border border-dashed border-[#efd9d0] bg-white/58 px-4 py-5 text-sm leading-6 text-[#8a7066]">
                目前還沒有便利貼。可以先記一句「看到什麼關鍵字 → 想到什麼答案」。
              </div>
            ) : (
              notes.map((note) => (
                <div
                  key={note.id}
                  className="rotate-[-0.4deg] rounded-[1rem] border border-[#f2d7a9] bg-[#fff8df] px-4 py-3 text-sm leading-6 text-[#604b43] shadow-sm"
                >
                  <div className="flex items-start justify-between gap-3">
                    <p className="whitespace-pre-wrap">{note.text}</p>
                    <button
                      type="button"
                      aria-label="刪除便利貼"
                      title="刪除便利貼"
                      onClick={() => removeNote(note.id)}
                      className="shrink-0 rounded-full p-1.5 text-[#9d7b58] transition hover:bg-white/70 hover:text-[#9a496b]"
                    >
                      <Trash2 size={14} />
                    </button>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      )}

      <div className="font-hand flex items-center gap-2 rounded-full border border-[#efd9d0] bg-white/84 p-1.5 text-[#7d6259] shadow-[0_16px_42px_rgba(181,133,117,0.22)] backdrop-blur-xl">
        <button
          type="button"
          onClick={() => setRunning((value) => !value)}
          className={clsx(
            "inline-flex h-10 items-center gap-2 rounded-full px-3 text-sm font-semibold transition hover:-translate-y-0.5",
            running
              ? "bg-[#ffe7ef] text-[#9a496b]"
              : "bg-[#b8e2d4] text-[#355249]",
          )}
          aria-label={running ? "暫停專注計時" : "開始專注計時"}
          title={running ? "暫停專注計時" : "開始專注計時"}
        >
          {running ? <Pause size={15} /> : <Play size={15} />}
          <Clock3 size={15} />
          {formatFocusTime(seconds)}
        </button>
        <button
          type="button"
          onClick={() => {
            setRunning(false);
            setSeconds(0);
          }}
          className="inline-flex h-10 w-10 items-center justify-center rounded-full text-[#8d7167] transition hover:bg-[#fff0f6] hover:text-[#9a496b]"
          aria-label="重置專注計時"
          title="重置專注計時"
        >
          <RotateCcw size={15} />
        </button>
        <button
          type="button"
          onClick={() => setPanelOpen((value) => !value)}
          className={clsx(
            "inline-flex h-10 w-10 items-center justify-center rounded-full transition hover:-translate-y-0.5",
            panelOpen ? "bg-[#ffddea] text-[#9a496b]" : "text-[#8d7167] hover:bg-[#fff0f6]",
          )}
          aria-label="開關我的便利貼"
          title="我的便利貼"
        >
          <StickyNote size={17} />
        </button>
        <button
          type="button"
          aria-label="返回頂部"
          title="返回頂部"
          onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
          className="inline-flex h-10 w-10 items-center justify-center rounded-full text-[#8d7167] transition hover:-translate-y-0.5 hover:bg-[#fff0f6] hover:text-[#9a496b]"
        >
          <ArrowUp size={18} />
        </button>
      </div>
    </div>
  );
}

function formatFocusTime(totalSeconds: number) {
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  if (hours > 0) {
    return `${hours}:${minutes.toString().padStart(2, "0")}:${seconds
      .toString()
      .padStart(2, "0")}`;
  }

  return `${minutes.toString().padStart(2, "0")}:${seconds
    .toString()
    .padStart(2, "0")}`;
}

function SubjectButton({
  active,
  onClick,
  children,
}: {
  active: boolean;
  onClick: () => void;
  children: ReactNode;
}) {
  return (
    <button
      type="button"
      onPointerDown={(event) => event.stopPropagation()}
      onClick={onClick}
      className={clsx(
        "h-10 shrink-0 rounded-[0.6rem] px-4 text-sm font-semibold transition",
        active
          ? "bg-[#d9e6ed] text-[#3e5965] shadow-[0_8px_20px_rgba(93,128,145,0.16)]"
          : "text-[#806b60] hover:bg-white/80 hover:text-[#3f342d]",
      )}
    >
      {children}
    </button>
  );
}

function ModeButton({
  active,
  onClick,
  icon,
  children,
}: {
  active: boolean;
  onClick: () => void;
  icon: ReactNode;
  children: ReactNode;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={clsx(
        "inline-flex min-w-20 items-center justify-center gap-2 rounded-[0.6rem] px-3 text-sm font-semibold transition",
        active
          ? "bg-[#dce8dc] text-[#405d49] shadow-[0_8px_20px_rgba(111,128,106,0.16)]"
          : "text-[#806b60] hover:text-[#3f342d]",
      )}
    >
      {icon}
      {children}
    </button>
  );
}

function groupExamsByStage(exams: ExamManifestItem[]) {
  return exams.reduce<Record<ExamStage, ExamManifestItem[]>>(
    (groups, exam) => {
      groups[getExamStage(exam)].push(exam);
      return groups;
    },
    { "stage-1": [], "stage-2": [] },
  );
}

function getExamStage(exam: ExamManifestItem): ExamStage {
  const subjectNumber = getSubjectNumber(exam);
  return subjectNumber <= 2 ? "stage-1" : "stage-2";
}

function getSubjectLabel(exam: ExamManifestItem) {
  const subjectNumber = getSubjectNumber(exam);
  const labels: Record<number, string> = {
    1: "醫學（一）",
    2: "醫學（二）",
    3: "醫學（三）",
    4: "醫學（四）",
    5: "醫學（五）",
    6: "醫學（六）",
  };

  return labels[subjectNumber] ?? exam.title;
}

function getSubjectNumber(exam: ExamManifestItem) {
  const match = exam.subject.match(/medicine-(\d+)/);
  return match ? Number(match[1]) : 1;
}

function getAvailableYears(exams: ExamManifestItem[]) {
  return Array.from(new Set(exams.map((exam) => exam.year))).sort((a, b) =>
    b.localeCompare(a, "zh-Hant", { numeric: true }),
  );
}

function findExamForYear({
  exams,
  year,
  activeExam,
  activeStage,
}: {
  exams: ExamManifestItem[];
  year: string;
  activeExam?: ExamManifestItem;
  activeStage: ExamStage;
}) {
  const sameSubject = activeExam
    ? exams.find((exam) => exam.year === year && exam.subject === activeExam.subject)
    : undefined;

  return (
    sameSubject ??
    exams.find((exam) => exam.year === year && getExamStage(exam) === activeStage) ??
    exams.find((exam) => exam.year === year)
  );
}
