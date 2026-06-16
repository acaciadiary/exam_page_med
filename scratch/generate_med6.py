# -*- coding: utf-8 -*-
import json
import os

# Ensure outputs directory exists
os.makedirs("reports/gemini_outputs", exist_ok=True)

batches_data = {}

# ----------------------------------------------------
# 109-1_medicine-6_batch-001 (Q1-Q15)
# ----------------------------------------------------
batches_data["109-1_medicine-6_batch-001"] = {
  "dataset_id": "109-1_medicine-6",
  "batch_id": "109-1_medicine-6_batch-001",
  "items": [
    {
      "question_id": "109-1_medicine-6_001",
      "question_number": 1,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "麻醉科",
      "category_confidence": "high",
      "key_point": "全身麻醉前評估困難通氣的臨床危險因子。",
      "explanation": "風濕性心臟病主要影響心臟瓣膜，通常不會直接造成上呼吸道解剖結構異常或頸椎活動受限，因此最不可能是預期困難通氣的患者，故選A。唐氏綜合症患者常有大舌頭、小下巴與短頸，類風濕性關節炎患者常有顳顎關節受侵犯及環樞椎不穩，阻塞性睡眠呼吸中止症（OSA）患者則因咽部軟組織塌陷，皆是困難通氣的高風險群。",
      "flashcard_front": "困難通氣 / 術前評估 / 唐氏症 / 類風濕關節炎 / 風濕性心臟病",
      "flashcard_back": "風濕性心臟病無呼吸道構造異常，非困難通氣高危險群；唐氏症、類風濕關節炎及OSA皆有呼吸道或關節結構受限，易發生困難通氣。",
      "flashcard_summary": "困難通氣危險因子 -> 唐氏症、類風濕關節炎及OSA易困難通氣，風濕性心臟病則無直接相關。"
    },
    {
      "question_id": "109-1_medicine-6_002",
      "question_number": 2,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "麻醉科",
      "category_confidence": "high",
      "key_point": "脈搏血氧儀的測量原理、干擾因素與臨床解讀。",
      "explanation": "脈搏血氧儀（SpO2）是利用氧合血紅素與去氧血紅素對紅光（660 nm）與遠紅外光（940 nm）的吸光率比值差異進行估算，故B正確。指甲油顏色（特別是藍色、黑色）會干擾測量，故A錯誤；一氧化碳中毒時，碳氧血紅素在660 nm的吸光率與氧合血紅素相似，會使SpO2呈現偽陽性偏高，故C錯誤；當SpO2為90%時，動脈血氧分壓約僅有60 mmHg，且組織灌流等亦會影響組織缺氧，故D錯誤。",
      "flashcard_front": "脈搏血氧儀 (SpO2) / 660nm與940nm / 一氧化碳中毒 / 指甲油干擾",
      "flashcard_back": "SpO2利用紅光(660nm)與紅外光(940nm)吸光比值測量；指甲油會干擾；一氧化碳中毒時數值會偽性偏高。",
      "flashcard_summary": "SpO2測量原理與干擾 -> 利用660nm與940nm吸光比，一氧化碳中毒時數值會偽性偏高，指甲油會干擾。"
    },
    {
      "question_id": "109-1_medicine-6_003",
      "question_number": 3,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "麻醉科",
      "category_confidence": "high",
      "key_point": "裝有心臟節律器患者的術中麻醉管理與電燒防範。",
      "explanation": "在裝有心臟節律器的患者胸前放置磁鐵，會使節律器轉為非同步固定頻率模式。這有助於避免電燒的電磁干擾被誤判定為自主心跳，但無法完全免除電燒造成的硬體損壞或心肌燒傷。因此術中仍需妥善安置電燒迴路板並儘量使用雙極電燒，故B選項敘述錯誤。",
      "flashcard_front": "節律器 (Pacemaker) / 術中電燒 / 放磁鐵作用 / 非同步模式",
      "flashcard_back": "置放磁鐵可使節律器改為固定頻率放電（非同步模式），防止電磁干擾引起暫停，但無法消除電燒的所有硬體危害。",
      "flashcard_summary": "節律器置放磁鐵限制 -> 置放磁鐵可轉為固定頻率放電，但不能完全免除電燒危害。"
    },
    {
      "question_id": "109-1_medicine-6_004",
      "question_number": 4,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "麻醉科",
      "category_confidence": "high",
      "key_point": "苯二氮平類藥物拮抗劑Flumazenil的臨床應用。",
      "explanation": "Flumazenil是苯二氮平類藥物（如Midazolam）的特異性競爭性拮抗劑，能與GABAA受體上的BDZ結合位點結合，從而逆轉Midazolam過量引起的鎮靜、認知障礙及呼吸抑制，故A為正確答案。Naloxone是鴉片類藥物的特異性拮抗劑；Dexmedetomidine為選擇性alpha-2腎上腺素受體致效劑；Ketamine則為NMDA受體拮抗劑。",
      "flashcard_front": "Midazolam過量 / 苯二氮平拮抗劑 / GABAA受體 / Flumazenil",
      "flashcard_back": "Flumazenil是Midazolam等苯二氮平類藥物的特異性拮抗劑；Naloxone則用於逆轉鴉片類藥物（Opioids）。",
      "flashcard_summary": "Midazolam解毒劑 -> Flumazenil為苯二氮平類藥物之競爭性拮抗劑，可用於治療過量中毒。"
    },
    {
      "question_id": "109-1_medicine-6_005",
      "question_number": 5,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "麻醉科",
      "category_confidence": "high",
      "key_point": "鴉片類藥物受體亞型與其藥理生理效應。",
      "explanation": "嗎啡引起的呼吸抑制以及最主要的止痛、成癮性等作用，主要是經由mu（μ）受體（特別是μ2受體介導呼吸抑制），而非經由kappa（κ）受體，故C選項敘述錯誤。鴉片類受體（包括mu、kappa、delta）均屬於G蛋白偶聯受體；Naloxone為非選擇性鴉片受體拮抗劑，可逆轉嗎啡作用。",
      "flashcard_front": "鴉片受體 / 嗎啡 / 呼吸抑制 / G蛋白偶聯 / Naloxone",
      "flashcard_back": "嗎啡引起的呼吸抑制主要是藉由mu受體（而非kappa受體）介導；Naloxone是鴉片受體的特異性拮抗劑。",
      "flashcard_summary": "嗎啡呼吸抑制受體 -> 嗎啡主要作用於mu受體引起呼吸抑制，而非kappa受體。"
    },
    {
      "question_id": "109-1_medicine-6_006",
      "question_number": 6,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "麻醉科",
      "category_confidence": "high",
      "key_point": "手術體位相關周邊神經損傷的防範指引。",
      "explanation": "在碎石姿勢下，當髖關節極度屈曲且膝關節外展時，會過度拉扯或壓迫股神經，但過度拉扯腿後肌群（hamstring）通常是造成坐骨神經或腓總神經受傷的機轉，而非股神經受損的主因，故C選項敘述錯誤。術前確認擺位容忍度、側臥時擺放胸軸以保護臂神經叢、以及避免手肘過度屈曲以防尺神經受壓，皆為標準防範建議。",
      "flashcard_front": "手術擺位 / 碎石姿勢 / 股神經受損 / 尺神經壓迫",
      "flashcard_back": "碎石姿勢過度屈髖拉扯會損傷股神經，但拉扯腿後肌主要造成坐骨神經損傷；手肘屈曲會增加尺神經受損風險。",
      "flashcard_summary": "擺位與神經損傷 -> 碎石位拉扯腿後肌易傷及坐骨神經而非股神經；肘屈曲易傷及尺神經。"
    },
    {
      "question_id": "109-1_medicine-6_007",
      "question_number": 7,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "麻醉科",
      "category_confidence": "high",
      "key_point": "子癲前症的產科與麻醉用藥禁忌與管理。",
      "explanation": "Methylergonovine（麥角新鹼）是一種強力的血管收縮劑。由於子癲前症患者本身已存在嚴重的血管痙攣與高血壓，使用此藥極易誘發高血壓危象甚至腦出血，因此在子癲前症患者中是禁忌症，不可常規使用，故D選項錯誤。硫酸鎂常用於預防抽搐，在全身麻醉時會增強非去極化肌鬆劑（如rocuronium）作用，應減少肌鬆劑劑量。",
      "flashcard_front": "子癲前症 / 硫酸鎂 / 肌鬆劑減量 / 麥角新鹼 (Methylergonovine) 禁用",
      "flashcard_back": "子癲前症患者禁用強血管收縮劑Methylergonovine以防腦出血；術中硫酸鎂會增強非去極化肌鬆劑作用，需減量。",
      "flashcard_summary": "子癲前症用藥禁忌 -> 禁用Methylergonovine以防血壓飆升；硫酸鎂會延長肌鬆劑作用，肌鬆劑需減量。"
    },
    {
      "question_id": "109-1_medicine-6_008",
      "question_number": 8,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "麻醉科",
      "category_confidence": "high",
      "key_point": "Pregabalin的藥理作用機轉與離子通道。",
      "explanation": "Pregabalin（普瑞巴林）的止痛機轉是高度選擇性地與中樞神經系統中電壓敏感性鈣離子通道的 alpha-2-delta 輔助亞基結合。這樣可以減少麩胺酸、去甲腎上腺素等興奮性神經傳導物質的釋放，從而達到止痛與抗癲癇效果，故選B。",
      "flashcard_front": "Pregabalin / 鈣離子通道 / alpha-2-delta 亞基 / 帶狀鋪疹後神經痛",
      "flashcard_back": "Pregabalin結合至電壓敏感性鈣離子通道的alpha-2-delta亞基，減少興奮性遞質釋放以達到止痛效果。",
      "flashcard_summary": "Pregabalin機轉 -> 結合於電壓敏感性鈣離子通道的alpha-2-delta亞基發揮止痛作用。"
    },
    {
      "question_id": "109-1_medicine-6_009",
      "question_number": 9,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "麻醉科",
      "category_confidence": "high",
      "key_point": "呼吸器拔管與脫離的臨床評估指標。",
      "explanation": "淺快呼吸指數（RSBI，定義為呼吸頻率除以潮氣容積L）是評估拔管成功率的重要指標。當RSBI > 105時，代表病人處於淺快呼吸狀態，拔管失敗的風險極高，因此最不適合拔管，故B為正確答案。拔管的適宜條件包括：RSBI < 105；潮氣容積 > 5 mL/kg；最大吸氣壓（MIP）小於 -25 cmH2O；以及在低濃度氧氣及低PEEP下血氧飽和度穩定。",
      "flashcard_front": "呼吸器脫離 / 拔管指標 / RSBI > 105 / 最大吸氣壓 (MIP)",
      "flashcard_back": "RSBI > 105 提示呼吸淺快，為拔管失敗的高危險指標；拔管適宜條件包括RSBI < 105 及 MIP < -20 cmH2O。",
      "flashcard_summary": "拔管評估指標 -> RSBI > 105 代表淺快呼吸不宜拔管，應在RSBI < 105及吸氣壓力足夠時拔管。"
    },
    {
      "question_id": "109-1_medicine-6_010",
      "question_number": 10,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "色素性視網膜炎的眼底特徵。",
      "explanation": "色素性視網膜炎（RP）的典型三聯徵（classical triad）為：骨刺狀黑色素沉著（bone-spicule pigmentation）、蠟黃色視神經盤蒼白（waxy pallor of the optic disc）以及視網膜小動脈變細（arteriolar attenuation）。黃斑部水腫（特別是囊樣黃斑部水腫）雖然是RP常見的併發症之一，但不屬於其經典三特徵，故選D。",
      "flashcard_front": "色素性視網膜炎 / 典型三特徵 / 骨刺狀 / 蠟黃色神經盤",
      "flashcard_back": "RP經典三特徵為骨刺狀黑色素沉積、蠟黃色視盤蒼白、小動脈變細；黃斑水腫為常見併發症而非三特徵。",
      "flashcard_summary": "色素性視網膜炎特徵 -> 經典三特徵為骨刺狀沉積、視盤蠟黃蒼白、動脈變細，黃斑水腫不在此列。"
    },
    {
      "question_id": "109-1_medicine-6_011",
      "question_number": 11,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "眼部化學性灼傷的病理生理與治療原則。",
      "explanation": "鹼性化學灼傷由於鹼性物質能溶解脂質並穿透細胞膜，引發液化性壞死，會迅速穿透角膜進入前房。其角膜輪部缺血（limbal ischaemia）的範圍越廣，代表幹細胞受損越嚴重，是決定視力預後的重要因子，故D正確。鹼性化學灼傷預後比酸性差（A錯誤）；急救首選大量生理食鹽水沖洗，絕不可用酸性水溶液中和（B錯誤）；術後早期可使用類固醇以控制發炎反應，但10天後因有角膜溶解風險需慎用（C錯誤）。",
      "flashcard_front": "眼部鹼性灼傷 / 液化壞死 / 沖洗方法 / 類固醇使用 / 輪部缺血",
      "flashcard_back": "鹼性灼傷呈液化壞死危害深；急救首選大量清水沖洗，禁用酸中和；角膜輪部缺血程度是視力預後之關鍵。",
      "flashcard_summary": "眼部鹼性灼傷特性 -> 液化壞死危害深，急救禁用酸中和，角膜輪部缺血程度決定視力預後。"
    },
    {
      "question_id": "109-1_medicine-6_012",
      "question_number": 12,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "頸動脈海綿竇瘻管的眼部臨床特徵。",
      "explanation": "頸動脈海綿竇瘻管（CCF）是由於頸動脈與海綿竇之間形成異常交通，導致高壓的動脈血逆流進入眼靜脈系統。這會引發眼壓升高、眼球突出，並在結膜及上鞏膜出現特徵性的血管高度擴張與迂曲，外觀呈螺旋軟木塞狀（corkscrew-like vessels），故選C。鮭色斑常見於眼結膜淋巴瘤；微小動脈瘤則是糖尿病視網膜病變的特徵。",
      "flashcard_front": "頸動脈海綿竇瘻管 (CCF) / 動靜脈交通 / 軟木塞狀血管 / 結膜血管曲張",
      "flashcard_back": "CCF因動脈血逆流入眼靜脈，會導致結膜與上鞏膜出現特徵性的螺旋軟木塞狀血管擴張（corkscrew vessels）。",
      "flashcard_summary": "CCF眼部特徵 -> 結膜與上鞏膜出現特徵性的螺旋軟木塞狀血管擴張。"
    },
    {
      "question_id": "109-1_medicine-6_013",
      "question_number": 13,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "白內障術後後囊混濁的處置方法。",
      "explanation": "水晶體後囊混濁（PCO，俗稱二次白內障）是白內障術後最常見的晚期併發症。治療時不需再次進行手術，只需在門診使用銣雅鉻雷射（Nd:YAG laser）進行後囊切開術（posterior capsulotomy），在混濁的後囊中央切開一個通道，即可快速恢復視力，故選A。超音波晶體乳化術是白內障摘除的手術方式。",
      "flashcard_front": "二次白內障 / 後囊混濁 (PCO) / Nd:YAG 雷射 / 後囊切開術",
      "flashcard_back": "白內障術後後囊混濁（PCO）首選銣雅鉻（Nd:YAG）雷射進行後囊切開治療，不需再次切開手術。",
      "flashcard_summary": "後囊混濁治療 -> 白內障術後混濁以Nd:YAG雷射切開治療，無須再次乳化手術。"
    },
    {
      "question_id": "109-1_medicine-6_014",
      "question_number": 14,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "眼外肌在不同眼球位置下的運動功能與神經支配。",
      "explanation": "眼球的外展運動（向顳側看）主要由外直肌支配。當眼球處於外展位置時，上直肌的肌肉收縮軸線與眼球光軸一致，此時上直肌的唯一主要作用就是使眼球向上看。因此，眼球要往外上方看時，必須靠外直肌（外展）與上直肌（向上）的共同作用，故選A。相反地，下斜肌雖然也有向上看的作用，但其在眼球內收時向上看的作用最大。",
      "flashcard_front": "眼球外上視 / 外直肌 / 上直肌 / 眼外肌動作",
      "flashcard_back": "眼球在外展位時，上直肌向上看的作用最大；因此外上視主要靠外直肌與上直肌共同作用。",
      "flashcard_summary": "眼球外上視肌肉 -> 外展位時上直肌向上看作用最大，故外上視靠外直肌與上直肌。"
    },
    {
      "question_id": "109-1_medicine-6_015",
      "question_number": 15,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "眼球運動學的定義與會聚分類。",
      "explanation": "雙眼的異向會聚運動（vergence）可細分為多種類型，其中「調節性會聚（accommodative convergence）」是指當眼睛進行調節（看近物變焦）時所主動誘發的會聚運動；而「強直性會聚（tonic convergence）」則是指從解剖生理靜止位置過渡到清醒注視位置時，由眼外肌基本張力所維持的會聚，兩者在機制上完全不同，故D選項錯誤。單眼運動稱為duction，雙眼同向運動稱為version，雙眼異向運動稱為vergence，A、B、C選項敘述皆正確。",
      "flashcard_front": "單眼運動 / 雙眼同向 / 雙眼異向 / 調節性會聚 / 強直性會聚",
      "flashcard_back": "duction為單眼運動；version為同向；vergence為異向。調節性會聚是由看近調節所誘發，與維持基底張力的強直性會聚不同。",
      "flashcard_summary": "眼球運動分類 -> duction為單眼，version為同向，vergence為異向；調節性會聚與強直性會聚機理不同。"
    }
  ]
}

