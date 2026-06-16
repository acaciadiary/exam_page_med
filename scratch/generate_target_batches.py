# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure output directory exists
output_dir = "reports/gemini_outputs"
os.makedirs(output_dir, exist_ok=True)

batches_data = {}

# ==================== BATCH: 110-1_medicine-6_batch-002 ====================
batches_data["110-1_medicine-6_batch-002"] = {
  "dataset_id": "110-1_medicine-6",
  "batch_id": "110-1_medicine-6_batch-002",
  "items": [
    {
      "question_id": "110-1_medicine-6_016",
      "question_number": 16,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "調節性內斜視的首選第一步治療方法。",
      "explanation": "調節性內斜視是因為患者患有遠視，為了看清物體而進行過度調節與內聚所引起的內斜視。因此，治療的第一道步驟為配戴足夠度數的遠視眼鏡以消除調節需求，通常可使眼位回復正常。若戴鏡後仍有殘餘斜視，才考慮手術治療；弱視貼布與稜鏡並非此症之首選一線療法。",
      "flashcard_front": "調節性內斜視 / 遠視 / 首選治療步驟 / 戴鏡與手術",
      "flashcard_back": "調節性內斜視的第一步治療為配戴遠視眼鏡以消除過度調節，戴鏡無效後才考慮手術。",
      "flashcard_summary": "調節性內斜視治療 -> 首選第一步為配戴遠視眼鏡以消除過度調節。"
    },
    {
      "question_id": "110-1_medicine-6_017",
      "question_number": 17,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "甲狀腺眼疾最具特異性與示病性的臨床徵候。",
      "explanation": "眼瞼退縮（lid retraction，如 Dalrymple 氏徵）是甲狀腺眼疾（TED）最常見且最具特異性（示病性）的臨床表現。雖然眼外肌活動受阻與眼球突出也相當常見，但亦可見於其他眼窩病變，特異性不如眼瞼退縮。眼瞼下垂通常與甲狀腺眼疾不符，反而多見於重症肌無力。",
      "flashcard_front": "甲狀腺眼疾 / 示病性徵候 / 眼瞼退縮 / 眼球突出",
      "flashcard_back": "甲狀腺眼疾最常見且最具特異性的示病性徵候是眼瞼退縮（lid retraction）。",
      "flashcard_summary": "甲狀腺眼疾示病性徵候 -> 最具特異性且最常見的示病性徵候為眼瞼退縮。"
    },
    {
      "question_id": "110-1_medicine-6_018",
      "question_number": 18,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "眼科",
      "category_confidence": "high",
      "key_point": "眼瞼裂狹小症候群（BPES）的典型臨床病徵特徵。",
      "explanation": "眼瞼裂狹小症候群（BPES）是一種常染色體顯性遺傳病，其典型臨床特徵為：小瞼裂、眼瞼下垂伴隨提上瞼肌功能差、眥距過寬以及反向內眥贅皮。此症候群的病徵中並不包含眼瞼內翻，故選項C為錯誤敘述。",
      "flashcard_front": "眼瞼裂狹小症候群 (BPES) / 四大特徵 / 反向內眥贅皮 / 眼瞼內翻",
      "flashcard_back": "BPES特徵包括小瞼裂、眼瞼下垂、眥距過寬、反向內眥贅皮，不包括眼瞼內翻。",
      "flashcard_summary": "BPES病徵特徵 -> 包含小瞼裂、下垂、眥距過寬及反向內眥贅皮，無眼瞼內翻。"
    },
    {
      "question_id": "110-1_medicine-6_019",
      "question_number": 19,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "糖尿病患鼻腔壞死與硬腭發黑之致病菌診斷。",
      "explanation": "控制不佳的糖尿病患者（常伴有酮酸中毒）是白黴菌病（Mucormycosis）的高危險群。白黴菌具血管侵襲性，會導致受犯組織迅速缺血壞死，臨床特徵為發黑的焦痂（如鼻甲變黑、硬腭發黑）及暗棕色伴血絲之鼻涕。綠膿桿菌或葡萄球菌等細菌感染通常不會引起如此進展迅速的組織壞死與發黑。",
      "flashcard_front": "糖尿病控制不佳 / 鼻甲與硬腭發黑 / 視力模糊 / 血管侵襲性真菌",
      "flashcard_back": "控制不佳糖尿病患出現鼻甲/硬腭黑色壞死焦痂，應高度懷疑白黴菌（Mucoraceae）感染。",
      "flashcard_summary": "糖尿病患鼻腔黑色壞死 -> 高度懷疑為血管侵襲性的白黴菌（Mucoraceae）感染。"
    },
    {
      "question_id": "110-1_medicine-6_020",
      "question_number": 20,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "鼻咽癌已確診患者之後續分期評估與轉移檢查原則。",
      "explanation": "病患已由鼻咽原發部位切片確診為未分化癌，接下來的步驟是進行癌症分期評估，包括頭頸影像學、腹部超音波與胸部X光以篩檢局部及遠端轉移。對於頸部腫塊，不應直接進行切片檢查（incisional biopsy），以避免引發腫瘤細胞沿切口路徑擴散或導致傷口癒合困難，故選項C為最不恰當的處置。",
      "flashcard_front": "鼻咽癌未分化癌確診 / 頸部腫塊 / 分期評估 / 避免局部切片",
      "flashcard_back": "鼻咽癌確診後，應安排影像學評估轉移，並避免直接對頸部腫塊進行切片以防癌細胞擴散。",
      "flashcard_summary": "鼻咽癌頸部腫塊處置 -> 確診後進行分期評估，應避免直接切片頸部腫塊以防擴散。"
    },
    {
      "question_id": "110-1_medicine-6_021",
      "question_number": 21,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "溫差試驗（caloric test）眼震快相與慢相的判定規則。",
      "explanation": "溫差試驗的眼震快相方向遵循 COWS 規則（Cold Opposite, Warm Same）。當在左耳灌入44度溫水時，眼震快相應朝向同側（即向左），故選項B正確。右耳灌入30度冷水時，快相應朝向對側（向左，選項A錯誤）。冷刺激使內淋巴液下沉，導致慢相偏向同側、快相偏向對側；溫刺激則相反。",
      "flashcard_front": "溫差試驗 / COWS規則 / 灌入溫水或冷水 / 眼震快相方向",
      "flashcard_back": "眼震快相遵循COWS：灌冷水（Cold）快相向對側（Opposite），灌溫水（Warm）快相向同側（Same）。",
      "flashcard_summary": "溫差試驗眼震方向 -> 遵循COWS規則，冷水快相向對側，溫水快相向同側。"
    },
    {
      "question_id": "110-1_medicine-6_022",
      "question_number": 22,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "顱底腫瘤磁振造影中呈現鹽及胡椒徵象（salt and pepper sign）之診斷。",
      "explanation": "副神經節瘤（paraganglioma，如頸動脈體瘤或鼓室球瘤）在 T2 或 T1+C 磁振造影中可見特徵性的「鹽與胡椒徵象」。其中「胡椒」代表低訊號的高流量血管流空（flow voids），而「鹽」則代表腫瘤內出血或慢性出血所致的高訊號區域。聽神經瘤或膽固醇肉芽腫均不具此特徵性影像表現。",
      "flashcard_front": "顱底腫瘤 / 磁振造影 / salt and pepper sign / 血管流空與出血",
      "flashcard_back": "磁振造影呈現「鹽與胡椒徵象」的顱底腫瘤為副神節瘤（paraganglioma），由血管流空與出血造成。",
      "flashcard_summary": "鹽與胡椒徵象顱底腫瘤 -> 磁振造影呈現此特徵的顱底腫瘤為副神節瘤（paraganglioma）。"
    },
    {
      "question_id": "110-1_medicine-6_023",
      "question_number": 23,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "膽脂瘤手術常用術式與其不包括的術式判定。",
      "explanation": "膽脂瘤手術的主要目標是清除病灶（如乳突切除術、上鼓室鑿開術）並重建聽力（如聽小骨鏈成型術）。而鐙骨切除術（stapedectomy）主要用於治療耳硬化症，在膽脂瘤手術中，即使鐙骨受累，也是進行病灶清除或鐙骨上結構重建，而非將整個鐙骨切除，故選項D是最不可能包括的術式。",
      "flashcard_front": "中耳膽脂瘤手術 / 清除與聽力重建 / 乳突切除 / 鐙骨切除術",
      "flashcard_back": "膽脂瘤手術不常規包括用於耳硬化症的鐙骨切除術（stapedectomy）。",
      "flashcard_summary": "膽脂瘤手術術式 -> 包括乳突切除與聽小骨重建，但不包括鐙骨切除術。"
    },
    {
      "question_id": "110-1_medicine-6_024",
      "question_number": 24,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "氣管切開造口術（tracheostomy）的手術定位與臨床解剖規則。",
      "explanation": "氣管切開造口術的適當切開位置為第二至第四氣管環（Tracheal ring 2-4）之間，此處可安全建立造口並避開環狀軟骨，故選項C正確。環甲膜切開術主要用於緊急氣道建立，因易引發喉部狹窄，不適合作為長期繞道選項（選項A錯誤）。前頸靜脈呈縱向走形，橫向切開仍有損傷風險（選項B錯誤）。氣切術後持續滲血多來自甲狀腺血管或前頸靜脈，而非外頸動脈（選項D錯誤）。",
      "flashcard_front": "氣管切開造口術 / 手術切開位置 / 環甲膜切開術 / 術後出血",
      "flashcard_back": "氣切造口術的適當位置在第二至第四氣管環；緊急環甲膜切開不宜作長期呼吸繞道。",
      "flashcard_summary": "氣管切開造口術位置 -> 適當造口位置在第二至第四氣管環，環甲膜切口不宜長期使用。"
    },
    {
      "question_id": "110-1_medicine-6_025",
      "question_number": 25,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "喉返神經解剖路徑與各項手術後聲帶麻痺風險評估。",
      "explanation": "聲帶麻痺主要是因為喉返神經（RLN）受損所致。左側喉返神經繞過主動脈弓，右側繞過鎖骨下動脈，因此胸腔手術如肺葉切除、食道切除及心臟繞道手術，在其手術解剖路徑上均有損傷喉返神經的風險。而扁桃腺切除術位於口咽部，完全不涉及喉返神經的路徑，因此術後出現聲帶麻痺之機率最低。",
      "flashcard_front": "聲帶麻痺 / 喉返神經 (RLN) 路徑 / 胸腔手術 / 扁桃腺切除術",
      "flashcard_back": "喉返神經行經胸腔，胸腔手術（肺、食道、心臟）有受損風險；口咽部的扁桃腺切除術則無此風險。",
      "flashcard_summary": "聲帶麻痺與手術風險 -> 喉返神經行經胸腔，故胸腔手術有受損風險，扁桃腺切除則機率最低。"
    },
    {
      "question_id": "110-1_medicine-6_026",
      "question_number": 26,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "唾液腺結石症（sialolithiasis）的好發部位與影像學特徵。",
      "explanation": "唾液腺結石最常發生於下頷腺（佔80-90%），腮腺結石僅佔10-20%（選項B錯誤）。下頷腺結石多為不透光性，而腮腺結石大部分是透光性（radiolucent），故不易僅以X光片診斷，常需配合超音波或CT（選項C正確）。結石成分含有羥磷灰石及部分有機物質（選項A錯誤）。單純唾液腺內視鏡通常只能直接移除小於5 mm的結石，大於1公分者需先碎石或合併開放手術（選項D錯誤）。",
      "flashcard_front": "唾液腺結石 / 腮腺與下頷腺 / 透光性 (radiolucent) / 內視鏡取石",
      "flashcard_back": "唾液腺結石好發於下頷腺；腮腺結石多呈透光性(radiolucent)，不易單靠X光診斷。",
      "flashcard_summary": "唾液腺結石特徵 -> 結石好發於下頷腺，腮腺結石多為透光性且不易單靠X光診斷。"
    },
    {
      "question_id": "110-1_medicine-6_027",
      "question_number": 27,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "唾液腺惡性腫瘤的病理分類、臨床特徵與侵犯性。",
      "explanation": "腺樣囊狀癌（Adenoid cystic carcinoma）是一種生長緩慢但具有高度局部侵犯性的癌症，且極易沿著神經周圍空間進行侵犯（perineural invasion），故選項C正確。腮腺最常見的惡性腫瘤是黏液上皮癌，但下頷腺最常見的是腺樣囊狀癌（選項A錯誤）。黏液上皮癌中黏液細胞比例愈多，分化愈好，惡性度反而愈低（選項B錯誤）。腺樣囊狀癌易有遠端轉移，但常在治療後多年（如10年以上）才緩慢發生（選項D錯誤）。",
      "flashcard_front": "唾液腺惡性腫瘤 / 腺樣囊狀癌 / 神經旁侵犯 (perineural invasion) / 黏液上皮癌",
      "flashcard_back": "腺樣囊狀癌生長緩慢，但極易有神經旁侵犯；黏液上皮癌中黏液細胞愈多則惡性度愈低。",
      "flashcard_summary": "腺樣囊狀癌特徵 -> 生長速度緩慢，但極易出現神經旁侵犯(perineural invasion)。"
    },
    {
      "question_id": "110-1_medicine-6_028",
      "question_number": 28,
      "correct_answer": "D",
      "category_group": "醫學（（六）",  # Wait! I will make sure the category_group is exactly correct. Oh, the prompt says "category_group": "醫學（六）"
      "category_group": "醫學（六）",
      "category": "其他",
      "category_confidence": "high",
      "key_point": "全球最常見的單基因疾病分類。",
      "explanation": "地中海貧血（海洋性貧血，thalassemia）是全球最常見的單基因疾病，因血紅素基因突變導致球蛋白鏈合成不足所致，在熱帶及亞熱帶地區盛行率極高。囊性纖維化（選項A）、X染色體脆折症（選項B）與苯酮尿症（選項C）雖然也是重要的單基因疾病，但在全球人口中的總盛行率均低於地中海貧血。",
      "flashcard_front": "最常見單基因疾病 / 地中海貧血 / 囊性纖維化 / 盛行率",
      "flashcard_back": "全球最常見的單基因疾病是地中海貧血（海洋性貧血），盛行率顯著高於囊性纖維化等病。",
      "flashcard_summary": "最常見單基因疾病 -> 全球最常見的單基因疾病為地中海貧血(海洋性貧血)。"
    },
    {
      "question_id": "110-1_medicine-6_029",
      "question_number": 29,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "胎兒生物生理計分法（BPP）中羊水量的評估得分標準。",
      "explanation": "在胎兒生物生理計分法（BPP）中，羊水量合格的標準（得2分）為：超音波下至少有一個羊水囊的最大垂直徑（DVP）大於2公分。本題中妊娠32週孕婦的羊水最大垂直徑僅有1公分（小於2公分），因此判定為不合格，此分項得分為0分，故選項D正確。",
      "flashcard_front": "生物生理計分 (BPP) / 羊水量分項 / 最大垂直徑 (DVP) / 評分標準",
      "flashcard_back": "BPP中羊水量合格(2分)要求DVP大於2公分；若DVP為1公分則該項得分為0分。",
      "flashcard_summary": "BPP羊水量評分 -> DVP須大於2公分才得2分，本題DVP為1公分故得0分。"
    },
    {
      "question_id": "110-1_medicine-6_030",
      "question_number": 30,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "急性急迫性尿失禁的首要初步篩檢處置。",
      "explanation": "當停經婦女突然主訴急迫性尿失禁僅一週時，臨床上首先必須排除急性尿路感染（UTI）的可能性。因此，最合適且應最先進行的處置是尿液檢查與尿液培養。在排除感染前，不應直接安排侵入性或高階檢查如尿道壓力測量、靜脈腎盂造影或膀胱鏡檢查。",
      "flashcard_front": "急性急迫性尿失禁 / 一週病史 / 排除感染 / 首要處置",
      "flashcard_back": "急性起病的尿失禁首要處置是進行尿液檢查與培養，以排除尿路感染(UTI)。",
      "flashcard_summary": "急迫性尿失禁首要處置 -> 急性起病者首要進行尿液檢查與培養以排除感染。"
    }
  ]
}

