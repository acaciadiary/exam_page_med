import os
import json
import re

batches = [
    "109-1_medicine-2_batch-005",
    "109-1_medicine-2_batch-006",
    "109-1_medicine-2_batch-007",
    "109-1_medicine-3_batch-001",
    "109-1_medicine-3_batch-002",
    "109-1_medicine-3_batch-003",
    "109-1_medicine-3_batch-004",
    "109-1_medicine-3_batch-005"
]

reports_dir = "reports/gemini_prompts"
out_lines = []

for batch in batches:
    path = os.path.join(reports_dir, f"{batch}.md")
    if not os.path.exists(path):
        out_lines.append(f"# Batch: {batch} - File not found\n")
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Try to find JSON block
    match = re.search(r"請處理以下 JSON 輸入：\s*(\{.*?\})\s*請完全依照以下 JSON Schema", content, re.DOTALL)
    if not match:
        match = re.search(r"(\{.*\})", content, re.DOTALL)
    
    if match:
        try:
            data = json.loads(match.group(1))
            out_lines.append(f"# Batch: {batch}")
            out_lines.append(f"Category Group: {data.get('category_group')}")
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
    else:
        out_lines.append(f"# Batch: {batch} - No JSON found\n")

os.makedirs("scratch", exist_ok=True)
with open("scratch/109_questions.md", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print("Dumped questions to scratch/109_questions.md")
