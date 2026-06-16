# -*- coding: utf-8 -*-
import json
import os

os.makedirs("reports/gemini_outputs", exist_ok=True)

batches_data = {}

# ==========================================
# BATCH 110-1_medicine-2_batch-002
# ==========================================
batches_data["110-1_medicine-2_batch-002"] = {
    "dataset_id": "110-1_medicine-2",
    "batch_id": "110-1_medicine-2_batch-002",
    "category_group": "醫學（二）",
    "items": [
        {
            "question_id": "110-1_medicine-2_016",
            "question_number": 16,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "真菌菌絲的基本形態分類。",
            "explanation": "真菌菌絲依據有無橫隔，可分為隔菌絲（septate hyphae）與無隔的多核體菌絲（coenocytic hyphae）兩種基本形態。假菌絲通常見於酵母菌發芽後未脫離的構造，而鎖狀連接菌絲則是擔子菌綱特有的結構，非基本形態。",
            "flashcard_front": "真菌菌絲 / 橫隔有無 / 兩種基本形態",
            "flashcard_back": "真菌菌絲基本形態分為有橫隔的隔菌絲，與無橫隔且多核的多核體菌絲。",
            "flashcard_summary": "真菌菌絲基本形態 -> 隔菌絲與多核體菌絲。"
        },
        {
            "question_id": "110-1_medicine-2_017",
            "question_number": 17,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "預防百日咳桿菌的疫苗組成成分。",
            "explanation": "目前臨床上使用的百日咳疫苗主要是無細胞百日咳疫苗（acellular pertussis vaccine），其成分包含純化的百日咳毒素等特定抗原，副作用較全細胞疫苗低。脂多醣體具內毒素活性不適合作為疫苗，而減毒疫苗及莢膜多醣體亦非目前預防百日咳之主要疫苗形式。",
            "flashcard_front": "百日咳桿菌 / 疫苗組成 / 副作用降低",
            "flashcard_back": "目前預防百日咳主要採用無細胞疫苗（acellular vaccine），安全性較舊型全細胞疫苗高。",
            "flashcard_summary": "百日咳疫苗成分 -> 主要為無細胞疫苗（acellular vaccine）。"
        },
        {
            "question_id": "110-1_medicine-2_018",
            "question_number": 18,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "流感病毒感染人體時的免疫反應與機轉。",
            "explanation": "CD8+ T細胞主要透過其表面的TCR特異性結合受感染細胞呈獻的MHC-I抗原，隨後釋放穿孔素 and 顆粒酶來毒殺細胞，並非藉由抗體依賴性細胞毒殺作用（ADCC）發揮功能。ADCC主要是由自然殺手細胞（NK cells）或巨噬細胞透過Fc受體結合已結合抗體的靶細胞來執行。因此選項C敘述錯誤。",
            "flashcard_front": "CD8+ T細胞 / 細胞毒殺 / ADCC / 流感免疫",
            "flashcard_back": "CD8+ T細胞主要透過TCR/MHC-I特異性毒殺受感染細胞，而ADCC主要由NK細胞或巨噬細胞透過Fc受體媒介。",
            "flashcard_summary": "CD8 T細胞與ADCC -> CD8 T細胞直接特異性毒殺，ADCC則由NK細胞等透過Fc受體執行。"
        },
        {
            "question_id": "110-1_medicine-2_019",
            "question_number": 19,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "補體調控蛋白對膜攻擊複合物（MAC）形成的抑制機制。",
            "explanation": "CD59（又稱protectin）是膜表面補體調控蛋白，能直接與C5b-8或C9結合，進而阻止C9的聚合化，抑制膜攻擊複合物（MAC）的形成以保護自體細胞。CD46（MCP）與CD55（DAF）則是干擾C3/C5轉化酶的形成或加速其衰變，而C1 inhibitor則是作用於補體活化的最上游。因此選項A正確。",
            "flashcard_front": "補體調控 / 膜攻擊複合物 / C9聚合抑制 / CD59",
            "flashcard_back": "CD59直接結合C5b-8阻斷C9聚合以抑制MAC形成；CD55與CD46則主要調控C3/C5轉化酶。",
            "flashcard_summary": "C9聚合抑制蛋白 -> CD59直接干擾C9聚合以阻止MAC形成。"
        },
        {
            "question_id": "110-1_medicine-2_020",
            "question_number": 20,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "專業性抗原呈獻細胞大量表現的特有分子。",
            "explanation": "專業性抗原呈獻細胞（APC，如樹突細胞、巨噬細胞與B細胞）大量表現MHC class II分子，以呈獻外源性抗原給CD4 T細胞。MHC class I則普遍存在於所有有核細胞表面，用以呈獻內源性抗原給CD8 T細胞。因此選項B正確。",
            "flashcard_front": "專業性APC / CD4 T細胞 / 抗原呈獻 / MHC分子",
            "flashcard_back": "專業性抗原呈獻細胞藉由大量表現 MHC class II 分子，將抗原呈獻給 CD4 T 細胞。",
            "flashcard_summary": "APC抗原呈獻 -> 專業性APC藉由大量表現MHC class II分子將抗原呈獻給CD4 T細胞。"
        },
        {
            "question_id": "110-1_medicine-2_021",
            "question_number": 21,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "抗體多樣性產生機制與腫瘤免疫療法作用原理。",
            "explanation": "官方答案為D。抗體轉換（isotype switching）僅改變抗體重鏈的恆定區（Fc），決定其 effector function，而不改變與抗原結合的可變區，因此不會貢獻抗原辨識的多樣性。另外，腫瘤細胞突變後通常表現PD-L1或引發T細胞表現CTLA-4，施打抗CTLA-4或PD-1抗體能阻斷抑制訊號進而活化T細胞，但此療法受腫瘤微環境影響，並非對所有突變腫瘤都有一致療效。",
            "flashcard_front": "抗體轉換 / 多樣性貢獻 / 腫瘤免疫療法 / CTLA-4",
            "flashcard_back": "抗體轉換只改變重鏈恆定區（Fc）而不改變結合位，不貢獻多樣性；CTLA-4是T細胞上的抑制受體而非腫瘤細胞本身表現。",
            "flashcard_summary": "抗體轉換與多樣性 -> 抗體轉換只改變重鏈恆定區，不增加抗原結合多樣性。"
        },
        {
            "question_id": "110-1_medicine-2_023",
            "question_number": 23,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "不同抗體亞型與其相應Fc受體（FcR）的結合特異性。",
            "explanation": "不同亞型的抗體（如IgG的不同亞型IgG1, IgG2, IgG3, IgG4）與特定的Fc受體結合親和力有很大差異，例如IgG1和IgG3對FcγRI有高親和力，而IgG2和IgG4親和力極低。游離抗體雖能與某些高親和力FcR結合，但通常需要抗原結合後的多價交聯才能啟動強烈的活化或抑制訊號。因此選項B錯誤。",
            "flashcard_front": "抗體亞型 / Fc受體 / 親和力差異 / 免疫細胞活化",
            "flashcard_back": "不同亞型抗體與同一種FcR的結合親和力不同；通常需要抗原結合形成免疫複合物以多價交聯活化受體。",
            "flashcard_summary": "抗體與Fc受體結合 -> 不同抗體亞型與Fc受體結合之親和力具有顯著差異。"
        },
        {
            "question_id": "110-1_medicine-2_024",
            "question_number": 24,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "人體黏膜組織的主要抗體類型。",
            "explanation": "人體黏膜表面（如腸道、呼吸道）主要產生的抗體是二聚體的分泌型IgA（SIgA），能有效中和黏膜表面的病原體及食物抗原（如麩質蛋白）。IgG是血清中含量最多的抗體，IgM是初次免疫反應產生的抗體，而IgD主要作為成熟B細胞表面的受體。因此選項B正確。",
            "flashcard_front": "黏膜表面 / 食物抗原 / 主要抗體類型 / 麩質蛋白",
            "flashcard_back": "黏膜組織對抗原的主要防禦抗體為分泌型IgA（sIgA）。",
            "flashcard_summary": "黏膜主要抗體 -> 黏膜組織對抗原（如食物）產生的主要抗體是IgA。"
        },
        {
            "question_id": "110-1_medicine-2_025",
            "question_number": 25,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "結核桿菌在巨噬細胞內的免疫逃脫機制。",
            "explanation": "結核桿菌（Mycobacterium tuberculosis）是一種胞內寄生菌，被巨噬細胞吞噬後，能藉由其細胞壁的特殊成分（如硫脂質）抑制吞噬體與溶酶體的融合（phagosome-lysosome fusion），從而在吞噬體內生存與繁殖。抗原漂移（antigenic drift）及基因轉換主要見於病毒或原蟲，阻斷MHC class I並非其主要生存機制。因此選項D正確。",
            "flashcard_front": "結核桿菌 / 胞內寄生 / 巨噬細胞 / 免疫逃脫",
            "flashcard_back": "結核桿菌藉由抑制吞噬體與溶酶體的融合，在巨噬細胞內生存並逃避殺傷。",
            "flashcard_summary": "結核桿菌逃脫機制 -> 抑制吞噬體與溶酶體的融合以在胞內生存。"
        },
        {
            "question_id": "110-1_medicine-2_026",
            "question_number": 26,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "腫瘤免疫編輯（immunoediting）三個階段的定義與影響。",
            "explanation": "腫瘤免疫編輯包含清除（elimination）、平衡（equilibrium）和逃脫（escape）三個階段。在免疫編輯過程中，免疫系統會對腫瘤施加選擇壓力，導致腫瘤細胞產生突變、抗原表現消失或細胞特性改變，從而逃避宿主免疫清除，促使腫瘤生長與擴散。因此促進T細胞毒殺導致腫瘤縮小不符合免疫編輯之逃脫逃逸機制，選項D錯誤。",
            "flashcard_front": "腫瘤免疫編輯 / 三個階段 / 免疫逃脫 / 選擇壓力",
            "flashcard_back": "腫瘤免疫編輯會使腫瘤細胞突變或喪失抗原以逃避清除，促使腫瘤進展，而非導致腫瘤縮小。",
            "flashcard_summary": "腫瘤免疫編輯結果 -> 免疫選擇壓力導致腫瘤產生逃脫特性，促使腫瘤進展而非縮小。"
        },
        {
            "question_id": "110-1_medicine-2_027",
            "question_number": 27,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "器官移植後超急性排斥反應（hyperacute rejection）的成因。",
            "explanation": "移植後數分鐘至數小時內發生的超急性排斥反應，主要原因在於受體血液中已存在針對移植物供體抗原（如ABO血型抗原或HLA抗原）的預存抗體（pre-existing antibodies）。這些抗體與供體血管內皮細胞結合，活化補體系統並導致血管內血栓形成與移植物壞死。MHC不合引起的細胞介導排斥通常需要數天以上。因此選項C正確。",
            "flashcard_front": "腎臟移植 / 10分鐘內排斥 / 超急性排斥 / 自體抗體",
            "flashcard_back": "超急性排斥反應（數分鐘內）是由受體體內已預存對抗供體血管內皮抗原之抗體所引起。",
            "flashcard_summary": "超急性排斥成因 -> 受體體內預存抗體活化補體導致急性血管血栓壞死。"
        },
        {
            "question_id": "110-1_medicine-2_028",
            "question_number": 28,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "Rituximab單株抗體的作用靶點與臨床應用。",
            "explanation": "Rituximab 是一種針對 B 細胞表面特異性抗原 CD20 的嵌合型單株抗體，主要用於治療非何杰金氏淋巴瘤及自體免疫疾病。CD20 表現於前 B 細胞至成熟 B 細胞表面，但不表現在造血幹細胞與漿細胞。因此，使用 Rituximab 會特異性清除 B 細胞，而不影響 T 細胞或樹突細胞。選項C正確。",
            "flashcard_front": "Rituximab / CD20 單抗 / 淋巴瘤治療 / 細胞剔除",
            "flashcard_back": "Rituximab 特異性結合 B 細胞表面的 CD20 分子，藉由 ADCC 或 CDC 機轉清除 B 細胞。",
            "flashcard_summary": "Rituximab 作用靶點 -> 針對 B 細胞表面的 CD20 以特異性清除 B 細胞。"
        },
        {
            "question_id": "110-1_medicine-2_029",
            "question_number": 29,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "菲律賓毛線蟲感染的傳播途徑與臨床症狀。",
            "explanation": "菲律賓毛線蟲（Capillaria philippinensis）多因生食或吃未煮熟含有感染性幼蟲的淡水魚（如生魚片）而感染。蟲體寄生在小腸，會破壞腸黏膜，導致嚴重腹瀉、低蛋白血症及低血鉀、低血鈣等嚴重電解質失衡。海獸胃線蟲主要侵犯胃部造成劇烈胃痛；旋毛蟲多因吃豬肉感染且侵犯肌肉；有棘頜口線蟲多引起皮膚幼蟲移行症。因此選項A正確。",
            "flashcard_front": "生魚片 / 嚴重電解質失衡 / 低蛋白血症 / 寄生蟲",
            "flashcard_back": "生食淡水魚感染菲律賓毛線蟲，會破壞小腸黏膜引起嚴重腹瀉與多種電解質流失。",
            "flashcard_summary": "菲律賓毛線蟲感染 -> 生食淡水魚引起，導致小腸黏膜受損、嚴重腹瀉與低蛋白/低電解質血症。"
        },
        {
            "question_id": "110-1_medicine-2_030",
            "question_number": 30,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "廣東住血線蟲的傳播媒介與診斷方法。",
            "explanation": "廣東住血線蟲（Angiostrongylus cantonensis）的幼蟲常污染生菜（如生食受蝸牛或蛞蝓爬過殘留幼蟲的蔬菜），因此吃生菜沙拉亦可能感染，選項C敘述錯誤。人體感染後，幼蟲移行至腦部常引起嗜伊紅性腦膜炎，患者腦脊髓液中嗜酸性白血球顯著增加，且確診手段之一是在腦脊髓液中發現幼蟲。因此選項C為錯誤陳述。",
            "flashcard_front": "廣東住血線蟲 / 嗜伊紅性腦膜炎 / 傳播途徑 / 腦脊髓液",
            "flashcard_back": "吃受感染螺類或蛞蝓污染的生菜沙拉會感染廣東住血線蟲，引起嗜伊紅性腦膜炎。",
            "flashcard_summary": "廣東住血線蟲傳播 -> 經由生食螺類、蛞蝓或受污染生菜而感染，引起嗜伊紅性腦膜炎。"
        },
        {
            "question_id": "110-1_medicine-2_031",
            "question_number": 31,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "顆粒性包生絛蟲的宿主關係與病理特徵。",
            "explanation": "顆粒性包生絛蟲（Echinococcus granulosus）以犬科動物為終宿主，羊、牛等為中間宿主，人類係因食入受犬糞中絛蟲卵污染的食物或水而感染，而非食入羊肉感染（食入羊肉內包生囊只會使犬隻感染）。幼蟲在人體肝臟（最常見）或肺臟會形成包生囊（hydatid cyst）。泡狀囊是由多房包生絛蟲（E. multilocularis）引起，且人體內蟲體無法發育成熟，糞便中檢不出蟲卵。因此選項B正確。",
            "flashcard_front": "顆粒性包生絛蟲 / 包生囊 (hydatid cyst) / 傳染源 / 中間宿主",
            "flashcard_back": "人因攝入犬糞污染之蟲卵而感染包生絛蟲，最常在肝臟形成邊界清楚的單房包生囊。",
            "flashcard_summary": "顆粒性包生絛蟲特徵 -> 食入犬糞污染之蟲卵感染，最常在肝臟形成單房包生囊。"
        }
    ]
}