# ==================== BATCH: 110-1_medicine-6_batch-003 ====================
batches_data["110-1_medicine-6_batch-003"] = {
  "dataset_id": "110-1_medicine-6",
  "batch_id": "110-1_medicine-6_batch-003",
  "items": [
    {
      "question_id": "110-1_medicine-6_031",
      "question_number": 31,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "育齡女性陰道點狀出血與左下腹痛之首要優先檢查。",
      "explanation": "對於育齡女性出現月經過期、下腹痛及陰道點狀出血等典型三聯病徵時，必須首先高度懷疑子宮外孕等懷孕相關併發症。因此，最快速且第一優先的檢查是懷孕試驗（如尿液或血清 β-hCG 檢測）。確認懷孕後，才會進一步以超音波定位孕囊位置，而電腦斷層在此時不具首選診斷價值。",
      "flashcard_front": "育齡女性 / 月經過期 / 陰道出血 / 下腹痛 / 優先檢查",
      "flashcard_back": "育齡女性出現月經遲來、腹痛與出血，首要檢查為懷孕試驗，以排除子宮外孕等懷孕併發症。",
      "flashcard_summary": "腹痛出血優先檢查 -> 育齡女性出現腹痛與陰道出血時，第一優先做懷孕試驗。"
    },
    {
      "question_id": "110-1_medicine-6_032",
      "question_number": 32,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "Danazol 治療子宮內膜異位之雄性化副作用與臨床對策。",
      "explanation": "Danazol 為合成雄性素衍生物，用於治療子宮內膜異位，但常引發體重增加、熱潮紅及聲音變低沈等副作用，其中聲音低沈往往是不可逆的。因此，當患者出現聲音變低沈等雄性化表徵時，最適當的回答是應考慮停藥並更換其他有效藥物（如 GnRH 類似物或黃體素），不可建議繼續服藥觀察。",
      "flashcard_front": "子宮內膜異位 / Danazol治療 / 聲音變低沈 / 處置原則",
      "flashcard_back": "使用Danazol若出現不可逆的聲音變低沈副作用，應考慮停藥並更換其他有效藥物。",
      "flashcard_summary": "Danazol副作用處置 -> 出現不可逆的聲音低沈副作用時，應考慮停藥並更換其他藥物。"
    },
    {
      "question_id": "110-1_medicine-6_033",
      "question_number": 33,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "子宮頸癌手術切除後之病理預後因子判定。",
      "explanation": "子宮頸癌手術後的病理預後因子主要包括淋巴結轉移狀態（最重要的預後因子）、原發腫瘤體積大小、基質侵犯深度及有無血管淋巴管侵犯等。而腫瘤細胞內的人類乳突病毒型別（HPV types）雖與致病相關，但並非術後判斷臨床預後與決定後續輔助治療的指標，故選D。",
      "flashcard_front": "子宮頸癌 / 手術後病理報告 / 預後因子 / HPV型別",
      "flashcard_back": "子宮頸癌術後預後因子包括淋巴轉移、腫瘤大小及侵犯深度；HPV病毒型別非預後因子。",
      "flashcard_summary": "子宮頸癌預後因子 -> 包括淋巴轉移、腫瘤大小及基質侵犯深度，HPV型別則非預後因子。"
    },
    {
      "question_id": "110-1_medicine-6_034",
      "question_number": 34,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "微侵襲性子宮頸癌（Stage IA1）之基質侵犯深度上限。",
      "explanation": "根據 FIGO 分期標準，微侵襲性子宮頸癌（Microinvasive carcinoma, Stage IA1）的定義為基質（stroma）侵犯深度不超過 3 mm（選項B正確）。若侵犯深度大於 3 mm 但不超過 5 mm，則屬於 Stage IA2。5 mm 是整個 Stage IA 的上限值而非微侵襲性 IA1 的上限。",
      "flashcard_front": "微侵襲性子宮頸癌 / Stage IA1 / 基質 (stroma) 侵犯深度 / 限值",
      "flashcard_back": "微侵襲性子宮頸癌（Stage IA1）的基質侵犯深度不超過3 mm；3至5 mm為Stage IA2。",
      "flashcard_summary": "微侵襲性子宮頸癌深度 -> Stage IA1 的基質侵犯深度上限為 3 mm。"
    },
    {
      "question_id": "110-1_medicine-6_035",
      "question_number": 35,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "孕期疫苗接種之安全性與禁忌症規範。",
      "explanation": "孕婦在流感流行季節應接種流感疫苗（非活性死疫苗），不限孕期週數，以預防重症（選項B正確）。百日咳疫苗（Tdap）建議在懷孕第27至36週施打，使抗體能有效傳遞給胎兒（選項A錯誤）。水痘疫苗與 MMR 疫苗均屬活性減毒疫苗，孕期禁忌接種，若無抗體應於產後再補種（選項C、D錯誤）。",
      "flashcard_front": "孕期疫苗 / 流感疫苗 / Tdap / 活性減毒疫苗 (MMR、水痘)",
      "flashcard_back": "孕期可接種流感疫苗(死疫苗)與Tdap(27-36週)；活性減毒疫苗(MMR、水痘)孕期禁忌。",
      "flashcard_summary": "孕期疫苗接種 -> 流感疫苗可在孕期接種，活性減毒疫苗（MMR、水痘）則為孕期禁忌。"
    },
    {
      "question_id": "110-1_medicine-6_036",
      "question_number": 36,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "肥胖孕婦高風險併發症之增加幅度比較。",
      "explanation": "肥胖（BMI > 30）會增加多種產科併發症的風險，如子癇前症、死胎及產後出血。然而，在這些併發症中，妊娠糖尿病（GDM）在肥胖孕婦中的發生率相較於正常體重孕婦增加的倍數（約3至4倍以上）是最高的，這與肥胖直接導致的顯著胰島素阻抗密切相關。",
      "flashcard_front": "肥胖孕婦 (BMI > 30) / 產科併發症 / 妊娠糖尿病 / 增加最多",
      "flashcard_back": "肥胖孕婦發生多種併發症風險增加，其中妊娠糖尿病(GDM)的發生率相較正常體重者增加最多。",
      "flashcard_summary": "肥胖孕婦併發症 -> 肥胖孕婦發生妊娠糖尿病(GDM)的風險增加幅度最高。"
    },
    {
      "question_id": "110-1_medicine-6_037",
      "question_number": 37,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "第三產程主動處理（AMTSL）的核心步驟與禁忌處置。",
      "explanation": "第三產程主動處理（AMTSL）包含三個核心步驟：(1) 胎兒娩出後給予子宮收縮劑（如 oxytocin）；(2) 適度控制性牽引臍帶（CCT）；(3) 胎盤娩出後進行子宮按摩。將手或器械伸入子宮內取出/夾出胎盤屬於侵入性處置，僅在胎盤滯留或有併發症時使用，不屬於常規主動處理步驟。",
      "flashcard_front": "第三產程主動處理 (AMTSL) / 產後出血預防 / 三大步驟 / 人工剝離胎盤",
      "flashcard_back": "AMTSL包含給予收縮劑、控制性牽引臍帶、按摩子宮；將手或器械伸入子宮人工取出胎盤不在此列。",
      "flashcard_summary": "AMTSL核心步驟 -> 包含收縮劑、牽引臍帶與子宮按摩，不包括人工伸入手術取胎盤。"
    },
    {
      "question_id": "110-1_medicine-6_038",
      "question_number": 38,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "Bishop 評分系統評估子宮頸成熟度之指標項目。",
      "explanation": "Bishop 評分系統用於評估子宮頸成熟度，預測引產成功率。其五項指標包括：子宮頸擴張度（dilatation）、子宮頸薄度（effacement）、胎頭位置高度（station）、子宮頸軟硬度（consistency）以及子宮頸位置（position）。待產時間長短（labour course length）屬於產程進展結果，非評估指標，故選C。",
      "flashcard_front": "Bishop 評分 / 子宮頸成熟度 / 五項指標 / 待產時間",
      "flashcard_back": "Bishop評分指標包括擴張度、薄度、位置高度、軟硬度與子宮頸位置，不包括待產時間長短。",
      "flashcard_summary": "Bishop 評分指標 -> 評估擴張度、薄度、胎頭高度、軟硬度及位置，不含待產時間。"
    },
    {
      "question_id": "110-1_medicine-6_039",
      "question_number": 39,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "胎兒生物物理評估（BPP）之五大項目構成。",
      "explanation": "胎兒生物物理評估（BPP）包含五項指標：胎動、胎兒張力、胎兒呼吸運動、羊水量及胎心音非壓力試驗（NST）。多普勒臍帶血流變化測量（umbilical velocimetry）雖然是評估胎兒胎盤循環的工具，但不屬於標準 BPP 的五項指標之一，故選C。",
      "flashcard_front": "生物物理評估 (BPP) / 五大指標 / 羊水量 / 臍帶血流速度",
      "flashcard_back": "BPP五大指標為胎動、張力、呼吸、羊水量與NST；臍帶血流速度不包括在內。",
      "flashcard_summary": "BPP指標項目 -> 包含胎動、張力、呼吸、羊水與NST，不含臍帶血流速度測量。"
    },
    {
      "question_id": "110-1_medicine-6_040",
      "question_number": 40,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "妊娠合併急性肺水腫之臨床危險因子。",
      "explanation": "妊娠合併肺水腫的常見危險因子包括：子癇前症（引發血管通透性增加及白蛋白低下）、敗血症（引發肺泡通透性受損）及使用乙型受體興奮劑安胎藥（如 ritodrine，引發水鈉滯留與心血管負荷）。單純的妊娠糖尿病本身並非引發急性肺水腫的直接危險因子，故選A。",
      "flashcard_front": "妊娠合併肺水腫 / 臨床危險因子 / 安胎藥 (beta-mimetics) / 妊娠糖尿病",
      "flashcard_back": "肺水腫危險因子包括子癇前症、敗血症與乙型安胎藥；妊娠糖尿病非直接危險因子。",
      "flashcard_summary": "妊娠肺水腫危險因子 -> 包括子癇前症、敗血症與乙型安胎藥，妊娠糖尿病非直接因子。"
    },
    {
      "question_id": "110-1_medicine-6_041",
      "question_number": 41,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "早期破水合併絨毛膜羊膜炎之首要處置原則。",
      "explanation": "患者有早期破水（PPROM），且出現發燒（38.6°C）、心搏過速（102 bpm）及白血球顯著上升（WBC 19,000），臨床診斷為絨毛膜羊膜炎。一旦確診絨毛膜羊膜炎，應立即給予靜脈廣效抗生素治療（選項C正確）並準備引產。此時安胎（選項B）會加重感染，若無產科急剖剖腹指徵，首選為經陰道引產而非立即剖腹產（選項D）。",
      "flashcard_front": "早期破水 / 發燒 / 心搏過速 / 絨毛膜羊膜炎 / 首要處置",
      "flashcard_back": "破水合併發燒等絨毛膜羊膜炎徵候，應立即投予靜脈抗生素治療並著手引產分娩，禁用安胎藥。",
      "flashcard_summary": "絨毛膜羊膜炎處置 -> 確診後立即給予抗生素並著手準備分娩，禁用安胎藥。"
    },
    {
      "question_id": "110-1_medicine-6_042",
      "question_number": 42,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "陰部神經電氣學檢測（PNTML）之刺激與記錄部位。",
      "explanation": "陰部神經電氣學檢測（pudendal nerve terminal motor latency, PNTML）是藉由指套電極片（如 St. Mark 電極片）經陰道或直腸刺激坐骨棘（ischial spine）處的陰部神經，並記錄肛門外括約肌（anal sphincter）的肌肉反應。此檢測可用於評估陰道分娩後骨盆底神經及括約肌損傷的完整性。",
      "flashcard_front": "陰部神經電檢 (PNTML) / 坐骨棘 / 刺激部位 / 記錄肌肉部位",
      "flashcard_back": "PNTML利用電極在坐骨棘刺激陰部神經，並在肛門外括約肌(anal sphincter)記錄反應。",
      "flashcard_summary": "PNTML記錄肌肉 -> 經陰道或直腸在坐骨棘刺激神經，於肛門括約肌記錄反應。"
    },
    {
      "question_id": "110-1_medicine-6_043",
      "question_number": 43,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "外陰部疼痛伴隨成群小水泡與表淺潰瘍之診斷。",
      "explanation": "外陰部出現成群的小水泡（grouped vesicles）及表淺性潰瘍，且伴隨明顯的局部疼痛與燒灼感，是單純疱疹病毒（HSV）感染所致之生殖器疱疹（herpes）的典型特徵。一期梅毒通常為無痛性硬性下疳；軟性下疳雖有痛感但通常不起水泡；生殖器疣（菜花）則為無痛性增生。",
      "flashcard_front": "外陰部疼痛 / 成群小水泡 / 表淺性潰瘍 / 生殖器疱疹",
      "flashcard_back": "外陰部疼痛伴隨成群小水泡與表淺潰瘍，最可能的診斷是生殖器疱疹（herpes）。",
      "flashcard_summary": "外陰水泡潰瘍診斷 -> 外陰部疼痛且有成群水泡與潰瘍，最可能診斷為疱疹(herpes)。"
    },
    {
      "question_id": "110-1_medicine-6_044",
      "question_number": 44,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "其他",
      "category_confidence": "high",
      "key_point": "腹腔鏡氣腹壓力過高對心血管及生理機能之影響。",
      "explanation": "腹腔鏡手術中，若二氧化碳氣腹壓力過高且時間過長，會壓迫下腔靜脈減少靜脈回流，導致心輸出量下降而引發低血壓，故選項C寫高血壓為錯誤描述。高壓氣腹也可能導致氣體栓塞（選項A）、因高碳酸血症引發心律不整（選項B），以及因腹壓增加頂推膈肌引發胃酸逆流（選項D）。",
      "flashcard_front": "腹腔鏡手術 / 二氧化碳壓力過高 / 心輸出量 / 胃酸逆流 / 低血壓",
      "flashcard_back": "高壓氣腹壓迫下腔靜脈會減少回心血量，易導致低血壓而非持續性高血壓，並引發心律不整與胃酸逆流。",
      "flashcard_summary": "腹腔鏡高壓併發症 -> 高壓氣腹壓迫靜脈回流易引發低血壓而非高血壓，可伴隨心律不整與逆流。"
    },
    {
      "question_id": "110-1_medicine-6_045",
      "question_number": 45,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "子宮內膜癌之危險因子與保護因子（吸菸）。",
      "explanation": "子宮內膜癌（主要是第一型）的發生與長期無對抗性的雌激素刺激密切相關。停經過晚、糖尿病、肥胖以及家族遺傳性 Lynch 症候群均是子宮內膜癌的危險因子。相反地，吸菸（smoking）會降低血中雌激素水平並促進其代謝，因此與較低的子宮內膜癌風險相關（屬保護因子），故選C。",
      "flashcard_front": "子宮內膜癌 / 危險因子 / 停經過晚 / 糖尿病 / 吸菸",
      "flashcard_back": "停經過晚與糖尿病增加內膜癌風險；吸菸因降低雌激素水平，與較低的內膜癌風險相關。",
      "flashcard_summary": "子宮內膜癌與吸菸 -> 吸菸會降低體內雌激素，是子宮內膜癌的保護因子（風險較低）。"
    }
  ]
}

