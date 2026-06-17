import type { AnswerOptionKey, ExamQuestion } from "../types/exam";

export function compactText(value: string, limit = 96) {
  const normalized = value.replace(/\s+/g, " ").trim();
  if (normalized.length <= limit) return normalized;
  return `${normalized.slice(0, limit - 1)}…`;
}

export function acceptedAnswers(question: ExamQuestion): AnswerOptionKey[] {
  if (question.correct_answers?.length) return question.correct_answers;
  return question.correct_answer ? [question.correct_answer] : [];
}

export function isAcceptedAnswer(
  selected: AnswerOptionKey | undefined,
  question: ExamQuestion,
) {
  if (!selected) return false;
  return acceptedAnswers(question).includes(selected);
}

export function formatCorrectAnswers(question: ExamQuestion) {
  const answers = acceptedAnswers(question);
  if (!answers.length) return "尚未提供";
  if (question.answer_status === "all_credit") return "全部給分";
  return answers.join(" / ");
}

export function getOptionTone(
  selected: AnswerOptionKey | undefined,
  correctAnswers: AnswerOptionKey[],
  option: AnswerOptionKey,
) {
  if (!selected) return "idle";
  if (correctAnswers.includes(option)) return "correct";
  if (option === selected) return "wrong";
  return "muted";
}
