import json
import sys

def print_batch(exam_file, start_idx, end_idx, output_file=None):
    with open(exam_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    questions = data["questions"][start_idx:end_idx]
    
    out_lines = []
    for i, q in enumerate(questions):
        idx = start_idx + i + 1
        out_lines.append(f"=== Q{idx}: {q['id']} (Answer: {q['correct_answer']}) ===")
        out_lines.append(f"Category: {q.get('category', '')}")
        out_lines.append(f"Text: {q['question_text']}")
        out_lines.append("Options:")
        for k, v in q['options'].items():
            out_lines.append(f"  {k}: {v}")
        out_lines.append(f"Current Explanation: {q.get('explanation', '')}")
        out_lines.append(f"Current Key Point: {q.get('key_point', '')}")
        out_lines.append(f"Current Flashcard Front: {q.get('flashcard_front', '')}")
        out_lines.append(f"Current Flashcard Back: {q.get('flashcard_back', '')}")
        out_lines.append(f"Current Flashcard Summary: {q.get('flashcard_summary', '')}")
        out_lines.append("")
    
    content = "\n".join(out_lines)
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Output written to {output_file}")
    else:
        sys.stdout.reconfigure(encoding='utf-8')
        print(content)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python read_batch.py <exam_file> <start_idx> <end_idx> [output_file]")
    else:
        out_file = sys.argv[4] if len(sys.argv) > 4 else None
        print_batch(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), out_file)
