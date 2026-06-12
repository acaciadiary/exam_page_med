# -*- coding: utf-8 -*-
import json

batch_data = {
    "dataset_id": "108-2_medicine-3",
    "batch_id": "108-2_medicine-3_batch-006",
    "items": [
        {
            "question_id": "108-2_medicine-3_076",
            "question_number": 76,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "急診医学科",
            "category_confidence": "high",
            "key_point": "分辨導致心搏過緩與低血壓的中毒藥物與其排除。",
            "explanation": "有機磷（Organophosphates）、氨基甲酸酯（Carbamates，兩者皆為膽鹼酯酶抑制劑）以及 Clonidine（alpha-2 促效劑）中毒時，皆會引起嚴重的副交感神經興奮或中樞交感抑制，導致心搏過緩合併低血壓。抗組織胺過量則常表現為抗膽鹼毒性，會出現心跳過速與皮膚乾燥，最不可能引起心搏過緩合併低血壓。",
            "flashcard_front": "藥物中毒 / 心搏過緩合併低血壓 / 有機磷 / 氨基甲酸酯 / 克隆尼丁 / 抗組織胺",
            "flashcard_back": "有機磷、氨基甲酸酯及克隆尼丁中毒可引起低血壓與心搏過緩；抗組織胺過量則常因抗膽鹼作用導致心跳過速。",
            "flashcard_summary": "藥物中毒心臟症狀 -> 有機磷與克隆尼丁引起心搏過緩，抗組織胺過量則引起心跳過速。"
        },
        {
            "question_id": "108-2_medicine-3_077",
            "question_number": 77,
            "correct_answer": "",
            "category_group": "醫學（三）",
            "category": "急診医学科",
            "category_confidence": "high",
            "key_point": "掌握路易絲湖急性高山病評估表的症狀評估標準。",
            "explanation": "路易絲湖急性高山病（AMS）評估標準包括頭痛（核心症狀）、胃腸症狀（噁心、嘔吐）、疲倦虛弱與頭暈。腹瀉（C）從未列入評估項目；此外，2018年修訂版評估表中，亦將睡眠障礙（D，失眠）移除。因此本題中腹瀉與失眠皆不屬於評估指標，官方最後更正答C、D皆給分。",
            "flashcard_front": "路易絲湖急性高山病 / 症狀評估 / 頭痛、噁心嘔吐 / 腹瀉、失眠 / 2018年修訂",
            "flashcard_back": "路易絲湖評估表包含頭痛、胃腸不適、頭暈與疲倦。腹瀉從未列入，且2018年版已刪除失眠指標。",
            "flashcard_summary": "高山病路易絲湖評估 -> 評估指標包含頭痛與胃腸症狀，不含腹瀉，且2018年起已移除失眠項目。"
        },
        {
            "question_id": "108-2_medicine-3_078",
            "question_number": 78,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "掌握二氫吡啶類鈣離子通道阻斷劑（CCB）的腸胃道副作用機轉。",
            "explanation": "Amlodipine 為二氫吡啶類（dihydropyridine）鈣離子通道阻斷劑，藉由阻斷 L 型鈣通道鬆弛平滑肌以降低血壓，但此機轉也會抑制胃腸道平滑肌蠕動，容易引起腹脹、便秘與下肢水腫。Valsartan（ARB）與 Renitec（ACEI）則較少引起便秘與腹脹副作用。",
            "flashcard_front": "高血壓換藥 / 腹脹與便秘 / L型鈣通道阻斷 / Amlodipine / 平滑肌鬆弛",
            "flashcard_back": "Amlodipine 阻斷鈣離子通道以降壓，但會抑制腸胃平滑肌蠕動，從而引發腹脹與便秘副作用。",
            "flashcard_summary": "Amlodipine副作用 -> Amlodipine 會抑制腸胃平滑肌收縮，進而引發腹脹與便秘。"
        },
        {
            "question_id": "108-2_medicine-3_079",
            "question_number": 79,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "醫學倫理與醫療決策",
            "category_confidence": "high",
            "key_point": "理解醫師親自診察並開立處方的法律義務義務。",
            "explanation": "依我國《醫師法》第 11 條規定，醫師非親自診察，不得施行治療、開給方劑或交付診斷書。王醫師交代護理人員在未親自診察病患的情況下蓋章交付處方箋，已嚴重違反親自診療的義務，不因「方便病人」或「釋出處方」而免責。",
            "flashcard_front": "醫師出國 / 護士蓋章開藥 / 親自診察義務 / 醫師法第11條 / 醫療法規",
            "flashcard_back": "醫師法規定醫師必須「親自診察」方得開立處方箋，交代護士代蓋章開藥屬違法行為。",
            "flashcard_summary": "醫師親自診察義務 -> 醫師必須親自診察病患才能開立處方，由護理人員代蓋章處方屬違法行為。"
        },
        {
            "question_id": "108-2_medicine-3_080",
            "question_number": 80,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "醫學倫理與醫療決策",
            "category_confidence": "high",
            "key_point": "釐清 DNR 意願書的適用範疇與急性可治癒併發症的治療原則。",
            "explanation": "DNR（拒絕施行心肺復甦術）僅在病人處於末期狀態且發生心肺衰竭需 CPR 時生效。患者本次因急性泌尿道感染合併敗血性休克入院，屬於仍可透過抗生素及點滴治癒的疾病，故不適用 DNR 限制，醫師在溝通後，仍可依臨床需要為其插管或進行積極抗感染與點滴治療。",
            "flashcard_front": "肺癌末期 / DNR 意願書 / 泌尿道發炎、敗血性休克 / 氣管插管、抗生素 / 適用界線",
            "flashcard_back": "DNR 僅適用於心肺衰竭急救；急性可治癒併發症（如敗血性休克）仍應積極治療，包括插管與抗生素。",
            "flashcard_summary": "DNR適用範疇 -> DNR 意願書僅於末期心肺衰竭急救時生效，對於可治癒之急性併發症仍應積極救治。"
        }
    ]
}
