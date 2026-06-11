import json
import os

# Create outputs directory if it doesn't exist
os.makedirs("reports/gemini_outputs", exist_ok=True)

# Batch 005
batch_005 = {
  "dataset_id": "108-1_medicine-6",
  "batch_id": "108-1_medicine-6_batch-005",
  "items": [
    {
      "question_id": "108-1_medicine-6_061",
      "question_number": 61,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "助行器的功能及其提供感覺回饋的特性",
      "explanation": "使用助行器除了能改善平衡、重新分配下肢承載區域並減少疼痛外，其與地面的接觸還能提供重要的本體感覺與觸覺回饋，協助使用者感知身體位置。因此選項B「無法提供感覺的回饋」為錯誤敘述。",
      "flashcard_front": "助行器 / 感覺回饋 / 平衡與承重",
      "flashcard_back": "助行器能提供本體感覺與觸覺回饋，並非只能提供力量支撐。",
      "flashcard_summary": "助行器 / 感覺回饋 / 平衡與承重 -> 助行器能提供本體感覺與觸覺回饋，並非只能提供力量支撐。"
    },
    {
      "question_id": "108-1_medicine-6_062",
      "question_number": 62,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "關節炎手部副木的臨床使用目的與限制",
      "explanation": "副木（splint）主要用於固定支持關節、增進抓握力、協助手部功能及減緩關節變形，但它屬於外部物理輔具，並無法改變關節炎本身的病理進展或延緩疾病本身的進程。因此選項D為錯誤敘述。",
      "flashcard_front": "關節炎副木 / 手部功能 / 延緩疾病進程",
      "flashcard_back": "副木能減緩變形與促進功能，但無法延緩關節炎疾病本身的病理進程。",
      "flashcard_summary": "關節炎副木 / 手部功能 / 延緩疾病進程 -> 副木能減緩變形與促進功能，但無法延緩關節炎疾病本身的病理進程。"
    },
    {
      "question_id": "108-1_medicine-6_063",
      "question_number": 63,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "間歇性跛行的首選診斷檢查",
      "explanation": "患者表現出走路十多分鐘後雙下肢酸痛麻木、休息後立即緩解的典型間歇性跛行，高度暗示為腰椎管狹窄症（spinal stenosis）。磁振造影（MRI）對於軟組織、神經根壓迫及椎管狹窄的結構解析度最佳，是確診的最佳檢查。因此選項D正確。",
      "flashcard_front": "間歇性跛行 / 走路酸痛 / 坐下改善 / 首選檢查",
      "flashcard_back": "間歇性跛行暗示腰椎管狹窄症，首選磁振造影（MRI）檢查以確診。",
      "flashcard_summary": "間歇性跛行 / 走路酸痛 / 坐下改善 / 首選檢查 -> 間歇性跛行暗示腰椎管狹窄症，首選磁振造影（MRI）檢查以確診。"
    },
    {
      "question_id": "108-1_medicine-6_064",
      "question_number": 64,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "類風濕性關節炎的復健治療團隊合作",
      "explanation": "類風濕性關節炎的復健需要物理治療與職能治療（OT）共同參與。職能治療在教導病患關節保護原則、設計副木、調整日常活動及適應居家/工作環境方面不可或缺。因此「大多數病人不需職能治療」是錯誤的。",
      "flashcard_front": "類風濕性關節炎 / 復健治療 / 職能治療必要性",
      "flashcard_back": "類風濕性關節炎患者高度需要職能治療來教導關節保護與副木製作，並非不需要。",
      "flashcard_summary": "類風濕性關節炎 / 復健治療 / 職能治療必要性 -> 類風濕性關節炎患者高度需要職能治療來教導關節保護與副木製作，並非不需要。"
    },
    {
      "question_id": "108-1_medicine-6_065",
      "question_number": 65,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "ACSM對正常人心肺耐力訓練的指引建議",
      "explanation": "根據美國運動醫學院（ACSM）的指引，針對正常人的心肺耐力訓練，建議每週進行3至5天。心肺訓練每次應持續20至60分鐘，且以大肌肉群的動態運動為主，而非小肌肉群靜態運動。因此選項C正確。",
      "flashcard_front": "ACSM / 心肺耐力訓練 / 頻率與時間 / 運動型態",
      "flashcard_back": "正常人心肺耐力訓練建議每週3-5天，每次20-60分鐘，以大肌肉群動態運動為主。",
      "flashcard_summary": "ACSM / 心肺耐力訓練 / 頻率與時間 / 運動型態 -> 正常人心肺耐力訓練建議每週3-5天，每次20-60分鐘，以大肌肉群動態運動為主。"
    },
    {
      "question_id": "108-1_medicine-6_066",
      "question_number": 66,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "COPD患者的肺部物理治療與呼吸運動原則",
      "explanation": "慢性阻塞性肺疾病（COPD）患者在進行呼吸運動時，應使用撅唇呼吸並強調「慢而深」的呼吸方式，這能維持吐氣期氣道的正壓，防止小氣道過早塌陷。因此「強調快而淺的呼吸法」是錯誤的。",
      "flashcard_front": "COPD / 呼吸運動 / 撅唇呼吸 / 呼吸節奏",
      "flashcard_back": "COPD患者應採用慢而深的呼吸法以減少死腔，撅唇呼吸可維持呼氣期氣道正壓。",
      "flashcard_summary": "COPD / 呼吸運動 / 撅唇呼吸 / 呼吸節奏 -> COPD患者應採用慢而深的呼吸法以減少死腔，撅唇呼吸可維持呼氣期氣道正壓。"
    },
    {
      "question_id": "108-1_medicine-6_067",
      "question_number": 67,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "裘馨氏肌肉失養症的遺傳模式與高爾氏徵象的病理機制",
      "explanation": "高爾氏徵象（Gowers' sign）是裘馨氏肌肉失養症（DMD）患者因「近端」骨盆帶肌肉與大腿肌無力，導致站立時必須雙手交替撐在自己大腿上才能起立的現象，而非遠端肢體無力所致。因此選項D敘述錯誤。",
      "flashcard_front": "DMD / 走路搖擺 / 高爾氏徵象 / 近端與遠端無力",
      "flashcard_back": "高爾氏徵象是由於近端肢體及骨盆帶肌肉無力，導致需雙手撐大腿起立，非遠端無力。",
      "flashcard_summary": "DMD / 走路搖擺 / 高爾氏徵象 / 近端與遠端無力 -> 高爾氏徵象是由於近端肢體及骨盆帶肌肉無力，導致需雙手撐大腿起立，非遠端無力。"
    },
    {
      "question_id": "108-1_medicine-6_068",
      "question_number": 68,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "其他",
      "category_confidence": "high",
      "key_point": "腦性麻痺的危險因子與病因評估",
      "explanation": "出生體重小於2500公克（早產/低體重）、新生兒癲癇發作（提示腦損傷）及母親智能障礙皆是文獻記載中明確的腦性麻痺危險因子。相較之下，胎兒心跳過快雖可能與胎兒窘迫相關，但並非腦性麻痺的直接致病因子。因此選項A為最不會造成腦性麻痺的因素。",
      "flashcard_front": "腦性麻痺 / 危險因子 / 低出生體重 / 新生兒癲癇",
      "flashcard_back": "低體重、新生兒癲癇與母親智障是腦麻危險因子，胎兒心跳過快本身非直接致病原因。",
      "flashcard_summary": "腦性麻痺 / 危險因子 / 低出生體重 / 新生兒癲癇 -> 低體重、新生兒癲癇與母親智障是腦麻危險因子，胎兒心跳過快本身非直接致病原因。"
    },
    {
      "question_id": "108-1_medicine-6_069",
      "question_number": 69,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "足底筋膜炎夜間護具固定角度的原則",
      "explanation": "足底筋膜炎患者在夜間使用足踝部護具（AFO）時，應將踝關節固定在「背屈（dorsiflexion）」或中立位置，以持續拉伸足底筋膜。若固定在最大蹠屈（plantar flexion）位置，會使筋膜處於縮短狀態，晨起下床時的第一步會更加劇痛。因此選項C錯誤。",
      "flashcard_front": "足底筋膜炎 / 夜間護具固定角度 / 背屈與蹠屈",
      "flashcard_back": "足底筋膜炎夜間護具應固定在背屈或中立位以拉伸筋膜，不可固定在最大蹠屈位。",
      "flashcard_summary": "足底筋膜炎 / 夜間護具固定角度 / 背屈與蹠屈 -> 足底筋膜炎夜間護具應固定在背屈或中立位以拉伸筋膜，不可固定在最大蹠屈位。"
    },
    {
      "question_id": "108-1_medicine-6_070",
      "question_number": 70,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "尺神經受損導致的鷹爪手與肌肉萎縮",
      "explanation": "尺神經（ulnar nerve）主要支配手部的小魚肌及第四、五指的蚓狀肌。當尺神經受損時，會因蚓狀肌無力導致第四、五指無法完全伸直，且伴隨小魚肌萎縮，形成臨床上典型的「鷹爪手（claw hand）」。因此選項A正確。",
      "flashcard_front": "鷹爪手 / 第四五指無法伸直 / 小魚肌萎縮 / 受損神經",
      "flashcard_back": "第四五指呈鷹爪狀且小魚肌萎縮，為尺神經（ulnar nerve）受損的特徵。",
      "flashcard_summary": "鷹爪手 / 第四五指無法伸直 / 小魚肌萎縮 / 受損神經 -> 第四五指呈鷹爪狀且小魚肌萎縮，為尺神經（ulnar nerve）受損的特徵。"
    },
    {
      "question_id": "108-1_medicine-6_071",
      "question_number": 71,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "不同類型失語症的覆誦能力比較",
      "explanation": "命名性失語症（anomic aphasia）患者的主要臨床表現為尋詞困難（即叫不出名字），但其口語理解與覆誦（repetition）能力通常保存良好。相較之下，傳導性失語症（conduction aphasia）的核心特徵即為嚴重的覆誦受損。因此選項B為覆誦能力最佳者。",
      "flashcard_front": "失語症 / 覆誦能力良好 / 命名困難",
      "flashcard_back": "命名性失語症（anomic aphasia）的覆誦能力良好，而傳導性失語症則覆誦嚴重受損。",
      "flashcard_summary": "失語症 / 覆誦能力良好 / 命名困難 -> 命名性失語症（anomic aphasia）的覆誦能力良好，而傳導性失語症則覆誦嚴重受損。"
    },
    {
      "question_id": "108-1_medicine-6_072",
      "question_number": 72,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "年輕男性頸部無痛性腫塊與鼻咽癌轉移",
      "explanation": "21歲年輕男性在台灣等鼻咽癌高盛行率地區，若出現上頸部（Level II）無痛性腫塊，且電腦斷層顯示淋巴結病變，臨床上必須首要警惕鼻咽癌轉移。深頸部感染及上呼吸道感染通常會伴隨明顯疼痛、發燒與發炎指標上升，而淋巴管瘤則多在嬰幼兒期即被發現。因此最可能診斷為鼻咽癌。",
      "flashcard_front": "21歲男性 / 上頸部無痛硬塊 / 台灣高盛行率 / 轉移性淋巴結",
      "flashcard_back": "年輕人上頸部無痛腫塊在台灣需高度懷疑為鼻咽癌轉移，應進行鼻咽內視鏡及切片。",
      "flashcard_summary": "21歲男性 / 上頸部無痛硬塊 / 台灣高盛行率 / 轉移性淋巴結 -> 年輕人上頸部無痛腫塊在台灣需高度懷疑為鼻咽癌轉移，應進行鼻咽內視鏡及切片。"
    },
    {
      "question_id": "108-1_medicine-6_073",
      "question_number": 73,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "停經後陰道出血與子宮頸癌的影像診斷",
      "explanation": "已停經女性若主訴不正常陰道出血，雖需排除子宮內膜癌，但在磁振造影（MRI）上觀察到子宮頸部明顯的實體腫瘤侵犯與邊緣破壞，為典型的子宮頸癌影像表現。因此本題最可能的診斷為子宮頸癌。",
      "flashcard_front": "停經後出血 / 子宮頸部實體腫瘤 / MRI影像",
      "flashcard_back": "已停經陰道出血且影像顯示子宮頸腫塊浸潤與破壞，最可能診斷為子宮頸癌。",
      "flashcard_summary": "停經後出血 / 子宮頸部實體腫瘤 / MRI影像 -> 已停經陰道出血且影像顯示子宮頸腫塊浸潤與破壞，最可能診斷為子宮頸癌。"
    },
    {
      "question_id": "108-1_medicine-6_074",
      "question_number": 74,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "臂神經叢損傷中神經根撕裂傷的解剖分類",
      "explanation": "神經根撕裂傷（root avulsion）是指神經根從脊髓連接處拉扯撕裂，此病理變化屬於「節前（pre-ganglionic）」損傷，而非節後（post-ganglionic）分離。節前損傷通常預後極差且不易自行恢復。因此選項D敘述錯誤。",
      "flashcard_front": "臂神經叢損傷 / 神經根撕裂 / 節前與節後損傷",
      "flashcard_back": "神經根撕裂傷（root avulsion）屬於脊髓連接處撕脫的節前（pre-ganglionic）損傷。",
      "flashcard_summary": "臂神經叢損傷 / 神經根撕裂 / 節前與節後損傷 -> 神經根撕裂傷（root avulsion）屬於脊髓連接處撕脫的節前（pre-ganglionic）損傷。"
    },
    {
      "question_id": "108-1_medicine-6_075",
      "question_number": 75,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "其他",
      "category_confidence": "high",
      "key_point": "顱外頸動脈剝離的治療策略與禁忌",
      "explanation": "顱外頸動脈剝離（carotid dissection）首選以抗凝血或抗血小板藥物治療，若藥物無效可考慮置放血管支架。由於血管壁剝離面非常脆弱且結構不穩定，進行頸動脈內膜切除術（carotid endarterectomy）極易造成動脈破裂或血栓栓塞，因此為手術禁忌。所以選項B敘述錯誤。",
      "flashcard_front": "頸動脈剝離 / 藥物治療 / 支架置放 / 內膜切除術禁忌",
      "flashcard_back": "頸動脈剝離因血管壁脆弱，禁用頸動脈內膜切除術治療以防血管破裂或血栓。",
      "flashcard_summary": "頸動脈剝離 / 藥物治療 / 支架置放 / 內膜切除術禁忌 -> 頸動脈剝離因血管壁脆弱，禁用頸動脈內膜切除術治療以防血管破裂或血栓。"
    }
  ]
}

