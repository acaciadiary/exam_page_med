export interface DiseaseInfo {
  name: string;
  aliases: string[];
  features: Record<string, string>;
}

export interface RelatedQuestion {
  question_id: string;
  note?: string;
}

export interface MustKnowNumber {
  value: string;
  unit: string;
  target_disease: string;
  context: string;
}

export interface DiseaseComparisonGroup {
  id: string;
  title: string;
  category: string;
  exam_importance: string;
  exam_focus_tips: string;
  common_traps: string;
  diseases: DiseaseInfo[];
  highlight_keywords: string[];
  related_questions?: RelatedQuestion[];
  must_know_numbers?: MustKnowNumber[];
  stage?: string;
}

export interface InstantKillFact {
  id: string;
  year: string;
  subject: string;
  category: string;
  reason: string;
  highlight_value: string;
  unit: string;
  question_text: string;
  explanation: string;
  flashcard_front: string;
  flashcard_back: string;
  options: Record<string, string>;
}

export interface InstantKillFactsData {
  facts: InstantKillFact[];
}

export interface DiseaseComparisonsData {
  comparison_groups: DiseaseComparisonGroup[];
}