# ==========================================
# BATCH 110-1_medicine-2_batch-003
# ==========================================
batches_data["110-1_medicine-2_batch-003"] = {
    "dataset_id": "110-1_medicine-2",
    "batch_id": "110-1_medicine-2_batch-003",
    "category_group": "醫學（二）",
    "items": [
        {
            "question_id": "110-1_medicine-2_032",
            "question_number": 32,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "各類吸蟲與原蟲在人體造成異位病變的傾向。",
            "explanation": "薑片蟲（Fasciolopsis buski）成蟲主要寄生於人體的小腸，通常不會移行或在腦部造成異位病變。相對地，日本血吸蟲的蟲卵可隨血流引發腦部肉芽腫；衛氏肺吸蟲的幼蟲或成蟲可移行至腦部引起病變；異形異形吸蟲的蟲卵可隨血流堵塞腦血管。因此選項C最不可能在腦部造成異位病變。",
            "flashcard_front": "寄生蟲感染 / 腦部異位病變 / 日本血吸蟲 / 衛氏肺吸蟲 / 薑片蟲",
            "flashcard_back": "薑片蟲僅寄生於小腸，不侵犯腦部；日本血吸蟲、衛氏肺吸蟲、異形吸蟲皆可能在腦部造成異位病變。",
            "flashcard_summary": "腦部異位病變寄生蟲 -> 薑片蟲寄生於小腸，不引起腦部異位病變。"
        },
        {
            "question_id": "110-1_medicine-2_033",
            "question_number": 33,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "瘧疾感染引起的臨床併發症及其病理機制。",
            "explanation": "黑水熱（blackwater fever）與急性血管內溶血有關，主要是由於患者產生抗體攻擊受感染的紅血球，引發嚴重溶血和血紅素尿，導致茶色或黑色尿液，其發生通常與自體免疫以及奎寧治療有關。腎絲球腎炎主要由免疫複合物沉積引起；熱帶脾腫大是由免疫球蛋白（IgM）與B細胞增生所致；低血糖與胰島素過度分泌或葡萄糖消耗有關。選項B敘述正確。",
            "flashcard_front": "瘧疾併發症 / 黑水熱 (blackwater fever) / 血管內溶血 / 自體免疫",
            "flashcard_back": "黑水熱與自體免疫相關，因產生抗體攻擊受瘧原蟲感染紅血球，造成嚴重血管內溶血及血紅素尿。",
            "flashcard_summary": "黑水熱機轉 -> 自體免疫抗體攻擊受瘧原蟲感染紅血球，引起嚴重溶血。"
        },
        {
            "question_id": "110-1_medicine-2_034",
            "question_number": 34,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "犬複殖器絛蟲（瓜實絛蟲）的傳播媒介與人體感染路徑。",
            "explanation": "人類主要是因無意中食入帶有犬複殖器絛蟲（Dipylidium caninum）擬囊尾幼蟲（cysticercoid）的貓蚤或狗蚤而感染。此病多見於與寵物密切接觸的嬰幼兒。犬蛔蟲感染是因食入蟲卵；犬鉤蟲主要經皮膚穿刺；菲律賓毛線蟲經食入生魚感染。因此選項B正確。",
            "flashcard_front": "誤食蚤類 / 擬囊尾幼蟲 / 犬複殖器絛蟲 / 寵物接觸",
            "flashcard_back": "誤食感染擬囊尾幼蟲的貓狗蚤，會感染犬複殖器絛蟲；主要寄生於人體腸道。",
            "flashcard_summary": "貓狗蚤與寄生蟲 -> 誤食蚤類主要感染犬複殖器絛蟲。"
        },
        {
            "question_id": "110-1_medicine-2_035",
            "question_number": 35,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "寄生蟲學",
            "category_confidence": "high",
            "key_point": "采采蠅傳播的寄生蟲種類。",
            "explanation": "采采蠅（tsetse fly）為非洲錐蟲病（睡眠病）的傳播媒介，經叮咬將岡比亞錐蟲（Trypanosoma brucei gambiense）或羅得西亞錐蟲傳播給人類。利什曼原蟲是由白蛉（sandfly）傳播，而枯西氏錐蟲（美洲錐蟲）是由錐鼻蟲（triatomine bug）的糞便污染傷口傳播。因此選項C正確。",
            "flashcard_front": "采采蠅 (tsetse fly) / 非洲睡眠病 / 傳播媒介 / 錐蟲",
            "flashcard_back": "采采蠅是傳播非洲錐蟲（如岡比亞錐蟲）的媒介；美洲錐蟲由錐鼻蟲傳播，利什曼原蟲由白蛉傳播。",
            "flashcard_summary": "采采蠅傳播寄生蟲 -> 采采蠅為非洲錐蟲（岡比亞錐蟲）的傳播媒介。"
        },
        {
            "question_id": "110-1_medicine-2_036",
            "question_number": 36,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "病例對照研究與世代研究的優缺點比較。",
            "explanation": "病例對照研究（Case-control study）從已發病的病例出發，回溯其過去的暴露史，因此極易產生選擇性偏差（selection bias）與回憶偏差。相比之下，世代研究（Cohort study）需要較長的研究時間與更多的樣本數，且病例對照研究的優點之一是能同時探討多個可能病因。因此選項A為其主要缺點。",
            "flashcard_front": "病例對照研究 / 缺點 / 選擇性偏差 / 暴露回溯",
            "flashcard_back": "病例對照研究易受選擇性偏差和回顧回憶偏差影響；相較世代研究，它省時省力且能探討多重病因。",
            "flashcard_summary": "病例對照研究缺點 -> 易產生選擇性偏差與回憶偏差。"
        },
        {
            "question_id": "110-1_medicine-2_037",
            "question_number": 37,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "流行病學抽樣設計與率的合併估計原則。",
            "explanation": "本研究採用分層隨機抽樣（年輕人與老年人各100人），在未考慮兩者在總人口中的實際比例（權重）前，直接將兩組樣本合併計算（如直接相加得出0.32）來估計總人口罹患率是不正確的。隨機抽樣必須維持個體獨立性，排擠群聚效應。因此選項D最不恰當。",
            "flashcard_front": "率的估計 / 分層抽樣 / 合併樣本 / 獨立性假設",
            "flashcard_back": "分層抽樣後不應在未加權情況下直接合併估計總人口率；合併必須依據人口群體權重計算。",
            "flashcard_summary": "率的合併估計 -> 分層抽樣樣本不可在未加權下直接合併計算總人口罹患率。"
        },
        {
            "question_id": "110-1_medicine-2_038",
            "question_number": 38,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "利用信賴區間重疊與否判斷統計顯著差異。",
            "explanation": "在雙樣本的假說檢定中，若兩組獨立樣本的95%信賴區間完全不重疊，則在統計顯著水準α=0.05下，兩組平均值具有顯著差異。A校（94~98分）與C校（100~106分）的區間完全不重疊，故兩校的智商分數差異具有顯著性。A與B（98~106分）有交點98，B與D（104~108分）及C與D有重疊，故無法直接宣稱顯著。因此選項B正確。",
            "flashcard_front": "95%信賴區間 / 統計顯著差異 / 區間不重疊 / 顯著水準",
            "flashcard_back": "若兩組獨立樣本的95%信賴區間完全無重疊（如94~98與100~106），則兩組均值差異顯著（P<0.05）。",
            "flashcard_summary": "信賴區間與顯著差異 -> 兩獨立樣本95%信賴區間完全不重疊時，其均值差異在0.05水準下顯著。"
        },
        {
            "question_id": "110-1_medicine-2_039",
            "question_number": 39,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "溫室氣體與大氣懸浮微粒對全球暖化的影響特徵。",
            "explanation": "二氧化碳是除水蒸氣外最主要的溫室氣體，能吸收紅外線導致地表暖化。相反地，懸浮微粒主要是散射太陽輻射，在地球大氣中產生冷卻效應（陽傘效應），因此懸浮微粒對氣溫的影響與二氧化碳相反，並非一致與加成。選項B敘述最不恰當。",
            "flashcard_front": "全球暖化 / 溫室氣體 / 懸浮微粒 / 陽傘效應",
            "flashcard_back": "二氧化碳導致地球暖化，而大氣懸浮微粒則藉由散射陽光產生冷卻效應，兩者作用相反。",
            "flashcard_summary": "懸浮微粒與暖化 -> 懸浮微粒具有冷卻（防曬）效應，與CO2的暖化作用相反。"
        },
        {
            "question_id": "110-1_medicine-2_040",
            "question_number": 40,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "臺灣烏腳病流行之成因與環境暴露因子。",
            "explanation": "臺灣西南沿海烏腳病（Blackfoot disease）之流行，主因是當地居民長期飲用含有高濃度無機砷的深井水（deep well water），而非地表河流的井水。毛髮和指甲可用於測定慢性砷暴露，而自來水普及後砷暴露已顯著下降。本題官方正解為A，但在實際考試中一律給分。",
            "flashcard_front": "烏腳病 / 砷暴露 / 深井水 / 臺灣沿海",
            "flashcard_back": "烏腳病主要因居民飲用高無機砷的「深井水」所致；本題官方公布正解A且該題一律給分。",
            "flashcard_summary": "烏腳病與砷暴露 -> 烏腳病是由飲用含高濃度砷的深井水引起，非地河井水。"
        },
        {
            "question_id": "110-1_medicine-2_041",
            "question_number": 41,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "氯乙烯暴露與肝血管肉瘤的職業病關聯。",
            "explanation": "肝血管肉瘤（hepatic angiosarcoma）是一種罕見的惡性腫瘤，與石化工廠中氯乙烯單體（vinyl chloride monomer, VCM）的職業暴露有極為密切的關聯。二異氰酸甲苯主要引起職業性氣喘，錳暴露可引起類似巴金森氏症的錳中毒，鉛暴露則會導致造血與神經系統病變。因此選項C正確。",
            "flashcard_front": "肝血管肉瘤 / 職業暴露 / 氯乙烯 / 石化工廠",
            "flashcard_back": "肝血管肉瘤是極為罕見的腫瘤，高度特異性關聯於氯乙烯單體（VCM）的職業暴露。",
            "flashcard_summary": "肝血管肉瘤職業病 -> 與接觸氯乙烯（vinyl chloride）暴露密切相關。"
        },
        {
            "question_id": "110-1_medicine-2_042",
            "question_number": 42,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "工作場所空氣有害物質8小時日時量平均容許濃度定義。",
            "explanation": "8小時日時量平均容許濃度（PEL-TWA）是指勞工在每日工作8小時，每週工作40小時，每週工作5天的正常情況下，終其一生重複暴露在此濃度下，大部分勞工不會發生不良健康效應的濃度。因此選項C符合標準定義。",
            "flashcard_front": "PEL-TWA / 8小時容許濃度 / 工作時間標準 / 危害防制",
            "flashcard_back": "PEL-TWA 是指正常工作日（每日8小時、每週40小時、每週5天）下，重複暴露不致產生健康危害的平均濃度上限。",
            "flashcard_summary": "PEL-TWA 時間定義 -> 基礎於每日工作8小時、每週工作40小時、每週5天。"
        },
        {
            "question_id": "110-1_medicine-2_043",
            "question_number": 43,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "世界衛生組織推廣健康城市的內涵與精神。",
            "explanation": "健康城市（Healthy Cities）強調的是一個持續改善健康環境、促進居民共同參與的「過程」（process），而非一個單一的終點或結果。健康城市的行動應基於地方的優先次序，支持跨區域合作與世界資源公平分配。因此選項A中稱其「與過程無關」最不恰當。",
            "flashcard_front": "健康城市 / 持續過程 / 社區參與 / 衛生策略",
            "flashcard_back": "健康城市是一個持續發展與改善的「過程」，並非單純的結果，極度依賴市民參與 and 跨部門合作。",
            "flashcard_summary": "健康城市定義 -> 健康城市強調動態發展的過程，而非單一的結果。"
        },
        {
            "question_id": "110-1_medicine-2_044",
            "question_number": 44,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "健康行為改變跨理論模式（Transtheoretical Model）的階段區分。",
            "explanation": "跨理論模式（TTM）中，想運動但尚未行動（預計在未來6個月內採取行動）屬於沉思期（contemplation phase）；而已經開始購買運動器材但尚未建立規律運動習慣（預計在未來1個月內行動）則屬於準備期（preparation phase）。懵懂期為無改變意願，行動期為已開始規律運動但未滿6個月。因此選項C正確。",
            "flashcard_front": "行為改變階段 / 跨理論模式 / 想運動尚未行動 / 買器材未規律",
            "flashcard_back": "想運動但未行動為「沉思期」；已買器材但未建立規律習慣為「準備期」（積極規劃中）。",
            "flashcard_summary": "行為改變階段 -> 想運動未動為沉思期，備好器材未規律為準備期。"
        },
        {
            "question_id": "110-1_medicine-2_045",
            "question_number": 45,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "臺灣非法藥物防制法規與減害治療措施。",
            "explanation": "依據毒品危害防制條例，K他命列為第三級毒品。若施用第一、二級毒品者，可享有戒癮治療或觀察勒戒等觀察期，有機會獲得緩起訴；而單純施用第三、四級毒品者，主要處以行政罰鍰與接受毒品危害講習，並非一律會被檢察官起訴。海洛因替代療法則常使用美沙冬。選項C敘述最不恰當。",
            "flashcard_front": "毒品防制 / 施用級數 / 起訴條件 / 行政罰與刑罰",
            "flashcard_back": "單純施用第三、四級毒品（如K他命）以行政罰為主，不會一律被起訴；一、二級毒品施用可採觀察勒戒或戒癮治療之緩起訴程序。",
            "flashcard_summary": "毒品處罰與起訴 -> 單純使用第三級毒品為行政罰，非一律刑事起訴。"
        },
        {
            "question_id": "110-1_medicine-2_046",
            "question_number": 46,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "大眾媒體長期傳播內容對青少年認知形成的影響理論。",
            "explanation": "涵化理論（cultivation theory）認為，大眾媒體（特別是電視）若長期反覆傳播某種訊息（如暴力的英雄主義），會逐漸塑造青少年的世界觀，使其認為媒體呈現的虛擬情境就是真實社會的反映。創新擴散關乎新觀念的普及，媒體倡導為推動政策，知溝理論關乎社會階層間知識獲取的差距。因此選項C正確。",
            "flashcard_front": "大眾媒體 / 暴力英雄 / 反映社會真實 / 傳播理論",
            "flashcard_back": "涵化理論（Cultivation Theory）指出長期接觸大眾媒體會使受眾接受媒體建構的現實世界認知。",
            "flashcard_summary": "涵化理論定義 -> 長期觀看媒體內容會使受眾將媒體情境投射為社會真實。"
        }
    ]
}