# Batch 006
batch_006 = {
  "dataset_id": "108-1_medicine-6",
  "batch_id": "108-1_medicine-6_batch-006",
  "items": [
    {
      "question_id": "108-1_medicine-6_076",
      "question_number": 76,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "紅眼合併畏光症狀的鑑別診斷",
      "explanation": "畏光（photophobia）通常表示病變累及較深層的眼部構造，如角膜炎、虹膜炎或急性青光眼等。而單純的急性結膜炎（acute conjunctivitis）主要表現為結膜充血、分泌物增多與異物感，極少會引起明顯的畏光症狀。因此選項A為最不可能之診斷。",
      "flashcard_front": "紅眼 / 畏光 / 急性結膜炎 / 虹膜炎與角膜炎",
      "flashcard_back": "單純急性結膜炎通常不引起明顯畏光；畏光常提示角膜炎、虹膜炎或青光眼等深層病變。",
      "flashcard_summary": "紅眼 / 畏光 / 急性結膜炎 / 虹膜炎與角膜炎 -> 單純急性結膜炎通常不引起明顯畏光；畏光常提示角膜炎、虹膜炎或青光眼等深層病變。"
    },
    {
      "question_id": "108-1_medicine-6_077",
      "question_number": 77,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "急性中耳炎的治療原則",
      "explanation": "急性中耳炎不論是兒童或成人，治療皆以口服抗生素（如 amoxicillin 作為首選）及症狀緩解藥物等保守治療為主，極少需要於急性期進行手術。因此選項D「成人急性中耳炎常需手術治療」是錯誤的。",
      "flashcard_front": "急性中耳炎 / 首選抗生素 / 手術時機",
      "flashcard_back": "急性中耳炎首選 amoxicillin 藥物治療，不論兒童或成人急性期皆不常需手術。",
      "flashcard_summary": "急性中耳炎 / 首選抗生素 / 手術時機 -> 急性中耳炎首選 amoxicillin 藥物治療，不論兒童或成人急性期皆不常需手術。"
    },
    {
      "question_id": "108-1_medicine-6_078",
      "question_number": 78,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "真產痛與假產痛的臨床特徵鑑別",
      "explanation": "真產痛（true labor pain）的疼痛通常起自「背部」並向前放射至「下腹部」，常伴隨子宮頸擴張與規則宮縮。假產痛（false labor pain）則多侷限於「下腹部」與腹股溝，並非先由上腹部開始痛到下腹。因此選項A敘述錯誤。",
      "flashcard_front": "真產痛 / 假產痛 / 疼痛起始部位 / 子宮頸擴張",
      "flashcard_back": "真產痛常起自背部並放射至下腹且伴子宮頸擴張；假產痛僅侷限於下腹或腹股溝。",
      "flashcard_summary": "真產痛 / 假產痛 / 疼痛起始部位 / 子宮頸擴張 -> 真產痛常起自背部並放射至下腹且伴子宮頸擴張；假產痛僅侷限於下腹或腹股溝。"
    },
    {
      "question_id": "108-1_medicine-6_079",
      "question_number": 79,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "醫學倫理與醫療決策",
      "category_confidence": "high",
      "key_point": "未成年性行為的醫療通報法定義務",
      "explanation": "根據我國《兒童及少年福利與權益保障法》與《性侵害犯罪防治法》，醫療人員知悉未滿16歲（此處為13歲，刑法上屬妨害性自主範疇）的兒少發生性行為，具有法定的強制通報義務。因此醫師必須通報家長或社會主管機關，不能以隱私為由而不予揭露。故選B。",
      "flashcard_front": "13歲少女性行為 / 醫師保密 vs. 通報義務",
      "flashcard_back": "未滿16歲發生性行為，醫療人員有法定強制通報義務，須依法報告家長或主管機關。",
      "flashcard_summary": "13歲少女性行為 / 醫師保密 vs. 通報義務 -> 未滿16歲發生性行為，醫療人員有法定強制通報義務，須依法報告家長或主管機關。"
    },
    {
      "question_id": "108-1_medicine-6_080",
      "question_number": 80,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "醫學倫理與醫療決策",
      "category_confidence": "high",
      "key_point": "醫療知情同意權的限制與法定強制例外",
      "explanation": "唐氏症患者雖有智能障礙，但其住院治療仍需取得法定代理人或監護人的同意，非屬免除知情同意的法定義外。而緊急危及生命（選項A）、嚴重精神疾病有自傷傷人之虞的強制住院（選項B）、法定傳染病強制隔離（選項C），皆是依法可免除當下患者同意的例外。因此選項D為正確答案。",
      "flashcard_front": "免除知情同意例外 / 緊急避難 / 精神強制住院 / 唐氏症住院",
      "flashcard_back": "唐氏症患者住院仍需取得監護人同意，不屬於免除知情同意的法定強制例外情形。",
      "flashcard_summary": "免除知情同意例外 / 緊急避難 / 精神強制住院 / 唐氏症住院 -> 唐氏症患者住院仍需取得監護人同意，不屬於免除知情同意的法定強制例外情形。"
    }
  ]
}

