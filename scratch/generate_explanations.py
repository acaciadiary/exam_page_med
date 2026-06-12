import json
from pathlib import Path

# Create reports/gemini_outputs if it doesn't exist
Path("reports/gemini_outputs").mkdir(parents=True, exist_ok=True)

batch_data = {}

# =====================================================================
# 108-1_medicine-2_batch-003
# =====================================================================
batch_data["108-1_medicine-2_batch-003"] = {
    "dataset_id": "108-1_medicine-2",
    "batch_id": "108-1_medicine-2_batch-003",
    "items": [
        {
            "question_id": "108-1_medicine-2_031",
            "question_number": 31,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "衛氏肺吸蟲感染的臨床與實驗室特徵。",
            "explanation": "患者食用浸酒毛蟹（醉蟹）為重要病史，出現咳嗽、血痰，且痰液中發現深褐色蟲卵與卡格里登結晶（Charcot-Leyden crystals），胸部X光有斑狀浸潤與囊體，並伴隨嗜酸性球增多，皆是衛氏肺吸蟲感染的典型表現。異形吸蟲與薑片蟲為腸道吸蟲，不會引起肺部症狀；日本血吸蟲主要侵犯肝門靜脈系統。",
            "flashcard_front": "醉蟹食用史 / 帶血絲濃痰 / 深褐色蟲卵 / Charcot-Leyden crystals",
            "flashcard_back": "應診斷為衛氏肺吸蟲感染。該寄生蟲以蟹類為第二中間宿主，侵犯肺部會導致血痰與嗜酸性球增多。",
            "flashcard_summary": "醉蟹食用史 / 帶血絲濃痰 / 深褐色蟲卵 / Charcot-Leyden crystals -> 衛氏肺吸蟲感染"
        },
        {
            "question_id": "108-1_medicine-2_032",
            "question_number": 32,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "豬囊尾幼蟲症的傳播途徑與臨床特徵。",
            "explanation": "人罹患豬囊尾幼蟲症（cysticercosis）是因為「食入豬肉絛蟲的蟲卵（eggs）」，而非食入未熟帶蟲豬肉。食入未熟帶有囊尾幼蟲的豬肉，人會得到豬肉絛蟲的成蟲寄生（絛蟲病）。囊蟲可侵犯肌肉與內臟器官，若侵犯腦部（腦囊蟲症）常引發癲癇，血清抗體檢查有助於診斷。",
            "flashcard_front": "豬囊尾幼蟲症 / 傳播途徑 / 腦部病變與癲癇",
            "flashcard_back": "人罹患此症是因食入「豬肉絛蟲蟲卵」而非囊尾幼蟲。食入含囊尾幼蟲的未熟豬肉會導致腸道成蟲感染。",
            "flashcard_summary": "豬囊尾幼蟲症 / 傳播途徑 -> 食入豬肉絛蟲蟲卵致病，而非食入未熟豬肉中的囊尾幼蟲"
        },
        {
            "question_id": "108-1_medicine-2_033",
            "question_number": 33,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "三日瘧與卵形瘧原蟲的形態鑑定與臨床特色。",
            "explanation": "帶狀型滋養體（band form trophozoites）是三日瘧原蟲（Plasmodium malariae）的特徵，而非卵形瘧原蟲（Plasmodium ovale）。瘧疾發作過程確實依序為惡寒、發燒、發汗。三日瘧原蟲偏好侵入成熟紅血球，而六個月以下嬰兒常因母體抗體保護而甚少患瘧疾。",
            "flashcard_front": "帶狀型滋養體 / 瘧原蟲鑑定 / 瘧疾發作三階段",
            "flashcard_back": "帶狀型滋養體為「三日瘧原蟲」之特徵。瘧疾典型發作依序為惡寒、發燒、發汗。",
            "flashcard_summary": "帶狀型滋養體 -> 三日瘧原蟲的特徵，而非卵形瘧原蟲"
        },
        {
            "question_id": "108-1_medicine-2_034",
            "question_number": 34,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "阿米巴原蟲的形態特徵與流行病學高危險群。",
            "explanation": "痢疾阿米巴主要經由糞口途徑傳播，群聚機構（如啟智、精神教養院）與男同性戀者（經由性行為糞口接觸）為其感染高危險群。嗜碘阿米巴的大肝醣泡主要存在於「囊體（cyst）」而非滋養體；哈氏阿米巴不吞噬紅血球；類染色體成分為核糖體核酸（RNA）而非DNA。",
            "flashcard_front": "痢疾阿米巴高危群 / 嗜碘阿米巴肝醣泡 / 類染色體成分",
            "flashcard_back": "男同性戀與教養院生為痢疾阿米巴高危群。大肝醣泡存在於嗜碘阿米巴「囊體」；類染色體成分為RNA。",
            "flashcard_summary": "痢疾阿米巴高危群 / 其它阿米巴特徵 -> 院生及男同志為高危群；類染色體為RNA；肝醣泡位於嗜碘阿米巴囊體"
        },
        {
            "question_id": "108-1_medicine-2_035",
            "question_number": 35,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "蠅蛆症的傳播媒介與地理分佈。",
            "explanation": "人膚蠅（Dermatobia hominis）主要分布於中南美洲地區，並非亞洲地區。人膚蠅產卵於吸血昆蟲腹部，藉其吸血時孵化幼蟲鑽入宿主皮膚；院內蠅蛆症常發生於有開放性傷口的長期臥床者；耳部感染常伴隨爬動感與惡臭分泌物。",
            "flashcard_front": "人膚蠅 / 蠅蛆症 / 地理分佈 / 傳播方式",
            "flashcard_back": "人膚蠅蠅蛆症主要發生於「中南美洲」而非亞洲。其利用吸血昆蟲攜帶蟲卵傳播。",
            "flashcard_summary": "人膚蠅地理分佈 -> 主要分布於中南美洲，而非亞洲"
        },
        {
            "question_id": "108-1_medicine-2_036",
            "question_number": 36,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "生物統計中測量尺度的分類與判斷。",
            "explanation": "膽固醇值（mg/100 ml）具有絕對零度，數值之間的比例有意義，屬於等比尺度（ratio scale）。血型為名目尺度（nominal scale）；體溫（攝氏）為等距尺度（interval scale，無絕對零度）；癌症分期為序位尺度（ordinal scale，有順序但無固定間距）。",
            "flashcard_front": "血型 / 膽固醇值 / 攝氏體溫 / 癌症分期 / 測量尺度",
            "flashcard_back": "膽固醇值為等比尺度；血型為名目尺度；體溫為等距尺度；癌症分期為序位尺度。",
            "flashcard_summary": "血型、膽固醇、體溫、癌症分期的測量尺度 -> 依序為名目、等比、等距、序位尺度"
        },
        {
            "question_id": "108-1_medicine-2_037",
            "question_number": 37,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "臺灣法定傳染病分類與通報時效。",
            "explanation": "狂犬病在臺灣傳染病分類中屬於第一類法定傳染病，必須於24小時內立即通報。瘧疾為第二類；日本腦炎與梅毒則屬於第三類法定傳染病，通報時限不同。",
            "flashcard_front": "狂犬病 / 日本腦炎 / 瘧疾 / 梅毒 / 通報分級",
            "flashcard_back": "狂犬病屬於第一類法定傳染病（需立即通報）。瘧疾為第二類；日本腦炎與梅毒為第三類。",
            "flashcard_summary": "狂犬病通報分級 -> 臺灣第一類法定傳染病，須立即通報"
        },
        {
            "question_id": "108-1_medicine-2_038",
            "question_number": 38,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "假設檢定中型一錯誤與型二錯誤的定義與關係。",
            "explanation": "型一錯誤機率（alpha）與型二錯誤機率（beta）之間沒有相加為1的關係。型一錯誤是指對立假設為假卻拒絕虛無假設（誤判有差異）的機率，即顯著水準；型二錯誤是當對立假設為真卻接受虛無假設的機率。若顯著水準不變，欲增加統計檢定力（1-beta），可透過增加樣本數來達成。",
            "flashcard_front": "型一錯誤 / 型二錯誤 / 顯著水準 / 統計檢定力",
            "flashcard_back": "型一錯誤（α）與型二錯誤（β）之和不等於1。增加樣本數可在α不變下降低β、提升檢定力。",
            "flashcard_summary": "型一錯誤與型二錯誤的關係 -> 兩者機率相加不等於1；增加樣本數可提升檢定力"
        },
        {
            "question_id": "108-1_medicine-2_039",
            "question_number": 39,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "篩檢試驗中平行檢定對敏感度與特異度的影響。",
            "explanation": "平行檢定（Simultaneous Testing）是指多項篩檢同時進行，只要其中任一項為陽性即判定為陽性。這種方式會使淨敏感度（Net sensitivity）增加，但淨特異度（Net specificity）會減少，偽陽性率也隨之增加。官方標準答案為A，強調淨敏感度的增加。",
            "flashcard_front": "平行檢定 / 淨敏感度 / 淨特異度 / 篩檢效度",
            "flashcard_back": "平行檢定只要任一陽性即算陽性，會增加「淨敏感度」，但會降低「淨特異度」。",
            "flashcard_summary": "平行檢定對篩檢效度之影響 -> 淨敏感度增加，淨特異度減少"
        },
        {
            "question_id": "108-1_medicine-2_040",
            "question_number": 40,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "多組連續型變數均值比較的統計方法選擇。",
            "explanation": "本研究欲比較五種不同吸菸狀況組別（三組以上獨立樣本）的肺功能平均值（連續型變數）是否不同，最適當的統計方法為單因子變異數分析（One-way ANOVA）。獨立t檢定僅適用於兩組獨立樣本比較；配對t檢定適用於兩組相關或配對樣本；卡方檢定適用於類別型變數的關聯性分析。",
            "flashcard_front": "五組吸菸狀況 / 肺功能平均值比較 / 統計方法選擇",
            "flashcard_back": "比較三組以上獨立樣本之平均值，應選用「單因子變異數分析（One-way ANOVA）」。",
            "flashcard_summary": "三組以上獨立樣本平均值比較 -> 使用單因子變異數分析"
        },
        {
            "question_id": "108-1_medicine-2_041",
            "question_number": 41,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "流行病學研究設計中生態學研究的定義。",
            "explanation": "該研究使用環保署的鄉鎮空氣污染資料與衛福部的癌症發生資料，缺乏個人生活相關資料，是以「群體（鄉鎮市區）」而非個人為分析單位，此研究設計屬於生態學研究（ecological study）。生態學研究易產生「生態謬誤（ecological fallacy）」，即群體關係不能直接推論至個人層面。",
            "flashcard_front": "鄉鎮市區資料 / 無個人生活資料 / 空氣污染與癌症 / 研究設計",
            "flashcard_back": "以群體為分析單位、缺乏個人層面暴露與疾病資料的研究，屬於「生態學研究」。",
            "flashcard_summary": "以群體為分析單位的研究設計 -> 生態學研究（ecological study）"
        },
        {
            "question_id": "108-1_medicine-2_042",
            "question_number": 42,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "造成酸雨的主要大氣污染物成分。",
            "explanation": "造成酸雨效應的主要空氣污染物為硫氧化物（SOx，如二氧化硫）與氮氧化物（NOx），它們在大氣中溶於水會形成硫酸與硝酸。一氧化碳與臭氧不會直接參與形成酸雨的化學反應。",
            "flashcard_front": "酸雨效應 / 空氣污染物 / 硫酸與硝酸來源",
            "flashcard_back": "造成酸雨的主要污染物是「硫氧化物（SOx）」與「氮氧化物（NOx）」。",
            "flashcard_summary": "酸雨主要污染物 -> 硫氧化物與氮氧化物"
        },
        {
            "question_id": "108-1_medicine-2_043",
            "question_number": 43,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "非致癌物風險評估的核心假設與方法。",
            "explanation": "非致癌物質的風險評估核心假設為「劑量反應具有閾值存在」，即在低於某一閾值（如參考劑量 RfD）時不會引起毒性反應。致癌物評估通常假設無閾值，並使用斜率因子（slope factor）計算多餘癌症風險，以10-6作為可接受風險的基準線。",
            "flashcard_front": "非致癌物 / 風險評估 / 閾值假設 / 斜率因子與10-6",
            "flashcard_back": "非致癌物評估核心為「劑量反應具有閾值」；而斜率因子與10-6基準線用於致癌物評估。",
            "flashcard_summary": "非致癌物風險評估特徵 -> 劑量反應假設具有閾值存在"
        },
        {
            "question_id": "108-1_medicine-2_044",
            "question_number": 44,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "臺灣登革熱的病媒蚊種類。",
            "explanation": "臺灣傳播登革熱的病媒蚊主要為埃及斑蚊（Aedes aegypti）與白線斑蚊（Aedes albopictus）。熱帶家蚊傳播絲蟲病與日本腦炎；中華瘧蚊傳播瘧疾；小黑蚊（台灣鋏蠓）為吸血昆蟲但非登革熱病媒。",
            "flashcard_front": "登革熱 / 臺灣病媒蚊種類 / 主要傳播媒介",
            "flashcard_back": "臺灣登革熱的病媒蚊為「埃及斑蚊」與「白線斑蚊」。",
            "flashcard_summary": "登革熱病媒蚊 -> 埃及斑蚊、白線斑蚊"
        },
        {
            "question_id": "108-1_medicine-2_045",
            "question_number": 45,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "職業衛生中時量平均暴露濃度（TWA）的計算。",
            "explanation": "時量平均暴露濃度（TWA）計算公式為每次暴露濃度乘以暴露時間的總和，再除以總工作時間（8小時）。本題中，每小時前10分鐘暴露60 ppm，後50分鐘暴露0 ppm，因此每小時的平均暴露量為 (60 ppm * 10 min + 0 ppm * 50 min) / 60 min = 10 ppm。由於每小時循環相同，8小時的時量平均暴露濃度即為10 ppm。",
            "flashcard_front": "時量平均暴露濃度 (TWA) / 8小時 / 10分鐘暴露60 ppm / 50分鐘無暴露",
            "flashcard_back": "TWA為暴露時間加權平均。計算為：(60 ppm * 10 min / 60 min) = 10 ppm。",
            "flashcard_summary": "TWA計算 -> 依時間加權平均計算，每小時暴露10分鐘60ppm的TWA為 10 ppm"
        }
    ]
}

