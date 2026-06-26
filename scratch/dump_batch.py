import sys
import json
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python dump_batch.py <batch_index>")
        return
    
    batch_idx = int(sys.argv[1])
    exam_file = Path("public/data/exams/113-1/medicine-5.json")
    if not exam_file.exists():
        print("Exam file not found.")
        return
        
    data = json.loads(exam_file.read_text(encoding="utf-8"))
    questions = data.get("questions", [])
    
    start = batch_idx * 10
    end = start + 10
    batch = questions[start:end]
    
    sys.stdout.reconfigure(encoding='utf-8')
    print(f"=== BATCH {batch_idx} (Questions {start+1} to {min(end, len(questions))}) ===")
    for q in batch:
        print(f"ID: {q['id']}")
        print(f"Number: {q['question_number']}")
        print(f"Category: {q.get('category')}")
        print(f"Question: {q['question_text']}")
        for k, v in q['options'].items():
            print(f"  {k}: {v}")
        print(f"Correct Answer: {q['correct_answer']}")
        print(f"Current Explanation: {q.get('explanation')}")
        print("-" * 50)

if __name__ == "__main__":
    main()
