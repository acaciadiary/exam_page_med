import {
  BookOpenCheck,
  ChevronDown,
  ClipboardX,
  Layers3,
  NotebookPen,
  PencilLine,
  RotateCcw,
} from "lucide-react";
import { useMemo, type ReactNode } from "react";
import clsx from "clsx";
import type { AppPage } from "../app/routes";
import {
  findExamForYear,
  getAvailableYears,
  getExamStage,
  getStageLabel,
  getSubjectLabel,
  groupExamsByStage,
} from "../lib/examMetadata";
import type { ExamManifestItem, Mode } from "../types/exam";
import { ThemeToggle } from "./ThemeToggle";

type AppShellProps = {
  children: ReactNode;
  exams: ExamManifestItem[];
  activeExamId: string;
  page: AppPage;
  mode: Mode;
  theme: "light" | "dark";
  answeredCount: number;
  questionCount: number;
  wrongQuestionCount: number;
  stickyNoteCount: number;
  onExamChange: (examId: string) => void;
  onPageChange: (page: AppPage) => void;
  onModeChange: (mode: Mode) => void;
  onThemeToggle: () => void;
  onReset: () => void;
};

export function AppShell({
  children,
  exams,
  activeExamId,
  page,
  mode,
  theme,
  answeredCount,
  questionCount,
  wrongQuestionCount,
  stickyNoteCount,
  onExamChange,
  onPageChange,
  onModeChange,
  onThemeToggle,
  onReset,
}: AppShellProps) {
  const groupedExams = groupExamsByStage(exams);
  const activeExam = exams.find((exam) => exam.id === activeExamId);
  const activeStage = activeExam ? getExamStage(activeExam) : "stage-1";
  const years = useMemo(() => getAvailableYears(exams), [exams]);
  const activeYear = activeExam?.year ?? years[0] ?? "";
  const activeStageExams = groupedExams[activeStage].filter(
    (exam) => exam.year === activeYear,
  );
  const progress =
    questionCount === 0 ? 0 : Math.round((answeredCount / questionCount) * 100);

  const handleStageChange = (stage: "stage-1" | "stage-2") => {
    const firstExam =
      groupedExams[stage].find((exam) => exam.year === activeYear) ??
      groupedExams[stage][0];

    if (firstExam) {
      onExamChange(firstExam.id);
    }
  };

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
        <div className="font-hand mx-auto max-w-[92rem] rounded-[1.5rem] border border-white/80 bg-white/78 px-4 py-4 shadow-[0_18px_60px_rgba(181,133,117,0.18)] backdrop-blur-2xl sm:px-6 lg:px-8">
          <div className="flex flex-col gap-4">
            <div className="flex flex-col gap-4 xl:flex-row xl:items-center xl:justify-between">
              <div className="flex items-center gap-3">
                <div className="flex h-11 w-11 items-center justify-center rounded-[1.1rem] border border-[#f7cddd] bg-[#ffe7ef] text-[#b65f7c] shadow-[0_8px_24px_rgba(118,91,78,0.12)]">
                  <PencilLine size={22} />
                </div>
                <div>
                  <h1 className="text-xl font-semibold tracking-[0.04em] text-[#3f342d] sm:text-2xl">
                    醫師國考複習站
                  </h1>
                  <p className="mt-1 text-xs font-semibold tracking-[0.14em] text-[#8b7666]">
                    年份、考試與題庫都能直接切換
                  </p>
                </div>
              </div>

              <div className="flex flex-wrap items-center gap-2">
                <PageButton
                  active={page === "exam"}
                  onClick={() => onPageChange("exam")}
                >
                  考題練習
                </PageButton>
                <PageButton
                  active={page === "mistakes"}
                  onClick={() => onPageChange("mistakes")}
                  icon={<ClipboardX size={16} />}
                  badge={wrongQuestionCount}
                >
                  我的錯題本
                </PageButton>
                <PageButton
                  active={page === "notes"}
                  onClick={() => onPageChange("notes")}
                  icon={<NotebookPen size={16} />}
                  badge={stickyNoteCount}
                >
                  我的便利貼
                </PageButton>
                <ThemeToggle theme={theme} onToggle={onThemeToggle} />
              </div>
            </div>

            <div className="grid gap-3 xl:grid-cols-[13rem_auto_minmax(16rem,24rem)_auto]">
              <SelectGroup label="年份">
                <select
                  value={activeYear}
                  onChange={(event) => {
                    const nextExam = findExamForYear({
                      exams,
                      year: event.target.value,
                      activeExam,
                      activeStage,
                    });

                    if (nextExam) {
                      onExamChange(nextExam.id);
                    }
                  }}
                  className={selectClassName}
                  aria-label="選擇年份"
                >
                  {years.map((year) => (
                    <option key={year} value={year}>
                      {year}
                    </option>
                  ))}
                </select>
              </SelectGroup>

              <div className="min-w-0">
                <p className="mb-2 text-xs font-semibold tracking-[0.14em] text-[#8b7666]">
                  考試
                </p>
                <div className="inline-flex h-11 rounded-[0.85rem] border border-[#e6d6c9] bg-white/80 p-1">
                  <SegmentButton
                    active={activeStage === "stage-1"}
                    onClick={() => handleStageChange("stage-1")}
                  >
                    {getStageLabel("stage-1")}
                  </SegmentButton>
                  <SegmentButton
                    active={activeStage === "stage-2"}
                    onClick={() => handleStageChange("stage-2")}
                  >
                    {getStageLabel("stage-2")}
                  </SegmentButton>
                </div>
              </div>

              <SelectGroup label="目前題庫">
                <select
                  value={activeExam?.id ?? ""}
                  onChange={(event) => onExamChange(event.target.value)}
                  className={selectClassName}
                  aria-label="選擇目前題庫"
                >
                  {activeStageExams.map((exam) => (
                    <option key={exam.id} value={exam.id}>
                      {getSubjectLabel(exam)}
                    </option>
                  ))}
                </select>
              </SelectGroup>

              <div className="flex flex-wrap items-start justify-start gap-2 xl:justify-end">
                <SummaryPill>作答進度：{answeredCount} / {questionCount}</SummaryPill>
                <SummaryPill>完成率：{progress}%</SummaryPill>
              </div>
            </div>

            <div className="flex flex-wrap items-center gap-2 border-t border-[#f0ded6] pt-4">
              <div className="inline-flex h-11 rounded-[0.85rem] border border-[#e6d6c9] bg-white/80 p-1">
                <ModeButton
                  active={mode === "exam"}
                  onClick={() => onModeChange("exam")}
                  icon={<BookOpenCheck size={16} />}
                >
                  作答模式
                </ModeButton>
                <ModeButton
                  active={mode === "flashcards"}
                  onClick={() => onModeChange("flashcards")}
                  icon={<Layers3 size={16} />}
                >
                  背卡模式
                </ModeButton>
              </div>

              <button
                type="button"
                onClick={onReset}
                className="inline-flex h-11 items-center justify-center gap-2 rounded-[0.85rem] border border-[#e6d6c9] bg-white/80 px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
              >
                <RotateCcw size={16} />
                清空本卷作答
              </button>
            </div>
          </div>
        </div>
      </header>

      <main className="relative z-10 mx-auto max-w-[92rem] px-4 py-8 sm:px-6 lg:px-8">
        {children}
      </main>
    </div>
  );
}

