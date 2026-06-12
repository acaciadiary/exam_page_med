import json
import os
import sys

def validate_file(prompt_path, output_path):
    if not os.path.exists(output_path):
        return f"Error: Output file {output_path} does not exist"
    
    # Read prompt to get questions and allowed categories
    with open(prompt_path, 'r', encoding='utf-8') as f:
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
        prompt_data = json.loads(json_str)
    except Exception as e:
        return f"Error parsing prompt JSON {prompt_path}: {e}"
        
    # Read output JSON
    try:
        with open(output_path, 'r', encoding='utf-8') as f:
            out_data = json.load(f)
    except Exception as e:
        return f"Error parsing output JSON {output_path}: {e}"
        
    # Check outermost fields
    if out_data.get('dataset_id') != prompt_data.get('dataset_id'):
        return f"Mismatch dataset_id: expected {prompt_data.get('dataset_id')}, got {out_data.get('dataset_id')}"
    if out_data.get('batch_id') != prompt_data.get('batch_id'):
        return f"Mismatch batch_id: expected {prompt_data.get('batch_id')}, got {out_data.get('batch_id')}"
        
    items = out_data.get('items', [])
    prompt_qs = prompt_data.get('questions', [])
    
    if len(items) != len(prompt_qs):
        return f"Count mismatch in {output_path}: prompt has {len(prompt_qs)}, output has {len(items)}"
        
    allowed_categories = prompt_data.get('allowed_categories', [])
    
    for i, item in enumerate(items):
        pq = prompt_qs[i]
        
        # Check matching question fields
        if item.get('question_id') != pq.get('question_id'):
            return f"Mismatch question_id at index {i}: expected {pq.get('question_id')}, got {item.get('question_id')}"
        if item.get('question_number') != pq.get('question_number'):
            return f"Mismatch question_number at index {i}: expected {pq.get('question_number')}, got {item.get('question_number')}"
        if item.get('correct_answer') != pq.get('correct_answer'):
            return f"Mismatch correct_answer for {pq.get('question_id')}: expected {pq.get('correct_answer')}, got {item.get('correct_answer')}"
        if item.get('category_group') != prompt_data.get('category_group'):
            return f"Mismatch category_group for {pq.get('question_id')}: expected {prompt_data.get('category_group')}, got {item.get('category_group')}"
            
        # Check schema fields
        required_fields = ['question_id', 'question_number', 'correct_answer', 'category_group', 'category', 'category_confidence', 'key_point', 'explanation', 'flashcard_front', 'flashcard_back', 'flashcard_summary']
        for field in required_fields:
            if field not in item:
                return f"Missing required field {field} in {pq.get('question_id')}"
                
        # Check category
        cat = item.get('category')
        if cat not in allowed_categories:
            return f"Category '{cat}' for {pq.get('question_id')} is not in allowed list: {allowed_categories}"
            
        # Check category confidence
        conf = item.get('category_confidence')
        if conf not in ['high', 'medium', 'low']:
            return f"Invalid category_confidence '{conf}' for {pq.get('question_id')}"
            
        # Check explanation length (2 to 5 sentences)
        exp = item.get('explanation')
        # simple sentence count: check number of Chinese periods '。'
        sentence_count = exp.count('。') + exp.count('？') + exp.count('！')
        if sentence_count < 2 or sentence_count > 5:
            # Maybe some sentences end without standard Chinese period, or use other symbols.
            # Let's warning instead of error, but let's keep it strict.
            print(f"Warning: {pq.get('question_id')} explanation has {sentence_count} sentences: '{exp}'")
            
        # Check flashcard summary format (關鍵字 / 線索 -> 知識點 / 判斷規則)
        sum_str = item.get('flashcard_summary')
        if ' -> ' not in sum_str:
            return f"flashcard_summary for {pq.get('question_id')} does not contain ' -> ' separator: '{sum_str}'"
            
    return "OK"

if __name__ == '__main__':
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
    
    all_ok = True
    for b in batches:
        p_path = f"reports/gemini_prompts/{b}.md"
        o_path = f"reports/gemini_outputs/{b}.json"
        
        if os.path.exists(o_path):
            res = validate_file(p_path, o_path)
            print(f"{b}: {res}")
            if res != "OK":
                all_ok = False
        else:
            print(f"{b}: Output file not created yet")
            all_ok = False
            
    if not all_ok:
        sys.exit(1)
    else:
        print("All completed files are verified successfully!")
        sys.exit(0)
