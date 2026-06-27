import {
  ArrowRight,
  BookOpenCheck,
  BookmarkCheck,
  CheckCircle2,
  ClipboardX,
  Flame,
  LayoutDashboard,
  Target,
} from "lucide-react";
import type { ReactNode } from "react";
import { useMemo, useState } from "react";
import clsx from "clsx";
import { useLocalStorage } from "../../hooks/useLocalStorage";
import {
  getExamDisplayTitle,
  getExamStage,
  getStageLabel,
  getSubjectLabel,
  type ExamStage,
} from "../../lib/examMetadata";
import { storageKeys } from "../../lib/storageKeys";
import type { ExamManifestItem } from "../../types/exam";

export type ExamProgressStat = {
  exam: ExamManifestItem;
  answered: number;
  total: number;
  correct: number;
  wrong: number;
  accuracy: number;
  completion: number;
};

export type CategoryProgressStat = {
  key: string;
  label: string;
  subjectLabel: string;
  answered: number;
  correct: number;
  wrong: number;
  accuracy: number;
};

export type StudyOverviewSummary = {
  totalAnswered: number;
  totalQuestions: number;
  totalCorrect: number;
  totalWrong: number;
  accuracy: number;
  completion: number;
  completedExamCount: number;
  wrongQuestionCount: number;
  activeWrongQuestionCount: number;
  favoriteCount: number;
  masteredMistakeCount: number;
};

type StudyOverviewPageProps = {
  summary: StudyOverviewSummary;
  examStats: ExamProgressStat[];
  categoryStats: CategoryProgressStat[];
  continueTitle: string;
  continueDescription: string;
  canContinue: boolean;
  onContinuePractice: () => void;
  onOpenExam: (examId: string) => void;
  onGoMistakes: () => void;
  onGoFavorites: () => void;
};

type StatusFilter = "all" | "unfinished" | "started" | "done";

const stageOrder: ExamStage[] = ["stage-1", "stage-2"];

