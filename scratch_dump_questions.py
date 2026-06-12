import os
import json
import re

batches = [
    "108-2_medicine-2_batch-003",
    "108-2_medicine-2_batch-004",
    "108-2_medicine-2_batch-005",
    "108-2_medicine-2_batch-006",
    "108-2_medicine-3_batch-004",
    "108-2_medicine-3_batch-005",
    "108-2_medicine-3_batch-006",
    "108-2_medicine-4_batch-001"
]

reports_dir = "reports/gemini_prompts"
out_lines = []

for batch in batches:
    path = os.path.join(reports_dir, f"{batch}.md")
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    match = re.search(r"請處理以下 JSON 輸入：\s*(\{.*?\})\s*請完全依照以下 JSON Schema", content, re.DOTALL)
    if not match:
        match = re.search(r"(\{.*\})", content, re.DOTALL)
    
    if match:
        try:
            data = json.loads(match.group(1))
            out_lines.append(f"# Batch: {batch}")
            out_lines.append(f"Allowed categories: {data.get('allowed_categories')}\n")
            for q in data.get("questions", []):
                out_lines.append(f"## Q{q['question_number']} ({q['question_id']})")
                out_lines.append(f"**Text:**\n{q['question_text']}\n")
                out_lines.append("**Options:**")
                for k, v in q.get("options", {}).items():
                    out_lines.append(f"- {k}: {v}")
                out_lines.append(f"\n**Correct Answer:** {q['correct_answer']}")
                if q.get('answer_note'):
                    out_lines.append(f"**Note:** {q['answer_note']}")
                out_lines.append("\n" + "-"*40 + "\n")
        except Exception as e:
            out_lines.append(f"# Batch: {batch} - Error parsing: {e}\n")

with open("scratch_questions.md", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print("Dumped questions to scratch_questions.md")
