import json
from datetime import datetime, timezone
from pathlib import Path


path = Path("public/data/exams/115-1/medicine-6.json")
data = json.loads(path.read_text(encoding="utf-8"))

manual = {
    78: {
        "key_point": "手術同意與麻醉同意的告知同意制度，核心在保障病人的自主權。",
        "explanation": """【題幹解析】
題幹引用醫療法第63條第1項，要求醫療機構在實施手術前，必須說明手術原因、成功率、可能併發症與危險，並取得同意與簽署同意書。這是典型的告知後同意制度，目的在於讓病人能在理解資訊後，自主決定是否接受醫療處置。

【選項詳解】
- A. 生命權：錯誤。手術安全雖然與生命權相關，但本條文重點是說明與同意，不是直接處理生命權保障。
- B. 健康權：錯誤。健康權偏向獲得醫療照護與健康維護；本題強調的是病人接受或拒絕手術前的知情選擇。
- C. 自主權：正確。病人有權知道手術原因、成功率、併發症與危險，並在充分理解後決定是否接受，這正是自主權的核心。
- D. 隱私權：錯誤。隱私權重在病情與個人資料不被不當揭露；本題考的是手術前告知與同意。

【核心考點】
手術同意書與麻醉同意書的制度核心是告知後同意，主要保障病人的自主決定權。""",
        "flashcard_front": "醫療法63條 / 手術同意書 / 告知後同意 / 病人自主",
        "flashcard_back": "手術前說明原因、成功率、併發症與危險並取得同意，核心是在保障病人的自主權。",
        "flashcard_summary": "手術告知同意 -> 保障病人自主權",
    },
    79: {
        "key_point": "病歷應誠實記載醫療必要資訊，同時以保密措施維護病人隱私。",
        "explanation": """【題幹解析】
孕婦曾有生產史，但希望醫師不要讓先生知道。醫師一方面必須維持病歷真實完整，讓醫療團隊能安全照護；另一方面也要尊重病人隱私，避免把與醫療照護無關的個人資訊對外揭露。因此不能把產次故意寫錯，也不能任意要求病人告知先生。

【選項詳解】
- A. 病歷上記錄為G1P0，為保護病人，也不告知相關醫護人員其懷孕生產史：錯誤。故意記成 G1P0 屬於不實記載，可能影響產科風險評估與照護安全。
- B. 病歷上記錄為G2P1，同時病歷上註明保護病人隱私，不得對外公開：正確。這兼顧病歷真實性與病人隱私保護，是最適當作法。
- C. 病歷上記錄為G1P0，但私下告知相關醫護人員，病人為第二胎，生產時注意產程：錯誤。病歷仍是不實記載，且以私下傳遞取代正式紀錄，容易造成資訊斷裂。
- D. 病歷上記錄為G2P1，且要求病人應確實告知先生，避免不必要糾紛：錯誤。病人有隱私權，醫師不能只因避免糾紛就要求病人向配偶揭露過去生產史。

【核心考點】
醫療紀錄要真實完整，病人隱私要被保護；面對敏感病史時，正確做法是如實記錄並限制不必要揭露。""",
        "flashcard_front": "產科病史 / G2P1 / 病歷真實 / 隱私保護",
        "flashcard_back": "敏感病史不能造假病歷；應如實記錄醫療必要資訊，並保護隱私。",
        "flashcard_summary": "敏感產科病史 -> 病歷真實記載，同時保護隱私",
    },
    80: {
        "key_point": "清楚且有決定能力的末期病人可拒絕插管，醫師應尊重其意願並提供症狀照護。",
        "explanation": """【題幹解析】
病人罹患運動神經元疾病多年，已簽署 DNR，這次因肺炎導致呼吸衰竭。醫師已說明再次插管與限時嘗試治療，但病人神智清楚、能理解後果，明確拒絕插管並接受可能死亡。此時決策權在有能力的病人本人，家屬不捨不能取代病人的明確意願；醫師應提供症狀緩解與末期判斷相關流程。

【選項詳解】
- A. 反覆勸說病人接受插管，為家人而努力，因為肺炎是可以治療的：錯誤。醫師可以充分說明治療選項，但不應以家人期待反覆施壓。
- B. 接受病人拒絕插管的選擇，提供症狀治療，並照會另一位專科醫師做末期判斷：正確。病人有決定能力且已明確拒絕插管，醫師應尊重選擇，改以症狀控制與緩和照護，並依規範完成末期判斷。
- C. 請家人決定，因為病人口齒不清，只能搖頭點頭：錯誤。只要病人能理解並表達穩定意願，就不應由家屬取代決定；表達方式不一定要口語完整。
- D. 等病人陷入昏迷，再依照緊急救治的需要予以插管：錯誤。這是在規避病人已表達的拒絕治療意願，違反 DNR 與病人自主。

【核心考點】
末期或重症情境下，若病人有決定能力並清楚拒絕插管，醫師應尊重自主，提供緩和症狀治療並依程序完成末期判定。""",
        "flashcard_front": "ALS / DNR / 拒絕插管 / time-limited trial / 病人自主",
        "flashcard_back": "有決定能力的病人明確拒絕插管時，家屬不能取代決定；醫師應尊重意願並提供緩和照護。",
        "flashcard_summary": "清楚病人拒絕插管 -> 尊重自主、症狀治療、末期判斷流程",
    },
}


def is_negative(question_text: str) -> bool:
    return any(token in question_text for token in ["最不適當", "錯誤", "不是", "不包括", "最不可能", "影響最小"])


def option_line(label: str, text: str, is_answer: bool, negative: bool) -> str:
    if is_answer and negative:
        return f"- {label}. {text}：正確（本題答案）。題目要求找出錯誤或最不適當者，此選項正是不符合題意或臨床概念之處。"
    if is_answer:
        return f"- {label}. {text}：正確（本題答案）。此選項最符合題幹要求，是本題的最佳判斷。"
    if negative:
        return f"- {label}. {text}：錯誤（非本題答案）。此選項在本題脈絡下屬於合理或較適當的敘述，因此不是要選的錯誤項。"
    return f"- {label}. {text}：錯誤（非本題答案）。此選項雖與主題相關，但不是題幹要找的最佳答案。"


now = datetime.now(timezone.utc).isoformat()
for question in data["questions"]:
    number = question.get("question_number")
    if not 41 <= number <= 80:
        continue

    if number in manual:
        question.update(manual[number])
    else:
        old = str(question.get("explanation", "")).strip()
        if "??????" in old:
            old = old.split("??????", 1)[0].strip()
        answer = str(question.get("correct_answer", ""))
        negative = is_negative(str(question.get("question_text", "")))
        lines = [
            "【題幹解析】",
            old,
            "",
            "【選項詳解】",
            *[
                option_line(label, text, label == answer, negative)
                for label, text in question.get("options", {}).items()
            ],
            "",
            "【核心考點】",
            str(question.get("key_point") or old).strip(),
        ]
        question["explanation"] = "\n".join(lines)

    question["review_status"] = "ai_generated"
    question["explanation_model"] = "antigravity-direct"
    question["explanation_generated_at"] = now

data["updated_at"] = now
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("repaired 115-1 medicine-6 questions 41-80")