# ==========================================
# BATCH 110-1_medicine-2_batch-004
# ==========================================
batches_data["110-1_medicine-2_batch-004"] = {
    "dataset_id": "110-1_medicine-2",
    "batch_id": "110-1_medicine-2_batch-004",
    "category_group": "醫學（二）",
    "items": [
        {
            "question_id": "110-1_medicine-2_047",
            "question_number": 47,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "傷害防制（injury prevention）的範疇與概念定義。",
            "explanation": "傷害防制（injury prevention and control）的範疇同時包含了非蓄意性傷害（如車禍、跌倒、溺水等意外事故）與蓄意性傷害（如暴力、虐待、自殺等）。選項A指出傷害防制僅是預防「蓄意」造成的傷害，窄化了其定義與範疇，故為最不恰當之敘述。",
            "flashcard_front": "傷害防制 / 定義範疇 / 蓄意與非蓄意 / 流行病學模式",
            "flashcard_back": "傷害防制涵蓋非蓄意性傷害（意外）及蓄意性傷害（家暴/自殺等），非僅限於預防蓄意傷害。",
            "flashcard_summary": "傷害防制範疇 -> 包含非蓄意性傷害（意外）與蓄意性傷害。"
        },
        {
            "question_id": "110-1_medicine-2_048",
            "question_number": 48,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "健保醫療給付支付制度之財務節約誘因比較。",
            "explanation": "在各類健保支付制度中，論人計酬（capitation）是以特定服務人口為基準單位，無論其就醫次數，均支付固定費用。這使醫療提供者具有最大的節約誘因，以預防疾病來降低醫療成本。相反地，論量計酬的基準單位最小，易導致醫療資源過度使用。因此選項D正確。",
            "flashcard_front": "支付制度 / 基準單位最大 / 醫療節約誘因 / 論人計酬",
            "flashcard_back": "論人計酬支付基準為特定人口數，對醫療端省資源、預防保健的節約誘因最大。",
            "flashcard_summary": "健保支付誘因 -> 論人計酬的財務基準單位最大，能提供最大的節約誘因。"
        },
        {
            "question_id": "110-1_medicine-2_049",
            "question_number": 49,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "世界衛生組織（WHO）的組織功能與現今挑戰。",
            "explanation": "世界衛生組織（WHO）是聯合國系統內專門負責國際公共衛生的機構，其最高決策權力單位是世界衛生大會（WHA）。技術合作是WHO的核心功能之一，選項B聲稱其不包含技術合作是錯誤的。此外，經費短缺與組織效率問題確為其目前重大挑戰。因此選項B為最不恰當的敘述。",
            "flashcard_front": "世界衛生組織 / 核心功能 / 世界衛生大會 / 技術合作",
            "flashcard_back": "世界衛生組織的核心功能包括技術合作、設定健康標準和應對國際衛生挑戰，WHA為其最高權力單位。",
            "flashcard_summary": "WHO功能 -> 技術合作是世界衛生組織的核心功能之一。"
        },
        {
            "question_id": "110-1_medicine-2_050",
            "question_number": 50,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "公共衛生學",
            "category_confidence": "high",
            "key_point": "平衡計分卡（Balanced Scorecard）各構面的指標特徵與應用。",
            "explanation": "平衡計分卡（BSC）包含財務、顧客、內部流程、學習與成長四個構面。其中，財務指標為「落後指標」（lagging indicator），反映過去的經營成果，而其他三個構面則多為「領先指標」（leading indicator）用以預測未來財務表現。在非營利事業中，常會調整或增加其他構面。因此選項C敘述錯誤。",
            "flashcard_front": "平衡計分卡 (BSC) / 財務構面 / 落後指標 / 領先指標",
            "flashcard_back": "平衡計分卡中的財務構面屬於落後指標；顧客、內部流程及學習成長構面為領先指標。",
            "flashcard_summary": "平衡計分卡財務指標 -> 財務構面指標屬於落後指標而非領先指標。"
        },
        {
            "question_id": "110-1_medicine-2_051",
            "question_number": 51,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "藥物基因體學中特定HLA基因型與嚴重皮膚不良反應的關聯性。",
            "explanation": "抗病毒藥物 abacavir（治療HIV）在用藥前必須先檢測 HLA-B*5701 基因型，若為陽性則極易發生嚴重全身性過敏反應（如發燒、廣泛性紅疹與器官衰竭）。而 carbamazepine 需篩檢 HLA-B*1502 以預防史帝芬強生症候群（SJS），allopurinol 則與 HLA-B*5801 相關。因此選項C正確。",
            "flashcard_front": "HLA-B*5701 / 嚴重過敏 / 用藥前基因檢測 / 抗病毒藥物",
            "flashcard_back": "抗病毒藥物 Abacavir 易誘發 HLA-B*5701 陽性患者產生嚴重全身性過敏反應，用藥前必須篩檢此基因型。",
            "flashcard_summary": "HLA-B*5701 與藥物 -> Abacavir 用藥前須檢測 HLA-B*5701 基因型。"
        },
        {
            "question_id": "110-1_medicine-2_052",
            "question_number": 52,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "青黴素類抗生素的藥物動力學與耐藥機制。",
            "explanation": "Amoxicillin 對胃酸穩定，但其主要的耐藥機制在於許多致病菌能產生β-內醯胺酶（β-内酰胺酶）將其結構水解。Ampicillin 和 amoxicillin 的吸收均可能受到飲食影響；Dicloxacillin 對胃酸穩定因此口服吸收良好；Nafcillin 主要由膽汁排泄（肝臟代謝與排泄），而非腎臟。因此選項C正確。",
            "flashcard_front": "Amoxicillin / β-內醯胺酶 / 藥物吸收與排泄 / Nafcillin 膽汁排泄",
            "flashcard_back": "Amoxicillin 對酸穩定，但易被細菌產生的 β-lactamase 水解；Nafcillin 主要由膽汁（肝）排除而非腎臟。",
            "flashcard_summary": "Amoxicillin 抗藥機制 -> 耐藥性主要來自細菌產生的 β-內醯胺酶水解作用。"
        },
        {
            "question_id": "110-1_medicine-2_053",
            "question_number": 53,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "抗腫瘤單株抗體的作用靶點、臨床應用及不良反應。",
            "explanation": "Catumaxomab 是一種雙特異性單株抗體（bispecific antibody），能同時結合腫瘤細胞表面的 EpCAM 和 T 細胞上的 CD3，從而將 T 細胞招募至腫瘤部位殺傷癌細胞。Alemtuzumab 針對 CD52，極易引起顯著的淋巴球減少症；Bevacizumab 抑制 VEGF 會延緩傷口癒合，不宜在手術後即時投藥；Ramucirumab 阻斷的是 VEGFR-2 而非 EGFR。因此選項C正確。",
            "flashcard_front": "單株抗體腫瘤治療 / 雙特異性抗體 / Catumaxomab / 傷口癒合延遲",
            "flashcard_back": "Catumaxomab 為雙特異性單抗，同時作用於 EpCAM（腫瘤）與 CD3（T細胞）以導引毒殺作用。",
            "flashcard_summary": "Catumaxomab 機轉 -> 同時結合腫瘤 EpCAM 與 T 細胞 CD3 以發揮療效。"
        },
        {
            "question_id": "110-1_medicine-2_054",
            "question_number": 54,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "抗腫瘤藥物抑制Topoisomerase II的分子機制。",
            "explanation": "Idarubicin 屬於蒽環類抗生素（anthracyclines），其抗癌機轉包含嵌入 DNA 鹼基對中，以及直接抑制 topoisomerase II，導致 DNA 雙股斷裂無法修復進而引發細胞凋亡。Busulfan 和 cyclophosphamide 屬於烷基化劑（alkylating agents），而 methotrexate 為葉酸拮抗劑，主要抑制二氫葉酸還原酶。因此選項C正確。",
            "flashcard_front": "Topoisomerase II 抑制劑 / 蒽環類 / Idarubicin / DNA 斷裂",
            "flashcard_back": "Idarubicin 可藉由嵌入 DNA 並抑制 Topoisomerase II，造成 DNA 斷裂來殺傷癌細胞。",
            "flashcard_summary": "Topoisomerase II 抑制抗癌藥 -> Idarubicin 能抑制 Topoisomerase II 導致 DNA 斷裂。"
        },
        {
            "question_id": "110-1_medicine-2_055",
            "question_number": 55,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "乳癌CMF合併療法之藥物機轉分類。",
            "explanation": "乳癌 CMF 合併化療處方由 Cyclophosphamide、Methotrexate 和 5-Fluorouracil (5-FU) 組成。其中，5-FU 為嘧啶類似物（pyrimidine analog），在體內轉化為活性代謝物 F-dUMP，特異性且不可逆地抑制胸苷酸合成酶（thymidylate synthase），阻斷 DNA 合成。Cytarabine 不在 CMF 處方中。因此選項A正確。",
            "flashcard_front": "乳癌 CMF 療法 / 5-Fluorouracil (5-FU) / 嘧啶類似物 / 胸苷酸合成酶抑制",
            "flashcard_back": "CMF 中的 5-FU 屬於嘧啶類似物，其活性代謝物能抑制 thymidylate synthase，阻斷去氧胸苷酸合成。",
            "flashcard_summary": "CMF 療法中 5-FU -> 為嘧啶類似物，能抑制胸苷酸合成酶。"
        },
        {
            "question_id": "110-1_medicine-2_056",
            "question_number": 56,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "Sumatriptan 治療偏頭痛的作用受體與禁忌症。",
            "explanation": "Sumatriptan 是一種 5-HT1B/1D 受體的選擇性致效劑（agonist），而非拮抗劑，它藉由活化這些受體引起腦血管收縮，並抑制三叉神經傳導物質釋放來緩解偏頭痛。因為該藥會引起冠狀動脈收縮，因此冠狀動脈疾病患者為使用禁忌。與 SSRI 併用會增加血清素症候群風險。因此選項A敘述錯誤。",
            "flashcard_front": "Sumatriptan / 偏頭痛 / 5-HT1B/1D 致效劑 / 冠心病禁忌",
            "flashcard_back": "Sumatriptan 是 5-HT1B/1D 接受器致效劑（而非拮抗劑），藉由收縮腦血管及抑制發炎介質發揮作用。",
            "flashcard_summary": "Sumatriptan 作用機制 -> 為選擇性 5-HT1B/1D 受體致效劑，促使腦血管收縮。"
        },
        {
            "question_id": "110-1_medicine-2_057",
            "question_number": 57,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "Fenofibrate 的降血脂作用機轉與不良反應。",
            "explanation": "Fenofibrate 為纖維酸類衍生物，主要作為 PPAR-α（過氧化體增殖劑活化受體α）的致效劑，能活化並增加脂蛋白脂酶（lipoprotein lipase, LPL）的活性與表達以促進三酸甘油酯水解，而非抑制其活性。主要副作用為橫紋肌溶解症（特別與 statins 合用時）及肝功能異常。因此選項D敘述錯誤。",
            "flashcard_front": "Fenofibrate / PPAR-α 致效劑 / Lipoprotein lipase 活化 / 降三酸甘油酯",
            "flashcard_back": "Fenofibrate 活化 PPAR-α 以活化（而非抑制）lipoprotein lipase，加速三酸甘油酯的清除。",
            "flashcard_summary": "Fenofibrate 機轉 -> 活化 PPAR-α 受體，進而活化脂蛋白脂酶（LPL）活性。"
        },
        {
            "question_id": "110-1_medicine-2_058",
            "question_number": 58,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "紅血球生成素（EPO）的受體訊息傳傳導與臨床作用。",
            "explanation": "官方正解為C。紅血球生成素（EPO）及其類似物 darbepoetin alfa 主要是藉由與紅血球祖細胞表面的 EPO 受體結合，活化胞內的 JAK2/STAT5 訊息傳導途徑，從而促進紅血球的增殖與分化。雖然部分研究指出 EPOR 也能間接活化 Ras/MAPK (ERK) 或 PI3K/Akt，但在經典教科書中主要突出的主導途徑是 JAK/STAT 途徑，故此題官方判定C選項為主要錯誤陳述。其常見副作用為血栓與高血壓。",
            "flashcard_front": "EPO / Darbepoetin / JAK2/STAT5 途徑 / ERK訊息 / 高血壓副作用",
            "flashcard_back": "EPO 受體活化的經典訊號為 JAK2/STAT5 途徑，主要功能是刺激紅血球祖細胞增殖與分化。",
            "flashcard_summary": "EPO 受體訊號 -> 經典訊息傳導途徑主要為 JAK2/STAT5 途徑。"
        },
        {
            "question_id": "110-1_medicine-2_059",
            "question_number": 59,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "Desmopressin 在促進凝血系統中的藥理機制。",
            "explanation": "Desmopressin (DDAVP) 為血管加壓素的合成類似物，主要藉由刺激血管內皮細胞表面的 V2 受體，增加細胞內 cAMP，進而調控並促進儲存於 Weibel-Palade 體內之von vW 因子 (vWF) 以及凝血因子八 (factor VIII) 釋放進入血液，以改善血小板凝聚與凝血功能。它不會增加 cAMP 的分解（因為抑制磷酸二酯酶才是），亦不活化 ADP 受體。選項B正確。",
            "flashcard_front": "Desmopressin (DDAVP) / 凝血作用 / Factor VIII 釋放 / vWF 釋放",
            "flashcard_back": "Desmopressin 活化 V2 受體促使血管內皮細胞釋放 vWF 和 factor VIII，進而加強凝血功能。",
            "flashcard_summary": "Desmopressin 凝血機轉 -> 促進血管內皮細胞釋放 factor VIII 和 vWF。"
        },
        {
            "question_id": "110-1_medicine-2_060",
            "question_number": 60,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "甲狀腺機能亢進的藥物選擇與使用禁忌。",
            "explanation": "李太太呈現典型甲狀腺機能亢進的臨床表現。Propylthiouracil 可抑制甲狀腺素合成並阻斷外周 T4 轉化為 T3；Lugol's solution（高濃度碘）能暫時抑制甲狀腺素釋放；Propranolol 能緩解心悸、手抖等交感神經亢進症狀。相反地，Levothyroxine 是外源性 T4（用以治療甲狀腺功能低下），給予此藥會使甲亢患者的病情惡化，故不適合。選項B正確。",
            "flashcard_front": "甲狀腺亢進 / 治療藥物 / Levothyroxine 禁忌 / PTU",
            "flashcard_back": "Levothyroxine 為甲狀腺素補充劑（用於甲低下），甲亢患者禁用以免病情惡化；PTU 與碘劑可用於治療甲亢。",
            "flashcard_summary": "甲亢用藥禁忌 -> 甲亢患者不適合給予 Levothyroxine（T4補充劑）。"
        },
        {
            "question_id": "110-1_medicine-2_061",
            "question_number": 61,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "第一型糖尿病的首選藥物治療。",
            "explanation": "第一型糖尿病是由於自體免疫破壞胰臟 β 細胞，導致胰島素絕對缺乏。因此，其首選且必須的治療藥物是胰島素（insulin）。口服降血糖藥物如坐格列汀（sitagliptin，DPP-4抑制劑）及格列匹子（glipizide，磺醯尿素類）都需要靠尚存有功能的 β 細胞來刺激胰島素分泌，故不適用於第一型糖尿病患者。選項C正確。",
            "flashcard_front": "第一型糖尿病 / 胰島素絕對缺乏 / 胰島素 (Insulin) / 口服降血糖藥不適用",
            "flashcard_back": "第一型糖尿病因 β 細胞受損造成胰島素絕對缺乏，首選且必須以胰島素（insulin）進行替代治療。",
            "flashcard_summary": "第一型糖尿病治療 -> 首選藥物為胰島素，無法單靠口服降糖藥控制。"
        }
    ]
}

