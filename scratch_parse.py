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
info = {}

for batch in batches:
    path = os.path.join(reports_dir, f"{batch}.md")
    if not os.path.exists(path):
        info[batch] = "File not found"
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    match = re.search(r"請處理以下 JSON 輸入：\s*(\{.*?\})\s*請完全依照以下 JSON Schema", content, re.DOTALL)
    if not match:
        match = re.search(r"(\{.*\})", content, re.DOTALL)
    
    if match:
        try:
            data = json.loads(match.group(1))
            info[batch] = {
                "questions_count": len(data.get("questions", [])),
                "range": [min(q.get("question_number") for q in data["questions"]), max(q.get("question_number") for q in data["questions"])] if data.get("questions") else [],
                "allowed_categories": data.get("allowed_categories"),
                "category_group": data.get("category_group"),
                "dataset_id": data.get("dataset_id"),
                "dataset_year": data.get("dataset_year")
            }
        except Exception as e:
            info[batch] = f"JSON parse error: {str(e)}"
    else:
        info[batch] = "No match"

with open("scratch_info.json", "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

print("Saved to scratch_info.json")
