import json

with open("public/data/exams/111-2/medicine-6.json", encoding="utf-8-sig") as f:
    data = json.load(f)

with open("scratch/questions_readable.txt", "w", encoding="utf-8") as out:
    for q in data["questions"]:
        num = q["question_number"]
        out.write(f"=== Question {num} (ID: {q['id']}) ===\n")
        out.write(f"Category: {q.get('category')} | Correct Answer: {q.get('correct_answer')}\n")
        out.write(f"Text:\n{q['question_text']}\n")
        out.write("Options:\n")
        for k, v in q['options'].items():
            out.write(f"  {k}: {v}\n")
        out.write(f"Current Explanation:\n{q.get('explanation')}\n\n")

print("Dumped questions to scratch/questions_readable.txt")
