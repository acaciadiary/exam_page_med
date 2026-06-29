import json
import re
import subprocess
import sys
from pathlib import Path


EXAM_FILE = Path("public/data/exams/110-1/medicine-3.json")
UPDATE_SCRIPT = Path("scripts/exams/update_question_fields.py")
UPDATES_FILE = Path("scratch/updates_110-1_medicine-3_categories.json")
STRUCTURE_SCRIPT = Path("scratch/structure_110_1_explanations.py")


RULES = [
    ("醫學倫理與醫療決策", ["倫理", "告知", "同意", "自主", "病人權利", "醫療決策", "DNR"]),
    ("心臟內科", ["心臟", "心肌", "冠狀", "心電圖", "ECG", "心衰竭", "瓣膜", "心房", "心室", "高血壓", "arrhythmia", "angina"]),
    ("胸腔內科", ["肺功能", "氣喘", "COPD", "慢性阻塞", "呼吸衰竭", "胸腔", "肋膜", "肺栓塞", "ARDS", "咳嗽", "喘"]),
    ("肝膽腸胃科", ["肝", "膽", "胃", "腸", "胰", "腹痛", "腹瀉", "黃疸", "食道", "消化", "hepatitis", "cirrhosis", "pancreatitis"]),
    ("腎臟科", ["腎", "透析", "尿毒", "蛋白尿", "血尿", "酸鹼", "電解質", "鈉", "鉀", "creatinine", "GFR"]),
    ("新陳代謝科", ["糖尿", "甲狀腺", "腎上腺", "內分泌", "低血糖", "高血糖", "低體溫", "高血脂", "肥胖", "代謝"]),
    ("血液腫瘤科", ["貧血", "白血病", "淋巴瘤", "血小板", "凝血", "癌", "腫瘤", "化療", "hemoglobin", "leukemia", "lymphoma"]),
    ("免疫風濕科", ["關節炎", "紅斑性狼瘡", "自體免疫", "血管炎", "類風濕", "痛風", "SLE", "ANA"]),
    ("感染科", ["感染", "抗生素", "發燒", "敗血", "結核", "HIV", "菌", "病毒", "寄生蟲", "肺炎", "腦膜炎"]),
    ("神經內科", ["中風", "癲癇", "頭痛", "失智", "巴金森", "神經", "腦", "脊髓", "neuropathy", "stroke"]),
    ("家庭醫學科", ["篩檢", "預防", "疫苗", "戒菸", "健康檢查", "家庭醫學"]),
    ("急診醫學科", ["休克", "CPR", "急救", "中毒", "創傷", "昏迷", "急診", "低體溫"]),
]


def guess_category(question):
    text = " ".join(
        [
            str(question.get("question_text") or ""),
            " ".join(str(v) for v in (question.get("options") or {}).values()),
            str(question.get("key_point") or ""),
            str(question.get("explanation") or ""),
        ]
    )
    lowered = text.lower()
    for category, keywords in RULES:
        for keyword in keywords:
            if keyword.lower() in lowered:
                return category
    return "其他"


def main():
    data = json.loads(EXAM_FILE.read_text(encoding="utf-8-sig"))
    updates = []
    for question in data.get("questions", []):
        if not question.get("category"):
            updates.append(
                {
                    "id": question.get("id"),
                    "category": guess_category(question),
                    "category_confidence": 0.65,
                }
            )
    UPDATES_FILE.write_text(json.dumps(updates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    subprocess.run(
        [
            sys.executable,
            str(UPDATE_SCRIPT),
            "--exam-file",
            str(EXAM_FILE),
            "--updates-file",
            str(UPDATES_FILE),
        ],
        check=True,
    )
    subprocess.run([sys.executable, str(STRUCTURE_SCRIPT)], check=True)
    print(f"Medicine-3 categories filled: {len(updates)}")


if __name__ == "__main__":
    main()