# =====================================================================
# 108-1_medicine-2_batch-004
# =====================================================================
batch_data["108-1_medicine-2_batch-004"] = {
    "dataset_id": "108-1_medicine-2",
    "batch_id": "108-1_medicine-2_batch-004",
    "items": [
        {
            "question_id": "108-1_medicine-2_046",
            "question_number": 46,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "有機溶劑苯暴露與職業性癌症的關聯。",
            "explanation": "長期職業暴露於有機溶劑苯（benzene），會對骨髓造血系統產生嚴重毒性，最容易誘發白血病（Leukemia，血癌）。石綿暴露與間皮瘤及肺癌相關；氯乙烯與肝血管肉瘤相關；芳香胺（如聯苯胺）與膀胱癌相關。",
            "flashcard_front": "苯暴露 / 職業病 / 骨髓造血系統毒性 / 易誘發癌症",
            "flashcard_back": "長期暴露於苯（benzene）最容易導致「血癌（白血病）」。",
            "flashcard_summary": "苯暴露 -> 易誘發血癌（白血病）"
        },
        {
            "question_id": "108-1_medicine-2_047",
            "question_number": 47,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "臺灣成人肥胖的身體質量指數（BMI）切點定義。",
            "explanation": "依據我國衛生福利部國民健康署之定義，成人肥胖（Obesity）的身體質量指數（BMI）切點為大於或等於 27 kg/m²。BMI介於18.5至24為正常範圍；24至27為過重；27至30為輕度肥胖；30至35為中度肥胖；35以上為重度肥胖。",
            "flashcard_front": "臺灣成人肥胖定義 / 身體質量指數 (BMI) / 衛福部切點",
            "flashcard_back": "我國成人肥胖的BMI判定標準切點為「大於或等於27」。",
            "flashcard_summary": "臺灣成人肥胖BMI切點 -> 大於或等於 27 kg/m²"
        },
        {
            "question_id": "108-1_medicine-2_048",
            "question_number": 48,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "健康信念模式在預防性醫療行為上的應用。",
            "explanation": "健康信念模式（Health Belief Model, HBM）最適合用來解釋個體對於預防性健康行為（如癌症篩檢）的採行意願。此模式強調自覺罹患性、自覺嚴重性、自覺行動利益、自覺行動障礙及行動線索等因子對行為決策的影響。",
            "flashcard_front": "預防性健康行為 / 癌症篩檢採行意願差異 / 行為科學模式",
            "flashcard_back": "解釋個人是否接受篩檢等預防性行為，最適用「健康信念模式（HBM）」。",
            "flashcard_summary": "篩檢行為決策解釋模式 -> 健康信念模式（Health Belief Model）"
        },
        {
            "question_id": "108-1_medicine-2_049",
            "question_number": 49,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "影響醫療費用成長率的主要因素。",
            "explanation": "整體醫療費用的長期成長主要與人口老化、國民所得增加及新醫療科技引進等供需面宏觀因素密切相關。醫病資訊不對稱是醫療市場的本質特徵，會導致市場失靈，但其對整體醫療費用「成長率」的直接影響相對較小。",
            "flashcard_front": "醫療費用成長率 / 人口老化 / 所得增加與醫療科技 / 資訊不對稱影響",
            "flashcard_back": "醫療費用成長率主要受人口老化、科技進步和所得影響；醫病資訊不對稱與成長率關聯性較小。",
            "flashcard_summary": "醫療費用成長率關聯較小的因素 -> 醫病資訊不對稱"
        },
        {
            "question_id": "108-1_medicine-2_050",
            "question_number": 50,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "新藥研發定價與成本構成因子。",
            "explanation": "原開發廠新藥定價昂貴主要是為回收高昂的研發成本、支付專利期保護費用以及負擔高失敗率的臨床試驗費用。相較之外，藥物本身的「生產製造原料與加工成本」占整體售價的比例極低，對定價的影響較小。",
            "flashcard_front": "原研新藥售價昂貴 / 研發費用 / 臨床試驗成本 / 生產製造與加工成本",
            "flashcard_back": "新藥昂貴主因是回收研發與試驗成本及專利保護；生產製造的直接成本對售價影響較小。",
            "flashcard_summary": "原研新藥定價影響較小的成本因子 -> 生產製造的成本"
        },
        {
            "question_id": "108-1_medicine-2_051",
            "question_number": 51,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "Metronidazole的臨床抗菌譜與治療用途。",
            "explanation": "Metronidazole主要針對厭氧菌（如困難梭狀芽孢桿菌 Clostridioides difficile）及原生動物（如陰道滴蟲 Trichomonas vaginalis、痢疾阿米巴 Entamoeba histolytica）感染，但對屬於革蘭氏陰性雙球菌的淋病雙球菌（Neisseria gonorrhoeae）無效。淋病雙球菌引起的感染臨床上主要以第三代頭孢菌素（如 Ceftriaxone）治療。",
            "flashcard_front": "Metronidazole / 臨床用途 / 厭氧菌與滴蟲 / 淋病雙球菌治療",
            "flashcard_back": "Metronidazole對厭氧菌、阿米巴與滴蟲有效；但「不適用於淋病雙球菌」感染（首選Ceftriaxone）。",
            "flashcard_summary": "Metronidazole非臨床用途 -> 淋病雙球菌引起之感染"
        },
        {
            "question_id": "108-1_medicine-2_052",
            "question_number": 52,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "抗癌化學治療藥物的分類與作用機轉。",
            "explanation": "Methotrexate（二氫葉酸還原酶抑制劑）與 5-fluorouracil（胸苷酸合成酶抑制劑）均會干擾核酸合成，屬於抗代謝藥物（anti-metabolites）。Cyclophosphamide 則屬於烷基化劑（alkylating agent），透過與DNA形成共價鍵結合來阻斷複製，故其餘配對皆有誤。",
            "flashcard_front": "Cyclophosphamide / Methotrexate / 5-Fluorouracil / 藥物機轉分類",
            "flashcard_back": "Methotrexate與5-FU為「抗代謝藥物（anti-metabolites）」；Cyclophosphamide為「烷基化劑」。",
            "flashcard_summary": "Methotrexate與5-FU之化療分類 -> 抗代謝藥物（anti-metabolites）"
        },
        {
            "question_id": "108-1_medicine-2_053",
            "question_number": 53,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "抗凝血藥物與抗血小板藥物的機轉區分。",
            "explanation": "Heparin（肝素）屬於抗凝血劑（anticoagulant），主要藉由活化抗凝血酶III（antithrombin III）來抑制凝血因子IIa與Xa，不屬於直接拮抗血小板凝集的藥物。Aspirin（抑制COX-1）、Dipyridamole（抑制PDE）及 Ticlopidine（阻斷ADP受體）皆為抗血小板凝集之藥物。",
            "flashcard_front": "Aspirin / Dipyridamole / Ticlopidine / Heparin / 藥理機轉分類",
            "flashcard_back": "Heparin為「抗凝血劑」；Aspirin、Dipyridamole及Ticlopidine為「抗血小板凝集拮抗劑」。",
            "flashcard_summary": "非血小板凝集拮抗劑之藥物 -> 肝素（heparin）"
        },
        {
            "question_id": "108-1_medicine-2_054",
            "question_number": 54,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "多巴胺致效劑Bromocriptine在內分泌疾病的作用機轉。",
            "explanation": "Bromocriptine為多巴胺受體致效劑，在肢端肥大症（acromegaly）患者中，能「直接」抑制腦下垂體前葉分泌生長激素（GH），並非藉由促進體制素（somatostatin）的分泌。此外，它能有效抑制泌乳激素（prolactin）分泌並改善巴金森氏症的症狀。",
            "flashcard_front": "Bromocriptine / 肢端肥大症治療 / 生長激素抑制機轉 / 體制素關係",
            "flashcard_back": "Bromocriptine治療肢端肥大症是「直接」抑制腦下垂體GH分泌，而非藉由增加體制素分泌。",
            "flashcard_summary": "Bromocriptine治療肢端肥大症機轉 -> 直接抑制腦下垂體生長激素分泌，而非藉由增加體制素"
        },
        {
            "question_id": "108-1_medicine-2_055",
            "question_number": 55,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "血管加壓素（Vasopressin/ADH）的生理與藥理作用。",
            "explanation": "血管加壓素（Vasopressin）又稱抗利尿激素（ADH），其主要生理作用為增加腎臟集合管對水分的重吸收，具有「抗利尿」作用，因而會減少水分流失並維持體液平衡。血管加壓素亦可活化V1受體引起血管收縮以提升血壓，並能刺激血小板釋放von Willebrand factor。",
            "flashcard_front": "血管加壓素 (Vasopressin/ADH) / 腎臟集合管 / 水分與鈉離子代謝 / 血管收縮",
            "flashcard_back": "Vasopressin具「抗利尿（保留水分）」作用而非利尿作用，不會造成水分與鈉離子大量流失。",
            "flashcard_summary": "血管加壓素錯誤描述 -> 具有利尿的作用，因此會造成水分與鈉離子流失"
        },
        {
            "question_id": "108-1_medicine-2_056",
            "question_number": 56,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "治療血鈣過高的利尿劑選擇與機轉。",
            "explanation": "治療高血鈣常合併使用生理食鹽水與環利尿劑（Loop diuretics，如 furosemide）。Furosemide 會抑制亨耳氏環粗上升支的 Na+/K+/2Cl- 共運輸體，進而降低管腔正電位，減少鈣離子與鎂離子的重吸收並促進其排出。Thiazide 類利尿劑則會促進腎臟重吸收鈣離子，會加重高血鈣，因此禁用於高血鈣患者。",
            "flashcard_front": "血鈣過高治療 / 腎臟鈣離子排泄 / Furosemide / Thiazide 比較",
            "flashcard_back": "高血鈣應選用環利尿劑「Furosemide」以促進鈣排泄；Thiazide會增加鈣重吸收，故禁用。",
            "flashcard_summary": "治療高血鈣的利尿劑選擇 -> 環利尿劑（furosemide）合併生理食鹽水"
        },
        {
            "question_id": "108-1_medicine-2_057",
            "question_number": 57,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "藥物誘發型紅斑性狼瘡（DILE）的常見致病藥物。",
            "explanation": "Procainamide（Ia類抗心律不整藥）為最容易引起藥物誘發型紅斑性狼瘡（DILE）的藥物之一。其他常引起DILE的藥物還包括降血壓藥 Hydralazine 以及抗結核藥 Isoniazid，此副作用多與患者體內慢速乙醯化（slow acetylator）基因型有關。",
            "flashcard_front": "藥物誘發型紅斑性狼瘡 (DILE) / 抗心律不整藥 / 慢速乙醯化 / 副作用",
            "flashcard_back": "常引起類紅斑性狼瘡症狀的抗心律不整藥為Ia類的「Procainamide」。",
            "flashcard_summary": "引起藥物誘發型紅斑性狼瘡的藥物 -> Procainamide"
        },
        {
            "question_id": "108-1_medicine-2_058",
            "question_number": 58,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "自主神經系統受體與胞內G蛋白偶聯關係。",
            "explanation": "膽鹼性M2受體（Muscarinic M2 receptor）與 Gi 蛋白偶聯，活化後會抑制腺苷酸環化酶（adenylyl cyclase）的活性，降低胞內 cAMP 濃度。M3 受體與 Gq 蛋白偶聯，活化 PLC；β1 與 β3 受體則與 Gs 蛋白偶聯，會活化腺苷酸環化酶，增加 cAMP 濃度。",
            "flashcard_front": "膽鹼性M2受體 / G蛋白偶聯 / 腺苷酸環化酶 (adenylyl cyclase) / cAMP 濃度",
            "flashcard_back": "M2受體與「Gi 蛋白」偶聯，活化會抑制 adenylyl cyclase 活性；而β受體多與 Gs 偶聯。",
            "flashcard_summary": "抑制腺苷酸環化酶活性的受體 -> 膽鹼性 M2 受體（M2 receptor）"
        },
        {
            "question_id": "108-1_medicine-2_059",
            "question_number": 59,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "前列環素（PGI2）類似物在肺高壓的應用。",
            "explanation": "Treprostinil 是前列環素（Prostacyclin, PGI2）的類似物（致效劑），藉由活化血管平滑肌細胞上的 IP 受體，增加 cAMP 以擴張肺血管，用於治療肺動脈高壓。Alprostadil 與 Misoprostol 為 PGE1 衍生物；Latanoprost 為 PGF2α 衍生物，主要用於青光眼治療。",
            "flashcard_front": "PGI2 致效劑 / 肺高壓 (pulmonary hypertension) / 血管舒張 / cAMP 增加",
            "flashcard_back": "用於治療肺高壓的PGI2致效劑為「Treprostinil」。Alprostadil及Misoprostol則為PGE1衍生物。",
            "flashcard_summary": "治療肺高壓的 PGI2 類似物 -> Treprostinil"
        },
        {
            "question_id": "108-1_medicine-2_060",
            "question_number": 60,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "多巴胺受體致效劑 Bromocriptine 治療巴金森氏症。",
            "explanation": "Bromocriptine 屬於麥角類（ergot）多巴胺受體致效劑，主要活化 dopaminergic D2 受體，用於改善巴金森氏症患者的運動症狀。Selegiline 為 MAO-B 抑制劑；Amantadine 主要促進多巴胺釋放；Entacapone 為 COMT 抑制劑，皆非直接作用於D2受體之致效劑。",
            "flashcard_front": "多巴胺 D2 受體致效劑 / 麥角類衍生物 / 巴金森氏症治療 / 藥物分類",
            "flashcard_back": "作用於多巴胺D2受體以治療巴金森氏症的致效劑為「Bromocriptine」。Selegiline是MAO-B抑制劑。",
            "flashcard_summary": "治療巴金森氏症的D2受體致效劑 -> Bromocriptine"
        }
    ]
}

