import json
import os

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

out = []

for b in batches:
    path = f'reports/gemini_prompts/{b}.md'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find JSON input
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
            out.append(f"============================================================")
            out.append(f"BATCH: {b}")
            out.append(f"Category Group: {data.get('category_group', '')}")
            out.append(f"Allowed Categories: {data.get('allowed_categories', [])}")
            out.append(f"============================================================")
            for q in data['questions']:
                out.append(f"Question Number: {q['question_number']}")
                out.append(f"Question ID: {q['question_id']}")
                out.append(f"Text: {q['question_text'].strip()}")
                out.append("Options:")
                for k, v in q['options'].items():
                    out.append(f"  {k}: {v.strip()}")
                out.append(f"Correct Answer: {q['correct_answer']}")
                out.append(f"Answer Note: {q.get('answer_note', '')}")
                out.append("-" * 30)
        except Exception as e:
            out.append(f"Error parsing {b}: {e}")
    else:
        out.append(f"File {path} not found")

with open('all_questions_dump.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("Done writing to all_questions_dump.txt")
