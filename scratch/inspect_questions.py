import json
import sys

def print_batch(start_idx, end_idx):
    with open("public/data/exams/114-2/medicine-1.json", encoding="utf-8") as f:
        data = json.load(f)
    questions = data["questions"][start_idx:end_idx]
    sys.stdout.reconfigure(encoding="utf-8")
    for q in questions:
        print(f"=== Q{q['question_number']} ({q['id']}) ===")
        print(f"Text: {q['question_text']}")
        print("Options:")
        for k, v in q["options"].items():
            print(f"  {k}: {v}")
        print(f"Answer: {q['correct_answer']}")
        print(f"Category: {q.get('category')}")
        print(f"Explanation: {q.get('explanation')}")
        print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print_batch(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print_batch(0, 10)