# =====================================================================
# 108-1_medicine-3_batch-001
# =====================================================================
batch_data["108-1_medicine-3_batch-001"] = {
    "dataset_id": "108-1_medicine-3",
    "batch_id": "108-1_medicine-3_batch-001",
    "items": [
        {
            "question_id": "108-1_medicine-3_001",
            "question_number": 1,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "新陳代謝科",
            "category_confidence": "high",
            "key_point": "原發性空蝶鞍症候群的診斷與處置原則。",
            "explanation": "空蝶鞍（empty sella）若無臨床症狀，且月經、血糖、甲狀腺功能、皮質醇等內分泌指標皆完全正常，多為偶然發現的原發性空蝶鞍。此時不需進行手術、放射線或藥物治療，最恰當的處置是說明病情以消除疑慮（reassurance）並定期追蹤即可。",
            "flashcard_front": "空蝶鞍 (empty sella) / 內分泌功能正常 / 無臨床症狀 / 處置原則",
            "flashcard_back": "內分泌與生理功能完全正常的空蝶鞍病患，處置應以「reassurance（使放心追蹤）」為主，不需手術或放療。",
            "flashcard_summary": "無症狀且內分泌正常之空蝶鞍處置 -> 說明病情使病患放心（reassurance）"
        },
        {
            "question_id": "108-1_medicine-3_002",
            "question_number": 2,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "高血鈉的矯正速度限制與生理水分估算。",
            "explanation": "矯正慢性高血鈉時，血鈉降低速度必須緩慢（一般建議不超過10 mEq/L/day或0.5 mEq/L/hour），否則水分會快速進入已代償平衡的腦細胞中而導致腦水腫。人體總水量（TBW）男性約占體重的60%，女性約占50%；不易感知的水分流失通常約為10-15 mL/kg/day。",
            "flashcard_front": "高血鈉矯正速度 / 腦水腫預防 / 體液量估算 / Insensible loss",
            "flashcard_back": "高血鈉矯正速度每天「不可超過10 mEq/L（或10 mM/day）」以避免腦水腫。男性總水量約占體重60%。",
            "flashcard_summary": "高血鈉矯正限制 -> 每日血鈉降低不可超過10 mEq/L以預防腦水腫"
        },
        {
            "question_id": "108-1_medicine-3_003",
            "question_number": 3,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "乳糜瀉（Celiac disease）的臨床與實驗室特徵。",
            "explanation": "病健因慢性腹瀉就醫，此症狀在使用麵粉製品（含麩質）後加劇，伴有因吸收不良導致的輕度血鈣偏低，加上血清 IgA tissue transglutaminase (tTG) 抗體陽性，是典型的乳糜瀉（Celiac disease）表現。克隆氏症與克隆氏大腸炎較少表現為與麵食有如此直接關聯的特異性抗體陽性。",
            "flashcard_front": "麵食加重腹瀉 / 輕度低血鈣 / IgA anti-tTG 陽性",
            "flashcard_back": "應診斷為「乳糜瀉（Celiac disease）」，此為自體免疫引起的麩質過敏性腸病。",
            "flashcard_summary": "麵食加重腹瀉、IgA anti-tTG (+) -> 乳糜瀉（Celiac disease）"
        },
        {
            "question_id": "108-1_medicine-3_004",
            "question_number": 4,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "二尖瓣狹窄與主動脈瓣疾病的病理特徵。",
            "explanation": "二尖瓣狹窄（mitral stenosis）最主要病因為風濕性慢性發炎，常發病於中老年女性，近年在臺灣隨著公共衛生提升其發病數已減少。馬凡氏症常引起主動脈逆流，但第二心音常會減弱而非增強；二尖瓣狹窄時左心室充盈受阻，但左心室舒張末期壓（LVEDP）通常仍保持正常，而非上升。",
            "flashcard_front": "二尖瓣狹窄最常見病因 / 馬凡氏症與第二心音 / 左心室舒張末壓 (LVEDP) 變化",
            "flashcard_back": "二尖瓣狹窄主因為風濕熱，近年病例減少。二尖瓣狹窄時，左心室收縮功能與LVEDP通常是正常的。",
            "flashcard_summary": "二尖瓣狹窄病因與生理 -> 最常見為風濕性慢性發炎，左心室舒張末壓正常"
        },
        {
            "question_id": "108-1_medicine-3_005",
            "question_number": 5,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "medium",
            "key_point": "心電圖判斷WPW症候群旁道位置的規則。",
            "explanation": "WPW症候群（預激綜合症）中，利用心電圖定位旁道（accessory pathway）是國考常考題。根據官方給予答案，若V1導程之delta波與QRS波呈現正向（R > S），提示為Type A WPW，旁道通常定位於左心室側壁（left lateral ventricle）。",
            "flashcard_front": "WPW症候群 / 旁道 (accessory pathway) 定位 / V1 QRS正向 (R>S)",
            "flashcard_back": "V1導程QRS波與delta波主要朝上（正向），提示旁道位於「左心室側壁（左側）」。",
            "flashcard_summary": "WPW旁道定位 -> V1呈正向R波提示旁道位於左心室側壁"
        },
        {
            "question_id": "108-1_medicine-3_006",
            "question_number": 6,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "高血鉀在心電圖上的典型表現。",
            "explanation": "82歲慢性腎臟病患，由於腎臟排鉀功能受損，疲倦無力並呈現典型高血鉀（Hyperkalemia）之心電圖變化。高血鉀心電圖早期特徵為T波高尖（peaked T），隨著血鉀濃度升高會陸續出現PR間期延長、P波消失、QRS波寬大變形甚至呈現正弦波（sine wave）圖形。",
            "flashcard_front": "慢性腎臟病 / 疲倦無力 / 心電圖 T波高尖 / QRS變寬",
            "flashcard_back": "此心電圖特徵提示為「高血鉀症（Hyperkalemia）」，需密切注意並給予降鉀治療以防心跳驟停。",
            "flashcard_summary": "T波高尖與QRS變寬的心電圖表現 -> 高血鉀症（hyperkalemia）"
        },
        {
            "question_id": "108-1_medicine-3_007",
            "question_number": 7,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "急性心包膜炎的診斷與特徵。",
            "explanation": "患者出現急性胸痛，其胸痛有「特定姿勢（如坐直前傾）可緩解」的姿勢性疼痛特徵，加上抽血發現發炎指標（CRP）升高、超音波顯示少量心包膜積液，此為典型的急性心包膜炎（Pericarditis）表現。心肌梗塞引起的胸痛通常為壓迫感，且不會因前傾姿勢成明顯改善。",
            "flashcard_front": "姿勢性胸痛 (前傾緩解) / CRP升高 / 少量心包膜積液",
            "flashcard_back": "應診斷為「急性心包膜炎（pericarditis）」。其胸痛典型為前傾時減輕，仰臥時加重。",
            "flashcard_summary": "前傾緩解之胸痛合併心包膜積液 -> 急性心包膜炎"
        },
        {
            "question_id": "108-1_medicine-3_008",
            "question_number": 8,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "心房中膈缺損（ASD）的身體檢查與心電圖特徵。",
            "explanation": "28歲女性運動時呼吸困難，聽診發現固定性第二心音分裂（fixed splitting S2），心電圖呈現右軸偏向與V1的 rSR'（右束支傳導阻滯圖形），心臟超音波證實右心房與右心室擴大，這些都是心房中膈缺損（ASD）造成左向右分流、導致右心血流量過多的典型臨床表徵。",
            "flashcard_front": "固定性第二心音分裂 (fixed splitting S2) / V1 rSR' / 右心擴大",
            "flashcard_back": "應診斷為「心房中膈缺損（ASD）」。其固定性S2分裂是由於右心回流血量恆定增加，使肺動脈瓣關閉延後所致。",
            "flashcard_summary": "固定性 S2 分裂與 V1 rSR' -> 心房中膈缺損（ASD）"
        },
        {
            "question_id": "108-1_medicine-3_009",
            "question_number": 9,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "踝肱血壓指數（ABI）的計算公式與臨床意義。",
            "explanation": "踝肱血壓指數（ABI）的計算公式為：下肢足背動脈（或後脛動脈）收縮壓，除以兩側上臂肱動脈收縮壓中的「較高者」。本題中患者下肢足背動脈收縮壓為90 mmHg，上臂肱動脈收縮壓為150 mmHg，故其 ABI = 90 / 150 = 0.6。ABI小於0.9提示有周邊動脈阻塞疾病（PAOD）。",
            "flashcard_front": "下肢收縮壓 90 mmHg / 上臂收縮壓 150 mmHg / ABI 計算",
            "flashcard_back": "ABI = 下肢收縮壓 / 上肢收縮壓較高者。計算為 90 / 150 = 0.6，小於0.9代表周邊血管阻塞。",
            "flashcard_summary": "ABI 計算 -> 下肢收縮壓除以上臂收縮壓，本題 90/150 = 0.6"
        },
        {
            "question_id": "108-1_medicine-3_010",
            "question_number": 10,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "頸靜脈壓評估及腹頸靜脈反流的臨床意義。",
            "explanation": "當按壓患者腹部時，若出現頸靜脈持續鼓脹，且高度在鎖骨上方超過5公分，此時稱為腹頸靜脈反流（Abdominojugular reflux）陽性。此現象代表右心房與右心室無法適應增加的回心血量，是體液容量過負荷（Volume overload）或右心衰竭的強烈指標。",
            "flashcard_front": "按壓腹部 / 頸靜脈鼓脹超鎖骨5公分 / Abdominojugular reflex",
            "flashcard_back": "此為腹頸靜脈反流陽性，提示體內有「容量過負荷（volume overload）」或右心衰竭。",
            "flashcard_summary": "腹頸靜脈反流（Abdominojugular reflux）陽性 -> 提示容量過負荷（volume overload）"
        },
        {
            "question_id": "108-1_medicine-3_011",
            "question_number": 11,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "改變前負荷動作對不同心臟雜音的影響機轉。",
            "explanation": "在肥厚性阻塞性心肌病變（HOCM）中，當患者從臥/坐姿站立時，靜脈回流減少導致心臟前負荷（preload）降低，左心室容積變小，進而「加重」左心室出口的狹窄，使得心雜音強度「增強」而非減弱，因此D選項錯誤。其餘動作如Valsalva或立姿，皆會因preload下降使HOCM雜音增強。",
            "flashcard_front": "肥厚性阻塞性心肌病變 (HOCM) / 站立姿勢改變 / Preload 下降 / 心雜音強度",
            "flashcard_back": "站立時回心血量下降（preload減少），左心室容積變小會「加重」HOCM的出口阻塞，使心雜音「增強」。",
            "flashcard_summary": "站立對 HOCM 雜音影響 -> 站立使前負荷降低，HOCM 心雜音增強而非減弱"
        },
        {
            "question_id": "108-1_medicine-3_012",
            "question_number": 12,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "其他",
            "category_confidence": "high",
            "key_point": "馬凡氏症候群的結締組織異常與身體特徵。",
            "explanation": "馬凡氏症候群（Marfan's syndrome）是一種體染色體顯性遺傳的結締組織疾病。患者在口腔上的典型特徵為「高拱的腭弓（high-arched palate）」，並非較低的腭弓，因此C選項敘述錯誤。患者常有水晶體脫位、瘦長指、關節過度伸展及主動脈瘤或夾層等特徵。",
            "flashcard_front": "馬凡氏症候群 (Marfan's) / 瘦長指與水晶體脫位 / 口腔顎弓特徵",
            "flashcard_back": "馬凡氏症病患口腔特徵為「高拱的腭弓（high-arched palate）」，而非較低的牙腭弓。",
            "flashcard_summary": "馬凡氏症口腔特徵 -> 具有高拱的腭弓（high-arched palate）"
        },
        {
            "question_id": "108-1_medicine-3_013",
            "question_number": 13,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "肝臟穿刺切片組織檢體的合格度判定標準。",
            "explanation": "為了確保肝穿刺病理診斷的準確性，合格的針刺檢體長度通常要求至少達到 1.5 cm 以上（或含有至少10-12個門脈區），若小於此長度（如0.5 cm）則極可能因代表性不足而無法提供足夠的病理診斷資訊，因此A選項錯誤。使用較粗的穿刺針雖然會增加出血風險，但所得組織資訊也較豐富。",
            "flashcard_front": "肝臟切片 (liver biopsy) / 檢體合格長度 / 門脈區數量",
            "flashcard_back": "肝臟穿刺切片檢體長度應「至少達到1.5 cm（而非0.5 cm）」才具備足夠的診斷代表性。",
            "flashcard_summary": "肝切片合格檢體長度 -> 應至少達到 1.5 cm 以提供足夠資訊"
        },
        {
            "question_id": "108-1_medicine-3_014",
            "question_number": 14,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "非侵入性肝纖維化檢測工具的臨床限制。",
            "explanation": "血清生物學標誌檢測（如 FibroTest, APRI）雖然是一項便利的非侵入性肝纖維化評估工具，但其容易受到急性發炎、溶血或黃疸等非纖維化因素的干擾，因此「無法」精準判定各種原因引起的各級肝纖維化程度，B選項過於誇大其準確度而錯誤。其餘如彈性造影等工具也均有其限制。",
            "flashcard_front": "非侵入性肝纖維化 / 血清生物學標誌 / 診斷精準度限制",
            "flashcard_back": "血清學肝纖維化檢測易受溶血、膽汁淤積或發炎干擾，無法對所有病因與各纖維化等級做出絕對精準的判定。",
            "flashcard_summary": "血清肝纖維化標誌限制 -> 易受溶血與急性發炎干擾，無法對所有等級做精準判定"
        },
        {
            "question_id": "108-1_medicine-3_015",
            "question_number": 15,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "感染科",
            "category_confidence": "high",
            "key_point": "B型肝炎病毒（HBV）的結構組成與分布。",
            "explanation": "B型肝炎病毒的核衣殼（nucleocapsid）內部主要包含核心抗原（HBcAg）、病毒DNA與DNA聚合酶，而表面抗原（HBsAg）是包裹在病毒最外層的脂質雙層「外膜（envelope）」上，並不屬於核衣殼的一部分，故C選項描述錯誤。完整病毒體（Dane particle）大小約為42 nm，核衣殼內核大小則為27 nm。",
            "flashcard_front": "B型肝炎病毒結構 / 核衣殼 (nucleocapsid) 組成 / 表面抗原 (HBsAg) 位置",
            "flashcard_back": "HBsAg存在於HBV的外膜上，核衣殼內部只包含DNA、DNA polymerase及HBcAg，不含HBsAg。",
            "flashcard_summary": "B肝病毒核衣殼成分 -> 包含核心抗原與DNA聚合酶，表面抗原（HBsAg）則位於外膜"
        }
    ]
}

