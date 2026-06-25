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

export interface MedicalGlossaryEntry {
  id: string;
  name: string;
  aliases: string[];
  category: string;
  explanation: string;
  exam_focus: string;
  related_questions?: RelatedQuestion[];
  stage: string;
  frequency: number;
}

export interface MedicalGlossaryData {
  terms: MedicalGlossaryEntry[];
}

export interface EponymEntry {
  id: string;
  name: string;
  aliases: string[];
  category: string;
  origin_type: string;
  description: string;
  clinical_signs: string;
  exam_focus: string;
  frequency: number;
  related_questions?: RelatedQuestion[];
  stage: string;
}

export interface EponymsData {
  eponyms: EponymEntry[];
}

export interface ClinicalGuidelineEntry {
  id: string;
  title: string;
  aliases: string[];
  category: string;
  scenario: string;
  first_line_action: string;
  dosage_info: string;
  common_traps: string;
  frequency: number;
  related_questions?: RelatedQuestion[];
  stage: string;
}

export interface ClinicalGuidelinesData {
  guidelines: ClinicalGuidelineEntry[];
}