# Batch 108-2_medicine-1_batch-001
batch_001 = {
  "dataset_id": "108-2_medicine-1",
  "batch_id": "108-2_medicine-1_batch-001",
  "items": [
    {
      "question_id": "108-2_medicine-1_001",
      "question_number": 1,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "進出眼眶不經過總腱環的腦神經分支",
      "explanation": "穿過上眼眶裂但走在總腱環（common tendinous ring）之外的構造主要包括額神經（1）、淚神經（4）與滑車神經（5），合稱 LFT。而鼻睫神經（2）、動眼神經（3）與外旋神經（6）則會穿過總腱環內部。因此不穿過總腱環者為1、4、5，選項D正確。",
      "flashcard_front": "總腱環外側 / 穿過上眼眶裂 / 額神經 / 淚神經 / 滑車神經",
      "flashcard_back": "額神經、淚神經與滑車神經（LFT）走在總腱環外；鼻睫、動眼與外旋神經則走在環內。",
      "flashcard_summary": "總腱環外側 / 穿過上眼眶裂 / 額神經 / 淚神經 / 滑車神經 -> 額神經、淚神經與滑車神經（LFT）走在總腱環外；鼻睫、動眼與外旋神經則走在環內。"
    },
    {
      "question_id": "108-2_medicine-1_003",
      "question_number": 3,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "翼腭窩與周邊顱骨孔道的解剖交通關係",
      "explanation": "翼腭窩（pterygopalatine fossa）的後上方可經由圓孔（foramen rotundum）及翼管（pterygoid canal）交通至中顱窩（middle cranial fossa）。其餘方向中，前內側經蝶腭孔通鼻腔（選項A），外側經翼上頜裂通顳下窩（選項B），下方經腭大管通口腔（選項D）。因此正確答案為C。",
      "flashcard_front": "翼腭窩 / 後上方通路 / 中顱窩 / 圓孔與翼管",
      "flashcard_back": "翼腭窩的後上方經由圓孔與翼管通往中顱窩；前內通鼻腔，外通顳下窩，下通口腔。",
      "flashcard_summary": "翼腭窩 / 後上方通路 / 中顱窩 / 圓孔與翼管 -> 翼腭窩的後上方經由圓孔與翼管通往中顱窩；前內通鼻腔，外通顳下窩，下通口腔。"
    },
    {
      "question_id": "108-2_medicine-1_004",
      "question_number": 4,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "咯血血液的解剖血管來源",
      "explanation": "咯血（hemoptysis）的血液主要來自體循環的支氣管動脈（bronchial artery），約佔所有咯血病例的90%以上，因為支氣管動脈為高壓系統，當支氣管發炎或病變（如肺結核）時易破裂出血。而肺動脈為低壓系統，其出血率相對極低。因此正確答案為C。",
      "flashcard_front": "咯血 / 血液來源 / 支氣管動脈 vs. 肺動脈",
      "flashcard_back": "咯血的血液最常源自高壓體循環的支氣管動脈，而非低壓的肺動脈。",
      "flashcard_summary": "咯血 / 血液來源 / 支氣管動脈 vs. 肺動脈 -> 咯血的血液最常源自高壓體循環的支氣管動脈，而非低壓的肺動脈。"
    },
    {
      "question_id": "108-2_medicine-1_005",
      "question_number": 5,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "迷走神經穿過膈肌的解剖裂孔",
      "explanation": "前、後迷走神經幹伴隨食道，一同穿過膈肌的食道裂孔（esophageal hiatus，約在T10水平）進入腹腔。腔靜脈孔（選項C，約T8）通過下腔靜脈與右膈神經；主動脈孔（選項B，約T12）通過主動脈、奇靜脈與胸導管。因此正確答案為A。",
      "flashcard_front": "迷走神經穿膈 / 食道伴行 / 膈肌裂孔 / 脊椎水平",
      "flashcard_back": "前、後迷走神經幹伴隨食道經由食道裂孔（T10）穿過膈肌進入腹腔。",
      "flashcard_summary": "迷走神經穿膈 / 食道伴行 / 膈肌裂孔 / 脊椎水平 -> 前、後迷走神經幹伴隨食道經由食道裂孔（T10）穿過膈肌進入腹腔。"
    },
    {
      "question_id": "108-2_medicine-1_006",
      "question_number": 6,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "卵巢動脈的起點、走行與懸韌帶的解剖關係",
      "explanation": "卵巢動脈（ovarian artery）直接起自腹主動脈（abdominal aorta），伴隨靜脈經由卵巢懸韌帶（suspensory ligament of ovary）跨越髂外血管前方進入骨盆腔並進入卵巢。它並非髂內動脈的分支，且不走在卵巢固有韌帶（ovarian ligament）內。因此選項D正確。",
      "flashcard_front": "卵巢動脈起點 / 卵巢懸韌帶 / 腹主動脈分支",
      "flashcard_back": "卵巢動脈直接起自腹主動脈，經由卵巢懸韌帶（骨盆漏斗韌帶）進入卵巢。",
      "flashcard_summary": "卵巢動脈起點 / 卵巢懸韌帶 / 腹主動脈分支 -> 卵巢動脈直接起自腹主動脈，經由卵巢懸韌帶（骨盆漏斗韌帶）進入卵巢。"
    },
    {
      "question_id": "108-2_medicine-1_007",
      "question_number": 7,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "坐骨大孔中穿過梨狀肌上方的血管神經",
      "explanation": "臀上動脈（superior gluteal artery）、臀上靜脈及臀上神經是唯一一組經由梨狀肌上孔（即梨狀肌上方）進入臀部的構造。而臀下動脈（選項B）、坐骨神經（選項C）及陰部神經（選項D）皆經由梨狀肌下孔（梨狀肌下方）穿出。因此選項A正確。",
      "flashcard_front": "梨狀肌上方 / 梨狀肌上孔 / 進入臀部構造 / 臀上血管神經",
      "flashcard_back": "臀上動靜脈及臀上神經穿過梨狀肌上孔；其餘臀下血管、坐骨神經及陰部神經穿過下孔。",
      "flashcard_summary": "梨狀肌上方 / 梨狀肌上孔 / 進入臀部構造 / 臀上血管神經 -> 臀上動靜脈及臀上神經穿過梨狀肌上孔；其餘臀下血管、坐骨神經及陰部神經穿過下孔。"
    },
    {
      "question_id": "108-2_medicine-1_008",
      "question_number": 8,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "腓深神經支配的肌群與垂足的解剖關係",
      "explanation": "腓深神經（deep fibular nerve）支配小腿前側肌群，包括負責足背屈的脛前肌（tibialis anterior），受損時會導致垂足。小腿外側肌群（腓長肌、腓短肌）由腓淺神經支配；小腿後側深肌群（脛後肌）則由脛神經支配。因此選項C正確。",
      "flashcard_front": "腓深神經受損 / 脛前肌無力 / 垂足 / 感覺異常部位",
      "flashcard_back": "腓深神經支配小腿前側肌群（如脛前肌），受損引起足背屈無力（垂足）與第一二趾間感覺麻木。",
      "flashcard_summary": "腓深神經受損 / 脛前肌無力 / 垂足 / 感覺異常部位 -> 腓深神經支配小腿前側肌群（如脛前肌），受損引起足背屈無力（垂足）與第一二趾間感覺麻木。"
    },
    {
      "question_id": "108-2_medicine-1_009",
      "question_number": 9,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "上肢主要神經通過肱骨關節處的解剖路徑",
      "explanation": "尺神經（ulnar nerve）走在肱骨內上髁（medial epicondyle）後方的尺神經溝內，此處位置表淺，容易因撞擊而產生麻痛感。正中神經走在肱骨前內側；橈神經繞行於肱骨後方的橈神經溝但隨後轉至外側。因此正確答案為C。",
      "flashcard_front": "肱骨內上髁後方 / 尺神經溝 / 撞擊麻痛感 / 受損神經",
      "flashcard_back": "尺神經行經肱骨內上髁後方的尺神經溝，此處受損易導致鷹爪手與手尺側麻木。",
      "flashcard_summary": "肱骨內上髁後方 / 尺神經溝 / 撞擊麻痛感 / 受損神經 -> 尺神經行經肱骨內上髁後方的尺神經溝，此處受損易導致鷹爪手與手尺側麻木。"
    },
    {
      "question_id": "108-2_medicine-1_010",
      "question_number": 10,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "肩部腋神經支配的肌肉",
      "explanation": "腋神經（axillary nerve）主要支配三角肌（deltoid muscle）與小圓肌。喙肱肌與肱二頭肌（選項B、C）由肌皮神經支配；肱三頭肌（選項D）由橈神經支配。因此當腋神經受損時，三角肌會無力，故選A。",
      "flashcard_front": "腋神經受損 / 三角肌 / 肩關節外展無力",
      "flashcard_back": "腋神經主要支配三角肌與小圓肌，受損會導致肩外展無力及肩峰處皮膚感覺麻木。",
      "flashcard_summary": "腋神經受損 / 三角肌 / 肩關節外展無力 -> 腋神經主要支配三角肌與小圓肌，受損會導致肩外展無力及肩峰處皮膚感覺麻木。"
    },
    {
      "question_id": "108-2_medicine-1_011",
      "question_number": 11,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "小腦與腦幹連接之小腦腳的傳導路徑",
      "explanation": "齒狀核-紅核-丘腦徑（dentato-rubro-thalamic tract）是小腦的主要輸出路徑，其傳出纖維經由上小腦腳（superior cerebellar peduncle）離開小腦。中小腦腳與下小腦腳則主要包含傳入小腦的纖維。因此選項A正確。",
      "flashcard_front": "齒狀核-紅核-丘腦徑 / 上小腦腳 / 小腦主要傳出纖維",
      "flashcard_back": "齒狀核-紅核-丘腦徑主要經由上小腦腳（superior cerebellar peduncle）傳出離開小腦。",
      "flashcard_summary": "齒狀核-紅核-丘腦徑 / 上小腦腳 / 小腦主要傳出纖維 -> 齒狀核-紅核-丘腦徑主要經由上小腦腳（superior cerebellar peduncle）傳出離開小腦。"
    },
    {
      "question_id": "108-2_medicine-1_012",
      "question_number": 12,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "脊髓白質側束所含的下行運動傳導徑路",
      "explanation": "脊髓白質之外側束（lateral funiculus）含有下行的外側皮質脊髓徑（lateral corticospinal tract），負責支配同側肢體的細緻運動。背柱內側蹄系（選項A）位於後束；前庭脊髓徑與四疊體脊髓徑（選項C、D）主要位於前束。因此選項B正確。",
      "flashcard_front": "脊髓外側束 / 外側皮質脊髓徑 / 下行運動徑路",
      "flashcard_back": "外側皮質脊髓徑走在脊髓白質之外側束，而前庭、四疊體脊髓徑則走在前束。",
      "flashcard_summary": "脊髓外側束 / 外側皮質脊髓徑 / 下行運動徑路 -> 外側皮質脊髓徑走在脊髓白質之外側束，而前庭、四疊體脊髓徑則走在前束。"
    },
    {
      "question_id": "108-2_medicine-1_013",
      "question_number": 13,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "傳導精細觸覺與本體感覺的感覺神經徑路",
      "explanation": "精細觸覺（discriminative touch）、本體感覺（proprioception）及震動覺主要由背柱內側蹄系（dorsal column-medial lemniscus system, DCML）向上傳導。前外側系統（選項D）傳導粗略觸覺與痛溫覺；脊髓小腦徑（選項B）傳導無意識本體感覺。因此選項C正確。",
      "flashcard_front": "精細觸覺 / 震動覺 / 位置覺 / 背柱內側蹄系 / DCML",
      "flashcard_back": "精細觸覺與本體感覺經由背柱內側蹄系（DCML）傳導；痛溫覺由前外側系統（ALS）傳導。",
      "flashcard_summary": "精細觸覺 / 震動覺 / 位置覺 / 背柱內側蹄系 / DCML -> 精細觸覺與本體感覺經由背柱內側蹄系（DCML）傳導；痛溫覺由前外側系統（ALS）傳導。"
    },
    {
      "question_id": "108-2_medicine-1_014",
      "question_number": 14,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "中腦腳間窩穿出的腦神經結構",
      "explanation": "腳間窩（interpeduncular fossa）位於中腦兩側大腦腳之間，為動眼神經（CN III）穿出腦幹的位置。滑車神經（選項A）從中腦背側穿出；基底動脈與腦下垂體則不屬於由此窩穿出的腦神經。因此選項B正確。",
      "flashcard_front": "腳間窩 / 中腦大腦腳之間 / 動眼神經穿出點",
      "flashcard_back": "動眼神經（CN III）經由腳間窩穿出中腦；滑車神經（CN IV）則由中腦背面穿出。",
      "flashcard_summary": "腳間窩 / 中腦大腦腳之間 / 動眼神經穿出點 -> 動眼神經（CN III）經由腳間窩穿出中腦；滑車神經（CN IV）則由中腦背面穿出。"
    },
    {
      "question_id": "108-2_medicine-1_015",
      "question_number": 15,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "初級運動皮質Brodmann area 4的解剖位置與結構",
      "explanation": "Brodmann area 4 代表初級運動皮質（primary motor cortex），位於「前中央迴（precentral gyrus）」，而非後中央迴（後中央迴為初級軀體感覺皮質，Brodmann area 3, 1, 2）。因此選項D敘述錯誤。",
      "flashcard_front": "Brodmann area 4 / 初級運動皮質 / 前中央迴 / 貝茲細胞",
      "flashcard_back": "Brodmann area 4 位於前中央迴，含巨型錐體細胞（貝茲細胞），後中央迴則為感覺皮質。",
      "flashcard_summary": "Brodmann area 4 / 初級運動皮質 / 前中央迴 / 貝茲細胞 -> Brodmann area 4 位於前中央迴，含巨型錐體細胞（貝茲細胞），後中央迴則為感覺皮質。"
    },
    {
      "question_id": "108-2_medicine-1_016",
      "question_number": 16,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "三叉神經下頜支支配的軟腭肌群",
      "explanation": "腭帆張肌（tensor veli palatini）在胚胎發育上與咀嚼肌同源，因此由三叉神經下頜支（V3）支配。其餘軟腭肌群如腭帆提肌（選項B）、腭咽肌（選項C）及腭舌肌（選項D）皆由迷走神經（CN X）所支配。因此選項A正確。",
      "flashcard_front": "腭帆張肌支配 / 三叉神經下頜支 / V3 / 腭部肌群神經支配",
      "flashcard_back": "腭帆張肌由三叉神經下頜支（V3）支配；其餘軟腭肌群（提肌、腭咽肌、腭舌肌）由迷走神經支配。",
      "flashcard_summary": "腭帆張肌支配 / 三叉神經下頜支 / V3 / 腭部肌群神經支配 -> 腭帆張肌由三叉神經下頜支（V3）支配；其餘軟腭肌群（提肌、腭咽肌、腭舌肌）由迷走神經支配。"
    }
  ]
}

