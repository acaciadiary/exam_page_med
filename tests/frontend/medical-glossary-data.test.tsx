import fs from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

interface ManifestExam {
  path: string;
}

interface Manifest {
  exams: ManifestExam[];
}

interface ExamQuestion {
  id: string;
}

interface ExamDataset {
  questions: ExamQuestion[];
}

interface MedicalGlossaryEntry {
  id: string;
  related_questions?: { question_id: string }[];
}

interface MedicalGlossaryData {
  terms: MedicalGlossaryEntry[];
}

const projectRoot = process.cwd();

function readJson<T>(filePath: string): T {
  return JSON.parse(fs.readFileSync(filePath, "utf8").replace(/^\uFEFF/, "")) as T;
}

describe("medical glossary data", () => {
  it("keeps every glossary term connected to existing practice questions", () => {
    const manifest = readJson<Manifest>(path.join(projectRoot, "public/data/manifest.json"));
    const questionIds = new Set<string>();

    for (const exam of manifest.exams) {
      const dataset = readJson<ExamDataset>(path.join(projectRoot, "public", exam.path));
      for (const question of dataset.questions) {
        questionIds.add(question.id);
      }
    }

    const glossary = readJson<MedicalGlossaryData>(path.join(projectRoot, "public/data/medical_glossary.json"));

    for (const term of glossary.terms) {
      expect(term.related_questions?.length, `${term.id} should have practice links`).toBeGreaterThan(0);

      for (const relatedQuestion of term.related_questions ?? []) {
        expect(
          questionIds.has(relatedQuestion.question_id),
          `${term.id} links to missing question ${relatedQuestion.question_id}`,
        ).toBe(true);
      }
    }
  });
});