# ----------------------------------------------------
# 109-1_medicine-6_batch-002 (Q16-30)
# ----------------------------------------------------
batches_data["109-1_medicine-6_batch-002"] = {
  "dataset_id": "109-1_medicine-6",
  "batch_id": "109-1_medicine-6_batch-002",
  "items": [
    {
      "question_id": "109-1_medicine-6_016",
      "question_number": 16,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "先天性葡萄膜/脈絡膜缺損的胚胎學成因與好發部位。",
      "explanation": "胚胎發育過程中，眼杯下方的胚胎裂（fetal fissure）大約在懷孕第6週時從中央向前後閉合。此裂縫位於眼球的下方（即6點鐘方位），若閉合不全，就會在下方形成先天性葡萄膜缺損，因此虹膜、睫狀體或脈絡膜缺損典型地發生在眼球的6點鐘部位，故選B。",
      "flashcard_front": "先天性缺損 / coloboma / 胚胎裂閉合不全 / 6點鐘部位",
      "flashcard_back": "先天性葡萄膜或脈絡膜缺損是由眼下方的胚胎裂閉合不全引起，因此典型好發於6點鐘方向。",
      "flashcard_summary": "coloboma部位 -> 胚胎裂閉合不全引起，典型發生在眼球6點鐘部位。"
    },
    {
      "question_id": "109-1_medicine-6_017",
      "question_number": 17,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "砂眼的病原體、病理特徵及臨床表現。",
      "explanation": "砂眼的病原體是砂眼衣原體（Chlamydia trachomatis）。在組織學病理切片中，衣原體在結膜上皮細胞的細胞質內（而非細胞核內）形成包含體（Halberstaedter-Prowazek inclusion bodies），且這些包含體在吉姆薩染色下呈現嗜鹼性，故C選項錯誤。瘢痕期在上瞼結膜可見水平橫行的白色瘢痕（Arlt's line，B正確）；治療可用口服或局部四環黴素（D正確）。",
      "flashcard_front": "砂眼 / 披衣菌 / Arlt line / 細胞質內包含體 / 嗜鹼性",
      "flashcard_back": "砂眼披衣菌感染會在結膜上皮細胞的「細胞質內」（非核內）形成包含體；瘢痕期上瞼結膜可見Arlt's line。",
      "flashcard_summary": "砂眼病理特徵 -> 衣原體包含體位於細胞質內，非細胞核內；瘢痕期有Arlt's line。"
    },
    {
      "question_id": "109-1_medicine-6_018",
      "question_number": 18,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "新生兒眼炎之淋球菌感染特徵與發病時間。",
      "explanation": "新生兒淋病性結膜炎（Neonatal gonococcal conjunctivitis）是由奈瑟氏淋病雙球菌引起，通常在出生後2至5天內（即第一週內）就會出現急性的超急性膿漏與結膜炎，潛伏期極短，而非第三至第四週，故C選項錯誤。此病多因經產道分娩時吸入病原體；因淋球菌具穿透角膜的能力，必須同時進行局部與全身抗生素治療以防失明；確診需靠分泌物Gram stain抹片與培養。",
      "flashcard_front": "新生兒淋病結膜炎 / 出生後2-5天 / 產道感染 / 全身抗生素",
      "flashcard_back": "淋病性結膜炎在出生後2-5天內發病（超急性膿漏），需全身抗生素以防角膜穿孔；披衣菌結膜炎發病較晚（5-14天）。",
      "flashcard_summary": "淋病性結膜炎發病時間 -> 出生後2-5天內發病，非3-4週；需全身與局部抗生素治療。"
    },
    {
      "question_id": "109-1_medicine-6_019",
      "question_number": 19,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "內耳生理學中內耳蝸電位（EP）的來源。",
      "explanation": "耳蝸中階（scala media）充滿高鉀、低鈉的內淋巴液，並具有約 +80 mV 的內耳蝸電位（EP）。此電位及內淋巴液的高鉀濃度主要是由位於耳蝸外側壁的血管紋（stria vascularis）透過主動運輸鉀離子所產生與維持，這對毛細胞的機械-電信號轉換至關重要，故選A。",
      "flashcard_front": "內耳蝸電位 / +80 mV / 內淋巴液 / 血管紋 (stria vascularis)",
      "flashcard_back": "內耳蝸中階的高鉀內淋巴液與+80 mV電位是由外側壁的血管紋（stria vascularis）主動分泌鉀離子所維持。",
      "flashcard_summary": "內耳蝸電位來源 -> 內耳蝸電位由外側壁血管紋（stria vascularis）維持。"
    },
    {
      "question_id": "109-1_medicine-6_020",
      "question_number": 20,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "後天性中耳膽脂瘤的耳鏡特徵與成因。",
      "explanation": "原發性後天性膽脂瘤通常是由於耳咽管功能不良導致中耳腔負壓，使得鼓膜的鬆弛部（pars flaccida）向內塌陷，逐漸形成內陷囊袋並積聚脫落的上皮角化碎屑。在耳鏡下，典型的表現是在鼓膜上方鬆弛部出現邊緣穿孔或內陷，並伴有白色的角化物質堆積，故選B。繼發性後天性膽脂瘤則通常繼發於鼓膜緊張部邊緣穿孔或外傷。",
      "flashcard_front": "膽脂瘤 / 鼓膜鬆弛部內陷 / 原發後天性 / 緊張部穿孔",
      "flashcard_back": "原發性後天性膽脂瘤起因於中耳負壓導致鼓膜鬆弛部（pars flaccida）內陷；繼發性則常繼發於鼓膜緊張部邊緣穿孔。",
      "flashcard_summary": "原發後天性膽脂瘤 -> 起因於鼓膜鬆弛部內陷，耳鏡下見上方鬆弛部穿孔與角化物堆積。"
    },
    {
      "question_id": "109-1_medicine-6_021",
      "question_number": 21,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "急性顏面神經麻痺的流行病學與最常見病因。",
      "explanation": "貝爾氏麻痺（Bell's palsy，特發性顏面神經麻痺）是臨床上最常見的急性單側顏面神經麻痺病因，約占所有急性顏面神經麻痺病例的60-70%。其確切病因尚未完全明瞭，但目前認為與單純疱疹病毒（HSV-1）在顏面神經管內的活化及神經水腫壓迫有關。Ramsay Hunt症候群（帶狀疱疹感染）及外傷性也是病因，但發生率遠低於Bell's palsy，故選B。",
      "flashcard_front": "急性顏面麻痺 / 最常見病因 / Bell's palsy / Ramsay Hunt",
      "flashcard_back": "急性顏面神經麻痺最常見原因為特發性的Bell's palsy；Ramsay Hunt症候群則伴隨外耳道水泡與前庭蝸神經症狀。",
      "flashcard_summary": "急性顏面麻痺最常見原因 -> 貝爾氏麻痺（Bell's palsy）為最常見之特發性單側顏面神經麻痺。"
    },
    {
      "question_id": "109-1_medicine-6_022",
      "question_number": 22,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "過敏原皮膚測試的臨床特點與藥物干擾。",
      "explanation": "過敏原皮膚測試（如皮膚點刺測試）會受到受試者正在使用的某些藥物的顯著影響。例如，抗組織胺藥、三環抗憂鬱藥及部分全身性類固醇會抑制皮膚的紅腫風疹反應，導致出現偽陰性結果，因此測試前必須停用這些藥物，故D選項錯誤。過敏原皮測具有操作簡便、敏感度高、迅速得出結果且費用低廉的優點。",
      "flashcard_front": "過敏原皮測 / 藥物干擾 / 抗組織胺 / 偽陰性",
      "flashcard_back": "皮膚測試易受抗組織胺等藥物影響而呈偽陰性，測試前需停藥；其具備快速、高敏感性與便宜等優點。",
      "flashcard_summary": "過敏原皮測受藥物影響 -> 抗組織胺等藥物會影響皮測結果，測試前需停藥。"
    },
    {
      "question_id": "109-1_medicine-6_023",
      "question_number": 23,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "阻塞性睡眠呼吸中止症之檢查與治療。",
      "explanation": "對於中重度阻塞性睡眠呼吸中止症（OSAS）患者，鼻部連續陽壓呼吸器（CPAP）是公認且首選的標準非侵入性治療，故C選項正確。PSG的呼吸暫停/低通氣指數（AHI）異常定義為成人每小時出現5次以上、每次持續10秒以上的呼吸暫停或低通氣，故A錯誤；OSAS最常發生阻礙的部位是軟顎與口咽後壁，而非單一舌根，故B錯誤；扁桃腺與腺樣體切除術是兒童OSAS的首選外科治療，而非成人，故D錯誤。",
      "flashcard_front": "OSAS / 診斷標準 (AHI) / 鼻部連續正壓 (CPAP) / 兒童與成人首選",
      "flashcard_back": "CPAP是多數成人OSAS的首選治療；PSG診斷標準為AHI >= 5次/小時（每次>=10秒）；腺樣體切除為兒童首選。",
      "flashcard_summary": "OSAS診斷與治療 -> AHI以每小時5次、每次10秒為標準，CPAP為成人首選治療，扁桃體切除為兒童首選。"
    },
    {
      "question_id": "109-1_medicine-6_024",
      "question_number": 24,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "聲門癌的病因、分期與早期治療策略。",
      "explanation": "本題圖中所示為局限於單側聲帶的早期喉腫瘤。聲門癌多為鱗狀上皮細胞癌，早期（T1-T2）局限於聲帶且活動度正常時，手術切除（如雷射微創切除）或單獨放射線治療（RT）均可達到高於90%的極佳根治率與發音保留，故D選項正確。喉癌主要與吸菸及飲酒密切相關，而非嚼檳榔，故A錯誤；此腫瘤位於聲門區而非上聲門區，故B錯誤；聲門區淋巴管稀疏，早期聲門癌的頸部淋巴結轉移極為罕見，故C錯誤。",
      "flashcard_front": "早期聲門癌 / 聲音沙啞 / 淋巴轉移罕見 / 手術或放療",
      "flashcard_back": "早期聲門癌局限於聲帶，淋巴轉移率低，手術（雷射）或放射線治療皆可達到極佳的局部控制率。",
      "flashcard_summary": "早期聲門癌治療 -> 早期聲門癌轉移罕見，單獨手術或放療療效相近且佳。"
    },
    {
      "question_id": "109-1_medicine-6_025",
      "question_number": 25,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "食道異物嵌頓的處置與食道破裂的急症處理。",
      "explanation": "在進行硬式或軟式食道鏡取異物過程中，若術中懷疑發生食道破裂/穿孔，必須立即停止經口進食（NPO），並小心放置鼻胃管進行胃腸減壓，同時給予廣效性抗生素與靜脈補液，以防嚴重的縱隔腔炎，故D選項正確。食道第一狹窄（環狀軟骨處）是異物最常嵌頓處，非會厭處，故A錯誤；食道異物手術多需在全身麻醉下進行，以防氣道誤吸與食道損傷，故B錯誤；硬式食道鏡發生食道穿孔的併發症機率（約1-2%）顯著高於軟式內視鏡，故C錯誤。",
      "flashcard_front": "食道異物 / 食道穿孔 / 硬式食道鏡風險 / 禁食與胃管",
      "flashcard_back": "懷疑食道穿孔時應立即禁食並置鼻胃管減壓以防縱隔腔炎；硬式食道鏡穿孔風險高於軟式，異物手術多在全麻下進行。",
      "flashcard_summary": "食道異物與穿孔處置 -> 懷疑食道破裂須立即禁食、置鼻胃管減壓以防縱隔腔炎，硬式食道鏡穿孔風險較高。"
    },
    {
      "question_id": "109-1_medicine-6_026",
      "question_number": 26,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "口腔癌（舌癌）AJCC TNM癌症分期。",
      "explanation": "根據AJCC癌症分期系統：1. 口腔癌腫瘤最大徑大於4公分（此處4.5公分）但未侵犯深部構造，T分期為 T3。2. 同側單個轉移淋巴結，直徑大於3公分且小於等於6公分（此處為4公分），且無淋巴外侵犯，N分期為 N2a。3. T3N2a在口腔癌的分期中歸類為 Stage IVA（任何T1-T3, N2皆為Stage IVA），因此為T3N2a, Stage IVA，故選D。",
      "flashcard_front": "舌癌分期 / 腫瘤 > 4cm / 單個同側淋巴結 4cm / T3N2a / Stage IVA",
      "flashcard_back": "腫瘤>4cm為T3；同側單個淋巴結3-6cm為N2a；T3N2a屬於Stage IVA（T1-T3伴N2即為IVA）。",
      "flashcard_summary": "舌癌TNM分期 -> 腫瘤>4cm為T3，淋巴結4cm為N2a，T3N2a分期為Stage IVA。"
    },
    {
      "question_id": "109-1_medicine-6_027",
      "question_number": 27,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "頭頸癌引起的牽涉性耳痛機制與診斷。",
      "explanation": "口咽部（特別是扁桃腺區）與下咽部的癌症常會壓迫或刺激舌咽神經（CN IX）或迷走神經（CN X），其感覺纖維與支配耳部的神經分支（如鼓室支、耳支）重疊，進而產生反射性耳痛（referred otalgia）。因此，對於有菸酒檳榔史且耳部檢查正常的患者，若出現單側間歇性耳痛，應高度懷疑扁桃腺癌或下咽癌等頭頸部惡性腫瘤，故選C。聲門癌早期多以聲音沙啞表現；舌癌與頰黏膜癌引起的牽涉痛通常出現在較晚期。",
      "flashcard_front": "牽涉性耳痛 / referred otalgia / 耳檢正常 / 扁桃腺癌 / 舌咽神經",
      "flashcard_back": "耳部正常的單側耳痛提示牽涉痛，常由扁桃腺癌或下咽癌刺激舌咽神經或迷走神經引起，是頭頸癌的重要警訊。",
      "flashcard_summary": "牽涉性耳痛警訊 -> 耳正常但單側耳痛提示牽涉痛，常見於扁桃腺癌或下咽癌刺激神經所致。"
    },
    {
      "question_id": "109-1_medicine-6_028",
      "question_number": 28,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "產科術語中孕次與產次的定義與計算。",
      "explanation": "在產科術語中：Gravida（孕次）指懷孕的總次數（不論結局）；Para（產次）指懷孕達20週以上（或胎兒體重達500克以上）並分娩的次數（不論活產或死產）。該患者懷孕過兩次（Gravida = 2），但兩次皆在早期自然流產終止，未曾有過懷孕達20週以上的分娩經歷，因此產次為0（Para = 0）。因此，她屬於未產婦（Nullipara，即產次為零者），故選C。",
      "flashcard_front": "產科術語 / 孕次 (Gravida) / 產次 (Para) / 自然流產 / 未產婦 (Nullipara)",
      "flashcard_back": "孕次指懷孕總次數；產次僅計算懷孕滿20週之分娩次數。懷孕2次均早期流產者為G2P0，屬於Nullipara（未產婦）。",
      "flashcard_summary": "孕次與產次計算 -> 懷孕次數不論結局計入孕次；僅滿20週之分娩計入產次（流產不計產次）。"
    },
    {
      "question_id": "109-1_medicine-6_029",
      "question_number": 29,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "羊水酸鹼值及其在破水診斷的應用。",
      "explanation": "羊水在懷孕中後期的pH值通常呈弱鹼性或中性，範圍大約在 7.0至7.5 之間，故選C。臨床上利用此特性進行石蕊試紙試驗（Nitrazine test）：正常陰道分泌物呈酸性（pH 4.5-5.5），而羊水呈弱鹼性，當發生破水時，流出的羊水會使石蕊試紙由黃色變為深藍色，以此輔助診斷胎膜早破。",
      "flashcard_front": "羊水 pH / 弱鹼性 / 破水診斷 / Nitrazine test",
      "flashcard_back": "羊水pH值介於7.0-7.5；陰道分泌物呈酸性(pH 4.5-5.5)；利用此鹼性差異可用Nitrazine試紙檢測破水（變藍色）。",
      "flashcard_summary": "羊水pH與破水診斷 -> 羊水pH值約7.0-7.5（弱鹼性），破水會使Nitrazine試紙變藍色。"
    },
    {
      "question_id": "109-1_medicine-6_030",
      "question_number": 30,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "肩難產的處置步驟與禁用操作。",
      "explanation": "在發生肩難產時，宮底壓迫法（Fundal pressure）是絕對禁忌的操作。因為宮底壓迫會使被嵌頓的胎兒前肩更加緊密地卡在母親的恥骨聯合後方，並大幅增加子宮破裂、胎兒鎖骨骨折及臂神經叢損傷（Erb's palsy）的危險，故選B。處理肩難產的正確步驟包括：McRoberts maneuver（雙腿極度屈曲）、Rubin/Woods corkscrew maneuver（旋轉胎肩）以及娩出後肩等。",
      "flashcard_front": "肩難產 / 禁用手法 / 宮底壓迫 (Fundal pressure) / McRoberts",
      "flashcard_back": "肩難產時禁用宮底壓迫法，因會加重肩膀嵌頓並造成臂神經叢損傷；首選McRoberts位與恥骨上壓迫。",
      "flashcard_summary": "肩難產處置禁忌 -> 禁用宮底壓迫法（會加重嵌頓與神經損傷），應採McRoberts與旋轉胎肩。"
    }
  ]
}