# =====================================================================
# 108-1_medicine-3_batch-002
# =====================================================================
batch_data["108-1_medicine-3_batch-002"] = {
    "dataset_id": "108-1_medicine-3",
    "batch_id": "108-1_medicine-3_batch-002",
    "items": [
        {
            "question_id": "108-1_medicine-3_016",
            "question_number": 16,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "晚期肝細胞癌（HCC）的全身性藥物治療指引。",
            "explanation": "患者為B型肝炎引起的肝細胞癌，伴隨門靜脈主幹栓塞及肺部轉移，已屬於晚期肝癌（BCLC Stage C），且其肝功能尚佳（Child-Pugh A，無失代償）。依據治療指引，此時最適合的治療為全身性標靶藥物治療（如口服 Sorafenib 或免疫療法組合），而不適合切除、栓塞等局部治療。",
            "flashcard_front": "肝細胞癌 (HCC) / 門靜脈主幹栓塞 / 肺部轉移 / Child-Pugh A / 治療選擇",
            "flashcard_back": "此為晚期肝癌（BCLC C），肝功能代償良好，首選治療為標靶藥物「Sorafenib」或全身性免疫治療。",
            "flashcard_summary": "晚期肝細胞癌合併門靜脈栓塞及轉移治療 -> 首選口服標靶藥物 Sorafenib 治療"
        },
        {
            "question_id": "108-1_medicine-3_017",
            "question_number": 17,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "肝腎症候群（HRS）的臨床分類、藥物治療與預後。",
            "explanation": "在肝腎症候群（HRS）的內科藥物治療中，血管收縮劑（如 Terlipressin）合併白蛋白（Albumin）輸注是目前最主要的標準治療方案。第一型 HRS 表現為急遽、快速惡化的急性腎損傷，預後極差；而由於 HRS 主要是功能性腎臟血管收縮所致，病患接受肝移植後，腎功能通常可以恢復。",
            "flashcard_front": "肝腎症候群 (HRS) / 內科藥物治療 / Terlipressin / 肝移植後腎功能",
            "flashcard_back": "HRS可用「Terlipressin + Albumin」治療。第一型惡化極快，肝移植後腎功能多可恢復正常。",
            "flashcard_summary": "肝腎症候群（HRS）治療與特性 -> 可用 Terlipressin 治療，移植後腎功能可恢復"
        },
        {
            "question_id": "108-1_medicine-3_018",
            "question_number": 18,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "發炎性腸道疾病（IBD）的流行病學與保護因子。",
            "explanation": "發炎性腸道疾病（IBD）包括克隆氏症（CD）與潰瘍性大腸炎（UC）。在流行病學上，抽菸是克隆氏症的危險因子，但卻是潰瘍性大腸炎的保護因子。此外，研究發現「闌尾切除術（appendectomy）」能降低潰瘍性大腸炎的發病風險，但對克隆氏症則無此保護效應，故第4點錯誤，僅1、2、3正確。",
            "flashcard_front": "克隆氏症與潰瘍性大腸炎 / 抽菸效應差異 / 闌尾切除術 (appendectomy)",
            "flashcard_back": "闌尾切除可降低「潰瘍性大腸炎（UC）」風險，但對克隆氏症無效。抽菸為CD危險因子、UC保護因子。",
            "flashcard_summary": "IBD 與闌尾切除術關係 -> 闌尾切除能降低潰瘍性大腸炎風險，對克隆氏症則無保護效果"
        },
        {
            "question_id": "108-1_medicine-3_019",
            "question_number": 19,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "大腸癌的病變解剖部位與臨床症狀連結。",
            "explanation": "大腸癌因慢性隱性失血，極容易導致缺鐵性貧血，在血球型態上表現為小球性貧血（microcytic anemia）。早期大腸癌通常無症狀；右側大腸（升結腸）因管腔大且糞便液狀，多以慢性貧血為主要症狀；左側大腸（降結腸、乙狀結腸）管腔小且糞便已成形，較易引起排便習慣改變與腸阻塞。",
            "flashcard_front": "大腸癌慢性出血 / 貧血型態 / 左右側大腸癌症狀差異",
            "flashcard_back": "大腸癌慢性失血會導致「小球性貧血（缺鐵性）」。右側易貧血，左側易排便習慣改變與阻塞。",
            "flashcard_summary": "大腸癌引起的貧血型態 -> 屬於缺鐵引起的小球性貧血"
        },
        {
            "question_id": "108-1_medicine-3_020",
            "question_number": 20,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "Zollinger-Ellison 症候群的病理生理與遺傳關聯。",
            "explanation": "Zollinger-Ellison 症候群（ZES）是由於分泌大量胃泌素的胃泌素瘤（gastrinoma）引起，在消化性潰瘍患者中約占0.1~1%，約有25%的患者與多發性內分泌腫瘤第一型（MEN 1）相關。胃泌素瘤多為惡性（約佔2/3），且多起源於非胰島β細胞，病患常因過多胃酸流入小腸而合併嚴重水瀉。",
            "flashcard_front": "Zollinger-Ellison 症候群 (ZES) / gastrinoma / 消化性潰瘍比例 / MEN 1 關係",
            "flashcard_back": "ZES由gastrinoma引起，與「MEN 1」高度相關，約有2/3的gastrinoma為惡性，常引起嚴重水瀉。",
            "flashcard_summary": "Zollinger-Ellison 症候群特性 -> 由胃泌素瘤引起，與 MEN 1 相關"
        },
        {
            "question_id": "108-1_medicine-3_021",
            "question_number": 21,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "胰臟癌的危險因子與篩檢限制。",
            "explanation": "抽菸是目前最明確的胰臟癌危險因子，約有20~25%的胰臟癌與吸菸相關。大約僅有5-10%的胰臟癌與家族遺傳基因突變有關；血清腫瘤指標 CA19-9 與 CEA 敏感度及特異度皆不足，不適合作為一般無症狀大眾的常規篩檢工具；晚期胰臟癌患者即使接受 Gemcitabine 治療，其一年存活率亦極低（遠低於70%）。",
            "flashcard_front": "胰臟癌危險因子 / 遺傳比例 / CA19-9 篩檢效力 / 晚期存活率",
            "flashcard_back": "「抽菸」是胰臟癌最重要的可預防危險因子（約占20-25%）。CA19-9不適合作為一般無症狀者的早期篩檢工具。",
            "flashcard_summary": "胰臟癌重要危險因子 -> 抽菸（約有20~25%的胰臟癌與其相關）"
        },
        {
            "question_id": "108-1_medicine-3_022",
            "question_number": 22,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "末期腎臟病患常發生的電解質與酸鹼失衡。",
            "explanation": "慢性腎臟病末期（Cr 6.3）患者由於腎絲球過濾率極低，腎臟對水分的濃縮與稀釋功能均完全喪失，極易因水分滯留而出現稀釋性「低血鈉」，而極少發生 148 mEq/L 之高血鈉。其餘如無法有效排鉀導致的高血鉀、無法排磷導致的高血磷，以及活性維生素D合成降低引起的低血鈣，都是末期腎病非常典型的實驗室異常。",
            "flashcard_front": "末期腎臟病 (CKD stage 5) / 電解質異常 / 高血鉀與高血磷 / 血鈉變化",
            "flashcard_back": "末期腎臟病患因水分排除障礙易出現「低血鈉」，「極少發生高血鈉 (如148 mEq/L)」。",
            "flashcard_summary": "末期腎臟病最少發生的異常 -> 高血鈉（通常為稀釋性低血鈉）"
        },
        {
            "question_id": "108-1_medicine-3_023",
            "question_number": 23,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "透析患者高血磷與無動力性骨病變的藥物選擇。",
            "explanation": "該透析病患同時有高血磷（6.8 mg/dL）與高血鈣（10.8 mg/dL），且 PTH 僅 88 pg/mL（低於透析患者建議目標，提示為無動力性骨病變）。此時不可給予會同時升高血鈣與血磷的活性維生素D，最適合的處理是給予非含鈣的「降磷藥物（磷結合劑，如 Sevelamer 或 Lanthanum）」，以控制血磷並避免血管鈣化。",
            "flashcard_front": "血液透析 / 高鈣高磷 / PTH 88 / 降磷藥物選擇 / 活性維生素 D 禁忌",
            "flashcard_back": "病患高鈣高磷且PTH偏低，禁用活性維生素D；首選使用非鈣非鋁的「磷結合劑（phosphate binder）」降磷。",
            "flashcard_summary": "透析患者高鈣高磷合併低PTH處理 -> 給予非鈣非鋁的磷結合劑（phosphate binder）"
        },
        {
            "question_id": "108-1_medicine-3_024",
            "question_number": 24,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "移植後新發糖尿病（NODAT）與免疫抑制劑的關聯。",
            "explanation": "末期腎病接受移植後出現新發糖尿病（NODAT），與免疫抑制劑的使用高度相關。其中以鈣調磷酸酶抑制劑（CNI）中的 Tacrolimus 誘發糖尿病的風險最高（高於 Cyclosporine），其機轉是抑制胰臟β細胞分泌胰島素，故B選項為正確答案。",
            "flashcard_front": "腎臟移植 / 血糖升高 (NODAT) / 鈣調磷酸酶抑制劑 (CNI) / 免疫抑制劑副作用",
            "flashcard_back": "腎移植後最容易引發糖尿病的免疫抑制劑是「Tacrolimus」（機轉為抑制胰島素分泌）。",
            "flashcard_summary": "移植後引發高血糖最常見免疫抑制劑 -> Tacrolimus"
        },
        {
            "question_id": "108-1_medicine-3_025",
            "question_number": 25,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "代謝性鹼中毒時區分腎前性與腎性急性腎損傷的指標。",
            "explanation": "當患者因大量嘔吐流失胃酸（HCl）而導致代謝性鹼中毒時，為了排出體內過多的碳酸氫根，腎臟會代償性增加鈉的排出，進而使尿鈉及鈉分數排泄率（FENa）假性升高。此時，為了準確區分腎前性（prerenal）與腎性（intrinsic）急性腎損傷，應使用「氯分數排泄率（FECl）」作為指標（腎前性 FECl < 1%）。",
            "flashcard_front": "嘔吐 / 代謝性鹼中毒 / 急性腎損傷區分 / FENa 限制 / FECl 應用",
            "flashcard_back": "代謝性鹼中毒時因尿鈉排出增加使FENa失真，應改用「氯分數排泄率（FECl）」來鑑別診斷。",
            "flashcard_summary": "鹼中毒時區分 AKI 病因指標 -> 使用氯分數排泄率（FECl）而非 FENa"
        },
        {
            "question_id": "108-1_medicine-3_026",
            "question_number": 26,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "伴隨外周血嗜酸性球增多（Eosinophilia）的急性腎損傷病因。",
            "explanation": "急性腎損傷（AKI）伴隨外周血嗜酸性球增多（Eosinophilia）常見於急性藥物誘導的間質性腎炎、膽固醇栓塞（atheroembolic disease）以及 Churg-Strauss 症候群。顯微鏡下多血管炎（Microscopic polyangiitis, MPA）屬於ANCA相關小血管炎，一般較少以嗜酸性球增多為特徵。",
            "flashcard_front": "急性腎損傷 / 嗜酸性球增多 (Eosinophilia) / 藥物間質性腎炎 / 膽固醇栓塞",
            "flashcard_back": "藥物間質性腎炎與膽固醇栓塞常伴有嗜酸性球增多；而「顯微鏡下多血管炎 (MPA)」則極少出現此特徵。",
            "flashcard_summary": "最少伴隨嗜酸性球增多的 AKI 疾病 -> 顯微鏡下多血管炎（Microscopic polyangiitis）"
        },
        {
            "question_id": "108-1_medicine-3_027",
            "question_number": 27,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "KDIGO 組織制定的急性腎損傷（AKI）診斷與分期標準。",
            "explanation": "KDIGO的AKI定義包含：48小時內血清肌酸酐值（SCr）上升大於或等於 0.3 mg/dL；或已知或假定在 7 天內（而非5天內）SCr 上升至基礎值的 1.5 倍（50%）以上；或尿量小於 0.5 mL/kg/hour 持續達 6 小時。因此，B選項中「5天內上升25%」不符合診斷標準而錯誤。",
            "flashcard_front": "KDIGO / 急性腎損傷 (AKI) 診斷標準 / 肌酸酐上升時間與幅度 / 尿量時間",
            "flashcard_back": "KDIGO標準為：48小時內SCr上升>=0.3 mg/dL，或「7天內上升>=1.5倍」，或尿量小於0.5 mL/kg/h達6小時。",
            "flashcard_summary": "KDIGO AKI定義錯誤描述 -> 血清肌酸酐值於 5 天內上升幅度大於或等於 25%"
        },
        {
            "question_id": "108-1_medicine-3_028",
            "question_number": 28,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "NSAID 藥物誘導的腎臟病變特徵。",
            "explanation": "病患服用非類固醇消炎止痛藥（Diclofenac）後迅速出現全身水腫、重度蛋白尿（12 g/g Cr）、低白蛋白血症（1.8 g/dL），且腎功能急性惡化（Cr 2.0）。此為典型的止痛藥引發之「急性間質性腎炎合併微小病變（Minimal change disease, MCD）」表現。膜性腎病變雖也是NSAID副作用，但通常病程進展較緩慢，不會在短時間內出現如此急性的腎衰竭表現。",
            "flashcard_front": "服用 Diclofenac / 泡沫尿與全身水腫 / 重度蛋白尿 / 急性腎衰竭 (Cr 2.0)",
            "flashcard_back": "NSAID常誘導「微小病變腎病（Minimal Change Disease, MCD）」合併急性間質性腎炎，表現為急性發作的重度腎病症候群。",
            "flashcard_summary": "止痛藥引起的急性重度蛋白尿與腎功能惡化 -> 微小病變（Minimal change disease）"
        },
        {
            "question_id": "108-1_medicine-3_029",
            "question_number": 29,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "免疫風濕科",
            "category_confidence": "high",
            "key_point": "高尿酸血症與痛風的遺傳、代謝及治療機轉。",
            "explanation": "次黃嘌呤鳥嘌呤磷酸核糖轉移酶（HPRT）基因位於X染色體上，當此基因發生先天突變完全缺乏時會導致 Lesch-Nyhan 症候群，表現為重度高尿酸血症與自殘行為。人體尿酸約有三分之二由腎臟排出，其餘由腸道排出；利尿劑（如 Thiazide）會抑制尿酸排泄而誘發痛風；化療引起的腫瘤溶解症候群預防首選為 Rasburicase，而非 Benzbromarone。",
            "flashcard_front": "HPRT 基因定位 / 尿酸主要排泄管道 / 利尿劑對尿酸影響 / 痛風生理",
            "flashcard_back": "HPRT基因位於「X染色體」；突變會引發重度高尿酸血症。尿酸主要由腎臟排出；Thiazide類利尿劑會使血尿酸上升。",
            "flashcard_summary": "高尿酸血症遺傳與病理 -> HPRT 基因位在 X 染色體上，突變會導致高尿酸血症"
        },
        {
            "question_id": "108-1_medicine-3_030",
            "question_number": 30,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "免疫風濕科",
            "category_confidence": "high",
            "key_point": "焦磷酸鈣沉積症（CPPD）與羥磷灰石（apatite）關節炎的流行病學。",
            "explanation": "焦磷酸鈣沉積症（CPPD，又稱假性痛風）引起的急性關節炎主要好發於「老年人」（通常大於60歲），在年輕男性中極罕見，故B選項敘述錯誤。CPPD常侵犯大關節（如膝關節），確診必須透過關節液偏光顯微鏡分析以尋找弱正雙折射的棒狀或磚塊狀結晶。",
            "flashcard_front": "假性痛風 (CPPD) / 好發年齡與性別 / 偏光顯微鏡結晶型態",
            "flashcard_back": "CPPD急性關節炎好發於「老年人（大於60歲）」，而非年輕男性；其結晶在偏光下呈「弱正雙折射」。",
            "flashcard_summary": "CPPD 關節炎好發特徵 -> 主要發生於老年人，而非年輕男性"
        }
    ]
}

