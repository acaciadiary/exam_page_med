import json

def dump():
    with open('public/data/exams/112-1/medicine-3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    with open('scratch/questions_112_1_m3.txt', 'w', encoding='utf-8') as out:
        for q in data['questions']:
            out.write(f"ID: {q['id']}\n")
            out.write(f"Number: {q['question_number']}\n")
            out.write(f"Category: {q.get('category', 'None')}\n")
            out.write(f"Text:\n{q['question_text']}\n")
            out.write("Options:\n")
            for k, v in q['options'].items():
                out.write(f"  {k}: {v}\n")
            out.write(f"Correct Answer: {q.get('correct_answer')} or {q.get('correct_answers')}\n")
            out.write(f"Current Explanation:\n{q.get('explanation', '')}\n")
            out.write(f"Current Key Point:\n{q.get('key_point', '')}\n")
            out.write("="*60 + "\n\n")

if __name__ == '__main__':
    dump()
