export type AnswerOptionKey = "A" | "B" | "C" | "D";

export type ExamQuestion = {
  id: string;
  question_number: number;
  question_text: string;
  options: Record<AnswerOptionKey, string>;
  correct_answer: AnswerOptionKey | null;
  correct_answers?: AnswerOptionKey[];
  answer_status?: "standard" | "multiple_correct" | "all_credit" | "corrected_pending_review";
  answer_source?: "official_answer" | "official_correction";
  answer_note?: string;
  explanation: string;
  key_point?: string;
  flashcard_front?: string;
  flashcard_back?: string;
  flashcard_summary: string;
  category?: string;
  category_group?: string;
  category_confidence?: "high" | "medium" | "low";
  category_source?: "manual_range" | "auto" | "unassigned";
  review_status?: "empty" | "ai_generated" | "reviewed";
  explanation_model?: string;
  explanation_generated_at?: string;
};

export type ExamDataset = {
  id: string;
  year: string;
  title: string;
  subject: string;
  source: string;
  updated_at: string;
  questions: ExamQuestion[];
};

export type ExamManifestItem = {
  id: string;
  year: string;
  title: string;
  subject: string;
  path: string;
  question_count: number;
};

export type ExamManifest = {
  updated_at: string;
  exams: ExamManifestItem[];
};

export type Mode = "exam" | "flashcards";

export type AnswerState = Record<string, AnswerOptionKey>;