# Batch 108-2_medicine-1_batch-002
batch_002 = {
  "dataset_id": "108-2_medicine-1",
  "batch_id": "108-2_medicine-1_batch-002",
  "items": [
    {
      "question_id": "108-2_medicine-1_017",
      "question_number": 17,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "喉部內在肌群的神經支配差異",
      "explanation": "環甲肌（cricothyroid muscle）是唯一由喉上神經外支（external laryngeal nerve）支配的喉部內在肌，負責拉緊聲帶。其他所有喉內在肌（如後環杓肌、外側環杓肌、甲杓肌等）均由喉返神經（recurrent laryngeal nerve）支配。因此選項C正確。",
      "flashcard_front": "環甲肌 / 喉外神經支配 / 喉上神經外支 / 聲帶拉緊",
      "flashcard_back": "環甲肌由喉上神經外支（喉外神經）支配；其餘所有喉內在肌皆由喉返神經支配。",
      "flashcard_summary": "環甲肌 / 喉外神經支配 / 喉上神經外支 / 聲帶拉緊 -> 環甲肌由喉上神經外支（喉外神經）支配；其餘所有喉內在肌皆由喉返神經支配。"
    },
    {
      "question_id": "108-2_medicine-1_018",
      "question_number": 18,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "硬腦膜靜脈竇流入內頸靜脈的直接出口",
      "explanation": "乙狀竇（sigmoid sinus）是硬腦膜靜脈竇系統的末端，穿過頸靜脈孔（jugular foramen）後直接延續並流入內頸靜脈（internal jugular vein）。其餘的橫竇、上岩竇和枕竇均需先匯入乙狀竇，或經其他路徑間接注入。因此選項A正確。",
      "flashcard_front": "乙狀竇 / 頸靜脈孔 / 內頸靜脈直接注入 / 硬腦膜靜脈竇",
      "flashcard_back": "乙狀竇穿過頸靜脈孔後直接注入內頸靜脈；橫竇、岩竇等皆是間接或先匯入乙狀竇。",
      "flashcard_summary": "乙狀竇 / 頸靜脈孔 / 內頸靜脈直接注入 / 硬腦膜靜脈竇 -> 乙狀竇穿過頸靜脈孔後直接注入內頸靜脈；橫竇、岩竇等皆是間接或先匯入乙狀竇。"
    },
    {
      "question_id": "108-2_medicine-1_019",
      "question_number": 19,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "甲狀頸幹分支與鎖骨下動脈分支的區別",
      "explanation": "甲狀頸幹（thyrocervical trunk）是鎖骨下動脈的分支，其主要分支有甲狀腺下動脈（D）、肩胛上動脈（B）和橫頸動脈（C）。深頸動脈（deep cervical artery）則是來自另一個分支——肋頸幹（costocervical trunk）。因此選項A不是甲狀頸幹的分支。",
      "flashcard_front": "甲狀頸幹分支 / 深頸動脈來源 / 肩胛上 / 橫頸 / 甲狀腺下動脈",
      "flashcard_back": "甲狀頸幹分支包括甲狀腺下、肩胛上、橫頸動脈；深頸動脈則是肋頸幹的分支。",
      "flashcard_summary": "甲狀頸幹分支 / 深頸動脈來源 / 肩胛上 / 橫頸 / 甲狀腺下動脈 -> 甲狀頸幹分支包括甲狀腺下、肩胛上、橫頸動脈；深頸動脈則是肋頸幹的分支。"
    },
    {
      "question_id": "108-2_medicine-1_020",
      "question_number": 20,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "柯氏三角內房室結的解剖定位",
      "explanation": "房室結（AV node）位於右心房的柯氏三角（Koch's triangle）內，該三角的邊界包括冠狀竇開口（opening of coronary sinus）、三尖瓣隔瓣附著緣以及Todaro腱，因此房室結最靠近冠狀竇開口。而竇房結靠近界脊（D）上端。因此選項C正確。",
      "flashcard_front": "房室結 / 柯氏三角 / 冠狀竇開口 / 三尖瓣隔瓣",
      "flashcard_back": "房室結位於右心房柯氏三角內，緊鄰冠狀竇開口；竇房結則位在界脊與上腔靜脈交界處。",
      "flashcard_summary": "房室結 / 柯氏三角 / 冠狀竇開口 / 三尖瓣隔瓣 -> 房室結位於右心房柯氏三角內，緊鄰冠狀竇開口；竇房結則位在界脊與上腔靜脈交界處。"
    },
    {
      "question_id": "108-2_medicine-1_021",
      "question_number": 21,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "肺臟淋巴引流的不對稱性與路徑",
      "explanation": "肺部的淋巴引流路徑具有左右不對稱性。左下肺葉的淋巴液主要跨越中線，匯入位於氣管分叉處下方的下氣管支氣管淋巴結（inferior tracheobronchial nodes，又稱隆突下淋巴結），隨後多流向右側。因此選項D敘述正確。",
      "flashcard_front": "左下肺葉淋巴引流 / 下氣管支氣管淋巴結 / 隆突下淋巴結 / 跨越中線",
      "flashcard_back": "左下肺葉的淋巴液常引流至氣管分叉下方的下氣管支氣管淋巴結，進而轉向右側通路。",
      "flashcard_summary": "左下肺葉淋巴引流 / 下氣管支氣管淋巴結 / 隆突下淋巴結 / 跨越中線 -> 左下肺葉的淋巴液常引流至氣管分叉下方的下氣管支氣管淋巴結，進而轉向右側通路。"
    },
    {
      "question_id": "108-2_medicine-1_022",
      "question_number": 22,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "肋間靜脈回流至奇靜脈系統的解剖差異",
      "explanation": "左側第一肋間靜脈（left 1st posterior intercostal vein）通常直接匯入左頭臂靜脈（left brachiocephalic vein），而不匯入奇靜脈系統。而右側第三肋間靜脈、右側第十肋間靜脈及左側第八肋間靜脈皆會回流至奇靜脈系統（直接或經由半奇/副半奇靜脈）。因此選項B正確。",
      "flashcard_front": "左側第一肋間靜脈 / 不入奇靜脈系統 / 左頭臂靜脈回流",
      "flashcard_back": "左側第一肋間靜脈直接回流至左頭臂靜脈，不匯入奇靜脈系統；其餘多數肋間靜脈入奇靜脈系。",
      "flashcard_summary": "左側第一肋間靜脈 / 不入奇靜脈系統 / 左頭臂靜脈回流 -> 左側第一肋間靜脈直接回流至左頭臂靜脈，不匯入奇靜脈系統；其餘多數肋間靜脈入奇靜脈系。"
    },
    {
      "question_id": "108-2_medicine-1_023",
      "question_number": 23,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "胸壁體表標記與胸椎水平面的解剖對應關係",
      "explanation": "在直立解剖姿勢下，劍胸關節（xiphisternal joint）水平面約對應第9胸椎（T9）水平。頸靜脈切跡（A）對應T2-T3之間，胸骨角（B）對應T4-T5椎間盤水平，男性乳頭（D）對應第4肋間。因此選項C正確。",
      "flashcard_front": "劍胸關節水平 / 胸椎對應 / 體表標記 / 胸骨角與乳頭",
      "flashcard_back": "劍胸關節直立時對應 T9 水平；胸骨角對應 T4-T5，頸靜脈切跡對應 T2-T3，乳頭對應第 4 肋間。",
      "flashcard_summary": "劍胸關節水平 / 胸椎對應 / 體表標記 / 胸骨角與乳頭 -> 劍胸關節直立時對應 T9 水平；胸骨角對應 T4-T5，頸靜脈切跡對應 T2-T3，乳頭對應第 4 肋間。"
    },
    {
      "question_id": "108-2_medicine-1_024",
      "question_number": 24,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "心臟各層構造與瓣膜的血液供應來源",
      "explanation": "心外膜（epicardium，即漿膜性心包膜臟層）及心肌層主要由冠狀動脈及其分支供應血流。心內膜（A）表淺，主要藉由心腔內血液擴散獲取氧氣；心包膜外層（B）由心包膈動脈等體循環動脈供應；心瓣膜（D）本身為無血管結構。因此選項C正確。",
      "flashcard_front": "心外膜血管供應 / 冠狀動脈 / 心內膜與心包壁層",
      "flashcard_back": "心外膜與心肌層由冠狀動脈供應；心內膜靠心腔血液擴散，心包壁層靠體循環分支。",
      "flashcard_summary": "心外膜血管供應 / 冠狀動脈 / 心內膜與心包壁層 -> 心外膜與心肌層由冠狀動脈供應；心內膜靠心腔血液擴散，心包壁層靠體循環分支。"
    },
    {
      "question_id": "108-2_medicine-1_025",
      "question_number": 25,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "胃十二指腸動脈來源血管的結紮止血部位",
      "explanation": "十二指腸近幽門處的潰瘍出血（主要源自胃十二指腸動脈及其分支）通常由肝總動脈（common hepatic artery）的分支供應。結紮肝總動脈或其分支可有效止血。而左胃動脈（C）與左胃網膜動脈（D）支配胃大彎與胃小彎左側，下胰十二指腸動脈（B）由腸繫膜上動脈分支，與幽門處出血較無直接關聯。因此選A。",
      "flashcard_front": "十二指腸幽門潰瘍出血 / 胃十二指腸動脈 / 結紮血管 / 肝總動脈",
      "flashcard_back": "幽門旁潰瘍出血來自胃十二指腸動脈，結紮其上游的肝總動脈可有效控制出血。",
      "flashcard_summary": "十二指腸幽門潰瘍出血 / 胃十二指腸動脈 / 結紮血管 / 肝總動脈 -> 幽門旁潰瘍出血來自胃十二指腸動脈，結紮其上游的肝總動脈可有效控制出血。"
    },
    {
      "question_id": "108-2_medicine-1_026",
      "question_number": 26,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "腹股溝管深環的邊界與腹橫筋膜的解剖關係",
      "explanation": "腹股溝管深環（deep inguinal ring）是腹橫筋膜（transversalis fascia）上的卵圓形裂孔。在解剖層次上，腹橫筋膜形成了深環並往外延伸為精索內筋膜，圍繞深環頂部的外側1/3。女性腹股溝管通過子宮圓韌帶而非卵巢韌帶；管內疝氣為間接疝氣。因此選項D正確。",
      "flashcard_front": "腹股溝深環 / 腹橫筋膜裂孔 / 精索內筋膜 / 頂部外側三分之一",
      "flashcard_back": "腹股溝深環是腹橫筋膜上的孔洞，腹橫筋膜並圍成深環頂部的外側 1/3。",
      "flashcard_summary": "腹股溝深環 / 腹橫筋膜裂孔 / 精索內筋膜 / 頂部外側三分之一 -> 腹股溝深環是腹橫筋膜上的孔洞，腹橫筋膜並圍成深環頂部的外側 1/3。"
    },
    {
      "question_id": "108-2_medicine-1_027",
      "question_number": 27,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "射精生理過程中尿道括約肌的反應",
      "explanation": "射精時，外尿道括約肌（external urethral sphincter）必須舒張以容許精液排出，若收縮則會阻礙精液流出。同時，內尿道括約肌會收縮以防止精液逆行射入膀胱；前列腺、輸精管與球尿道腺的平滑肌則會收縮以推進精液。因此選項A「外尿道括約肌收縮」不會發生。",
      "flashcard_front": "射精生理 / 外尿道括約肌 / 內尿道括約肌 / 副性腺收縮",
      "flashcard_back": "射精時外尿道括約肌需舒張，內尿道括約肌收縮（防逆流），前列腺等平滑肌收縮推精。",
      "flashcard_summary": "射精生理 / 外尿道括約肌 / 內尿道括約肌 / 副性腺收縮 -> 射精時外尿道括約肌需舒張，內尿道括約肌收縮（防逆流），前列腺等平滑肌收縮推精。"
    },
    {
      "question_id": "108-2_medicine-1_028",
      "question_number": 28,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "會陰體的肌肉附著與受損後的影響肌群",
      "explanation": "會陰體（perineal body）是會陰中心腱，為球海綿體肌（1）、會陰淺橫肌（3）、會陰深橫肌（2）及肛門外括約肌等的附著處。而坐骨海綿體肌（4，附著於坐骨）及尿道外括約肌（5，環繞尿道膜部）不直接附著於會陰體，其作用最不受其受損影響。因此選D。",
      "flashcard_front": "會陰體附著肌群 / 球海綿體 / 坐骨海綿體 / 尿道外括約肌",
      "flashcard_back": "球海綿體及會陰橫肌附著於會陰體；坐骨海綿體肌與尿道外括約肌不附著於會陰體。",
      "flashcard_summary": "會陰體附著肌群 / 球海綿體 / 坐骨海綿體 / 尿道外括約肌 -> 坐骨海綿體肌與尿道外括約肌不直接附著於會陰體，故受損時不受影響。"
    },
    {
      "question_id": "108-2_medicine-1_029",
      "question_number": 29,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "大腿內收肌群的閉孔神經支配",
      "explanation": "內收長肌（adductor longus）屬於大腿內收肌群，由閉孔神經（obturator nerve）支配。股薄肌（gracilis）亦屬於內收肌群，由相同的閉孔神經支配。恥骨肌（C）主要由股神經支配，股方肌（B）與閉孔內肌（D）則分別由其專屬的神經支配。因此選項A正確。",
      "flashcard_front": "內收長肌 / 閉孔神經支配 / 股薄肌 / 大腿內收肌群",
      "flashcard_back": "內收長肌與股薄肌皆由閉孔神經支配；恥骨肌主由股神經支配，股方肌由其同名神經支配。",
      "flashcard_summary": "內收長肌 / 閉孔神經支配 / 股薄肌 / 大腿內收肌群 -> 內收長肌與股薄肌皆由閉孔神經支配；恥骨肌主由股神經支配，股方肌由其同名神經支配。"
    },
    {
      "question_id": "108-2_medicine-1_030",
      "question_number": 30,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "通過腕隧道的肌腱結構",
      "explanation": "腕隧道（carpal tunnel）內含有正中神經及9條肌腱，其中包含1條屈拇指長肌腱（flexor pollicis longus tendon）。而伸拇指長肌腱（A）、外展拇指長肌腱（C）及內收拇指肌（D）皆不通過腕隧道，因此在腕隧道症候群時不受直接壓迫。因此選項B正確。",
      "flashcard_front": "腕隧道內容物 / 屈拇指長肌 / 正中神經 / 伸肌腱與外展肌",
      "flashcard_back": "屈拇指長肌腱與8條屈指肌腱及正中神經通過腕隧道；伸肌與內收肌腱不通過。",
      "flashcard_summary": "腕隧道內容物 / 屈拇指長肌 / 正中神經 / 伸肌腱與外展肌 -> 屈拇指長肌腱與8條屈指肌腱及正中神經通過腕隧道；伸肌與內收肌腱不通過。"
    },
    {
      "question_id": "108-2_medicine-1_031",
      "question_number": 31,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "背部與後頸部深層肌群的解剖分層",
      "explanation": "大後頭直肌（rectus capitis posterior major）屬於枕下肌群（suboccipital muscles），位於後頸部最深層，緊貼環枕關節。而頭夾肌（A）、頭最長肌（B）及頭半棘肌（C）的解剖層次皆較大後頭直肌表淺。因此選項D正確。",
      "flashcard_front": "後頸最深層肌肉 / 枕下肌群 / 大後頭直肌 / 半棘肌與夾肌",
      "flashcard_back": "大後頭直肌屬於最深層的枕下肌群，頭夾肌、最長肌與半棘肌的位置皆較其表淺。",
      "flashcard_summary": "後頸最深層肌肉 / 枕下肌群 / 大後頭直肌 / 半棘肌與夾肌 -> 大後頭直肌屬於最深層的枕下肌群，頭夾肌、最長肌與半棘肌的位置皆較其表淺。"
    }
  ]
}

