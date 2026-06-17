import { ArrowRight } from "lucide-react";
import { EmptyState } from "../../components/EmptyState";
import { formatCorrectAnswers, isAcceptedAnswer } from "../../lib/text";
import type { AnswerState, ExamDataset } from "../../types/exam";

type MistakeNotebookPageProps = {
  dataset: ExamDataset;
  answers: AnswerState;
  onOpenQuestion: (questionId: string) => void;
};

export function MistakeNotebookPage({
  dataset,
  answers,
  onOpenQuestion,
}: MistakeNotebookPageProps) {
  const wrongQuestions = dataset.questions.filter((question) => {
    const selected = answers[question.id];
    return selected && !isAcceptedAnswer(selected, question);
  });

  return (
    <section className="space-y-6">
      <div className="rounded-[1.5rem] border border-white/80 bg-white/80 p-6 shadow-[0_18px_60px_rgba(181,133,117,0.16)] backdrop-blur-2xl">
        <p className="text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
          我的錯題本
        </p>
        <h2 className="mt-3 text-3xl font-semibold text-[#3f342d]">
          {dataset.title}
        </h2>
        <p className="mt-3 text-sm leading-7 text-[#725b52]">
          這裡會整理你在目前這一卷答錯的題目，方便你集中複習、回頭訂正。
        </p>
        <div className="mt-4 inline-flex rounded-full bg-[#fff1f6] px-4 py-2 text-sm font-semibold text-[#9a496b]">
          目前共 {wrongQuestions.length} 題答錯
        </div>
      </div>

      {wrongQuestions.length === 0 ? (
        <EmptyState
          title="目前還沒有錯題"
          description="先去作答這一卷，答錯的題目就會自動整理到這裡。"
        />
      ) : (
        <div className="grid gap-5">
          {wrongQuestions.map((question) => {
            const selected = answers[question.id];

            return (
              <article
                key={question.id}
                className="rounded-[1.35rem] border border-white/80 bg-white/82 p-6 shadow-[0_18px_60px_rgba(181,133,117,0.14)] backdrop-blur-2xl"
              >
                <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
                  <div className="min-w-0 flex-1">
                    <p className="text-sm font-semibold text-[#c4869b]">
                      第 {question.question_number} 題
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
                    onClick={() => onOpenQuestion(question.id)}
                    className="inline-flex shrink-0 items-center gap-2 rounded-full border border-[#efd9d0] bg-white px-4 py-2 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
                  >
                    回到題目
                    <ArrowRight size={16} />
                  </button>
                </div>

                <div className="mt-5 flex flex-wrap gap-3 text-sm">
                  <span className="rounded-full bg-[#fff0f3] px-3 py-1 font-semibold text-[#9a496b]">
                    你的答案：{selected}
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
            );
          })}
        </div>
      )}
    </section>
  );
}