# =====================================================================
# 108-1_medicine-4_batch-001
# =====================================================================
batch_data["108-1_medicine-4_batch-001"] = {
    "dataset_id": "108-1_medicine-4",
    "batch_id": "108-1_medicine-4_batch-001",
    "items": [
        {
            "question_id": "108-1_medicine-4_001",
            "question_number": 1,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "小兒哮吼（Croup）的典型影像特徵與常見病原體。",
            "explanation": "小兒哮吼（Croup）常見聲門下氣道狹窄，在頸部X光上會呈現典型的尖塔徵象（steeple sign）。此疾病最常見的病原體是副流感病毒（parainfluenza virus），而非腸病毒（enterovirus）。臨床症狀包括犬吠樣咳嗽、吸氣性喘鳴及聲音沙啞等。",
            "flashcard_front": "哮吼 (Croup) / Steeple sign / 聲門下狹窄 / 最常見病原體",
            "flashcard_back": "哮吼典型X光呈「Steeple sign」，最常見病原為「副流感病毒（parainfluenza virus）」，而非腸病毒。",
            "flashcard_summary": "哮吼最常見病原 -> 副流感病毒（parainfluenza virus），X光見尖塔徵象"
        },
        {
            "question_id": "108-1_medicine-4_002",
            "question_number": 2,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "EBV急性感染的抗體力價特徵。",
            "explanation": "當病童發生EBV急性感染（傳染性單核球增多症）時，免疫系統剛開始針對病毒外殼抗原（VCA）產生抗體，此時 anti-VCA IgM 與 anti-VCA IgG 會呈現陽性；而針對核抗原的 anti-EBNA 抗體一般要在感染數週至數月後才會轉陽，因此急性期為陰性，C選項為正確診斷指標。",
            "flashcard_front": "EBV 急性感染 / 傳染性單核球增多 / VCA 抗體 / EBNA 抗體",
            "flashcard_back": "EBV急性感染時，「anti-VCA IgM 與 IgG 均為陽性」，但「anti-EBNA 為陰性」。",
            "flashcard_summary": "EBV急性感染抗體特性 -> anti-VCA IgM(+)、anti-VCA IgG(+)、anti-EBNA(-)"
        },
        {
            "question_id": "108-1_medicine-4_003",
            "question_number": 3,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "嬰幼兒急性細支氣管炎（Bronchiolitis）的最常見病原。",
            "explanation": "急性細支氣管炎（Bronchiolitis）是兩歲以下嬰幼兒非常常見的下呼吸道感染，最主要的病原體為呼吸道融合病毒（Respiratory syncytial virus, RSV），約占所有病例的六成以上。其餘病原如腺病毒、流感病毒及人類偏肺病毒等亦可引起，但盛行率皆低於RSV。",
            "flashcard_front": "1歲幼兒 / 急性細支氣管炎 (Bronchiolitis) / 喘鳴與下陷 / 最常見病原",
            "flashcard_back": "嬰幼兒急性細支氣管炎最常見的致病原為「呼吸道融合病毒（RSV）」。",
            "flashcard_summary": "急性細支氣管炎最常見病原 -> 呼吸道融合病毒（RSV）"
        },
        {
            "question_id": "108-1_medicine-4_004",
            "question_number": 4,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "兒童社區感染性肺炎的併發症盛行率。",
            "explanation": "兒童細菌性社區肺炎常見的局部併發症包含肋膜積水、膿胸及肺膿瘍；心包膜炎則可由鄰近發炎蔓延引起。相較之下，血行傳播至中樞神經系統引起腦膜炎（Meningitis），在現今常規肺炎鏈球菌及嗜血桿菌疫苗接種普及後，已極為罕見，為最不常見的併發症。",
            "flashcard_front": "兒童細菌性肺炎 / 肺部局部併發症 / 腦膜炎 / 疫苗普及影響",
            "flashcard_back": "兒童細菌性肺炎最不常見的併發症為「腦膜炎」；膿胸、肋膜積水及肺膿瘍為常見局部併發症。",
            "flashcard_summary": "細菌性肺炎最不常見併發症 -> 腦膜炎（Meningitis）"
        },
        {
            "question_id": "108-1_medicine-4_005",
            "question_number": 5,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "各型肝炎病毒的傳播途徑與周產期傳染。",
            "explanation": "A型肝炎主要經由糞口途徑（fecal-oral route）傳播，不會經由周產期或母嬰垂直傳染。相較之下，B型、C型與D型肝炎均可藉由血液或體液接觸傳播，在臨床上都有明確的周產期或垂直傳染風險。",
            "flashcard_front": "肝炎病毒 / 糞口傳播 / 周產期傳染 / 垂直感染風險",
            "flashcard_back": "「A型肝炎」經由糞口傳染，無周產期傳染风险。B、C、D型肝炎則皆有周產期傳染風險。",
            "flashcard_summary": "不會經周產期傳染的肝炎 -> A型肝炎（主要經由糞口途徑傳染）"
        },
        {
            "question_id": "108-1_medicine-4_006",
            "question_number": 6,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "小兒常規疫苗的接種時程與年齡限制。",
            "explanation": "輪狀病毒疫苗（口服）通常必須在嬰兒出生後 8 個月大以前完成所有劑量的接種，滿周歲後已不適合給予。水痘疫苗、A型肝炎疫苗第一劑及 13 價結合型肺炎鏈球菌疫苗（第三劑）皆是臺灣現行建議在嬰兒滿 12 個月大時常規接種的疫苗。",
            "flashcard_front": "滿12個月常規疫苗 / 輪狀病毒疫苗 / 水痘與A肝疫苗 / 接種年齡限制",
            "flashcard_back": "「輪狀病毒疫苗（口服）」須在8個月大前完成接種，滿1歲已不適合接種。滿1歲應接種水痘、A肝及肺炎鏈球菌疫苗。",
            "flashcard_summary": "1歲時不適合接種的疫苗 -> 輪狀病毒疫苗（必須在8個月大前口服完畢）"
        },
        {
            "question_id": "108-1_medicine-4_007",
            "question_number": 7,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "先天性食道閉鎖與氣管食道瘻管的分類與臨床診斷。",
            "explanation": "嬰兒出生後流涎、嘴角冒泡且鼻胃管無法順利置入，代表有食道閉鎖（Esophageal atresia）。出生12小時後 X 光（KUB）呈現「無腸氣（氣腹無氣）」，說明胃腸道內沒有氣體進入，這排除了下段食道與氣管相通的可能（最常見的C型），故最可能的診斷為食道閉鎖合併「上段」食道氣管瘻管（B型）或單純食道閉鎖（A型，但選項中以B型為最可能且選項對應正解B）。",
            "flashcard_front": "新生兒口吐白沫 / 鼻胃管阻擋 / KUB 無腸氣 / 食道氣管瘻管分類",
            "flashcard_back": "胃管受阻且KUB無腸氣，代表「食道閉鎖合併上段食道氣管瘻管（Type B）」或無瘻管（Type A）。",
            "flashcard_summary": "胃管受阻合併KUB無腸氣 -> 食道閉鎖合併上段食道氣管瘻管（或無瘻管）"
        },
        {
            "question_id": "108-1_medicine-4_008",
            "question_number": 8,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "新生兒病理性黃疸的鑑別診斷與ABO血型不合。",
            "explanation": "病童在出生後 19 小時即出現顯著黃疸（總膽紅素 12 mg/dL），屬於出生24小時內的病理性黃疸。母親血型為 O 型，父親為 B 型（小孩血型可能為B型），且已排除母乳性黃疸（常在一週後才顯著）及海洋性貧血（新生兒期極少表現為急性溶血性黃疸），最可能的診斷為 ABO 血型不合（ABO incompatibility）引起的溶血性黃疸。",
            "flashcard_front": "出生19小時黃疸 / Bil 12 / 母親O型 / 父親B型 / 溶血",
            "flashcard_back": "24小時內出現黃疸且母O型子B型，高度懷疑「ABO血型不合（ABO incompatibility）」引起的溶血性黃疸。",
            "flashcard_summary": "出生24小時內病理性黃疸且母O型父B型 -> ABO血型不合（ABO incompatibility）"
        },
        {
            "question_id": "108-1_medicine-4_009",
            "question_number": 9,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "先天性橫膈膜疝氣的影像學與臨床特徵。",
            "explanation": "新生兒出生後立即有呼吸窘迫、發紺、舟狀腹（胸高腹低）等特徵。最大心音偏向右側（心臟受壓移位），加上 X 光顯示胸腔內充滿腸氣陰影且縱膈腔向對側移位，是典型的先天性橫膈膜疝氣（Congenital diaphragmatic hernia）表現。此症常伴有同側肺發育不全，需緊急氣管插管給予呼吸支持。",
            "flashcard_front": "新生兒呼吸窘迫 / 心音偏右 / 胸腔見腸氣 / 縱膈腔移位",
            "flashcard_back": "應診斷為「先天性橫膈膜疝氣（Diaphragmatic hernia）」。心臟與縱膈腔會被擠壓移向對側（常為右側）。",
            "flashcard_summary": "胸腔充滿腸氣且心音偏右之新生兒呼吸窘迫 -> 橫膈膜疝氣（Diaphragmatic hernia）"
        },
        {
            "question_id": "108-1_medicine-4_010",
            "question_number": 10,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "先天性巨結腸症與功能性便秘的臨床鑑別診斷。",
            "explanation": "大便失禁或溢屎（encopresis）是功能性便秘（FC）的常見特徵（直腸因糞便堆積而擴張，稀便從邊緣滲出），而在先天性巨結腸症（HD）病童中極為罕見（因為無神經節段痙攣狹窄，大便無法到達直腸），因此A選項稱 HD > FC 是錯誤的。HD病童常見生長遲緩、腹脹及合併小腸結腸炎的風險。",
            "flashcard_front": "大便失禁 (Encopresis) / 先天性巨結腸症 (HD) / 功能性便秘 (FC) 比較",
            "flashcard_back": "大便失禁（溢屎）在「功能性便秘（FC）」較常見，先天性巨結腸症（HD）病童則極少出現（FC > HD）。",
            "flashcard_summary": "大便失禁在 HD 與 FC 的比較 -> 功能性便秘（FC）發生率高於先天性巨結腸症（HD）"
        },
        {
            "question_id": "108-1_medicine-4_011",
            "question_number": 11,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "遺傳性腸胃道息肉症候群的惡性化風險。",
            "explanation": "家族性結直腸息肉症（Familial adenomatous polyposis, FAP）是一種體染色體顯性遺傳疾病，病患大腸內會長出成百上千個腺瘤性息肉。若不進行預防性大腸切除術，患者在中年（40歲前）惡化發展為大腸癌（Colon cancer）的風險高達近 100%，顯著高於幼年性息肉症及 Peutz-Jeghers 等症候群。",
            "flashcard_front": "大腸息肉 / 體染色體顯性遺傳 / 大腸癌風險最高 / 腺瘤性息肉",
            "flashcard_back": "發生大腸癌風險最高的為「家族性結直腸息肉症（FAP）」，其惡變機率近乎 100%。",
            "flashcard_summary": "大腸癌風險最高的腸道息肉症 -> 家族性結直腸息肉症（FAP）"
        },
        {
            "question_id": "108-1_medicine-4_012",
            "question_number": 12,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "非傷寒沙門氏菌腸胃炎的治療原則。",
            "explanation": "1歲大女嬰確診為非傷寒沙門氏菌（Nontyphoidal Salmonella）腸胃炎，此時已退燒、血絲便減少且精神活動力良好。對無免疫缺陷的健康嬰幼兒（大於3個月），此病為自體限制性，給予電解質口服液與飲食控制等支持性治療即可，不需要且應避免常規使用抗生素，因為抗生素會延長糞便排菌時間並增加帶菌率。",
            "flashcard_front": "1歲幼兒 / 非傷寒沙門氏菌 / 症狀改善且無發燒 / 抗生素治療指引",
            "flashcard_back": "健康且大於3個月幼兒罹患此病，只需「支持性飲食治療，無需給與抗生素」，以免延長排菌時間。",
            "flashcard_summary": "非傷寒沙門氏菌腸胃炎處置 -> 症狀改善的健康患兒只需飲食支持，不需抗生素"
        },
        {
            "question_id": "108-1_medicine-4_013",
            "question_number": 13,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "嬰幼兒副食品添加原則與時程。",
            "explanation": "目前兒科醫學指引建議，為建立免疫耐受性並預防過敏，嬰兒在 4-6 個月大時即可開始添加副食品，即使是有過敏體質的嬰兒也不應延後（延後至8個月反而會增加過敏風險），故B選項最不適當。1歲以下嬰兒因免疫系統發育未完全，必須嚴禁食用蜂蜜以防肉毒桿菌中毒。",
            "flashcard_front": "過敏體質嬰兒 / 副食品添加時間 / 蜂蜜限制 / 添加原則",
            "flashcard_back": "過敏體質嬰兒「不需延後」添加副食品，仍建議於4-6個月大開始添加。1歲以下禁食蜂蜜。",
            "flashcard_summary": "過敏體質嬰兒副食品添加時間 -> 不應延後，同樣建議於 4-6 個月大時開始添加"
        },
        {
            "question_id": "108-1_medicine-4_014",
            "question_number": 14,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "純母乳哺育嬰兒的營養補充（維生素與微量元素）。",
            "explanation": "純母乳哺育的嬰兒在出生後 6 個月內一般不需要額外補充氟。母乳雖然含鐵量低，但足月兒體內儲存的鐵可維持 4-6 個月，之後亦需注意鐵質補充；維生素D則建議從出生後即每日補充 400 IU；維生素K則是在新生兒剛出生時由醫院常規注射補充以防出血。",
            "flashcard_front": "純母乳哺育 / 氟補充時間 / 維生素 D 補充 / 鐵質缺乏風險",
            "flashcard_back": "純母乳哺育嬰兒在「出生6個月內無需補充氟」。出生後需立即每日補充維生素D 400 IU。",
            "flashcard_summary": "純母乳哺育氟補充規範 -> 出生後 6 個月內無需額外補充氟"
        },
        {
            "question_id": "108-1_medicine-4_015",
            "question_number": 15,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "Alport 症候群的臨床表徵與遺傳病史。",
            "explanation": "10歲女童在感冒（上呼吸道感染）後 1-2 天內快速出現肉眼可見血尿，且其舅舅在國中時即因末期腎臟病而接受透析，此顯著的家族男性早期腎衰竭病史高度提示 X 染色體聯鎖隱性遺傳的 Alport 症候群（IV型膠原蛋白突變）。薄基底膜疾病預後佳、極少進展至腎衰竭；IgA腎膜炎雖也有感冒後血尿，但如此明確的家族透析病史更支持 Alport 症候群。",
            "flashcard_front": "感冒後1-2天血尿 / 舅舅年輕透析病史 / 血尿合併蛋白尿 / 遺傳性腎病",
            "flashcard_back": "應診斷為「Alport症候群」。此為IV型膠原蛋白基因缺陷，X-linked隱性遺傳，男性患者易年輕進展至ESRD。",
            "flashcard_summary": "感冒後快速血尿伴男性家族成員早期洗腎史 -> Alport 症候群"
        }
    ]
}

