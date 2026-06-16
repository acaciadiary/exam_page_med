import json
import os

batches = [
    "109-1_medicine-5_batch-003",
    "109-1_medicine-5_batch-004",
    "109-1_medicine-5_batch-005",
    "109-1_medicine-5_batch-006",
    "109-1_medicine-6_batch-001",
    "109-1_medicine-6_batch-002",
    "109-1_medicine-6_batch-003",
    "109-1_medicine-6_batch-004"
]

os.makedirs("scratch", exist_ok=True)

for batch in batches:
    p_path = f"reports/gemini_prompts/{batch}.md"
    if not os.path.exists(p_path):
        print(f"File not found: {p_path}")
        continue
    with open(p_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract JSON input
    start_idx = content.find('{"dataset_id"')
    if start_idx == -1:
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
        out_path = f"scratch/{batch}_input.json"
        with open(out_path, 'w', encoding='utf-8') as out_f:
            json.dump(data, out_f, ensure_ascii=False, indent=2)
        print(f"Extracted {batch} -> {out_path}")
    except Exception as e:
        print(f"Error parsing {batch}: {e}")
