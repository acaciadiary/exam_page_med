import clsx from "clsx";
import { Check, X } from "lucide-react";
import type { AnswerOptionKey, ExamQuestion } from "../../types/exam";
import { acceptedAnswers, getOptionTone } from "../../lib/text";

type AnswerOptionsProps = {
  question: ExamQuestion;
  selected?: AnswerOptionKey;
  onAnswer: (answer: AnswerOptionKey) => void;
};

const optionKeys: AnswerOptionKey[] = ["A", "B", "C", "D"];

export function AnswerOptions({
  question,
  selected,
  onAnswer,
}: AnswerOptionsProps) {
  return (
    <div className="mt-6 grid gap-3">
      {optionKeys.map((option) => {
        const tone = getOptionTone(selected, acceptedAnswers(question), option);

        return (
          <button
            key={option}
            type="button"
            onClick={() => onAnswer(option)}
            className={clsx(
              "group flex min-h-16 w-full min-w-0 items-start gap-3 overflow-hidden rounded-[1.05rem] border px-4 py-4 text-left shadow-sm transition sm:gap-4",
              tone === "correct" &&
                "border-[#8fd5bd] bg-[#e7f8f0] text-[#315447] shadow-[0_12px_28px_rgba(132,197,174,0.2)]",
              tone === "wrong" &&
                "border-[#efa6b9] bg-[#fff0f3] text-[#7b4652]",
              tone === "muted" &&
                "border-[#ead8cf] bg-[#fffaf7] text-[#a58d82]",
              tone === "idle" &&
                "border-[#ead8cf] bg-white/80 text-[#604b43] hover:-translate-y-0.5 hover:border-[#f0adc9] hover:bg-[#fff3f8]",
            )}
          >
            <span
              className={clsx(
                "flex h-8 w-8 shrink-0 items-center justify-center rounded-full text-sm font-bold",
                tone === "correct" && "bg-[#9edcc5] text-[#315447]",
                tone === "wrong" && "bg-[#efa6b9] text-white",
                tone === "muted" && "bg-[#f3e7e0] text-[#aa9186]",
                tone === "idle" &&
                  "bg-[#f8eae3] text-[#8b6d62] group-hover:bg-[#ffddea] group-hover:text-[#9a496b]",
              )}
            >
              {tone === "correct" ? (
                <Check size={16} />
              ) : tone === "wrong" ? (
                <X size={16} />
              ) : (
                option
              )}
            </span>
            <span className="min-w-0 flex-1 break-words text-base leading-7">
              {question.options[option]}
            </span>
          </button>
        );
      })}
    </div>
  );
}
