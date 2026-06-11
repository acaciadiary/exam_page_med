import json
import os
from pathlib import Path

MANIFEST_PATH = Path("reports/gemini_prompts/manifest.json")
OUTPUT_DIR = Path("reports/gemini_outputs")

def load_manifest():
    if not MANIFEST_PATH.exists():
        print(f"Manifest not found at {MANIFEST_PATH}")
        return []
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("batches", [])

def get_status():
    batches = load_manifest()
    total = len(batches)
    completed = []
    pending = []
    
    if OUTPUT_DIR.exists():
        completed_ids = {p.stem for p in OUTPUT_DIR.glob("*.json")}
    else:
        completed_ids = set()
        
    for b in batches:
        bid = b["batch_id"]
        if bid in completed_ids:
            completed.append(b)
        else:
            pending.append(b)
            
    return total, completed, pending

def main():
    total, completed, pending = get_status()
    print(f"Total batches: {total}")
    print(f"Completed batches: {len(completed)}")
    print(f"Pending batches: {len(pending)}")
    
    # Print next few pending batches
    if pending:
        print("\nNext 10 pending batches:")
        for b in pending[:10]:
            print(f" - {b['batch_id']} ({b['question_count']} questions)")

if __name__ == "__main__":
    main()
