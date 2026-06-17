import type { ExamManifestItem } from "../types/exam";

export type ExamStage = "stage-1" | "stage-2";

const subjectLabels: Record<number, string> = {
  1: "醫學（一）",
  2: "醫學（二）",
  3: "醫學（三）",
  4: "醫學（四）",
  5: "醫學（五）",
  6: "醫學（六）",
};

export function getSubjectNumber(exam: ExamManifestItem) {
  const match = exam.subject.match(/medicine-(\d+)/);
  return match ? Number(match[1]) : 1;
}

export function getExamStage(exam: ExamManifestItem): ExamStage {
  return getSubjectNumber(exam) <= 2 ? "stage-1" : "stage-2";
}

export function getStageLabel(stage: ExamStage) {
  return stage === "stage-1" ? "醫師一" : "醫師二";
}

export function getSubjectLabel(exam: ExamManifestItem) {
  return subjectLabels[getSubjectNumber(exam)] ?? exam.title;
}

export function groupExamsByStage(exams: ExamManifestItem[]) {
  return exams.reduce<Record<ExamStage, ExamManifestItem[]>>(
    (groups, exam) => {
      groups[getExamStage(exam)].push(exam);
      return groups;
    },
    { "stage-1": [], "stage-2": [] },
  );
}

export function getAvailableYears(exams: ExamManifestItem[]) {
  return Array.from(new Set(exams.map((exam) => exam.year))).sort((a, b) =>
    b.localeCompare(a, "zh-Hant", { numeric: true }),
  );
}

export function findExamForYear({
  exams,
  year,
  activeExam,
  activeStage,
}: {
  exams: ExamManifestItem[];
  year: string;
  activeExam?: ExamManifestItem;
  activeStage: ExamStage;
}) {
  const sameSubject = activeExam
    ? exams.find((exam) => exam.year === year && exam.subject === activeExam.subject)
    : undefined;

  return (
    sameSubject ??
    exams.find((exam) => exam.year === year && getExamStage(exam) === activeStage) ??
    exams.find((exam) => exam.year === year)
  );
}