# =====================================================================
# 108-1_medicine-4_batch-002
# =====================================================================
batch_data["108-1_medicine-4_batch-002"] = {
    "dataset_id": "108-1_medicine-4",
    "batch_id": "108-1_medicine-4_batch-002",
    "items": [
        {
            "question_id": "108-1_medicine-4_016",
            "question_number": 16,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "小兒腎病症候群高血脂的臨床治療原則。",
            "explanation": "3歲女童呈現典型小兒微小病變（MCD）引起的腎病症候群（水腫、重度蛋白尿、低白蛋白血症及高血脂）。其高血脂是因低蛋白血症刺激肝臟代償性合成脂蛋白所致，一般在給予類固醇治療、蛋白尿緩解且血中白蛋白回升後即會自行恢復，不需且不應立即使用 Statin 類降血脂藥物治療，故A選項敘述錯誤。",
            "flashcard_front": "小兒腎病症候群 / MCD / 白蛋白 1.5 / 膽固醇 420 / 降血脂治療",
            "flashcard_back": "腎病症候群之高血脂不需立即使用Statin；應先給予類固醇治療，蛋白尿緩解後血脂通常會自行恢復正常。",
            "flashcard_summary": "小兒腎病症候群高血脂處置 -> 先以類固醇治療原發病症，不需立即使用 Statin 降血脂"
        },
        {
            "question_id": "108-1_medicine-4_017",
            "question_number": 17,
            "correct_answer": "B",
            "category_group": "醫學（四")",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "幼兒動作及語言發展里程碑判斷。",
            "explanation": "幼兒發展評估中，能夠不扶東西單腳站立 10 秒（粗動作）、能模仿畫出圓圈（細動作）以及能使用代名詞表達「你的」、「我的」（語言與社會性），其最接近的發展年齡為滿 3 歲但未滿 4 歲（3歲至3歲半左右的里程碑）。滿4歲通常能單腳跳躍或畫正方形；滿2歲發展則尚未成熟至單腳站立10秒。",
            "flashcard_front": "單腳站立10秒 / 照樣畫圓 / 表達「你的」「我的」 / 發展年齡",
            "flashcard_back": "符合這些發展里程碑的幼兒，其年齡最接近「滿 3 歲但未滿 4 歲」。",
            "flashcard_summary": "單腳站立10秒與畫圓之發展年齡 -> 滿 3 歲但未滿 4 歲"
        },
        {
            "question_id": "108-1_medicine-4_018",
            "question_number": 18,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "小兒熱性痙攣的評估原則與腰椎穿刺適應症。",
            "explanation": "年紀小於6個月的嬰兒若出現發燒合併痙攣，由於腦膜炎症狀在該年齡層常不典型，強烈建議進行腰椎穿刺以排除中樞神經感染。複雜型熱性痙攣病童日後罹患癲癇機率高於一般人；首次發生的單純型熱性痙攣不需常規安排神經影像學檢查；熱性痙攣與遺傳及家族史有高度相關。",
            "flashcard_front": "嬰幼兒發燒抽搐 / 小於6個月 / 腰椎穿刺 / 癲癇風險",
            "flashcard_back": "小於6個月之熱性痙攣患者，「須做腰椎穿刺以排除腦膜炎」；首次單純型熱性痙攣不需常規影像檢查。",
            "flashcard_summary": "小於6個月發燒痙攣處理 -> 須做腰椎穿刺排除中樞神經感染"
        },
        {
            "question_id": "108-1_medicine-4_019",
            "question_number": 19,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "中樞性與周邊性性早熟的致病機轉區分。",
            "explanation": "下視丘錯構瘤（Hypothalamic hamartoma）會提早分泌 GnRH，進而活化下視丘-腦下垂體-性腺軸，屬於「中樞性（GnRH依賴性）性早熟」。相較之下，外源性雌激素接觸、先天性腎上腺增生（CAH）及 McCune-Albright 症候群均是不依賴 GnRH 的「周邊性（非GnRH依賴性）性早熟」，故D選項機轉與其他最不相同。",
            "flashcard_front": "女童性早熟 / 下視丘錯構瘤 / McCune-Albright / 先天性腎上腺增生 / 機轉分類",
            "flashcard_back": "下視丘錯構瘤屬於「中樞性（GnRH依賴性）」性早熟，而其餘選項均為「周邊性」性早熟。",
            "flashcard_summary": "下視丘錯構瘤引發性早熟機轉 -> 屬於中樞性性早熟，其餘為周邊性"
        },
        {
            "question_id": "108-1_medicine-4_020",
            "question_number": 20,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "先天性腎上腺增生（CAH）的最常見酵素缺乏型別。",
            "explanation": "先天性腎上腺增生（CAH）是由於類固醇合成路徑中特定酵素缺乏所致，其中以 21-hydroxylase 缺乏症最為常見（佔90%以上）。而在 21-hydroxylase 缺乏症中，又以非典型（nonclassic type）的盛行率最高，常在青春期後以高雄性素表現。",
            "flashcard_front": "先天性腎上腺增生 (CAH) / 酵素缺乏 / 盛行率最高型別",
            "flashcard_back": "CAH最常見的酵素缺陷型別是「21-hydroxylase deficiency, nonclassic type（非典型21-羥化酶缺乏症）」。",
            "flashcard_summary": "CAH 盛行率最高型別 -> 21-hydroxylase deficiency, nonclassic type"
        },
        {
            "question_id": "108-1_medicine-4_021",
            "question_number": 21,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "類過敏性紫斑症（HSP）的全身性系統侵犯特徵。",
            "explanation": "類過敏性紫斑症（HSP）是一種 IgA 介導的系統性小血管炎。其典型症狀除了下肢非血小板低下性紫斑外，常合併腹痛（嚴重可併發腸套疊）、關節炎/關節痛以及腎臟侵犯（血尿/蛋白尿），故臨床需密切注意這些合併症。它並非以 IgE 為主的過敏，大多數輕症病患只需支持性治療，不需常規使用類固醇。",
            "flashcard_front": "IgA 血管炎 / HSP / 紫斑 / 腹痛 / 關節痛與血尿",
            "flashcard_back": "HSP為IgA介導，臨床上「必須注意是否合併腹痛、關節痛及血尿（腎臟受累）」。大多數病患不需常規使用類固醇。",
            "flashcard_summary": "類過敏性紫斑症（HSP）監測重點 -> 注意是否合併腹痛、關節痛、血尿等系統性侵犯"
        },
        {
            "question_id": "108-1_medicine-4_022",
            "question_number": 22,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "川崎氏症與腸病毒咽峽炎的臨床鑑別診斷。",
            "explanation": "軟顎與扁桃腺出現水泡與潰瘍是腸病毒感染引起的疱疹性咽峽炎（herpangina）的特徵，而非川崎氏症（Kawasaki disease）的表現。川崎氏症的典型診斷標準包含：發燒大於5天，並合併有草莓舌與唇裂、雙眼非化膿性結膜炎、頸部淋巴結腫大、手腳紅腫脫皮以及多形性皮疹等。",
            "flashcard_front": "發燒6天 / 草莓舌 / 雙眼結膜炎 / 喉嚨水泡與潰瘍 / 川崎氏症鑑別",
            "flashcard_back": "「軟顎與扁桃腺水泡潰瘍」為腸病毒特徵，非川崎氏症表現；後者表現為草莓舌與唇部龜裂紅腫。",
            "flashcard_summary": "不屬於川崎氏症的臨床表徵 -> 軟顎與扁桃腺出現水泡與潰瘍（提示為腸病毒）"
        },
        {
            "question_id": "108-1_medicine-4_023",
            "question_number": 23,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "小兒呼吸道異物吸入的臨床診斷要點。",
            "explanation": "2歲病童在玩耍跑動時突發持續咳嗽，聽診呈現「單側」喘鳴音（wheezing），且給予支氣管擴張劑治療後喘鳴音完全沒有改善，這些特徵高度提示為氣道異物阻塞（Airway foreign body obstruction）。此時切勿誤診為氣喘或細支氣管炎，應儘速安排支氣管鏡檢以取出異物。",
            "flashcard_front": "玩耍後突發咳嗽 / 單側喘鳴音 / 支氣管擴張劑無效 / 2歲幼兒",
            "flashcard_back": "突發單側喘鳴且支氣管擴張劑無效，高度提示「氣道異物阻塞」，應安排支氣管鏡檢查。",
            "flashcard_summary": "突發單側喘鳴且支氣管擴張劑無效 -> 氣道異物阻塞（Airway foreign body obstruction）"
        },
        {
            "question_id": "108-1_medicine-4_024",
            "question_number": 24,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "嬰幼兒過敏預防的母親飲食原則與最新醫學共識。",
            "explanation": "最新的國際過敏預防指引指出，母親在懷孕及哺乳期間「不需要」特別避免食用高過敏食物（如海鮮、花生等），過度限制飲食反而可能導致母嬰營養不良，且微量接觸有助於嬰兒建立免疫耐受性，故D選項最不恰當。添加副食品以4-6個月大為宜，益生菌亦不建議常規用於預防過敏。",
            "flashcard_front": "過敏預防 / 哺乳媽媽飲食限制 / 4-6個月副食品 / 益生菌預防過敏",
            "flashcard_back": "母乳餵哺期間，母親「不需要避免食用高過敏食物」。常規避開高過敏食物無助於預防嬰兒過敏。",
            "flashcard_summary": "哺乳期過敏預防飲食原則 -> 母親不需避免食用高過敏食物"
        },
        {
            "question_id": "108-1_medicine-4_025",
            "question_number": 25,
            "correct_answer": "",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "漏斗胸的流行病學與病理生理特徵（本題官方公佈無正解）。",
            "explanation": "本題官方更正為無正解（一律給分）。漏斗胸（Funnel chest）在流行病學上是「男孩發生率顯著高於女孩」（約3-4:1），因此B選項稱女孩較高是錯誤的；此外，漏斗胸病患的肺功能檢查主要為正常或呈現輕度限制性通氣障礙，阻塞性異常（C選項）同樣較罕見。美觀常為手術考量主因之一。",
            "flashcard_front": "漏斗胸 (Funnel chest) / 男女性別比 / 肺功能檢查型態 / 官方更正答案",
            "flashcard_back": "本題無正解。漏斗胸是「男孩發生率高於女孩（約3~4:1）」；肺功能以限制性障礙為主而非阻塞性。",
            "flashcard_summary": "漏斗胸特徵說明（無正解） -> 男孩發生率高於女孩，肺功能以限制性障礙為主"
        },
        {
            "question_id": "108-1_medicine-4_026",
            "question_number": 26,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "小兒猛爆性肝衰竭的臨床評估與處置原則。",
            "explanation": "當肝病病童發生疑似猛爆性肝衰竭且凝血時間（PT/aPTT）延長時，應給予維生素K治療以排除因維生素K缺乏所致的凝血因子（II, VII, IX, X）合成不足。AST/ALT數值的高低並不與肝衰竭嚴重度成正比（有時肝細胞大片壞死後轉氨酶反而下降）；白蛋白低下合併腹水應限水限鈉並使用利尿劑，盲目給予大量維持性點滴會加重腹水；肝腦病變二期尚不需立即插管。",
            "flashcard_front": "猛爆性肝衰竭 / 凝血時間延長 / 維生素 K / AST與ALT嚴重度 / 腹水處置",
            "flashcard_back": "凝血時間（PT/aPTT）延長時，應首選「給予維生素K」治療。AST/ALT數值高低不能用來判斷肝衰竭的嚴重度。",
            "flashcard_summary": "猛爆性肝衰竭凝血異常處置 -> 凝血時間延長應先給予維生素K治療"
        },
        {
            "question_id": "108-1_medicine-4_027",
            "question_number": 27,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "主動脈弓窄縮伴隨開放性動脈導管的血氧特徵。",
            "explanation": "2天大足月新生兒，右手血氧飽和度正常（98%），但雙側下肢血氧降至 90%，此臨床表現稱為導管後發紺（post-ductal cyanosis）。此現象是由於主動脈弓窄縮（CoA）造成體循環受阻，下肢的血流主要依賴肺動脈右向左分流、經由開放性動脈導管（PDA）輸送而來的缺氧血，B選項為最典型診斷。",
            "flashcard_front": "右手血氧98% / 下肢血氧90% / 導管後發紺 (post-ductal cyanosis) / 新生兒",
            "flashcard_back": "此為導管後發紺，提示為「主動脈弓窄縮合併開放性動脈導管（CoA + PDA）」致使下肢主要接收分流缺氧血。",
            "flashcard_summary": "上下肢血氧差異（右手正常下肢發紺） -> 主動脈弓窄縮合併開放性動脈導管（CoA with PDA）"
        },
        {
            "question_id": "108-1_medicine-4_028",
            "question_number": 28,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "小兒生理性/功能性心雜音的特徵區分。",
            "explanation": "兒童常見的功能性（生理性）心雜音通常較小聲，強度多在第 1 至 3 級之間。若心雜音強度達到第 4 級以上（通常伴有觸覺震顫 thrill），高度提示為病理性心雜音，不可能是功能性雜音。功能性心雜音通常僅在收縮期出現，且會隨呼吸或姿勢改變而變化。",
            "flashcard_front": "功能性心雜音 / 生理性 / 心雜音分級限制 / 收縮期雜音",
            "flashcard_back": "功能性心雜音強度「不會達到第4級（多小於等於3級）」且無震顫；它必為「收縮期雜音」，舒張期雜音必為病理性。",
            "flashcard_summary": "不屬於功能性心雜音的特徵 -> 心雜音強度達第 4 級（提示為病理性）"
        },
        {
            "question_id": "108-1_medicine-4_029",
            "question_number": 29,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "前列腺素 E1（PGE1）在動脈導管相依型心臟病的應用限制。",
            "explanation": "前列腺素 E1（PGE1）常用於維持動脈導管開放，以保障肺循環或體循環相依型先天性心臟病的血流。然而，在阻塞型全肺靜脈回流異常（TAPVR with obstruction）中，病因是肺靜脈回流左心房受阻，導致嚴重肺淤血，此時維持動脈導管開放不僅無法解決阻塞，還可能因右向左分流加重發紺，對病情毫無幫助（首選為緊急外科手術）。",
            "flashcard_front": "前列腺素 E1 (PGE1) / 動脈導管 (PDA) 開放 / 全肺靜脈回流異常 / 主動脈弓窄縮",
            "flashcard_back": "PGE1維持動脈導管開放在「阻塞型全肺靜脈回流異常（TAPVR with obstruction）」中最無幫助，應儘速手術解決定障礙。",
            "flashcard_summary": "PGE1 治療最無幫助的先天性心臟病 -> 阻塞型全肺靜脈回流異常（TAPVR with obstruction）"
        },
        {
            "question_id": "108-1_medicine-4_030",
            "question_number": 30,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "體染色體隱性遺傳疾病的帶因機率計算。",
            "explanation": "Phenylketonuria 屬於體染色體隱性遺傳疾病（AR）。女嬰確診代表其基因型為 aa，其無症狀的父母必定皆為帶因者（Aa x Aa）。其哥哥和姊姊目前發育正常且無症狀，代表他們已排除了是患者（aa）的可能性，因此他們在 Aa x Aa 雜交子代中，帶有突變基因（Aa）的機率為 2/3。",
            "flashcard_front": "體染色體隱性 (AR) / 患病妹妹 aa / 無症狀兄姐 / 帶因機率計算",
            "flashcard_back": "在AR遺傳中，父母均為帶因者，其無症狀子代為帶因者的機率「皆為 2/3」（已扣除患者aa的可能）。",
            "flashcard_summary": "隱性遺傳無症狀同胞之帶因機率 -> 皆為 2/3"
        }
    ]
}

