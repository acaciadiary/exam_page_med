import json
import os
import re

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
        print(f"Batch: {batch}")
        print(f"  Title: {data.get('dataset_title')}")
        print(f"  Allowed Categories: {data.get('allowed_categories')}")
        qs = data.get('questions', [])
        print(f"  Number of questions: {len(qs)}")
        if qs:
            print(f"  Range: {qs[0]['question_number']} to {qs[-1]['question_number']}")
    except Exception as e:
        print(f"Error parsing {batch}: {e}")