export function StudyOverviewPage({
  summary,
  examStats,
  categoryStats,
  continueTitle,
  continueDescription,
  canContinue,
  onContinuePractice,
  onOpenExam,
  onGoMistakes,
  onGoFavorites,
}: StudyOverviewPageProps) {
  const [activeStage, setActiveStage] = useLocalStorage<ExamStage>(
    storageKeys.progressStage,
    "stage-1",
  );
  const [statusFilter, setStatusFilter] = useState<StatusFilter>("all");

  const stageSummaries = useMemo(() => {
    return stageOrder.map((stage) => {
      const stats = examStats.filter((stat) => getExamStage(stat.exam) === stage);
      return {
        stage,
        ...summarizeStats(stats),
      };
    });
  }, [examStats]);
  const activeStageSummary =
    stageSummaries.find((stageSummary) => stageSummary.stage === activeStage) ?? stageSummaries[0];

  const weakestExam = examStats
    .filter((stat) => stat.answered >= 5)
    .sort((a, b) => a.accuracy - b.accuracy)[0];
  const mostUnfinished = examStats
    .filter((stat) => stat.completion < 100)
    .sort((a, b) => b.total - b.answered - (a.total - a.answered))[0];
  const activeWeakCategories = categoryStats
    .filter((stat) => stat.answered >= 3)
    .sort((a, b) => a.accuracy - b.accuracy || b.wrong - a.wrong)
    .slice(0, 6);

  const years = Array.from(new Set(examStats.map((stat) => stat.exam.year))).sort((a, b) =>
    b.localeCompare(a, "zh-Hant", { numeric: true }),
  );

  const hasVisibleProgress = (stats: ExamProgressStat[]) => {
    if (statusFilter === "all") return true;
    if (statusFilter === "unfinished") return stats.some((stat) => stat.answered < stat.total);
    if (statusFilter === "started") return stats.some((stat) => stat.answered > 0 && stat.answered < stat.total);
    return stats.length > 0 && stats.every((stat) => stat.total > 0 && stat.answered >= stat.total);
  };

  return (
    <section className="space-y-5 pb-24 lg:pb-6">
      <div className="rounded-[1.45rem] border border-white/80 bg-white/82 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl sm:p-6">
        <div className="flex flex-col gap-4 xl:flex-row xl:items-start xl:justify-between">
          <div>
            <p className="flex items-center gap-2 text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
              <LayoutDashboard size={17} />
              進度總覽
            </p>
            <h2 className="mt-2 text-3xl font-semibold tracking-normal text-[#3f342d] dark:text-[#f8edf3]">
              進度總覽
            </h2>
          </div>
          <button
            type="button"
            onClick={onContinuePractice}
            disabled={!canContinue}
            className="inline-flex min-h-12 items-center justify-center gap-2 rounded-full bg-[#b8e2d4] px-5 text-sm font-bold text-[#315447] shadow-[0_10px_26px_rgba(123,190,168,0.24)] transition hover:-translate-y-0.5 hover:bg-[#a7d9c9] disabled:cursor-not-allowed disabled:opacity-50"
          >
            繼續練習
            <ArrowRight size={16} />
          </button>
        </div>

        <div className="mt-5 grid gap-3 lg:grid-cols-4">
          <ActionCard
            title={continueTitle}
            description={continueDescription}
            icon={<BookOpenCheck size={18} />}
            onClick={onContinuePractice}
            disabled={!canContinue}
          />
          <ActionCard
            title={weakestExam ? `先補弱科：${getSubjectLabel(weakestExam.exam)}` : "先累積一點題目"}
            description={
              weakestExam
                ? `${weakestExam.exam.year} 正確率 ${weakestExam.accuracy}%，已作答 ${weakestExam.answered} 題。`
                : "作答 5 題以上後，我會幫你抓出最弱科目。"
            }
            icon={<Target size={18} />}
            onClick={() => weakestExam && onOpenExam(weakestExam.exam.id)}
            disabled={!weakestExam}
          />
          <ActionCard
            title={`錯題回練：${summary.activeWrongQuestionCount} 題`}
            description={
              summary.activeWrongQuestionCount > 0
                ? "先把未掌握錯題收回來，考前會安心很多。"
                : "目前沒有尚未掌握的錯題。"
            }
            icon={<ClipboardX size={18} />}
            onClick={onGoMistakes}
            disabled={summary.wrongQuestionCount === 0}
          />
          <ActionCard
            title={`收藏複習：${summary.favoriteCount} 題`}
            description={
              summary.favoriteCount > 0
                ? "快速回看你標記過的重要題與閃卡。"
                : "遇到想回看的題目時，可以先加入收藏。"
            }
            icon={<BookmarkCheck size={18} />}
            onClick={onGoFavorites}
            disabled={summary.favoriteCount === 0}
          />
        </div>
      </div>

      <div className="rounded-[1.2rem] border border-white/80 bg-white/82 p-3 shadow-[0_12px_38px_rgba(181,133,117,0.12)] backdrop-blur-2xl">
        <div className="grid grid-cols-2 gap-2">
          {stageOrder.map((stage) => {
            const stageSummary = stageSummaries.find((item) => item.stage === stage);
            return (
              <button
                key={stage}
                type="button"
                onClick={() => setActiveStage(stage)}
                className={clsx(
                  "flex min-h-24 items-center justify-between gap-3 rounded-[1rem] border px-4 py-3 text-left transition",
                  activeStage === stage
                    ? "border-[#b8527a] bg-[#b8527a] text-white shadow-[0_12px_28px_rgba(184,82,122,0.2)]"
                    : "border-[#efd9d0] bg-white/75 text-[#6f5b50] hover:bg-[#fff0f6]",
                )}
              >
                <span className="min-w-0">
                  <span className="block text-base font-extrabold">{stage === "stage-1" ? "一階" : "二階"}</span>
                  <span className={clsx("mt-1 block text-xs font-bold", activeStage === stage ? "text-white/82" : "text-[#9c7b70]")}>
                    {stageSummary?.answered ?? 0} / {stageSummary?.total ?? 0} 題
                  </span>
                </span>
                <ProgressGauge
                  value={stageSummary?.completion ?? 0}
                  active={activeStage === stage}
                />
              </button>
            );
          })}
        </div>
      </div>

      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-6">
        <MetricCard label={`${getStageLabel(activeStage)}作答`} value={`${activeStageSummary.answered}`} suffix={` / ${activeStageSummary.total}`} />
        <MetricCard label="階段完成" value={`${activeStageSummary.completion}%`} />
        <MetricCard label="階段正確率" value={`${activeStageSummary.accuracy}%`} />
        <MetricCard label="階段錯題" value={`${activeStageSummary.wrong}`} />
        <MetricCard label="未作答" value={`${Math.max(0, activeStageSummary.total - activeStageSummary.answered)}`} />
        <MetricCard label="完成考卷" value={`${activeStageSummary.completedExamCount}`} suffix={` / ${activeStageSummary.examCount}`} />
      </div>

      <div className="grid gap-5 xl:grid-cols-[minmax(0,1.35fr)_minmax(21rem,0.65fr)]">
        <div className="rounded-[1.45rem] border border-white/80 bg-white/82 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl sm:p-6">
          <div className="flex flex-col gap-3 lg:flex-row lg:items-end lg:justify-between">
            <div>
              <p className="text-sm font-semibold tracking-[0.12em] text-[#b36a84]">年度進度總表</p>
              <h3 className="mt-2 text-2xl font-semibold text-[#3f342d] dark:text-[#f8edf3]">
                {getStageLabel(activeStage)}年度完成表
              </h3>
            </div>
            {mostUnfinished ? (
              <button
                type="button"
                onClick={() => onOpenExam(mostUnfinished.exam.id)}
                className="inline-flex h-10 items-center justify-center gap-2 rounded-full border border-[#efd9d0] bg-white/80 px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
              >
                從最大缺口開始
                <ArrowRight size={15} />
              </button>
            ) : null}
          </div>

          <div className="mt-4 flex flex-wrap gap-2">
            {[
              ["all", "全部狀態"],
              ["unfinished", "有未寫"],
              ["started", "寫到一半"],
              ["done", "已完成"],
            ].map(([value, label]) => (
              <button
                key={value}
                type="button"
                onClick={() => setStatusFilter(value as StatusFilter)}
                className={filterButtonClass(statusFilter === value)}
              >
                {label}
              </button>
            ))}
          </div>

          <div className="mt-5 grid gap-3">
            {years.map((year) => {
              const yearStats = examStats.filter((stat) => stat.exam.year === year);
              const visibleStages = stageOrder
                .filter((stage) => stage === activeStage)
                .map((stage) => yearStats.filter((stat) => getExamStage(stat.exam) === stage))
                .filter(hasVisibleProgress);

              if (visibleStages.length === 0) return null;

              return (
                <div key={year} className="rounded-[1.1rem] border border-[#efd9d0] bg-white/58 p-3">
                  <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
                    <h4 className="text-base font-extrabold text-[#5b4841] dark:text-[#f8edf3]">{year}</h4>
                    <span className="text-xs font-semibold text-[#9c7b70] dark:text-[#cbb8c2]">
                      已作答 {yearStats.reduce((sum, stat) => sum + stat.answered, 0)} 題
                    </span>
                  </div>
                  <div className="grid min-w-0 gap-3 lg:grid-cols-2">
                    {visibleStages.map((stats) => (
                      <YearStageCard
                        key={`${year}-${getExamStage(stats[0].exam)}`}
                        stats={stats}
                        onOpenExam={onOpenExam}
                      />
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        <div className="space-y-5">
          <div className="rounded-[1.45rem] border border-white/80 bg-white/82 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl">
            <p className="flex items-center gap-2 text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
              <Flame size={16} />
              需要補強
            </p>
            <h3 className="mt-2 text-xl font-semibold text-[#3f342d] dark:text-[#f8edf3]">
              目前最容易失分的分類
            </h3>
            <div className="mt-4 space-y-3">
              {activeWeakCategories.length === 0 ? (
                <div className="rounded-[1rem] border border-dashed border-[#eacfc4] bg-white/52 px-4 py-8 text-center text-sm leading-6 text-[#8a7066]">
                  再多寫幾題後，這裡會整理最需要回頭看的分類。
                </div>
              ) : (
                activeWeakCategories.map((stat) => (
                  <div key={stat.key} className="rounded-[1rem] border border-[#efd9d0] bg-white/68 p-3">
                    <div className="flex items-start justify-between gap-3">
                      <div className="min-w-0">
                        <p className="truncate text-sm font-bold text-[#3f342d] dark:text-[#f8edf3]">
                          {stat.label}
                        </p>
                        <p className="mt-1 text-xs font-semibold text-[#9c7b70] dark:text-[#cbb8c2]">
                          {stat.subjectLabel} · 錯 {stat.wrong} / {stat.answered} 題
                        </p>
                      </div>
                      <span className="shrink-0 rounded-full bg-[#fff1f6] px-2.5 py-1 text-xs font-extrabold text-[#9a496b]">
                        {stat.accuracy}%
                      </span>
                    </div>
                    <ProgressBar value={stat.accuracy} tone="danger" />
                  </div>
                ))
              )}
            </div>
          </div>

          <div className="rounded-[1.45rem] border border-white/80 bg-white/82 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl">
            <p className="flex items-center gap-2 text-sm font-semibold tracking-[0.12em] text-[#4c806e]">
              <CheckCircle2 size={16} />
              作答摘要
            </p>
            <div className="mt-4 grid gap-3">
              <StatusLine label="答對題數" value={`${summary.totalCorrect} 題`} />
              <StatusLine label="答錯題數" value={`${summary.totalWrong} 題`} />
              <StatusLine label="尚未掌握錯題" value={`${summary.activeWrongQuestionCount} 題`} />
              <StatusLine label="收藏複習" value={`${summary.favoriteCount} 題`} />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function summarizeStats(stats: ExamProgressStat[]) {
  const total = stats.reduce((sum, stat) => sum + stat.total, 0);
  const answered = stats.reduce((sum, stat) => sum + stat.answered, 0);
  const correct = stats.reduce((sum, stat) => sum + stat.correct, 0);
  const wrong = stats.reduce((sum, stat) => sum + stat.wrong, 0);
  return {
    total,
    answered,
    correct,
    wrong,
    accuracy: answered === 0 ? 0 : Math.round((correct / answered) * 100),
    completion: total === 0 ? 0 : Math.round((answered / total) * 100),
    completedExamCount: stats.filter((stat) => stat.total > 0 && stat.answered >= stat.total).length,
    examCount: stats.length,
  };
}

function filterButtonClass(active: boolean) {
  return clsx(
    "rounded-full border px-3 py-1.5 text-xs font-bold transition",
    active
      ? "border-[#b8527a] bg-[#b8527a] text-white"
      : "border-[#efd9d0] bg-white/80 text-[#6f5b50] hover:bg-[#fff0f6] hover:text-[#9a496b]",
  );
}

function ProgressGauge({ value, active }: { value: number; active: boolean }) {
  const normalizedValue = Math.max(0, Math.min(100, value));

  return (
    <span
      className={clsx(
        "grid h-14 w-14 shrink-0 place-items-center rounded-full text-[11px] font-extrabold",
        active ? "bg-white/18 text-white" : "bg-[#fff7fb] text-[#9a496b]",
      )}
      style={{
        background: active
          ? `conic-gradient(rgba(255,255,255,0.95) ${normalizedValue * 3.6}deg, rgba(255,255,255,0.2) 0deg)`
          : `conic-gradient(#b8527a ${normalizedValue * 3.6}deg, #f2e4dd 0deg)`,
      }}
      aria-label={`完成 ${normalizedValue}%`}
    >
      <span className={clsx("grid h-10 w-10 place-items-center rounded-full", active ? "bg-[#b8527a]" : "bg-white")}>
        {normalizedValue}%
      </span>
    </span>
  );
}

function YearStageCard({
  stats,
  onOpenExam,
}: {
  stats: ExamProgressStat[];
  onOpenExam: (examId: string) => void;
}) {
  const stage = getExamStage(stats[0].exam);
  const summary = summarizeStats(stats);
  const unfinished = summary.total - summary.answered;

  return (
    <div className="min-w-0 rounded-[1rem] border border-[#efd9d0] bg-white/72 p-3">
      <div className="flex items-center justify-between gap-2">
        <div>
          <p className="text-sm font-extrabold text-[#3f342d] dark:text-[#f8edf3]">{getStageLabel(stage)}</p>
          <p className="mt-1 text-xs font-semibold text-[#9c7b70]">
            已寫 {summary.answered} / {summary.total}，未寫 {unfinished}
          </p>
        </div>
        <span
          className={clsx(
            "rounded-full px-2.5 py-1 text-xs font-extrabold",
            summary.completion === 100
              ? "bg-[#e7f6ef] text-[#4c806e]"
              : summary.answered > 0
              ? "bg-[#fff1f6] text-[#9a496b]"
              : "bg-[#f8eee8] text-[#8b7666]",
          )}
        >
          {summary.completion}%
        </span>
      </div>
      <ProgressBar value={summary.completion} />
      <div className="mt-3 grid min-w-0 grid-cols-2 gap-2 sm:flex sm:flex-wrap">
        {stats
          .slice()
          .sort((a, b) => a.exam.subject.localeCompare(b.exam.subject, "zh-Hant", { numeric: true }))
          .map((stat) => (
            <SubjectPill key={stat.exam.id} stat={stat} onOpenExam={onOpenExam} />
          ))}
      </div>
    </div>
  );
}

function SubjectPill({
  stat,
  onOpenExam,
}: {
  stat: ExamProgressStat;
  onOpenExam: (examId: string) => void;
}) {
  const state =
    stat.total > 0 && stat.answered >= stat.total ? "done" : stat.answered > 0 ? "started" : "empty";

  return (
    <button
      type="button"
      title={getExamDisplayTitle(stat.exam)}
      onClick={() => onOpenExam(stat.exam.id)}
      className={clsx(
        "min-h-9 min-w-0 rounded-full border px-2.5 py-1 text-left text-[11px] font-bold transition hover:-translate-y-0.5 sm:px-3",
        state === "done" && "border-[#a8d9c8] bg-[#edf9f4] text-[#315447]",
        state === "started" && "border-[#f1aac8] bg-[#fff1f6] text-[#9a496b]",
        state === "empty" && "border-[#e7d7cf] bg-[#fffaf7] text-[#8b7666]",
      )}
    >
      <span className="inline-block max-w-full truncate align-bottom">{getSubjectLabel(stat.exam)}</span>
      <span className="ml-1 inline-block opacity-80">
        {stat.answered}/{stat.total}
      </span>
    </button>
  );
}

function ActionCard({
  title,
  description,
  icon,
  onClick,
  disabled,
}: {
  title: string;
  description: string;
  icon: ReactNode;
  onClick: () => void;
  disabled?: boolean;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className="group min-h-36 rounded-[1.05rem] border border-[#efd9d0] bg-white/72 p-4 text-left transition hover:-translate-y-0.5 hover:border-[#f1aac8] hover:bg-[#fff7fb] disabled:cursor-not-allowed disabled:opacity-60 dark:border-white/10 dark:bg-white/5"
    >
      <span className="inline-flex h-9 w-9 items-center justify-center rounded-full bg-[#fff1f6] text-[#b36a84]">
        {icon}
      </span>
      <p className="mt-3 text-sm font-bold text-[#3f342d] dark:text-[#f8edf3]">{title}</p>
      <p className="mt-2 line-clamp-3 text-sm leading-6 text-[#725b52] dark:text-[#dccbd3]">
        {description}
      </p>
    </button>
  );
}

function MetricCard({
  label,
  value,
  suffix,
}: {
  label: string;
  value: string;
  suffix?: string;
}) {
  return (
    <div className="rounded-[1.15rem] border border-white/80 bg-white/80 p-4 shadow-[0_12px_38px_rgba(181,133,117,0.12)] backdrop-blur-2xl">
      <p className="text-xs font-bold tracking-[0.12em] text-[#9c7b70] dark:text-[#cbb8c2]">{label}</p>
      <p className="mt-2 text-2xl font-extrabold text-[#9a496b]">
        {value}
        {suffix ? <span className="ml-1 text-sm font-bold text-[#8b7666] dark:text-[#a2949e]">{suffix}</span> : null}
      </p>
    </div>
  );
}

function ProgressBar({ value, tone = "default" }: { value: number; tone?: "default" | "danger" }) {
  return (
    <div className="mt-3 h-2 overflow-hidden rounded-full bg-[#f2e4dd] dark:bg-white/10">
      <div
        className={clsx(
          "h-full rounded-full transition-[width]",
          tone === "danger" ? "bg-[#f1aac8]" : "bg-[#b8e2d4]",
        )}
        style={{ width: `${Math.max(0, Math.min(100, value))}%` }}
      />
    </div>
  );
}

function StatusLine({ label, value }: { label: string; value: string }) {
  return (
    <div className="flex items-center justify-between gap-3 rounded-[0.9rem] bg-[#fff8f4] px-3 py-2.5 text-sm dark:bg-white/5">
      <span className="font-semibold text-[#725b52] dark:text-[#dccbd3]">{label}</span>
      <span className="font-extrabold text-[#9a496b]">{value}</span>
    </div>
  );
}