# =====================================================================
# 108-1_medicine-4_batch-003
# =====================================================================
batch_data["108-1_medicine-4_batch-003"] = {
    "dataset_id": "108-1_medicine-4",
    "batch_id": "108-1_medicine-4_batch-003",
    "items": [
        {
            "question_id": "108-1_medicine-4_031",
            "question_number": 31,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "臺灣新生兒代謝異常篩檢的採血時程與方法。",
            "explanation": "臺灣現行新生兒代謝異常篩檢，其採血時間為「出生滿 48 小時或餵奶滿 24 小時後」，並非在出生一天以內，故A選項敘述錯誤。太早採血會因嬰兒尚未充分攝取奶水，使體內異常代謝物累積不足而導致檢測出現偽陰性。目前串聯質譜儀（Tandem mass spectrometry）是主要的篩檢工具。",
            "flashcard_front": "新生兒代謝異常篩檢 / 腳跟血採血時程 / 串聯質譜儀 / 偽陰性預防",
            "flashcard_back": "代謝篩檢採血應在「出生滿 48 小時或餵奶24小時後」進行，出生一天內採血太早易造成偽陰性。",
            "flashcard_summary": "新生兒代謝篩檢錯誤描述 -> 剛出生的寶寶需一天內採腳跟血檢測"
        },
        {
            "question_id": "108-1_medicine-4_032",
            "question_number": 32,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "常見遺傳性疾病的基因遺傳模式判定。",
            "explanation": "附圖之遺傳譜系呈現男女均有罹病機率，且有隔代或同胞發病的特徵，符合體染色體隱性（AR）遺傳模式。在庫利氏貧血（Cooley anemia，即重型乙型海洋性貧血）中，其遺傳模式正是體染色體隱性遺傳。軟骨發育不全與結節性硬化症為體染色體顯性（AD）遺傳；DMD則為X染色體聯鎖隱性遺傳。",
            "flashcard_front": "體染色體隱性遺傳 (AR) / 庫利氏貧血 / 軟骨發育不全 / 遺傳譜系判定",
            "flashcard_back": "重型乙型海洋性貧血（庫利氏貧血）為「體染色體隱性（AR）」遺傳；軟骨發育不全為顯性（AD）。",
            "flashcard_summary": "體染色體隱性遺傳疾病範例 -> 庫利氏貧血（Cooley anemia）"
        },
        {
            "question_id": "108-1_medicine-4_033",
            "question_number": 33,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "小兒科",
            "category_confidence": "high",
            "key_point": "青少年急性睪丸扭轉的急診處置原則。",
            "explanation": "15歲男生突發半夜左側睪丸劇痛並伴有自主神經症狀（臉色蒼白、冷汗），高度懷疑為急性睪丸扭轉。睪丸扭轉的黃金挽救時間通常在症狀發生後 6 小時內。在缺乏即時超音波檢查的情況下，為避免睪丸缺血壞死，臨床常規應直接進行緊急「睪丸探查手術（testicular exploration）」以爭取復位時間。",
            "flashcard_front": "15歲男生 / 半夜睪丸劇痛 / 睪丸扭轉 / 無超音波急診處置",
            "flashcard_back": "高度懷疑睪丸扭轉時，應立即安排「睪丸探查手術（exploration）」，切勿因等待檢查或給予抗生素而延誤復位黃金期。",
            "flashcard_summary": "疑似睪丸扭轉之緊急處置 -> 在缺乏即時影像檢查時，應直接行睪丸探查手術"
        },
        {
            "question_id": "108-1_medicine-4_034",
            "question_number": 34,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "脂漏性皮膚炎的病因與藥物治療。",
            "explanation": "脂漏性皮膚炎的好發部位為頭皮、眉毛及鼻翼兩側等皮脂腺豐富區域，其發病常與皮膚上的馬拉色菌（Malassezia，一種黴菌）過度增殖及免疫反應有關。因此，外用抗黴菌藥物（如 Ketoconazole 藥膏或洗劑）是臨床上非常有效且常用的治療手段，C選項敘述錯誤。",
            "flashcard_front": "脂漏性皮膚炎 / 馬拉色菌 (Malassezia) / 好發部位 / 抗黴菌藥物效果",
            "flashcard_back": "脂漏性皮膚炎的發病與皮屑芽孢菌有關，「外用抗黴菌藥物能有效治療」此病；病程頑固者需排除HIV感染。",
            "flashcard_summary": "脂漏性皮膚炎治療錯誤描述 -> 外用抗黴菌藥物不能有效治療脂漏性皮膚炎"
        },
        {
            "question_id": "108-1_medicine-4_035",
            "question_number": 35,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "類天疱瘡（Bullous pemphigoid）的流行病學與病理特徵。",
            "explanation": "類天疱瘡（Bullous pemphigoid, BP）是一種自體免疫表皮下水疱病，好發於「老年人」（通常大於60歲），在年輕人中非常罕見，故A選項敘述錯誤。其初期常以劇癢的蕁麻疹樣紅斑表現，水疱多為張力性，病理切片下可見表皮下水疱，並有大量嗜伊紅球浸潤，治療以類固醇為主。",
            "flashcard_front": "類天疱瘡 (Bullous pemphigoid) / 好發年齡 / 表皮下水疱 / 嗜伊紅球浸潤",
            "flashcard_back": "類天疱瘡主要好發於「老年人」，而非年輕人。水疱壁厚呈張力性，病理可見大量嗜伊紅球浸潤。",
            "flashcard_summary": "類天疱瘡流行病學錯誤描述 -> 常發生於年輕人（實為好發於老年人）"
        },
        {
            "question_id": "108-1_medicine-4_036",
            "question_number": 36,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "類澱粉性苔癬（Lichen amyloidosis）的病理診斷特徵。",
            "explanation": "病患背部與四肢出現慢性發癢之丘疹，皮膚切片在 Congo red 染色下，於真皮乳頭層見到類澱粉蛋白沉積；在偏光顯微鏡下觀察會呈現特異性的蘋果綠雙折射（apple-green birefringence），這些都是類澱粉性苔癬（lichen amyloidosis）的典型病理診斷特徵。",
            "flashcard_front": "發癢皮疹 / Congo red 染色 / 偏光顯微鏡 / 蘋果綠雙折射",
            "flashcard_back": "Congo red 染色在偏光顯微鏡下呈蘋果綠雙折射，是「類澱粉性苔癬（Lichen amyloidosis）」的特異性診斷特徵。",
            "flashcard_summary": "Congo red 染偏光呈蘋果綠之診斷 -> 類澱粉性苔癬（lichen amyloidosis）"
        },
        {
            "question_id": "108-1_medicine-4_037",
            "question_number": 37,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "貼膚試驗（Patch testing）的臨床應用目的。",
            "explanation": "貼膚試驗（Patch testing）是用於診斷接觸性過敏原引起的第IV型（遲發性）超敏反應，其主要臨床目的是為了幫患者「找出特定的接觸性過敏原」，進而在日常生活中避免接觸。它無法用來確診所有類型的接觸性皮膚炎（如刺激性接觸性皮膚炎即無法以此確診）。",
            "flashcard_front": "貼膚試驗 (Patch testing) / 接觸性皮膚炎 / 診斷目的 / 第 IV 型超敏反應",
            "flashcard_back": "貼膚試驗的主要目的為「找出遲發性接觸過敏原」，非用來判定嚴重度或確診非過敏性皮膚炎。",
            "flashcard_summary": "貼膚試驗的主要目的 -> 找出接觸性過敏原"
        },
        {
            "question_id": "108-1_medicine-4_038",
            "question_number": 38,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "兒童異位性皮膚炎的臨床特徵與家族史關聯。",
            "explanation": "6歲男孩自幼兒期（2歲）起即反覆在關節屈側等處出現劇癢皮膚病變，且雙親均有過敏性鼻炎病史（強烈的異位性體質家族史）。這些特徵完全符合異位性皮膚炎（Atopic dermatitis）的典型診斷。脂漏性皮膚炎與接觸性皮膚炎多無如此顯著的慢性反覆發作與遺傳傾向。",
            "flashcard_front": "2歲起反覆劇癢 / 肘窩或膝窩病灶 / 父母過敏性鼻炎家族史",
            "flashcard_back": "此為典型的「異位性皮膚炎（Atopic dermatitis）」，與遺傳過敏體質（atopy）密切相關。",
            "flashcard_summary": "幼年起反覆劇癢皮膚病變合併過敏家族史 -> 異位性皮膚炎"
        },
        {
            "question_id": "108-1_medicine-4_039",
            "correct_answer": "D",
            "question_number": 39,
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "常見水疱性皮膚疾病的 Nikolsky sign 反應區分。",
            "explanation": "Nikolsky sign 是以手指輕推水疱旁皮膚時，若表皮輕易剝離或水疱擴大即為陽性，代表表皮細胞內鬆解（如尋常性天疱瘡 pemphigus vulgaris、SSSS、SJS）。類天疱瘡（bullous pemphigoid）由於是自體抗體攻擊半抗原、導致「表皮下」水疱，其水疱壁厚實且緊繃，故 Nikolsky sign 為陰性。",
            "flashcard_front": "Nikolsky sign 陰性 / 表皮下水疱 / 天疱瘡與類天疱瘡比較",
            "flashcard_back": "「類天疱瘡（bullous pemphigoid）」因為是表皮下水疱，Nikolsky sign呈陰性；而天疱瘡呈陽性。",
            "flashcard_summary": "Nikolsky sign呈陰性的水疱病 -> 類天疱瘡（bullous pemphigoid）"
        },
        {
            "question_id": "108-1_medicine-4_040",
            "question_number": 40,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "中毒性休克症候群（TSS）的病原體與致病毒素。",
            "explanation": "中毒性休克症候群（TSS）主要由金黃色葡萄球菌（Staphylococcus aureus）產生的超抗原毒素 TSST-1 或鏈球菌產生的外毒素引起，並非由 Pseudomonas（綠膿桿菌）產生的剝脫性毒素（exfoliative toxin）引起，故D選項錯誤。剝脫性毒素是由金黃色葡萄球菌產生，且與 SSSS 相關。",
            "flashcard_front": "Toxic shock syndrome (TSS) / 超抗原毒素 / 金黃色葡萄球菌 / 剝脫性毒素關係",
            "flashcard_back": "TSS主要由「金黃色葡萄球菌的 TSST-1」或鏈球菌毒素引起，而非綠膿桿菌或剝脫性毒素（exfoliative toxin）。",
            "flashcard_summary": "TSS致病機轉錯誤描述 -> 主要致病機轉為 Pseudomonas 製造的 exfoliative toxin 所引起"
        },
        {
            "question_id": "108-1_medicine-4_041",
            "question_number": 41,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "青年型皮肌炎與惡性腫瘤關聯性的特徵。",
            "explanation": "成人型皮肌炎（dermatomyositis）與惡性腫瘤（如鼻咽癌、乳癌、肺癌等）有相當高的關聯性；但青年型皮肌炎（juvenile dermatomyositis, JDM）在病因與預後上與成人不同，其極少併發惡性腫瘤，故D選項錯誤。JDM 易合併皮膚鈣化症（calcinosis cutis）及血管病變。",
            "flashcard_front": "青年型皮肌炎 (JDM) / 成人型皮肌炎比較 / 皮膚鈣化 / 惡性腫瘤關聯",
            "flashcard_back": "青年型皮肌炎（JDM）「極少併發惡性腫瘤（如鼻咽癌）」，此特徵與成人型皮肌炎高度伴隨癌症不同。",
            "flashcard_summary": "青年型皮肌炎特徵錯誤描述 -> 易併發鼻咽癌"
        },
        {
            "question_id": "108-1_medicine-4_042",
            "question_number": 42,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "汗斑對皮膚色素沉著的影響與機轉。",
            "explanation": "汗斑（pityriasis versicolor）是由皮屑芽孢菌感染所致，該菌產生的壬二酸（azelaic acid）會抑制黑色素細胞的活性，因此汗斑在臨床上既可表現為膚色變深的紅褐色斑塊，亦可表現為膚色變淺的「脫色斑（低色素沉著）」，B選項稱只會變深是錯誤的。",
            "flashcard_front": "汗斑 (Tinea versicolor) / 壬二酸 (azelaic acid) / 膚色變深或變淺 / 黑色素抑制",
            "flashcard_back": "汗斑因馬拉色菌分泌壬二酸抑制黑色素，「既可使膚色變深亦可使膚色變淺」，並非只會變深。",
            "flashcard_summary": "汗斑對膚色影響錯誤描述 -> 汗斑只會造成膚色變深，不會變淺"
        },
        {
            "question_id": "108-1_medicine-4_043",
            "question_number": 43,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "真皮與表皮黑色素沉著的雷射治療原理。",
            "explanation": "真皮層的黑色素因為位於皮膚深層，脈衝光（IPL）因波長較短且能量穿透力有限，療效極差；而釹雅各（Nd:YAG）雷射（特別是1064 nm波長）具有極佳的深層穿透力，是治療真皮層黑色素沉著的首選。因此B選項稱脈衝光效果較好是錯誤的。",
            "flashcard_front": "真皮層黑色素 / 雷射治療選擇 / 釹雅各 (Nd:YAG) / 脈衝光 (IPL) 比較",
            "flashcard_back": "治療真皮層深部黑色素應選用穿透力強的「釹雅各雷射」，而非穿透力有限的脈衝光（IPL）。",
            "flashcard_summary": "真皮層黑色素沉著治療錯誤描述 -> 真皮層色素使用脈衝光比釹雅各雷射效果更好"
        },
        {
            "question_id": "108-1_medicine-4_044",
            "question_number": 44,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "卡波西氏肉瘤（Kaposi's sarcoma）的臨床與病理特徵。",
            "explanation": "75歲老年男性逐漸在足部出現紫色血管性斑塊，病理切片顯示真皮層內有梭形細胞（spindle cells）及裂隙狀、篩板狀（sieve-like）血管腔增生，並有紅血球外滲，這是典型的卡波西氏肉瘤（Kaposi's sarcoma）病理特徵。血管肉瘤多呈高度惡性且篩板狀增生較不典型；血管角化瘤通常無此篩板樣血管侵犯。",
            "flashcard_front": "足部紫色斑塊 / 老年男性 / 篩板狀血管增生 / 裂隙腔",
            "flashcard_back": "此臨床與病理特徵最符合「卡波西氏肉瘤（Kaposi's sarcoma）」。其病理特徵為梭形細胞與篩板狀裂隙血管增生。",
            "flashcard_summary": "足部紫色斑塊合併篩板狀血管增生之診斷 -> 卡波西氏肉瘤（Kaposi's sarcoma）"
        },
        {
            "question_id": "108-1_medicine-4_045",
            "question_number": 45,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "皮膚科",
            "category_confidence": "high",
            "key_point": "卡波西氏肉瘤與病毒感染的關聯性。",
            "explanation": "卡波西氏肉瘤（Kaposi's sarcoma）的發生與人類皰疹病毒第八型（HHV-8，又稱卡波西氏肉瘤相關皰疹病毒 KSHV）感染有絕對的因果關係。不論是經典型、流行型（AIDS相關）或醫源性（免疫抑制相關）的卡波西氏肉瘤，均可在病灶內偵測到 HHV-8 的 DNA。",
            "flashcard_front": "卡波西氏肉瘤 / 皰疹病毒 / HHV-8 / 臨床相關病毒",
            "flashcard_back": "卡波西氏肉瘤的發生與「人類皰疹病毒第八型（HHV-8）」感染密切相關，又稱 KSHV。",
            "flashcard_summary": "與卡波西氏肉瘤相關之病毒 -> 人類皰疹病毒第八型（HHV-8）"
        }
    ]
}