# ----------------------------------------------------
# 109-1_medicine-6_batch-003 (Q31-45)
# ----------------------------------------------------
batches_data["109-1_medicine-6_batch-003"] = {
  "dataset_id": "109-1_medicine-6",
  "batch_id": "109-1_medicine-6_batch-003",
  "items": [
    {
      "question_id": "109-1_medicine-6_031",
      "question_number": 31,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "泌乳與噴乳反射的內分泌調節機制。",
      "explanation": "產後乳汁的分泌與噴出是由不同的激素控制。泌乳素（prolactin）由腦下垂體前葉分泌，負責刺激乳腺細胞合成乳汁；而催產素（oxytocin）由腦下垂體後葉釋放，因嬰兒吸吮乳頭反射性分泌，負責促使乳腺管周圍的肌上皮細胞收縮，從而引發噴乳反射，故選B。多巴胺會抑制泌乳素分泌。",
      "flashcard_front": "泌乳與噴乳 / 泌乳素 (Prolactin) / 催產素 (Oxytocin) / 肌上皮細胞",
      "flashcard_back": "泌乳素（垂體前葉）負責乳汁合成與分泌；催產素（垂體後葉）刺激肌上皮細胞收縮引發「噴乳反射」。",
      "flashcard_summary": "泌乳與噴乳激素 -> 泌乳素刺激乳汁分泌，催產素引起噴乳反射。"
    },
    {
      "question_id": "109-1_medicine-6_032",
      "question_number": 32,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "胎兒無壓力測試（NST）的判讀標準。",
      "explanation": "胎兒無壓力測試（NST）是藉由監測胎動時胎兒心跳的加速來評估胎兒健康。在20分鐘的監測期內，若胎心音加速次數未達2次，且每次加速幅度未達15 bpm或持續未達15秒，即判讀為 Nonreactive（無反應型），提示胎兒可能存在缺氧或處於睡眠狀態，故選D。正常的NST應在20分鐘內有至少2次胎動伴隨心跳加速（>=15 bpm且持續>=15秒）。",
      "flashcard_front": "NST 判讀 / 20分鐘 / 胎心音加速 / Reactive vs Nonreactive",
      "flashcard_back": "20分鐘內至少有2次胎心加速（幅度>=15 bpm, 持續>=15秒）為Reactive；若未達標則為Nonreactive，需進一步評估。",
      "flashcard_summary": "NST判讀標準 -> 20分鐘內有至少2次振幅>=15 bpm且持續>=15秒之加速為Reactive，否則為Nonreactive。"
    },
    {
      "question_id": "109-1_medicine-6_033",
      "question_number": 33,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "胎兒生物生理評估（BPP）中胎兒呼吸項目的評分標準。",
      "explanation": "在胎兒生物生理評估（BPP）中，胎兒呼吸運動的正常標準為：在30分鐘的超音波連續觀察中，胎兒有至少1次持續30秒以上的規律呼吸運動。若符合此標準，該項目即可獲得 2分（BPP各單項僅評0分或2分，無1分或3分），因此本題中胎兒有5次每次持續30秒以上的呼吸，符合正常標準，得分為2分，故選C。",
      "flashcard_front": "BPP 評分 / 胎兒呼吸 / 30分鐘 / 評分級距",
      "flashcard_back": "BPP各單項評分僅有0分（異常）或2分（正常）；呼吸正常標準為30分鐘內有至少1次持續30秒以上的呼吸運動。",
      "flashcard_summary": "BPP呼吸評分 -> 30分鐘內有至少一次持續>=30秒呼吸即可得2分，無1分或3分之評級。"
    },
    {
      "question_id": "109-1_medicine-6_034",
      "question_number": 34,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "女性尿失禁的流行病學與分類。",
      "explanation": "在女性患者中，應力性尿失禁（Stress Urinary Incontinence, SUI）是最常見的尿失禁類型，約占所有病例的一半。SUI通常是由於生產、老化導致骨盆底肌肉鬆弛或尿道括約肌功能不全，使得患者在腹壓增加（如咳嗽、打噴嚏、大笑或運動）時，尿液會不自主漏出，故選B。急迫性尿失禁和混合型尿失禁也常見，但單純SUI盛行率最高。",
      "flashcard_front": "女性尿失禁 / 腹壓增加 / 骨盆底鬆弛 / 應力性尿失禁 (SUI)",
      "flashcard_back": "應力性尿失禁（SUI）是女性最常見的尿失禁類型，因骨盆底支持結構鬆弛，在咳嗽等腹壓增加時漏尿。",
      "flashcard_summary": "女性最常見尿失禁 -> 應力性尿失禁（SUI）為女性最常見類型，與腹壓增高及骨盆底鬆弛有關。"
    },
    {
      "question_id": "109-1_medicine-6_035",
      "question_number": 35,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "敗血症引起的急性呼吸窘迫症候群（ARDS）之病理生理學。",
      "explanation": "當患者因敗血症引發全身性發炎反應，導致肺泡-毛細血管膜受損、通透性急劇增加，並產生富含蛋白質的滲出性肺泡水腫，臨床上會引起急性進行性低血氧症與雙側肺浸潤，此臨床綜合徵稱為急性呼吸窘迫症候群（ARDS），故選D。ARDS是敗血症患者致命的嚴重肺部併發症之一。",
      "flashcard_front": "敗血症 / 肺泡毛細血管膜受損 / 通透性增加 / ARDS",
      "flashcard_back": "敗血症引發的肺毛細血管通透性增加及非心因性肺水腫，會造成急性呼吸窘迫症候群（ARDS）。",
      "flashcard_summary": "敗血症致ARDS -> 敗血症引發肺毛細血管通透性增高，造成急性呼吸窘迫症候群（ARDS）。"
    },
    {
      "question_id": "109-1_medicine-6_036",
      "question_number": 36,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "無精蟲症的臨床診斷步驟與確認流程。",
      "explanation": "單次精液分析若發現無精蟲症（azoospermia），因可能受到近期生病、發燒或檢體收集不完全等暫時性因素干擾，不應立即下診斷，最恰當的處置是建議患者間隔數星期後進行第二次精液分析以確認診斷，並可抽血檢測FSH、LH與睪固酮以做初步評估，故選A。睪丸切片及人工生殖應在重複確認無精蟲症並完成病因診斷後再行考慮。",
      "flashcard_front": "單次無精蟲 / 診斷流程 / 重複檢驗 / 睪丸切片時機",
      "flashcard_back": "單次精液檢驗發現無精蟲不能直接確診，應於數週後重複檢查確認；睪丸切片等侵入性檢查不列為首步處置。",
      "flashcard_summary": "無精蟲症初步處置 -> 單次檢出無精蟲應於數週後複檢以排除暫時性干擾，不可立即做侵入性檢查。"
    },
    {
      "question_id": "109-1_medicine-6_037",
      "question_number": 37,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "繼發性無月經的定義與病因診斷流程。",
      "explanation": "在婦產科診斷中，繼發性無月經（secondary amenorrhea）的定義是：原本月經規律的女性連續3個月以上無月經，或原本月經不規律者連續6個月以上無月經，並非2個月月經沒來，故A選項敘述錯誤。評估任何生育年齡女性的無月經，首要步驟皆為排除懷孕（B正確）；高泌乳血症會抑制GnRH脈衝分泌進而導致無月經（D正確）；結構異常比例確實較少（C正確）。",
      "flashcard_front": "繼發性無月經 / 定義 / 排除懷孕 / 高泌乳血症",
      "flashcard_back": "繼發性無月經定義為原規律者停經3個月或不規律者停經6個月；評估首步是排除懷孕，高泌乳素血症是常見病因。",
      "flashcard_summary": "繼發性無月經定義 -> 規律者停經3個月或不規律者停經6個月以上，評估首步是排除懷孕。"
    },
    {
      "question_id": "109-1_medicine-6_038",
      "question_number": 38,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "口服排卵藥Clomiphene citrate的作用機轉與適應症限制。",
      "explanation": "口服排卵藥 Clomiphene citrate（CC）是藉由阻斷下視丘的氣味受體，使下視丘誤判體內雌激素不足，進而增加GnRH脈衝分泌，刺激腦下垂體釋放FSH/LH來誘導排卵。因此，CC的發揮作用必須依賴功能完整的下視丘-腦下垂體軸。當患者存在下視丘-腦下垂體功能衰竭時，由於無法分泌促性腺激素，CC治療一定無效，故B選項正確。此時需直接給予外源性促性腺激素治療。",
      "flashcard_front": "Clomiphene (CC) / 下視丘-腦下垂體衰竭 / 排卵機制 / 促性腺激素",
      "flashcard_back": "CC藉由阻斷下視丘雌激素受體促使FSH分泌，故對下視丘-腦下垂體功能衰竭者無效（因無法分泌FSH/LH），此時需直接注射促性腺激素。",
      "flashcard_summary": "Clomiphene無效指徵 -> CC需依賴正常的下視丘-腦下垂體軸，對下視丘-腦下垂體衰竭者一定無效。"
    },
    {
      "question_id": "109-1_medicine-6_039",
      "question_number": 39,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "子宮頸癌FIGO臨床分期標準。",
      "explanation": "根據FIGO子宮頸癌分期系統，當腫瘤侵犯至「下1/3陰道」（lower third of the vagina），且未侵犯至骨盆壁時，此期別被明確定義為 IIIa期，故選D。相對地，若侵犯陰道但局限於上2/3且無子宮旁侵犯，當腫瘤大於4公分為IIa2期；若有子宮旁侵犯但未達骨盆壁為IIb期。",
      "flashcard_front": "子宮頸癌 / 陰道下1/3侵犯 / FIGO分期 / IIIa期",
      "flashcard_back": "子宮頸癌腫瘤侵犯累及陰道下1/3（不論大小），且無子宮旁/骨盆壁侵犯者，分期為FIGO IIIa期。",
      "flashcard_summary": "子宮頸癌IIIa期定義 -> 腫瘤侵犯至陰道下1/3且無骨盆壁浸潤者，為FIGO IIIa期。"
    },
    {
      "question_id": "109-1_medicine-6_040",
      "question_number": 40,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "唐氏症篩檢之生化與超音波指標。",
      "explanation": "第一孕期母血唐氏症篩檢（約在懷孕11至13加6週進行）包含的項目為：超音波測量胎兒頸部透明帶（NT）以及抽取母血檢測游離貝他人類絨毛膜性腺激素（free β-hCG）與妊娠相關血漿蛋白-A（PAPP-A）。非游離雌三醇（uE3）是「第二孕期」唐氏症四合一篩檢所包含的項目，而非第一孕期，故選C。",
      "flashcard_front": "第一孕期唐氏症篩檢 / 頸部透明帶 (NT) / free β-hCG / PAPP-A / uE3 時機",
      "flashcard_back": "第一孕期篩檢包含NT、free β-hCG及PAPP-A；uE3及甲型胎兒蛋白（AFP）則屬於第二孕期四合一篩檢項目。",
      "flashcard_summary": "第一孕期唐氏篩檢指標 -> 包含NT、free β-hCG及PAPP-A，uE3為第二孕期指標。"
    },
    {
      "question_id": "109-1_medicine-6_041",
      "question_number": 41,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "雙胞胎輸血症候群的病理生理與超音波特徵。",
      "explanation": "此病例為經典的雙胞胎輸血症候群（TTTS），發生於單絨毛膜雙胞胎。由於胎盤內血管吻合導致血液分配失衡，受贈者（recipient twin，體重大、羊水多）會出現多尿、羊水過多與充血性心衰竭；而捐贈者（donor twin，體重小、羊水少）則會出現寡尿、羊水過少、脫水及貧血。藉由超音波，可以觀察到兩者體重差異、羊水量對比及胎兒水腫等明顯表徵（phenotype）差異，故D正確。捐贈者發生貧血而非溶血性貧血，受贈者發生紅血球增多症。",
      "flashcard_front": "TTTS / 雙胞胎輸血症候群 / 捐贈者與受贈者 / 羊水多寡",
      "flashcard_back": "TTTS中，受贈胎兒體重大、多尿致羊水過多，易紅血球增多及心衰竭；捐贈胎兒體重小、寡尿致羊水過少及貧血。超音波可辨識此表徵差異。",
      "flashcard_summary": "TTTS特徵 -> 受贈者體重大且羊水過多，捐贈者體重小且羊水過少，超音波可見此表徵差異。"
    },
    {
      "question_id": "109-1_medicine-6_042",
      "question_number": 42,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "重度子癇前症的診斷標準與急症處置原則。",
      "explanation": "該孕婦血壓高達 172/116 mmHg，且伴隨尿蛋白 3+ 及短時間內體重快速增加，已符合重度子癇前症（preeclampsia with severe features）的診斷標準，且伴有不規則宮縮（先兆早產跡象）。重度子癇前症隨時可能惡化為子癇症、胎盤早期剝離或HELLP症候群，危及母嬰生命，因此最安全且最佳的處置是立即住院接受治療，控制血壓並預防抽搐，故選D。",
      "flashcard_front": "重度子癇前症 / 診斷指標 / 住院治療 / 硫酸鎂預防",
      "flashcard_back": "血壓 >= 160/110 mmHg 且有蛋白尿等症狀即診斷為重度子癇前症，有高度母嬰危險，必須立即住院治療並投予硫酸鎂預防癲癇。",
      "flashcard_summary": "重度子癇前症處置 -> 血壓達160/110以上屬重度，需立即住院並投予硫酸鎂，不宜門診追蹤。"
    },
    {
      "question_id": "109-1_medicine-6_043",
      "question_number": 43,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "Burch陰道懸吊術與恥骨後間隙的解剖構造標示。",
      "explanation": "Burch陰道懸吊術（Burch colposuspension）是治療女性應力性尿失禁的經典手術。手術中是將尿道兩側的陰道周圍筋膜縫合懸吊至雙側恥骨梳韌帶（iliopectineal ligament，又稱為 Cooper's ligament）。在恥骨後間隙（space of Retzius）的解剖視野中，位於骨盆側壁、恥骨上支後緣的緻密白色韌帶即為 Cooper's ligament，圖中標示為 C，故選C。",
      "flashcard_front": "Burch 手術 / 擺尿失禁 / 懸吊位置 / Cooper's ligament",
      "flashcard_back": "Burch陰道懸吊術是將尿道旁的筋膜縫合固定於雙側的Cooper's ligament（即iliopectineal ligament）。",
      "flashcard_summary": "Burch手術固定位置 -> 縫合懸吊於恥骨梳韌帶（Cooper's ligament）。"
    },
    {
      "question_id": "109-1_medicine-6_044",
      "question_number": 44,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "子宮外孕的治療預後比較及早期妊娠hCG變化規律。",
      "explanation": "對於輸卵管子宮外孕患者，接受單次藥物（Methotrexate, MTX）保守治療能完全保留輸卵管結構且無手術瘢痕，其後續的輸卵管通暢率及再次子宮外孕的風險，與接受手術保守治療（輸卵管造口術）的患者相比並無顯著差異，因此B選項「再次外孕風險尤高」的敘述錯誤。骨盆腔發炎是子宮外孕的危險因子（A正確）；正常早期懷孕hCG 48小時應增加至少66%以上（C正確）。",
      "flashcard_front": "子宮外孕 / MTX 治療 / 輸卵管造口 / 再次外孕風險 / hCG 翻倍",
      "flashcard_back": "MTX藥物治療與輸卵管造口手術相比，再次子宮外孕的風險相似；正常早期妊娠hCG在48小時內應上升至少66%。",
      "flashcard_summary": "子宮外孕治療與hCG -> MTX與手術造口術後再次外孕風險相似；正常懷孕hCG在48小時內應上升66%以上。"
    },
    {
      "question_id": "109-1_medicine-6_045",
      "question_number": 45,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "子宮內膜異位症的診斷金標準。",
      "explanation": "子宮內膜異位症的確診金標準是進行「腹腔鏡檢查並進行病理切片（laparoscopy with biopsy）」，在直視下觀察到典型的子宮內膜樣病灶並經病理證實，故選D。超音波（A）僅能診斷較大的巧克力囊腫，無法診斷腹膜散在病灶；理學檢查（B）及血清CA-125升高（C）雖然有助於診斷，但不具特異性，無法作為確定診斷。",
      "flashcard_front": "子宮內膜異位 / 確定診斷 / 診斷金標準 / 腹腔鏡切片",
      "flashcard_back": "子宮內膜異位症的確定診斷需透過腹腔鏡手術直視病灶並進行病理切片；超音波與CA-125僅具輔助診斷價值。",
      "flashcard_summary": "子宮內膜異位確診 -> 診斷金標準為腹腔鏡檢查併病理切片。"
    }
  ]
}