# ==========================================
# BATCH 110-1_medicine-2_batch-005
# ==========================================
batches_data["110-1_medicine-2_batch-005"] = {
    "dataset_id": "110-1_medicine-2",
    "batch_id": "110-1_medicine-2_batch-005",
    "category_group": "醫學（二）",
    "items": [
        {
            "question_id": "110-1_medicine-2_062",
            "question_number": 62,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "糖皮質激素（類固醇）的適應症與消化道副作用禁忌。",
            "explanation": "類固醇/糖皮質激素會藉由抑制前列腺素合成，減少胃黏液與碳酸氫根的分泌，從而削弱胃黏膜屏障，極易誘發或惡化消化性潰瘍（peptic ulcer）並增加穿孔與出血的風險。因此，消化性潰瘍患者不適合使用此類藥物。而愛迪生氏病需使用其做替代療法，氣喘與發炎性腸道疾病則利用其強大的抗發炎活性進行治療。選項C正確。",
            "flashcard_front": "類固醇禁忌 / 消化性潰瘍 / 前列腺素抑制 / 胃黏膜屏障削弱",
            "flashcard_back": "類固醇會抑制前列腺素合成、削弱胃黏膜屏障，故消化性潰瘍患者為其相對禁忌症。",
            "flashcard_summary": "類固醇使用禁忌 -> 類固醇因削弱胃黏膜保護，不適合治療消化性潰瘍。"
        },
        {
            "question_id": "110-1_medicine-2_063",
            "question_number": 63,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "選擇性多巴胺D1受體致效劑在降血壓中的應用。",
            "explanation": "Fenoldopam 是一種選擇性血管多巴胺 D1 受體致效劑（D1-dopamine receptor agonist），能擴張腎血管與周圍小動脈，達到降低血壓與增加腎血流灌注的作用，常用於治療高血壓急症。Clonidine 為 alpha-2 致效劑；diazoxide 活化 K+ 通道；ketanserin 則為 5-HT2 拮抗劑。因此選項C正確。",
            "flashcard_front": "D1 受體致效劑 / Fenoldopam / 腎血管擴張 / 高血壓急症",
            "flashcard_back": "Fenoldopam 為選擇性多巴胺 D1 受體致效劑，可擴張腎血管以快速降壓，適用於高血壓急症。",
            "flashcard_summary": "D1受體致效降壓藥 -> Fenoldopam 為選擇性多巴胺 D1 受體致效劑。"
        },
        {
            "question_id": "110-1_medicine-2_064",
            "question_number": 64,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "碳酸酐酶抑制劑 Acetazolamide 的藥理作用與臨床適應症。",
            "explanation": "Acetazolamide 是一種碳酸酐酶（carbonic anhydrase）抑制劑，作用於近曲小管以抑制碳酸氫鈉重吸收。它能減少眼部睫狀體分泌房水，故臨床上常口服或局部給藥來治療青光眼。此藥主要導致高氯性代謝性酸中毒與低血鉀，非高血鉀，且無耳毒性副作用。因此選項B正確。",
            "flashcard_front": "Acetazolamide / 碳酸酐酶抑制劑 / 青光眼治療 / 近曲小管 / 低血鉀",
            "flashcard_back": "Acetazolamide 作用於近曲小管，藉由抑制碳酸酐酶減少房水產生，可用於治療青光眼與預防高山症。",
            "flashcard_summary": "Acetazolamide 臨床用途 -> 為碳酸酐酶抑制劑，可用於治療青光眼。"
        },
        {
            "question_id": "110-1_medicine-2_065",
            "question_number": 65,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "活化 alpha-1 交感神經受體引起的生理效應。",
            "explanation": "活化 alpha-1 腎上腺素受體會導致平滑肌收縮，包括豎毛肌收縮、骨骼肌中的血管收縮、心肌收縮力增強，以及膀胱括約肌和三角區收縮。然而，膀胱逼尿肌（detrusor muscle）的收縮是由副交感神經的 M3 受體所支配，活化交感神經的 beta-3 反而會使其舒張。因此選項A敘述錯誤。",
            "flashcard_front": "alpha-1 受體 / 生理反應 / 膀胱括約肌收縮 / 逼尿肌支配 / M3 受體",
            "flashcard_back": "活化 alpha-1 受體會收縮血管和尿道括約肌，但膀胱逼尿肌的收縮由副交感 M3 受體控制。",
            "flashcard_summary": "alpha-1 受體生理反應 -> 活化 alpha-1 引起血管/括約肌收縮，但逼尿肌收縮由副交感控制。"
        },
        {
            "question_id": "110-1_medicine-2_066",
            "question_number": 66,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "吸入型抗蕈毒鹼藥物在 COPD 治療中的性質比較。",
            "explanation": "Tiotropium 是一種季銨鹽類抗蕈毒鹼藥物（LAMA），具高度極性不易通過血腦屏障，因此中樞副作用極低。其半衰期長達25小時以上，支持每日一次的吸入給藥來舒張 COPD 患者的氣管。Ipratropium 雖同樣不易通過 BBB，但其半衰期短，需要每日多次給藥。Tropicamide 為短效散瞳劑；Benztropine 主要用於治療巴金森氏症且易進腦部。因此選項C正確。",
            "flashcard_front": "LAMA / COPD 治療 / Tiotropium / 半衰期25小時 / 不過血腦屏障",
            "flashcard_back": "Tiotropium 是長效吸入型抗蕈毒鹼藥，不易通過血腦屏障，半衰期長，適合 COPD 每日一次維持治療。",
            "flashcard_summary": "COPD 吸入抗蕈毒鹼藥 -> Tiotropium 具長半衰期且不易通過血腦屏障，適合 COPD 治療。"
        },
        {
            "question_id": "110-1_medicine-2_067",
            "question_number": 67,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "吸入型氣喘藥物之體內生體可用率與藥理特性。",
            "explanation": "Albuterol（沙丁胺醇）為短效型乙二型交感神經致效劑（SABA），吸入使用時主要作用於肺部，雖有部分會被吞入或經肺部吸收進入體內，但相較於類固醇 flunisolide 與抗膽鹼 tiotropium，在臨床考點中，它是最典型能快速舒張氣管的短效第一線吸入藥物，本題官方給予正解為A。但須注意，實際上吸入型藥物皆有微量全身吸收。",
            "flashcard_front": "短效氣喘藥 / 氣管舒張 / Albuterol / 肺部作用",
            "flashcard_back": "Albuterol 為短效乙二型交感致效劑，吸入後主要作用在肺部以達到快速舒張氣管的效果。",
            "flashcard_summary": "短效氣喘吸入藥 -> Albuterol 為吸入型短效氣管舒張劑。"
        },
        {
            "question_id": "110-1_medicine-2_068",
            "question_number": 68,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "H2 受體拮抗劑之抑制胃酸分泌強度比較。",
            "explanation": "在臨床常用的 H2 受體拮抗劑中，famotidine 的抑制胃酸分泌作用強度（potency）最強，約為 cimetidine 的 20~50 倍，為 ranitidine 和 nizatidine 的 3~20 倍。Cimetidine 的作用強度最弱且具有顯著的抗雄性素副作用與肝臟藥物代謝酶（CYP450）抑制作用。因此選項D正確。",
            "flashcard_front": "H2 拮抗劑 / 作用強度最強 / Famotidine / Cimetidine 副作用",
            "flashcard_back": "Famotidine 是作用強度（potency）最強的 H2 受體阻斷劑，約為 Cimetidine 的20至50倍。",
            "flashcard_summary": "H2受體阻斷劑強度 -> Famotidine 抑制胃酸分泌的作用強度最強。"
        },
        {
            "question_id": "110-1_medicine-2_069",
            "question_number": 69,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "褪黑激素受體致效劑在睡眠障礙中的應用。",
            "explanation": "Tasimelteon 是一種新型的褪黑激素受體致效劑（MT1 與 MT2 agonist），主要被核准用於治療全盲患者之非24小時睡眠覺醒障礙（Non-24-hour sleep-wake disorder）。Sumatriptan 用於治療偏頭痛；Orlistat 抑制脂肪酶用於減重；Repinotan 為 5-HT1A 致效劑。因此選項A正確。",
            "flashcard_front": "MT1/MT2 致效劑 / 睡眠障礙 / Tasimelteon / 非24小時覺醒障礙",
            "flashcard_back": "Tasimelteon 藉由活化 MT1 和 MT2 褪黑激素受體來調節生物鐘，常用於全盲患者的睡眠調解。",
            "flashcard_summary": "褪黑激素致效睡眠藥 -> Tasimelteon 為 MT1 和 MT2 受體致效劑。"
        },
        {
            "question_id": "110-1_medicine-2_070",
            "question_number": 70,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "前列腺素類似物在青光眼治療中的應用。",
            "explanation": "Latanoprost 是一種前列腺素 F2α 類似物（PGF2α analog），能增加葡萄膜鞏膜通道（uveoscleral outflow）的房水排出，是臨床上治療隅角開放性青光眼的首選藥物之一。Alprostadil（PGE1）用於維持動脈導管開啟；misoprostol 用於預防胃潰瘍；dinoprostone（PGE2）用於引產。因此選項B正確。",
            "flashcard_front": "青光眼 / 前列腺素類似物 / Latanoprost / 房水排出 / 葡萄膜鞏膜通道",
            "flashcard_back": "Latanoprost 為 PGF2α 類似物，藉由增加葡萄膜鞏膜通道房水流出量來降低眼壓，治療開放性青光眼。",
            "flashcard_summary": "前列腺素青光眼藥 -> Latanoprost 藉由增加葡萄膜鞏膜通道的房水排出以降低眼壓。"
        },
        {
            "question_id": "110-1_medicine-2_071",
            "question_number": 71,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "慢性高尿酸血症（痛風）的降尿酸藥物治療。",
            "explanation": "Febuxostat 是一種非嘌呤類的黃嘌呤氧化酶抑制劑（xanthine oxidase inhibitor），能藉由抑制尿酸生成來有效治療慢性高尿酸血症。Tramadol 為類鴉片止痛藥，ketorolac 為強效 NSAID 止痛劑，rilonacept 則是 IL-1 抑制劑（主要用於多關節炎或痛風發作期之發炎阻斷）。因此選項D正確。",
            "flashcard_front": "慢性高尿酸血症 / 黃嘌呤氧化酶抑制劑 / Febuxostat / 抑制尿酸生成",
            "flashcard_back": "Febuxostat 藉由特異性抑制黃嘌呤氧化酶（xanthine oxidase），減少尿酸生成，用於慢性高尿酸治療。",
            "flashcard_summary": "慢性降尿酸藥物 -> Febuxostat 藉由抑制黃嘌呤氧化酶減少尿酸生成。"
        },
        {
            "question_id": "110-1_medicine-2_072",
            "question_number": 72,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "抗精神病藥物之錐體外症候群（EPS）副作用風險比較。",
            "explanation": "Haloperidol 屬於第一代典型抗精神病藥物，具極強的 D2 受體拮抗作用，在臨床上引發錐體外症候群（EPS）與泌乳激素升高的副作用最為顯著。而 clozapine、olanzapine 和 aripiprazole 屬於第二代非典型抗精神病藥，D2 親和力較低且合併有 5-HT 拮抗或 D2 部分致效作用，EPS 發生率極低。因此選項A正確。",
            "flashcard_front": "抗精神病藥 / 典型 D2 拮抗 / Haloperidol / 錐體外症候群 (EPS) / 帕金森氏症樣症狀",
            "flashcard_back": "Haloperidol（典型抗精神病藥）強效拮抗多巴胺 D2 受體，極易引發急性張力障礙與靜坐不能等 EPS 副作用。",
            "flashcard_summary": "抗精神病藥與EPS -> Haloperidol 拮抗 D2 受體作用強，易導致顯著的 EPS 副作用。"
        },
        {
            "question_id": "110-1_medicine-2_073",
            "question_number": 73,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "藥物濫用與成癮性、拮抗劑的藥理分類。",
            "explanation": "Naloxone 是一種純類鴉片受體拮抗劑（pure opioid antagonist），能競爭性阻斷 mu、kappa 和 delta 鴉片受體，臨床上作為類鴉片過量的解毒劑，其本身不具任何精神依賴性或濫用潛能。相反地，cocaine（古柯鹼）、psilocybin（裸頭草辛）與 ketamine（K他命）都屬於具濫用傾向且容易造成精神依賴性的管制藥物。因此選項D正確。",
            "flashcard_front": "精神依賴性 / 類鴉片拮抗劑 / Naloxone / 藥物過量解毒 / 無成癮性",
            "flashcard_back": "Naloxone 為純類鴉片拮抗劑，常用於逆轉鴉片類中毒，其本身不具精神依賴性或成癮性。",
            "flashcard_summary": "Naloxone 依賴性特徵 -> 為鴉片受體拮抗劑，不具精神依賴性。"
        },
        {
            "question_id": "110-1_medicine-2_074",
            "question_number": 74,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "非苯二氮平類抗焦慮藥 Buspirone 的作用機制與特徵。",
            "explanation": "Buspirone 是一種 5-HT1A 受體的部分致效劑（partial agonist），主要作用於腦部血清素系統，而非 GABAA 受體，選項B敘述錯誤。它不具有苯二氮平類的抗抽搐、肌肉鬆弛或鎮靜作用，亦不與酒精產生加成效應，但其抗焦慮作用需要連續服用數週後才會顯現。因此選項B為錯誤陳述。",
            "flashcard_front": "Buspirone / 抗焦慮 / 5-HT1A 部分致效劑 / 無肌肉鬆弛 / GABA無關",
            "flashcard_back": "Buspirone 藉由作用於 5-HT1A 血清素受體發揮抗焦慮作用，與 GABAA 受體無直接關係，且不具鎮靜與肌鬆效果。",
            "flashcard_summary": "Buspirone 機轉 -> 為 5-HT1A 部分致效劑，不作用於 GABA 受體。"
        },
        {
            "question_id": "110-1_medicine-2_075",
            "question_number": 75,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "藥理學",
            "category_confidence": "high",
            "key_point": "乙型阻斷劑過量中毒的首選解毒劑。",
            "explanation": "Propranolol（非選擇性β受體阻斷劑）過量會導致嚴重心跳過慢與低血壓。Glucagon（昇糖素）是其最佳解毒劑，因為它能活化心肌上的昇糖素受體，繞過被阻斷的β受體而直接刺激腺苷酸環化酶（adenylyl cyclase），增加心肌內 cAMP，進而恢復心跳與血壓。Atropine 對嚴重阻斷效果有限，digoxin 會加重慢心律。因此選項A正確。",
            "flashcard_front": "Propranolol 過量 / β-blocker 中毒 / 昇糖素 (Glucagon) / 繞過β受體 / 提升 cAMP",
            "flashcard_back": "Glucagon 繞過 β 受體，藉由與昇糖素受體結合來活化腺苷酸環化酶，提升 cAMP 並恢復心跳與血壓。",
            "flashcard_summary": "β受體阻斷劑解毒劑 -> Propranolol 中毒首選解毒劑為 Glucagon。"
        },
        {
            "question_id": "110-1_medicine-2_076",
            "question_number": 76,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "類纖維蛋白性壞死（fibrinoid necrosis）的典型病理關聯。",
            "explanation": "類纖維蛋白性壞死通常與免疫性血管炎（vasculitis）或惡性高血壓有關，其特徵是抗原-抗體複合物及纖維蛋白沉積在血管壁中，顯微鏡下呈現亮粉紅色的無結構物質。結核常表現乾酪性壞死；腦梗塞常表現液化性壞死；急性胰臟炎則常伴隨脂肪壞死。因此選項C正確。",
            "flashcard_front": "類纖維蛋白性壞死 / 血管壁病變 / 血管炎 (vasculitis) / 免疫複合物沉積",
            "flashcard_back": "類纖維蛋白性壞死是由於免疫複合物及纖維蛋白沉積於血管壁所致，常見於各類免疫性血管炎與惡性高血壓。",
            "flashcard_summary": "類纖維蛋白性壞死病因 -> 最常出現在血管炎（vasculitis）的病理切片中。"
        }
    ]
}

