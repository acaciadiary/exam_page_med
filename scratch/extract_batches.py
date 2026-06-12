# -*- coding: utf-8 -*-
import os
import json
import re

batches = [
    "109-1_medicine-6_batch-004",
    "109-1_medicine-6_batch-005",
    "109-1_medicine-6_batch-006",
    "109-2_medicine-1_batch-001",
    "109-2_medicine-1_batch-002",
    "109-2_medicine-1_batch-003",
    "109-2_medicine-1_batch-004",
    "109-2_medicine-1_batch-005"
]

reports_dir = "reports/gemini_prompts"
extracted = {}

for batch in batches:
    path = os.path.join(reports_dir, f"{batch}.md")
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Try to find JSON block between '請處理以下 JSON 輸入：' and '請完全依照以下 JSON Schema'
    match = re.search(r"請處理以下 JSON 輸入：\s*(\{.*?\})\s*請完全依照以下 JSON Schema", content, re.DOTALL)
    if not match:
        match = re.search(r"(\{.*\})", content, re.DOTALL)
    
    if match:
        try:
            data = json.loads(match.group(1))
            extracted[batch] = data
            print(f"Parsed {batch}: {len(data.get('questions', []))} questions. Allowed categories: {data.get('allowed_categories')}")
        except Exception as e:
            print(f"Error parsing JSON for {batch}: {e}")
    else:
        print(f"Could not find JSON block in {batch}")

with open("scratch/extracted_questions.json", "w", encoding="utf-8") as f:
    json.dump(extracted, f, ensure_ascii=False, indent=2)
print("Saved to scratch/extracted_questions.json")
