import json
from pathlib import Path

def dump():
    json_path = Path("public/data/exams/114-2/medicine-2.json")
    out_path = Path("scratch/all_questions.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    data = json.loads(json_path.read_text(encoding="utf-8"))
    
    with open(out_path, "w", encoding="utf-8") as f:
        for q in data["questions"]:
            f.write(f"Q{q['question_number']} ({q['id']}) [Ans: {q['correct_answer']}]\n")
            f.write(f"Text: {q['question_text']}\n")
            f.write("Options:\n")
            for k, v in q.get("options", {}).items():
                f.write(f"  {k}: {v}\n")
            f.write(f"Current Category: {q.get('category')}\n")
            f.write("-" * 80 + "\n\n")

if __name__ == "__main__":
    dump()
