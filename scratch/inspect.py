import json

with open("public/data/exams/115-1/medicine-4.json", "r", encoding="utf-8") as f:
    data = json.load(f)

output_lines = []
output_lines.append(f"Total questions: {len(data['questions'])}")
for idx, q in enumerate(data['questions']):
    output_lines.append(f"Index: {idx}, ID: {q['id']}, Category: {q.get('category')}")
    output_lines.append(f"Question text: {q['question_text']}")
    output_lines.append(f"Options: {q.get('options')}")
    output_lines.append("-" * 50)

with open("scratch/inspect_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("Successfully written to scratch/inspect_output.txt")