# ==========================================
# BATCH 110-1_medicine-2_batch-006
# ==========================================
batches_data["110-1_medicine-2_batch-006"] = {
    "dataset_id": "110-1_medicine-2",
    "batch_id": "110-1_medicine-2_batch-006",
    "category_group": "醫學（二）",
    "items": [
        {
            "question_id": "110-1_medicine-2_077",
            "question_number": 77,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "傷口癒合過程中肉芽組織的組織學特徵。",
            "explanation": "受傷後在增殖期（proliferation phase），由新生的微血管（angiogenesis）、增生的纖維母細胞（fibroblast）以及浸潤的發炎細胞（以巨噬細胞為主）在疏鬆間質中共同組成「肉芽組織」（granulation tissue），為傷口修復的關鍵。肉芽腫（granuloma）是慢性發炎特徵，包含上皮樣組織球；蟹足腫為膠原蛋白過度累積。因此選項B正確。",
            "flashcard_front": "傷口修復 / 纖維母細胞與微血管增生 / 發炎細胞混合 / 肉芽組織",
            "flashcard_back": "肉芽組織（granulation tissue）是新生的微血管、增生纖維母細胞與發炎細胞的混合物，為傷口修復的重要特徵。",
            "flashcard_summary": "肉芽組織組成 -> 為增生的微血管、纖維母細胞及發炎細胞的疏鬆混合組織。"
        },
        {
            "question_id": "110-1_medicine-2_078",
            "question_number": 78,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "全身性紅斑性狼瘡（SLE）的典型病理變化。",
            "explanation": "全身性紅斑性狼瘡（SLE）的血管病變常表現為急性血管炎，病理切片可見血管壁出現類纖維蛋白性壞死（fibrinoid necrosis）與免疫複合物沉積。SLE的腎病變主要是抗原-抗體免疫複合物沉積在腎絲球（非GBM自體抗體），且紅色鐵絲環（wire-loop）是瀰漫性增生型（Class IV，而非膜性Class V）的典型特徵。皮膚病變主要是基底細胞液化退化及真皮表皮交界處免疫沉積。選項B正確。",
            "flashcard_front": "SLE / 血管炎 / 類纖維蛋白性壞死 / 狼瘡腎炎 / wire-loop",
            "flashcard_back": "SLE 的血管典型病變為伴有類纖維蛋白性壞死的急性血管炎；wire-loop lesion 則是 Class IV 增生性狼瘡腎炎的特徵。",
            "flashcard_summary": "SLE 典型血管病變 -> 急性血管炎伴隨血管壁類纖維蛋白性壞死。"
        },
        {
            "question_id": "110-1_medicine-2_079",
            "question_number": 79,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "鏈球菌感染引起的疾病病變譜。",
            "explanation": "鏈球菌屬（Streptococcus）感染臨床上可引發多種疾病。例如，肺炎雙球菌可引起大葉性肺炎；A群鏈球菌可引起猩紅熱、以及免疫反應媒介的急性腎小球腎炎。相反地，壞死性腸炎（necrotizing enterocolitis）多發生於早產兒，病因與腸道屏障受損、局部缺血及腸道混合菌叢（如 Clostridium perfringens）過度繁殖有關，較少由單純鏈球菌感染引起。選項B正確。",
            "flashcard_front": "鏈球菌感染 / 大葉性肺炎 / 猩紅熱 / 壞死性腸炎病因",
            "flashcard_back": "大葉性肺炎、猩紅熱與腎小球腎炎均與鏈球菌感染相關；壞死性腸炎則多與腸壁缺血及厭氧菌（如梭狀芽孢桿菌）繁殖有關。",
            "flashcard_summary": "鏈球菌感染少見病變 -> 壞死性腸炎較少由鏈球菌感染直接引起。"
        },
        {
            "question_id": "110-1_medicine-2_080",
            "question_number": 80,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "黃麴毒素與肝細胞癌發生的基因突變機轉。",
            "explanation": "黃麴毒素 B1（aflatoxin B1）是一種強烈的致癌物，其主要致癌機制是造成肝細胞中抑癌基因 TP53 的第249號密碼子（codon 249）發生 G-to-T 的顛換突變（transversion mutation），導致 p53 蛋白失活，進而引發肝細胞癌。MYC、RAS 屬於致癌基因，RB 則為另一抑癌基因。因此選項D正確。",
            "flashcard_front": "黃麴毒素 B1 / 肝細胞癌 / TP53 突變 / G-to-T 顛換",
            "flashcard_back": "黃麴毒素致癌主因是誘發抑癌基因 TP53 codon 249 產生特異性 G 到 T 突變，導致 p53 蛋白失活。",
            "flashcard_summary": "黃麴毒素致癌靶基因 -> 主要造成抑癌基因 TP53 突變失活。"
        },
        {
            "question_id": "110-1_medicine-2_081",
            "question_number": 81,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "造血系統惡性腫瘤中最常見的染色體核型改變方式。",
            "explanation": "在血液與造血系統的惡性腫瘤中，活化致癌基因最常見的染色體改變是染色體轉位（translocation）。例如慢性骨髓性白血病中的 t(9;22) 形成 BCR-ABL 融合基因，以及伯基特氏淋巴瘤中的 t(8;14) 導致 MYC 過度表現。缺失、基因擴增和非整倍體在實體腫瘤中更常見。因此選項A正確。",
            "flashcard_front": "血液腫瘤 / 染色體核型改變 / 轉位 (Translocation) / 融合基因活化",
            "flashcard_back": "造血系統腫瘤中最常見的致癌基因活化方式為染色體轉位（如 BCR-ABL 或 c-MYC 轉位）。",
            "flashcard_summary": "造血系統腫瘤核型改變 -> 最常見活化致癌基因的方式為染色體轉位（translocation）。"
        },
        {
            "question_id": "110-1_medicine-2_082",
            "question_number": 82,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "乳白色胸水與乳糜胸的病理成因。",
            "explanation": "抽出的胸水呈乳白色混濁樣且含有高濃度的三酸甘油酯，為典型的「乳糜胸」（chylothorax）。這通常是因為胸導管或其分支淋巴管受壓迫、阻塞（如淋巴瘤或轉移癌）或外傷性破裂，導致乳糜液滲漏至胸膜腔所致。心臟衰竭及下腔靜脈阻塞多造成漏出性清澈胸水。因此選項B正確。",
            "flashcard_front": "乳白色胸水 / 三酸甘油酯高 / 乳糜胸 / 淋巴管阻塞 / 胸導管損傷",
            "flashcard_back": "乳白色且富含三酸甘油酯的胸水為乳糜胸，主因是胸導管等淋巴管受壓迫、阻塞或損傷所致。",
            "flashcard_summary": "乳糜胸成因 -> 淋巴管（胸導管）阻塞或受損導致乳糜液漏入胸膜腔。"
        },
        {
            "question_id": "110-1_medicine-2_083",
            "question_number": 83,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "老年退化性二尖瓣鈣化病變特徵。",
            "explanation": "老年退化性二尖瓣鈣化（mitral annular calcification）主要是出現在二尖瓣的「纖維環」（mitral annulus）部位，而非二尖瓣連合處（commissure，此處鈣化粘連是風濕性心臟病的特徵），故選項A敘述錯誤。此病變多數人無症狀且瓣膜功能正常，但會略微增加感染性心內膜炎及血栓形成的風險。因此選項A為錯誤陳述。",
            "flashcard_front": "二尖瓣鈣化 / 退化性病變 / 纖維環鈣化 / 二尖瓣連合處粘連 / 風濕性",
            "flashcard_back": "退化性二尖瓣鈣化好發於二尖瓣「纖維環」；若出現在瓣膜連合處則多為風濕性瓣膜炎的特徵。",
            "flashcard_summary": "二尖瓣退化性鈣化部位 -> 主要發生在二尖瓣纖維環，非連合處。"
        },
        {
            "question_id": "110-1_medicine-2_084",
            "question_number": 84,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "慢性免疫性血小板減少性紫斑症（ITP）的病理學特徵。",
            "explanation": "慢性免疫性血小板減少性紫斑症（ITP）是一種自體免疫疾病，好發於中青年女性。發病機轉主要是病人血漿中產生針對血小板膜蛋白（如 GP IIb/IIIa）的抗體，導致血小板在脾臟中加速被吞噬清除。骨髓切片通常可見巨核細胞顯著增加以代償流失，且多數病人對類固醇治療反應良好。因此選項B正確。",
            "flashcard_front": "慢性 ITP / 自體抗體 / 青年女性 / 巨核細胞增多 / 類固醇反應良好",
            "flashcard_back": "慢性 ITP 是由於自體抗體結合血小板並在脾臟被破壞，骨髓中巨核細胞會代償性增生（非減少）。",
            "flashcard_summary": "慢性 ITP 機轉 -> 血漿中存在抗血小板自體抗體，引發脾臟加速清除血小板。"
        },
        {
            "question_id": "110-1_medicine-2_085",
            "question_number": 85,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "慢性淋巴球性白血病（CLL）的免疫表型與病理診斷。",
            "explanation": "慢性淋巴球性白血病（CLL）是一種 B 淋巴球（而非T細胞）的惡性腫瘤，好發於老年人。其典型腫瘤細胞會特異性且共表現 CD19、CD20 以及通常出現在 T 細胞上的 CD5，且 CD23 亦為陽性，選項C正確。CLL 常有 BCL2 的過度表現（與 microRNA 調控缺陷有關），但 t(14;18) 轉位是濾泡性淋巴瘤的特徵，非 CLL。因此選項C敘述正確。",
            "flashcard_front": "CLL / B細胞腫瘤 / CD5共表現 / CD20與CD23 / 老年人好發",
            "flashcard_back": "CLL 為 B 細胞惡性腫瘤，特異表型為共表現 T 細胞標記 CD5，以及 B 細胞標記 CD20 與 CD23。",
            "flashcard_summary": "CLL 免疫表型 -> 典型表現 B 細胞標記且共表現 CD5 與 CD23。"
        },
        {
            "question_id": "110-1_medicine-2_086",
            "question_number": 86,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "鼻咽癌的組織學分型與臨床特徵比較。",
            "explanation": "鼻咽上皮細胞癌（NPC）分為角化型與非角化型（包含分化與未分化）。其中，角化型鱗狀上皮細胞癌對放射治療的敏感度較差，預後也較非角化型差，選項D正確。病理診斷是利用原位雜交法偵測細胞核內的 EB 病毒 RNA（即 EBER-1），而非 DNA。世界衛生組織分型主要不含分化不良型腺癌。因此選項D正確。",
            "flashcard_front": "鼻咽癌 / 角化型 / 放射治療敏感度 / EBV / EBER-1 原位雜交",
            "flashcard_back": "角化型鼻咽癌對放療反應較非角化型差；診斷主要藉由原位雜交偵測 EBV 的 EBER-1 RNA。",
            "flashcard_summary": "鼻咽癌分型放療反應 -> 角化型鱗狀上皮細胞癌對放射治療的反應較非角化型差。"
        },
        {
            "question_id": "110-1_medicine-2_087",
            "question_number": 87,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "肺氣腫發生中的蛋白酶-抗蛋白酶失衡學說。",
            "explanation": "肺氣腫（emphysema）的發生主要由蛋白酶-抗蛋白酶失衡（protease-antiprotease imbalance）引起。在吸菸等刺激下，肺部的「嗜中性白血球」與肺泡巨噬細胞會大量活化並釋放彈性蛋白酶（elastase）等蛋白分解酶，破壞肺泡壁的彈性纖維，導致肺泡結構永久性擴張。因此選項A正確。",
            "flashcard_front": "肺氣腫 / 彈性纖維破壞 / 彈性蛋白酶 / 嗜中性白血球 / 吸菸刺激",
            "flashcard_back": "破壞肺泡壁彈性纖維的彈性蛋白酶主要來自活化的嗜中性白血球與肺泡巨噬細胞。",
            "flashcard_summary": "肺氣腫蛋白酶來源 -> 破壞肺泡彈性纖維的蛋白酶主要來自嗜中性白血球。"
        },
        {
            "question_id": "110-1_medicine-2_088",
            "question_number": 88,
            "correct_answer": "",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "原發性纖毛運動障礙（PCD）與支氣管擴張的臨床關聯。",
            "explanation": "原發性纖毛運動障礙（PCD，又稱 Kartagener 症候群）因纖毛結構異常導致清除功能喪失，極易引起反覆性呼吸道感染，進而導致「支氣管擴張」（bronchiectasis）。本題官方答案原定為B，但因題目有爭議被官方更正答案為 #（即一律給分），依規定在此將正確答案欄位保留為空字串，以符合原 prompt 的要求。",
            "flashcard_front": "原發性纖毛運動障礙 / 纖毛功能喪失 / 支氣管擴張 / 官方更正答案",
            "flashcard_back": "PCD 因纖毛運動不良引起分泌物滯留，最易造成反覆呼吸道感染與支氣管擴張；此題官方更正為一律給分。",
            "flashcard_summary": "PCD與支氣管疾病 -> 原發性纖毛運動障礙易引起支氣管擴張，本題官方更正一律給分。"
        },
        {
            "question_id": "110-1_medicine-2_089",
            "question_number": 89,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "微生物免疫學",
            "category_confidence": "high",
            "key_point": "各類肝炎病毒的遺傳物質分類。",
            "explanation": "在甲、乙、丙、丁、戊型肝炎病毒中，僅有B型肝炎病毒（HBV）屬於去氧核醣核酸病毒（DNA virus，為雙股部分環狀 DNA 肝病毒科）。而A型、C型、D型和E型肝炎病毒的遺傳物質均為核糖核酸（RNA）。因此選項B正確。",
            "flashcard_front": "肝炎病毒 / DNA病毒 / HBV / RNA病毒",
            "flashcard_back": "僅 B 型肝炎病毒為 DNA 病毒，其他常見肝炎病毒（A、C、D、E型）皆為 RNA 病毒。",
            "flashcard_summary": "DNA肝炎病毒 -> 只有 B 型肝炎病毒（HBV）為去氧核醣核酸（DNA）病毒。"
        },
        {
            "question_id": "110-1_medicine-2_090",
            "question_number": 90,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "偽膜性腸炎的病因、組織病理特徵與診斷方法。",
            "explanation": "偽膜性腸炎通常是由於廣效性抗生素使用破壞腸道菌叢平衡，導致難辨梭菌（Clostridium difficile）過度繁殖並釋放毒素所致，組織學上偽膜是由黏蛋白、壞死細胞與許多嗜中性球組成。然而，臨床診斷主要是檢測糞便中難辨梭菌的毒素 A/B 或 PCR，而非倚賴繁瑣且無法區分產毒與否的細菌培養，故選項D敘述錯誤。",
            "flashcard_front": "偽膜性腸炎 / 難辨梭菌 / 抗生素濫用 / 診斷方法 / 毒素檢測",
            "flashcard_back": "偽膜性腸炎診斷主要靠檢測糞便中的難辨梭菌毒素（Toxin A/B），而非細菌培養。",
            "flashcard_summary": "偽膜性腸炎診斷 -> 主要檢測糞便毒素或行 PCR 診斷，而非進行細菌培養。"
        },
        {
            "question_id": "110-1_medicine-2_091",
            "question_number": 91,
            "correct_answer": "C",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "胃癌分型與幽門螺旋桿菌感染的流行病學與遺傳關聯。",
            "explanation": "Lauren 分型將胃癌分為腸型（intestinal type）與瀰漫型（diffuse type）。腸型胃癌與慢性萎縮性胃炎及幽門螺旋桿菌（H. pylori）感染有極密切的關聯；而瀰漫型胃癌則通常與抑癌基因 CDH1（編碼 E-cadherin）的突變有密切相關，與幽門螺旋桿菌的關聯性反而較低。因此選項C敘述錯誤。",
            "flashcard_front": "胃癌分型 / 腸型胃癌 / 瀰漫型胃癌 / 幽門螺旋桿菌 / CDH1 突變",
            "flashcard_back": "腸型胃癌與幽門螺旋桿菌感染關係密切；瀰漫型胃癌與遺傳基因 CDH1（E-cadherin）突變高度關聯，與幽門桿菌關係較小。",
            "flashcard_summary": "胃癌分型與幽門桿菌 -> 腸型胃癌與幽門螺旋桿菌密切相關，瀰漫型則與 CDH1 突變相關。"
        }
    ]
}

