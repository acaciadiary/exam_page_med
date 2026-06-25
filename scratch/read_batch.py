import sys
import json
from pathlib import Path

# Reconfigure stdout to use UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def main():
    if len(sys.argv) < 2:
        print("Usage: python read_batch.py <start_index> [count]")
        return
    
    start = int(sys.argv[1])
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    
    exam_file = Path("public/data/exams/114-1/medicine-6.json")
    if not exam_file.exists():
        print(f"File not found: {exam_file}")
        return
        
    data = json.loads(exam_file.read_text(encoding="utf-8"))
    questions = data.get("questions", [])
    
    batch = questions[start:start+count]
    print(f"=== Displaying {len(batch)} questions starting from index {start} ===")
    
    for i, q in enumerate(batch):
        print(f"\n[{start + i}] ID: {q.get('id')} | Question #{q.get('question_number')}")
        print(f"Category: {q.get('category')} | Correct: {q.get('correct_answer')}")
        print(f"Text:\n{q.get('question_text')}")
        print("Options:")
        opts = q.get("options", {})
        for opt_key in sorted(opts.keys()):
            print(f"  {opt_key}: {opts[opt_key]}")
        print("-" * 40)

if __name__ == "__main__":
    main()
