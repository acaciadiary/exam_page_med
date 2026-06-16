import json
import os
from collections import defaultdict

def check():
    manifest_path = "reports/gemini_prompts/manifest.json"
    if not os.path.exists(manifest_path):
        print("Manifest not found!")
        return
        
    with open(manifest_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    batches = data.get("batches", [])
    
    # Group batches by year
    # batch_id looks like: "109-1_medicine-3_batch-006"
    # year would be "109-1"
    by_year_batches = defaultdict(list)
    for b in batches:
        bid = b["batch_id"]
        parts = bid.split("_")
        year = parts[0]
        by_year_batches[year].append(b)
        
    completed_ids = set()
    output_dir = "reports/gemini_outputs"
    if os.path.exists(output_dir):
        completed_ids = {f[:-5] for f in os.listdir(output_dir) if f.endswith(".json")}
        
    print(f"{'Year':<8} | {'Total Batches':<15} | {'Completed':<10} | {'Pending':<8} | {'Status'}")
    print("-" * 60)
    
    for year in sorted(by_year_batches.keys()):
        year_batches = by_year_batches[year]
        total = len(year_batches)
        comp = sum(1 for b in year_batches if b["batch_id"] in completed_ids)
        pend = total - comp
        status = "ALL COMPLETED" if pend == 0 else "Incomplete"
        print(f"{year:<8} | {total:<15} | {comp:<10} | {pend:<8} | {status}")
        
if __name__ == "__main__":
    check()
