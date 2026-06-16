import json
import os

def check_status():
    manifest_path = "public/data/manifest.json"
    if not os.path.exists(manifest_path):
        print("manifest.json not found!")
        return

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    exams = manifest.get("exams", [])
    
    # Group by year
    by_year = {}
    for exam in exams:
        year = exam["year"]
        if year not in by_year:
            by_year[year] = []
        by_year[year].append(exam)

    print(f"{'Year':<8} | {'Exam ID':<20} | {'Total Qs':<8} | {'With Exp':<8} | {'Pct':<6} | {'Missing Qs'}")
    print("-" * 80)

    summary_by_year = {}

    for year in sorted(by_year.keys()):
        year_total_qs = 0
        year_exp_qs = 0
        year_exams_info = []
        
        for exam in by_year[year]:
            exam_id = exam["id"]
            path = os.path.join("public", exam["path"].replace("/", os.sep))
            
            if not os.path.exists(path):
                print(f"File not found: {path} for exam {exam_id}")
                continue
                
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            questions = data.get("questions", [])
            total_qs = len(questions)
            
            # check how many have non-empty explanation
            with_exp = 0
            missing = []
            for q in questions:
                # check if explanation is empty or default or missing
                exp = q.get("explanation", "").strip()
                # standard check for valid explanation
                # let's also check if review_status is empty or not
                if exp and exp != "" and "請在此填寫" not in exp:
                    with_exp += 1
                else:
                    missing.append(q.get("question_number", "?"))
                    
            year_total_qs += total_qs
            year_exp_qs += with_exp
            
            pct = (with_exp / total_qs * 100) if total_qs > 0 else 0
            missing_str = ", ".join(map(str, missing[:10])) + ("..." if len(missing) > 10 else "")
            if not missing_str:
                missing_str = "None"
            print(f"{year:<8} | {exam_id:<20} | {total_qs:<8} | {with_exp:<8} | {pct:.1f}% | {missing_str}")
            
            year_exams_info.append({
                "id": exam_id,
                "total": total_qs,
                "with_exp": with_exp
            })
            
        summary_by_year[year] = {
            "total_qs": year_total_qs,
            "exp_qs": year_exp_qs,
            "pct": (year_exp_qs / year_total_qs * 100) if year_total_qs > 0 else 0,
            "exams": year_exams_info
        }
        print("-" * 80)

    print("\nSummary by Year:")
    print(f"{'Year':<8} | {'Total Qs':<8} | {'With Exp':<8} | {'Pct':<8} | {'Status'}")
    print("-" * 50)
    for year, info in sorted(summary_by_year.items()):
        status = "Ready" if info["pct"] == 100.0 else "Incomplete"
        print(f"{year:<8} | {info['total_qs']:<8} | {info['exp_qs']:<8} | {info['pct']:.1f}% | {status}")

if __name__ == "__main__":
    check_status()
