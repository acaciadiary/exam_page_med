import json
import subprocess

updates = [
  {
    "id": "112-1_medicine-3_031",
    "category": "免疫風濕科",
    "category_confidence": "high",
    "key_point": "認知功能障礙是全身性紅斑狼瘡最常見的神經精神症狀。",
    "explanation": "【題幹解析】\n本題考查神經精神性紅斑狼瘡（Neuropsychiatric Systemic Lupus Erythematosus, NPSLE）的臨床表現與盛行率統計。NPSLE 是全身性紅斑狼瘡的嚴重併發症之一，可侵犯中樞與周邊神經系統。\n\n【選項詳解】\n- A. 認知功能障礙（Cognitive dysfunction）：在 NPSLE 的各種臨床表現中是最常見的，主要表現為注意力不集中、記憶力減退、執行功能受損等，文獻報導其盛行率在 SLE 患者中可達 50-80% 左右，此選項正確。\n- B. 橫斷性脊髓病變（Transverse myelopathy）：是 SLE 罕見但極為嚴重的神經病變，會導致截癱、感覺喪失與括約肌障礙，發生率通常小於 1-2%，此選項不選。\n- C. 腦出血（Cerebral hemorrhage）：雖然可能發生在伴有嚴重血小板低下或抗磷脂抗體症候群的患者中，但並非 NPSLE 常見的表現，此選項不選。\n- D. 自主神經不平衡（Autonomic nerve imbalance）：雖可能以心率變異度下降等形式存在，但在 NPSLE 的正式診斷指引（含ACR之19種NPSLE定義）中，並不是最主要和最常見的診斷表現，此選項不選。\n\n【核心考點】\n神經精神性紅斑狼瘡（NPSLE）的常見臨床表現：以認知功能障礙（Cognitive dysfunction）和頭痛（Headache）最為常見。",
    "flashcard_front": "SLE / NPSLE / 最常見神經症狀 / 認知功能障礙",
    "flashcard_back": "全身性紅斑狼瘡（SLE）最常見的神經精神症狀為認知功能障礙（cognitive dysfunction）和頭痛；橫斷性脊髓病變及腦出血較少見。",
    "flashcard_summary": "NPSLE 最常見表現 -> 認知功能障礙 (cognitive dysfunction)"
  },
  {
    "id": "112-1_medicine-3_032",
    "category": "免疫風濕科",
    "category_confidence": "high",
    "key_point": "肉芽腫併多發性血管炎（GPA）是典型的 ANCA 相關血管炎。",
    "explanation": "【題幹解析】\n抗中性白血球胞質抗體（Antineutrophil cytoplasmic antibodies, ANCA）是特定系統性小血管炎（稱為 ANCA-associated vasculitis, AAV）的核心致病與診斷性抗體。\n\n【選項詳解】\n- A. 血清病（Serum sickness）：屬於第三型（免疫複合物介導）超敏反應，與 ANCA 無關，此選項不選。\n- B. 川崎病（Kawasaki disease）：是累及中型血管的急性自限性血管炎，好發於嬰幼兒，其診斷依靠臨床症狀，血清 ANCA 通常為陰性，此選項不選。\n- C. 肉芽腫併多發性血管炎（Granulomatosis with polyangiitis, GPA，舊稱韋格納肉芽腫 Wegener's granulomatosis）：是一種典型的 ANCA 相關血管炎。患者血清中高機率能檢測到 ANCA，特別是針對蛋白酶-3（Proteinase 3）的 c-ANCA（PR3-ANCA），此選項最正確。\n- D. 膠原血管疾病相關血管炎（如 SLE 或 RA 相關血管炎）：主要是免疫複合物沉積引起，非 ANCA 相關血管炎，此選項不選。\n\n【核心考點】\nANCA 相關血管炎（AAV）的分類與診斷：GPA（c-ANCA / PR3-ANCA 陽性）、MPA（p-ANCA / MPO-ANCA 陽性）、EGPA（p-ANCA / MPO-ANCA 陽性）。",
    "flashcard_front": "血管炎 / ANCA / GPA / 韋格納肉芽腫 / PR3-ANCA",
    "flashcard_back": "肉芽腫併多發性血管炎（GPA）為 ANCA 相關血管炎（多呈 c-ANCA / PR3-ANCA 陽性）；川崎病、血清病等均非 ANCA 血管炎。",
    "flashcard_summary": "ANCA 相關血管炎代表 -> 肉芽腫併多發性血管炎 (GPA)"
  },
  {
    "id": "112-1_medicine-3_033",
    "category": "感染科",
    "category_confidence": "high",
    "key_point": "IL-5 主要調控嗜酸性球，與敗血症的急性發炎反應關係較不密切。",
    "explanation": "【題幹解析】\n敗血症（Sepsis）的病理生理關鍵在於病原體引發宿主產生失控的全身性發炎反應（SIRS）。在感染早期，巨噬細胞與內皮細胞被活化，釋放大量促發炎細胞激素（Pro-inflammatory cytokines），進而引發細胞激素風暴與器官衰竭。\n\n【選項詳解】\n- A. 白血球介素-5（Interleukin-5, IL-5）：是由 Th2 細胞分泌的細胞激素，主要負責刺激「嗜酸性白血球」的增殖、分化與活化。主要參與過敏性疾病與寄生蟲感染免疫，在敗血症的急性全身性發炎級聯反應中角色極不重要，此選項正確（關係最不密切）。\n- B. 白血球介素-1（Interleukin-1, IL-1）：是早期發炎的核心細胞激素，能活化內皮細胞、誘導發燒與急性期蛋白合成，在敗血症發病機制中極為關鍵，此選項不選。\n- C. 腫瘤壞死因子-α（Tumor necrosis factor α, TNF-α）：是敗血症早期釋放的最主要促發炎介質，可直接引發低血壓、血管擴張及內皮細胞損害，此選項不選。\n- D. 白血球介素-6（Interleukin-6, IL-6）：在敗血症中顯著升高，能誘導肝臟產生 C反應蛋白等急性反應物，是反映發炎嚴重度與預後的重要細胞激素，此選項不選。\n\n【核心考點】\n敗血症發炎級聯反應中的關鍵促發炎細胞激素（TNF-α, IL-1, IL-6）與 Th2 型細胞激素（IL-5）在功能上的區別。",
    "flashcard_front": "敗血症 / 發炎細胞激素 / 細胞激素風暴 / IL-5",
    "flashcard_back": "敗血症主要涉及 TNF-α、IL-1、IL-6 等促發炎細胞激素的急劇釋放；而 IL-5 主要是調控嗜酸性球，與敗血症無直接密切關係。",
    "flashcard_summary": "敗血症中不重要的細胞激素 -> Interleukin-5 (IL-5)"
  },
  {
    "id": "112-1_medicine-3_034",
    "category": "免疫風濕科",
    "category_confidence": "high",
    "key_point": "肉芽腫併多發性血管炎（GPA）屬於自體免疫疾病，不屬於自體發炎性疾病。",
    "explanation": "【題幹解析】\n本題考查自體發炎性疾病（Autoinflammatory diseases）與自體免疫性疾病（Autoimmune diseases）的分類區別。\n- 自體發炎性疾病：主要是「先天免疫系統」缺陷或調節異常所致，且無高力價的特異性自體抗體或抗原特異性 T 細胞。\n- 自體免疫性疾病：則是「後天/獲得性免疫系統」異常，針對自體抗原產生特異性抗體（B細胞）或致敏的 T 細胞。\n\n【選項詳解】\n- A. TRAPS（腫瘤壞死因子受體相關週期性症候群）：是常染色體顯性遺傳的自體發炎性疾病，因 TNFRSF1A 基因突變引起，此選項不選。\n- B. FMF（家族性地中海熱）：是典型的遺傳性自體發炎性疾病，因 MEFV 基因突變導致發炎小體異常活化，此選項不選。\n- C. GPA（肉芽腫併多發性血管炎）：是以 ANCA 自體抗體陽性為特徵的「自體免疫性小血管炎」，發病主要涉及 T 與 B 細胞的特異性獲得性免疫反應，不屬於先天免疫缺陷的自體發炎性疾病，此選項最符合。\n- D. NOMID（新生兒發病多系統發炎性疾病）：屬於 cryopyrin 相關週期性症候群的一種，由 NLRP3 基因突變引起發炎小體過度活化，是典型的自體發炎性疾病，此選項不選。\n\n【核心考點】\n自體發炎性疾病（先天免疫異常、發炎小體活化、FMF/TRAPS/CAPS）與自體免疫疾病（後天免疫異常、自體抗體/T細胞介導、GPA/SLE/RA）的本質差異。",
    "flashcard_front": "自體發炎性疾病 / 自體免疫疾病 / 先天免疫 / GPA / FMF",
    "flashcard_back": "自體發炎性疾病（如 FMF、TRAPS、NOMID）涉及先天免疫及發炎小體活化，無特異性抗體；GPA 屬於獲得性自體免疫小血管炎。",
    "flashcard_summary": "自體發炎與自體免疫疾病區分 -> GPA 為自體免疫，FMF/TRAPS/NOMID 為自體發炎"
  },
  {
    "id": "112-1_medicine-3_035",
    "category": "免疫風濕科",
    "category_confidence": "high",
    "key_point": "皮肌炎（DM）與惡性腫瘤風險增加密切相關，特別是中老年患者。",
    "explanation": "【題幹解析】\n本題考查特發性發炎性肌病（Idiopathic Inflammatory Myopathies, IIM）包括皮肌炎（DM）、多發性肌炎（PM）與包涵體肌炎（IBM）的臨床特徵、好發年齡與併發症。\n\n【選項詳解】\n- A. 包涵體肌炎（Inclusion body myositis, IBM）：好發於「50歲以上的老年人」，臨床常以不對稱的遠端肌肉無力與萎縮起步，非年輕人好發，此選項錯誤。\n- B. 皮肌炎（Dermatomyositis, DM）：除了典型的皮膚病變及近端肌無力外，常伴有豐富的「肌肉外表現」，最常見且危險的是「間質性肺病（ILD）」，也可累及心臟與關節，此選項錯誤。\n- C. 多發性肌炎（Polymyositis, PM）：多為散發性，雖然有 HLA 相關的易感性，但「並無」強烈的家族遺傳聚集現象，此選項錯誤。\n- D. 皮肌炎與惡性腫瘤（癌症）有強烈關聯，尤其在「中老年患者」中更為顯著，這常被視為副腫瘤表徵，常見的合併腫瘤包括乳癌、肺癌、卵巢癌。因此，新診斷皮肌炎的患者必須進行全面的癌症篩檢，此選項正確。\n\n【核心考點】\n發炎性肌肉病變（DM, PM, IBM）的鑑別：IBM 好發老年人；DM 與中老年人惡性腫瘤高度相關，且常合併間質性肺病（ILD）等肌肉外表現。",
    "flashcard_front": "皮肌炎 / 包涵體肌炎 / 多發性肌炎 / 癌症風險",
    "flashcard_back": "皮肌炎（DM）與中老年惡性腫瘤高度相關（副腫瘤表徵）；包涵體肌炎（IBM）好發 50 歲以上老年人且常侵犯遠端肌。",
    "flashcard_summary": "皮肌炎併發症與風險 -> 與中老年惡性腫瘤 (癌症) 有高度關聯"
  },
  {
    "id": "112-1_medicine-3_036",
    "category": "血液腫瘤科",
    "category_confidence": "high",
    "key_point": "子宮頸癌侵犯至膀胱黏膜屬於 Stage IVA，預後在所有選項中差。",
    "explanation": "【題幹解析】\n子宮頸癌的分期主要依據國際婦產科聯盟（FIGO）分期系統。分期愈晚，腫瘤侵犯的範圍愈廣，5年預後（存活率）愈差。\n\n【選項詳解】\n- A. 腫瘤侷限於子宮頸：為 Stage I（第一期），5年存活率通常大於 80-90%，預後最好，此選項不選。\n- B. 腫瘤侵犯到陰道下 1/3：屬於 Stage IIIA（第三期 A），5年存活率約為 40-50%，此選項不選。\n- C. 腫瘤侵犯到骨盆側壁：屬於 Stage IIIB（第三期 B），5年存活率約為 30-40%，此選項不選。\n- D. 腫瘤侵犯至「膀胱或直腸的黏膜」：屬於 Stage IVA（第四期 A），代表已屬晚期，5年存活率通常小於 15-20%，預後在所有選項中差，此選項最符合。\n\n【核心考點】\nFIGO 子宮頸癌分期及其臨床意義：第一期局限子宮頸，第三期侵犯陰道下1/3或骨盆壁，第四期A侵犯膀胱或直腸黏膜，分期越晚預後越差。",
    "flashcard_front": "子宮頸癌 / FIGO 分期 / 膀胱侵犯 / 預後評估",
    "flashcard_back": "子宮頸癌侵犯至膀胱或直腸黏膜屬於 Stage IVA（第四期A），5年存活率顯著降低，為選項中預後最差者。",
    "flashcard_summary": "子宮頸癌膀胱受侵犯 FIGO 分期 -> Stage IVA (第四期 A)"
  },
  {
    "id": "112-1_medicine-3_037",
    "category": "血液腫瘤科",
    "category_confidence": "high",
    "key_point": "與大腸癌高度相關的是牛鏈球菌菌血症，而非腸球菌菌血症。",
    "explanation": "【題幹解析】\n本題考查大腸直腸癌（Colorectal Cancer, CRC）的危險因子（飲食、遺傳性綜合症、慢性炎症、以及特定的細菌感染關聯）。\n\n【選項詳解】\n- A. 高動物性脂肪與紅肉飲食：消化過程中會增加膽酸分泌，大腸細菌會將其轉化為具致癌性的次級膽酸，是 CRC 的公認環境危險因子，此選項不選。\n- B. 發炎性腸道疾病（IBD，特別是長期且廣泛的潰瘍性大腸炎 UC）：由於腸道黏膜長期反覆發炎，罹患大腸癌的風險隨病程顯著增加，此選項不選。\n- C. 遺傳性非息肉症大腸直腸癌（Lynch 症候群）：是由 DNA 錯配修復（MMR）基因突變引起的染色體顯性遺傳病，患者一生中罹患大腸癌的風險高達 70-80%，此選項不選。\n- D. 腸球菌菌血症（Enterococcus bacteremia）：腸球菌是常見的尿路或腹腔感染致病菌，但在臨床上並無與大腸癌的明確關聯性。與大腸直腸癌高度相關的細菌感染是「牛鏈球菌菌血症（Streptococcus bovis / Streptococcus gallolyticus bacteremia）」，因此「腸球菌菌血症」的描述最不恰當，此選項正確。\n\n【核心考點】\n大腸癌的危險因子，特別是與大腸癌有高度關聯性的特定病原體感染：牛鏈球菌（Streptococcus bovis）而非腸球菌（Enterococcus）。",
    "flashcard_front": "大腸直腸癌 / 菌血症關聯 / 牛鏈球菌 / 腸球菌 / Lynch症候群",
    "flashcard_back": "與大腸癌密切相關的細菌為牛鏈球菌（S. bovis/S. gallolyticus），其感染者常合併大腸腺瘤或癌；腸球菌菌血症與大腸癌無特異相關性。",
    "flashcard_summary": "與大腸癌具高度關聯性的細菌 -> 牛鏈球菌 (Streptococcus bovis/gallolyticus)"
  },
  {
    "id": "112-1_medicine-3_038",
    "category": "血液腫瘤科",
    "category_confidence": "high",
    "key_point": "藥物誘發之急性溶血性貧血伴隨咬痕細胞且 Coombs 陰性高度提示 G6PD 缺乏症。",
    "explanation": "【題幹解析】\n本題考查藥物誘發之急性溶血性貧血。\n1. 病史：23歲年輕男性，感冒服藥2天後出現暗紅色尿。小學時有類似「吃感冒藥後尿色變暗、數天後自癒」的病史，提示為基因缺陷性疾病在特定藥物誘發下的急性溶血。\n2. 實驗室檢查：\n   - 暗紅色尿、尿潛血陽性，但尿沉渣無紅血球（RBC 0-2/HPF）：顯示尿中為「遊離血紅素」，代表發生了「血管內溶血」。\n   - 網狀紅血球（Reticulocyte 7.6%）及 LDH（1,080 U/L）顯著上升：提示骨髓代償造血及細胞溶血釋放。\n   - 總膽紅素 4.3 mg/dL，直接型 0.8 mg/dL：以間接型膽紅素升高為主，符合溶血性黃疸。\n   - Coombs test 陰性：排除抗體介導的自體免疫性溶血性貧血（AIHA）。\n   - 抹片特徵：G6PD 缺乏症典型抹片會出現 Heinz bodies 及 bite cells 咬痕細胞。\n\n【選項詳解】\n- A. 自體免疫溶血性貧血（AIHA）：通常 Coombs test 呈陽性，且多為血管外溶血，此患者為陰性，此選項排除。\n- B. 葡萄糖-6-磷酸去氫酶缺乏症（G6PD deficiency，俗稱蠶豆症）：為X染色體聯鎖遺傳。患者在接觸特定藥物（如氧化性藥物磺胺類、解熱鎮痛藥）後，紅血球因缺乏 NADPH 無法對抗氧化壓力，導致急性血管內溶血，數天後隨老化紅血球溶完、新紅血球生成可自癒，完全符合此案，此選項最正確。\n- C. 急性腎絲球腎炎（AGN）：暗紅色尿若因腎小球腎炎引起，尿中應有大量變形紅血球，且潛血陽性時顯微鏡檢會看到紅血球，與本題 RBC 0-2/HPF 且 Coombs 陰性溶血不符，此選項排除。\n- D. 急性肝炎（Acute hepatitis）：黃疸雖可能由肝炎引起，但急性肝炎會伴隨 ALT/AST 極度升高，且尿液呈深色是因直接膽紅素排入尿液，本例 ALT 正常，且為間接膽紅素升高及溶血表徵，此選項排除。\n\n【核心考點】\nG6PD 缺乏症（蠶豆症）的急性溶血臨床表徵（氧化性藥物誘發、血管內溶血血紅素尿、間接膽紅素上升、LDH升高、Coombs 陰性、咬痕細胞/Heinz小體）。",
    "flashcard_front": "G6PD 缺乏症 / 藥物誘發 / 血管內溶血 / Coombs 陰性 / 尿液沉渣",
    "flashcard_back": "吃感冒藥後急性血管內溶血（尿潛血陽性但無 RBC），且 Coombs 試驗陰性、有既往自癒史，高度診斷為 G6PD 缺乏症（蠶豆症）。",
    "flashcard_summary": "藥物誘發急性血管內溶血且 Coombs 陰性 -> 優先考慮 G6PD 缺乏症"
  },
  {
    "id": "112-1_medicine-3_039",
    "category": "血液腫瘤科",
    "category_confidence": "high",
    "key_point": "骨髓大量漿細胞浸潤與骨骼穿鑿樣溶骨病變是多發性骨髓瘤的特徵。",
    "explanation": "【題幹解析】\n62歲中老年男性，因跌倒就醫，實驗室檢查呈現正球性貧血（Hb 7.6 g/dL, MCV 85 fL）與輕度血小板低下。\n- 骨骼 X 光：顯示多處穿鑿樣溶骨性病變（punched-out lytic lesions，典型出現在顱骨、脊椎骨、肋骨等處）。\n- 骨髓抹片：見到大量異常增生的「漿細胞（plasma cells）」，通常 ≧ 10%，漿細胞具有偏心核、深藍色質及核旁庭。\n這些特徵均高度指向多發性骨髓瘤。\n\n【選項詳解】\n- A. 腺癌併多處骨轉移：雖然可能引起貧血及溶骨性病變，但其骨髓抹片應見到成團的轉移性上皮癌細胞，而非單一的漿細胞大量浸潤，此選項不選。\n- B. 嚴重維生素D缺乏：會引起骨質流失與骨質軟化，但不會在 X 光片上呈現多發性、邊界清晰的穿鑿樣溶骨結節，且不會伴有骨髓內大量異常漿細胞，此選項排除。\n- C. 多發性骨髓瘤（Multiple Myeloma）：是漿細胞惡性增生性疾病。臨床典型符合 CRAB 標準：血鈣上升（C）、腎功能不全（R）、貧血（A，此例 Hb 7.6）、骨折/骨痛/溶骨病變（B）。骨髓抹片內可見 > 10% 惡性漿細胞，此選項最正確。\n- D. 原發性骨癌併多處轉移：臨床罕見以多發性顱骨穿鑿樣病變及骨髓大量漿細胞浸潤起病，此選項排除。\n\n【核心考點】\n多發性骨髓瘤（Multiple Myeloma）的診斷核心：CRAB 準則、X 光片穿鑿樣溶骨病變、骨髓抹片中惡性漿細胞（Plasma cells）比例 ≧ 10%。",
    "flashcard_front": "多發性骨髓瘤 / X光顱骨穿鑿樣 / 骨髓抹片 / CRAB 準則",
    "flashcard_back": "多發性骨髓瘤（MM）特徵為骨髓惡性漿細胞浸潤 ≧ 10% 及多處 punched-out 溶骨病變，臨床表現包括高血鈣、腎衰、貧血及骨折。",
    "flashcard_summary": "多發性骨髓瘤診斷指標 -> 骨髓漿細胞 ≧ 10% 與穿鑿樣溶骨病變"
  },
  {
    "id": "112-1_medicine-3_040",
    "category": "血液腫瘤科",
    "category_confidence": "high",
    "key_point": "KPS 70分表示癌症患者可自理生活但無法進行正常工作或活動。",
    "explanation": "【題幹解析】\nKarnofsky Performance Status (KPS) 是腫瘤科常用來評估癌症患者生理活動功能的量表，評分範圍為 0 到 100 分，分數越高代表患者活動能力及自理能力越好。\n\n【選項詳解】\n- A. KPS 100 分：無任何症狀，活動及工作不受限。KPS 90 分：能進行正常活動及工作，僅有輕微症狀。\n- B. KPS 10-20 分：垂危或瀕死，需要住院及積極支持治療，完全無法自理。\n- C. KPS 70 分的定義是：「能照料自己，但不能維持正常生活或工作」，此敘述完全正確。\n- D. KPS 50 分的定義是：「需要相當多的協助及頻繁的醫療照料」。KPS 60 分為：「偶爾需要協助，但大部分時間能自理日常生活」。\n\n【核心考點】\nKarnofsky 活動狀態量表（KPS）各分段定義：70分代表能自理生活但無法正常工作/活動；60分以下代表開始需要他人照護協助。",
    "flashcard_front": "Karnofsky / KPS / 癌症活動能力 / 70分定義",
    "flashcard_back": "KPS 70分定義為「能自理生活，但已無法進行正常工作或正常活動」；80-90分代表能正常工作但有症狀；60分以下需要他人協助。",
    "flashcard_summary": "Karnofsky (KPS) 70 分定義 -> 能自我照顧，但無法維持正常活動或工作"
  }
]

# Write to json file
with open('scratch/updates_112-1_medicine-3_batch4.json', 'w', encoding='utf-8') as f:
    json.dump(updates, f, ensure_ascii=False, indent=2)

# Run update command
res = subprocess.run([
    'python', 'scripts/exams/update_question_fields.py',
    '--exam-file', 'public/data/exams/112-1/medicine-3.json',
    '--updates-file', 'scratch/updates_112-1_medicine-3_batch4.json'
], capture_output=True, text=True)

print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
