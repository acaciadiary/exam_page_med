import json
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=10)
    args = parser.parse_args()

    with open("public/data/exams/111-2/medicine-6.json", encoding="utf-8-sig") as f:
        data = json.load(f)
    
    questions = data["questions"]
    for q in questions:
        num = q["question_number"]
        if args.start <= num <= args.end:
            print(f"=== Question {num} (ID: {q['id']}) ===")
            print(f"Category: {q.get('category')} | Correct Answer: {q.get('correct_answer')}")
            print(f"Text:\n{q['question_text']}")
            print("Options:")
            for k, v in q['options'].items():
                print(f"  {k}: {v}")
            print(f"Current Explanation:\n{q.get('explanation')}\n")

if __name__ == "__main__":
    main()
