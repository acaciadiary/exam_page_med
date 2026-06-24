import {
  ArrowUp,
  Bold,
  BookOpenCheck,
  BookmarkCheck,
  ChevronDown,
  ClipboardX,
  Download,
  NotebookPen,
  PencilLine,
  RotateCcw,
  GitCompare,
  Settings,
} from "lucide-react";
import { useMemo, useState, useEffect, type ReactNode } from "react";
import clsx from "clsx";
import { motion } from "motion/react";
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
import type { ExamManifestItem } from "../types/exam";
import { ThemeToggle, type AppTheme } from "./ThemeToggle";

type AppShellProps = {
  children: ReactNode;
  exams: ExamManifestItem[];
  activeExamId: string;
  page: AppPage;
  theme: AppTheme;
  readingBold: boolean;
  answeredCount: number;
  questionCount: number;
  wrongQuestionCount: number;
  favoriteCount: number;
  stickyNoteCount: number;
  isInstallable?: boolean;
  onInstall?: () => void;
  onExamChange: (examId: string) => void;
  onPageChange: (page: AppPage) => void;
  onThemeChange: (theme: AppTheme) => void;
  onReadingBoldChange: (enabled: boolean) => void;
  onReset: () => void;
  onResetAll: () => void;
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
  theme,
  readingBold,
  answeredCount,
  questionCount,
  wrongQuestionCount,
  favoriteCount,
  stickyNoteCount,
  isInstallable,
  onInstall,
  onExamChange,
  onPageChange,
  onThemeChange,
  onReadingBoldChange,
  onReset,
  onResetAll,
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

  const [isVisible, setIsVisible] = useState(true);
  const [lastScrollY, setLastScrollY] = useState(0);

  const handleHomeClick = () => {
    onPageChange("exam");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  useEffect(() => {
    let ticking = false;

    const handleScroll = () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          const currentScrollY = window.scrollY;
          const maxScrollY = document.documentElement.scrollHeight - window.innerHeight;

          // 1. Always show at the top of the page
          if (currentScrollY < 10) {
            setIsVisible(true);
            setLastScrollY(currentScrollY);
            ticking = false;
            return;
          }

          // 2. Always show at the bottom of the page (within 10px buffer)
          if (currentScrollY >= maxScrollY - 10) {
            setIsVisible(true);
            setLastScrollY(currentScrollY);
            ticking = false;
            return;
          }

          // 3. Threshold to avoid jittery behavior (15px)
          if (Math.abs(currentScrollY - lastScrollY) < 15) {
            ticking = false;
            return;
          }

          // 4. Determine direction
          if (currentScrollY > lastScrollY) {
            // Scrolling down -> hide
            setIsVisible(false);
          } else {
            // Scrolling up -> show
            setIsVisible(true);
          }

          setLastScrollY(currentScrollY);
          ticking = false;
        });
        ticking = true;
      }
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, [lastScrollY]);

  return (
    <div
      className={clsx(
        "study-journal min-h-screen text-[#4b3b35] transition-colors duration-500",
        theme === "light" && "bg-[#fff8f4]",
        theme === "dark" && "theme-dark bg-[#19161e] text-[#f8edf3]",
        theme === "clinical" && "theme-clinical bg-[#f4f8fb] text-[#26384a]",
        readingBold && "reading-bold",
      )}
    >
      {/* Dynamic Backgrounds */}
      <div
        className={clsx(
          "pointer-events-none fixed inset-0 z-0 bg-[url('/assets/pastel-study-desk.png')] bg-cover bg-top transition-opacity duration-500",
          theme === "light" && "opacity-35",
          theme === "dark" && "opacity-[0.04] saturate-50 brightness-50",
          theme === "clinical" && "opacity-12 saturate-50",
        )}
      />
      <div
        className={clsx(
          "pointer-events-none fixed inset-0 z-0 journal-paper transition-opacity duration-500",
          theme === "dark" ? "opacity-95" : "opacity-70",
        )}
      />

      {/* Desktop Left Fixed Sidebar */}
      <aside
        className={clsx(
          "fixed bottom-0 left-0 top-0 z-40 hidden w-64 flex-col border-r bg-white/70 backdrop-blur-xl lg:flex",
          theme === "dark"
            ? "border-white/12 bg-[#2b2430]/70"
            : theme === "clinical"
            ? "border-[#a3bed0]/45 bg-white/86"
            : "border-[#efd9d0] bg-white/70"
        )}
      >
        {/* Logo and Title */}
        <button
          type="button"
          onClick={handleHomeClick}
          className="flex w-full items-center gap-3 border-b border-[#f0ded6]/65 p-6 text-left transition hover:bg-white/45 focus:outline-none focus:ring-4 focus:ring-[#ffd9e8]/45 dark:border-white/10 dark:hover:bg-white/5"
          aria-label="回到首頁"
          title="回到首頁"
        >
          <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-[0.95rem] border border-[#f7cddd] bg-[#ffe7ef] text-[#b65f7c] shadow-[0_6px_18px_rgba(118,91,78,0.08)]">
            <PencilLine size={20} />
          </div>
          <div>
            <h1 className="text-lg font-bold tracking-[0.02em] text-[#3f342d] dark:text-[#f8edf3]">
              醫師國考
            </h1>
            <p className="text-[10px] font-semibold tracking-[0.14em] text-[#8b7666] dark:text-[#a2949e]">
              你的專屬筆記
            </p>
          </div>
        </button>

        {/* Navigation items */}
        <nav className="flex-1 space-y-1.5 p-4">
          <SidebarLink active={page === "exam"} onClick={() => onPageChange("exam")} icon={<BookOpenCheck size={18} />} theme={theme}>
            國考題
          </SidebarLink>
          <SidebarLink active={page === "diseases"} onClick={() => onPageChange("diseases")} icon={<GitCompare size={18} />} theme={theme}>
            必看區
          </SidebarLink>
          <SidebarLink
            active={page === "mistakes"}
            onClick={() => onPageChange("mistakes")}
            icon={<ClipboardX size={18} />}
            badge={wrongQuestionCount}
            theme={theme}
          >
            錯題本
          </SidebarLink>
          <SidebarLink
            active={page === "favorites"}
            onClick={() => onPageChange("favorites")}
            icon={<BookmarkCheck size={18} />}
            badge={favoriteCount}
            theme={theme}
          >
            收藏區
          </SidebarLink>
          <SidebarLink
            active={page === "notes"}
            onClick={() => onPageChange("notes")}
            icon={<NotebookPen size={18} />}
            badge={stickyNoteCount}
            theme={theme}
          >
            便條貼
          </SidebarLink>
        </nav>

        {/* Sidebar bottom settings and theme controls */}
        <div className="p-4 border-t border-[#f0ded6]/65 dark:border-white/10 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-[#8b7666] dark:text-[#a2949e]">切換主題</span>
            <div className="flex items-center gap-2">
              <ThemeToggle theme={theme} onChange={onThemeChange} />
              <ReadingBoldButton
                enabled={readingBold}
                onChange={onReadingBoldChange}
                theme={theme}
              />
            </div>
          </div>
          {isInstallable && onInstall && (
            <button
              type="button"
              onClick={onInstall}
              className="flex w-full items-center justify-center gap-2 rounded-xl border border-[#b8e2d4] bg-[#e8f4ee] py-2.5 text-sm font-semibold text-[#355249] transition hover:border-[#a5d9c7] hover:bg-[#d5ebe1] cursor-pointer"
            >
              <Download size={16} />
              <span>加入桌面</span>
            </button>
          )}
        </div>
      </aside>

      {/* Main Content Area (shifted right on Desktop) */}
      <div className="flex min-h-screen flex-col lg:pl-64">
        {/* Top Header */}
        <header
          className={clsx(
            "sticky top-0 z-30 px-3 pt-3 sm:px-5 sm:pt-5 transition-transform duration-300 ease-in-out",
            !isVisible && "max-lg:-translate-y-full"
          )}
        >
          <div className="mx-auto w-full max-w-[92rem] rounded-[1.25rem] border border-white/80 bg-white/78 px-4 py-3 shadow-[0_12px_40px_rgba(181,133,117,0.12)] backdrop-blur-2xl sm:px-6">
            {/* Desktop Header Layout */}
            <div className="hidden lg:flex items-center justify-between gap-4">
              <div className="flex items-center gap-3 min-w-0">
                <FilterControl
                  exams={exams}
                  activeExamId={activeExamId}
                  activeYear={activeYear}
                  activeStage={activeStage}
                  yearOptions={yearOptions}
                  subjectOptions={subjectOptions}
                  onExamChange={onExamChange}
                  handleYearChange={handleYearChange}
                  handleStageChange={handleStageChange}
                  onReset={onReset}
                  onResetAll={onResetAll}
                  theme={theme}
                />
              </div>
              <div className="flex items-center gap-2">
                <SummaryPill>已作答：{answeredCount} / {questionCount}</SummaryPill>
                <SummaryPill>完成度：{progress}%</SummaryPill>
              </div>
            </div>

            {/* Mobile Header Layout */}
            <div className="flex lg:hidden flex-col gap-2.5">
              {/* Row 1: Title & Theme Switch */}
              <div className="flex items-center justify-between">
                <button
                  type="button"
                  onClick={handleHomeClick}
                  className="flex min-w-0 items-center gap-2 rounded-xl pr-2 text-left transition hover:opacity-80 focus:outline-none focus:ring-4 focus:ring-[#ffd9e8]/45"
                  aria-label="回到首頁"
                  title="回到首頁"
                >
                  <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-[0.8rem] border border-[#f7cddd] bg-[#ffe7ef] text-[#b65f7c]">
                    <PencilLine size={18} />
                  </div>
                  <span className="font-hand text-lg font-bold text-[#3f342d] dark:text-[#f8edf3] truncate">
                    國考筆記
                  </span>
                </button>
                <div className="flex items-center gap-2 shrink-0">
                  <ThemeToggle theme={theme} onChange={onThemeChange} />
                  <ReadingBoldButton
                    enabled={readingBold}
                    onChange={onReadingBoldChange}
                    theme={theme}
                  />
                  {isInstallable && onInstall && (
                    <button
                      type="button"
                      onClick={onInstall}
                      className="inline-flex h-9 w-9 items-center justify-center rounded-full border border-[#b8e2d4] bg-[#e8f4ee] text-[#355249] transition hover:bg-[#d5ebe1] cursor-pointer"
                      title="加入桌面"
                    >
                      <Download size={16} />
                    </button>
                  )}
                </div>
              </div>

              {/* Row 2: Filter Controls & Mobile Progress */}
              <div className="flex items-center justify-between gap-2 border-t border-[#f0ded6]/50 dark:border-white/5 pt-2">
                <FilterControl
                  exams={exams}
                  activeExamId={activeExamId}
                  activeYear={activeYear}
                  activeStage={activeStage}
                  yearOptions={yearOptions}
                  subjectOptions={subjectOptions}
                  onExamChange={onExamChange}
                  handleYearChange={handleYearChange}
                  handleStageChange={handleStageChange}
                  onReset={onReset}
                  onResetAll={onResetAll}
                  theme={theme}
                />
                
                <div className="flex flex-col items-end text-[10px] font-semibold text-[#8b7666] dark:text-[#a2949e]">
                  <span>進度: {progress}%</span>
                  <span>{answeredCount}/{questionCount} 題</span>
                </div>
              </div>
            </div>
          </div>
        </header>

        {/* Main Content Area */}
        <main className="relative z-10 mx-auto w-full max-w-[92rem] flex-1 px-4 py-6 sm:px-6 lg:px-8 pb-24 lg:pb-8">
          {children}
        </main>
      </div>

      {/* Mobile Floating Bottom Navigation Bar */}
      <nav
        className={clsx(
          "fixed bottom-4 left-1/2 z-40 flex h-16 w-[92%] max-w-[28rem] -translate-x-1/2 items-center justify-around rounded-full border bg-white/78 px-3 shadow-[0_12px_36px_rgba(181,133,117,0.2)] backdrop-blur-2xl lg:hidden transition-transform duration-300 ease-in-out",
          theme === "dark"
            ? "border-white/10 bg-[#2b2430]/78"
            : theme === "clinical"
            ? "border-[#a3bed0]/45 bg-white/86"
            : "border-white/80 bg-white/78",
          !isVisible && "translate-y-[calc(100%+1.5rem)]"
        )}
      >
        <MobileNavLink active={page === "exam"} onClick={() => onPageChange("exam")} icon={<BookOpenCheck size={20} />} label="國考題" theme={theme} />
        <MobileNavLink active={page === "diseases"} onClick={() => onPageChange("diseases")} icon={<GitCompare size={20} />} label="必看區" theme={theme} />
        <MobileNavLink
          active={page === "mistakes"}
          onClick={() => onPageChange("mistakes")}
          icon={<ClipboardX size={20} />}
          label="錯題"
          badge={wrongQuestionCount}
          theme={theme}
        />
        <MobileNavLink
          active={page === "favorites"}
          onClick={() => onPageChange("favorites")}
          icon={<BookmarkCheck size={20} />}
          label="收藏區"
          badge={favoriteCount}
          theme={theme}
        />
        <MobileNavLink
          active={page === "notes"}
          onClick={() => onPageChange("notes")}
          icon={<NotebookPen size={20} />}
          label="便條貼"
          badge={stickyNoteCount}
          theme={theme}
        />
      </nav>

      {/* Back to top button */}
      <button
        type="button"
        onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
        className={clsx(
          "fixed right-5 z-50 inline-flex h-12 w-12 items-center justify-center rounded-full border border-[#f1aac8] bg-white/90 text-[#9a496b] shadow-[0_12px_34px_rgba(181,133,117,0.2)] backdrop-blur-xl transition-all duration-300 ease-in-out hover:-translate-y-0.5 hover:bg-[#fff0f6] focus:outline-none focus:ring-4 focus:ring-[#ffd9e8]/55 sm:right-6 lg:right-6",
          "bottom-24 sm:bottom-6 lg:bottom-6",
          !isVisible && "max-sm:translate-y-18"
        )}
        aria-label="回到頂部"
        title="回到頂部"
      >
        <ArrowUp size={20} />
      </button>
    </div>
  );
}

/* ------------------ Sub Components ------------------ */

function SidebarLink({
  active,
  onClick,
  children,
  icon,
  badge,
  theme,
}: {
  active: boolean;
  onClick: () => void;
  children: ReactNode;
  icon: ReactNode;
  badge?: number;
  theme: AppTheme;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={clsx(
        "flex w-full items-center justify-between rounded-xl px-4 py-3 text-sm font-semibold transition cursor-pointer font-hand",
        active
          ? theme === "dark"
            ? "bg-[#4a2c3a] text-[#f3a6c4]"
            : theme === "clinical"
            ? "bg-[#dbeafe] text-[#1f4e79]"
            : "bg-[#ffddea] text-[#9a496b]"
          : theme === "dark"
          ? "text-[#dccbd3] hover:bg-[#2b2430] hover:text-[#f3a6c4]"
          : theme === "clinical"
          ? "text-[#26384a] hover:bg-[#e8f2f9] hover:text-[#1f4e79]"
          : "text-[#6f5b50] hover:bg-[#fff0f6] hover:text-[#9a496b]"
      )}
    >
      <div className="flex items-center gap-3">
        <span className={clsx(
          active
            ? theme === "dark" ? "text-[#f3a6c4]" : theme === "clinical" ? "text-[#1f4e79]" : "text-[#9a496b]"
            : theme === "dark" ? "text-[#a2949e]" : theme === "clinical" ? "text-[#5b6f82]" : "text-[#9a7469]"
        )}>
          {icon}
        </span>
        <span>{children}</span>
      </div>
      {typeof badge === "number" && badge > 0 ? (
        <span className={clsx(
          "inline-flex min-w-5 h-5 items-center justify-center rounded-full px-1.5 py-0.5 text-xs font-bold border",
          theme === "dark"
            ? "bg-[#2b2430] border-white/10 text-[#f3a6c4]"
            : theme === "clinical"
            ? "bg-white border-[#c8dbe7] text-[#1f4e79]"
            : "bg-white border-[#efd9d0] text-[#9a496b]"
        )}>
          {badge}
        </span>
      ) : null}
    </button>
  );
}

function MobileNavLink({
  active,
  onClick,
  icon,
  label,
  badge,
  theme,
}: {
  active: boolean;
  onClick: () => void;
  icon: ReactNode;
  label: string;
  badge?: number;
  theme: AppTheme;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={clsx(
        "relative flex flex-col items-center justify-center w-12 h-12 rounded-xl transition cursor-pointer font-hand",
        active
          ? theme === "dark" ? "text-[#f3a6c4]" : theme === "clinical" ? "text-[#1f4e79]" : "text-[#9a496b]"
          : theme === "dark" ? "text-[#a2949e] hover:text-[#f3a6c4]" : theme === "clinical" ? "text-[#5b6f82] hover:text-[#1f4e79]" : "text-[#8b7666] hover:text-[#9a496b]"
      )}
    >
      {active && (
        <motion.div
          layoutId="mobile-nav-active"
          className={clsx(
            "absolute inset-0 rounded-xl -z-10",
            theme === "dark" ? "bg-[#4a2c3a]" : theme === "clinical" ? "bg-[#dbeafe]" : "bg-[#ffddea]"
          )}
          transition={{ type: "spring", stiffness: 380, damping: 30 }}
        />
      )}
      <span className="shrink-0">{icon}</span>
      <span className="text-[10px] font-bold tracking-[0.02em] mt-0.5">{label}</span>
      {typeof badge === "number" && badge > 0 ? (
        <span className={clsx(
          "absolute -top-1 -right-1 inline-flex min-w-4 h-4 items-center justify-center rounded-full text-[9px] font-extrabold text-white px-1 shadow-sm border",
          theme === "dark" ? "bg-[#b65f7c] border-white/10" : theme === "clinical" ? "bg-[#1f4e79] border-white" : "bg-[#f6a9c6] border-white"
        )}>
          {badge}
        </span>
      ) : null}
    </button>
  );
}

function ReadingBoldButton({
  enabled,
  onChange,
  theme,
}: {
  enabled: boolean;
  onChange: (enabled: boolean) => void;
  theme: AppTheme;
}) {
  return (
    <button
      type="button"
      onClick={() => onChange(!enabled)}
      className={clsx(
        "inline-flex h-11 w-11 shrink-0 items-center justify-center rounded-full border text-xs font-extrabold transition shadow-sm",
        enabled
          ? theme === "dark"
            ? "border-white/20 bg-[#4a2c3a] text-[#f3a6c4]"
            : theme === "clinical"
            ? "border-[#1f4e79] bg-[#dbeafe] text-[#1f4e79]"
            : "border-[#f1aac8] bg-[#ffddea] text-[#9a496b]"
          : theme === "dark"
          ? "border-white/10 bg-[#2b2430]/80 text-[#dccbd3] hover:border-white/20"
          : theme === "clinical"
          ? "border-[#c8dbe7] bg-white/80 text-[#26384a] hover:border-[#1f4e79]"
          : "border-[#e6d6c9] bg-white/80 text-[#6f5b50] hover:bg-white",
      )}
      aria-pressed={enabled}
      aria-label={enabled ? "關閉閱讀加粗" : "開啟閱讀加粗"}
      title={enabled ? "關閉閱讀加粗" : "開啟閱讀加粗"}
    >
      <Bold size={16} strokeWidth={2.6} />
    </button>
  );
}

function SummaryPill({ children }: { children: ReactNode }) {
  return (
    <div className="inline-flex h-9 items-center rounded-full border border-[#efd9d0] bg-white/82 px-3 text-xs font-semibold text-[#6f5b50] dark:border-white/10 dark:text-[#dccbd3]">
      {children}
    </div>
  );
}

function FilterControl({
  exams,
  activeExamId,
  activeYear,
  activeStage,
  yearOptions,
  subjectOptions,
  onExamChange,
  handleYearChange,
  handleStageChange,
  onReset,
  onResetAll,
  theme,
}: {
  exams: ExamManifestItem[];
  activeExamId: string;
  activeYear: string;
  activeStage: "stage-1" | "stage-2";
  yearOptions: DropdownOption[];
  subjectOptions: DropdownOption[];
  onExamChange: (id: string) => void;
  handleYearChange: (year: string) => void;
  handleStageChange: (stage: "stage-1" | "stage-2") => void;
  onReset: () => void;
  onResetAll: () => void;
  theme: AppTheme;
}) {
  const [filterOpen, setFilterOpen] = useState(false);
  const [settingsOpen, setSettingsOpen] = useState(false);

  const activeExam = exams.find((exam) => exam.id === activeExamId);
  const stageLabel = activeStage === "stage-1" ? "一階" : "二階";
  const subjectLabel = activeExam ? getSubjectLabel(activeExam) : "選擇科目";

  return (
    <div className="flex items-center gap-1.5 font-hand shrink-0">
      {/* Filter Dropdown Popover */}
      <div
        className="relative"
        onBlur={(event) => {
          if (!event.currentTarget.contains(event.relatedTarget)) setFilterOpen(false);
        }}
      >
        <button
          type="button"
          onClick={() => setFilterOpen((prev) => !prev)}
          className={clsx(
            "flex h-9 items-center gap-1.5 rounded-full border px-3.5 text-xs font-semibold outline-none transition cursor-pointer shadow-sm",
            theme === "dark"
              ? "border-white/10 bg-[#2b2430]/80 text-[#dccbd3] hover:border-white/20 focus:border-white/20 focus:ring-2 focus:ring-white/10"
              : theme === "clinical"
              ? "border-[#c8dbe7] bg-white/86 text-[#26384a] hover:border-[#1f4e79] focus:border-[#1f4e79] focus:ring-2 focus:ring-[#e8f2f9]"
              : "border-[#efd9d0] bg-white/80 text-[#6f5b50] hover:border-[#f1aac8] focus:border-[#f1aac8] focus:ring-2 focus:ring-[#ffd9e8]/55"
          )}
          aria-expanded={filterOpen}
        >
          <span>{activeYear} · {stageLabel} · {subjectLabel}</span>
          <ChevronDown size={12} className={clsx("shrink-0 transition", filterOpen && "rotate-180")} />
        </button>

        {filterOpen && (
          <div
            className={clsx(
              "absolute left-0 top-[calc(100%+0.5rem)] z-50 w-72 sm:w-80 rounded-[1.2rem] border p-4 shadow-[0_18px_50px_rgba(181,133,117,0.22)] backdrop-blur-xl space-y-4",
              theme === "dark"
                ? "border-white/15 bg-[#2b2430]/95"
                : theme === "clinical"
                ? "border-[#c8dbe7] bg-white/95"
                : "border-[#e6d6c9] bg-white/95"
            )}
          >
            {/* Year Selector */}
            <div>
              <p className="mb-2 text-[10px] font-bold uppercase tracking-[0.15em] text-[#8b7666] dark:text-[#a2949e]">年度</p>
              <div className="flex flex-wrap gap-1.5">
                {yearOptions.map((opt) => (
                  <button
                    key={opt.value}
                    type="button"
                    onMouseDown={(e) => e.preventDefault()}
                    onClick={() => handleYearChange(opt.value)}
                    className={clsx(
                      "h-7 rounded-lg px-2.5 text-xs font-semibold transition cursor-pointer",
                      opt.value === activeYear
                        ? theme === "dark"
                          ? "bg-[#4a2c3a] text-[#f3a6c4]"
                          : theme === "clinical"
                          ? "bg-[#dbeafe] text-[#1f4e79]"
                          : "bg-[#f7e2ea] text-[#8a4561]"
                        : theme === "dark"
                        ? "bg-[#201b25]/60 text-[#dccbd3] border border-white/10 hover:bg-[#2b2430]"
                        : theme === "clinical"
                        ? "bg-white/60 text-[#26384a] border border-[#c8dbe7] hover:bg-[#e8f2f9]"
                        : "bg-white/60 text-[#806b60] border border-[#e6d6c9] hover:bg-[#fff0f6]"
                    )}
                  >
                    {opt.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Stage Selector */}
            <div>
              <p className="mb-2 text-[10px] font-bold uppercase tracking-[0.15em] text-[#8b7666] dark:text-[#a2949e]">階段</p>
              <div className={clsx(
                "inline-flex h-8 rounded-lg border p-0.5",
                theme === "dark" ? "border-white/10 bg-[#201b25]/80" : theme === "clinical" ? "border-[#c8dbe7] bg-white/80" : "border-[#e6d6c9] bg-white/80"
              )}>
                <button
                  type="button"
                  onMouseDown={(e) => e.preventDefault()}
                  onClick={() => handleStageChange("stage-1")}
                  className={clsx(
                    "flex items-center justify-center rounded-[0.35rem] px-3 text-xs font-semibold transition cursor-pointer",
                    activeStage === "stage-1"
                      ? theme === "dark"
                        ? "bg-[#4a2c3a] text-[#f3a6c4]"
                        : theme === "clinical"
                        ? "bg-[#dbeafe] text-[#1f4e79]"
                        : "bg-[#f7e2ea] text-[#8a4561]"
                      : theme === "dark"
                      ? "text-[#dccbd3] hover:bg-white/5"
                      : theme === "clinical"
                      ? "text-[#26384a] hover:bg-white"
                      : "text-[#806b60] hover:bg-white"
                  )}
                >
                  第一階段
                </button>
                <button
                  type="button"
                  onMouseDown={(e) => e.preventDefault()}
                  onClick={() => handleStageChange("stage-2")}
                  className={clsx(
                    "flex items-center justify-center rounded-[0.35rem] px-3 text-xs font-semibold transition cursor-pointer",
                    activeStage === "stage-2"
                      ? theme === "dark"
                        ? "bg-[#4a2c3a] text-[#f3a6c4]"
                        : theme === "clinical"
                        ? "bg-[#dbeafe] text-[#1f4e79]"
                        : "bg-[#f7e2ea] text-[#8a4561]"
                      : theme === "dark"
                      ? "text-[#dccbd3] hover:bg-white/5"
                      : theme === "clinical"
                      ? "text-[#26384a] hover:bg-white"
                      : "text-[#806b60] hover:bg-white"
                  )}
                >
                  第二階段
                </button>
              </div>
            </div>

            {/* Subject Selector */}
            <div>
              <p className="mb-2 text-[10px] font-bold uppercase tracking-[0.15em] text-[#8b7666] dark:text-[#a2949e]">科目</p>
              <div className="grid gap-1 max-h-40 overflow-y-auto pr-1">
                {subjectOptions.map((opt) => (
                  <button
                    key={opt.value}
                    type="button"
                    onMouseDown={(e) => e.preventDefault()}
                    onClick={() => {
                      onExamChange(opt.value);
                      setFilterOpen(false);
                    }}
                    className={clsx(
                      "flex h-8 items-center rounded-lg px-2.5 text-left text-xs font-semibold transition cursor-pointer",
                      opt.value === activeExamId
                        ? theme === "dark"
                          ? "bg-[#4a2c3a] text-[#f3a6c4]"
                          : theme === "clinical"
                          ? "bg-[#dbeafe] text-[#1f4e79]"
                          : "bg-[#f7e2ea] text-[#8a4561]"
                        : theme === "dark"
                        ? "text-[#dccbd3] hover:bg-[#2b2430] hover:text-[#f3a6c4]"
                        : theme === "clinical"
                        ? "text-[#26384a] hover:bg-[#e8f2f9] hover:text-[#1f4e79]"
                        : "text-[#806b60] hover:bg-[#fff0f6] hover:text-[#3f342d]"
                    )}
                  >
                    {opt.label}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Settings Options Gear Button */}
      <div
        className="relative shrink-0"
        onBlur={(event) => {
          if (!event.currentTarget.contains(event.relatedTarget)) setSettingsOpen(false);
        }}
      >
        <button
          type="button"
          onClick={() => setSettingsOpen((prev) => !prev)}
          className={clsx(
            "flex h-9 w-9 items-center justify-center rounded-full border outline-none transition cursor-pointer shadow-sm",
            settingsOpen
              ? theme === "dark"
                ? "border-white/20 bg-[#4a2c3a] text-[#f3a6c4]"
                : theme === "clinical"
                ? "border-[#1f4e79] bg-[#dbeafe] text-[#1f4e79]"
                : "border-[#f1aac8] bg-[#ffddea] text-[#9a496b]"
              : theme === "dark"
              ? "border-white/10 bg-[#2b2430]/80 text-[#dccbd3] hover:border-white/20"
              : theme === "clinical"
              ? "border-[#c8dbe7] bg-white/80 text-[#26384a] hover:border-[#1f4e79]"
              : "border-[#efd9d0] bg-white/80 text-[#6f5b50] hover:border-[#f1aac8] hover:bg-[#fff0f6]"
          )}
          aria-label="更多選項"
        >
          <Settings size={14} />
        </button>

        {settingsOpen && (
          <div
            className={clsx(
              "absolute right-0 top-[calc(100%+0.5rem)] z-50 w-52 rounded-xl border p-1 shadow-[0_12px_36px_rgba(181,133,117,0.18)] backdrop-blur-xl",
              theme === "dark"
                ? "border-white/15 bg-[#2b2430]/95"
                : theme === "clinical"
                ? "border-[#c8dbe7] bg-white/95"
                : "border-[#e6d6c9] bg-white/95"
            )}
          >
            <button
              type="button"
              onMouseDown={(e) => e.preventDefault()}
              onClick={() => {
                onReset();
                setSettingsOpen(false);
              }}
              className={clsx(
                "flex h-8 w-full items-center gap-2 rounded-lg px-3 text-left text-xs font-semibold transition cursor-pointer",
                theme === "dark"
                  ? "text-[#b65f7c] hover:bg-white/5"
                  : theme === "clinical"
                  ? "text-[#b65f7c] hover:bg-[#fff0f6]"
                  : "text-[#8a4561] hover:bg-[#fff0f6]"
              )}
            >
              <RotateCcw size={12} />
              <span>重置本科作答</span>
            </button>
            <button
              type="button"
              onMouseDown={(e) => e.preventDefault()}
              onClick={() => {
                onResetAll();
                setSettingsOpen(false);
              }}
              className={clsx(
                "flex h-8 w-full items-center gap-2 rounded-lg px-3 text-left text-xs font-semibold transition cursor-pointer border-t border-[#f0ded6]/40 dark:border-white/10 mt-1 pt-1",
                theme === "dark"
                  ? "text-[#b65f7c] hover:bg-white/5"
                  : theme === "clinical"
                  ? "text-[#b65f7c] hover:bg-[#fff0f6]"
                  : "text-[#8a4561] hover:bg-[#fff0f6]"
              )}
            >
              <RotateCcw size={12} className="rotate-180" />
              <span>重置所有作答和筆記</span>
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
