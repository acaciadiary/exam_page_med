import sys
from pathlib import Path
from scripts.exams.import_gemini_explanations import import_outputs, expand_paths

years = ["108-1", "108-2", "109-1", "109-2", "110-1", "110-2", "111-1", "111-2", "112-1"]

print("Starting direct dry run verification for all completed years...")
print("-" * 65)

all_ok = True
for y in years:
    pattern = f"reports/gemini_outputs/{y}_*.json"
    paths = expand_paths([pattern])
    
    if not paths:
        print(f"Year {y:<8}: FAILED (No files found for pattern {pattern})")
        all_ok = False
        continue
        
    try:
        report = import_outputs(
            output_paths=paths,
            data_dir=Path("public/data/exams"),
            dry_run=True,
            model_label="gemini-pro-manual"
        )
        print(f"Year {y:<8}: OK (Imported: {report['imported']}, Skipped: {report['skipped']})")
    except Exception as e:
        print(f"Year {y:<8}: FAILED")
        print(f"  Error: {e}")
        all_ok = False

print("-" * 65)
if all_ok:
    print("All completed years passed dry-run validation successfully!")
    sys.exit(0)
else:
    print("Some completed years failed dry-run validation!")
    sys.exit(1)
