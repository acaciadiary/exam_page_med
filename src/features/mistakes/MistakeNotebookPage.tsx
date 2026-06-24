import { ArrowRight, CheckCircle2, Flame, Repeat2, Trash2 } from "lucide-react";
import clsx from "clsx";
import type { ReactNode } from "react";
import { EmptyState } from "../../components/EmptyState";
import { getExamDisplayTitle } from "../../lib/examMetadata";
import { formatCorrectAnswers } from "../../lib/text";
import type {
  AnswerOptionKey,
  ExamManifestItem,
  ExamQuestion,
} from "../../types/exam";

export type MistakeStatus = "first" | "repeat" | "mastered" | "final";

export type MistakeEntry = {
  exam: ExamManifestItem;
  question: ExamQuestion;
  selectedAnswer: AnswerOptionKey;
  status: MistakeStatus;
};

type MistakeNotebookPageProps = {
  mistakes: MistakeEntry[];
  loading: boolean;
  onOpenQuestion: (examId: string, questionId: string) => void;
  onClearMistakes: () => void;
  onRemoveMistake: (examId: string, questionId: string) => void;
  onStartPractice: () => void;
  onStatusChange: (examId: string, questionId: string, status: MistakeStatus) => void;
};

const statusOptions: Array<{
  value: MistakeStatus;
  label: string;
  icon: ReactNode;
}> = [
  { value: "first", label: "初次錯題", icon: <Repeat2 size={14} /> },
  { value: "repeat", label: "重複錯題", icon: <Flame size={14} /> },
  { value: "mastered", label: "已掌握", icon: <CheckCircle2 size={14} /> },
  { value: "final", label: "考前必看", icon: <Flame size={14} /> },
];

export function MistakeNotebookPage({
  mistakes,
  loading,
  onOpenQuestion,
  onClearMistakes,
  onRemoveMistake,
  onStartPractice,
  onStatusChange,
}: MistakeNotebookPageProps) {
  const pendingMistakes = mistakes.filter((mistake) => mistake.status !== "mastered");

  return (
    <section className="space-y-6">
      <div className="rounded-[1.5rem] border border-white/80 bg-white/80 p-6 shadow-[0_18px_60px_rgba(181,133,117,0.16)] backdrop-blur-2xl">
        <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
          <div>
            <p className="text-sm font-semibold tracking-[0.12em] text-[#b36a84]">錯題本</p>
            <h2 className="mt-3 text-3xl font-semibold text-[#3f342d]">錯題複習流程</h2>
            <p className="mt-3 text-sm leading-7 text-[#725b52]">
              把錯題分成狀態，複習時會更知道先看哪一批。
            </p>
            <div className="mt-4 inline-flex rounded-full bg-[#fff1f6] px-4 py-2 text-sm font-semibold text-[#9a496b]">
              目前 {mistakes.length} 題，未掌握 {pendingMistakes.length} 題
            </div>
          </div>

          <div className="flex flex-wrap gap-2 lg:justify-end">
            <button
              type="button"
              onClick={onStartPractice}
              disabled={loading || pendingMistakes.length === 0}
              className="inline-flex h-11 items-center justify-center rounded-full bg-[#b8e2d4] px-4 text-sm font-semibold text-[#355249] shadow-[0_8px_22px_rgba(123,190,168,0.24)] transition hover:-translate-y-0.5 disabled:cursor-not-allowed disabled:opacity-50"
            >
              重練未掌握錯題
            </button>

            <button
              type="button"
              onClick={onClearMistakes}
              disabled={loading || mistakes.length === 0}
              className="inline-flex h-11 items-center justify-center gap-2 rounded-full border border-[#efd9d0] bg-white px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b] disabled:cursor-not-allowed disabled:opacity-50"
            >
              <Trash2 size={16} />
              清空錯題
            </button>
          </div>
        </div>
      </div>

      {loading ? (
        <div className="rounded-[1.1rem] border border-dashed border-[#eacfc4] bg-white/52 px-6 py-10 text-center text-sm font-semibold text-[#8a7066]">
          正在整理錯題...
        </div>
      ) : mistakes.length === 0 ? (
        <EmptyState title="目前沒有錯題" description="答錯的題目會自動出現在這裡。" />
      ) : (
        <div className="grid gap-5">
          {mistakes.map(({ exam, question, selectedAnswer, status }) => (
            <article
              key={`${exam.id}-${question.id}`}
              className="rounded-[1.35rem] border border-white/80 bg-white/82 p-6 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl"
            >
              <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
                <div className="min-w-0 flex-1">
                  <p className="text-sm font-semibold text-[#c4869b]">
                    {getExamDisplayTitle(exam)} · 第 {question.question_number} 題
                  </p>
                  <h3 className="mt-2 text-lg font-semibold leading-8 text-[#3f342d]">
                    {question.question_text}
                  </h3>
                </div>

                <div className="flex shrink-0 flex-wrap gap-2 sm:justify-end">
                  <button
                    type="button"
                    onClick={() => onRemoveMistake(exam.id, question.id)}
                    className="inline-flex items-center gap-2 rounded-full border border-[#efd9d0] bg-white px-4 py-2 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
                  >
                    <Trash2 size={16} />
                    從錯題本移除
                  </button>

                  <button
                    type="button"
                    onClick={() => onOpenQuestion(exam.id, question.id)}
                    className="inline-flex items-center gap-2 rounded-full border border-[#efd9d0] bg-white px-4 py-2 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
                  >
                    回到題目
                    <ArrowRight size={16} />
                  </button>
                </div>
              </div>

              <div className="mt-5 flex flex-wrap gap-3 text-sm">
                <span className="rounded-full bg-[#fff0f3] px-3 py-1 font-semibold text-[#9a496b]">
                  你的答案：{selectedAnswer}
                </span>
                <span className="rounded-full bg-[#e7f6ef] px-3 py-1 font-semibold text-[#4c806e]">
                  正解：{formatCorrectAnswers(question)}
                </span>
              </div>

              <div className="mt-4 flex flex-wrap gap-2 border-t border-[#f0ded6] pt-4">
                {statusOptions.map((option) => (
                  <button
                    key={option.value}
                    type="button"
                    onClick={() => onStatusChange(exam.id, question.id, option.value)}
                    className={clsx(
                      "inline-flex items-center gap-1.5 rounded-full border px-3 py-1.5 text-xs font-semibold transition",
                      status === option.value
                        ? "border-[#f1aac8] bg-[#ffddea] text-[#9a496b]"
                        : "border-[#efd9d0] bg-white/70 text-[#806b60] hover:border-[#f1aac8] hover:bg-[#fff0f6]",
                    )}
                  >
                    {option.icon}
                    {option.label}
                  </button>
                ))}
              </div>

              {question.explanation && (
                <div className="mt-5 rounded-[1rem] bg-[#fff8f4] px-4 py-4 text-sm leading-7 text-[#604b43]">
                  <p className="font-semibold text-[#5b4841]">解析</p>
                  <p className="mt-2 whitespace-pre-wrap">{question.explanation}</p>
                </div>
              )}
            </article>
          ))}
        </div>
      )}
    </section>
  );
}
