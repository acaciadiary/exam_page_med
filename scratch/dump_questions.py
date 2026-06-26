import json

with open("public/data/exams/113-2/medicine-5.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("scratch/questions_all.txt", "w", encoding="utf-8") as out:
    for q in data["questions"]:
        out.write(f"ID: {q['id']}\n")
        out.write(f"Number: {q['question_number']}\n")
        out.write(f"Category: {q.get('category', '')}\n")
        out.write(f"Question: {q['question_text']}\n")
        out.write("Options:\n")
        for k, v in q["options"].items():
            out.write(f"  {k}: {v}\n")
        out.write(f"Answer: {q['correct_answer']}\n")
        out.write(f"Current Explanation: {q.get('explanation', '')}\n")
        out.write("="*60 + "\n\n")

print("Dumped all questions to scratch/questions_all.txt")