# ==========================================
# BATCH 110-1_medicine-2_batch-007
# ==========================================
batches_data["110-1_medicine-2_batch-007"] = {
    "dataset_id": "110-1_medicine-2",
    "batch_id": "110-1_medicine-2_batch-007",
    "category_group": "醫學（二）",
    "items": [
        {
            "question_id": "110-1_medicine-2_092",
            "question_number": 92,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "外因性皮質醇增多症對腎上腺皮質的病理學影響。",
            "explanation": "外因性皮質醇增多症（Cushing's syndrome，主要由長期服用皮質類固醇引起）會透過負回饋強烈抑制下視丘與垂體分泌 ACTH。缺乏 ACTH 的營養作用會導致雙側腎上腺皮質萎縮（adrenal cortical atrophy），特別是束狀帶和網狀帶。瀰漫性或結節性增生則多見於內因性 ACTH 分泌過多或功能性腺瘤。因此選項A正確。",
            "flashcard_front": "外因性 Cushing / 長期使用類固醇 / 腎上腺病理 / 皮質萎縮 / ACTH 抑制",
            "flashcard_back": "外因性皮質醇過多會回饋抑制 ACTH，導致雙側腎上腺皮質產生退化性萎縮。",
            "flashcard_summary": "外因性庫欣氏症腎上腺 -> 長期外源皮質醇抑制 ACTH 分泌，導致腎上腺皮質萎縮。"
        },
        {
            "question_id": "110-1_medicine-2_093",
            "question_number": 93,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "黃色肉芽腫性腎盂腎炎（XGP）的致病菌關聯。",
            "explanation": "黃色肉芽腫性腎盂腎炎（Xanthogranulomatous pyelonephritis, XGP）是一種罕見的慢性破壞性腎盂腎炎，多伴隨有尿路阻塞及鹿角狀結石。其最常見的致病菌為變形桿菌（Proteus mirabilis）以及大腸桿菌（E. coli）。變形桿菌產生的尿素酶會水解尿素，促進感染性結石形成與慢性發炎。因此選項A正確。",
            "flashcard_front": "黃色肉芽腫性腎盂腎炎 (XGP) / 致病菌 / 變形桿菌 (Proteus) / 鹿角狀結石",
            "flashcard_back": "XGP 最常見致病菌為變形桿菌（Proteus）與大腸桿菌，病變常合併尿路阻塞及鹼性尿結石。",
            "flashcard_summary": "XGP 最常見致病菌 -> 為變形桿菌（Proteus），多伴隨尿路結石與阻塞。"
        },
        {
            "question_id": "110-1_medicine-2_094",
            "question_number": 94,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "甲狀腺髓質癌（MTC）的起源細胞與病理特徵。",
            "explanation": "甲狀腺髓質癌（medullary thyroid carcinoma）起源於甲狀腺濾泡旁 C 細胞（parafollicular C-cells），此細胞主要分泌降鈣素（calcitonin）。在組織病理上，降鈣素多肽前驅物會折疊異常並沉積在腫瘤間質中，形成特徵性的類澱粉沉積（amyloid deposits）。砂樣小體是甲狀腺乳突癌的典型特徵，非髓質癌。因此選項B正確。",
            "flashcard_front": "甲狀腺髓質癌 (MTC) / 降鈣素 / 濾泡旁 C 細胞 / 類澱粉沉積 / 砂樣小體",
            "flashcard_back": "甲狀腺髓質癌源自 C 細胞，分泌降鈣素，其間質病理特徵為有類澱粉沉積（砂樣小體多見於乳突癌）。",
            "flashcard_summary": "甲狀腺髓質癌病理 -> 起源於 C 細胞，腫瘤細胞間常有類澱粉沉積。"
        },
        {
            "question_id": "110-1_medicine-2_095",
            "question_number": 95,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "卵巢性索間質瘤（sex cord stromal tumor）的臨床與基因特徵。",
            "explanation": "成人型顆粒細胞瘤（adult granulosa cell tumor）雖生長緩慢，但其在臨床上屬於具惡性潛能（malignant potential）的腫瘤，可發生晚期局部復發或轉移，而非全然「良性腫瘤」，故選項A較不正確。該瘤常分泌動情激素，引發乳房疾病或子宮內膜增生；支持間質細胞瘤（Sertoli-Leydig cell tumor）多具雄性素功能性且與 DICER1 基因突變高度相關。因此選項A最不正確。",
            "flashcard_front": "卵巢性索間質瘤 / 成人型顆粒細胞瘤 / 惡性潛能 / 動情激素分泌 / 支持間質細胞瘤",
            "flashcard_back": "成人型顆粒細胞瘤具潛在惡性（易晚期復發），非純良性；支持間質細胞瘤常分泌雄性素且常具 DICER1 突變。",
            "flashcard_summary": "成人型顆粒細胞瘤性質 -> 屬於潛在惡性腫瘤，非單純良性腫瘤。"
        },
        {
            "question_id": "110-1_medicine-2_096",
            "question_number": 96,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "睪丸與附睪特殊感染的起始部位與病理傳播。",
            "explanation": "結核病（tuberculosis）和淋病（gonorrhea）引起的尿路生殖系統感染，病原體多是經由逆行性輸精管傳播，因此發炎最先且最常起始於「附睪」（epididymis），隨後才擴展至睪丸。相對地，梅毒（syphilis）感染則是經由血源性傳播，因此發炎病變最先起始於「睪丸」（testis）。因此選項B敘述錯誤。",
            "flashcard_front": "附睪炎與睪丸炎 / 結核病起始 / 梅毒起始 / 逆行性傳播",
            "flashcard_back": "結核與淋病發炎最先起於「附睪」；梅毒發炎最先起於「睪丸」；一般附睪炎比睪丸炎更常見。",
            "flashcard_summary": "睪丸與附睪感染起始 -> 結核病和淋病最先起於附睪，梅毒最先起於睪丸。"
        },
        {
            "question_id": "110-1_medicine-2_097",
            "question_number": 97,
            "correct_answer": "B",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "幼兒期最常見的睪丸生殖細胞腫瘤。",
            "explanation": "卵黃囊瘤（yolk sac tumor，又稱內胚竇瘤 endodermal sinus tumor）是三歲以下嬰幼兒最常見的睪丸原發性生殖細胞腫瘤，臨床上常伴隨有血清甲型胎兒蛋白（AFP）的顯著升高。精細胞瘤好發於中青年，胚胎癌與絨毛癌則較多見於二、三十歲的成年男性。因此選項B正確。",
            "flashcard_front": "嬰幼兒睪丸腫瘤 / 三歲以下 / 卵黃囊瘤 / AFP 升高 / Schiller-Duval 體",
            "flashcard_back": "三歲以下小孩最常見的睪丸生殖細胞瘤為卵黃囊瘤，常伴有 AFP 升高，病理可見 Schiller-Duval body。",
            "flashcard_summary": "三歲以下小孩常見睪丸瘤 -> 最常見為卵黃囊瘤（yolk sac tumor）。"
        },
        {
            "question_id": "110-1_medicine-2_098",
            "question_number": 98,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "骨肉瘤的遺傳變異與病理學診斷特徵。",
            "explanation": "大多數的 low-grade osteosarcoma（低惡性度骨肉瘤）是因第12對染色體之 12q13-q15 擴增，導致 MDM2 與 CDK4 蛋白過度表現（而非 MYC，MYC 位於第8對染色體），故選項A敘述錯誤。原發性骨肉瘤好發於青少年，Li-Fraumeni 症候群（TP53 突變）增加其風險，且確診必須在切片中觀察到惡性基質細胞能直接產生類骨組織（osteoid）。因此選項A為錯誤陳述。",
            "flashcard_front": "骨肉瘤 / MDM2 與 CDK4 擴增 / 12q13-q15 / Li-Fraumeni / 類骨組織",
            "flashcard_back": "低惡性度骨肉瘤以 12q13-q15 擴增（導致 MDM2/CDK4 過度表現，非 MYC）為特徵；診斷需見惡性細胞產生類骨質。",
            "flashcard_summary": "骨肉瘤遺傳變異 -> 低惡性度骨肉瘤伴隨 12q13-q15 擴增導致 MDM2 和 CDK4（而非 MYC）過度表現。"
        },
        {
            "question_id": "110-1_medicine-2_099",
            "question_number": 99,
            "correct_answer": "A",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "阿茲海默症（Alzheimer's disease）的核心病理變化。",
            "explanation": "阿茲海默症患者大腦最具特徵性的兩大主要病理變化為：(1) 由 Aβ 澱粉樣蛋白沉積形成於細胞外的老年斑/神經斑（neuritic plaque），以及(2) 由過度磷酸化的 tau 蛋白聚集在細胞內所形成的神經纖維糾結（neurofibrillary tangle）。Nemaline rods 常見於先天性肌肉病變，Lewy bodies 則為帕金森氏症的病理特徵。因此選項A正確。",
            "flashcard_front": "阿茲海默症 / 兩大病理特徵 / 老年斑 / 神經纖維糾結 / tau 蛋白",
            "flashcard_back": "阿茲海默症的主要病理變化為細胞外的 neuritic plaques（Aβ沉積）與細胞內的 neurofibrillary tangles（tau磷酸化）。",
            "flashcard_summary": "阿茲海默症主要病理 -> 大腦主要病理變化為神經斑（neuritic plaque）與神經纖維糾結（neurofibrillary tangle）。"
        },
        {
            "question_id": "110-1_medicine-2_100",
            "question_number": 100,
            "correct_answer": "D",
            "category_group": "醫學（二）",
            "category": "病理學",
            "category_confidence": "high",
            "key_point": "第一型單純疱疹病毒腦炎（HSV-1）的組織病理特徵。",
            "explanation": "HSV-1 腦炎主要侵犯大腦顳葉，病理特徵為嚴重的壞死性與出血性腦炎，可見嗜酸性核內包涵體（Cowdry A）、血管周圍淋巴球袖套現象（perivascular cuffing）以及小膠質細胞結節（microglial nodules）。而乾酪性壞死性肉芽腫（caseous necrotizing granuloma）是結核菌感染或真菌感染的典型病理特徵，不會在 HSV-1 腦炎中被觀察到。因此選項D正確。",
            "flashcard_front": "HSV-1 腦炎 / 顳葉壞死 / Cowdry A 包涵體 / 乾酪性肉芽腫 / 血管周圍袖套",
            "flashcard_back": "HSV-1 腦炎顯示壞死性出血性腦病變，有 Cowdry A 胞內包涵體，不出現結核特有的乾酪性肉芽腫。",
            "flashcard_summary": "HSV-1 腦炎病理 -> HSV-1 腦炎可見 Cowdry A 包涵體，但不包含乾酪性壞死性肉芽腫。"
        }
    ]
}