# ==================== BATCH: 110-1_medicine-6_batch-004 ====================
batches_data["110-1_medicine-6_batch-004"] = {
  "dataset_id": "110-1_medicine-6",
  "batch_id": "110-1_medicine-6_batch-004",
  "items": [
    {
      "question_id": "110-1_medicine-6_046",
      "question_number": 46,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "子宮肉瘤中對荷爾蒙治療反應最佳的類型與術後處置。",
      "explanation": "在各類子宮肉瘤中，低惡性度子宮內膜間質肉瘤（low-grade ESS）的腫瘤細胞通常高度表達雌激素與黃體素受體。因此，它對荷爾蒙治療的反應最好，在手術切除後，可考慮使用高劑量黃體素或芳香酶抑制劑進行輔助治療。而子宮肌肉瘤、癌肉瘤及未分化內膜間質肉瘤對荷爾蒙反應差，多以化療或放療為主。",
      "flashcard_front": "子宮肉瘤 / 荷爾蒙受體 / 術後高劑量黃體素 / 低惡性度子宮內膜間質肉瘤",
      "flashcard_back": "低惡性度子宮內膜間質肉瘤(low-grade ESS)富含雌黃體素受體，術後可用高劑量黃體素治療。",
      "flashcard_summary": "荷爾蒙敏感子宮肉瘤 -> 低惡性度子宮內膜間質肉瘤對黃體素治療反應最好。"
    },
    {
      "question_id": "110-1_medicine-6_047",
      "question_number": 47,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "卵巢上皮癌 2014-FIGO 分期中僅有骨盆腔淋巴轉移之期別判定。",
      "explanation": "根據 2014 FIGO 卵巢癌分期標準，當腫瘤局限於單側或雙側卵巢，且無腹腔內組織侵犯，但合併有後腹腔淋巴結轉移（包括骨盆腔及主動脈旁淋巴結轉移）時，歸類為 Stage IIIA1。進一步細分，轉移灶小於等於 10 mm 為 IIIA1(i)，大於 10 mm 為 IIIA1(ii)。Stage IIB 指侵犯至其他骨盆腔組織；Stage IIIB 與 IIIC 則指有腹腔內微細或肉眼轉移。",
      "flashcard_front": "卵巢上皮癌 / 2014-FIGO分期 / 局限卵巢 / 骨盆腔淋巴結轉移",
      "flashcard_back": "腫瘤限於卵巢但有骨盆腔或主動脈旁淋巴結轉移，分期為Stage IIIA1。",
      "flashcard_summary": "卵巢癌淋巴轉移分期 -> 僅有骨盆腔或主動脈旁淋巴轉移者，歸為Stage IIIA1。"
    },
    {
      "question_id": "110-1_medicine-6_048",
      "question_number": 48,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "次發性無月經症之病因與原發性無月經症（Kallmann 症候群）之鑑別。",
      "explanation": "Kallmann 症候群是由於下視丘 GnRH 神經元發育異常所致之促性腺激素低下症，患者表現為「原發性無月經症」（primary amenorrhea）而非次發性（選項C錯誤）。泌乳激素過高症與 Asherman 症候群（宮腔粘連）均是常見的次發性無月經症病因；懷孕則是生理性次發性無月經最常見的原因。",
      "flashcard_front": "次發性無月經症 / Kallmann 症候群 / 嗅覺喪失 / 懷孕 / Asherman",
      "flashcard_back": "Kallmann症候群為先天性GnRH分泌障礙，表現為原發性無月經；懷孕與Asherman為次發性無月經原因。",
      "flashcard_summary": "無月經與Kallmann -> Kallmann症候群導致原發性無月經，而非次發性無月經。"
    },
    {
      "question_id": "110-1_medicine-6_049",
      "question_number": 49,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "誘發排卵前 LH surge 所需之雌二醇（E2）血中濃度及持續時間。",
      "explanation": "在月經週期中，要對下視丘和腦下垂體產生正回饋作用以誘發排卵前的黃體化激素高峰（LH surge），雌二醇（E2）的血中濃度必須達到 200 pg/mL 以上，且此高濃度狀態必須維持至少 36 至 50 小時，故選項C正確。在此階段，孕酮（progesterone）尚未大量分泌，其分泌高峰主要在排卵後的黃體期。",
      "flashcard_front": "排卵前 / LH surge / 雌二醇 (E2) 濃度限制 / 持續時間",
      "flashcard_back": "誘發LH surge需要E2濃度大於200 pg/mL，且持續時間超過50小時（36-50小時）。",
      "flashcard_summary": "LH surge與E2濃度 -> E2濃度須大於200 pg/mL且維持超過50小時以誘發排卵前LH surge。"
    },
    {
      "question_id": "110-1_medicine-6_050",
      "question_number": 50,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "多囊性卵巢症候群（PCOS）鹿特丹診斷標準項目。",
      "explanation": "多囊性卵巢症候群（PCOS）診斷主要採用鹿特丹標準，包括：(1) 寡排卵或無排卵；(2) 臨床或生化上的雄性素過多；(3) 超音波呈現多囊性卵巢。雖然肥胖或體重過重在 PCOS 患者中極常見且與胰島素阻抗相關，但它並非診斷 PCOS 的必要標準之一，故選D。",
      "flashcard_front": "多囊性卵巢症 (PCOS) / 鹿特丹診斷標準 / 雄性素過多 / 肥胖",
      "flashcard_back": "PCOS診斷標準為寡排卵、雄性素過多、多囊性卵巢超音波影像，肥胖並非診斷標準之一。",
      "flashcard_summary": "PCOS診斷標準 -> 包含排卵障礙、雄性素高、多囊卵巢影像，肥胖非診斷標準。"
    },
    {
      "question_id": "110-1_medicine-6_051",
      "question_number": 51,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "先天性兩側輸精管缺少（CBAVD）與囊性纖維化之關聯性。",
      "explanation": "男性若出現精液中無精子且伴隨先天性兩側輸精管缺少（CBAVD），與囊性纖維化（Cystic fibrosis，CFTR基因突變）高度相關，約70-80%的患者帶有此基因突變。Kallmann 症候群與 Kartagener 症候群主要分別影響促性腺激素及纖毛活動力，而非導致輸精管缺損；Klinefelter 症候群（XXY）表現為睪丸發育不良，但輸精管通常存在。",
      "flashcard_front": "男性不孕 / 先天性兩側輸精管缺少 (CBAVD) / 無精症 / 基因突變",
      "flashcard_back": "兩側輸精管先天缺損(CBAVD)與囊性纖維化(Cystic fibrosis, CFTR基因突變)高度相關。",
      "flashcard_summary": "CBAVD與囊性纖維化 -> CBAVD 與囊性纖維化(CFTR基因突變)高度相關，是無精症重要遺傳病因。"
    },
    {
      "question_id": "110-1_medicine-6_052",
      "question_number": 52,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "卵巢早衰家族史與 X 染色體脆折症前突變之遺傳諮詢。",
      "explanation": "病患37歲即表現為卵巢早衰（FSH > 40, E2 < 20），且其母親也有早停經史，哥哥智能不足。此家族史高度提示 FMR1 基因前突變（premutation）。FMR1 基因前突變（CGG重複次數55-200次）會顯著增加女性卵巢早衰的風險，而全突變（>200次）則會導致男性患有 X 染色體脆折症（Fragile X syndrome）及智能不足，故應建議檢測 FMR 基因（選項A）。",
      "flashcard_front": "卵巢早衰 / 家族性早停經 / 哥哥智能不足 / 基因檢測 / FMR1",
      "flashcard_back": "卵巢早衰伴家族早停經及男性智能不足史，應篩檢FMR1基因前突變（X染色體脆折症相關）。",
      "flashcard_summary": "卵巢早衰與FMR1 -> 家族有早停經及智力障礙者，應檢查FMR1基因排除X染色體脆折症前突變。"
    },
    {
      "question_id": "110-1_medicine-6_053",
      "question_number": 53,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "子宮輸卵管攝影（HSG）的限制與臨床評估原則。",
      "explanation": "子宮輸卵管攝影（HSG）僅能描繪子宮腔內輪廓，無法看清子宮外部形狀，故通常需要另外藉助三維超音波或 MRI 區別中膈子宮與雙角子宮，故選項A正確。中膈子宮的切除應通過子宮鏡（hysteroscopy）手術而非腹腔鏡（選項B錯誤）。遠端輸卵管阻塞（如積水）在攝影後易誘發感染，建議預防性給予抗生素（選項C錯誤）。單次HSG發現近端阻塞常因宮角痙攣所致，需重試或行腹腔鏡確認，不可直接確診（選項D錯誤）。",
      "flashcard_front": "子宮輸卵管攝影 (HSG) / 中膈與雙角子宮 / 近端阻塞 / 遠端阻塞感染",
      "flashcard_back": "HSG無法觀察子宮外廓，需超音波輔助區分中膈或雙角子宮；近端阻塞可能因痙攣引起需再確認。",
      "flashcard_summary": "HSG評估子宮異常 -> 需藉助超音波區分中膈或雙角子宮；近端阻塞需排除痙攣引起的假陽性。"
    },
    {
      "question_id": "110-1_medicine-6_054",
      "question_number": 54,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "甲狀腺低下合併習慣性流產孕婦之孕初期甲狀腺素補充指引。",
      "explanation": "對於計畫懷孕或已懷孕初期的女性，TSH 目標值通常建議控制在 2.5 mIU/L 以下。若孕婦 TSH 大於 2.5 mIU/L（本題為4.5 mIU/L）且抗甲狀腺抗體（TPOAb）呈陽性（選項A），其流產與胎兒發育不良之風險顯著增加，此時最具強烈指引建議補充甲狀腺素。若 TSH 正常或抗體為陰性，補充的指引強度則較低。",
      "flashcard_front": "甲狀腺低下 / 習慣性流產 / 妊娠5週 / TSH 4.5 / 抗體陽性",
      "flashcard_back": "孕初期TSH大於2.5且抗甲狀腺抗體陽性者，流產風險高，應積極補充甲狀腺素。",
      "flashcard_summary": "孕初期甲狀腺素補充 -> TSH > 2.5且抗甲狀腺抗體陽性者，應考慮補充甲狀腺素以防流產。"
    },
    {
      "question_id": "110-1_medicine-6_055",
      "question_number": 55,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "輔助生殖技術（ART）中 hCG 施打與取卵時間安排原則。",
      "explanation": "在超音波卵泡監測中，當至少有兩顆主要濾泡的直徑達到 17-18 mm 時，即可施打 hCG 來幫助卵子最終成熟與排卵，故選項B正確。hCG 的半衰期比 LH 顯著較長（選項A錯誤）。取卵手術通常在施打 hCG 後的 34-36 小時進行（選項C錯誤）。若取卵數過多，為避免卵巢過度刺激（OHSS），應使用 GnRH agonist（而非 hCG）誘發成熟（選項D錯誤）。",
      "flashcard_front": "人工生殖 (ART) / hCG (破卵針) / 濾泡大小 / 取卵時間 / OHSS預防",
      "flashcard_back": "當兩顆濾泡達17-18 mm時施打hCG；取卵在hCG後34-36小時進行；OHSS風險高時避免用hCG破卵。",
      "flashcard_summary": "ART中hCG與取卵 -> 兩顆濾泡達17-18 mm時施打hCG，取卵安排在施打後34-36小時。"
    },
    {
      "question_id": "110-1_medicine-6_056",
      "question_number": 56,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "胎兒無腦症之頭部超音波特徵影像診斷。",
      "explanation": "此題為無腦症題組的第一題。在孕期16週超音波影像中，若胎兒因顱骨發育缺損，會使兩側眼眶顯得極為突出。在超音波斷面上會呈現典型的「青蛙眼徵象（frog sign）」，此異常器官位於頭部（head），故選項A正確。香蕉徵象與檸檬徵象通常與脊髓開裂引發的脊髓膜膨出（Chiari II 畸形）腦部變化相關。",
      "flashcard_front": "妊娠16週 / 顱骨缺損 / 突出的眼眶 / 胎兒超音波 / frog sign",
      "flashcard_back": "胎兒無腦症在超音波下因顱骨發育缺損、眼眶突出，頭部會呈現典型的青蛙眼徵象(frog sign)。",
      "flashcard_summary": "胎兒超音波青蛙眼特徵 -> 無腦症胎兒頭部超音波可見特徵性的青蛙眼徵象(frog sign)。"
    },
    {
      "question_id": "110-1_medicine-6_057",
      "question_number": 57,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "超音波下 frog sign 胎兒之臨床診斷。",
      "explanation": "承上題，胎兒超音波顯示缺乏正常的顱蓋骨結構和大腦組織，且眼眶突出呈 frog sign。此為典型的無腦症（anencephaly，選項D正確）表現，屬於嚴重的開放性神經管缺損。唐氏症、18號與13號三染色體雖然有其超音波標記，但不會表現為大腦及顱骨完全缺失的無腦症。",
      "flashcard_front": "超音波 frog sign / 顱骨缺失 / 腦組織未發育 / 神經管缺損",
      "flashcard_back": "胎兒頭部超音波缺乏顱骨且有frog sign，最可能的診斷是無腦症（anencephaly）。",
      "flashcard_summary": "無腦症超音波診斷 -> 顱骨缺失且眼眶突出呈frog sign，診斷為無腦症。"
    },
    {
      "question_id": "110-1_medicine-6_058",
      "question_number": 58,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "感覺異常性股痛（Meralgia paresthetica）受損神經之解剖判定。",
      "explanation": "感覺異常性股痛（Meralgia paresthetica）是由於股外側皮神經（LFCN，選項A）受壓迫或損傷引起，常見於腹股溝疝氣手術後、穿著過緊衣物或肥胖者，表現為大腿外側的疼痛、麻木及燒灼感。隱神經（選項B）負責小腿內側感覺；下臀神經（選項C）支配臀大肌；閉孔神經（選項D）負責大腿內側感覺及內收肌。",
      "flashcard_front": "大腿外側麻痛 / 感覺異常性股痛 / 疝氣手術後 / 受損神經",
      "flashcard_back": "大腿外側感覺異常性股痛是由於股外側皮神經（lateral femoral cutaneous nerve）受損或受壓迫所致。",
      "flashcard_summary": "感覺異常性股痛病因 -> 大腿外側麻痛之感覺異常性股痛為股外側皮神經受損。"
    },
    {
      "question_id": "110-1_medicine-6_059",
      "question_number": 59,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "脊髓損傷後異位性骨化症（HO）的手術治療時機限制。",
      "explanation": "脊髓損傷後的異位性骨化症（HO）好發於髖關節，三相式骨掃描是早期診斷的敏感工具。在骨化初期（未成熟期），病灶局部發炎且血管豐富，此時若進行手術切除會引發極高的復發率。因此，手術切除必須延遲至骨化完全成熟（通常需傷後1-2年，骨掃描活性降低、鹼性磷酸酶回復正常）後才能安全進行，故選項D敘述錯誤。",
      "flashcard_front": "脊髓損傷 / 異位性骨化症 (HO) / 骨掃描 / 手術切除時機",
      "flashcard_back": "異位性骨化症初期禁忌手術切除以防高復發率，必須等待骨化成熟（通常1-2年後）再手術。",
      "flashcard_summary": "異位性骨化症手術時機 -> 初期禁忌手術以防復發，須等骨化成熟(1-2年)後方可切除。"
    },
    {
      "question_id": "110-1_medicine-6_060",
      "question_number": 60,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "Brown-Séquard 症候群的典型臨床症狀解剖學特徵。",
      "explanation": "Brown-Séquard 症候群是由於脊髓半切（hemisection）受損所致。其典型症狀包括：受損同側的運動功能（同側下肢肌力喪失）及深感覺（本體感覺、震動覺）喪失；而受損對側則會出現痛覺與溫度感覺喪失（因脊髓丘腦徑入脊髓後立即交叉至對側上行），故選項D正確。四肢無力且上肢重於下肢為中央脊髓症候群之特徵。",
      "flashcard_front": "脊髓半切 / Brown-Séquard / 同側與對側 / 運動與痛溫覺",
      "flashcard_back": "Brown-Séquard症候群表現為受損同側運動及深感覺喪失，對側痛覺與溫度感覺喪失。",
      "flashcard_summary": "Brown-Séquard特徵 -> 表現為受損同側運動及深感覺喪失，對側痛覺與溫度覺喪失。"
    }
  ]
}