# =====================================================================
# 108-1_medicine-4_batch-004
# =====================================================================
batch_data["108-1_medicine-4_batch-004"] = {
    "dataset_id": "108-1_medicine-4",
    "batch_id": "108-1_medicine-4_batch-004",
    "items": [
        {
            "question_id": "108-1_medicine-4_046",
            "question_number": 46,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "醒後中風（Wake-up stroke）的急性期處理原則。",
            "explanation": "患者在睡醒後被發現偏癱、失語，由於無法確定確切發病時間，臨床上應將最後正常時間（前晚10點，已超過12小時）視為發病起點。這已遠超出靜脈血栓溶解（IV tPA）的黃金3-4.5小時時效視窗，故此時急性期最適當的藥物治療為給予抗血小板藥物（antiplatelets，如 Aspirin）以預防血栓擴大。",
            "flashcard_front": "睡醒發現中風 / 發病時間未知 / 超出黃金時效 / 急性期用藥",
            "flashcard_back": "對於醒後中風（wake-up stroke），因無法確定時間且多超出時效，禁用 tPA；「急性期首選抗血小板藥物（antiplatelet）」治療。",
            "flashcard_summary": "醒後中風急性期處置 -> 給予抗血小板藥物（antiplatelets），禁用靜脈溶栓"
        },
        {
            "question_id": "108-1_medicine-4_047",
            "question_number": 47,
            "correct_answer": "",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "蜘蛛膜下腔出血（SAH）最常見病因的判定（本題官方公佈無正解）。",
            "explanation": "本題官方更正為無正解（一律給分）。蜘蛛膜下腔出血（SAH）若指「自發性（非外傷性）」，最常見病因為腦囊狀動脈瘤破裂（約占80-85%）；但若將所有原因計入，最常見的原因其實是「頭部外傷（trauma）」。因題目語意未指明自發性或外傷性，導致選項 A 與 C 均有其正確性，故官方予以全部給分。",
            "flashcard_front": "蜘蛛膜下腔出血 (SAH) / 腦動脈瘤破裂 / 頭部外傷 / 最常見病因 (無正解)",
            "flashcard_back": "本題無正解。自發性SAH主因為「囊狀動脈瘤破裂」；但整體SAH最常見原因為「頭部外傷（trauma）」。",
            "flashcard_summary": "SAH最常見病因說明（無正解） -> 自發性以囊狀動脈瘤破裂居多，全因則以頭部外傷最常見"
        },
        {
            "question_id": "108-1_medicine-4_048",
            "question_number": 48,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "腦靜脈竇栓塞（CVST）的最常見臨床症狀。",
            "explanation": "腦靜脈竇栓塞（Cerebral venous sinus thrombosis, CVST）是由於腦靜脈迴流受阻引起顱內壓增高。其最常見（大於90%）的臨床表現為急性或亞急性「頭痛（headache）」，常伴有視乳頭水腫。局灶性神經缺損（如偏癱、複視）與意識障礙亦可出現，但盛行率均低於頭痛。",
            "flashcard_front": "腦靜脈竇栓塞 (CVST) / 顱內壓增高 / 臨床表現 / 最常見首發症狀",
            "flashcard_back": "CVST最常見且幾乎都會出現的臨床表現是「頭痛（headache）」，多因顱內壓增高所致。",
            "flashcard_summary": "腦靜脈竇栓塞（CVST）最常見症狀 -> 頭痛（headache）"
        },
        {
            "question_id": "108-1_medicine-4_049",
            "question_number": 49,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "快速動眼期睡眠行為疾患（RBD）的臨床特徵與神經退化預測。",
            "explanation": "快速動眼期（REM）睡眠多集中在後半夜，因此快速動眼期睡眠行為疾患（RBD）的異常動作多發生在後半夜，且夢境多為不愉快或暴力的。RBD 患者日後極高機率發展為「突觸核蛋白病變（α-synucleinopathy）」，如巴金森氏症或路易氏體失智症，而非阿茲海默氏症。",
            "flashcard_front": "REM 睡眠行為異常 (RBD) / 後半夜發作 / 夢境特徵 / 日後神經退化疾病",
            "flashcard_back": "RBD「通常在後半夜出現」（因REM睡眠集中於此時），日後極易發展為「巴金森氏症或路易氏體失智症」而非阿茲海默氏症。",
            "flashcard_summary": "RBD 臨床特色與預後 -> 異常動作多在後半夜出現，日後易發展為巴金森氏症"
        },
        {
            "question_id": "108-1_medicine-4_050",
            "question_number": 50,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "青少年肌陣攣性癲癇（JME）的臨床與診斷特徵。",
            "explanation": "14歲智力正常女孩，有癲癇家族史，晨起常有不自主肢體抽搐跌倒，此為青少年肌陣攣性癲癇（Juvenile Myoclonic Epilepsy, JME）的典型症狀，而非「兒童失神性癲癇」（後者表現為短暫發呆、斷片，無肢體抽搐）。JME 腦波特徵為 4-6 Hz 廣泛性多棘慢波，首選藥物為 Valproate。",
            "flashcard_front": "14歲女孩 / 晨起肢體抽搐跌倒 / 4-6Hz 棘波 / 癲癇診斷與藥物",
            "flashcard_back": "此表現應診斷為「青少年肌陣攣性癲癇（JME）」，而非兒童失神性癲癇。首選治療藥物為「Valproate」。",
            "flashcard_summary": "晨起抽搐且腦波見4-6Hz棘波之診斷 -> 青少年肌陣攣性癲癇（JME），非失神性癲癇"
        },
        {
            "question_id": "108-1_medicine-4_051",
            "question_number": 51,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "偏頭痛（Migraine）的臨床診斷標準。",
            "explanation": "依據 ICHD-3 偏頭痛診斷標準，偏頭痛每次發作持續 4-72 小時，特徵為單側、搏動性、中重度頭痛，日常活動會加劇，並常伴有噁心、嘔吐或畏光怕吵。而「流淚及眼結膜充血」是三叉自主神經頭痛（如叢集性頭痛 cluster headache）的典型特徵，不屬於偏頭痛的診斷標準。",
            "flashcard_front": "偏頭痛診斷標準 / 每次持續時間 / 噁心嘔吐 / 流淚與眼結膜充血",
            "flashcard_back": "偏頭痛不包含「流淚及眼結膜充血」（此為叢集性頭痛特徵）。每次發作持續時間為 4-72 小時。",
            "flashcard_summary": "不屬於偏頭痛診斷標準的特徵 -> 伴隨流淚及眼結膜充血（為三叉自主神經頭痛特徵）"
        },
        {
            "question_id": "108-1_medicine-4_052",
            "question_number": 52,
            "correct_answer": "B",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "瞻妄與失智症的關鍵臨床鑑別診斷。",
            "explanation": "瞻妄（delirium）與失智症（dementia）均可表現為認知功能下降、幻覺或行為異常。但兩者最關鍵的區別在於，瞻妄病患會出現「急性的意識波動與注意力不集中（attention deficit）」，且症狀常在一天內有高低起伏，而失智症患者的注意力在早期多能保持相對正常。",
            "flashcard_front": "瞻妄 (delirium) / 失智症 (dementia) / 臨床鑑別點 / 注意力功能",
            "flashcard_back": "兩者最大區別在於瞻妄患者會出現明顯的「注意力（attention）不集中」，且病程呈急性、波動性起伏。",
            "flashcard_summary": "瞻妄與失智症最大鑑別點 -> 瞻妄病人易出現注意力（attention）不集中"
        },
        {
            "question_id": "108-1_medicine-4_053",
            "question_number": 53,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "軟腭肌陣攣與下橄欖核假性肥大之解剖路徑。",
            "explanation": "中腦紅核（red nucleus）附近受損，數月後出現節奏性軟腭向上收縮（軟腭肌陣攣 palatal myoclonus），這是由於 Guillain-Mollaret 三角（齒狀核-紅核-下橄欖核路徑）中斷，導致下橄欖核出現逆行性變性與肥大。此路徑中，左側紅核受損會導致同側「左側下橄欖核（inferior olivary nucleus）」發生肥大，C選項為正確答案。",
            "flashcard_front": "中腦紅核出血 / 軟腭肌陣攣 / Guillain-Mollaret 三角 / 下橄欖核肥大定位",
            "flashcard_back": "一側紅核病變會導致「同側下橄欖核肥大」（左側紅核受損 -> 左側下橄欖核肥大），引起軟腭肌陣攣。",
            "flashcard_summary": "左側紅核病變導致的下橄欖核變化 -> 左側下橄欖核（inferior olivary nucleus）肥大"
        },
        {
            "question_id": "108-1_medicine-4_054",
            "question_number": 54,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "原發性巴金森氏病與非典型巴金森症候群之鑑別點。",
            "explanation": "原發性巴金森氏病（PD）的早期非運動症狀常包括嗅覺減退、不寧腳症候群及快速動眼期睡眠行為異常（RBD）。而「皮質性感覺喪失（cortical sensory loss，如立體覺或兩點辨識覺喪失）」代表大腦頂葉皮質受損，是皮質基底核變性（CBD，一種非典型巴金森症候群）的特徵，而非原發性巴金森氏病表現。",
            "flashcard_front": "巴金森 / 嗅覺減退與 RBD / 皮質性感覺喪失 / 非典型巴金森",
            "flashcard_back": "「皮質性感覺喪失（cortical sensory loss）」提示皮質病變（如CBD），而非原發性巴金森氏病特徵。",
            "flashcard_summary": "非原發性巴金森氏病典型表現 -> 皮質性感覺喪失（提示為皮質基底核變性）"
        },
        {
            "question_id": "108-1_medicine-4_055",
            "question_number": 55,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "運動神經元疾病（MND）的受損系統選擇性。",
            "explanation": "運動神經元疾病（MND，如漸凍症 ALS）是選擇性侵犯皮質、腦幹及脊髓運動神經元的退化性疾病，其感覺系統（痛溫覺、本體感覺）通常完全不受侵犯。而糖尿病多發性神經病變、腕隧道症候群及腰神經根病變，在病理上均會侵犯周邊的混合神經，故常伴隨感覺異常與麻痛。",
            "flashcard_front": "運動神經元病變 (MND) / 感覺系統 / 漸凍症 / 周邊神經根病變比較",
            "flashcard_back": "MND（漸凍症）為「純運動神經侵犯」，其感覺系統最不會受到影響；而神經根病變等則常有感覺症狀。",
            "flashcard_summary": "感覺系統不受侵犯的神經退化疾病 -> 運動神經元病變（motor neuron disease）"
        },
        {
            "question_id": "108-1_medicine-4_056",
            "question_number": 56,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "腰椎椎間盤突出壓迫神經根的典型症狀。",
            "explanation": "30歲男性重度負重（背50公斤沙袋）後突發嚴重腰痛，並伴隨沿右下肢後側放射至腳底的麻痛感，此為典型的坐骨神經痛（特別是壓迫第一薦椎神經根 S1 radiculopathy）。此起病急驟且與負重拉傷密切相關，最可能的診斷為腰椎椎間盤突出（herniation of intervertebral disc）。",
            "flashcard_front": "負重後突發腰痛 / 下肢後側放射至腳底麻痛 / S1 神經根壓迫",
            "flashcard_back": "負重突發腰痛伴隨下肢後側放射至腳底痛麻，應診斷為「腰椎椎間盤突出（HIVD）」。",
            "flashcard_summary": "重負後突發腰痛放射至腳底麻痛 -> 腰椎椎間盤突出（herniation of intervertebral disc）"
        },
        {
            "question_id": "108-1_medicine-4_057",
            "question_number": 57,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "脊髓半切症候群與急性脊髓炎的 MRI 特徵。",
            "explanation": "患者右腳無力，且肚臍以下左側痛溫覺喪失，是典型的脊髓半切症候群（Brown-Séquard syndrome）。在急性脊髓炎的磁振造影（MRI）病灶處，典型表現應為「T2訊號上升（T2-weighted hyperintense，代表水腫與去髓鞘）」，而 T1 訊號多為正常或下降（hypointense），故A選項稱 T1上升、T2不變是錯誤的。",
            "flashcard_front": "Brown-Séquard / 急性脊髓炎 MRI / T1與T2訊號變化 / 視神經檢查",
            "flashcard_back": "急性脊髓炎在MRI的病灶處表現為「T2訊號上升、T1訊號下降或正常」，而非T1上升、T2不變。",
            "flashcard_summary": "急性脊髓炎之 MRI 訊號特徵錯誤描述 -> 磁振造影呈現病灶處 T1 訊號上升、T2 訊號不變"
        },
        {
            "question_id": "108-1_medicine-4_058",
            "question_number": 58,
            "correct_answer": "C",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "神經纖維瘤第一型與第二型（NF1 vs NF2）的臨床症狀區分。",
            "explanation": "神經纖維瘤第一型（NF1）的典型診斷標準包含：6個以上的咖啡牛奶斑、2個以上的皮膚神經纖維瘤、腋窩或腹股溝雀斑以及虹膜色素瘤（Lisch nodules）等。而「雙側聽神經瘤（bilateral acoustic neuromas）」是神經纖維瘤第二型（NF2）的標誌性特徵，不屬於 NF1 的典型症狀。",
            "flashcard_front": "神經纖維瘤 / 咖啡牛奶斑 / Lisch nodule / 雙側聽神經瘤",
            "flashcard_back": "「雙側聽神經瘤」為神經纖維瘤第二型（NF2）之典型特徵，非第一型（NF1）典型表現。",
            "flashcard_summary": "不屬於 NF1 的典型症狀 -> 雙側聽神經瘤（為 NF2 之特徵）"
        },
        {
            "question_id": "108-1_medicine-4_059",
            "question_number": 59,
            "correct_answer": "A",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "視神經脊髓炎（NMOSD）的脊髓病灶長度特徵。",
            "explanation": "視神經脊髓炎（NMOSD）對脊髓的侵犯在 MRI 上常表現為縱向延伸性橫斷性脊髓炎（LETM），其連續病灶長度「通常會超過三個椎骨節段（>=3 segments）」，這是與多發性硬化症（通常小於2個節段）最關鍵的影像學鑑別點。NMOSD 的臨床預後通常比多發性硬化症差，且其脊髓液有時也會出現 oligoclonal band 陽性反應。",
            "flashcard_front": "NMOSD / LETM / 連續脊髓病灶長度 / 多發性硬化症鑑別",
            "flashcard_back": "NMOSD之脊髓病灶在MRI上「常連續侵犯3個椎骨節段以上（LETM）」，此為診斷其重要特徵。",
            "flashcard_summary": "NMOSD 脊髓病灶影像學特徵 -> 對脊髓的侵犯範圍通常可以超過三節以上"
        },
        {
            "question_id": "108-1_medicine-4_060",
            "question_number": 60,
            "correct_answer": "D",
            "category_group": "醫學（四）",
            "category": "神經科",
            "category_confidence": "high",
            "key_point": "神經性梅毒晚期脊髓癆（Tabes dorsalis）的臨床特徵與檢驗限制。",
            "explanation": "神經性梅毒晚期會侵犯脊髓後索與後根，引發脊髓癆（tabes dorsalis），病患會出現刀割般的神經痛、進行性感覺性共濟失調（Proprioceptive loss）及本體感覺喪失。血中 VDRL 效價增高不能單獨確診神經梅毒；FTA-ABS 敏感性高但治癒後仍會呈陽性，不適合監測療效；Argyll-Robertson 瞳孔是光反射消失但「近看（調節）反射仍保存」。",
            "flashcard_front": "神經性梅毒晚期 / 脊髓後索受損 / 刀割痛與共濟失調 / 瞳孔與實驗室限制",
            "flashcard_back": "晚期神經梅毒會引起「脊髓癆（tabes dorsalis）」，表現為本體感覺缺失與刀割般神經痛。VDRL特異性低，無法單獨確診。",
            "flashcard_summary": "神經梅毒晚期脊髓癆之病徵 -> 表現為刀割樣痛、進行性共濟失調及本體感覺缺失"
        }
    ]
}

# =====================================================================
# Write all outputs to reports/gemini_outputs/<batch_id>.json
# =====================================================================
for batch_id, data in batch_data.items():
    output_path = Path("reports/gemini_outputs") / f"{batch_id}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        # Write clean raw JSON without markdown formatting or escape characters
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {output_path}")

print("All batches processed successfully.")
