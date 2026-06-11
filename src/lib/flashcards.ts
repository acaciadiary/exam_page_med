import type { ExamQuestion } from "../types/exam";
import { compactText, formatCorrectAnswers } from "./text";

export type FlashcardStudyContent = {
  front: string;
  back: string;
  keyPoint: string;
  hasGeneratedCard: boolean;
};

export function getFlashcardStudyContent(
  question: ExamQuestion,
): FlashcardStudyContent {
  const summaryParts = splitFlashcardSummary(question.flashcard_summary);
  const front = cleanText(question.flashcard_front) || summaryParts.front;
  const back = cleanText(question.flashcard_back) || summaryParts.back;
  const keyPoint = cleanText(question.key_point);

  return {
    front:
      front ||
      compactText(question.question_text, 84) ||
      "尚未建立關鍵線索",
    back:
      back ||
      keyPoint ||
      `${formatCorrectAnswers(question)} 相關考點尚未整理。`,
    keyPoint: keyPoint || "知識點尚未建立，請先回到考題頁查看詳解。",
    hasGeneratedCard: Boolean(front || back || keyPoint),
  };
}

function splitFlashcardSummary(summary: string) {
  const normalized = cleanText(summary);
  if (!normalized) return { front: "", back: "" };

  const [front, ...rest] = normalized.split(/\s*(?:->|→|=>|⇒)\s*/);
  return {
    front: cleanText(front),
    back: cleanText(rest.join(" -> ")) || normalized,
  };
}

function cleanText(value?: string) {
  return String(value || "").replace(/\s+/g, " ").trim();
}
