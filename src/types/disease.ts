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
}

export interface DiseaseComparisonsData {
  comparison_groups: DiseaseComparisonGroup[];
}
