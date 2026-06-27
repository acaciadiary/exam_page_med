import {
  ArrowRight,
  CalendarDays,
  ClipboardCheck,
  Flame,
  LineChart,
  Radar,
  Settings2,
  Sparkles,
} from "lucide-react";
import type { ReactNode } from "react";
import clsx from "clsx";
import { RadarChart } from "../../components/RadarChart";
import { getExamDisplayTitle, getSubjectLabel } from "../../lib/examMetadata";
import { compactText } from "../../lib/text";
import type { AppTheme } from "../../components/ThemeToggle";
import type { ExamDataset, ExamManifest, ExamManifestItem } from "../../types/exam";
import type { FavoriteEntry } from "../favorites/FavoritesPage";
import type { MistakeEntry } from "../mistakes/MistakeNotebookPage";

export type StudyActivityDay = {
  answered: number;
  correct: number;
};

export type StudyActivityLog = Record<string, StudyActivityDay>;

export type ExamPlan = {
  targetDate: string;
  targetStage: "stage-1" | "stage-2";
  focusExamId: string;
};

export type PerformanceStat = {
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

type HomeDashboardPageProps = {
  dailyGoal: number;
  examPlan: ExamPlan;
  studyActivity: StudyActivityLog;
  mistakes: MistakeEntry[];
  favorites: FavoriteEntry[];
  stats: PerformanceStat[];
  activeStage: "stage-1" | "stage-2";
  theme: AppTheme;
  exams: ExamManifestItem[];
  continueTarget: LastPractice | null;
  continueQuestion: ExamDataset["questions"][number] | null;
  continueExam: ExamManifest["exams"][number] | null;
  onDailyGoalChange: (goal: number) => void;
  onExamPlanChange: (plan: ExamPlan) => void;
  onContinuePractice: () => void;
  onOpenQuestion: (examId: string, questionId: string) => void;
  onOpenExam: (examId: string) => void;
  onGoMistakes: () => void;
  onGoFavorites: () => void;
  onGoProgress: () => void;
};

const quickGoals = [5, 10, 20];

export function HomeDashboardPage({
  dailyGoal,
  examPlan,
  studyActivity,
  mistakes,
  favorites,
  stats,
  activeStage,
  theme,
  exams,
  continueTarget,
  continueQuestion,
  continueExam,
  onDailyGoalChange,
  onExamPlanChange,
  onContinuePractice,
  onOpenQuestion,
  onOpenExam,
  onGoMistakes,
  onGoFavorites,
  onGoProgress,
}: HomeDashboardPageProps) {
  const todayKey = formatDateKey(new Date());
  const todayActivity = studyActivity[todayKey] ?? { answered: 0, correct: 0 };
  const todayRemaining = Math.max(0, dailyGoal - todayActivity.answered);
  const todayProgress =
    dailyGoal === 0 ? 100 : Math.min(100, Math.round((todayActivity.answered / dailyGoal) * 100));
  const streak = getGoalStreak(studyActivity, dailyGoal);
  const week = getWeeklySummary(studyActivity);
  const activeMistakes = mistakes.filter((mistake) => mistake.status !== "mastered");
  const firstMistake = activeMistakes.find((mistake) => mistake.status === "final") ?? activeMistakes[0];
  const firstFavorite = favorites.find((favorite) => favorite.tags.includes("考前必看")) ?? favorites[0];
  const weakest = stats.find((stat) => stat.answered >= 3) ?? stats[0];
  const targetExam = exams.find((exam) => exam.id === examPlan.focusExamId) ?? null;
  const countdown = getCountdownDays(examPlan.targetDate);

  return (
    <section className="space-y-5 pb-24 lg:pb-6">
      <div className="grid gap-5 xl:grid-cols-[minmax(0,1.35fr)_minmax(22rem,0.65fr)]">
        <div className="rounded-[1.5rem] border border-white/80 bg-white/82 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl sm:p-6">
          <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
            <div>
              <p className="flex items-center gap-2 text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
                <ClipboardCheck size={16} />
                今日任務
              </p>
              <h2 className="mt-2 text-3xl font-semibold tracking-normal text-[#3f342d] dark:text-[#f8edf3]">
                {todayRemaining === 0
                  ? "今天已達標，手感保持得很好"
                  : `今天再做 ${todayRemaining} 題，完成自己的節奏`}
              </h2>
            </div>
            <GoalPicker dailyGoal={dailyGoal} onChange={onDailyGoalChange} />
          </div>

          <div className="mt-5 grid gap-3 md:grid-cols-[minmax(0,1.1fr)_minmax(14rem,0.9fr)]">
            <button
              type="button"
              onClick={onContinuePractice}
              disabled={!continueTarget}
              className="flex min-h-40 flex-col justify-between gap-4 rounded-[1.15rem] border border-[#b8e2d4] bg-[#effaf5] p-5 text-left shadow-[0_12px_30px_rgba(123,190,168,0.16)] transition hover:-translate-y-0.5 hover:border-[#8fd5bd] hover:bg-[#e7f8f0] disabled:cursor-not-allowed disabled:opacity-60"
            >
              <div>
                <p className="text-xs font-bold tracking-[0.16em] text-[#4c806e]">一鍵繼續</p>
                <h3 className="mt-2 text-xl font-semibold text-[#315447]">
                  {continueQuestion
                    ? `從第 ${continueQuestion.question_number} 題繼續`
                    : continueExam
                    ? `回到 ${getExamDisplayTitle(continueExam)}`
                    : "開始今天的第一題"}
                </h3>
                <p className="mt-2 line-clamp-2 text-sm leading-6 text-[#4f6f65]">
                  {continueQuestion
                    ? compactText(continueQuestion.question_text, 96)
                    : continueExam
                    ? getExamDisplayTitle(continueExam)
                    : "系統會帶你回到最近一次練習的位置。"}
                </p>
              </div>
              <span className="inline-flex h-11 w-fit items-center justify-center gap-2 rounded-full bg-[#b8e2d4] px-4 text-sm font-bold text-[#315447]">
                繼續練習
                <ArrowRight size={16} />
              </span>
            </button>

            <div className="rounded-[1.15rem] border border-[#efd9d0] bg-white/70 p-5">
              <div className="flex items-center justify-between gap-3">
                <div>
                  <p className="text-xs font-bold tracking-[0.14em] text-[#9c7b70]">今日完成度</p>
                  <p className="mt-1 text-2xl font-extrabold text-[#9a496b]">
                    {todayActivity.answered}
                    <span className="ml-1 text-sm text-[#8b7666]">/ {dailyGoal} 題</span>
                  </p>
                </div>
                <ProgressRing value={todayProgress} />
              </div>
              <div className="mt-4 h-2 overflow-hidden rounded-full bg-[#f2e4dd]">
                <div className="h-full rounded-full bg-[#b8e2d4] transition-[width]" style={{ width: `${todayProgress}%` }} />
              </div>
              <p className="mt-3 text-sm font-semibold leading-6 text-[#725b52]">
                {todayRemaining === 0 ? "今日目標已完成，可以改刷錯題或收藏。" : `剩下 ${todayRemaining} 題，完成後會納入連續達標。`}
              </p>
            </div>
          </div>

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
              title="收藏複習"
              description={
                firstFavorite
                  ? compactText(firstFavorite.question.flashcard_summary || firstFavorite.question.question_text, 76)
                  : "尚未收藏重點題"
              }
              action={firstFavorite ? "複習" : "查看"}
              onClick={() =>
                firstFavorite ? onOpenQuestion(firstFavorite.exam.id, firstFavorite.question.id) : onGoFavorites()
              }
            />
            <TaskCard
              title="弱科練習"
              description={weakest ? `${weakest.label} 目前正確率 ${weakest.accuracy}%` : "作答後會自動分析弱點"}
              action={weakest ? "看進度" : "去作答"}
              onClick={weakest ? onGoProgress : onContinuePractice}
            />
          </div>
        </div>

        <div className="grid gap-5">
          <MetricPanel
            icon={<Flame size={17} />}
            label="連續達標"
            value={`${streak} 天`}
            description={todayRemaining === 0 ? "今天已經保住節奏。" : `今天還差 ${todayRemaining} 題。`}
          />
          <MetricPanel
            icon={<CalendarDays size={17} />}
            label="考試倒數"
            value={countdown === null ? "未設定" : countdown < 0 ? "已到期" : `${countdown} 天`}
            description={targetExam ? `主攻 ${getSubjectLabel(targetExam)}` : "設定目標後，書桌會更像你的。"}
          />
          <MetricPanel
            icon={<LineChart size={17} />}
            label="本週作答"
            value={`${week.answered} 題`}
            description={`練習 ${week.practiceDays} 天，正確率 ${week.accuracy}%`}
          />
        </div>
      </div>

      <div className="grid gap-5 xl:grid-cols-[minmax(0,0.95fr)_minmax(0,1.05fr)]">
        <PlanPanel
          examPlan={examPlan}
          exams={exams}
          onExamPlanChange={onExamPlanChange}
          onOpenExam={onOpenExam}
        />

        <div className="rounded-[1.5rem] border border-white/80 bg-white/82 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl">
          <div className="flex items-start justify-between gap-3">
            <div>
              <p className="flex items-center gap-2 text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
                <Radar size={16} />
                弱點雷達
              </p>
              <h3 className="mt-2 text-xl font-semibold text-[#3f342d] dark:text-[#f8edf3]">
                今天要補哪一塊？
              </h3>
            </div>
            <button
              type="button"
              onClick={onGoProgress}
              className="inline-flex h-10 items-center justify-center gap-2 rounded-full border border-[#efd9d0] bg-white/75 px-4 text-xs font-bold text-[#6f5b50] transition hover:bg-[#fff0f6] hover:text-[#9a496b]"
            >
              進度總覽
              <ArrowRight size={14} />
            </button>
          </div>
          <div className="mt-4 grid gap-4 lg:grid-cols-[minmax(16rem,0.85fr)_minmax(0,1.15fr)]">
            <div className="flex min-h-64 items-center justify-center">
              {stats.length === 0 ? (
                <div className="rounded-[1rem] border border-dashed border-[#eacfc4] bg-white/52 px-4 py-8 text-center text-sm leading-6 text-[#8a7066]">
                  作答後會自動產生弱點雷達。
                </div>
              ) : (
                <RadarChart stats={stats} activeStage={activeStage} theme={theme} />
              )}
            </div>
            <div className="grid content-start gap-3">
              {(stats.length > 0 ? stats.slice(0, 5) : []).map((stat) => (
                <div key={stat.label} className="rounded-[1rem] border border-[#efd9d0] bg-white/68 p-3">
                  <div className="flex items-center justify-between gap-3 text-sm">
                    <span className="font-bold text-[#3f342d] dark:text-[#f8edf3]">{stat.label}</span>
                    <span className="font-extrabold text-[#9a496b]">{stat.accuracy}%</span>
                  </div>
                  <div className="mt-2 h-2 overflow-hidden rounded-full bg-[#f2e4dd]">
                    <div className="h-full rounded-full bg-[#f1aac8]" style={{ width: `${Math.max(0, Math.min(100, stat.accuracy))}%` }} />
                  </div>
                  <p className="mt-2 text-xs font-semibold text-[#8b7666]">
                    {stat.correct}/{stat.answered} 題答對
                  </p>
                </div>
              ))}
              {stats.length === 0 ? (
                <p className="text-sm leading-6 text-[#725b52]">
                  先完成幾題，這裡會整理出目前最需要補強的科目。
                </p>
              ) : null}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function GoalPicker({ dailyGoal, onChange }: { dailyGoal: number; onChange: (goal: number) => void }) {
  return (
    <div className="flex flex-wrap items-center gap-2">
      {quickGoals.map((goal) => (
        <button
          key={goal}
          type="button"
          onClick={() => onChange(goal)}
          className={clsx(
            "h-9 rounded-full border px-3 text-xs font-extrabold transition",
            dailyGoal === goal
              ? "border-[#b8527a] bg-[#b8527a] text-white"
              : "border-[#efd9d0] bg-white/78 text-[#6f5b50] hover:bg-[#fff0f6]",
          )}
        >
          {goal} 題
        </button>
      ))}
      <label className="inline-flex h-9 items-center gap-2 rounded-full border border-[#efd9d0] bg-white/78 px-3 text-xs font-bold text-[#6f5b50]">
        自訂
        <input
          type="number"
          min={1}
          max={200}
          value={dailyGoal}
          onChange={(event) => onChange(clampGoal(Number(event.target.value)))}
          className="w-14 bg-transparent text-right font-extrabold text-[#9a496b] outline-none"
        />
      </label>
    </div>
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
      <p className="mt-3 text-sm font-bold text-[#3f342d] dark:text-[#f8edf3]">{title}</p>
      <p className="mt-2 line-clamp-3 text-sm leading-6 text-[#725b52] dark:text-[#dccbd3]">{description}</p>
      <span className="mt-3 inline-flex items-center gap-1 text-xs font-bold text-[#9a496b]">
        {action}
        <ArrowRight size={14} />
      </span>
    </button>
  );
}

function MetricPanel({
  icon,
  label,
  value,
  description,
}: {
  icon: ReactNode;
  label: string;
  value: string;
  description: string;
}) {
  return (
    <div className="rounded-[1.3rem] border border-white/80 bg-white/82 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.12)] backdrop-blur-2xl">
      <p className="flex items-center gap-2 text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
        {icon}
        {label}
      </p>
      <p className="mt-3 text-3xl font-extrabold text-[#3f342d] dark:text-[#f8edf3]">{value}</p>
      <p className="mt-2 text-sm font-semibold leading-6 text-[#725b52] dark:text-[#dccbd3]">{description}</p>
    </div>
  );
}

function PlanPanel({
  examPlan,
  exams,
  onExamPlanChange,
  onOpenExam,
}: {
  examPlan: ExamPlan;
  exams: ExamManifestItem[];
  onExamPlanChange: (plan: ExamPlan) => void;
  onOpenExam: (examId: string) => void;
}) {
  const focusExam = exams.find((exam) => exam.id === examPlan.focusExamId) ?? exams[0] ?? null;

  return (
    <div className="rounded-[1.5rem] border border-white/80 bg-white/82 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl">
      <p className="flex items-center gap-2 text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
        <Settings2 size={16} />
        目標設定
      </p>
      <h3 className="mt-2 text-xl font-semibold text-[#3f342d] dark:text-[#f8edf3]">
        讓讀書計畫更貼近你的考期
      </h3>

      <div className="mt-5 grid gap-3">
        <label className="grid gap-2 rounded-[1rem] border border-[#efd9d0] bg-white/62 p-3 text-sm font-bold text-[#6f5b50]">
          目標日期
          <input
            type="date"
            value={examPlan.targetDate}
            onChange={(event) => onExamPlanChange({ ...examPlan, targetDate: event.target.value })}
            className="h-10 rounded-xl border border-[#e6d6c9] bg-white/82 px-3 text-sm font-semibold outline-none focus:border-[#f1aac8] focus:ring-2 focus:ring-[#ffd9e8]/45"
          />
        </label>
        <label className="grid gap-2 rounded-[1rem] border border-[#efd9d0] bg-white/62 p-3 text-sm font-bold text-[#6f5b50]">
          目標階段
          <select
            value={examPlan.targetStage}
            onChange={(event) =>
              onExamPlanChange({ ...examPlan, targetStage: event.target.value as ExamPlan["targetStage"] })
            }
            className="h-10 rounded-xl border border-[#e6d6c9] bg-white/82 px-3 text-sm font-semibold outline-none focus:border-[#f1aac8] focus:ring-2 focus:ring-[#ffd9e8]/45"
          >
            <option value="stage-1">一階</option>
            <option value="stage-2">二階</option>
          </select>
        </label>
        <label className="grid gap-2 rounded-[1rem] border border-[#efd9d0] bg-white/62 p-3 text-sm font-bold text-[#6f5b50]">
          主攻科目
          <select
            value={examPlan.focusExamId}
            onChange={(event) => onExamPlanChange({ ...examPlan, focusExamId: event.target.value })}
            className="h-10 rounded-xl border border-[#e6d6c9] bg-white/82 px-3 text-sm font-semibold outline-none focus:border-[#f1aac8] focus:ring-2 focus:ring-[#ffd9e8]/45"
          >
            {exams.map((exam) => (
              <option key={exam.id} value={exam.id}>
                {getExamDisplayTitle(exam)}
              </option>
            ))}
          </select>
        </label>
      </div>

      <button
        type="button"
        onClick={() => focusExam && onOpenExam(focusExam.id)}
        disabled={!focusExam}
        className="mt-4 inline-flex h-11 items-center justify-center gap-2 rounded-full bg-[#b8e2d4] px-4 text-sm font-bold text-[#315447] shadow-[0_10px_26px_rgba(123,190,168,0.22)] transition hover:-translate-y-0.5 hover:bg-[#a7d9c9] disabled:cursor-not-allowed disabled:opacity-50"
      >
        開始主攻科目
        <ArrowRight size={15} />
      </button>
    </div>
  );
}

function ProgressRing({ value }: { value: number }) {
  const normalizedValue = Math.max(0, Math.min(100, value));

  return (
    <span
      className="grid h-16 w-16 shrink-0 place-items-center rounded-full text-xs font-extrabold text-[#9a496b]"
      style={{
        background: `conic-gradient(#b8527a ${normalizedValue * 3.6}deg, #f2e4dd 0deg)`,
      }}
    >
      <span className="grid h-12 w-12 place-items-center rounded-full bg-white">
        {normalizedValue}%
      </span>
    </span>
  );
}

function getWeeklySummary(activity: StudyActivityLog) {
  const days = Array.from({ length: 7 }, (_, index) => {
    const date = new Date();
    date.setDate(date.getDate() - index);
    return formatDateKey(date);
  });
  const totals = days.reduce(
    (summary, day) => {
      const item = activity[day] ?? { answered: 0, correct: 0 };
      return {
        answered: summary.answered + item.answered,
        correct: summary.correct + item.correct,
        practiceDays: summary.practiceDays + (item.answered > 0 ? 1 : 0),
      };
    },
    { answered: 0, correct: 0, practiceDays: 0 },
  );

  return {
    ...totals,
    accuracy: totals.answered === 0 ? 0 : Math.round((totals.correct / totals.answered) * 100),
  };
}

function getGoalStreak(activity: StudyActivityLog, dailyGoal: number) {
  let streak = 0;
  const date = new Date();

  if ((activity[formatDateKey(date)]?.answered ?? 0) < dailyGoal) {
    date.setDate(date.getDate() - 1);
  }

  while ((activity[formatDateKey(date)]?.answered ?? 0) >= dailyGoal) {
    streak += 1;
    date.setDate(date.getDate() - 1);
  }

  return streak;
}

function getCountdownDays(targetDate: string) {
  if (!targetDate) return null;

  const target = new Date(`${targetDate}T00:00:00`);
  if (Number.isNaN(target.getTime())) return null;

  const today = new Date();
  today.setHours(0, 0, 0, 0);
  return Math.ceil((target.getTime() - today.getTime()) / 86400000);
}

function formatDateKey(date: Date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

function clampGoal(value: number) {
  if (!Number.isFinite(value)) return 1;
  return Math.max(1, Math.min(200, Math.round(value)));
}
