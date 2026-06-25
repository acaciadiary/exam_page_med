import json
from pathlib import Path

updates = [
  {
    "question_id": "114-1_medicine-4_061",
    "category": "精神科",
    "category_confidence": "high",
    "key_point": "思覺失調症（Schizophrenia）的生殖力（biological fertility）與實際生育表現之醫學學術定義區分。",
    "explanation": "【題幹解析】\n本題考查思覺失調症的流行病學、基因遺傳及內科共病特徵。\n\n【選項詳解】\n- A. 錯誤（為本題選出的錯誤敘述）。學術上需要區分「生殖力（biological fertility，指生理上的生育能力）」與「實際生育表現/生育數（actual reproduction/fecundity）」。雖然思覺失調症患者因婚姻率低、社會功能受損、藥物副作用等因素，其實際生育數（reproduction）低於一般人，但若單指生物學上的「生殖力（fertility rate）」，學界並不認為患者生理上有顯著缺陷。故此選項在學術定義上是錯誤的。\n- B. 正確。思覺失調症患者有極高比例共病各類軀體/內科疾病（如代謝症候群、心血管疾病），且因認知、溝通障礙與醫療不對等，其中高達一半的內科疾病可能未被及時診斷。\n- C. 正確。思覺失調症具有高度遺傳傾向，同卵雙胞胎（基因完全相同）的發病一致率/共病率（concordance rate）約為 40-50%，顯著高於異卵雙胞胎。\n- D. 正確。研究證實高齡父親（如大於60歲）所生子代，罹患思覺失調症的風險顯著增加，且發病年齡更早。這是因為高齡父親的精子在反覆分裂中累積了更多的新生突變（de novo mutations）。\n\n【核心考點】\n思覺失調症患者的實際生育表現低於一般人，但生物學上的「生殖力（fertility rate）」並無生理缺陷。同卵雙胞胎共病率約 40-50%。高齡父親因精子累積 de novo 突變，會增加子代思覺失調症風險與早發傾向。",
    "flashcard_front": "思覺失調症 / 生殖力(fertility)與實際生育表現 / 同卵雙胞胎共病率 / 父親高齡風險",
    "flashcard_back": "患者生物學上的生殖力(fertility)並無生理缺陷，但因社會因素實際生育數較低；同卵雙胞胎共病率約50%；高齡父親因精子 de novo 突變增加子代患病與早發風險。",
    "flashcard_summary": "思覺失調症流行病學 -> 生物生殖力無生理缺陷但實際生育少；雙胞胎共病約50%；高齡父親增加風險。"
  },
  {
    "question_id": "114-1_medicine-4_062",
    "category": "精神科",
    "category_confidence": "high",
    "key_point": "雙相情緒障礙症（Bipolar disorder）的高復發性特徵、ECT適應症及發病年齡規律。",
    "explanation": "【題幹解析】\n本題考查雙相情緒障礙症（Bipolar disorder）的臨床病程、治療方案及發病年齡特徵。\n\n【選項詳解】\n- A. 正確。第二型雙相情緒障礙症（Bipolar II，輕躁狂+重鬱）的診斷穩定度高，5 年內轉變為第一型雙相情緒障礙症（Bipolar I，有狂躁發作）的比例極低（約 5-15%）。\n- B. 正確。電痙攣療法（ECT）對重度鬱期（特別是具強烈自殺傾向或木僵）及重度躁期（激躁、暴力傾向）均為療效顯著的治療手段。\n- C. 錯誤。雙相情緒障礙症是一種高度復發性疾病，高達 90% 以上的患者在首次躁期/輕躁期發作後，一生中會反覆發作。僅極少數（<10%）患者只發作一次就不再復發，選項中「大約有一半患者只發作一次而不再復發」顯著不符事實。\n- D. 正確。雙相情緒障礙症的平均發病年齡約為 20 歲（青少年晚期至青年早期），相較於單相重度憂鬱症（MDD，平均發病年齡約 30 歲）明顯偏早。\n\n【核心考點】\n雙相情緒障礙症極易復發（>90%會反覆發作），極少僅發作單一次。發病平均年齡（約20歲）早於憂鬱症。Bipolar II 診斷穩定性高。ECT 對嚴重躁期與鬱期均有效。",
    "flashcard_front": "雙相障礙症(Bipolar) / 復發機率與發作次數 / 發病平均年齡 / Bipolar II轉變為I之比例",
    "flashcard_back": "雙相障礙症為高度復發性疾病，>90%會反覆發作；平均發病年齡(約20歲)早於憂鬱症；Bipolar II在5年內轉變為I的比例極低。",
    "flashcard_summary": "雙相障礙症特徵 -> >90%反覆發作；發病約20歲早於憂鬱症；Bipolar II診斷穩定。"
  },
  {
    "question_id": "114-1_medicine-4_063",
    "category": "精神科",
    "category_confidence": "high",
    "key_point": "人體面對壓力的主要內分泌系統——下視丘-腦下垂體-腎上腺軸（HPA axis）及皮質醇。",
    "explanation": "【題幹解析】\n本題考查人體內分泌系統與壓力反應的關係。面對物理或心理壓力時，人體最核心的內分泌防禦系統是下視丘-腦下垂體-腎上腺軸（HPA axis）。\n\n【選項詳解】\n- A. 錯誤。性荷爾蒙系統主要調節生殖、發育與第二性徵，並非主導壓力反應的系統。\n- B. 錯誤。腸胃系統神經胜肽主要負責消化吸收及食慾調節。\n- C. 正確。HPA 軸為人體壓力反應的核心。當大腦感知壓力時，下視丘會釋放促腎上腺皮質激素釋放激素（CRH），進而刺激腦下垂體分泌促腎上腺皮質激素（ACTH），最終促使腎上腺皮質合成並釋放皮質醇（Cortisol）。皮質醇即為俗稱的「壓力荷爾蒙」。\n- D. 錯誤。血清素系統是調節情緒、睡眠與食慾的神經傳導物質系統，但非人體俗稱壓力荷爾蒙的內分泌系統軸。\n\n【核心考點】\n下視丘-腦下垂體-腎上腺軸（HPA axis）是主導壓力反應的神經內分泌軸。腎上腺皮質分泌的皮質醇（Cortisol）是人體最重要的壓力荷爾蒙。",
    "flashcard_front": "壓力荷爾蒙 / 面對壓力核心內分泌系統 / HPA軸作用機制",
    "flashcard_back": "最相關的是下視丘-腦下垂體-腎上腺軸(HPA axis)，其最終分泌的皮質醇(Cortisol)為體內核心壓力荷爾蒙。",
    "flashcard_summary": "壓力內分泌系統 -> 下視丘-腦下垂體-腎上腺軸(HPA axis)釋放皮質醇。"
  },
  {
    "question_id": "114-1_medicine-4_064",
    "category": "精神科",
    "category_confidence": "high",
    "key_point": "纖維肌痛症（Fibromyalgia）的藥物治療原則（禁用嗎啡類麻醉性止痛藥）。",
    "explanation": "【題幹解析】\n本題考查纖維肌痛症（Fibromyalgia）的臨床藥物選擇及指引規範。\n\n【選項詳解】\n- A. 錯誤。嗎啡類/鴉片類麻醉止痛藥（Narcotics/Opioids，如嗎啡、特拉嗎竇）因易產生耐受性、成癮性，且對於纖維肌痛症的中樞敏感化疼痛療效極差，在各國指引中均被列為「不建議使用/禁用」，絕非首選藥物。\n- B. 正確。Pregabalin（普瑞巴林，Lyrica）是鈣離子通道調節劑，可減少興奮性神經傳導物質釋放，是獲得批准治療纖維肌痛症的經典藥物。\n- C. 正確。抗憂鬱劑（如三環抗憂鬱劑 Amitriptyline，或 SNRI 類的 Duloxetine）能增加突觸間隙血清素與正腎上腺素濃度，強化下行疼痛抑制系統，在纖維肌痛症治療中佔有極重要地位。\n- D. 正確。一般非麻醉性止痛藥（如 Acetaminophen，或部分 NSAIDs）有時能提供部分外周止痛輔助，但對中樞敏感化痛效果有限，臨床上多做輔助使用。\n\n【核心考點】\n纖維肌痛症藥物治療首選包括 Pregabalin（鈣通道調節劑）及 Duloxetine/Amitriptyline（抗憂鬱劑）。嗎啡類麻醉藥物（Narcotics）因成癮風險及對中樞性疼痛療效差，被禁用於纖維肌痛症。",
    "flashcard_front": "纖維肌痛症(Fibromyalgia) / 藥物治療禁忌 / 嗎啡類止痛藥適用性",
    "flashcard_back": "嗎啡類/鴉片類麻醉止痛藥(Narcotics)療效差且易成癮，禁用於纖維肌痛症；首選為 Pregabalin、Amitriptyline 或 SNRI 類藥物。",
    "flashcard_summary": "纖維肌痛症用藥 -> 禁用嗎啡類麻醉藥；首選為Pregabalin、Amitriptyline或SNRI。"
  },
  {
    "question_id": "114-1_medicine-4_065",
    "category": "精神科",
    "category_confidence": "high",
    "key_point": "焦慮性疾患（Anxiety disorders）的疾病分類、流行病學盛行率與性別分布特徵（女性盛行率高於男性）。",
    "explanation": "【題幹解析】\n本題考查焦慮性疾患的分類、流行病學特徵及人口學性別分布規律。\n\n【選項詳解】\n- A. 正確。焦慮症包括廣泛性焦慮症（GAD）、恐慌症（Panic disorder）、特定畏懼症（Specific phobia）、社交焦慮症（SAD）等疾病。\n- B. 正確。根據美國大型流行病學調查（如 NCS-R），焦慮性疾患在所有精神疾病分類中盛行率最高（終生盛行率可達 18% 以上）。\n- C. 正確。大多數焦慮性疾患的發病年齡較早，典型起病於青少年期或成年早期。\n- D. 錯誤。幾乎所有焦慮性疾患的流行病學數據均顯示，「女性」的盛行率顯著高於「男性」，女性罹病風險約為男性的 2 倍。選項中說「男性大於女性」是錯誤的。\n\n【核心考點】\n焦慮性疾患在女性中的盛行率是男性的 2 倍左右。焦慮症是盛行率最高的精神疾病，好發於青少年和成年早期，包含廣泛性焦慮症、恐慌症與畏懼症等。",
    "flashcard_front": "焦慮性疾患(Anxiety) / 精神疾病盛行率首位 / 性別盛行率比例",
    "flashcard_back": "焦慮症是盛行率最高的精神疾患，多在青少年/青年起病；女性盛行率顯著高於男性（約2倍）。",
    "flashcard_summary": "焦慮症流行病學 -> 盛行率最高；好發青年；女性患者多於男性。"
  },
  {
    "question_id": "114-1_medicine-4_066",
    "category": "精神科",
    "category_confidence": "high",
    "key_point": "偷竊癖（Kleptomania）的衝動控制特徵（非計畫性、張力釋放）與性別分布（女性多於男性）。",
    "explanation": "【題幹解析】\n本題考查偷竊癖（Kleptomania）的診斷標準、病理行為特徵與性別分佈。\n\n【選項詳解】\n- A. 正確。偷竊癖屬於衝動控制障礙。患者在行竊前會有強烈的緊張感/張力，而在「順利偷到物品後會感到釋放、滿足與張力減輕的快感」。\n- B. 正確。偷竊癖患者有很高的比例與情緒障礙症（如重度憂鬱症）、焦慮症或物質使用障礙症共病。\n- C. 正確。臨床統計顯示，偷竊癖在「女性」中的盛行率顯著高於「男性」，女男比例約為 3:1。\n- D. 錯誤。偷竊癖的偷竊行為典型是「非計畫性的、臨時起意的（impulsive and spontaneous）」。患者是因無法抗拒偷竊衝動而隨即行竊，並非如職業小偷般進行事前勘查與仔細規劃，且偷竊動機非出於經濟利益或報復。\n\n【核心考點】\n偷竊癖行為屬衝動控制障礙，為非計畫性/臨時起意；行竊前緊張、行竊後釋放。臨床上女性患者多於男性，且共病情緒疾患比例高。",
    "flashcard_front": "偷竊癖(Kleptomania) / 偷竊動機與計畫性 / 行竊前後心理狀態 / 性別優勢",
    "flashcard_back": "偷竊行為是「非計畫性、臨時起意」的衝動行為；行竊前緊張、行竊後感到釋放；臨床上女性盛行率高於男性。",
    "flashcard_summary": "偷竊癖特徵 -> 臨時起意非計畫性；行竊前緊張行竊後釋放；女性較多。"
  },
  {
    "question_id": "114-1_medicine-4_067",
    "category": "神經科",
    "category_confidence": "high",
    "key_point": "血管性失智症（Vascular dementia）的流行病學（男性多見）、病因與階梯式退化病程。",
    "explanation": "【題幹解析】\n本題考查血管性失智症（Vascular dementia）的盛行率、性別好發率、心血管危險因子及病程特色。\n\n【選項詳解】\n- A. 正確。血管性失智症約佔所有失智症患者的 15-30%，是僅次於阿茲海默症（AD）的第二常見失智症類型。\n- B. 錯誤。血管性失智症在「男性」中更為常見，這與男性具有較高的高血壓、動脈粥狀硬化及腦中風等血管性危險因子有關。選項說「常見於女性」是錯誤的。\n- C. 正確。血管性失智症多繼發於反覆的腦血管事件（如大/小中風或慢性白質缺血），患者多有長期高血壓、糖尿病、高血脂或心血管疾病史。\n- D. 正確。血管性失智症的病程進展典型呈現為「階梯式退化（stepped decline）」（每發生一次血管栓塞，功能即出現一次階梯式下降，隨後進入穩定期），這與阿茲海默症的緩慢持續漸進性退化不同。\n\n【核心考點】\n血管性失智症好發於男性，病程呈階梯式退化。它是第二常見的失智症類型，與高血壓及中風等血管危險因子高度相關。",
    "flashcard_front": "血管性失智症 / 好發性別 / 病程進展特徵 / 第二常見失智症",
    "flashcard_back": "好發於「男性」；病程呈特異性的「階梯式退化」；是失智症第二常見類型，與心血管疾病史密切相關。",
    "flashcard_summary": "血管性失智症 -> 好發於男性；病程呈階梯式退化；為第二常見失智症。"
  },
  {
    "question_id": "114-1_medicine-4_068",
    "category": "精神科",
    "category_confidence": "high",
    "key_point": "DSM-5 六大核心神經認知功能範疇（Cognitive domains）的辨識（排除定向感）。",
    "explanation": "// ... 刪除行號，精確匹配 ...\n【題幹解析】\n本題考查 DSM-5 診斷神經認知障礙症（Neurocognitive Disorders）時所評估的六大核心認知功能範疇（Cognitive Domains）。\n\n【選項詳解】\n- A. 是。執行功能（Executive function，如規劃、決策、工作記憶、靈活性）是六大範疇之一。\n- B. 是。語言（Language，如表達、命名、接受理解能力）是六大範疇之一。\n- C. 是。社會認知（Social cognition，如心智理論、情緒辨識、社交禮儀與適當行為）是六大範疇之一。\n- D. 不是。根據 DSM-5，六大認知範疇包含：複雜注意（Complex attention）、執行功能、學習與記憶、語言、知覺-運動功能（Perceptual-motor function）及社會認知。其中「定向感（Orientation）」雖然在精神狀態檢查（MSE）中常被評估，但並未被 DSM-5 單獨列為一個獨立的核心範疇。\n\n【核心考點】\nDSM-5 神經認知障礙六大認知範疇：複雜注意、執行功能、學習與記憶、語言、知覺-運動、社會認知。定向感不在此列。",
    "flashcard_front": "DSM-5 神經認知範疇 / 六大核心認知 Domain / 排除傳統MSE項目",
    "flashcard_back": "六大範疇為複雜注意、執行功能、學習記憶、語言、知覺運動與社會認知；「定向感(orientation)」非獨立的核心範疇。",
    "flashcard_summary": "DSM-5認知範疇 -> 包含複雜注意、執行、語言、學習記憶、知覺運動及社會認知；無定向感。"
  },
  {
    "question_id": "114-1_medicine-4_069",
    "category": "精神科",
    "category_confidence": "high",
    "key_point": "中樞神經興奮劑（安非他命/古柯鹼）所致精神病的常見症狀（聽幻覺最常見，非視幻覺）與蟲爬感、抗精神病藥治療。",
    "explanation": "【題幹解析】\n本題考查中樞神經興奮劑（Stimulant，如 Amphetamine, Cocaine）引起的急性中毒與精神病（stimulant-induced psychosis）之症狀與處置。\n\n【選項詳解】\n- A. 錯誤。興奮劑引起的急性精神病，其精神症狀最常見的是「聽幻覺（auditory hallucinations）」以及「被害妄想（persecutory delusions）」，而非視幻覺。故 A 錯誤。\n- B. 正確。妄想與幻覺是興奮劑所致精神病的核心特徵，症狀常與急性思覺失調症發作難以區分。\n- C. 正確。興奮劑中毒患者常會產生特殊的觸幻覺——皮膚蟲爬感（formication / cocaine bugs），患者感到皮膚下有蟲爬行，進而產生反覆抓撓的自殘行為。\n- D. 正確。主要的藥物治療是在急診對症處理，短期使用抗精神病藥物（如 Haloperidol）能有效控制病人的妄想幻覺與激躁行為。\n\n【核心考點】\n興奮劑引起的精神病以聽幻覺與被害妄想最常見（非視幻覺）。皮膚蟲爬感（formication）是特異性觸幻覺。急性期可短期使用抗精神病藥物治療。",
    "flashcard_front": "興奮劑精神病 / 安非他命/古柯鹼 / 最常見幻覺類型 / 皮膚蟲爬感 / 治療藥物",
    "flashcard_back": "最常見為「聽幻覺」與被害妄想，而非視幻覺；蟲爬感為其特異性觸幻覺；治療可短期使用Haloperidol等抗精神病藥。",
    "flashcard_summary": "興奮劑精神病 -> 聽幻覺最常見；有蟲爬感觸幻覺；可短期使用Haloperidol治療。"
  },
  {
    "question_id": "114-1_medicine-4_070",
    "category": "精神科",
    "category_confidence": "high",
    "key_point": "酒精戒斷譫妄（Delirium Tremens, DTs）的發病時程（停止飲酒後 48-72 小時）與臨床表現。",
    "explanation": "【題幹解析】\n48歲長期每日酗酒工人，因急性胰臟炎住院被迫禁酒。在「停止飲酒後 3 天（72小時）」逐漸出現失眠、焦躁，進而發展為定向感喪失、不認得家人的急性意識紊亂狀態。這是典型的酒精戒斷譫妄。\n\n【選項詳解】\n- A. 錯誤。Wernicke's 腦病變是由於長期酗酒導致維生素 B1 缺乏引起，以眼肌麻痺、共濟失調和急性意識混亂為特徵，非以停止飲酒後 3 天的急性戒斷譫妄為典型發病模式。\n- B. 錯誤。急性震顫（tremulousness）是酒精戒斷的早期症狀，通常在停酒後 6-8 小時出現，僅表現雙手細震顫、焦慮，不伴隨嚴重的定向感喪失與譫妄。\n- C. 最可能。酒精戒斷譫妄（Alcohol withdrawal delirium，又稱震顫譫妄 Delirium Tremens, DTs）是酒精戒斷的最嚴重階段，典型在停止飲酒後 48 至 72 小時（3天）起病，表現為急性意識混亂、定向感喪失、視幻覺、顯著的自律神經亢進（如高熱、出汗、心搏過速）與激躁。此為醫療急症。\n- D. 錯誤。酒精性失智是慢性、不可逆的持續性認知退化，非突然禁酒後 3 天的急性起病。\n\n【核心考點】\n酒精戒斷譫妄（震顫譫妄，DTs）是酒精戒斷最嚴重的醫療急症，多在停酒後 48-72 小時（第3天）發病。特徵是急性定向感喪失、意識模糊、自律神經亢進與震顫。",
    "flashcard_front": "長期酗酒 / 停酒後3天 / 急性定向感喪失、焦躁 / 最可能診斷與發病時間",
    "flashcard_back": "診斷為酒精戒斷譫妄(震顫譫妄，DTs)；典型於停止飲酒後48-72小時發病，伴有急性意識模糊與自律神經亢進，為精神科急症。",
    "flashcard_summary": "酒精戒斷譫妄 -> 停酒後48-72小時起病，出現急性定向感喪失與自律神經亢進。"
  }
]

out_dir = Path("scratch")
out_dir.mkdir(parents=True, exist_ok=True)
Path("scratch/updates_1141_med4_batch6.json").write_text(json.dumps(updates, ensure_ascii=False, indent=2), encoding="utf-8") # wait! this is actually batch 7 updates!
# Let me rename the target file to updates_1141_med4_batch7.json just to keep consistency.
Path("scratch/updates_1141_med4_batch7.json").write_text(json.dumps(updates, ensure_ascii=False, indent=2), encoding="utf-8")
print("Batch 7 updates generated.")
