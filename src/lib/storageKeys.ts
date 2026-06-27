const prefix = "medical-exam-prep";

export const storageKeys = {
  theme: `${prefix}:theme`,
  activeMode: `${prefix}:active-mode`,
  activeExam: `${prefix}:active-exam`,
  answers: (examId: string) => `${prefix}:answers:${examId}`,
  markedQuestions: (examId: string) => `${prefix}:marked-questions:${examId}`,
  markedFlashcards: (examId: string) => `${prefix}:marked-flashcards:${examId}`,
  favoriteTags: (examId: string) => `${prefix}:favorite-tags:${examId}`,
  mistakeStatus: `${prefix}:mistake-status`,
  focusSeconds: `${prefix}:focus-seconds`,
  stickyNotes: `${prefix}:sticky-notes`,
  appInstalled: `${prefix}:app-installed`,
  installPromptDismissed: `${prefix}:install-prompt-dismissed`,
  readingBold: `${prefix}:reading-bold`,
  lastPractice: `${prefix}:last-practice`,
  dailyGoal: `${prefix}:daily-goal`,
  examPlan: `${prefix}:exam-plan`,
  progressStage: `${prefix}:progress-stage`,
  studyActivity: `${prefix}:study-activity`,
};
