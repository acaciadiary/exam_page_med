import json
from pathlib import Path

def dump_questions():
    exam_path = Path("public/data/exams/114-1/medicine-4.json")
    if not exam_path.exists():
        print(f"Error: {exam_path} does not exist.")
        return

    data = json.loads(exam_path.read_text(encoding="utf-8"))
    questions = data.get("questions", [])
    
    output_lines = []
    output_lines.append(f"Exam: {data.get('title', 'Unknown')} ({data.get('year', 'Unknown')} - {data.get('subject', 'Unknown')})")
    output_lines.append(f"Total Questions: {len(questions)}")
    output_lines.append("="*80 + "\n")
    
    for q in questions:
        q_num = q.get("question_number")
        q_id = q.get("id")
        q_text = q.get("question_text")
        options = q.get("options", {})
        correct_answer = q.get("correct_answer") or q.get("correct_answers")
        
        output_lines.append(f"Question {q_num} (ID: {q_id})")
        output_lines.append(f"Text:\n{q_text}")
        output_lines.append("Options:")
        for opt, val in sorted(options.items()):
            output_lines.append(f"  {opt}. {val}")
        output_lines.append(f"Correct Answer: {correct_answer}")
        output_lines.append("-" * 40 + "\n")
        
    out_path = Path("scratch/medicine_4_questions.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(output_lines), encoding="utf-8")
    print(f"Successfully dumped questions to {out_path}")

if __name__ == "__main__":
    dump_questions()