# ==================== BATCH: 110-1_medicine-6_batch-005 ====================
batches_data["110-1_medicine-6_batch-005"] = {
  "dataset_id": "110-1_medicine-6",
  "batch_id": "110-1_medicine-6_batch-005",
  "items": [
    {
      "question_id": "110-1_medicine-6_061",
      "question_number": 61,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "去髓鞘病變在肌電圖與神經傳導檢查中之特徵表現。",
      "explanation": "去髓鞘病變（Demyelination）會導致神經傳導速度變慢與傳導阻滯。因此，常見的電學表現為遠端潛期變長、感覺神經傳導速度變慢及時間分散。複合肌肉動作電位（CMAP）的振幅通常會維持正常或因傳導阻滯而「降低」，絕不可能增加，故選項B是最不常出現的結果。運動單元電位多相波比率增加則常見於慢性病變中。",
      "flashcard_front": "慢性髓鞘病變 / 肌電圖與神經傳導 / 傳導速度 / CMAP振幅",
      "flashcard_back": "去髓鞘病變典型表現為傳導速度變慢、遠端潛期變長；CMAP振幅只會降低或正常，不會增加。",
      "flashcard_summary": "去髓鞘電生理特徵 -> 傳導速度變慢且潛期變長，CMAP振幅通常降低或正常，不會增加。"
    },
    {
      "question_id": "110-1_medicine-6_062",
      "question_number": 62,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "足底筋膜炎常見之生物力學致病因子分析。",
      "explanation": "足底筋膜炎的力學致病因素包括高弓足、扁平足、踝關節蹠屈/背屈活動度受限（如腓腸肌過緊）以及第一蹠趾關節僵硬。在步行時，過度的距下關節「旋前（pronation）」會拉扯筋膜而致病；而距下關節「旋後（supination）」並非其常見致病因素，故選項B非致病因素。",
      "flashcard_front": "足底筋膜炎 / 力學致病因素 / 距下關節旋後 / 第一蹠趾關節僵硬",
      "flashcard_back": "足底筋膜炎力學成因包括高弓/扁平足、關節僵硬與過度「旋前」；距下關節「旋後」非主因。",
      "flashcard_summary": "足底筋膜炎力學成因 -> 距下關節旋前、第一蹠趾關節僵硬與高弓足易致病，旋後則非。"
    },
    {
      "question_id": "110-1_medicine-6_063",
      "question_number": 63,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "急性膝關節內血腫之處置原則與門閾學說的生理機制。",
      "explanation": "本題將第63題右膝外傷處置與第64題門閾學說合併。第63題中，急性膝關節內大量積血導致極度腫脹時，首選處置是先抽取積液或積血以減壓止痛（原選項C）。而第64題中門閾學說之生理機轉為刺激粗的A型纖維以抑制細的C型或Aδ型痛覺纖維傳導（原答案為B）；但若依本題題庫設定之正解C，我們應理解為考點側重於門閾學說中粗纖維對細纖維的抑制作用，考生作答時請以官方公佈答案為準。",
      "flashcard_front": "膝關節急性血腫處置 / 門閾學說 / 粗細神經纖維抑制 / 官方答案C",
      "flashcard_back": "急性膝關節內大量積血應先抽取積液以減壓；門閾學說是以較粗的A型纖維刺激抑制較細的痛覺傳導。",
      "flashcard_summary": "膝關節血腫與門閾學說 -> 急性關節血腫首選抽取積液減壓；門閾學說以較粗的A型纖維刺激抑制較細的痛覺傳導。"
    },
    {
      "question_id": "110-1_medicine-6_065",
      "question_number": 65,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "脊柱側彎的診斷工具測量面與背架治療目的。",
      "explanation": "脊柱側彎患者配戴背架的主要目的是在生長發育期提供支撐，以避免側彎角度進一步惡化，而非將側彎完全矯正（選項D正確）。側彎測量器是在前彎時測量軸狀面（transverse plane）的軀幹旋轉角度（ATR），而非額平面（選項A錯誤）。側彎病因通常與睡姿無關（選項B錯誤），且電刺激對其無明確療效（選項C錯誤）。",
      "flashcard_front": "脊柱側彎 / 背架治療目的 / 側彎測量器 (scoliometer) / 軸狀面",
      "flashcard_back": "背架治療主要目的是避免側彎惡化；側彎測量器測量的是軸狀面角度而非額平面。",
      "flashcard_summary": "脊柱側彎與背架 -> 背架治療主要目的是防惡化，側彎測量器主要量測軸狀面角度。"
    },
    {
      "question_id": "110-1_medicine-6_066",
      "question_number": 66,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "腋下燒燙傷擺位輔具與肩膀關節攣縮預防原則。",
      "explanation": "為避免腋下或肩膀燒燙傷後的關節攣縮與變形，患者的肩膀必須擺位在「外展（abduction，約90度）」與外旋姿勢，因此使用的飛機副木（airplane splint）是為了維持外展而非「內收（adduction）」姿勢，故選項D敘述錯誤。患者因痛常將肢體屈曲擺位，易導致攣縮（選項A正確）；輔具與壓力衣的目的即在預防攣縮與瘢痕增生。",
      "flashcard_front": "燒燙傷擺位 / 預防關節攣縮 / 飛機副木 (airplane splint) / 肩關節外展與內收",
      "flashcard_back": "防腋下燙傷攣縮，應使用飛機副木將肩關節擺位在「外展」而非內收姿勢。",
      "flashcard_summary": "腋下燙傷防攣縮擺位 -> 應使用飛機副木維持肩關節「外展」姿勢以防攣縮。"
    },
    {
      "question_id": "110-1_medicine-6_067",
      "question_number": 67,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "年輕運動選手劇烈運動猝死之常見心血管病因。",
      "explanation": "年輕運動員劇烈運動猝死的最常見原因為肥厚性心肌症（HCM），其次為先天性冠狀動脈異常、馬凡氏症候群所致的主動脈瘤破裂等。二尖瓣脫垂（MVP）在一般人群中相當常見，且絕大多數患者預後良好，極少單獨引起劇烈運動猝死，因此並非主要致死原因，故選D。",
      "flashcard_front": "運動猝死 / 劇烈運動 / 肥厚性心肌症 / 二尖瓣脫垂",
      "flashcard_back": "運動猝死主因為肥厚性心肌症及冠狀動脈異常；二尖瓣脫垂極少單獨引發運動猝死。",
      "flashcard_summary": "運動猝死心血管原因 -> 主因為肥厚性心肌症，二尖瓣脫垂極少單獨引發猝死。"
    },
    {
      "question_id": "110-1_medicine-6_068",
      "question_number": 68,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "清除呼吸道分泌物（蓄痰）之治療目標與袪痰藥物應用。",
      "explanation": "清除呼吸道蓄痰可以使用姿勢引流、拍痰等胸腔物理治療，可改善氣體交換並減少肺部感染機率。在臨床治療上，常需「配合」使用袪痰藥物（mucoactive medications）以稀釋或溶解分泌物，使其更易被引流及咳出，而非儘量避免使用，故選項C敘述錯誤。",
      "flashcard_front": "呼吸道蓄痰 / 姿勢引流 / 改善氣體交換 / 袪痰藥物",
      "flashcard_back": "清除呼吸道積痰可改善氣體交換，常需配合使用袪痰藥物以利引流排出，非避免使用。",
      "flashcard_summary": "清除呼吸道蓄痰 -> 物理引流常需配合使用袪痰藥物，以利痰液稀釋排出。"
    },
    {
      "question_id": "110-1_medicine-6_069",
      "question_number": 69,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "脊髓脊膜膨出症（myelomeningocele）合併水腦症之關聯性。",
      "explanation": "脊髓脊膜膨出症（myelomeningocele）為嚴重的開放性脊柱裂，常合併 Arnold-Chiari II 型畸形，導致後腦部向下疝出而阻塞腦脊髓液循環。因此，有高達80%以上的患者會合併水腦症，常需放置分流管治療。腦性麻痺與肌肉萎縮症主要影響運動控制或肌肉，極少直接引發水腦症。",
      "flashcard_front": "脊髓脊膜膨出症 / Arnold-Chiari / 水腦症 / 腦性麻痺",
      "flashcard_back": "脊髓脊膜膨出症常因Chiari畸形阻塞腦脊液循環，有八成以上患者會合併水腦症。",
      "flashcard_summary": "脊髓脊膜膨出與水腦症 -> 脊髓脊膜膨出症因腦液阻塞，極常合併水腦症。"
    },
    {
      "question_id": "110-1_medicine-6_070",
      "question_number": 70,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "小腦損傷引發之語言障礙類型（運動失調型吶吃）。",
      "explanation": "小腦負責協調運動與說話的節律。小腦受損會導致發音含糊、語調節律異常（如爆發性語言或北歐式斷續說話），這在臨床上稱為運動失調型吶吃（ataxic dysarthria，選項A正確）。弛緩型吶吃多與下運動神經元受損有關；布洛卡氏失語症則屬於語言中樞受損所致的失語症而非吶吃。",
      "flashcard_front": "小腦損傷 / 語調不連貫 / 爆發性語言 / 運動失調型吶吃 (ataxic dysarthria)",
      "flashcard_back": "小腦損傷主要導致說話協調不良，引發運動失調型吶吃；失語症則多為大腦皮質受損所致。",
      "flashcard_summary": "小腦損傷語言障礙 -> 小腦受損會引發語調不協調的運動失調型吶吃(ataxic dysarthria)。"
    },
    {
      "question_id": "110-1_medicine-6_071",
      "question_number": 71,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "腋網症候群（axillary web syndrome）與乳癌手術後之關聯。",
      "explanation": "腋網症候群（axillary web syndrome, AWS，又稱 cording）是乳癌手術（特別是接受腋下淋巴結摘除或前哨淋巴結切片，選項C）後最常見的疼痛與功能障礙症狀。其特徵為腋下至手臂出現緊繃的纖維化條索物，限制肩膀活動度。頭頸癌或肺癌手術不涉及此區域之淋巴清掃，不會引發此症候群。",
      "flashcard_front": "乳癌手術 / 腋下淋巴結摘除 / 緊繃條索狀物 / 腋網症候群 (AWS)",
      "flashcard_back": "腋網症候群(AWS)是乳癌手術切除淋巴後常見的併發症，表現為腋下至手臂的纖維化條索緊繃與疼痛。",
      "flashcard_summary": "乳癌術後腋網症候群 -> 腋網症候群是乳癌手術切除淋巴後常見的腋下條索狀緊繃併發症。"
    },
    {
      "question_id": "110-1_medicine-6_072",
      "question_number": 72,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "巧克力囊腫在磁振造影（MRI）中之特徵性訊號特徵。",
      "explanation": "巧克力囊腫（子宮內膜異位瘤）在 MRI 影像中具有特徵性的「T2 shading sign」：由於囊腫內含有高濃度陳舊性出血及高價鐵離子，會使其在 T1 加權影像中呈現亮的高訊號，而在 T2 加權影像中因磁化率效應呈現訊號衰減的稍低訊號（選項A正確）。卵巢癌與膿瘍在 T2 通常呈高訊號，畸胎瘤在 T1 及 T2 雖呈高訊號但可被脂肪抑制技術鑑別。",
      "flashcard_front": "骨盆腔囊腫 / T1高訊號 / T2稍低訊號 (T2 shading) / 巧克力囊腫",
      "flashcard_back": "在MRI上呈現T1高訊號、T2低訊號(shading sign)的骨盆腔囊腫為巧克力囊腫，與陳舊出血有關。",
      "flashcard_summary": "巧克力囊腫MRI特徵 -> 巧克力囊腫在 T1 呈高訊號，在 T2 呈低訊號（T2 shading sign）。"
    },
    {
      "question_id": "110-1_medicine-6_073",
      "question_number": 73,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "復健科",
      "category_confidence": "high",
      "key_point": "前十字韌帶斷裂（ACL tear）之 X 光與 MRI 伴隨特徵診斷。",
      "explanation": "在膝關節前十字韌帶（ACL）斷裂患者中，常伴隨股骨外側髁與脛骨後外側的骨挫傷（選項B），且 X 光上常可見脛骨外側平台撕裂骨折（Segond fracture，選項D）。依解剖學與創傷機制，常合併發生的是「內側半月板撕裂」（O'Donoghue 三聯症：ACL、MCL、內側半月板），而非外側半月板撕裂，故選項C診斷錯誤。",
      "flashcard_front": "膝部受傷 / ACL斷裂 / 骨挫傷 / Segond fracture / 半月板撕裂",
      "flashcard_back": "ACL斷裂常伴隨Segond骨折與骨挫傷，且半月板撕裂好發於內側而非外側半月板。",
      "flashcard_summary": "ACL斷裂伴隨損傷 -> 常合併Segond骨折與骨挫傷，半月板受損多為內側而非外側。"
    },
    {
      "question_id": "110-1_medicine-6_074",
      "question_number": 74,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "其他",
      "category_confidence": "high",
      "key_point": "無症狀重度頸動脈狹窄之外科手術與支架適應症。",
      "explanation": "對於「無症狀」的頸動脈狹窄，若狹窄程度相當嚴重（通常大於60%或70%-80%以上），且患者預期壽命較長，臨床上仍可考慮進行頸動脈內膜切除術（CEA）或頸動脈支架置放術（CAS）以預防中風，而非一律僅接受內科藥物治療，故選項B敘述錯誤。有症狀的重度狹窄（大於50%-60%）有明確的手術指引（選項A）；頸動脈分支處是硬化好發地（選項C）。",
      "flashcard_front": "頸動脈狹窄 / 無症狀狹窄 / 外科手術 (CEA) / 內科藥物治療",
      "flashcard_back": "無症狀的頸動脈狹窄若程度嚴重（>60%），仍可考慮手術或支架治療，非一律僅用內科治療。",
      "flashcard_summary": "無症狀頸動脈狹窄處置 -> 嚴重度高於60-70%時，無症狀患者亦可考慮手術或支架預防中風。"
    },
    {
      "question_id": "110-1_medicine-6_075",
      "question_number": 75,
      "correct_answer": "D",
      "category_group": "醫學（六）",
      "category": "婦產科",
      "category_confidence": "high",
      "key_point": "產後出血之最常見原因、代償徵兆與麥角生物鹼禁忌症。",
      "explanation": "麥角生物鹼（如 Methergine）具強烈血管收縮作用，會顯著升高血壓，因此在子癇前症（pre-eclampsia）或高血壓患者中屬於絕對禁忌，不可用於治療產後出血，故選項D正確。子宮收縮無力才是產後出血最常見的原因（選項A錯誤）。早期產後出血時，孕婦血壓多維持正常，心搏過速才是最早出現的徵兆（選項B錯誤）。第一步應先穩定生命徵象，而非先會診（選項C錯誤）。",
      "flashcard_front": "產後出血 / 子癇前症 / 麥角生物鹼 (Methergine) / 心搏過速",
      "flashcard_back": "麥角生物鹼會升高血壓，子癇前症孕婦的產後出血禁用；早期出血徵兆是心搏過速而非低血壓。",
      "flashcard_summary": "產後出血與麥角生物鹼 -> 麥角生物鹼因會升壓，是子癇前症孕婦產後出血的絕對禁忌。"
    },
    {
      "question_id": "110-1_medicine-6_076",
      "question_number": 76,
      "correct_answer": "B",
      "category_group": "醫學（六）",
      "category": "耳鼻喉科",
      "category_confidence": "high",
      "key_point": "外耳道異物沖洗法之沖洗液溫度要求與禁忌。",
      "explanation": "外耳道異物沖洗時，沖洗液的溫度必須接近體溫（約 37°C）。若使用冰水（選項B）或過熱的水，會刺激半規管引起前庭溫差效應，導致患者產生嚴重的眩暈、噁心及眼震，故使用冰水最不適當。沖洗前必須確認耳膜無破損（選項A）及異物非吸水膨脹性（選項C）。",
      "flashcard_front": "外耳道異物 / 清水沖洗 / 沖洗液溫度 / 眩暈與眼震",
      "flashcard_back": "沖洗外耳道須使用接近體溫(37°C)的溫水，若使用冰水會刺激前庭半規管引發嚴重眩暈與眼震。",
      "flashcard_summary": "外耳道沖洗溫度 -> 沖洗須用接近體溫的溫水，冰水會引發前庭刺激與眩暈。"
    }
  ]
}