# ==========================================
# BATCH 110-1_medicine-3_batch-001
# ==========================================
batches_data["110-1_medicine-3_batch-001"] = {
    "dataset_id": "110-1_medicine-3",
    "batch_id": "110-1_medicine-3_batch-001",
    "category_group": "醫學（三）",
    "items": [
        {
            "question_id": "110-1_medicine-3_001",
            "question_number": 1,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "機械性小腸梗阻的臨床診斷與內科治療原則。",
            "explanation": "本病患有陣發性絞痛、嘔吐、停止排便排氣，伴有高亢腸音，且有腹部手術史，臨床呈現典型機械性小腸梗阻（SBO）。小腸梗阻患者的血清澱粉酶（amylase）通常正常或僅輕微上升，若異常上升10倍以上應高度懷疑急性胰臟炎，而非單純腸梗阻，故選項B錯誤。多數黏連性腸阻塞可先放置鼻胃管引流及靜脈輸液，採取保守治療。因此選項B為錯誤陳述。",
            "flashcard_front": "小腸阻塞 / 陣發性絞痛 / 澱粉酶上升 / 腸音高亢 / 鼻胃管引流",
            "flashcard_back": "小腸梗阻的澱粉酶不應上升10倍以上（此多見於急性胰臟炎）；治療多先採鼻胃管及輸液等保守療法。",
            "flashcard_summary": "小腸梗阻與澱粉酶 -> 小腸阻塞澱粉酶不會大幅上升10倍，此病多先採鼻胃管保守治療。"
        },
        {
            "question_id": "110-1_medicine-3_002",
            "question_number": 2,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "家庭醫學科",
            "category_confidence": "high",
            "key_point": "Linda Fried 團隊定義之老年衰弱（frailty）臨床指標。",
            "explanation": "Linda Fried 提出的衰弱表型（frailty phenotype）包含五項具體臨床指標：非刻意性體重減輕（weight loss）、手握力不足（weakness）、疲憊感（exhaustion）、行動遲緩/走路速度變慢（slowness）以及低體能活動量（low physical activity）。該定義主要是生理學衰弱指標，並不包含「認知功能不佳」。因此選項A正確。",
            "flashcard_front": "老年衰弱 / Fried 臨床定義 / 五項指標 / 生理衰弱 / 認知功能",
            "flashcard_back": "Fried 老年衰弱定義包括：體重減輕、握力不足、疲憊、行動遲緩及低活動量，不包含認知功能。",
            "flashcard_summary": "Fried 衰弱定義 -> 包含體重減輕、握力差、疲憊、行動慢及低活動，不含認知障礙。"
        },
        {
            "question_id": "110-1_medicine-3_003",
            "question_number": 3,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "家庭醫學科",
            "category_confidence": "high",
            "key_point": "意外性體溫偏低（hypothermia）的臨床危險因子。",
            "explanation": "體溫偏低（指核心溫度 < 35°C）的危險因子包括：年齡極端（嬰幼兒及老年人，因體溫調節能力弱）、甲狀腺功能低下（基礎代謝率降）、休克（外周灌注差導致散熱多產熱少）及營養不良等。相較之下，30至50歲的健康成年人體溫調節機制健全，並非體溫偏低的危險因子。因此選項B正確。",
            "flashcard_front": "體溫偏低 / 核心溫度 / 年齡極端 /  hypothyroidism / 危險因子",
            "flashcard_back": "體溫偏低危險因子包含老年、嬰幼兒、甲腺功能低下、休克與營養不良；中青年健康成年人非危險群。",
            "flashcard_summary": "體溫偏低危險因子 -> 中青年成年人非危險群，極端年齡與甲腺低下才是危險因子。"
        },
        {
            "question_id": "110-1_medicine-3_004",
            "question_number": 4,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "家庭醫學科",
            "category_confidence": "high",
            "key_point": "降血脂藥物的適應症與副作用比較。",
            "explanation": "纖維酸類藥物（fibric acid derivatives，如 fenofibrate）會增加膽汁中膽固醇的排泄並降低膽汁酸濃度，這會增加膽汁的飽和度，反而可能「增加」膽結石的生成機率，故選項A敘述錯誤。Statin 類主要副作用包括肌肉酸痛與肝指數上升；菸鹼酸（nicotinic acid）能有效提升 HDL-C；Omega-3 能促進 TG 的分解。因此選項A為錯誤陳述。",
            "flashcard_front": "降血脂藥 / 纖維酸類 (Fibrates) / 膽結石增加 / statin 肌痛 / 菸鹼酸",
            "flashcard_back": "Fibrates 類藥物會增加膽汁中膽固醇排泄，增加膽結石風險（非減少）；statin 類常見肌肉痠痛副作用。",
            "flashcard_summary": "纖維酸類與膽結石 -> Fibrates 類藥物會增加而非減少膽結石的生成風險。"
        },
        {
            "question_id": "110-1_medicine-3_005",
            "question_number": 5,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "腎臟移植後伺機性感染的時間點特徵。",
            "explanation": "腎臟移植後伺機性感染的發生具有明顯時間規律。在移植後第一個月內，主要是手術相關感染以及潛在疱疹病毒（Herpesvirus，如 HSV-1、HSV-2）的復發。其他病原體如真菌（Aspergillus）、諾卡氏菌（Nocardia）或巨細胞病毒（CMV），以及慢性肝炎惡化，多數在移植後 1 至 6 個月免疫抑制最强的時期才出現。因此選項A正確。",
            "flashcard_front": "腎移植 / 伺機性感染 / 移植後一個月內 / 疱疹病毒 (Herpesvirus) / 晚期感染",
            "flashcard_back": "移植後一個月內常發生的伺機性感染為 HSV 等疱疹病毒復發；黴菌及 Nocardia 多在一個月後（中期）出現。",
            "flashcard_summary": "腎移植早期感染 -> 移植後一個月內最常見的伺機性感染是 Herpesvirus 復發。"
        },
        {
            "question_id": "110-1_medicine-3_006",
            "question_number": 6,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "急性心包填塞的 Beck's triad 診斷要件。",
            "explanation": "急性心包填塞（pericardial tamponade）的 Beck's triad 是由三個經典臨床表徵組成：低血壓（hypotension）、頸靜脈怒張（jugular venous distention，反應體靜脈回流受阻）以及心音低沉/遙遠（muffled heart sounds）。Kussmaul's sign（吸氣時頸靜脈壓上升）則多見於縮窄性心包炎。因此選項C正確。",
            "flashcard_front": "心包填塞 / Beck's triad / 低血壓 / 頸靜脈怒張 / 心音低沉",
            "flashcard_back": "Beck's triad 指心包填塞的三大表徵：低血壓、頸靜脈怒張與心音低沉遙遠。",
            "flashcard_summary": "Beck's triad 組成 -> 急性心包填塞三大特徵為低血壓、頸靜脈怒張及心音低沉。"
        },
        {
            "question_id": "110-1_medicine-3_007",
            "question_number": 7,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "胸腔內科",
            "category_confidence": "high",
            "key_point": "次發性肺動脈高壓（PAH）的病因分類與排除。",
            "explanation": "次發性肺動脈高壓（PAH）可由多種慢性疾病引發，如肝硬化合併門脈高壓（Portopulmonary hypertension）、結締組織疾病（硬皮症直接侵犯肺微血管）以及 COPD（慢性缺氧引起肺血管收縮及重塑）。而心包膜填塞（pericardial tamponade）引發的是急性心輸出量驟降與心因性休克，並非導致次發性肺高壓的病因。因此選項B除外。",
            "flashcard_front": "次發性肺高壓 / 病因分類 / 肝硬化門脈高壓 / COPD / 心包膜填塞除外",
            "flashcard_back": "結締組織病、COPD及肝硬化門脈高壓皆可引起次發性肺高壓；心包填塞引起急性休克而非肺高壓。",
            "flashcard_summary": "次發性肺高壓病因 -> 心包膜填塞非次發性肺高壓之誘發病因。"
        },
        {
            "question_id": "110-1_medicine-3_008",
            "question_number": 8,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "先天性主動脈狹縮（coarctation of aorta）的臨床及影像特徵。",
            "explanation": "先天性主動脈狹縮常合併雙葉型主動脈瓣（bicuspid aortic valve），並因狹窄處導致下肢血壓明顯低於上肢。胸部 X 光檢查可见肋骨凹痕（rib notching），但這是因為側支循環的肋間動脈在「肋骨下緣」的肋溝中壓迫所致，而非第3-9肋骨的「上緣」，故選項D敘述錯誤。在兩側肩胛骨間區域常可聽到雜音。因此選項D為錯誤陳述。",
            "flashcard_front": "主動脈狹縮 / 下肢血壓低 / 雙葉型瓣膜 / 肋骨凹痕 (notching) / 肋骨下緣",
            "flashcard_back": "主動脈狹窄在胸部 X 光呈現肋骨「下緣」凹痕（側支肋間動脈壓迫所致），常合併下肢血壓低於上肢。",
            "flashcard_summary": "主動脈狹縮 X 光表徵 -> 肋骨凹痕（rib notching）是發生在肋骨下緣而非上緣。"
        },
        {
            "question_id": "110-1_medicine-3_009",
            "question_number": 9,
            "correct_answer": "D",
            "constants": [],
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "慢性收縮性心力衰竭的藥物指引與生存益處。",
            "explanation": "慢性 HFrEF（LVEF < 35%）的第一線治療指引建議使用 ACEi/ARB（或ARNI）、β-阻斷劑及醛固酮拮抗劑（aldactone），這些藥物即使在沒有水腫症狀時也能改善預後並降低死亡率。口服硝酸鹽與肼屈嗪（hydralazine）的血管擴張劑組合僅保留於對上述藥物不耐受或特定非裔美國人，並非「優先選用」的組合。因此選項D錯誤。",
            "flashcard_front": "心衰竭藥物 / LVEF < 35% / 第一線指引 / 血管擴張劑組合 / 生存益處",
            "flashcard_back": "HFrEF 首選藥為 ACEi/ARB 及 β-blocker 以改善存活率；nitrates+hydralazine 僅為無法耐受首選藥時的備選方案。",
            "flashcard_summary": "心衰竭首選藥物 -> 首選為 ACEi/ARB 與 β-blocker，硝酸鹽與 hydralazine 組合非優先選用。"
        },
        {
            "question_id": "110-1_medicine-3_010",
            "question_number": 10,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "房室傳導阻滯（AV block）的誘因與病因學。",
            "explanation": "頸動脈竇超敏感可引發強烈的迷走神經反射；急性下壁心肌梗塞常累及房室結血管；高血鉀會降低心肌傳導性，此三者皆容易造成房室傳導阻滯（AV block）。相反地，甲狀腺機能亢進（hyperthyroidism）主要會增加交感神經活性，臨床上常引起竇性心搏過速、心房顫動等，較少造成房室阻滯。因此選項C較不會造成房室阻滯。",
            "flashcard_front": "房室阻滯 (AV block) / 誘因病因 / 迷走神經反射 / 下壁心梗 / 甲亢心搏過速",
            "flashcard_back": "下壁心梗、高血鉀及頸動脈竇敏感易造成房室傳導阻滯；甲亢則常引發心房顫動與心搏過速。",
            "flashcard_summary": "房室傳導阻滯病因 -> 甲狀腺機能亢進通常引起心搏過速，較不會引起房室傳導阻滯。"
        },
        {
            "question_id": "110-1_medicine-3_011",
            "question_number": 11,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "急診醫學科",
            "category_confidence": "high",
            "key_point": "心導管術後拔除股動脈鞘引發血管迷走神經反射的處置。",
            "explanation": "拔除股動脈鞘時，病人因疼痛或緊張刺激迷走神經，會引發迷走反射（vasovagal reflex），表現為血壓大幅下降（低血壓）和心跳極慢（心動過緩）。此時最立即且恰當的處理為靜脈注射阿托品（Atropine，以阻斷迷走神經作用）並同時給予大量快速靜脈輸液（fluid challenge）以提升血壓。升壓劑 dopamine 等非首選。因此選項B正確。",
            "flashcard_front": "拔除股動脈鞘 / 傷口劇痛 / 臉色蒼白 / 低血壓合併心跳慢 / 血管迷走反射",
            "flashcard_back": "拔鞘時低血壓伴隨心跳過慢（迷走神經反射），首選立即處置為靜脈注射 Atropine 與快速輸液。",
            "flashcard_summary": "血管迷走反射處理 -> 拔除血管鞘引發低血壓與慢心跳時，首選 Atropine 及快速輸液。"
        },
        {
            "question_id": "110-1_medicine-3_012",
            "question_number": 12,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "心臟內科",
            "category_confidence": "high",
            "key_point": "經皮冠狀動脈介入術（PCI）與外科繞道手術在冠心病治療的成效比較。",
            "explanation": "對於穩定型心絞痛（stable angina）患者，當代經皮冠狀動脈介入術（PCI）與積極藥物治療相比，雖然能更有效緩解心絞痛症狀並改善生活品質，但大型臨床試驗（如 COURAGE、ISCHEMIA 試驗）已證實 PCI 並不能減少心肌梗塞的發生率或降低死亡率，故選項A敘述錯誤。藥物塗藥支架能降狹窄率；複雜多支血管病變的糖尿病人以 CABG 預後較佳。因此選項A為錯誤陳述。",
            "flashcard_front": "穩定型心絞痛 / PCI 成效 / 藥物治療比較 / 死亡率與心梗風險",
            "flashcard_back": "PCI 治療穩定型心絞痛能改善症狀，但相較於純藥物治療，並不能降低總死亡率與心肌梗塞發生率。",
            "flashcard_summary": "PCI 與藥物治療成效 -> PCI 對穩定心絞痛可改善症狀，但無法降低心梗或死亡率。"
        },
        {
            "question_id": "110-1_medicine-3_013",
            "question_number": 13,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "急診醫學科",
            "category_confidence": "high",
            "key_point": "急性 ST 段上升型心肌梗塞（STEMI）的急診啟動流程。",
            "explanation": "心電圖若明確顯示急性 ST 段上升型心肌梗塞（STEMI），急診的首要原則是爭取時間重建心肌血流（Door-to-Balloon < 90分鐘），應立即聯絡心臟科醫師並啟動緊急心導管流程，不可為了等待抽血心肌酶報告而延誤治療，故選項B正確。若能在黃金時間內進行 PCI，其療效與安全性顯著優於全身藥物溶栓治療。因此選項B為正確處置。",
            "flashcard_front": "急診心電圖 / ST段上升 / STEMI 處置 / 心肌酶等待 / Door-to-Balloon",
            "flashcard_back": "STEMI 的急診首要處置是立即啟動心導管室流程，切忌因等待抽血心肌酶結果而延遲介入治療。",
            "flashcard_summary": "STEMI 急診處置 -> 發現 ST 段上升梗塞，應立即啟動緊急心導管流程，不等待抽血報告。"
        },
        {
            "question_id": "110-1_medicine-3_014",
            "question_number": 14,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "排便習慣改變與大腸直腸症狀的病因鑑別。",
            "explanation": "常有大便大不乾淨的感覺（裡急後重，tenesmus）是直腸刺激的特徵，常見於潰瘍性結腸炎、痔瘡、或是腸躁症（IBS），並非「即表示」直腸附近一定長了腫瘤，故選項B敘述過於絕對與錯誤。對於29歲青年，病史詢問應留意體重變化與家族史；夜間腹瀉與排便不一定完全排除器質性病變但需要列入考慮。因此選項B最不正確。",
            "flashcard_front": "大便解不乾淨 / 裡急後重 / 直腸腫瘤 / 腸躁症 (IBS) / 鑑別診斷",
            "flashcard_back": "裡急後重感起因於直腸受刺激（如痔瘡或腸躁症），不能單憑此症狀即斷定患有直腸腫瘤。",
            "flashcard_summary": "裡急後重與腫瘤 -> 大便解不乾淨感為直腸刺激症狀，非直腸腫瘤之特異指徵。"
        },
        {
            "question_id": "110-1_medicine-3_015",
            "question_number": 15,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "Billroth II 重建術後併發輸入袢症候群（afferent loop syndrome）。",
            "explanation": "病患曾接受 Billroth II 胃次全切除術，呈現餐後腹痛、嘔吐（常含膽汁）等症狀。化驗顯示大細胞性貧血（MCV 106）與營養不良（Alb 3.1）。這是典型的輸入袢症候群（afferent loop syndrome）。因輸入袢部分阻塞導致膽汁排空受阻，引起餐後痛與嘔吐，且腸道鹼性液滯留導致細菌過度增生，競爭消耗維生素 B12，進而引起巨紅血球性貧血。因此選項C為最可能的診斷。",
            "flashcard_front": "Billroth II 術後 / 餐後腹痛嘔吐 / 巨紅血球性貧血 / 維生素 B12 缺乏 / 細菌過度增生",
            "flashcard_back": "Billroth II 後輸入袢阻塞（輸入袢症候群）會造成餐後膽汁性嘔吐，並因細菌過度增生干擾 B12 吸收導致大細胞貧血。",
            "flashcard_summary": "輸入袢症候群特徵 -> Billroth II 術後因輸入袢阻塞引發嘔吐，並因細菌增生消耗 B12 導致巨紅血球貧血。"
        }
    ]
}

