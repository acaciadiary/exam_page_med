import { Bookmark, BookmarkCheck, Rotate3D } from "lucide-react";
import { useState } from "react";
import { motion } from "motion/react";
import { IconButton } from "../../components/IconButton";
import { getFlashcardStudyContent } from "../../lib/flashcards";
import type { ExamQuestion } from "../../types/exam";

type FlashcardProps = {
  question: ExamQuestion;
  marked: boolean;
  onToggleMarked: () => void;
};

export function Flashcard({ question, marked, onToggleMarked }: FlashcardProps) {
  const [flipped, setFlipped] = useState(false);
  const card = getFlashcardStudyContent(question);

  return (
    <article className="group relative min-w-0 [perspective:1400px]">
      <div className="mb-3 flex items-center justify-between">
        <span className="text-xs font-bold uppercase tracking-[0.22em] text-[#c4869b]">
          Card {question.question_number.toString().padStart(3, "0")}
        </span>
        <div className="flex gap-2">
          <IconButton
            label="翻轉閃卡"
            onClick={() => setFlipped((value) => !value)}
          >
            <Rotate3D size={17} />
          </IconButton>
          <IconButton
            label={marked ? "取消收藏閃卡" : "收藏閃卡"}
            active={marked}
            onClick={onToggleMarked}
          >
            {marked ? <BookmarkCheck size={17} /> : <Bookmark size={17} />}
          </IconButton>
        </div>
      </div>

      <button
        type="button"
        onClick={() => setFlipped((value) => !value)}
        className="flashcard-shell block h-80 w-full min-w-0 text-left transition duration-300 ease-out [transform-style:preserve-3d] hover:-translate-y-1 focus-visible:-translate-y-1 focus-visible:outline-none"
        aria-label="翻轉閃卡"
      >
        <motion.div
          className="relative h-full w-full [transform-style:preserve-3d]"
          animate={{ rotateY: flipped ? 180 : 0 }}
          transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
        >
          <div className="flashcard-face absolute inset-0 overflow-y-auto rounded-[1.35rem] border border-white/90 bg-[#fffdf9]/88 p-6 shadow-[0_18px_54px_rgba(181,133,117,0.18)] transition duration-300 group-hover:border-[#f2c9d8] group-hover:shadow-[0_24px_68px_rgba(181,133,117,0.26)] [backface-visibility:hidden]">
            <p className="text-xs font-semibold uppercase tracking-[0.18em] text-[#aa8a7d]">
              關鍵字 / 線索
            </p>
            {question.category && (
              <p className="mt-3 inline-flex rounded-full bg-[#f8eae3] px-3 py-1 text-xs font-semibold text-[#7d6259]">
                {question.category}
              </p>
            )}
            <h3 className="mt-6 text-2xl font-semibold leading-9 text-[#4b3b35]">
              {card.front}
            </h3>
            <p className="mt-5 rounded-[0.9rem] border border-[#efd9d0] bg-white/62 px-4 py-3 text-sm font-semibold leading-6 text-[#7d6259]">
              看到這些線索時，先想：它在考哪個觀念？判斷規則是什麼？
            </p>
            {!card.hasGeneratedCard && (
              <p className="mt-4 text-xs leading-5 text-[#8a7066]">
                這張卡尚未產生專用線索，重新產生詳解後會自動更新。
              </p>
            )}
          </div>

          <div className="flashcard-face absolute inset-0 overflow-y-auto rounded-[1.35rem] border border-[#d7eadf] bg-[#effaf5]/92 p-6 shadow-[0_18px_54px_rgba(132,197,174,0.18)] transition duration-300 group-hover:border-[#a9d9c8] group-hover:shadow-[0_24px_68px_rgba(132,197,174,0.28)] [backface-visibility:hidden] [transform:rotateY(180deg)]">
            <p className="text-xs font-semibold uppercase tracking-[0.18em] text-[#4c806e]">
              知識點 / 判斷規則
            </p>
            <p className="mt-5 rounded-[0.9rem] border border-[#d8eadf] bg-white/64 px-4 py-3 text-sm font-semibold leading-6 text-[#4c806e]">
              {card.keyPoint}
            </p>
            <p className="mt-5 text-2xl font-semibold leading-9 text-[#4b3b35]">
              {card.back}
            </p>
            {question.answer_note && (
              <p className="mt-3 text-xs font-medium leading-5 text-[#8a7066]">
                {question.answer_note}
              </p>
            )}
          </div>
        </motion.div>
      </button>
    </article>
  );
}