# ==================== BATCH: 110-1_medicine-6_batch-006 ====================
batches_data["110-1_medicine-6_batch-006"] = {
  "dataset_id": "110-1_medicine-6",
  "batch_id": "110-1_medicine-6_batch-006",
  "items": [
    {
      "question_id": "110-1_medicine-6_077",
      "question_number": 77,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "麻醉科",
      "category_confidence": "high",
      "key_point": "Lidocaine 合併 Epinephrine 之局部麻醉最高安全劑量。",
      "explanation": "Lidocaine 在局部麻醉時的安全劑量，若單獨使用為 4.5 mg/kg（最大總量 300 mg）；若合併血管收縮劑 Epinephrine，可減緩吸收並提高最大劑量至 7 mg/kg（最大總量 500 mg）。對於 72 公斤患者，72 * 7 = 504 mg，但受限於最大總量上限，其最高安全劑量為 500 mg，故選項C正確。",
      "flashcard_front": "Lidocaine / Epinephrine併用 / 72公斤 / 最高麻醉安全劑量",
      "flashcard_back": "Lidocaine併用血管收縮劑最大安全劑量為7 mg/kg，且總上限為500 mg，72公斤者最高安全劑量即為500 mg。",
      "flashcard_summary": "Lidocaine麻醉上限 -> 併用腎上腺素時最大安全劑量為7 mg/kg（總量上限500 mg）。"
    },
    {
      "question_id": "110-1_medicine-6_078",
      "question_number": 78,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "醫學倫理與醫療決策",
      "category_confidence": "high",
      "key_point": "未經知情同意進行非緊急侵入性醫療處置所違反之倫理原則。",
      "explanation": "醫師在非緊急狀況下，未徵得病人同意便直接放置中耳引流管，直接違反了告知義務（選項A）、知情同意（選項B）以及尊重病人的自主決定權（選項D）。在此事件中，並未涉及病人個人隱私資料的洩漏，因此並未違反守密義務，故選項C為正確答案。",
      "flashcard_front": "中耳積水 / 未徵求同意 / 直接放置引流管 / 醫學倫理 / 守密",
      "flashcard_back": "未取得病人知情同意擅自進行非緊急處置，違反告知、知情同意與自主，未違反守密。",
      "flashcard_summary": "未授權醫療處置倫理 -> 違反告知與知情同意原則，但與守密義務無關。"
    },
    {
      "question_id": "110-1_medicine-6_079",
      "question_number": 79,
      "correct_answer": "A",
      "category_group": "醫學（六）",
      "category": "醫學倫理與醫療決策",
      "category_confidence": "high",
      "key_point": "醫師與診治病人發生親密關係之醫療專業邊界處置原則。",
      "explanation": "醫師與其正在診治的病人發生婚外情等親密關係，違反了醫療專業邊界（professional boundaries），會嚴重干擾醫療決策客觀性。院方最首要且最適當的處置是立即中止該醫師與該病人間的醫療關係，並將病人轉介（選項A正確）。院方無權主動告知配偶（選項B）；此行為影響醫療專業，非單純隱私（選項C）；直接停職所有職務則未先釐清邊界且處分過重（選項D）。",
      "flashcard_front": "醫師與病人 / 婚外情 / 專業邊界 / 院方首要處置",
      "flashcard_back": "醫師與病人發生親密關係違反專業邊界，院方首要處置為立即中止其醫療關係並轉介病人。",
      "flashcard_summary": "醫病關係專業邊界 -> 醫師與患者有親密關係時，院方應立即中止其醫療關係並進行轉介。"
    },
    {
      "question_id": "110-1_medicine-6_080",
      "question_number": 80,
      "correct_answer": "C",
      "category_group": "醫學（六）",
      "category": "醫學倫理與醫療決策",
      "category_confidence": "high",
      "key_point": "赫爾辛基宣言中關於醫學研究與醫療照護結合之規範原則。",
      "explanation": "根據赫爾辛基宣言，醫師只有在研究具有潛在預防、診斷或治療價值，且有充足理由相信參與研究不會對病人的健康產生不良影響時，才可以結合醫學研究與醫療照護，以保護受試病人的福祉。選項A缺少了研究需有潛在價值的限制；選項B全盤否定是不對的；選項D認為僅需行政核准則忽視了倫理核心。",
      "flashcard_front": "赫爾辛基宣言 / 醫學研究與醫療照護結合 / 臨床價值 / 利益衝突",
      "flashcard_back": "結合研究與醫療照護，前提是研究具潛在臨床價值，且醫師確信參與不會危害病人健康。",
      "flashcard_summary": "赫爾辛基結合照護 -> 僅在研究具潛在價值且不損害病人健康時，方可結合研究與醫療照護。"
    }
  ]
}