# Batch 108-2_medicine-1_batch-003
batch_003 = {
  "dataset_id": "108-2_medicine-1",
  "batch_id": "108-2_medicine-1_batch-003",
  "items": [
    {
      "question_id": "108-2_medicine-1_032",
      "question_number": 32,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "胚胎及發育生物學",
      "category_confidence": "high",
      "key_point": "精子發生過程中第一次減數分裂的產物",
      "explanation": "在精子發生（spermatogenesis）中，雙倍體的初級精母細胞（primary spermatocyte）完成第一次減數分裂（meiosis I）後，會產生兩個單倍體的次級精母細胞（secondary spermatocyte）。次級精母細胞完成第二次減數分裂後則產生精細胞（spermatid）。因此選項C正確。",
      "flashcard_front": "第一次減數分裂產物 / 精子生成 / 初級精母細胞 / 次級精母細胞",
      "flashcard_back": "初級精母細胞進行 Meiosis I 產生次級精母細胞；次級精母細胞進行 Meiosis II 產生精細胞。",
      "flashcard_summary": "第一次減數分裂產物 / 精子生成 / 初級精母細胞 / 次級精母細胞 -> 初級精母細胞進行 Meiosis I 產生次級精母細胞；次級精母細胞進行 Meiosis II 產生精細胞。"
    },
    {
      "question_id": "108-2_medicine-1_033",
      "question_number": 33,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "胚胎及發育生物學",
      "category_confidence": "high",
      "key_point": "橫膈胚胎發育的四個來源構造",
      "explanation": "橫膈的發育來源包括橫中隔（A）、胸腹膜（B）、食道背側繫膜（C）以及體壁的外側向內生長。胸心包膜（pleuropericardial membrane，D）與縱膈及心包腔的形成有關，與橫膈組成無關。因此選項D正確。",
      "flashcard_front": "橫膈胚胎來源 / 橫中隔 / 胸腹膜 / 胸心包膜無關",
      "flashcard_back": "橫膈來自橫中隔、胸腹膜、食道背繫膜與體壁；胸心包膜與心包膜及縱膈有關，與橫膈無關。",
      "flashcard_summary": "橫膈胚胎來源 / 橫中隔 / 胸腹膜 / 胸心包膜無關 -> 橫膈來自橫中隔、胸腹膜、食道背繫膜與體壁；胸心包膜與心包膜及縱膈有關，與橫膈無關。"
    },
    {
      "question_id": "108-2_medicine-1_034",
      "question_number": 34,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "胚胎及發育生物學",
      "category_confidence": "high",
      "key_point": "十二指腸胚胎發育的上皮變化與旋轉",
      "explanation": "十二指腸在發育第5至6週時，因上皮細胞快速增生而暫時閉鎖（obliteration），隨後經由再通作用（recanalization）於第8週重新打通。其前半段源自前腸，後半段源自中腸；旋轉時十二指腸環會轉向右側，而非左側。因此選項D正確。",
      "flashcard_front": "十二指腸發育 / 上皮增生閉鎖 / 再通作用 / 旋轉至右側",
      "flashcard_back": "十二指腸在第5-6週因上皮增生暫時閉鎖，第8週再通打通；胃旋轉時將十二指腸推向右側。",
      "flashcard_summary": "十二指腸發育 / 上皮增生閉鎖 / 再通作用 / 旋轉至右側 -> 十二指腸在第5-6週因上皮增生暫時閉鎖，第8週再通打通；胃旋轉時將十二指腸推向右側。"
    },
    {
      "question_id": "108-2_medicine-1_035",
      "question_number": 35,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "胚胎及發育生物學",
      "category_confidence": "high",
      "key_point": "性腺分化中原始性腺索的發育歸宿",
      "explanation": "在男性胚胎發育中，原始性腺索（gonadal cords）會向髓質延伸發育成細精管（seminiferous tubules）。在女性中，原始性腺索退化，由皮質索（cortical cords）發育成原始濾泡的濾泡細胞；副睪與輸卵管則分別發育自中腎管與旁中腎管。因此選項C正確。",
      "flashcard_front": "原始性腺索 / 細精管發育 / 髓質 / 男性性腺分化",
      "flashcard_back": "男性中原始性腺索（gonadal cords）發育成細精管；女性中原始性腺索退化，由皮質索發育濾泡。",
      "flashcard_summary": "原始性腺索 / 細精管發育 / 髓質 / 男性性腺分化 -> 男性中原始性腺索（gonadal cords）發育成細精管；女性中原始性腺索退化，由皮質索發育濾泡。"
    },
    {
      "question_id": "108-2_medicine-1_036",
      "question_number": 36,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "胚胎及發育生物學",
      "category_confidence": "high",
      "key_point": "眼睛與視網膜血管發育來源",
      "explanation": "視網膜中央動靜脈是源自玻璃體血管（hyaloid vessels）的「近側端（proximal part）」，其遠側端在發育過程中退化消失。眼裂位於眼杯腹側面，視網膜色素上皮來自眼杯外層，視神經由視網膜神經節細胞軸突構成，這些敘述皆正確。因此選項B錯誤。",
      "flashcard_front": "視網膜中央血管 / 玻璃體血管 / 近側端與遠側端 / 眼睛發育",
      "flashcard_back": "視網膜中央血管衍生自玻璃體血管的近側端，玻璃體血管遠側端在出生前退化。",
      "flashcard_summary": "視網膜中央血管 / 玻璃體血管 / 近側端與遠側端 / 眼睛發育 -> 視網膜中央血管衍生自玻璃體血管的近側端，玻璃體血管遠側端在出生前退化。"
    },
    {
      "question_id": "108-2_medicine-1_037",
      "question_number": 37,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "組織學",
      "category_confidence": "high",
      "key_point": "平滑肌細胞的超微結構與外板特徵",
      "explanation": "平滑肌細胞外部被一層基底膜樣的結構，即外板（external lamina）所包圍。緻密體（dense body）主要供肌動蛋白絲（細肌絲）附著；平滑肌細胞無T小管，而是由小凹（caveolae）傳遞信號；細胞間連接主要為間隙連結（gap junction）而非橋粒。因此選項B正確。",
      "flashcard_front": "平滑肌超微結構 / 外板 / 緻密體附著 / 小凹傳遞",
      "flashcard_back": "平滑肌細胞外包覆外板；緻密體為細肌絲（Actin）附著點，無T管，藉小凹與間隙連結起作用。",
      "flashcard_summary": "平滑肌超微結構 / 外板 / 緻密體附著 / 小凹傳遞 -> 平滑肌細胞外包覆外板；緻密體為細肌絲（Actin）附著點，無T管，藉小凹與間隙連結起作用。"
    },
    {
      "question_id": "108-2_medicine-1_038",
      "question_number": 38,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "組織學",
      "category_confidence": "high",
      "key_point": "細胞接合處與細胞骨架絲的連結關係",
      "explanation": "黏著斑（macula adherens，即橋粒 desmosome）是細胞與細胞間的接合構造，其板狀結構與細胞內的中間絲（intermediate filaments）相連結。閉鎖小帶（A）、黏著小帶（B）與局部黏著（D）則是與微絲（actin filaments）相連結。因此選項C正確。",
      "flashcard_front": "中間絲連結 / 黏著斑 / 橋粒 / 閉鎖小帶與黏著小帶微絲",
      "flashcard_back": "黏著斑（橋粒）與半橋粒連結中間絲；閉鎖小帶與黏著小帶則連結微絲（Actin）。",
      "flashcard_summary": "中間絲連結 / 黏著斑 / 橋粒 / 閉鎖小帶與黏著小帶微絲 -> 黏著斑（橋粒）與半橋粒連結中間絲；閉鎖小帶與黏著小帶則連結微絲（Actin）。"
    },
    {
      "question_id": "108-2_medicine-1_039",
      "question_number": 39,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "組織學",
      "category_confidence": "high",
      "key_point": "長骨軟骨內骨化的初級骨化中心位置",
      "explanation": "在長骨的軟骨內骨化（endochondral ossification）中，初級骨化中心（primary ossification center）位於骨幹（diaphysis），主要負責骨幹的骨化；次級骨化中心則位於骨骺（epiphysis）。因此選項A正確。",
      "flashcard_front": "軟骨內骨化 / 初級骨化中心 / 骨幹 / 次級骨化中心骨骺",
      "flashcard_back": "長骨軟骨內骨化的初級骨化中心位於骨幹；次級骨化中心則位於骨骺。",
      "flashcard_summary": "軟骨內骨化 / 初級骨化中心 / 骨幹 / 次級骨化中心骨骺 -> 長骨軟骨內骨化的初級骨化中心位於骨幹；次級骨化中心則位於骨骺。"
    },
    {
      "question_id": "108-2_medicine-1_040",
      "question_number": 40,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "組織學",
      "category_confidence": "high",
      "key_point": "中樞與周邊神經系統形成髓鞘之膠細胞對應",
      "explanation": "中樞神經系統中的寡突膠細胞（oligodendrocyte）負責形成髓鞘，其功能與周邊神經系統中的許旺細胞（Schwann cell）類似。室管膜細胞分布於腦室與中央管；星狀膠細胞在灰質最多且分支與血管相接；微小膠細胞具吞噬功能。因此選項A正確。",
      "flashcard_front": "中樞髓鞘形成 / 寡突膠細胞 / 許旺細胞對應 / 星狀與室管膜",
      "flashcard_back": "中樞神經由寡突膠細胞形成髓鞘；周邊由許旺細胞形成。室管膜細胞覆蓋腦室腔面。",
      "flashcard_summary": "中樞髓鞘形成 / 寡突膠細胞 / 許旺細胞對應 / 星狀與室管膜 -> 中樞神經由寡突膠細胞形成髓鞘；周邊由許旺細胞形成。室管膜細胞覆蓋腦室腔面。"
    },
    {
      "question_id": "108-2_medicine-1_041",
      "question_number": 41,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "組織學",
      "category_confidence": "high",
      "key_point": "氣管與支氣管管壁結構彈性纖維與平滑肌的特徵",
      "explanation": "氣管與支氣管的管壁皆含有彈性纖維（elastic fibers）以提供肺部呼吸時的彈性。氣管與支氣管的上皮高度不同（氣管為高假複層，支氣管漸變矮），氣管含有透明軟骨而非纖維軟骨，且兩者皆含有平滑肌細胞。因此選項A正確。",
      "flashcard_front": "氣管與支氣管 / 彈性纖維 / 軟骨與平滑肌 / 上皮高度比較",
      "flashcard_back": "氣管與支氣管皆富含彈性纖維與平滑肌；氣管上皮較高，且含C型透明軟骨環而非纖維軟骨。",
      "flashcard_summary": "氣管與支氣管 / 彈性纖維 / 軟骨與平滑肌 / 上皮高度比較 -> 氣管與支氣管皆富含彈性纖維與平滑肌；氣管上皮較高，且含C型透明軟骨環而非纖維軟骨。"
    },
    {
      "question_id": "108-2_medicine-1_042",
      "question_number": 42,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "組織學",
      "category_confidence": "high",
      "key_point": "胰臟內分泌部蘭氏小島的組織學特徵",
      "explanation": "胰臟的內分泌部是由蘭氏小島（islets of Langerhans）所組成，負責分泌激素。胰臟的外分泌部則是由漿液性腺細胞、泡心細胞組成，內含豐富的嗜酸性酶原顆粒。因此選項B正確。",
      "flashcard_front": "胰臟內分泌 / 蘭氏小島 / 泡心細胞與漿液腺 / 酶原顆粒",
      "flashcard_back": "蘭氏小島為胰臟內分泌部；泡心細胞、漿液性腺泡與酶原顆粒皆屬於胰臟外分泌部結構。",
      "flashcard_summary": "胰臟內分泌 / 蘭氏小島 / 泡心細胞與漿液腺 / 酶原顆粒 -> 蘭氏小島為胰臟內分泌部；泡心細胞、漿液性腺泡與酶原顆粒皆屬於胰臟外分泌部結構。"
    },
    {
      "question_id": "108-2_medicine-1_043",
      "question_number": 43,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "組織學",
      "category_confidence": "high",
      "key_point": "培亞氏斑在小腸黏膜下層的組織學分佈",
      "explanation": "培亞氏斑（Peyer's patches）是聚集的淋巴濾泡，是小腸中迴腸（ileum）的特徵性組織學結構，主要分佈於迴腸的黏膜下層中。因此選項C正確。",
      "flashcard_front": "培亞氏斑 / 迴腸特徵 / Peyer's patches / 小腸淋巴組織",
      "flashcard_back": "培亞氏斑（聚集淋巴濾泡）為小腸中迴腸（ileum）黏膜下層的代表性特徵構造。",
      "flashcard_summary": "培亞氏斑 / 迴腸特徵 / Peyer's patches / 小腸淋巴組織 -> 培亞氏斑（聚集淋巴濾泡）為小腸中迴腸（ileum）黏膜下層的代表性特徵構造。"
    },
    {
      "question_id": "108-2_medicine-1_044",
      "question_number": 44,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "組織學",
      "category_confidence": "high",
      "key_point": "緻密斑的組織起源與位置",
      "explanation": "緻密斑（macula densa）是由「遠直小管（distal straight tubule）」（或稱遠曲小管起始段）的上皮細胞特化而成，而非近直小管。腎絲球內皮為穿孔型，近腎絲球細胞由入球小動脈平滑肌特化，弓形動脈位於皮髓質交界，這些皆正確。因此選項B錯誤。",
      "flashcard_front": "緻密斑起源 / 遠直小管特化 / 近腎絲球細胞 / 穿孔型內皮",
      "flashcard_back": "緻密斑是由遠直小管的上皮特化而成，而非近直小管；近腎絲球細胞由入球小動脈平滑肌特化。",
      "flashcard_summary": "緻密斑起源 / 遠直小管特化 / 近腎絲球細胞 / 穿孔型內皮 -> 緻密斑是由遠直小管的上皮特化而成，而非近直小管；近腎絲球細胞由入球小動脈平滑肌特化。"
    },
    {
      "question_id": "108-2_medicine-1_045",
      "question_number": 45,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "組織學",
      "category_confidence": "high",
      "key_point": "子宮肌層在懷孕期間的平滑肌細胞生理變化",
      "explanation": "在懷孕期間，子宮肌層（myometrium）的平滑肌細胞會發生肥大（hypertrophy，細胞體積增大）與增生（hyperplasia，細胞數量增加），以適應胎兒發育。子宮內膜及肌層皆隨月經週期改變；子宮體平滑肌含量遠多於子宮頸。因此選項C正確。",
      "flashcard_front": "懷孕子宮肌層 / 平滑肌肥大與增生 / 子宮體與子宮頸平滑肌",
      "flashcard_back": "懷孕時子宮肌層平滑肌細胞同時發生肥大與增生；子宮體平滑肌含量多於子宮頸（主為結締組織）。",
      "flashcard_summary": "懷孕子宮肌層 / 平滑肌肥大與增生 / 子宮體與子宮頸平滑肌 -> 懷孕時子宮肌層平滑肌細胞同時發生肥大與增生；子宮體平滑肌含量多於子宮頸（主為結締組織）。"
    },
    {
      "question_id": "108-2_medicine-1_046",
      "question_number": 46,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "組織學",
      "category_confidence": "high",
      "key_point": "細精管生精上皮的組織學特徵與分層",
      "explanation": "細精管的生精上皮屬於複合型複層上皮（complex stratified epithelium），由支持細胞及各階段生精細胞組成。支持細胞位於管壁內部；管壁外的間質細胞負責分泌睪固酮而非類肌細胞；成熟的精細胞位於管腔靠近中心處而非基底部。因此選項C正確。",
      "flashcard_front": "細精管上皮 / 複合型複層上皮 / 生質細胞 / 支持細胞與間質細胞",
      "flashcard_back": "細精管上皮為複合型複層上皮；支持細胞在管壁內，分泌睪固酮的間質細胞位於管腔外。",
      "flashcard_summary": "細精管上皮 / 複合型複層上皮 / 生質細胞 / 支持細胞與間質細胞 -> 細精管上皮為複合型複層上皮；支持細胞在管壁內，分泌睪固酮的間質細胞位於管腔外。"
    }
  ]
}

# Write files
with open("reports/gemini_outputs/108-1_medicine-6_batch-005.json", "w", encoding="utf-8") as f:
    json.dump(batch_005, f, ensure_ascii=False, indent=2)

with open("reports/gemini_outputs/108-1_medicine-6_batch-006.json", "w", encoding="utf-8") as f:
    json.dump(batch_006, f, ensure_ascii=False, indent=2)

with open("reports/gemini_outputs/108-2_medicine-1_batch-001.json", "w", encoding="utf-8") as f:
    json.dump(batch_001, f, ensure_ascii=False, indent=2)

with open("reports/gemini_outputs/108-2_medicine-1_batch-002.json", "w", encoding="utf-8") as f:
    json.dump(batch_002, f, ensure_ascii=False, indent=2)

with open("reports/gemini_outputs/108-2_medicine-1_batch-003.json", "w", encoding="utf-8") as f:
    json.dump(batch_003, f, ensure_ascii=False, indent=2)

print("All batch output files written successfully.")
