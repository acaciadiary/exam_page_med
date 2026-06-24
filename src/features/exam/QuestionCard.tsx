import { memo } from "react";
import { Bookmark, BookmarkCheck } from "lucide-react";
import { IconButton } from "../../components/IconButton";
import { formatCorrectAnswers, isAcceptedAnswer } from "../../lib/text";
import type { AnswerOptionKey, ExamQuestion } from "../../types/exam";
import { AnswerOptions } from "./AnswerOptions";
import { ExplanationPanel } from "./ExplanationPanel";

type QuestionCardProps = {
  question: ExamQuestion;
  selected?: AnswerOptionKey;
  marked: boolean;
  onAnswer: (answer: AnswerOptionKey) => void;
  onToggleMarked: () => void;
};

export const QuestionCard = memo(
  function QuestionCard({
    question,
    selected,
    marked,
    onAnswer,
    onToggleMarked,
  }: QuestionCardProps) {
    const isCorrect = isAcceptedAnswer(selected, question);

    return (
      <article
        id={question.id}
        className="relative min-w-0 overflow-hidden scroll-mt-32 rounded-[1.45rem] border border-white/90 bg-white/82 p-5 shadow-[0_18px_60px_rgba(181,133,117,0.16)] backdrop-blur-2xl dark:border-white/14 dark:bg-[#2b2430]/88 dark:shadow-[0_18px_60px_rgba(0,0,0,0.28)] sm:p-7 question-card-item"
      >
        <div className="absolute -left-2 top-8 hidden h-12 w-4 rounded-full bg-[#ffddea] dark:bg-[#b65f7c] sm:block" />
        <div className="flex items-start justify-between gap-4">
          <div className="min-w-0 flex-1">
            <p className="text-xs font-bold uppercase tracking-[0.22em] text-[#c4869b] dark:text-[#f3a6c4]">
              Note {question.question_number.toString().padStart(3, "0")}
            </p>
            <h2 className="mt-3 break-words text-lg font-semibold leading-8 text-[#4b3b35] sm:text-xl">
              {question.question_text}
            </h2>
          </div>
          <IconButton
            label={marked ? "取消收藏題目" : "收藏題目"}
            active={marked}
            onClick={onToggleMarked}
          >
            {marked ? <BookmarkCheck size={18} /> : <Bookmark size={18} />}
          </IconButton>
        </div>

        <AnswerOptions question={question} selected={selected} onAnswer={onAnswer} />

        {selected && (
          <div className="mt-5 flex flex-wrap items-center gap-3 text-sm">
            <span className="rounded-full bg-[#f8eae3] px-3 py-1 font-semibold text-[#6d534a] dark:bg-[#3a3038] dark:text-[#eadbe3]">
              你的答案：{selected}
            </span>
            <span className="rounded-full bg-[#e9f6f1] px-3 py-1 font-semibold text-[#4c806e] dark:bg-[#18372e] dark:text-[#b8efd9]">
              正解：{formatCorrectAnswers(question)}
            </span>
            {question.answer_source === "official_correction" && (
              <span className="rounded-full bg-[#fff3cb] px-3 py-1 font-semibold text-[#87693d] dark:bg-[#493c22] dark:text-[#f7db91]">
                官方更正
              </span>
            )}
            <span
              className={
                isCorrect
                  ? "rounded-full bg-[#e2f6ed] px-3 py-1 font-semibold text-[#4c806e] dark:bg-[#18372e] dark:text-[#b8efd9]"
                  : "rounded-full bg-[#fff0f3] px-3 py-1 font-semibold text-[#9a496b] dark:bg-[#472431] dark:text-[#ffc8da]"
              }
            >
              {isCorrect ? "答對了" : "再複習一次"}
            </span>
            {question.answer_note && (
              <span className="basis-full text-xs font-medium leading-6 text-[#8a7066] dark:text-[#cbb8c2]">
                {question.answer_note}
              </span>
            )}
          </div>
        )}

        {selected && <ExplanationPanel question={question} />}
      </article>
    );
  },
  (prevProps, nextProps) => {
    return (
      prevProps.question.id === nextProps.question.id &&
      prevProps.selected === nextProps.selected &&
      prevProps.marked === nextProps.marked
    );
  }
);