const selectClassName =
  "h-11 w-full appearance-none rounded-[0.85rem] border border-[#e6d6c9] bg-white/84 px-4 pr-10 text-sm font-semibold text-[#6f5b50] outline-none transition hover:border-[#f1aac8] focus:border-[#f1aac8] focus:ring-4 focus:ring-[#ffd9e8]/55";

function SelectGroup({
  label,
  children,
}: {
  label: string;
  children: ReactNode;
}) {
  return (
    <label className="block min-w-0">
      <span className="mb-2 block text-xs font-semibold tracking-[0.14em] text-[#8b7666]">
        {label}
      </span>
      <span className="relative block">
        {children}
        <ChevronDown
          size={16}
          className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-[#9a7469]"
        />
      </span>
    </label>
  );
}

function SegmentButton({
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
      onClick={onClick}
      className={clsx(
        "inline-flex min-w-24 items-center justify-center rounded-[0.7rem] px-4 text-sm font-semibold transition",
        active
          ? "bg-[#f7e2ea] text-[#8a4561] shadow-[0_10px_24px_rgba(181,133,117,0.18)]"
          : "text-[#806b60] hover:bg-white hover:text-[#3f342d]",
      )}
    >
      {children}
    </button>
  );
}

function PageButton({
  active,
  onClick,
  children,
  icon,
  badge,
}: {
  active: boolean;
  onClick: () => void;
  children: ReactNode;
  icon?: ReactNode;
  badge?: number;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={clsx(
        "inline-flex h-11 items-center gap-2 rounded-full border px-4 text-sm font-semibold transition",
        active
          ? "border-[#f1aac8] bg-[#ffddea] text-[#9a496b] shadow-[0_8px_24px_rgba(238,148,185,0.22)]"
          : "border-[#efd9d0] bg-white/80 text-[#6f5b50] hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]",
      )}
    >
      {icon}
      <span>{children}</span>
      {typeof badge === "number" && badge > 0 ? (
        <span className="inline-flex min-w-6 items-center justify-center rounded-full bg-white/80 px-2 py-0.5 text-xs font-bold text-[#9a496b]">
          {badge}
        </span>
      ) : null}
    </button>
  );
}

function SummaryPill({ children }: { children: ReactNode }) {
  return (
    <div className="inline-flex h-11 items-center rounded-full border border-[#efd9d0] bg-white/82 px-4 text-sm font-semibold text-[#6f5b50]">
      {children}
    </div>
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
        "inline-flex min-w-24 items-center justify-center gap-2 rounded-[0.7rem] px-3 text-sm font-semibold transition",
        active
          ? "bg-[#dce8dc] text-[#405d49] shadow-[0_8px_20px_rgba(111,128,106,0.16)]"
          : "text-[#806b60] hover:bg-white hover:text-[#3f342d]",
      )}
    >
      {icon}
      {children}
    </button>
  );
}