# ----------------------------------------------------
# 109-1_medicine-6_batch-004 (Q46-60)
# ----------------------------------------------------
batches_data["109-1_medicine-6_batch-004"] = {
  "dataset_id": "109-1_medicine-6",
  "batch_id": "109-1_medicine-6_batch-004",
  "items": [
    {
      "question_id": "109-1_medicine-6_046",
      "question_number": 46,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "卵巢上皮癌的病理分型與臨床預後特徵。",
      "explanation": "在漿液性（serous）卵巢上皮癌中，沙狀瘤體（Psammoma bodies）是一種同心圓狀的鈣化結構。研究表明，在卵巢漿液性癌中，若見到大量的沙狀瘤體，通常是低惡性度（low-grade）或交界性漿液性腫瘤的特徵，或者是病情進展較慢、生長遲緩的表現，通常與較好的預後相關，而非代表預後極差，故D選項敘述最不適當。子宮內膜異位症與卵巢清亮細胞癌和類子宮內膜癌有強烈相關性；清亮細胞癌在病理分級上直接歸類為高惡性度（grade 3）。",
      "flashcard_front": "卵巢上皮癌 / 沙狀瘤體 / 子宮內膜異位 / 清亮細胞癌級別",
      "flashcard_back": "大量沙狀瘤體多見於低惡性度漿液性癌，提示預後較好而非極差；子宮內膜異位症與清亮細胞癌及類子宮內膜癌有關。",
      "flashcard_summary": "卵巢癌病理特徵 -> 大量沙狀瘤體通常提示預後較好；子宮內膜異位與清亮細胞及類子宮內膜卵巢癌有關。"
    },
    {
      "question_id": "109-1_medicine-6_047",
      "question_number": 47,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "卵巢生殖細胞腫瘤的組織病理特徵。",
      "explanation": "題目英文病理描述：「細胞大、圓形或多角形，含有豐富且清亮/淡染的細胞質，核大且不規則，具有明顯的核仁。」這是無性細胞瘤（Dysgerminoma，又稱無性胚胎瘤）最經典的組織學特徵，且其間質常有淋巴細胞浸潤，故選B。無性細胞瘤是年輕女性最常見的卵巢生殖細胞腫瘤。Sertoli-Leydig細胞瘤表現為小管結構；顆粒細胞瘤典型特徵為Call-Exner bodies與咖啡豆樣核；內胚層竇瘤則可見Schiller-Duval bodies。",
      "flashcard_front": "卵巢腫瘤病理 / 無性細胞瘤 / dysgerminoma / 豐富清亮胞質 / 大核仁",
      "flashcard_back": "鏡下見細胞大、胞質豐富清亮、核大且有明顯核仁，是無性細胞瘤（dysgerminoma）的典型病理描述，多見於年輕女性。",
      "flashcard_summary": "無性細胞瘤病理 -> 細胞大、胞質清亮、核大有明顯核仁為無性細胞瘤（dysgerminoma）特徵。"
    },
    {
      "question_id": "109-1_medicine-6_048",
      "question_number": 48,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "卵巢週期與子宮內膜周期的同步對應關係。",
      "explanation": "女性月經週期中，卵巢週期與子宮內膜週期在時間上是同步對應的。排卵前的「卵巢濾泡期」由雌激素主導，對應子宮內膜的「增生期」；排卵後的「卵巢黃體期」由黃體素主導，對應子宮內膜的「分泌期」（而非增生期，故B錯誤）。排卵後，殘餘的濾泡顆粒細胞和卵囊膜細胞會黃體化，開始大量分泌黃體素（D正確）。",
      "flashcard_front": "月經週期對應 / 濾泡期 / 增生期 / 黃體期 / 分泌期",
      "flashcard_back": "濾泡期（雌激素為主）對應內膜的增生期；黃體期（黃體素為主）對應內膜的分泌期，而非增生期。",
      "flashcard_summary": "月經週期同步對應 -> 濾泡期相當於內膜增生期，黃體期相當於內膜分泌期。"
    },
    {
      "question_id": "109-1_medicine-6_049",
      "question_number": 49,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "卵巢性激素合成的雙細胞雙促性腺激素假說。",
      "explanation": "根據卵巢類固醇合成的「雙細胞雙促性腺激素假說」：1. 卵囊膜細胞（Theca cells）主要受黃體化激素（LH）的刺激，將膽固醇轉化為雄性素；2. 顆粒細胞（Granulosa cells）主要受濾泡刺激素（FSH）的刺激，藉由其內的芳香環轉化酶將雄性素轉化為雌激素。因此，B選項中「theca cells受FSH刺激製造雄性素」的敘述錯誤，應為受LH刺激。",
      "flashcard_front": "雙細胞雙激素 / Theca cells / Granulosa cells / LH與FSH / 雄性素合成",
      "flashcard_back": "Theca cells受LH刺激合成雄性素；Granulosa cells受FSH刺激，利用aromatase將雄性素轉化為雌激素。",
      "flashcard_summary": "雙細胞雙激素假說 -> Theca細胞受LH刺激產生雄性素，Granulosa細胞受FSH刺激將其轉化為雌激素。"
    },
    {
      "question_id": "109-1_medicine-6_050",
      "question_number": 50,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "激素受體的定位分類。",
      "explanation": "人類絨毛膜性腺刺激素（hCG）是一種醣蛋白質類的蛋白質性激素。由於蛋白質激素分子量大且具親水性，無法穿過雙層脂質細胞膜，因此其受體是位於細胞膜上（屬於G蛋白偶聯受體），而非存在於細胞核中，故C選項敘述錯誤。類固醇激素（如雌、孕激素，A正確）及甲狀腺素（D正確）其受體主要位於細胞核內（或細胞質內）。",
      "flashcard_front": "蛋白質激素 / 類固醇受體 / hCG 受體 / 細胞核 vs 細胞膜",
      "flashcard_back": "類固醇與甲狀腺激素受體位於細胞核（內）調控基因；hCG及蛋白質激素受體則位於細胞膜上。",
      "flashcard_summary": "激素受體定位 -> hCG及蛋白質激素受體位於細胞膜，類固醇及甲狀腺激素受體位於細胞核。"
    },
    {
      "question_id": "109-1_medicine-6_051",
      "question_number": 51,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "下視丘GnRH的結構、釋放模式與生理作用。",
      "explanation": "促性腺激素釋放激素（GnRH）由下視丘分泌，其主要功能是「同時刺激」腦下垂體前葉分泌FSH與LH，其分泌的比例與脈衝頻率有關，而非只能刺激LH，故A選項敘述錯誤。GnRH確實以脈衝性方式釋放（B正確），為十肽結構（C正確），且在體內極不穩定，半衰期僅2-4分鐘（D正確）。",
      "flashcard_front": "GnRH / 促性腺激素釋放 / FSH與LH / 脈衝分泌 / 半衰期",
      "flashcard_back": "GnRH由下視丘分泌，可同時刺激腦下垂體釋放FSH與LH；其分泌呈脈衝性，半衰期僅2-4分鐘。",
      "flashcard_summary": "GnRH生理特性 -> 同時刺激垂體釋放FSH與LH，分泌呈脈衝性，半衰期短（2-4分鐘）。"
    },
    {
      "question_id": "109-1_medicine-6_052",
      "question_number": 52,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "不孕症常見病因的流行病學。",
      "explanation": "在不孕症的常見病因中，排卵障礙（約佔25-30%）、男性因素（約佔30-40%）及輸卵管/骨盆腔因素（約佔20-30%）是引致不孕最常見的三大主因。相較之下，子宮肌瘤雖然在生育年齡女性中盛行率很高，但絕大多數肌瘤患者仍能正常受孕，肌瘤直接導致不孕的比率相對較低（僅約2-3%），故選C。",
      "flashcard_front": "不孕症病因 / 盛行率 / 排卵障礙 / 輸卵管阻塞 / 子宮肌瘤",
      "flashcard_back": "不孕症三大主因為男性因素、排卵障礙及輸卵管問題；子宮肌瘤雖常見，但直接導致不孕的比例相對較少。",
      "flashcard_summary": "不孕症主要病因 -> 男性因素、排卵障礙及輸卵管病變為三大主因，子宮肌瘤直接致不孕的比例較低。"
    },
    {
      "question_id": "109-1_medicine-6_053",
      "question_number": 53,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "多囊性卵巢症候群無生育要求患者的治療原則。",
      "explanation": "該患者臨床表現（肥胖、稀發月經、超音波示竇卵泡增多及內膜增厚）高度符合多囊性卵巢症候群（PCOS）。由於患者目前無生育考量且無性經驗，此時給予口服排卵藥（如Clomiphene）是最不合適的，因為排卵藥是用於治療PCOS患者的不孕症，對無生育需求者無治療必要，故選A。此時的處置重點是：給予黃體素保護子宮內膜免於過度增生、減重與生活習慣調整以及篩檢胰島素抗性。",
      "flashcard_front": "PCOS / 肥胖 / 無生育考量 / 內膜增厚 / 治療原則 / 排卵藥",
      "flashcard_back": "PCOS無生育考量者治療以減重、保護內膜（給予黃體素催經）及監測代謝為主，不應給予排卵藥（排卵藥僅用於不孕症治療）。",
      "flashcard_summary": "PCOS無生育期治療 -> 首選減重與黃體素保護內膜，無生育需求者不給排卵藥。"
    },
    {
      "question_id": "109-1_medicine-6_054",
      "question_number": 54,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "雌激素在濾泡期的反饋機制及LH surge的生理作用。",
      "explanation": "在月經週期中：1. 雌激素在濾泡期逐漸上升，會對下視丘/腦下垂體產生負回饋，抑制FSH分泌（此為Hormone X）；2. 當濾泡成熟，雌激素濃度持續維持在高水平時，回饋機制會轉變為正回饋，進而誘發LH surge（此為Hormone Y）。3. LH surge（此為Hormone Z）會促使初級卵母細胞完成第一次減數分裂，轉變為次級卵母細胞並排出。因此，Hormone X與Hormone Y皆為雌激素，兩者相同，故選A。",
      "flashcard_front": "雌激素回饋 / 負回饋 FSH / 正回饋 LH surge / 減數分裂",
      "flashcard_back": "濾泡期中低濃度的雌激素負回饋抑制FSH，持續高濃度雌激素正回饋誘發LH surge；LH surge進而促使初級卵細胞完成第一次減數分裂。",
      "flashcard_summary": "雌激素反饋機制 -> 濾泡期雌激素負回饋抑制FSH，高濃度時正回饋誘發LH surge。"
    },
    {
      "question_id": "109-1_medicine-6_055",
      "question_number": 55,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "人工輔助生殖技術的分類與操作步驟。",
      "explanation": "人工授精（IUI）是將洗滌篩選後的精子直接注入女性子宮腔內，讓其在體內自然受精，因此完全不需要對女性進行手術取卵，故選A。相對地，試管嬰兒（IVF）、單精子顯微注射（ICSI）以及胚胎著床前基因診斷（PGD）皆屬於體外受精與胚胎培養技術，必須先進行促排卵及手術取卵。",
      "flashcard_front": "人工生殖 / 不需取卵 / 人工授精 (IUI) / 體外受精 (IVF)",
      "flashcard_back": "人工授精（IUI）是在體內受精，不需取卵；IVF、ICSI及PGD皆需手術取卵以在體外進行受精與培養。",
      "flashcard_summary": "人工生殖分類 -> 人工授精（IUI）於體內受精，不需取卵；體外受精（IVF/ICSI）則必須取卵。"
    },
    {
      "question_id": "109-1_medicine-6_056",
      "question_number": 56,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "胎兒都卜勒超音波檢查波形與臨床應用。",
      "explanation": "本題考查胎兒多普勒（Doppler）超音波評估。在孕晚期評估胎盤功能時，最常進行的篩檢是測量 臍動脈血流速度波形（umbilical artery velocity waveform）。臍動脈多普勒波形典型呈現鋸齒狀的動脈搏動波形，可用於計算收縮期與舒張期血流比值（S/D比值），以評估胎盤阻力，故選A。",
      "flashcard_front": "胎兒多普勒 / 臍動脈血流 / 鋸齒狀波形 / 胎盤阻力",
      "flashcard_back": "評估胎盤血流灌注首選臍動脈血流速度波形檢查；波形典型呈鋸齒狀，用於計算S/D比值以評估阻力。",
      "flashcard_summary": "臍動脈都卜勒檢查 -> 最常用於評估胎盤灌流阻力的多普勒檢查，波形呈鋸齒狀。"
    },
    {
      "question_id": "109-1_medicine-6_057",
      "question_number": 57,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "臍動脈都卜勒舒張末期血流反向的臨床意義。",
      "explanation": "當胎盤血管阻力極高（胎盤功能嚴重衰竭）時，在心臟舒張期時，血液不僅無法向前流動，甚至會逆流回胎兒體內，此時多普勒波形會呈現「舒張末期血流逆流（Reversed end-diastolic velocity, REDV）」，在影像上表現為舒張期波形反向低於基線。REDV是胎兒宮內窘迫、瀕臨酸中毒或死亡的危急指標，必須考慮立即終止妊娠，故選B。",
      "flashcard_front": "臍動脈多普勒 / 舒張末期血流逆流 / REDV / 胎兒危急",
      "flashcard_back": "臍動脈都卜勒出現舒張末期血流逆流（REDV，波形低於基線）提示胎盤功能極度受損，是胎兒宮內窘迫、需緊急分娩的危急指徵。",
      "flashcard_summary": "臍動脈REDV意義 -> 舒張末期血流逆流（REDV）提示胎盤阻力極高，是需立即生產的胎兒危急指徵。"
    },
    {
      "question_id": "109-1_medicine-6_058",
      "question_number": 58,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "中風後複雜區域疼痛症候群第一型的受累特徵。",
      "explanation": "偏癱後複雜區域疼痛症候群第一型（CRPS Type 1，又稱肩手症候群）是腦中風患者常見的慢性疼痛併發症。其特徵是主要累及「肩膀」與「手腕/手指」，表現為肩膀疼痛與關節活動受限，以及手部腫脹與慢性疼痛；而肘關節的受累程度與受影響機率在臨床上相對罕見且顯著較少，故選B。",
      "flashcard_front": "偏癱後 CRPS Type 1 / 肩手症候群 / 肘關節受累 / 臨床表現",
      "flashcard_back": "偏癱後CRPS Type 1主要侵犯同側肩膀與手部（肩手症候群），表現為肩痛及手部腫痛，肘關節受累相對稀少。",
      "flashcard_summary": "偏癱後CRPS受累部位 -> 主要影響肩膀與手部，肘部受影響相對較少。"
    },
    {
      "question_id": "109-1_medicine-6_059",
      "question_number": 59,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "脊髓損傷患者自主神經反射異常的病生理特徵。",
      "explanation": "自主神經反射異常（Autonomic dysreflexia, AD）通常發生在脊髓損傷過後的慢性期（大多在受傷數月、脊髓休克期結束且反射恢復後才開始發生），極少在受傷後一個月內的急性脊髓休克期發生，故A選項敘述錯誤。AD主要見於T6以上的高位脊髓損傷患者；最常見的誘因是膀胱脹尿或直腸便秘；急性發作時，首步處置是將患者坐起並迅速尋找並移除誘發刺激，故選A。",
      "flashcard_front": "自主神經反射異常 (AD) / 脊髓損傷 / T6以上 / 發生時機 / 膀胱脹尿",
      "flashcard_back": "AD發生於脊髓損傷數月後的慢性期（非1個月內）；由T6以上損傷及膀胱脹尿等下位刺激引起，發作時需坐起並立刻移除刺激。",
      "flashcard_summary": "自主神經反射異常特性 -> 發生在損傷數月後（慢性期），由T6以上損傷及下位刺激（如脹尿）引起，首步需移除刺激。"
    },
    {
      "question_id": "109-1_medicine-6_060",
      "question_number": 60,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "反射性勃起與心理性勃起的自主神經支配與脊髓節段。",
      "explanation": "男性的反射性勃起（reflexogenic erection）是指外生殖器受到直接的觸覺等物理刺激時，刺激經由陰部神經傳入，直接通過薦椎反射弧，由S2-S4薦髓發源的副交感神經（骨盆神經）傳出，支配陰莖海綿體血管舒張所引起的勃起，因此是由副交感神經系統（源自S2-S4）控制，故選B。相對地，由大腦性幻想引起的心理性勃起（psychogenic erection）則主要由T11-L2的交感神經（下腹神經）通路介導。",
      "flashcard_front": "反射性勃起 / 心理性勃起 / S2-S4 副交感 / 骨盆神經",
      "flashcard_back": "反射性勃起由外陰部直接刺激引起，經S2-S4薦髓的副交感神經（骨盆神經）控制；心理性勃起則由T11-L2交感神經控制。",
      "flashcard_summary": "反射性勃起控制 -> 反射性勃起由源自S2-S4之副交感神經（骨盆神經）控制。"
    }
  ]
}

# Write medicine-6 batches
for b_id in ["109-1_medicine-6_batch-001", "109-1_medicine-6_batch-002", "109-1_medicine-6_batch-003", "109-1_medicine-6_batch-004"]:
    o_path = f"reports/gemini_outputs/{b_id}.json"
    with open(o_path, "w", encoding="utf-8") as f:
        json.dump(batches_data[b_id], f, ensure_ascii=False, indent=2)
    print(f"Wrote {o_path}")
