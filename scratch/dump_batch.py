import json
import sys

def dump_batch(batch_idx):
    with open("public/data/exams/111-2/medicine-4.json", encoding="utf-8-sig") as f:
        data = json.load(f)
    
    questions = data["questions"]
    start = batch_idx * 10
    end = start + 10
    batch = questions[start:end]
    
    output_lines = []
    output_lines.append(f"--- BATCH {batch_idx + 1} (Questions {start+1} to {min(end, len(questions))}) ---")
    for q in batch:
        output_lines.append(f"ID: {q['id']}")
        output_lines.append(f"Number: {q['question_number']}")
        output_lines.append(f"Text:\n{q['question_text']}")
        output_lines.append("Options:")
        for k, v in q["options"].items():
            output_lines.append(f"  {k}: {v}")
        output_lines.append(f"Correct Answer: {q['correct_answer']}")
        output_lines.append(f"Current Category: {q.get('category')}")
        output_lines.append(f"Current Explanation:\n{q.get('explanation')}")
        output_lines.append("-" * 40)
    
    with open("scratch/batch_output.txt", "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(output_lines))
    print(f"Batch {batch_idx + 1} written to scratch/batch_output.txt")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dump_batch(int(sys.argv[1]) - 1)
    else:
        dump_batch(0)
