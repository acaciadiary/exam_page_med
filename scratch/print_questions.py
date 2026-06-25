import json
import sys

def print_batch(start_idx, end_idx):
    with open("public/data/exams/114-1/medicine-5.json", encoding="utf-8") as f:
        data = json.load(f)
    
    questions = data["questions"]
    output = []
    output.append(f"Total questions: {len(questions)}")
    for q in questions[start_idx:end_idx]:
        output.append(f"=== Question {q['question_number']} (ID: {q['id']}) ===")
        output.append(f"Text: {q['question_text']}")
        output.append("Options:")
        for opt, val in q['options'].items():
            output.append(f"  {opt}: {val}")
        output.append(f"Correct Answer: {q['correct_answer']}")
        output.append(f"Current Category: {q.get('category')}")
        output.append("")
    
    with open("scratch/questions_output.txt", "w", encoding="utf-8") as out_f:
        out_f.write("\n".join(output))
    print(f"Successfully wrote questions {start_idx} to {end_idx} to scratch/questions_output.txt")

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    print_batch(start, end)
