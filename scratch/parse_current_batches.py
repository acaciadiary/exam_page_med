import os
import json
import re

batches = [
    "111-1_medicine-1_batch-006",
    "111-1_medicine-1_batch-007",
    "111-1_medicine-2_batch-001",
    "111-1_medicine-2_batch-002",
    "111-1_medicine-2_batch-003",
    "111-1_medicine-2_batch-004"
]

reports_dir = "reports/gemini_prompts"
out_lines = []

for batch in batches:
    path = os.path.join(reports_dir, f"{batch}.md")
    if not os.path.exists(path):
        out_lines.append(f"=== BATCH {batch}: NOT FOUND ===")
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Try parsing json from content
    input_mark = "請處理以下 JSON 輸入："
    input_pos = content.find(input_mark)
    if input_pos != -1:
        start_idx = content.find('{', input_pos)
    else:
        start_idx = content.find('{')
        
    brace_count = 0
    end_idx = -1
    for i in range(start_idx, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                break
                
    json_str = content[start_idx:end_idx]
    try:
        data = json.loads(json_str)
        out_lines.append(f"=== BATCH {batch} ===")
        out_lines.append(f"Dataset ID: {data.get('dataset_id')}")
        out_lines.append(f"Category Group: {data.get('category_group')}")
        out_lines.append(f"Allowed Categories: {data.get('allowed_categories')}")
        out_lines.append("")
        for q in data.get("questions", []):
            out_lines.append(f"Question {q.get('question_number')} ({q.get('question_id')})")
            out_lines.append(q.get("question_text").strip())
            for opt, val in q.get("options", {}).items():
                out_lines.append(f"  {opt}: {val}")
            out_lines.append(f"Correct Answer: {q.get('correct_answer')}")
            out_lines.append("")
    except Exception as e:
        out_lines.append(f"=== BATCH {batch}: Error parsing JSON: {e} ===")

with open("scratch/current_questions_parsed.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print("Parsing complete. Saved to scratch/current_questions_parsed.txt")