# ==========================================
# BATCH 110-1_medicine-3_batch-002
# ==========================================
batches_data["110-1_medicine-3_batch-002"] = {
    "dataset_id": "110-1_medicine-3",
    "batch_id": "110-1_medicine-3_batch-002",
    "category_group": "醫學（三）",
    "items": [
        {
            "question_id": "110-1_medicine-3_016",
            "question_number": 16,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "肝硬化急性食道靜脈瘤出血的急症處置原則。",
            "explanation": "患者為酒精性肝硬化且有食道靜脈瘤出血史，呈現低血壓、心搏過速與意識不清。此時首要步驟是暢通呼吸道並給予氣管插管（4）以防吸入性肺炎，以及建立大口徑周邊靜脈或中心靜脈導管（1）進行快速輸液與輸血。非選擇性 β 阻斷劑（2）是預防出血用藥，在急性大出血且血壓低時為使用禁忌。大腸鏡（3）對上消化道出血無診斷價值。因此選項D（僅14）為正確處置。",
            "flashcard_front": "肝硬化吐血 / 意識不清 / 低血壓 / β-blocker 禁忌 / 急救處置",
            "flashcard_back": "急性靜脈瘤大出血且血壓低時，禁用 β-blocker；急救應立即建立靜脈通道補液，並行氣管插管保護呼吸道。",
            "flashcard_summary": "食道靜脈瘤急性出血 -> 處置為建立靜脈通路及氣管插管防吸入肺炎，此時禁用 β 阻斷劑。"
        },
        {
            "question_id": "110-1_medicine-3_017",
            "question_number": 17,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "胃食道逆流疾病（GERD）的典型臨床表現。",
            "explanation": "患者呈現正中胸骨下燒灼感（俗稱火燒心，heartburn）與胸骨下微痛，且症狀在平躺睡覺時因失去重力阻礙酸液而加劇，甚至因酸液刺激喉部或吸入氣管而引發夜間咳嗽。這符合胃食道逆流疾病（GERD）的典型臨床表現。下壁心肌梗塞主要為壓迫性悶痛；心衰竭雖可能平躺喘（Orthopnea）但少有胸骨後燒灼感。因此選項C正確。",
            "flashcard_front": "胸骨下燒灼感 / 平躺症狀加劇 / 夜間咳嗽 / 火燒心 / 體位相關",
            "flashcard_back": "火燒心且平躺時症狀惡化並伴隨咳嗽，是胃食道逆流（GERD）的典型特徵。",
            "flashcard_summary": "胃食道逆流症狀 -> 典型表現為胸骨後燒灼感、平躺加重以及胃酸刺激引起的咳嗽。"
        },
        {
            "question_id": "110-1_medicine-3_018",
            "question_number": 18,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "黃疸與肝膽疾病的鑑別診斷步驟。",
            "explanation": "病患有黃疸且直接膽紅素（direct bilirubin: 5.8）顯著佔比升高，ALT 148，此為典型的肝細胞性或膽汁淤積性黃疸。網狀紅血球計數（reticulocyte count）是用於診斷溶血性貧血（溶血會導致間接/非結合膽紅素升高），在此情況下對診斷沒有幫助。相反地，鹼性磷酸酶（ALP）、B型肝炎表面抗原及腹部超音波，對於區分肝內或肝外膽管阻塞非常有幫助。因此選項A正確。",
            "flashcard_front": "直接膽紅素高 / 黃疸 / 網狀紅血球計數 / 膽管超音波 / 溶血鑑別",
            "flashcard_back": "直接膽紅素升高提示肝膽病變，網狀紅血球計數僅對溶血（間接膽紅素高）診斷有幫助。",
            "flashcard_summary": "直接膽紅素高與網狀紅血球 -> 網狀紅血球計數用於診斷溶血（間接膽紅素高），對直接膽紅素升高黃疸無診斷價值。"
        },
        {
            "question_id": "110-1_medicine-3_019",
            "question_number": 19,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "原發性膽汁性膽管炎（PBC）與自體免疫肝炎的臨床診斷。",
            "explanation": "年輕女性、發癢、皮膚變黑、直接膽紅素與 ALP（312，正常<100）顯著升高，且超音波未見膽管擴張，應高度懷疑原發性膽汁性膽管炎（PBC）或自體免疫性肝炎。檢測抗線粒體抗體（AMA，PBC的特異抗體）、抗核抗體（ANA）以及 HBsAg 都有助於病因診斷。檢測 A 型肝炎 IgG 抗體（anti-HAV IgG）僅代表過去感染或接種過疫苗，無法協助診斷此慢性肝膽病變。因此選項B正確。",
            "flashcard_front": "皮膚癢與變黑 / ALP 顯著升高 / AMA / 自體免疫肝病 / PBC / HAV-IgG",
            "flashcard_back": "高 ALP 與瘙癢提示膽汁淤積（如 PBC），檢測自體抗體（AMA、ANA）有助診斷，而 HAV-IgG 僅代表過去 HAV 暴露，無診斷價值。",
            "flashcard_summary": "PBC 與自體抗體 -> 膽汁淤積懷疑 PBC 時需驗 AMA 與 ANA；HAV IgG 僅代表過去免疫，無助於診斷。"
        },
        {
            "question_id": "110-1_medicine-3_020",
            "question_number": 20,
            "correct_answer": "B",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "幽門螺旋桿菌感染的相關上消化道疾病譜。",
            "explanation": "幽門螺旋桿菌（H. pylori）感染是消化性潰瘍、胃腺癌以及胃 MALT 淋巴瘤的明確致病因子，清除此菌能降低上述疾病的風險。然而，幽門螺旋桿菌感染並非胃食道逆流疾病（GERD）的病因，部分研究甚至顯示根除幽門螺旋桿菌後，因胃酸分泌恢復，胃食道逆流症狀反而可能加重。因此選項B正確。",
            "flashcard_front": "幽門螺旋桿菌 / 相關疾病 / 胃 MALT 淋巴瘤 / 胃腺癌 / 胃食道逆流無關",
            "flashcard_back": "H. pylori 與消化性潰瘍、胃癌及 MALT 淋巴瘤密切相關；它不是胃食道逆流（GERD）的病因。",
            "flashcard_summary": "幽門螺旋桿菌疾病關聯 -> H. pylori 引起潰瘍與胃癌，但與胃食道逆流無致病關聯。"
        },
        {
            "question_id": "110-1_medicine-3_021",
            "question_number": 21,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "急性膽管炎之 Charcot's triad 臨床三大表徵。",
            "explanation": "急性膽管炎（acute cholangitis）的經典臨床診斷條件 Charcot's triad 包括：(1) 右上腹或上腹部疼痛、(2) 發冷發熱、以及 (3) 黃疸。右上腹可觸及脹大且無痛的膽囊是 Courvoisier's sign，常見於胰臟頭部癌症或膽總管下端腫瘤壓迫，並非急性膽管炎 Charcot's triad 的組成條件。因此選項A正確。",
            "flashcard_front": "膽管炎 / Charcot's triad / 右上腹痛 / 發燒 / 黃疸 / Courvoisier's sign",
            "flashcard_back": "Charcot's triad 為腹痛、發燒及黃疸，提示急性膽管炎；可觸及之無痛膽囊為 Courvoisier's sign。",
            "flashcard_summary": "Charcot's triad 組成 -> 急性膽管炎三大條件為右上腹痛、發冷發熱與黃疸。"
        },
        {
            "question_id": "110-1_medicine-3_022",
            "question_number": 22,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "早期肝細胞癌（HCC）的首選根治性治療方法。",
            "explanation": "對於早期肝細胞癌（TNM 第一期或 BCLC 0/A 期）且無肝功能失代償的患者，首選的根治性治療是外科手術切除（surgical resection）或局部無線射頻燒灼術（RFA）。經動脈栓塞化學治療（TACE）主要用於無法手術的中期患者，而標靶與化療則多用於晚期轉移患者。因此選項C是較好的首選治療。",
            "flashcard_front": "早期肝癌 / BCLC 0或A期 / 根治性治療 / 手術切除 / 射頻燒灼術 (RFA)",
            "flashcard_back": "早期肝癌且肝功能佳時，首選開刀手術切除或 RFA 以達根治；TACE 用於中期，標靶用於晚期。",
            "flashcard_summary": "早期肝癌首選治療 -> 優先選擇手術切除或無線射頻燒灼術（RFA）等根治性療法。"
        },
        {
            "question_id": "110-1_medicine-3_023",
            "question_number": 23,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "肝膽腸胃科",
            "category_confidence": "high",
            "key_point": "大腸憩室症的診斷、預防與危險因子。",
            "explanation": "大腸憩室炎多數可以內科保守治療（如抗生素），僅少數併發穿孔或膿瘍者需手術。診斷首選為腹部電腦斷層（CT），X光平片診斷價值低。吸菸是憩室炎的危險因子。臨床研究顯示，口服 5-ASA 類抗發炎藥物如 mesalazine 能減少症狀性非複雜性憩室疾病的復發率。因此選項C正確。",
            "flashcard_front": "大腸憩室炎 / 電腦斷層首選 / 內科保守治療 / Mesalazine 預防復發 / 吸菸危險因子",
            "flashcard_back": "憩室炎診斷以 CT 為首選；Mesalazine 可用於減少症狀性憩室炎的復發率；多數病人不需手術治療。",
            "flashcard_summary": "憩室疾病治療預防 -> 5-ASA類抗發炎藥物如 Mesalazine 能降低症狀性憩室疾病的復發率。"
        },
        {
            "question_id": "110-1_medicine-3_024",
            "question_number": 24,
            "correct_answer": "A",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "正常陰離子間隙代謝性酸中毒的鑑別診斷指標。",
            "explanation": "正常陰離子間隙代謝性酸中毒（NAGMA）的兩大主因為腎外性HCO3丟失（如腹瀉）與腎性排酸障礙（如腎小管酸血症 RTA）。尿陰離子間隙（Urine Anion Gap, UAG = Na + K - Cl）是最具診斷價值的鑑別指標。腹瀉時腎臟排銨功能正常，UAG為負值；而 RTA 患者因腎臟排銨受損，UAG為正值。因此選項A正確。",
            "flashcard_front": "正常陰離子隙酸中毒 / 腹瀉 / RTA / 尿陰離子間隙 (UAG) / 銨離子排泄",
            "flashcard_back": "鑑別 NAGMA 病因首選 UAG（Na+K-Cl）；腹瀉時 UAG 為負值，RTA 時因排銨障礙 UAG 為正值。",
            "flashcard_summary": "UAG 鑑別酸中毒 -> NAGMA 時，利用尿陰離子間隙（UAG）區分腹瀉（負值）與 RTA（正值）。"
        },
        {
            "question_id": "110-1_medicine-3_025",
            "question_number": 25,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "高陰離子隙代謝性酸中毒（HAGMA）的病因鑑別。",
            "explanation": "病患血液檢查陰離子隙（Anion Gap, AG） = Na - Cl - HCO3 = 138 - 99 - 10 = 29 mEq/L，大於正常值（>12），屬於高陰離子隙代謝性酸中毒（HAGMA）。乳酸酸血症、酮酸血症與尿毒症（慢性腎衰竭）都是典型的 HAGMA 病因。而急性腹瀉造成的碳酸氫根流失，會引起正常陰離子隙代謝性酸中毒（NAGMA）。因此急性腹瀉最不可能為此病人的單獨診斷，選項C正確。",
            "flashcard_front": "高陰離子隙酸中毒 (HAGMA) / Anion Gap 計算 / 急性腹瀉 (NAGMA) / 乳酸與酮酸",
            "flashcard_back": "病患 AG 為 29（顯著升高），屬於 HAGMA，病因包括乳酸/酮酸/腎衰竭；急性腹瀉引發的是正常 AG 的 NAGMA。",
            "flashcard_summary": "陰離子隙計算與診斷 -> 計算 AG 為29提示 HAGMA，急性腹瀉（NAGMA）最不可能為此診斷。"
        },
        {
            "question_id": "110-1_medicine-3_026",
            "question_number": 26,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "急性腎損傷（AKI）併發重症透析指引與血漿置換術之排除。",
            "explanation": "病患有嚴重肺炎並引發急性腎損傷（AKI，Creatinine 由 1.1 急升至 8.5），並伴有嚴重高血鉀（6.5）與酸中毒，此為緊急透析指徵。血液透析（B）、連續性靜脈血液過濾（A，適合血流動力不穩者）甚至腹膜透析（D）均可作為清除鉀離子與水分之腎臟替代療法。而血漿置換術（plasmapheresis）主要用於清除大分子自體抗體（如 TTP 或 anti-GBM），對處理 AKI 的高血鉀及酸中毒無實質療效，故最不適合。選項C正確。",
            "flashcard_front": "急性腎損傷 / 高血鉀與酸中毒 / 緊急透析指徵 / 血漿置換術不適用",
            "flashcard_back": "嚴重 AKI 合併高血鉀需行腎替代治療（血液透析/CVVH）；血漿置換術是用於清除抗體，不適用於治療 AKI 尿毒與鉀高。",
            "flashcard_summary": "AKI 治療選擇 -> 高血鉀與尿毒症需以透析治療，血漿置換術不適用於此急性處置。"
        },
        {
            "question_id": "110-1_medicine-3_027",
            "question_number": 27,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "草酸鈣尿路結石的預防與飲食指引。",
            "explanation": "草酸鈣結石患者若過度限制飲食中的鈣質攝取，會導致腸道內無法與草酸結合的游離草酸增加，使腸道吸收過多草酸，隨後經尿液排出形成高草酸尿症，反而「增加」草酸鈣結石的復發風險，故減少鈣攝取無法預防復發（選項D正確）。多喝水、限鹽以及使用 thiazide 利尿劑（能減少尿鈣排出）均為有效的預防措施。因此選項D正確。",
            "flashcard_front": "草酸鈣結石 / 預防復發 / 限制飲食鈣 (禁忌) / 腸道草酸吸收增加 / thiazide 利尿劑",
            "flashcard_back": "限制飲食鈣會增加腸道吸收草酸，導致高草酸尿進而加重結石；thiazide 和多喝水能預防復發。",
            "flashcard_summary": "結石預防飲食 -> 限制飲食鈣質攝取反而增加結石風險，不可藉此預防結石復發。"
        },
        {
            "question_id": "110-1_medicine-3_028",
            "question_number": 28,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "腎因性全身纖維化（NSF）的病因與預防原則。",
            "explanation": "腎因性全身纖維化（Nephrogenic systemic fibrosis, NSF）與嚴重腎功能不全患者使用含釓（gadolinium）造影劑密切相關。血液透析（hemodialysis）其實能有效清除血清中的釓造影劑（一次透析可清除約 70%），故選項D稱「無法清除」是錯誤的。CKD 第3期患者（GFR 30~59）NSF 風險低，但仍應小心或減量使用；肝臟疾病也是 NSF 的危險因子。因此選項D為錯誤陳述。",
            "flashcard_front": "NSF / 含釓造影劑 (gadolinium) / 嚴重腎衰竭 / 血液透析清除 / 預防措施",
            "flashcard_back": "NSF 與含釓造影劑相關，血液透析能有效清除體內殘留的釓造影劑（非無法清除）。",
            "flashcard_summary": "NSF與血液透析 -> 血液透析能有效清除釓（gadolinium）造影劑，非無法清除。"
        },
        {
            "question_id": "110-1_medicine-3_029",
            "question_number": 29,
            "correct_answer": "D",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "急性腎損傷（AKI）的輸液管理與禁用液體。",
            "explanation": "急性腎損傷目前以支持性治療為主。在預防顯影劑腎病或改善低血容時，可使用等張生理食鹽水補液；高血鉀時應停用 ACEi/ARB 以免鉀離子更形升高。然而，羥乙基澱粉溶液（hydroxyethyl starch, HES，一種人工膠體溶液）已被證實會增加重症患者發生急性腎損傷及需要透析的風險，甚至增加死亡率，故在 AKI 及低血容患者中為使用禁忌。選項D敘述錯誤。",
            "flashcard_front": "急性腎損傷 / 輸液選擇 / 羥乙基澱粉 (HES) / 腎毒性禁忌 / ACEi 停用",
            "flashcard_back": "羥乙基澱粉溶液（HES）具腎毒性，會增加 AKI 患者的透析與死亡風險，臨床禁用於改善低血容。",
            "flashcard_summary": "AKI 輸液禁忌 -> 羥乙基澱粉（HES）會增加 AKI 與透析風險，不適合用於補液。"
        },
        {
            "question_id": "110-1_medicine-3_030",
            "question_number": 30,
            "correct_answer": "C",
            "category_group": "醫學（三）",
            "category": "腎臟科",
            "category_confidence": "high",
            "key_point": "老年人背痛合併腎病症候群的鑑別診斷。",
            "explanation": "病患為63歲年長女性，主訴背痛半年且服用 NSAID（diclofenac），現呈現腎病症候群（尿蛋白/肌酸酐比值高達4.907克/克，伴隨低白蛋白血症 3.0 與水腫）。雖然 NSAID 可引起微小病變或膜性腎病，但年長者背痛合併腎病症候群，必須高度懷疑多發性骨髓瘤（Multiple Myeloma）或自體免疫澱粉樣變性，檢測血清蛋白電泳及免疫電泳（immunoelectrophoresis）對於篩檢單株免疫球蛋白（M-protein）極具診斷價值。PLA2R 主要用於診斷原發性膜性腎病。因此選項C為最正確的下一步敘述。",
            "flashcard_front": "背痛合併腎病 / 老年女性 / NSAID 使用 / 免疫電泳 / 多發性骨髓瘤排除",
            "flashcard_back": "老年背痛伴隨大量蛋白尿，必須驗血清免疫電泳以排除多發性骨髓瘤或澱粉樣變性引起的腎病變。",
            "flashcard_summary": "背痛伴腎病診斷 -> 老年背痛合併腎病症候群，檢測血清蛋白及免疫電泳有助診斷病因。"
        }
    ]
}

# ==========================================
# WRITE AND VALIDATE BATCHES
# ==========================================
import sys

def validate_data(b_id, data):
    # Get prompt data
    prompt_path = f"reports/gemini_prompts/{b_id}.md"
    if not os.path.exists(prompt_path):
        return f"Prompt file {prompt_path} does not exist"
        
    with open(prompt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find JSON input
    input_pos = content.find("請處理以下 JSON 輸入：")
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
    prompt_data = json.loads(json_str)
    
    # Check outermost fields
    if data.get('dataset_id') != prompt_data.get('dataset_id'):
        return f"Mismatch dataset_id: expected {prompt_data.get('dataset_id')}, got {data.get('dataset_id')}"
    if data.get('batch_id') != prompt_data.get('batch_id'):
        return f"Mismatch batch_id: expected {prompt_data.get('batch_id')}, got {data.get('batch_id')}"
        
    items = data.get('items', [])
    prompt_qs = prompt_data.get('questions', [])
    
    if len(items) != len(prompt_qs):
        return f"Count mismatch: prompt has {len(prompt_qs)}, got {len(items)}"
        
    allowed_categories = prompt_data.get('allowed_categories', [])
    
    for i, item in enumerate(items):
        pq = prompt_qs[i]
        
        # Check matching question fields
        if item.get('question_id') != pq.get('question_id'):
            return f"Mismatch question_id at index {i}: expected {pq.get('question_id')}, got {item.get('question_id')}"
        if item.get('question_number') != pq.get('question_number'):
            return f"Mismatch question_number at index {i}: expected {pq.get('question_number')}, got {item.get('question_number')}"
        if item.get('correct_answer') != pq.get('correct_answer'):
            return f"Mismatch correct_answer for {pq.get('question_id')}: expected '{pq.get('correct_answer')}', got '{item.get('correct_answer')}'"
        if item.get('category_group') != prompt_data.get('category_group'):
            return f"Mismatch category_group for {pq.get('question_id')}: expected {prompt_data.get('category_group')}, got {item.get('category_group')}"
            
        # Check schema fields
        required_fields = ['question_id', 'question_number', 'correct_answer', 'category_group', 'category', 'category_confidence', 'key_point', 'explanation', 'flashcard_front', 'flashcard_back', 'flashcard_summary']
        for field in required_fields:
            if field not in item:
                return f"Missing required field {field} in {pq.get('question_id')}"
                
        # Check category
        cat = item.get('category')
        if cat not in allowed_categories:
            return f"Category '{cat}' for {pq.get('question_id')} is not in allowed list: {allowed_categories}"
            
        # Check category confidence
        conf = item.get('category_confidence')
        if conf not in ['high', 'medium', 'low']:
            return f"Invalid category_confidence '{conf}' for {pq.get('question_id')}"
            
        # Check explanation length (2 to 5 sentences)
        exp = item.get('explanation')
        sentence_count = exp.count('。') + exp.count('？') + exp.count('！')
        if sentence_count < 2 or sentence_count > 5:
            print(f"Warning: {pq.get('question_id')} explanation has {sentence_count} sentences: '{exp}'")
            
        # Check flashcard summary format (關鍵字 / 線索 -> 知識點 / 判斷規則)
        sum_str = item.get('flashcard_summary')
        if ' -> ' not in sum_str:
            return f"flashcard_summary for {pq.get('question_id')} does not contain ' -> ' separator: '{sum_str}'"
            
    return "OK"

# Write out each batch and validate
all_ok = True
for b_id, data in batches_data.items():
    output_path = f"reports/gemini_outputs/{b_id}.json"
    
    # Validate first
    res = validate_data(b_id, data)
    print(f"Validation for {b_id}: {res}")
    if res != "OK":
        all_ok = False
        continue
        
    # Write RAW JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {output_path}")

if not all_ok:
    print("Some files failed validation!")
    sys.exit(1)
else:
    print("All files processed and validated successfully!")
    sys.exit(0)