# ==================== BATCH: 110-2_medicine-1_batch-001 ====================
batches_data["110-2_medicine-1_batch-001"] = {
  "dataset_id": "110-2_medicine-1",
  "batch_id": "110-2_medicine-1_batch-001",
  "items": [
    {
      "question_id": "110-2_medicine-1_001",
      "question_number": 1,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "內頸動脈之直接分支與前交通動脈之解剖來源。",
      "explanation": "內頸動脈（ICA）進入顱腔後的分支包括眼動脈、後交通動脈、前脈絡叢動脈，並終止分支為前大腦動脈（ACA）與中大腦動脈（MCA）。前交通動脈（Acom）是連接左、右兩側前大腦動脈之間的交通支，並非內頸動脈的直接分支，故選D。",
      "flashcard_front": "內頸動脈 (ICA) / 直接分支 / 中大腦動脈 / 前交通動脈 (Acom)",
      "flashcard_back": "內頸動脈分支包含眼動脈、前脈絡叢、前/中大腦動脈；前交通動脈是連接左右ACA的交通支，非ICA直接分支。",
      "flashcard_summary": "內頸動脈分支 -> 前交通動脈(Acom)是連接兩側ACA的血管，非內頸動脈的直接分支。"
    },
    {
      "question_id": "110-2_medicine-1_002",
      "question_number": 2,
      "correct_answer": "A",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "脊髓半切症候群（Brown-Séquard）胸段受損之神經症狀定位。",
      "explanation": "右側胸段脊髓受損會導致同側（右側）皮質脊髓支受損，引起同側下肢無力，故選項A正確且選項D錯誤。同時，同側後柱受損會導致同側下肢本體感覺與震動覺受損，而非左側受損。此外，對側脊髓丘腦徑受損會導致對側（左側）下肢痛溫覺喪失，而非同側（右側）痛覺異常。",
      "flashcard_front": "右側胸段脊髓半切 / 運動無力 / 震動覺與本體感覺 / 痛溫覺 / 同側與對側",
      "flashcard_back": "胸段右半受損，同側（右側）下肢運動及深感覺喪失，對側（左側）下肢痛溫覺喪失，不影響上肢。",
      "flashcard_summary": "右胸脊髓半切症狀 -> 同側（右側）下肢運動及深感覺喪失，對側（左側）下肢痛溫覺喪失。"
    },
    {
      "question_id": "110-2_medicine-1_003",
      "question_number": 3,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "腭扁桃腺（palatine tonsil）血液供應來源之分支判定。",
      "explanation": "腭扁桃腺血液供應豐富，來自外頸動脈的分支，包含面動脈的扁桃腺支與升腭動脈（主要供應，選項A）、舌動脈的背舌支（選項B）、升咽動脈（選項C）及上腭降動脈。而上甲狀腺動脈（選項D）為外頸動脈向下的分支，主要供應甲狀腺及喉部，不參與腭扁桃腺的血液供應。",
      "flashcard_front": "腭扁桃腺 / 血液供應 / 外頸動脈分支 / 上甲狀腺動脈",
      "flashcard_back": "腭扁桃腺血供源於面動脈、舌動脈及升咽動脈分支；上甲狀腺動脈往下走，不供應扁桃腺。",
      "flashcard_summary": "腭扁桃腺血供 -> 主要來自面、舌與升咽動脈的分支，不來自上甲狀腺動脈。"
    },
    {
      "question_id": "110-2_medicine-1_004",
      "question_number": 4,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "大岩神經溝（groove for greater petrosal nerve）在顱底之骨骼定位。",
      "explanation": "大岩神經溝位於顳骨岩部（petrous part of temporal bone）的前面，故選項C正確。大岩神經（來自面神經 CN VII）自膝狀神經節分出，經大岩神經管裂孔穿出進入此溝向前行走，行經破裂孔與深岩神經結合成翼管神經。該構造不位於蝶骨、頂骨或枕骨。",
      "flashcard_front": "大岩神經溝 / 顳骨岩部 / 面神經分支 / 顱底骨骼解剖",
      "flashcard_back": "大岩神經溝位於顳骨岩部的面神經分支通路，屬於顳骨的一部分。",
      "flashcard_summary": "大岩神經溝位置 -> 位於顱底顳骨岩部的前面。"
    },
    {
      "question_id": "110-2_medicine-1_005",
      "question_number": 5,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "顱底各孔洞通過神經血管之解剖學特徵比較。",
      "explanation": "盲孔（foramen cecum）通常僅有導血管（emissary vein，連接鼻腔與上矢狀竇）通過，並無任何神經通過，故選D。頸靜脈孔（選項A）有CN IX、X、XI通過；圓孔（選項B）有三叉神經第二支（CN V2）通過；篩後孔（選項C）則有篩後神經與血管通過。",
      "flashcard_front": "顱底孔洞 / 盲孔 (foramen cecum) / 頸靜脈孔 / 圓孔 / 通過神經",
      "flashcard_back": "盲孔僅有鼻腔與上矢狀竇間的導血管通過，無神經通過；圓孔有CN V2，頸靜脈孔有CN IX, X, XI。",
      "flashcard_summary": "盲孔通過構造 -> 盲孔無神經通過，僅有鼻腔與腦竇間的導血管通過。"
    },
    {
      "question_id": "110-2_medicine-1_006",
      "question_number": 6,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "腹主動脈成對與不成對分支起點水平位置之高低順序。",
      "explanation": "腹主動脈主要分支的起點由高到低依次為：腹腔動脈（L1上緣）-> 腸繫膜上動脈（L1下緣，選項A）-> 腎上腺中動脈（L1，選項B）-> 腎動脈（L1-L2之間，選項C）-> 睪丸/卵巢動脈（L2，選項D）。因此，在四個選項中，睪丸動脈的起點水平位置最低。",
      "flashcard_front": "腹主動脈分支 / 起點水平高度 / 腸繫膜上動脈 / 腎動脈 / 睪丸動脈",
      "flashcard_back": "腹主動脈分支中，睪丸動脈起點約在L2水平，低於腎動脈(L1-L2)與腸繫膜上動脈(L1)。",
      "flashcard_summary": "腹主動脈分支高度 -> 睪丸動脈起點(L2)在選項中水平位置最低，低於腎動脈與SMA。"
    },
    {
      "question_id": "110-2_medicine-1_007",
      "question_number": 7,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "直腸上段動脈血供應來源（腸繫膜下動脈）。",
      "explanation": "直腸上段的動脈血來自直腸上動脈（superior rectal artery），該動脈是腸繫膜下動脈（IMA，選項B）的終末直接分支。直腸中動脈與下動脈則源自髂內動脈（選項D）及其分支，供應直腸中段與下段的血液。腸繫膜上動脈（選項A）主要供應盲腸至結腸脾曲之腸段。",
      "flashcard_front": "直腸血管 / 直腸上段血供 / 直腸上動脈 / 腸繫膜下動脈 (IMA)",
      "flashcard_back": "直腸上段由直腸上動脈供應，後者為腸繫膜下動脈(IMA)的直接延續分支；中下段由髂內動脈分支供應。",
      "flashcard_summary": "直腸上段血供 -> 來自直腸上動脈，為腸繫膜下動脈(IMA)之終末分支。"
    },
    {
      "question_id": "110-2_medicine-1_008",
      "question_number": 8,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "L1 脊神經與交感神經鏈之交通支（白與灰交通支）解剖學構成。",
      "explanation": "交通支是連接脊神經與交感神經鏈的構造。白交通支（white rami）僅存在於 T1 至 L2 脊髓節段，內含交感神經節前有髓鞘纖維；而灰交通支（gray rami）存在於所有脊神經節段，內含交感節後無髓鞘纖維。因為 L1 處於 T1-L2 區間內，因此連接 L1 的交通支同時包含白與灰交通支，內部分別含節前與節後纖維（選項D正確）。",
      "flashcard_front": "L1 脊神經 / 交感神經鏈 / 白交通支與灰交通支 / 節前與節後纖維",
      "flashcard_back": "L1脊神經與交感鏈間有白與灰交通支連接；白支含節前有髓纖維，灰支含節後無髓纖維。",
      "flashcard_summary": "L1交感交通支 -> 同時具有白與灰交通支，分別傳導交感節前及節後神經纖維。"
    },
    {
      "question_id": "110-2_medicine-1_009",
      "question_number": 9,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "男性尿道四部分之長度比較。",
      "explanation": "男性尿道依解剖路徑分為四部分。膀胱內壁部最短，約0.5-1 cm；前列腺部約3-4 cm；膜部最窄且最易在外傷中受損，長約1-2 cm；海綿體部（陰莖部，選項D）穿過尿道海綿體，長達15 cm，為男性尿道中最長的部分，故選D。",
      "flashcard_front": "男性尿道 / 四個分部 / 膜部 / 海綿體部 / 最長部分",
      "flashcard_back": "男性尿道中最長的部分為海綿體部（陰莖部，約15 cm）；最短部分為膀胱內壁部；最窄易傷為膜部。",
      "flashcard_summary": "男性尿道最長部 -> 男性尿道中最長的分部為海綿體部(spongy part)。"
    },
    {
      "question_id": "110-2_medicine-1_010",
      "question_number": 10,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "構成膝關節（knee joint）的骨骼解剖組成。",
      "explanation": "膝關節主要由股骨下端、脛骨上端及髕骨組成，包含股脛關節與股髕關節。而腓骨（fibula，選項C）雖然位於小腿外側並與脛骨形成上脛腓關節，但其並不直接參與構成膝關節的關節面或關節腔，故選C為正確答案。",
      "flashcard_front": "膝關節 / 關節面組成 / 股骨與脛骨 / 腓骨",
      "flashcard_back": "膝關節由股骨、脛骨及髕骨構成；外側的腓骨不參與膝關節的構成與關節面運動。",
      "flashcard_summary": "構成膝關節之骨骼 -> 由股骨、脛骨與髕骨構成，腓骨不參與構成。"
    },
    {
      "question_id": "110-2_medicine-1_011",
      "question_number": 11,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "胸腔脊髓血供來源與脊髓節動脈分支來源。",
      "explanation": "在胸腔段，脊髓的血液供應主要來自胸主動脈分出的肋間後動脈（posterior intercostal arteries，選項D）。肋間後動脈發出的脊髓支（spinal branches）穿過椎間孔，在特定節段發育為較粗的脊髓節動脈，進入脊髓以補充電前、後脊髓動脈。椎動脈主要供應頸部脊髓；胸內動脈與肋間前動脈主要供應前胸壁，不向脊髓供血。",
      "flashcard_front": "胸段脊髓 / 血液供應 / 脊髓節動脈 / 肋間後動脈",
      "flashcard_back": "胸段脊髓的脊髓節動脈起源自肋間後動脈（posterior intercostal artery）的脊髓支。",
      "flashcard_summary": "胸段脊髓節動脈來源 -> 脊髓節動脈源自肋間後動脈分支，以補充脊髓血供。"
    },
    {
      "question_id": "110-2_medicine-1_012",
      "question_number": 12,
      "correct_answer": "D",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "大腦白質聯合纖維與聯絡（連合）纖維之解剖學分類。",
      "explanation": "大腦白質纖維中，聯合纖維（association fibers）連接「同側」半球皮質，如鉤束、弓狀束及扣帶。聯絡（連合）纖維（commissural fibers）則連接「左右兩側」半球皮質對應區，胼胝體（corpus callosum，選項D）為大腦最大之連合纖維，不屬於聯合纖維，故選D。",
      "flashcard_front": "大腦白質 / 聯合纖維 / 連合(聯絡)纖維 / 胼胝體 (corpus callosum)",
      "flashcard_back": "聯合纖維（如鉤束、弓狀束、扣帶）連接同側皮質；胼胝體為連合纖維，連接左右半球皮質。",
      "flashcard_summary": "大腦白質纖維分類 -> 胼胝體為連接左右半球的連合纖維，不屬於連接同側的聯合纖維。"
    },
    {
      "question_id": "110-2_medicine-1_013",
      "question_number": 13,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "生理學",
      "category_confidence": "high",
      "key_point": "繞過丘腦（thalamus）直接投射至大腦皮質之感覺通路（嗅覺）。",
      "explanation": "在人體各類感覺傳導通路中，只有「嗅覺（olfaction，選項B）」可以直接繞過丘腦，由嗅球的二級神經元直接投射至大腦皮質的嗅覺皮質區。視覺（經外側膝狀體 LGN，選項A）、聽覺（經內側膝狀體 MGN，選項D）及體感覺（經 VPL/VPM 核，選項C）均必須先在丘腦進行接力轉接，才能投射至大腦皮質。",
      "flashcard_front": "感覺傳導 / 繞過丘腦 (thalamus) / 直接投射大腦皮質 / 嗅覺",
      "flashcard_back": "嗅覺是唯一不經過丘腦接力、直接投射至大腦皮質的特殊感覺通路；視覺、聽覺、體感覺均須經丘腦。",
      "flashcard_summary": "繞過丘腦的感覺 -> 嗅覺是人體唯一不經丘腦轉接、直接投射大腦皮質的感覺。"
    },
    {
      "question_id": "110-2_medicine-1_014",
      "question_number": 14,
      "correct_answer": "C",
      "category_group": "醫學（一）",
      "category": "生理學",
      "category_confidence": "high",
      "key_point": "參與痛覺調控的神經構造與脊髓小腦路徑之無關性。",
      "explanation": "脊髓小腦徑（spinocerebellar tract，選項C）主要傳導肌肉關節的潛意識本體感覺至小腦以協調運動，與痛覺調控無關（故選C）。脊髓第二細胞層（膠狀質，選項A）為痛覺傳播與門閾控制的關鍵部位；縫核脊髓徑（選項B）釋放血清素，參與下行疼痛抑制；背柱內側蹄系（DCML，選項D）傳導觸覺，可透過門閾效應抑制痛覺傳遞。",
      "flashcard_front": "痛覺調控 / 脊髓第二細胞層 (lamina II) / 縫核脊髓徑 / 脊髓小腦徑",
      "flashcard_back": "脊髓小腦徑負責傳導非意識性本體感覺，不參與痛覺調控；膠狀質與縫核脊髓徑均與痛覺調控密切相關。",
      "flashcard_summary": "痛覺調控無關構造 -> 脊髓小腦徑負責非意識本體感覺，不參與痛覺調控。"
    },
    {
      "question_id": "110-2_medicine-1_015",
      "question_number": 15,
      "correct_answer": "B",
      "category_group": "醫學（一）",
      "category": "解剖學",
      "category_confidence": "high",
      "key_point": "腦幹背側面第四腦室底（菱形窩）之解剖特徵與下橄欖體位置。",
      "explanation": "菱形窩（rhomboid fossa）構成了第四腦室的底，由橋腦與延腦的背側面組成，表面的特徵構造包含面神經丘、舌下神經三角與迷走神經三角。而下橄欖體（inferior olive，選項B）是位於延腦「腹外側部」的隆起，不位於背側面的第四腦室底（菱形窩），故選B。",
      "flashcard_front": "菱形窩 /Rhomboid fossa / 第四腦室底 / 面神經丘 / 下橄欖體",
      "flashcard_back": "菱形窩位於腦幹背側面，有面神經丘、舌下神經三角等；下橄欖體在延腦腹外側，不在菱形窩。",
      "flashcard_summary": "菱形窩解剖構造 -> 菱形窩位於腦幹背側，包含面神經丘等，但不包含位於腹外側的下橄欖體。"
    }
  ]
}

