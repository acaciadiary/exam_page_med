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

  function removeAnswers(questionIds: string[]) {
    const removableIds = new Set(questionIds);

    setAnswers((current) =>
      Object.fromEntries(
        Object.entries(current).filter(([questionId]) => !removableIds.has(questionId)),
      ),
    );
  }

  return { answers, answerQuestion, removeAnswers, resetAnswers };
}
