import json
import subprocess
import sys

def apply(updates):
    updates_path = "scratch/temp_updates.json"
    with open(updates_path, "w", encoding="utf-8") as f:
        json.dump(updates, f, ensure_ascii=False, indent=2)
    
    cmd = [
        "python",
        "scripts/exams/update_question_fields.py",
        "--exam-file", "public/data/exams/111-2/medicine-6.json",
        "--updates-file", updates_path
    ]
    print(f"Running command: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print("STDOUT:")
    print(res.stdout)
    print("STDERR:")
    print(res.stderr)
    if res.returncode != 0:
        raise RuntimeError("Failed to run update script")

if __name__ == "__main__":
    # Test script import check
    print("Loaded apply_updates.py helper")
