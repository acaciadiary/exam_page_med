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
import clsx from "clsx";
import { getExamDisplayTitle, getSubjectLabel } from "../../lib/examMetadata";
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
              今天先處理最值得補的地方
            </h2>
            <p className="mt-3 max-w-3xl text-sm leading-7 text-[#725b52] dark:text-[#dccbd3]">
              這裡會整理所有年度與科目的作答紀錄，幫你看見完成度、正確率和目前最需要回頭補強的範圍。
            </p>
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
            title={weakestExam ? `優先補強：${getSubjectLabel(weakestExam.exam)}` : "先累積一點題目"}
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
                : "目前沒有待處理錯題。"
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
                : "遇到高頻或易混觀念時，可以先收藏。"
            }
            icon={<BookmarkCheck size={18} />}
            onClick={onGoFavorites}
            disabled={summary.favoriteCount === 0}
          />
        </div>
      </div>

      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-6">
        <MetricCard label="總作答" value={`${summary.totalAnswered}`} suffix={` / ${summary.totalQuestions}`} />
        <MetricCard label="整體完成" value={`${summary.completion}%`} />
        <MetricCard label="整體正確率" value={`${summary.accuracy}%`} />
        <MetricCard label="錯題數" value={`${summary.wrongQuestionCount}`} />
        <MetricCard label="已掌握錯題" value={`${summary.masteredMistakeCount}`} />
        <MetricCard label="完成考卷" value={`${summary.completedExamCount}`} suffix={` / ${examStats.length}`} />
      </div>

      <div className="grid gap-5 xl:grid-cols-[minmax(0,1.35fr)_minmax(21rem,0.65fr)]">
        <div className="rounded-[1.45rem] border border-white/80 bg-white/82 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl sm:p-6">
          <div className="flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
            <div>
              <p className="text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
                年度與科目
              </p>
              <h3 className="mt-2 text-2xl font-semibold text-[#3f342d] dark:text-[#f8edf3]">
                哪些卷已經推進，哪些還沒開始
              </h3>
            </div>
            {mostUnfinished ? (
              <button
                type="button"
                onClick={() => onOpenExam(mostUnfinished.exam.id)}
                className="inline-flex h-10 items-center justify-center gap-2 rounded-full border border-[#efd9d0] bg-white/80 px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
              >
                未完成最多
                <ArrowRight size={15} />
              </button>
            ) : null}
          </div>

          <div className="mt-5 space-y-5">
            {years.map((year) => {
              const yearStats = examStats
                .filter((stat) => stat.exam.year === year)
                .sort((a, b) => a.exam.subject.localeCompare(b.exam.subject, "zh-Hant", { numeric: true }));

              return (
                <div key={year}>
                  <div className="mb-2 flex items-center justify-between">
                    <h4 className="text-base font-bold text-[#5b4841] dark:text-[#f8edf3]">{year}</h4>
                    <span className="text-xs font-semibold text-[#9c7b70] dark:text-[#cbb8c2]">
                      {yearStats.reduce((sum, stat) => sum + stat.answered, 0)} 題已作答
                    </span>
                  </div>
                  <div className="grid gap-2">
                    {yearStats.map((stat) => (
                      <ExamProgressRow
                        key={stat.exam.id}
                        stat={stat}
                        onClick={() => onOpenExam(stat.exam.id)}
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
              弱點排行
            </p>
            <h3 className="mt-2 text-xl font-semibold text-[#3f342d] dark:text-[#f8edf3]">
              先補這幾塊
            </h3>
            <div className="mt-4 space-y-3">
              {activeWeakCategories.length === 0 ? (
                <div className="rounded-[1rem] border border-dashed border-[#eacfc4] bg-white/52 px-4 py-8 text-center text-sm leading-6 text-[#8a7066]">
                  再多作答幾題後，這裡會顯示分類弱點。
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
              目前狀態
            </p>
            <div className="mt-4 grid gap-3">
              <StatusLine label="答對題數" value={`${summary.totalCorrect} 題`} />
              <StatusLine label="答錯題數" value={`${summary.totalWrong} 題`} />
              <StatusLine label="待處理錯題" value={`${summary.activeWrongQuestionCount} 題`} />
              <StatusLine label="收藏複習" value={`${summary.favoriteCount} 題`} />
            </div>
          </div>
        </div>
      </div>
    </section>
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

function ExamProgressRow({ stat, onClick }: { stat: ExamProgressStat; onClick: () => void }) {
  const unanswered = stat.total - stat.answered;

  return (
    <button
      type="button"
      onClick={onClick}
      className="rounded-[1rem] border border-[#efd9d0] bg-white/70 p-3 text-left transition hover:-translate-y-0.5 hover:border-[#f1aac8] hover:bg-[#fff7fb] dark:border-white/10 dark:bg-white/5"
    >
      <div className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
        <div className="min-w-0">
          <p className="text-sm font-bold text-[#3f342d] dark:text-[#f8edf3]">
            {getExamDisplayTitle(stat.exam)}
          </p>
          <p className="mt-1 text-xs font-semibold text-[#9c7b70] dark:text-[#cbb8c2]">
            已作答 {stat.answered} / {stat.total} · 未作答 {unanswered} · 正確率 {stat.answered > 0 ? `${stat.accuracy}%` : "尚未開始"}
          </p>
        </div>
        <span
          className={clsx(
            "inline-flex h-8 shrink-0 items-center justify-center rounded-full px-3 text-xs font-extrabold",
            stat.completion === 100
              ? "bg-[#e7f6ef] text-[#4c806e]"
              : stat.answered > 0
              ? "bg-[#fff1f6] text-[#9a496b]"
              : "bg-[#f8eee8] text-[#8b7666]",
          )}
        >
          {stat.completion}%
        </span>
      </div>
      <ProgressBar value={stat.completion} />
    </button>
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
