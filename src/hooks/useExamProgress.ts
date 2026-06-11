import type { AnswerOptionKey, AnswerState } from "../types/exam";
import { useLocalStorage } from "./useLocalStorage";

export function useExamProgress(key: string) {
  const [answers, setAnswers, resetAnswers] = useLocalStorage<AnswerState>(
    key,
    {},
  );

  function answerQuestion(questionId: string, answer: AnswerOptionKey) {
    setAnswers((current) => ({
      ...current,
      [questionId]: answer,
    }));
  }

  return { answers, answerQuestion, resetAnswers };
}
