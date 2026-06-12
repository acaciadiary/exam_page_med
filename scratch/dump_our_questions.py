import json
import re
from pathlib import Path

batches = [
    "108-2_medicine-6_batch-002",
    "108-2_medicine-6_batch-003",
    "108-2_medicine-6_batch-004",
    "108-2_medicine-6_batch-005",
    "108-2_medicine-6_batch-006",
    "109-1_medicine-1_batch-001",
    "109-1_medicine-1_batch-002",
    "109-1_medicine-1_batch-003"
]

def extract_questions(batch_id):
    md_path = Path(f"reports/gemini_prompts/{batch_id}.md")
    if not md_path.exists():
        print(f"File {md_path} does not exist")
        return None
    content = md_path.read_text(encoding="utf-8")
    
    # Try finding the JSON block
    match = re.search(r"請處理以下 JSON 輸入：\s*\n(\{.*?\})\n\s*\n請完全依照以下", content, re.DOTALL)
    if not match:
        match = re.search(r"(\{.*\})", content, re.DOTALL)
    
    if match:
        try:
            return json.loads(match.group(1))
        except Exception as e:
            try:
                return json.loads(match.group(0))
            except Exception as e2:
                print(f"JSON load failed for {batch_id}: {e2}")
                return None
    else:
        print(f"No JSON block found in {batch_id}")
        return None

out_lines = []
for bid in batches:
    data = extract_questions(bid)
    if data:
        out_lines.append(f"# Batch: {bid}")
        out_lines.append(f"Category Group: {data.get('category_group')}")
        out_lines.append(f"Allowed Categories: {data.get('allowed_categories')}\n")
        for q in data.get("questions", []):
            out_lines.append(f"## Q{q['question_number']} (ID: {q['question_id']}) -> Correct Answer: {q['correct_answer']}")
            out_lines.append(q['question_text'].strip())
            for opt, val in q.get('options', {}).items():
                out_lines.append(f"- **{opt}**: {val.strip()}")
            note = q.get('answer_note', '')
            if note:
                out_lines.append(f"*Note: {note}*")
            out_lines.append("\n" + "-"*40 + "\n")

Path("scratch/our_questions.md").write_text("\n".join(out_lines), encoding="utf-8")
print("Wrote all questions to scratch/our_questions.md")
