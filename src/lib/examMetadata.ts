import type { ExamManifestItem } from "../types/exam";

export type ExamStage = "stage-1" | "stage-2";

const subjectLabels: Record<number, string> = {
  1: "醫學一",
  2: "醫學二",
  3: "醫學三",
  4: "醫學四",
  5: "醫學五",
  6: "醫學六",
};

export function getSubjectNumber(exam: ExamManifestItem | { subject: string }) {
  const match = exam.subject.match(/medicine-(\d+)/);
  return match ? Number(match[1]) : 1;
}

export function getExamStage(exam: ExamManifestItem | { subject: string }): ExamStage {
  return getSubjectNumber(exam) <= 2 ? "stage-1" : "stage-2";
}

export function getStageLabel(stage: ExamStage) {
  return stage === "stage-1" ? "一階" : "二階";
}

export function getSubjectLabel(exam: ExamManifestItem | { subject: string }) {
  return subjectLabels[getSubjectNumber(exam)] ?? exam.subject;
}

export function getExamDisplayTitle(exam: ExamManifestItem | { year: string; subject: string }) {
  return `${exam.year}・${getStageLabel(getExamStage(exam))}・${getSubjectLabel(exam)}`;
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
