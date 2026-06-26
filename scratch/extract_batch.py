import json
import sys
from pathlib import Path

def extract_batch(batch_idx):
    exam_file = Path("public/data/exams/115-1/medicine-5.json")
    with open(exam_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    questions = data["questions"]
    start_idx = batch_idx * 10
    end_idx = min(start_idx + 10, len(questions))
    
    batch = questions[start_idx:end_idx]
    
    output = []
    for q in batch:
        q_info = {
            "id": q["id"],
            "question_number": q["question_number"],
            "question_text": q["question_text"],
            "options": q["options"],
            "correct_answer": q["correct_answer"],
            "current_category": q.get("category"),
            "current_explanation": q.get("explanation"),
        }
        output.append(q_info)
        
    out_file = Path(f"scratch/batch_{batch_idx}.json")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {len(output)} questions to {out_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_batch.py <batch_index>")
        sys.exit(1)
    extract_batch(int(sys.argv[1]))