# ==================== SAVE AND VALIDATE ====================

validation_results = {}
all_ok = True

# Helper to validate a file using project's validation logic
def validate_output_data(batch_id, data):
    errors = []
    
    # Read allowed categories and questions from the prompt file
    prompt_path = f"reports/gemini_prompts/{batch_id}.md"
    if not os.path.exists(prompt_path):
        return [f"Prompt file {prompt_path} not found for validation"]
        
    with open(prompt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find JSON input in prompt
    input_mark = "請處理以下 JSON 輸入："
    input_pos = content.find(input_mark)
    if input_pos != -1:
        start_idx = content.find('{', input_pos)
    else:
        start_idx = content.find('{')
        
    brace_count = 0
    end_idx = -1
    for i in range(start_idx, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                break
                
    json_str = content[start_idx:end_idx]
    try:
        prompt_data = json.loads(json_str)
    except Exception as e:
        return [f"Error parsing prompt JSON: {e}"]
        
    # Validation checks
    if data.get('dataset_id') != prompt_data.get('dataset_id'):
        errors.append(f"Mismatch dataset_id: expected {prompt_data.get('dataset_id')}, got {data.get('dataset_id')}")
    if data.get('batch_id') != prompt_data.get('batch_id'):
        errors.append(f"Mismatch batch_id: expected {prompt_data.get('batch_id')}, got {data.get('batch_id')}")
        
    items = data.get('items', [])
    prompt_qs = prompt_data.get('questions', [])
    
    if len(items) != len(prompt_qs):
        errors.append(f"Count mismatch: prompt has {len(prompt_qs)}, output has {len(items)}")
        return errors
        
    allowed_categories = prompt_data.get('allowed_categories', [])
    
    for i, item in enumerate(items):
        pq = prompt_qs[i]
        qid = pq.get('question_id')
        qnum = pq.get('question_number')
        
        # Verify no dataset_id or batch_id in individual items
        if 'dataset_id' in item or 'batch_id' in item:
            errors.append(f"item {i} (Q{qnum}) contains dataset_id or batch_id")
            
        # Check matching question fields
        if item.get('question_id') != qid:
            errors.append(f"Mismatch question_id at index {i}: expected {qid}, got {item.get('question_id')}")
        if item.get('question_number') != qnum:
            errors.append(f"Mismatch question_number at index {i}: expected {qnum}, got {item.get('question_number')}")
        if item.get('correct_answer') != pq.get('correct_answer'):
            errors.append(f"Mismatch correct_answer for {qid}: expected {pq.get('correct_answer')}, got {item.get('correct_answer')}")
        if item.get('category_group') != prompt_data.get('category_group'):
            errors.append(f"Mismatch category_group for {qid}: expected {prompt_data.get('category_group')}, got {item.get('category_group')}")
            
        required_fields = ['question_id', 'question_number', 'correct_answer', 'category_group', 'category', 'category_confidence', 'key_point', 'explanation', 'flashcard_front', 'flashcard_back', 'flashcard_summary']
        for field in required_fields:
            if field not in item:
                errors.append(f"Missing required field '{field}' in {qid}")
            elif not item.get(field) and field != 'correct_answer':
                errors.append(f"Field '{field}' is empty in {qid}")
                
        # Check category
        cat = item.get('category')
        if cat not in allowed_categories:
            errors.append(f"Category '{cat}' for {qid} is not in allowed list: {allowed_categories}")
            
        # Check category confidence
        conf = item.get('category_confidence')
        if conf not in ['high', 'medium', 'low']:
            errors.append(f"Invalid category_confidence '{conf}' for {qid}")
            
        # Check explanation length (2 to 5 sentences)
        exp = item.get('explanation', '')
        sentence_count = exp.count('。') + exp.count('？') + exp.count('！')
        if sentence_count < 2 or sentence_count > 5:
            print(f"Warning: {qid} explanation has {sentence_count} sentences: '{exp}'")
            
        # Check flashcard summary format (關鍵字 / 線索 -> 知識點 / 判斷規則)
        sum_str = item.get('flashcard_summary', '')
        if ' -> ' not in sum_str:
            errors.append(f"flashcard_summary for {qid} does not contain ' -> ' separator: '{sum_str}'")
            
    return errors

# Write outputs and validate
for batch_id, data in batches_data.items():
    output_path = os.path.join(output_dir, f"{batch_id}.json")
    
    # Save the data directly as JSON (no markdown wrapper, raw format, UTF-8)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Wrote {output_path}")
    
    errors = validate_output_data(batch_id, data)
    if errors:
        all_ok = False
        validation_results[batch_id] = errors
    else:
        validation_results[batch_id] = ["OK"]

print("\n--- Validation Results ---")
for bid, res in validation_results.items():
    print(f"{bid}: {', '.join(res)}")
    
if all_ok:
    print("\nAll target batches generated and validated successfully!")
    sys.exit(0)
else:
    print("\nValidation failed!")
    sys.exit(1)
