import {
  ArrowUp,
  BookOpenCheck,
  BookmarkCheck,
  ChevronDown,
  ClipboardX,
  Layers3,
  NotebookPen,
  PencilLine,
  RotateCcw,
} from "lucide-react";
import { useMemo, useState, type ReactNode } from "react";
import clsx from "clsx";
import type { AppPage } from "../app/routes";
import {
  findExamForYear,
  getAvailableYears,
  getExamStage,
  getStageLabel,
  getSubjectLabel,
  getSubjectNumber,
  groupExamsByStage,
} from "../lib/examMetadata";
import type { ExamManifestItem, Mode } from "../types/exam";
import { ThemeToggle, type AppTheme } from "./ThemeToggle";

type AppShellProps = {
  children: ReactNode;
  exams: ExamManifestItem[];
  activeExamId: string;
  page: AppPage;
  mode: Mode;
  theme: AppTheme;
  answeredCount: number;
  questionCount: number;
  wrongQuestionCount: number;
  favoriteCount: number;
  stickyNoteCount: number;
  onExamChange: (examId: string) => void;
  onPageChange: (page: AppPage) => void;
  onModeChange: (mode: Mode) => void;
  onThemeChange: (theme: AppTheme) => void;
  onReset: () => void;
};

type DropdownOption = {
  label: string;
  value: string;
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
  favoriteCount,
  stickyNoteCount,
  onExamChange,
  onPageChange,
  onModeChange,
  onThemeChange,
  onReset,
}: AppShellProps) {
  const groupedExams = groupExamsByStage(exams);
  const activeExam = exams.find((exam) => exam.id === activeExamId);
  const activeStage = activeExam ? getExamStage(activeExam) : "stage-1";
  const years = useMemo(() => getAvailableYears(exams), [exams]);
  const activeYear = activeExam?.year ?? years[0] ?? "";
  const activeStageExams = groupedExams[activeStage]
    .filter((exam) => exam.year === activeYear)
    .sort((left, right) => getSubjectNumber(left) - getSubjectNumber(right));
  const progress =
    questionCount === 0 ? 0 : Math.round((answeredCount / questionCount) * 100);

  const yearOptions = years.map((year) => ({ label: year, value: year }));
  const subjectOptions = activeStageExams.map((exam) => ({
    label: getSubjectLabel(exam),
    value: exam.id,
  }));

  const handleStageChange = (stage: "stage-1" | "stage-2") => {
    const firstExam =
      groupedExams[stage].find((exam) => exam.year === activeYear) ??
      groupedExams[stage][0];

    if (firstExam) onExamChange(firstExam.id);
  };

  const handleYearChange = (year: string) => {
    const nextExam = findExamForYear({
      exams,
      year,
      activeExam,
      activeStage,
    });

    if (nextExam) onExamChange(nextExam.id);
  };

  return (
    <div
      className={clsx(
        "study-journal min-h-screen overflow-hidden bg-[#fff8f4] text-[#4b3b35] transition-colors duration-500",
        theme === "dark" && "theme-dark bg-[#19161e] text-[#f8edf3]",
        theme === "clinical" && "theme-clinical bg-[#f4f8fb] text-[#26384a]",
      )}
    >
      <div
        className={clsx(
          "pointer-events-none fixed inset-0 z-0 bg-[url('/assets/pastel-study-desk.png')] bg-cover bg-top opacity-35 transition-opacity duration-500",
          theme === "dark" && "opacity-10",
          theme === "clinical" && "opacity-12 saturate-50",
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
                    醫師國考複習筆記
                  </h1>
                  <p className="mt-1 text-xs font-semibold tracking-[0.14em] text-[#8b7666]">
                    你的專屬筆記
                  </p>
                </div>
              </div>

              <div className="flex flex-wrap items-center gap-2">
                <PageButton active={page === "exam"} onClick={() => onPageChange("exam")}>
                  題庫
                </PageButton>
                <PageButton
                  active={page === "mistakes"}
                  onClick={() => onPageChange("mistakes")}
                  icon={<ClipboardX size={16} />}
                  badge={wrongQuestionCount}
                >
                  錯題
                </PageButton>
                <PageButton
                  active={page === "favorites"}
                  onClick={() => onPageChange("favorites")}
                  icon={<BookmarkCheck size={16} />}
                  badge={favoriteCount}
                >
                  收藏
                </PageButton>
                <PageButton
                  active={page === "notes"}
                  onClick={() => onPageChange("notes")}
                  icon={<NotebookPen size={16} />}
                  badge={stickyNoteCount}
                >
                  便條
                </PageButton>
                <ThemeToggle theme={theme} onChange={onThemeChange} />
              </div>
            </div>

            <div className="grid gap-3 xl:grid-cols-[13rem_auto_minmax(16rem,24rem)_auto]">
              <Dropdown label="年度" value={activeYear} options={yearOptions} onChange={handleYearChange} />

              <div className="min-w-0">
                <p className="mb-2 text-xs font-semibold tracking-[0.14em] text-[#8b7666]">
                  階段
                </p>
                <div className="inline-flex h-11 rounded-[0.85rem] border border-[#e6d6c9] bg-white/80 p-1">
                  <SegmentButton active={activeStage === "stage-1"} onClick={() => handleStageChange("stage-1")}>
                    {getStageLabel("stage-1")}
                  </SegmentButton>
                  <SegmentButton active={activeStage === "stage-2"} onClick={() => handleStageChange("stage-2")}>
                    {getStageLabel("stage-2")}
                  </SegmentButton>
                </div>
              </div>

              <Dropdown
                label="科目"
                value={activeExam?.id ?? ""}
                options={subjectOptions}
                onChange={onExamChange}
              />

              <div className="flex flex-wrap items-start justify-start gap-2 xl:justify-end">
                <SummaryPill>已作答：{answeredCount} / {questionCount}</SummaryPill>
                <SummaryPill>完成度：{progress}%</SummaryPill>
              </div>
            </div>

            <div className="flex flex-wrap items-center gap-2 border-t border-[#f0ded6] pt-4">
              <div className="inline-flex h-11 rounded-[0.85rem] border border-[#e6d6c9] bg-white/80 p-1">
                <ModeButton active={mode === "exam"} onClick={() => onModeChange("exam")} icon={<BookOpenCheck size={16} />}>
                  題目模式
                </ModeButton>
                <ModeButton active={mode === "flashcards"} onClick={() => onModeChange("flashcards")} icon={<Layers3 size={16} />}>
                  卡片模式
                </ModeButton>
              </div>

              <button
                type="button"
                onClick={onReset}
                className="inline-flex h-11 items-center justify-center gap-2 rounded-[0.85rem] border border-[#e6d6c9] bg-white/80 px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
              >
                <RotateCcw size={16} />
                重置本科作答
              </button>
            </div>
          </div>
        </div>
      </header>

      <main className="relative z-10 mx-auto max-w-[92rem] px-4 py-8 sm:px-6 lg:px-8">
        {children}
      </main>

      <button
        type="button"
        onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
        className="fixed bottom-5 right-5 z-50 inline-flex h-12 w-12 items-center justify-center rounded-full border border-[#f1aac8] bg-white/90 text-[#9a496b] shadow-[0_12px_34px_rgba(181,133,117,0.2)] backdrop-blur-xl transition hover:-translate-y-0.5 hover:bg-[#fff0f6] focus:outline-none focus:ring-4 focus:ring-[#ffd9e8]/55 sm:bottom-6 sm:right-6"
        aria-label="回到頂部"
        title="回到頂部"
      >
        <ArrowUp size={20} />
      </button>
    </div>
  );
}

function Dropdown({
  label,
  value,
  options,
  onChange,
}: {
  label: string;
  value: string;
  options: DropdownOption[];
  onChange: (value: string) => void;
}) {
  const [open, setOpen] = useState(false);
  const selected = options.find((option) => option.value === value);

  return (
    <div
      className="relative min-w-0"
      onBlur={(event) => {
        if (!event.currentTarget.contains(event.relatedTarget)) setOpen(false);
      }}
    >
      <p className="mb-2 text-xs font-semibold tracking-[0.14em] text-[#8b7666]">{label}</p>
      <button
        type="button"
        onClick={() => setOpen((current) => !current)}
        className="flex h-11 w-full items-center justify-between gap-3 rounded-[0.85rem] border border-[#e6d6c9] bg-white/84 px-4 text-left text-sm font-semibold text-[#6f5b50] outline-none transition hover:border-[#f1aac8] focus:border-[#f1aac8] focus:ring-4 focus:ring-[#ffd9e8]/55"
        aria-expanded={open}
      >
        <span className="truncate">{selected?.label ?? "請選擇"}</span>
        <ChevronDown size={16} className={clsx("shrink-0 text-[#9a7469] transition", open && "rotate-180")} />
      </button>

      {open && (
        <div className="absolute left-0 right-0 top-[calc(100%+0.35rem)] z-50 max-h-72 overflow-y-auto rounded-[0.9rem] border border-[#e6d6c9] bg-white/95 p-1.5 shadow-[0_18px_50px_rgba(181,133,117,0.2)] backdrop-blur-xl">
          {options.map((option) => (
            <button
              key={option.value}
              type="button"
              onMouseDown={(event) => event.preventDefault()}
              onClick={() => {
                onChange(option.value);
                setOpen(false);
              }}
              className={clsx(
                "flex h-10 w-full items-center rounded-[0.7rem] px-3 text-left text-sm font-semibold transition",
                option.value === value
                  ? "bg-[#f7e2ea] text-[#8a4561]"
                  : "text-[#806b60] hover:bg-[#fff0f6] hover:text-[#3f342d]",
              )}
            >
              {option.label}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

function SegmentButton({ active, onClick, children }: { active: boolean; onClick: () => void; children: ReactNode }) {
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
