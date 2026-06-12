# -*- coding: utf-8 -*-
import json

with open("scratch/extracted_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("scratch/questions_info.txt", "w", encoding="utf-8") as f:
    for batch_id, bdata in data.items():
        f.write("="*80 + "\n")
        f.write(f"BATCH ID: {batch_id}\n")
        f.write(f"ALLOWED CATEGORIES: {', '.join(bdata['allowed_categories'])}\n")
        f.write(f"CATEGORY GROUP: {bdata['category_group']}\n")
        f.write(f"DATASET YEAR: {bdata.get('dataset_year')}\n")
        f.write("="*80 + "\n\n")
        for q in bdata["questions"]:
            f.write(f"Question ID: {q['question_id']} (Number: {q['question_number']})\n")
            f.write(f"Correct Answer: {q['correct_answer']}\n")
            f.write(f"Text:\n{q['question_text']}\n")
            f.write("Options:\n")
            for opt, text in q["options"].items():
                f.write(f"  {opt}: {text}\n")
            f.write("-" * 40 + "\n\n")

print("Wrote questions to scratch/questions_info.txt")
