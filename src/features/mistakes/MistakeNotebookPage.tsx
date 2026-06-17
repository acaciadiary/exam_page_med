import { ArrowRight } from "lucide-react";
import { EmptyState } from "../../components/EmptyState";
import { getExamStage, getStageLabel, getSubjectLabel } from "../../lib/examMetadata";
import { formatCorrectAnswers } from "../../lib/text";
import type {
  AnswerOptionKey,
  ExamManifestItem,
  ExamQuestion,
} from "../../types/exam";

export type MistakeEntry = {
  exam: ExamManifestItem;
  question: ExamQuestion;
  selectedAnswer: AnswerOptionKey;
};

type MistakeNotebookPageProps = {
  mistakes: MistakeEntry[];
  loading: boolean;
  onOpenQuestion: (examId: string, questionId: string) => void;
};

export function MistakeNotebookPage({
  mistakes,
  loading,
  onOpenQuestion,
}: MistakeNotebookPageProps) {
  return (
    <section className="space-y-6">
      <div className="rounded-[1.5rem] border border-white/80 bg-white/80 p-6 shadow-[0_18px_60px_rgba(181,133,117,0.16)] backdrop-blur-2xl">
        <p className="text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
          我的錯題本
        </p>
        <h2 className="mt-3 text-3xl font-semibold text-[#3f342d]">
          全部錯題
        </h2>
        <p className="mt-3 text-sm leading-7 text-[#725b52]">
          這裡會集中整理所有年份、所有科目中你曾經答錯的題目。
        </p>
        <div className="mt-4 inline-flex rounded-full bg-[#fff1f6] px-4 py-2 text-sm font-semibold text-[#9a496b]">
          目前共 {mistakes.length} 題答錯
        </div>
      </div>

      {loading ? (
        <div className="rounded-[1.1rem] border border-dashed border-[#eacfc4] bg-white/52 px-6 py-10 text-center text-sm font-semibold text-[#8a7066]">
          正在整理全部錯題...
        </div>
      ) : mistakes.length === 0 ? (
        <EmptyState
          title="目前還沒有錯題"
          description="只要你在任何年份或科目答錯，題目就會自動集中到這裡。"
        />
      ) : (
        <div className="grid gap-5">
          {mistakes.map(({ exam, question, selectedAnswer }) => (
            <article
              key={`${exam.id}-${question.id}`}
              className="rounded-[1.35rem] border border-white/80 bg-white/82 p-6 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl"
            >
              <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
                <div className="min-w-0 flex-1">
                  <p className="text-sm font-semibold text-[#c4869b]">
                    {exam.year}・{getStageLabelForExam(exam)}・
                    {getSubjectLabel(exam)}・第 {question.question_number} 題
                  </p>
                  <h3 className="mt-2 text-lg font-semibold leading-8 text-[#3f342d]">
                    {question.question_text}
                  </h3>
                  {question.category && (
                    <p className="mt-3 inline-flex rounded-full bg-[#f8eee8] px-3 py-1 text-xs font-semibold text-[#7d6259]">
                      {question.category}
                    </p>
                  )}
                </div>

                <button
                  type="button"
                  onClick={() => onOpenQuestion(exam.id, question.id)}
                  className="inline-flex shrink-0 items-center gap-2 rounded-full border border-[#efd9d0] bg-white px-4 py-2 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
                >
                  回到題目
                  <ArrowRight size={16} />
                </button>
              </div>

              <div className="mt-5 flex flex-wrap gap-3 text-sm">
                <span className="rounded-full bg-[#fff0f3] px-3 py-1 font-semibold text-[#9a496b]">
                  你的答案：{selectedAnswer}
                </span>
                <span className="rounded-full bg-[#e7f6ef] px-3 py-1 font-semibold text-[#4c806e]">
                  正確答案：{formatCorrectAnswers(question)}
                </span>
              </div>

              {question.explanation && (
                <div className="mt-5 rounded-[1rem] bg-[#fff8f4] px-4 py-4 text-sm leading-7 text-[#604b43]">
                  <p className="font-semibold text-[#5b4841]">重點解析</p>
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

function getStageLabelForExam(exam: ExamManifestItem) {
  return getStageLabel(getExamStage(exam));
}
