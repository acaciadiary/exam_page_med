import json
from pathlib import Path

exam_file = Path(r"d:\Antigravity\exam_page_med\public\data\exams\112-1\medicine-5.json")
data = json.loads(exam_file.read_text(encoding="utf-8"))

output_lines = []
output_lines.append(f"Total questions: {len(data['questions'])}")
for q in data["questions"]:
    output_lines.append(f"Q{q['question_number']} ({q['id']}): {q['category']}")
    output_lines.append(f"Text: {q['question_text']}")
    output_lines.append(f"Options: {q['options']}")
    output_lines.append(f"Correct: {q['correct_answer']}")
    output_lines.append("-" * 40)

Path(r"d:\Antigravity\exam_page_med\scratch\questions_list.txt").write_text("\n".join(output_lines), encoding="utf-8")
print("Done")
