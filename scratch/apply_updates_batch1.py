import json
import subprocess

updates = [
  {
    "id": "112-1_medicine-3_001",
    "category": "肝膽腸胃科",
    "category_confidence": "high",
    "key_point": "年輕人不明原因肝硬化伴隨血清銅藍蛋白降低應高度懷疑威爾森氏症。",
    "explanation": "【題幹解析】\n患者為19歲女性，無酗酒或病毒性肝炎病史，但已出現肝硬化與下肢浮腫。實驗室檢查顯示血清銅藍蛋白（ceruloplasmin）降低（11.1 mg/dL，正常值 20-60 mg/dL），這是體內銅堆積的特徵性指標，高度指向威爾森氏症。\n\n【選項詳解】\n- A. hemochromatosis（血鐵沉積症）：是因鐵質代謝異常導致體內鐵質過度堆積，好發於中老年男性，診斷通常以血清鐵蛋白（ferritin）與轉鐵蛋白飽和度（transferrin saturation）升高為主。\n- B. amyloidosis（澱粉樣變性）：多見於老年人或伴隨慢性發炎/骨髓瘤的患者，主要表現為器官浸潤（如心臟、腎臟），少以年輕女性單純肝硬化伴隨低銅藍蛋白起病。\n- C. primary biliary cirrhosis（原發性膽汁性膽管炎，現稱 PBC）：典型好發於中年女性，特徵為抗線粒體抗體（AMA）陽性及鹼性磷酸酶（ALP）顯著升高，而非低銅藍蛋白。\n- D. Wilson's disease（威爾森氏症）：為體染色體隱性遺傳疾病，因 ATP7B 基因突變導致銅排出受阻，常於青少年或年輕成人期出現不明原因的急性/慢性肝病、肝硬化、或神經精神症狀，典型血液特徵為血清銅藍蛋白（ceruloplasmin）顯著降低（< 20 mg/dL）。\n\n【核心考點】\n威爾森氏症（Wilson's disease）的臨床特徵（年輕人不明原因肝硬化）、診斷指標（血清銅藍蛋白 ceruloplasmin 降低、24小時尿銅升高等）。",
    "flashcard_front": "年輕女性 / 肝硬化 / ceruloplasmin 降低 / 隱性遺傳",
    "flashcard_back": "年輕患者出現原因不明肝硬化，且血清銅藍蛋白（ceruloplasmin）降低，應優先考慮威爾森氏症（Wilson's disease）。",
    "flashcard_summary": "年輕女性 + 肝硬化 + 銅藍蛋白降低 -> 威爾森氏症 (Wilson's disease)"
  },
  {
    "id": "112-1_medicine-3_002",
    "category": "神經內科",
    "category_confidence": "high",
    "key_point": "偏頭痛常呈現單側搏動性疼痛並伴隨噁心、嘔吐、畏光。",
    "explanation": "【題幹解析】\n本題考查頭痛（Headache）的臨床分類、常見病因與臨床警訊（red flags）。頭痛分為原發性（如緊縮型頭痛、偏頭痛）與次發性（由腦瘤、血管病變、感染等其他疾病引起）。\n\n【選項詳解】\n- A. 原發性頭痛（primary headache）最常見原因為緊縮型頭痛（tension-type headache）。腦瘤引起的頭痛屬於次發性頭痛，且並非最常見原因。\n- B. 偏頭痛（migraine）的典型特徵為單側性、搏動性（抽痛），常伴隨噁心、嘔吐、畏光或怕吵，此敘述完全正確。\n- C. 次發性頭痛（secondary headache）最常見的原因為全身性感染（如感冒、發燒）或系統性疾病，而非腦部血管異常。\n- D. 新發生的嚴重頭痛（俗稱「雷擊樣頭痛」thunderclap headache）是危險的臨床警訊，可能是蛛網膜下腔出血（SAH）等危急重症，必須立即進行影像學檢查排除次發性病因，絕不能僅給予止痛劑治療。\n\n【核心考點】\n原發性與次發性頭痛的區別、偏頭痛的典型臨床症狀，以及新發嚴重頭痛的急症處理原則。",
    "flashcard_front": "偏頭痛 / 臨床特徵 / 單側 / 伴隨症狀",
    "flashcard_back": "偏頭痛以單側、搏動性跳痛為典型表現，且常伴隨噁心、嘔吐、畏光、畏聲；緊縮型頭痛才是最常見的原發性頭痛。",
    "flashcard_summary": "單側搏動性頭痛 + 噁心嘔吐畏光 -> 偏頭痛"
  },
  {
    "id": "112-1_medicine-3_003",
    "category": "急診醫學科",
    "category_confidence": "high",
    "key_point": "獨居老人嚴重脫水、高血鈉與低血壓提示低血容積性休克。",
    "explanation": "【題幹解析】\n患者為80歲獨居老人，多日未外出。臨床表現包括意識不清、皮膚乾癟、眼眶深陷、低血壓（80/55 mmHg）、竇性頻脈與頸靜脈塌陷（低抑），這些都是極度缺水與體液嚴重流失的臨床表徵。生化檢查顯示高血鈉（Na+ 155 mEq/L，提示高滲透壓脫水）及 BUN/Cr > 30（提示腎前性急性腎損傷）。\n\n【選項詳解】\n- A. 急性心肌梗塞引起心因性休克：常伴有胸痛病史、心電圖專一性缺血變化，且常因左心衰竭而出現肺溢血或肺水腫（胸部 X 光顯示肺野有浸潤或淤血），本例 X 光肺野清晰且有頸靜脈塌陷（心因性通常頸靜脈怒張），故不符合。\n- B. 嚴重性過敏反應：常有接觸過敏原史，並伴隨皮疹、喉頭水腫、支氣管痙攣等，與多日未外出且無過敏徵象的老人脫水表現不符。\n- C. 低血容積性休克：由於多日未進食水分，體液嚴重流失，導致血壓下降、反射性心搏過速（竇性頻脈），且頸靜脈低陷與脫水表徵（高血鈉、BUN/Cr 升高）均完全符合。\n- D. 心包膜填塞：典型表現為貝克氏三聯徵（Beck's triad：低血壓、頸靜脈怒張、心音遙遠），本例病人為頸靜脈塌陷（低陷），可排除。\n\n【核心考點】\n脫水與低血容積性休克（Hypovolemic shock）的臨床與實驗室特徵，以及與其他類型休克（如心因性、阻塞性）的鑑別診斷。",
    "flashcard_front": "獨居老人 / 皮膚乾癟 / 低血壓 / 高血鈉",
    "flashcard_back": "嚴重脫水表現（皮膚乾癟、眼眶深陷、頸靜脈塌陷）伴隨高血鈉及低血壓，應診斷為低血容積性休克；肺野清晰可排除急性心衰竭所致肺水腫。",
    "flashcard_summary": "嚴重脫水 + 低血壓 + 高血鈉 -> 低血容積性休克"
  },
  {
    "id": "112-1_medicine-3_004",
    "category": "急診醫學科",
    "category_confidence": "high",
    "key_point": "血液酒精濃度大於 0.30 g/dL 可能引發輕度昏迷與生命徵候不穩。",
    "explanation": "【題幹解析】\n本題考查急性酒精中毒（Acute ethanol intoxication）之血液酒精濃度（Blood Alcohol Concentration, BAC）與臨床表現之對應關係。血液中酒精濃度的單位通常以 g/dL（或 mg/dL）表示。\n\n【選項詳解】\n- A. 0.05 g/dL (50 mg/dL)：通常引起輕度興奮、話多、注意力與反射力稍微下降。\n- B. 0.10 g/dL (100 mg/dL)：顯著的運動協調能力下降、步態不穩、說話含糊。\n- C. 0.20 g/dL (200 mg/dL)：呈現嚴重共濟失調、情緒不穩、顯著嗜睡（lethargy）或混亂。\n- D. 0.30 g/dL (300 mg/dL)：此濃度以上對大腦及腦幹產生嚴重抑制，開始出現木僵（stupor）、輕度昏迷（light coma）及生命徵候受抑制（如心跳變慢、呼吸變慢、血壓下降）。\n\n【核心考點】\n血液酒精濃度（BAC）對中樞神經系統的抑制分級與各階段臨床表徵。",
    "flashcard_front": "血液酒精濃度 / 輕度昏迷 / 生命徵候不穩 / 毒性濃度",
    "flashcard_back": "血液酒精濃度（BAC）達 0.30 g/dL 以上，極可能造成患者陷入輕度昏迷及生命徵候不穩；0.40 g/dL 以上有致死風險。",
    "flashcard_summary": "血液酒精濃度 >= 0.30 g/dL -> 輕度昏迷與生命徵候不穩"
  },
  {
    "id": "112-1_medicine-3_005",
    "category": "家庭醫學科",
    "category_confidence": "high",
    "key_point": "老年人即使無明顯腎病，其藥物腎廓清率生理上仍會顯著下降。",
    "explanation": "【題幹解析】\n本題考查心臟衰竭及老年病患在藥物動力學（Pharmacokinetics）與藥效學（Pharmacodynamics）上的生理改變。\n\n【選項詳解】\n- A. 心臟衰竭時，由於心輸出量減少，血流會優先供應給心臟和腦部（血流重分配），因此藥物在心臟或腦部的局部濃度與效用反而會相對「增加」，而非減低。\n- B. 心臟衰竭時，常伴隨胃腸道黏膜淤血及水腫，導致胃腸道蠕動減弱，藥物從腸胃道的吸收會「減少」，而非增加。\n- C. 心臟衰竭時，心輸出量降低導致腎臟及肝臟的灌流血流量顯著下降，因此藥物經由腎臟或肝臟的廓清率（clearance）會「降低」，而非增加。\n- D. 老年人隨著年齡增長，腎臟會發生生理性退化（腎小球硬化、腎血流減少），即使沒有明確的腎臟病史，其腎小球過濾率（GFR）和腎臟藥物廓清率仍可能比年輕人降低 35-50%，此描述完全正確。\n\n【核心考點】\n老年人及心臟衰竭病患的藥物動力學改變（吸收減少、廓清率下降、血流重分配對特定器官藥效增強）。",
    "flashcard_front": "心臟衰竭 / 老年人 / 藥物動力學 / 腎廓清率",
    "flashcard_back": "心臟衰竭會使藥物吸收減少、廓清率降低；老年人即使無明顯腎病，生理性退化也會使藥物腎廓清率降低 35-50%。",
    "flashcard_summary": "老年人無明顯腎病 -> 藥物腎廓清率生理性降低35-50%"
  },
  {
    "id": "112-1_medicine-3_006",
    "category": "其他",
    "category_confidence": "high",
    "key_point": "淋巴水腫患者使用潤膚劑保濕是重要護理措施而非禁忌。",
    "explanation": "【題幹解析】\n本題考查淋巴水腫（Lymphedema）的病理生理機制、常見原因、臨床表現與日常護理原則。\n\n【選項詳解】\n- A. 淋巴液富含蛋白質，長期滯留皮下會刺激慢性發炎與免疫細胞浸潤，活化纖維母細胞，進而導致脂肪和膠原蛋白大量堆積，造成皮膚硬化與增厚，此敘述正確。\n- B. 次發性淋巴水腫最常見的原因是癌症治療，如乳癌或骨盆腔癌症手術切除淋巴結，或是接受局部放射線治療造成淋巴通道纖維化，此敘述正確。\n- C. 淋巴水腫側支體極易發生乾裂與微小傷口，且局部免疫功能低下，一旦受損極易引發蜂窩性組織炎。因此，使用潤膚劑（emollients）保持皮膚濕潤、維持皮膚屏障完整是極為重要的保養措施，絕非禁忌，此敘述錯誤。\n- D. 淋巴水腫主要表現為肢體腫脹、沉重感與緊繃感，除非合併急性感染或神經壓迫，否則通常「不會」伴隨明顯的疼痛，此敘述正確。\n\n【核心考點】\n淋巴水腫的病理生理（富含蛋白質液體刺激發炎與纖維化）、次發性原因（手術、放療）及皮膚護理原則（使用潤膚劑以預防感染）。",
    "flashcard_front": "淋巴水腫 / 皮膚護理 / 潤膚劑 / 蜂窩性組織炎",
    "flashcard_back": "淋巴水腫患者應使用潤膚劑保濕以防皮膚乾裂感染；次發性水腫常因淋巴結摘除或放療所致，多不伴隨明顯疼痛。",
    "flashcard_summary": "淋巴水腫肢體保養 -> 應使用潤膚劑保濕以預防蜂窩性組織炎"
  },
  {
    "id": "112-1_medicine-3_007",
    "category": "心臟內科",
    "category_confidence": "high",
    "key_point": "BNP/NT-proBNP 血中濃度在健康人中會隨年齡上升。",
    "explanation": "【題幹解析】\n本題考查心臟衰竭的重要生物標記：B型利鈉肽（BNP）與 N端前B型利鈉肽前體（NT-proBNP）的臨床應用及影響因素。這兩者是由於心室壁張力增加（壓力或容積過載）而由心肌細胞分泌。\n\n【選項詳解】\n- A. 在舒張性心衰竭（即保留收縮分率的心衰竭 HFpEF）中，由於心室舒張受限、充盈壓升高，心室壁張力同樣增加，因此 BNP 和 NT-proBNP 依然會上升，此敘述錯誤。\n- B. BNP/NT-proBNP 不僅對收縮性心衰竭的診斷與排除有極高價值，同時也是評估疾病預後、追蹤治療效果及預測死亡率的重要指標，此敘述錯誤。\n- C. 在健康人群中，BNP 與 NT-proBNP 的血中濃度會隨著年齡增長而生理性上升（且女性普遍高於男性），此敘述正確。\n- D. 右心衰竭（如肺高壓、右心室心肌梗塞）會導致右心室壁張力及壓力上升，因此 BNP/NT-proBNP 同樣會顯著上升，此敘述錯誤。\n\n【核心考點】\nBNP 和 NT-proBNP 的分泌機制（心室壁壓力）、臨床應用（診斷與預後評估價值）及生理影響因素（年齡、性別、腎功能）。",
    "flashcard_front": "BNP / NT-proBNP / 心衰竭診斷 / 生理因子",
    "flashcard_back": "健康人血中 BNP/NT-proBNP 會隨年齡增長而生理性上升；此類指標在舒張性與右心衰竭中均會上升，且能評估預後。",
    "flashcard_summary": "BNP / NT-proBNP 濃度影響因子 -> 隨年齡增加生理性上升"
  },
  {
    "id": "112-1_medicine-3_008",
    "category": "心臟內科",
    "category_confidence": "high",
    "key_point": "Austin Flint murmur 是指嚴重主動脈瓣反流導致功能性二尖瓣狹窄的心尖部舒張期雜音。",
    "explanation": "【題幹解析】\n本題考查心臟聽診（Cardiac Auscultation）中各種特殊心音與心雜音（Heart Murmurs）的臨床意義及特徵。\n\n【選項詳解】\n- A. 嚴重肺高壓會導致肺動脈擴大與肺動脈瓣環拉伸，進而引發肺動脈瓣閉鎖不全（PR）。聽診時在左胸骨旁會聽到高頻、遞減型的舒張期雜音，此雜音即稱為 Graham Steell murmur，敘述正確。\n- B. 主動脈瓣閉鎖不全（AR）本身產生的心雜音是左胸骨旁或主動脈瓣區的「舒張早期遞減型如風吹樣雜音」。而 Austin Flint murmur 是指嚴重 AR 時，返流血液衝擊二尖瓣前葉，限制其開啟，形成「功能性二尖瓣狹窄」，進而在心尖部產生的舒張中晚期低頻滾動樣雜音，因此選項中將 AR 本身的舒張早期雜音直接稱為 Austin Flint murmur 是錯誤的。\n- C. 嚴重二尖瓣狹窄（MS）患者，在第二心音（S2）之後，瓣膜開放時由於瓣葉彈性受限突然繃緊會產生開瓣音（Opening Snap, OS），通常位於心尖內側，距 S2 約 0.05-0.12 秒，敘述正確。\n- D. 二尖瓣閉鎖不全（MR）的典型雜音是位於心尖部的全收縮期雜音（Holosystolic murmur），且雜音常向左腋下傳導，敘述正確。\n\n【核心考點】\n各種瓣膜疾病（AR、MR、MS、PR）的典型心雜音聽診部位、時間相（收縮期/舒張期）及命名（Graham Steell, Austin Flint, Opening Snap）。",
    "flashcard_front": "Austin Flint murmur / Graham Steell murmur / Opening snap",
    "flashcard_back": "AR 產生的舒張早期風吹樣雜音非 Austin Flint murmur；後者是因嚴重 AR 造成功能性 MS，於心尖部產生的舒張期低頻滾動樣雜音。",
    "flashcard_summary": "Austin Flint murmur 產生機制 -> 嚴重 AR 造成功能性 MS 產生的心尖部舒張期滾動樣雜音"
  },
  {
    "id": "112-1_medicine-3_009",
    "category": "心臟內科",
    "category_confidence": "high",
    "key_point": "竇結細胞特徵為動作電位第4期具有舒張期去極化。",
    "explanation": "【題幹解析】\n本題比較心臟自律性細胞（以竇房結細胞 sinus nodal cell 為代表）與工作心肌細胞（以心室肌細胞 ventricular cell 為代表）動作電位（Action Potential）的電生理特徵。\n\n【選項詳解】\n- A. 竇結細胞的靜態膜電位（最大舒張電位）約為 -60 mV，比心室細胞的靜態膜電位（約 -90 mV）更不極化（less polarized），因此 A 錯誤。\n- B. 竇結細胞第 0 期去極化是靠慢鈣通道（L-type Ca2+ channel）介導，其上衝速度較慢；心室細胞第 0 期則是靠快鈉通道（Fast Na+ channel）介導，上衝速度極快，因此 B 錯誤。\n- C. 竇結細胞動作電位波形較圓鈍，沒有明顯的第 2 期（平台期, Plateau phase）；而心室細胞的第 2 期非常顯著（主要由鈣離子內流與鉀離子外流平衡維持），因此 C 錯誤。\n- D. 竇結細胞具有自律性，其第 4 期（Phase 4）具有自動且緩慢的「舒張期去極化」（diastolic depolarization，主要由有趣的離子流 Funny current, If 驅動），這是其產生自動節律的生理基礎，此描述完全正確。\n\n【核心考點】\n心臟自律細胞與收縮細胞動作電位各期（0-4期）的電生理機制對比。",
    "flashcard_front": "竇結細胞 / 心室細胞 / 動作電位 / 舒張期去極化",
    "flashcard_back": "竇結細胞（自律細胞）的特徵是第4期具備由 If 電流驅動的舒張期去極化；其第0期由 Ca2+ 介導，靜態電位較心室細胞不極化。",
    "flashcard_summary": "竇結細胞動作電位特徵 -> 第4期舒張期去極化 (If 電流)"
  },
  {
    "id": "112-1_medicine-3_010",
    "category": "心臟內科",
    "category_confidence": "high",
    "key_point": "主動脈縮窄在整體人群中以男性較為多見。",
    "explanation": "【題幹解析】\n本題考查先天性心血管畸形——主動脈縮窄（Coarctation of the Aorta）的流行病學、解剖位置與臨床關聯。\n\n【選項詳解】\n- A. 主動脈縮窄最常見的位置是在左鎖骨下動脈的遠端，緊鄰動脈導管韌帶（ligamentum arteriosum）的附著處，通常稱為導管後型（postductal type），此敘述正確。\n- B. 主動脈縮窄是一種典型的先天性心血管發育異常（Congenital heart disease），此敘述正確。\n- C. 在一般人群中，主動脈縮窄在「男性」中的發生率顯著高於女性（男女比例約為 2:1 至 5:1），因此「通常女性多於男性」的說法錯誤。\n- D. 主動脈縮窄與特納氏症候群（Turner's syndrome, 45,XO，常表現為性腺發育不全）有強烈的關聯性，約有 10-20% 的 Turner's 症候群患者會合併此畸形，此敘述正確。\n\n【核心考點】\n主動脈縮窄（Coarctation of the Aorta）的解剖定位（動脈韌帶旁）、性別傾向（男性居多）及遺傳關聯（特納氏症候群 Turner's syndrome）。",
    "flashcard_front": "主動脈縮窄 / 解剖定位 / 性別比例 / Turner's syndrome",
    "flashcard_back": "主動脈縮窄多見於男性；狹窄處最常位於左鎖骨下動脈遠端（動脈韌帶旁），且常合併 Turner's syndrome。",
    "flashcard_summary": "主動脈縮窄性別傾向 -> 男性多於女性 (2:1 至 5:1)"
  }
]

# Write to json file
with open('scratch/updates_112-1_medicine-3_batch1.json', 'w', encoding='utf-8') as f:
    json.dump(updates, f, ensure_ascii=False, indent=2)

# Run update command
res = subprocess.run([
    'python', 'scripts/exams/update_question_fields.py',
    '--exam-file', 'public/data/exams/112-1/medicine-3.json',
    '--updates-file', 'scratch/updates_112-1_medicine-3_batch1.json'
], capture_output=True, text=True)

print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
