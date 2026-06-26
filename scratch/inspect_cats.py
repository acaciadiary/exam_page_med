import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("public/data/exams/115-1/medicine-4.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for idx, q in enumerate(data['questions']):
    print(f"{idx}: {q['id']} - Category: {q.get('category')}")
