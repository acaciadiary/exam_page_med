import json
import os
import glob
import sys

# Reconfigure stdout to use utf-8 if needed, but writing to file is safer
batches = [
    '109-1_medicine-3_batch-006',
    '109-1_medicine-4_batch-001',
    '109-1_medicine-4_batch-002',
    '109-1_medicine-4_batch-003',
    '109-1_medicine-4_batch-004',
    '109-1_medicine-4_batch-005',
    '109-1_medicine-4_batch-006',
    '109-1_medicine-5_batch-001'
]

out_lines = []

for b in batches:
    path = f'reports/gemini_prompts/{b}.md'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find JSON block by looking for "請處理以下 JSON 輸入："
        input_mark = "請處理以下 JSON 輸入："
        input_pos = content.find(input_mark)
        if input_pos != -1:
            start_idx = content.find('{', input_pos)
        else:
            start_idx = content.find('{\n  "dataset_id"')
            if start_idx == -1:
                start_idx = content.find('{"dataset_id"')
            if start_idx == -1:
                start_idx = content.find('{')
        
        # Find the matching closing bracket
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
            out_lines.append(f"{b}: {len(data['questions'])} questions. Allowed: {data.get('allowed_categories', [])}")
            for q in data['questions']:
                out_lines.append(f"  {q['question_number']}: {q['question_id']} - {q['question_text'].strip()[:60]}... (Answer: {q['correct_answer']})")
        except Exception as e:
            out_lines.append(f"Error parsing {b}: {e}")
            out_lines.append(f"Extracted string preview: {json_str[:200]}")
    else:
        out_lines.append(f"{path} not found")

with open('inspect_output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))
print("Done writing to inspect_output.txt")
