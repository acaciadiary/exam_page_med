# -*- coding: utf-8 -*-
import json
import os
import sys

# Define all batch data
batches_data = {}

# ==================== BATCH 002 ====================
batches_data["110-1_medicine-2_batch-002"] = {
  "dataset_id": "110-1_medicine-2",
  "batch_id": "110-1_medicine-2_batch-002",
  "items": [
    {
      "question_id": "110-1_medicine-2_016",
      "question_number": 16,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "真菌菌絲依隔膜存在與否分為隔菌絲與多核體菌絲。",
      "explanation": "真菌的菌絲依據是否有隔膜分割，基本形態分為有隔膜的隔菌絲(septate hyphae)以及無隔膜、多核相通的多核體菌絲(coenocytic hyphae)。假菌絲(pseudohyphae)為酵母菌出芽後未脫離所形成的鏈狀結構，並非基本菌絲形態；發芽管與鎖狀連接則屬於特定的生長或連接結構。",
      "flashcard_front": "真菌菌絲 / 基本形態分類 / 有無隔膜",
      "flashcard_back": "真菌菌絲之基本形態分為有隔膜的隔菌絲與無隔膜的多核體菌絲。",
      "flashcard_summary": "真菌菌絲基本形態 -> 分為有隔膜的隔菌絲與無隔膜的多核體（無隔）菌絲。"
    },
    {
      "question_id": "110-1_medicine-2_017",
      "question_number": 17,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "目前預防百日咳疫苗的主要組成成分。",
      "explanation": "現行常規預防百日咳的疫苗主要是無細胞百日咳疫苗（acellular vaccine, aP），常與白喉、破傷風類毒素結合為三合一疫苗（DTaP）接種。傳統全細胞疫苗因副作用較高已較少使用；脂多醣體與莢膜多醣體皆非現行百日咳疫苗的主要抗原成分。",
      "flashcard_front": "百日咳桿菌疫苗 / 疫苗組成 / DTaP",
      "flashcard_back": "現行百日咳疫苗以無細胞疫苗(acellular vaccine)為主，副作用較全細胞疫苗少。",
      "flashcard_summary": "百日咳疫苗組成 -> 主要組成為無細胞疫苗(acellular vaccine)，常以DTaP形式接種。"
    },
    {
      "question_id": "110-1_medicine-2_018",
      "question_number": 18,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "流行性感冒病毒感染中CD8 T細胞的活化與毒殺機制。",
      "explanation": "在病毒感染過程中，CD8+ 毒殺性T細胞（CTL）是藉由其TCR特異性辨識靶細胞上的MHC-I呈獻抗原，並釋放穿孔素與顆粒酶來殺死被感染細胞，而非藉由抗體依賴性細胞毒殺作用（ADCC）發揮作用，故選項(C)敘述錯誤。干擾素、NK細胞的早期毒殺與B細胞分化分泌中和抗體均為流感感染時的正確免疫反應。",
      "flashcard_front": "流感病毒感染 / CD8 T細胞毒殺機制 / 抗體依賴性細胞毒殺 (ADCC)",
      "flashcard_back": "CD8+ T細胞主要透過MHC-I辨識並直接毒殺靶細胞，而ADCC主要由NK細胞或吞噬細胞執行。",
      "flashcard_summary": "CD8 T細胞毒殺機制 -> CD8+ T細胞直接透過MHC-I辨識靶細胞，不以ADCC為主要機制。"
    },
    {
      "question_id": "110-1_medicine-2_019",
      "question_number": 19,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "CD59對補體系統膜攻擊複合物（MAC）形成的抑制機制。",
      "explanation": "CD59（又稱protectin）是細胞膜上的補體調控蛋白，能結合已裝配的C5b-8複合物，直接阻斷C9的聚合與插入，從而抑制膜攻擊複合物（MAC）的形成。DAF (CD55)與MCP (CD46)作用於C3/C5轉化酶階段；C1 inhibitor則抑制古典路徑C1的活化，皆非直接干擾C9聚合。",
      "flashcard_front": "補體調控蛋白 / 抑制C9聚合 / 膜攻擊複合物 (MAC) 抑制",
      "flashcard_back": "CD59（protectin）能直接結合C5b-8並阻止C9聚合，抑制MAC形成。",
      "flashcard_summary": "CD59與補體抑制 -> CD59直接阻斷C9聚合以抑制膜攻擊複合物(MAC)的形成。"
    },
    {
      "question_id": "110-1_medicine-2_020",
      "question_number": 20,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "專業性抗原呈獻細胞呈獻抗原給CD4 T細胞之分子標記。",
      "explanation": "CD4+ T細胞（輔助型T細胞）主要透過其TCR辨識與主要組織相容性複合體第二型（MHC class II）結合的外源性抗原。專業性抗原呈獻細胞（APC）如樹突細胞、巨噬細胞及B細胞，因能大量表現MHC class II分子，故能執行此抗原呈獻功能。MHC class I主要呈獻給CD8+ T細胞，MHC class III則不參與抗原呈獻。",
      "flashcard_front": "專業性抗原呈獻細胞 (APC) / CD4 T細胞辨識 / 主要組織相容性複合物",
      "flashcard_back": "專業性APC透過大量表現MHC class II分子，將外源性抗原呈獻給CD4+ T細胞。",
      "flashcard_summary": "APC與CD4 T細胞呈獻 -> 專業性APC利用MHC class II分子呈獻抗原給CD4+ T細胞。"
    },
    {
      "question_id": "110-1_medicine-2_021",
      "question_number": 21,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "抗體類別轉換的特性與免疫檢點療法之受體表現位置。",
      "explanation": "本題將第21題與第22題合併。第21題問抗體多樣性何者錯誤，正解為(D)，因為抗體類別轉換（isotype switching）僅改變重鏈恆定區，不影響結合抗原的變異區，故不貢獻抗體多樣性。而第22題問免疫與腫瘤交互作用何者錯誤，選項中(B)提及腫瘤細胞表現CTLA-4是錯誤的，因為CTLA-4主要表現於T細胞表面而非腫瘤細胞。",
      "flashcard_front": "抗體類別轉換 (isotype switching) / 變異區與恆定區 / CTLA-4表現細胞",
      "flashcard_back": "抗體類別轉換僅改變重鏈恆定區而不改變特異性；CTLA-4主要表現於T細胞表面而非腫瘤細胞。",
      "flashcard_summary": "類別轉換與CTLA-4定位 -> 類別轉換不改變結合區；CTLA-4表現在T細胞而非腫瘤細胞。"
    },
    {
      "question_id": "110-1_medicine-2_023",
      "question_number": 23,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "不同抗體亞型與Fc受體的親和力差異。",
      "explanation": "不同亞型（subclasses）的抗體雖然可以結合相同的Fc受體，但其親和力（affinity）通常有顯著的差異，例如IgG1與IgG3對FcγR的結合力明顯高於IgG2與IgG4，故(B)選項錯誤。Fc受體可以單體或多亞基複合體形式存在；自由狀態的抗體與受體結合為正常生理過程；抗體與補體雙重調理可顯著增強吞噬細胞的吞噬作用。",
      "flashcard_front": "抗體亞型 / Fc受體 (Fc receptor) / 結合親和力",
      "flashcard_back": "不同抗體亞型與同一種Fc受體的結合親和力有顯著不同，並非完全一樣。",
      "flashcard_summary": "抗體亞型與Fc受體親和力 -> 不同亞型抗體與同一Fc受體的結合親和力有顯著差異。"
    },
    {
      "question_id": "110-1_medicine-2_024",
      "question_number": 24,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "黏膜組織中針對食物抗原產生的主要抗體類型。",
      "explanation": "黏膜組織（如腸道黏膜）中主要的免疫球蛋白為分泌型IgA (sIgA)，它在黏膜表面扮演局部防禦與對食物抗原（如小麥麩質蛋白）產生免疫耐受的重要角色。IgG主要存在於血清中，IgM為初次免疫反應產生的抗體，IgD主要作為未成熟B細胞的膜受體。",
      "flashcard_front": "黏膜組織 / 食物抗原 (如麩質) / 主要抗體種類",
      "flashcard_back": "黏膜組織接觸食物抗原時所產生的抗體主要為分泌型 IgA。",
      "flashcard_summary": "黏膜抗原與IgA -> 黏膜組織針對食物抗原所產生的主要抗體種類為IgA。"
    },
    {
      "question_id": "110-1_medicine-2_025",
      "question_number": 25,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "結核桿菌抑制吞噬體與溶酶體融合之免疫逃脫機制。",
      "explanation": "結核桿菌（Mycobacterium tuberculosis）被巨噬細胞吞噬後，主要藉由其細胞壁成分（如硫脂質）來抑制吞噬體（phagosome）與溶酶體（lysosome）的融合，從而在巨噬細胞內得以長期存活與繁殖。抗原漂變與基因轉換主要見於病毒與錐蟲等，而非結核桿菌的主要逃脫方式。",
      "flashcard_front": "結核桿菌 / 胞內寄生 / 免疫逃脫機制 / 吞噬體與溶酶體",
      "flashcard_back": "結核桿菌藉由抑制吞噬體與溶酶體的融合，在巨噬細胞內存活以逃避清除。",
      "flashcard_summary": "結核桿菌逃脫機制 -> 結核桿菌主要透過抑制吞噬體與溶酶體融合而在胞內存活。"
    },
    {
      "question_id": "110-1_medicine-2_026",
      "question_number": 26,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "腫瘤免疫編輯（tumor immunoediting）之定義與階段結果。",
      "explanation": "腫瘤免疫編輯（tumor immunoediting）是指免疫系統塑造腫瘤免疫原性的過程，包含清除、平衡與逃脫三階段。在「逃脫」階段，由於免疫系統篩選的結果，腫瘤會產生突變、抗原流失或改變細胞特性以逃避毒殺，最終導致腫瘤持續生長，而非導致其縮小，故(D)選項錯誤。",
      "flashcard_front": "腫瘤免疫編輯 (immunoediting) / 免疫監測壓力 / 腫瘤生長變化",
      "flashcard_back": "腫瘤免疫編輯的逃脫階段會導致腫瘤逃避防禦並持續生長，而非縮小。",
      "flashcard_summary": "腫瘤免疫編輯結果 -> 免疫編輯的逃脫階段會篩選出抗原流失的腫瘤細胞並導致腫瘤生長。"
    },
    {
      "question_id": "110-1_medicine-2_027",
      "question_number": 27,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "腎臟移植超急性排斥之致病原因。",
      "explanation": "移植後數分鐘至數小時內發生的超急性排斥（hyperacute rejection），主因是受體體內已預先存在對抗供體血管內皮抗原（如ABO血型或HLA抗原）的抗體。這些預存抗體激活補體系統，迅速引發血栓與血管壞死。而MHC錯配所誘導的T細胞介導急性排斥通常需數天到數週才會顯現。",
      "flashcard_front": "腎臟移植 / 10分鐘內排斥 / 超急性排斥 / 免疫機制",
      "flashcard_back": "移植後數分鐘發生的超急性排斥是因受體體內已存有對抗移植物的預存抗體。",
      "flashcard_summary": "超急性移植排斥 -> 移植後數分鐘內發生排斥主要源於受體體內預先存在的自體抗體。"
    },
    {
      "question_id": "110-1_medicine-2_028",
      "question_number": 28,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "單株抗體藥物 Rituximab 的治療靶點與剔除細胞。",
      "explanation": "Rituximab 是一種針對 CD20 的嵌合型單株抗體。CD20 主要表現於前 B 細胞至成熟 B 細胞 the 表面（但不表現於漿細胞），因此 Rituximab 主要藉由補體介導的毒殺與 ADCC 機制來剔除 B 細胞。CD4/CD8 T 細胞及樹突細胞表面均不表現 CD20，故不受其影響。",
      "flashcard_front": "Rituximab / CD20單株抗體 / 剔除之免疫細胞",
      "flashcard_back": "Rituximab 針對成熟 B 細胞表面的 CD20 分子，主要用於剔除 B 細胞。",
      "flashcard_summary": "Rituximab靶點 -> Rituximab 為抗 CD20 單株抗體，主要用於剔除 B 細胞。"
    },
    {
      "question_id": "110-1_medicine-2_029",
      "question_number": 29,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "寄生蟲學",
      "category_confidence": "high",
      "key_point": "菲律賓毛線蟲感染引發的蛋白質流失與電解質失衡。",
      "explanation": "菲律賓毛線蟲（Capillaria philippinensis）主要因食入未煮熟的淡水魚而感染。蟲體在小腸大量繁殖會嚴重破壞腸黏膜，導致蛋白質流失性腸病變，臨床上呈現嚴重的低蛋白血症、低血鉀及低血鈣等電解質失衡症狀。海獸胃線蟲主要侵犯胃部引起急性劇痛；旋毛蟲常侵犯肌肉；有棘頜口線蟲以幼蟲移行症為主。",
      "flashcard_front": "吃生魚片 / 嚴重電解質失衡 / 低蛋白血症 / 小腸寄生蟲",
      "flashcard_back": "菲律賓毛線蟲感染會破壞腸黏膜，引發嚴重的蛋白質與電解質流失。",
      "flashcard_summary": "菲律賓毛線蟲症狀 -> 菲律賓毛線蟲寄生於小腸，造成嚴重的低蛋白血症與電解質失衡。"
    },
    {
      "question_id": "110-1_medicine-2_030",
      "question_number": 30,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "寄生蟲學",
      "category_confidence": "high",
      "key_point": "廣東住血線蟲的傳播途徑與診斷方法。",
      "explanation": "廣東住血線蟲（Angiostrongylus cantonensis）的第三期感染性幼蟲可污染生菜，因此食入未洗淨的生菜沙拉仍可能感染，故(C)選項錯誤。此蟲感染人體會引起嗜酸性腦膜炎，病患腦脊髓液中嗜酸性白血球會異常增多，確診方法通常是在腦脊髓液中發現幼蟲或成蟲。",
      "flashcard_front": "廣東住血線蟲 / 傳播途徑 / 腦脊髓液 / 嗜酸性白血球",
      "flashcard_back": "廣東住血線蟲可經由受幼蟲污染的生菜沙拉傳播；感染會引發嗜伊紅性腦膜炎。",
      "flashcard_summary": "廣東住血線蟲傳播與診斷 -> 廣東住血線蟲可經生菜傳播，引發嗜伊紅性腦膜炎並可在CSF中驗出蟲體。"
    },
    {
      "question_id": "110-1_medicine-2_031",
      "question_number": 31,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "寄生蟲學",
      "category_confidence": "high",
      "key_point": "顆粒性包生絛蟲的感染源、病灶特徵與診斷限制。",
      "explanation": "人類感染顆粒性包生絛蟲（Echinococcus granulosus）是因誤食被犬糞污染的「蟲卵」而非羊肉，且人類作為中間/迷入宿主，糞便中不會排出蟲卵，故(A)(D)錯誤。幼蟲在人體肝臟（最常見）會形成包生囊（hydatid cyst，單房性），病灶切面呈現多空腔的肺泡狀囊（alveolar cyst）是多房性包生絛蟲（E. multilocularis）的特徵，故(C)錯誤、(B)正確。",
      "flashcard_front": "顆粒性包生絛蟲 / 包生囊 (hydatid cyst) / 肝臟病灶 / 感染源",
      "flashcard_back": "顆粒性包生絛蟲在人體肝臟形成單房性包生囊；人類是食入犬糞中蟲卵而感染。",
      "flashcard_summary": "顆粒性包生絛蟲特徵 -> 顆粒性包生絛蟲在肝臟形成包生囊，經食入蟲卵感染，人糞中無蟲卵。"
    }
  ]
}

# ==================== BATCH 003 ====================
batches_data["110-1_medicine-2_batch-003"] = {
  "dataset_id": "110-1_medicine-2",
  "batch_id": "110-1_medicine-2_batch-003",
  "items": [
    {
      "question_id": "110-1_medicine-2_032",
      "question_number": 32,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "寄生蟲學",
      "category_confidence": "high",
      "key_point": "分辨吸蟲在人類腦部造成異位病變的可能性。",
      "explanation": "薑片蟲（Fasciolopsis buski）為小腸寄生蟲，成蟲僅附著於小腸黏膜，不發生體內移行，故最不可能在人類腦部造成異位病變。日本血吸蟲蟲卵可隨血流栓塞至腦部；衛氏肺吸蟲有移行至腦部引起病變的傾向；異形異形吸蟲的極小蟲卵亦常隨血流移行至腦部、心臟等處造成病變。",
      "flashcard_front": "吸蟲感染 / 腦部異位病變 / 薑片蟲 / 日本血吸蟲 / 衛氏肺吸蟲",
      "flashcard_back": "薑片蟲僅寄生於小腸且不移行，不會造成腦部病變；日本血吸蟲、衛氏肺吸蟲等可造成腦部病變。",
      "flashcard_summary": "腦部異位病變吸蟲 -> 薑片蟲不侵犯腦部，而日本血吸蟲、衛氏肺吸蟲等則可能造成腦部病變。"
    },
    {
      "question_id": "110-1_medicine-2_033",
      "question_number": 33,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "寄生蟲學",
      "category_confidence": "high",
      "key_point": "瘧疾嚴重併發症之免疫與病理機制。",
      "explanation": "黑水熱（blackwater fever）是惡性瘧的嚴重併發症，與自體免疫機制高度相關，因患者體內產生針對受感染與未受感染紅血球的自身抗體，導致嚴重的急性血管內溶血與血紅素尿。三日瘧引起的腎絲球腎炎是免疫複合物沉積而非原蟲直接沉積；熱帶脾腫大主要與B細胞多株活化及IgM大量增生有關。",
      "flashcard_front": "瘧疾併發症 / 黑水熱 (blackwater fever) / 腎絲球腎炎 / 熱帶脾腫大",
      "flashcard_back": "黑水熱與自體免疫溶血相關，造成紅血球破裂與黑尿；三日瘧腎病變則由免疫複合物沉積引起。",
      "flashcard_summary": "瘧疾併發症機制 -> 黑水熱與自體免疫溶血相關，三日瘧腎病變為抗原-抗體複合物沉積所致。"
    },
    {
      "question_id": "110-1_medicine-2_034",
      "question_number": 34,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "寄生蟲學",
      "category_confidence": "high",
      "key_point": "跳蚤作為傳播絛蟲之中間宿主。",
      "explanation": "犬複殖器絛蟲（Dipylidium caninum，又稱瓜實絛蟲）以貓蚤或狗蚤為中間宿主。當人類（尤其是兒童）與寵物親密接觸並誤食含有擬囊尾幼蟲的跳蚤時便會遭到感染。犬蛔蟲與犬鉤蟲主要經土傳蟲卵或經皮感染，菲律賓毛線蟲則因食入未煮熟淡水魚而感染。",
      "flashcard_front": "誤食貓狗蚤 / 擬囊尾幼蟲 / 犬複殖器絛蟲 / 傳播媒介",
      "flashcard_back": "誤食含擬囊尾幼蟲的貓狗蚤，主要會感染犬複殖器絛蟲(Dipylidium caninum)。",
      "flashcard_summary": "跳蚤傳播寄生蟲 -> 誤食貓狗蚤最可能感染犬複殖器絛蟲。"
    },
    {
      "question_id": "110-1_medicine-2_035",
      "question_number": 35,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "寄生蟲學",
      "category_confidence": "high",
      "key_point": "采采蠅傳播非洲睡病之病原體。",
      "explanation": "岡比亞錐蟲（Trypanosoma brucei gambiense）為非洲睡病的病原體，主要藉由采采蠅（tsetse fly）叮咬傳播。利什曼原蟲由白蛉（sandfly）傳播；枯西氏錐蟲（美洲錐蟲病病原）主要由錐鼻蟲（triatomine bug）的糞便污染傷口傳播。",
      "flashcard_front": "采采蠅 (tsetse fly) / 叮咬傳播 / 岡比亞錐蟲 / 非洲睡病",
      "flashcard_back": "采采蠅是岡比亞錐蟲（非洲睡病）的傳播媒介；利什曼原蟲與美洲錐蟲則非由其傳播。",
      "flashcard_summary": "采采蠅與岡比亞錐蟲 -> 采采蠅叮咬主要傳播岡比亞錐蟲，引發非洲睡病。"
    },
    {
      "question_id": "110-1_medicine-2_036",
      "question_number": 36,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "病例對照研究相較於佇列研究的缺點。",
      "explanation": "病例對照研究（case-control study）為回溯性設計，在選擇病例與對照時極易產生選擇性偏差（selection bias），且容易有回憶偏差。相比之下，佇列研究需要更長的時間與更多樣本數；病例對照研究雖然是回溯性，但能夠同時探討單一疾病的多重暴露病因。",
      "flashcard_front": "病例對照研究 / 世代追蹤 (佇列) 研究 / 選擇性偏差 / 研究缺點",
      "flashcard_back": "病例對照研究為回溯性設計，其主要缺點是極易產生選擇性偏差與回憶偏差。",
      "flashcard_summary": "病例對照研究缺點 -> 病例對照研究較佇列研究更易產生選擇性偏差與回憶偏差。"
    },
    {
      "question_id": "110-1_medicine-2_037",
      "question_number": 37,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "比較流感罹患率之統計抽樣與推論局限。",
      "explanation": "年輕人與老年人屬於兩個獨立的次群體，其罹患率（0.42 與 0.22）不同，且在沒有調整母群體實際年齡權重的情況下直接合併兩組（200人）計算出 0.32 來代表總人口流感罹患率是極不恰當的，故(D)選項最不恰當。隨機抽樣需考量群聚效應與獨立性假設，安養中心隨機抽樣常因互相傳染而不宜視為獨立樣本。",
      "flashcard_front": "流感罹患率比較 / 獨立樣本假設 / 合併樣本估計 / 次群體權重",
      "flashcard_back": "不同流感罹患率的次群體不能在未做權重調整下直接合併估計整體人口罹患率。",
      "flashcard_summary": "合併估計罹患率限制 -> 具差異之次群體在未調整權重前，不得直接合併估計整體人口罹患率。"
    },
    {
      "question_id": "110-1_medicine-2_038",
      "question_number": 38,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "利用信賴區間重疊與否判定兩組平均值是否具有顯著差異。",
      "explanation": "若兩群體的 95% 信賴區間（CI）完全沒有重疊，則在統計顯著水準 α = 0.05 下，兩者的平均值具有顯著差異。A校(94~98分)與C校(100~106分)的區間完全沒有重疊（98與100之間有空隙），因此兩校智商分數具顯著差異。其餘學校的信賴區間皆有重疊，不能直接推論為具顯著差異。",
      "flashcard_front": "95%信賴區間 / 顯著水準 0.05 / 區間不重疊 / 顯著差異判定",
      "flashcard_back": "兩組平均值的 95% 信賴區間若完全沒有重疊，代表其平均值在顯著水準 0.05 下具顯著差異。",
      "flashcard_summary": "信賴區間與顯著差異 -> 95%信賴區間完全無重疊時，兩組平均值具有顯著差異。"
    },
    {
      "question_id": "110-1_medicine-2_039",
      "question_number": 39,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "懸浮微粒與溫室氣體對全球暖化的相反效應。",
      "explanation": "大氣中的懸浮微粒（如氣膠、硫酸鹽）主要會反射太陽輻射，對氣溫產生「冷卻效應」（反溫室效應），這與 CO2 的「增溫效應」（溫室效應）相反，兩者並無相互加成作用，故(B)敘述最不恰當。二氧化碳是除水蒸氣外最重要的溫室氣體，京都議定書也確實旨在削減其排放量。",
      "flashcard_front": "全球暖化 / 懸浮微粒 / 二氧化碳 (CO2) / 冷卻與增溫效應",
      "flashcard_back": "懸浮微粒大多產生冷卻效應，與CO2之增溫溫室效應相反且不具加成作用。",
      "flashcard_summary": "懸浮微粒與全球暖化 -> 懸浮微粒產生冷卻效應，與CO2的溫室效應相反，無加成作用。"
    },
    {
      "question_id": "110-1_medicine-2_040",
      "question_number": 40,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "烏腳病成因之井水類型與砷暴露特徵。",
      "explanation": "本題為官方更正之一律給分題，正解設定為(A)。爭議在於早期台灣西南沿海烏腳病流行是由於飲用「深井水」（而非地下河井水或淺井水）中的無機砷暴露所致，題幹用詞不夠精確。砷暴露確實會增加膀胱癌、肝癌等多種癌症風險，並可在毛髮指甲中累積，自來水提供後暴露風險已顯著下降。",
      "flashcard_front": "烏腳病 / 深井水 / 無機砷暴露 / 癌症風險與檢測",
      "flashcard_back": "台灣烏腳病與飲用深井水中的無機砷暴露有關；此題因用詞不精確一律給分。",
      "flashcard_summary": "烏腳病與砷暴露 -> 烏腳病流行是由於飲用深井水中的無機砷暴露，此題因文字瑕疵一律給分。"
    },
    {
      "question_id": "110-1_medicine-2_041",
      "question_number": 41,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "氯乙烯暴露與肝血管肉瘤之職業病關係。",
      "explanation": "肝血管肉瘤（hepatic angiosarcoma）是一種罕見且惡性度極高的血管腫瘤，石化工廠員工長期暴露於氯乙烯單體（vinyl chloride monomer, VCM）是其明確的職業致病原因。二異氰酸甲苯主要引發職業性氣喘；錳暴露會導致類似巴金森氏症的錳中毒；鉛暴露則主要造成貧血與周邊神經炎。",
      "flashcard_front": "肝血管肉瘤 / 石化工廠 / 氯乙烯 (VCM) 暴露 / 職業病",
      "flashcard_back": "石化工廠中的氯乙烯單體(VCM)暴露是導致罕見肝血管肉瘤的明確職業因素。",
      "flashcard_summary": "氯乙烯與肝血管肉瘤 -> 氯乙烯(VCM)職業暴露與罕見肝血管肉瘤有明確因果關係。"
    },
    {
      "question_id": "110-1_medicine-2_042",
      "question_number": 42,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "職業衛生8小時日時量平均容許濃度的基準工時。",
      "explanation": "八小時日時量平均容許濃度（TLV-TWA）是指勞工在「每日工作8小時、每週工作40小時（每週工作5天）」的常規職業暴露下，絕大多數健康勞工終其一生重複暴露在此濃度下，不致產生不良健康效應的平均濃度。此定義符合國際與我國職業安全衛生法規的標準工時。",
      "flashcard_front": "時量平均容許濃度 (TLV-TWA) / 8小時 / 基準工時 / 職業暴露上限",
      "flashcard_back": "TLV-TWA 的定義基準是每日工作 8 小時、每週工作 40 小時（每週工作 5 天）。",
      "flashcard_summary": "TLV-TWA基準工時 -> TLV-TWA 的定義基準是每日8小時、每週40小時（每週5天）的工時。"
    },
    {
      "question_id": "110-1_medicine-2_043",
      "question_number": 43,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "健康城市之持續改善過程定義。",
      "explanation": "世界衛生組織（WHO）強調，健康城市（Healthy Cities）並非僅指一個城市達到特定的健康「結果」，而是一個持續改善環境、開拓資源並使居民在生活中互相支援的「過程」，故選項(A)敘述錯誤。健康城市注重依自訂優先次序實施行動、加強鄉鎮間合作，並關心世界資源的公平分配。",
      "flashcard_front": "健康城市 / 改善過程 / 資源公平 / 世界衛生組織",
      "flashcard_back": "健康城市是一個持續改善環境與支援居民的「過程」，而非僅看特定健康指標的「結果」。",
      "flashcard_summary": "健康城市定義 -> 健康城市的核心在於持續改善的「過程」，而非單純的「結果」。"
    },
    {
      "question_id": "110-1_medicine-2_044",
      "question_number": 44,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "跨理論模式中行為改變階段之判定。",
      "explanation": "根據跨理論模式（TTM），員工「有想運動但尚未行動」代表處於沉思期（contemplation phase），即打算在未來六個月內開始行動。而「已經開始買運動器材但尚未規律運動」則代表已採取初期準備步驟，處於準備期（preparation phase），打算在未來一個月內採取行動，故(C)選項正確。",
      "flashcard_front": "跨理論模式 (TTM) / 想動尚未行動 / 買器材但未規律 / 行為改變階段",
      "flashcard_back": "想動但未行動屬於沉思期；買了運動器材但未規律運動則屬於準備期。",
      "flashcard_summary": "跨理論模式階段判定 -> 想動未動為沉思期，買器材但未規律運動為準備期。"
    },
    {
      "question_id": "110-1_medicine-2_045",
      "question_number": 45,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "毒品危害防制條例之分級與處罰機制。",
      "explanation": "根據毒品危害防制條例，施用第三級毒品（如 K 他命）或第四級毒品者，主要是處以行政罰（罰鍰及毒品危害防制講習），並非一律由檢察官起訴，故(C)選項敘述最不恰當。K他命為第三級毒品；偏好追求新奇刺激者接觸毒品機率高；海洛因成癮者前往機構進行美沙冬治療屬於替代療法。",
      "flashcard_front": "毒品分級 / 施用第三級毒品 (如K他命) / 行政罰與起訴 / 美沙冬替代療法",
      "flashcard_back": "施用第三級或第四級毒品者處以行政罰（罰鍰與講習），並非一律刑事起訴。",
      "flashcard_summary": "施用三級毒品處罰 -> 施用第三級毒品主要是行政罰與講習，不一律起訴。"
    },
    {
      "question_id": "110-1_medicine-2_046",
      "question_number": 46,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "涵化理論對受眾社會認知之形塑作用。",
      "explanation": "涵化理論（Cultivation Theory）指出，長期且大量接觸電視等大眾傳播媒體的受眾，其對於現實世界的認知會逐漸被媒體所描繪的「媒體現實」所塑造與同化，進而將暴力的情境視為真實世界的反映。創新擴散理論探討新觀念如何傳播普及；媒體倡導強調利用媒體進行社會或政策改變；知溝理論則說明社會階層造成的知識獲取差距。",
      "flashcard_front": "大眾媒體暴力 / 反映真實世界 / 傳播理論 / 認知形塑",
      "flashcard_back": "長期觀看媒體暴力並認為其反映社會真實，是應用了「涵化理論」（Cultivation Theory）。",
      "flashcard_summary": "涵化理論應用 -> 涵化理論說明長期接觸大眾媒體會使受眾的現實認知被媒體內容所形塑。"
    }
  ]
}

# ==================== BATCH 004 ====================
batches_data["110-1_medicine-2_batch-004"] = {
  "dataset_id": "110-1_medicine-2",
  "batch_id": "110-1_medicine-2_batch-004",
  "items": [
    {
      "question_id": "110-1_medicine-2_047",
      "question_number": 47,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "傷害防制之對象與流行病學模式。",
      "explanation": "傷害防制（injury prevention and control）主要且傳統上針對的是「非蓄意性傷害」（即意外事故，如車禍、溺水），雖然現代亦延伸至蓄意性傷害（如家暴、自殺），但將其狹隘地定義為僅預防蓄意性傷害是極不恰當的，故(A)選項最不恰當。傷害防制需多學門合作，且可用宿主-致病原-環境的疾病三角模式解釋。",
      "flashcard_front": "傷害防制 / 蓄意與非蓄意傷害 / 疾病三角模式 / 多專業合作",
      "flashcard_back": "傷害防制主要針對非蓄意性傷害（意外），不可定義為僅預防蓄意傷害。",
      "flashcard_summary": "傷害防制對象 -> 傷害防制主要針對非蓄意性意外傷害，不應限於蓄意傷害。"
    },
    {
      "question_id": "110-1_medicine-2_048",
      "question_number": 48,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "健保支付制度之基準單位與節約誘因比較。",
      "explanation": "健保支付制度中，依支付單位的基準大小排序為：論人計酬 > 論病例計酬 > 論日計酬 > 論量計酬。論人計酬（Capitation）是以每位投保人在特定期間內的所有醫療服務作為支付基準，其單位最大。在定額預算下，醫療提供者有最大誘因推動預防醫學及避免不必要醫療，故其節約誘因最大。",
      "flashcard_front": "健保支付制度 / 基準單位最大 / 節約誘因最大 / 論人計酬",
      "flashcard_back": "論人計酬(Capitation)的支付基準單位最大，能提供醫療院所最大的節約誘因。",
      "flashcard_summary": "支付制度節約誘因 -> 論人計酬支付單位最大，對醫療服務提供者的節約誘因最大。"
    },
    {
      "question_id": "110-1_medicine-2_049",
      "question_number": 49,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "世界衛生組織之組織結構與技術合作功能。",
      "explanation": "世界衛生組織（WHO）是聯合國系統內負責國際衛生的專門機構，其主要功能與憲章明文規定即包含向各國政府提供「技術合作」與協助以建立醫療體系，故(B)敘述最不恰當。WHO 的最高權力機構為世界衛生大會（WHA），且該組織近年確實面臨全球公共衛生經費短缺與行政效率的挑戰。",
      "flashcard_front": "世界衛生組織 (WHO) / 聯合國專門機構 / 技術合作 / 世界衛生大會 (WHA)",
      "flashcard_back": "WHO的主要功能明確包含向各國提供「技術合作」與衛生協助。",
      "flashcard_summary": "WHO功能與結構 -> WHO為聯合國專門機構，其功能明文包含技術合作，最高權力機構為WHA。"
    },
    {
      "question_id": "110-1_medicine-2_050",
      "question_number": 50,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "公共衛生學",
      "category_confidence": "high",
      "key_point": "平衡計分卡各構面之指標性質。",
      "explanation": "在平衡計分卡（Balanced Scorecard）中，財務指標反映過去經營的成果，屬於滯後指標（lagging indicator，落後指標），而非預測未來表現的領先指標（leading indicator，如學習與成長構面），故(C)敘述最不恰當。平衡計分卡旨在將策略轉換為行動，通常包含四大構面，非營利組織可增設第五構面。",
      "flashcard_front": "平衡計分卡 / 四大構面 / 財務構面 / 領先與落後指標",
      "flashcard_back": "財務構面在平衡計分卡中屬於落後指標（滯後指標），而非領先指標。",
      "flashcard_summary": "平衡計分卡指標性質 -> 財務構面為落後（滯後）指標，學習與成長等才屬於領先指標。"
    },
    {
      "question_id": "110-1_medicine-2_051",
      "question_number": 51,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "Abacavir 過敏反應與 HLA-B*5701 基因型檢測。",
      "explanation": "抗病毒藥物 Abacavir（一種核苷類反轉錄酶抑制劑）易引發嚴重的全身性過敏反應（如致命皮疹、發燒、多器官受累），此不良反應與患者攜帶 HLA-B*5701 基因具有高度相關性，用藥前必須進行篩檢。Carbamazepine SJS 過敏與 HLA-B*1502 相關；Allopurinol 過敏則與 HLA-B*5801 相關。",
      "flashcard_front": "抗病毒藥物 / 嚴重皮疹水疱過敏 / HLA-B*5701 / 基因檢測",
      "flashcard_back": "使用 Abacavir 前必須檢測 HLA-B*5701 基因型，以預防嚴重的全身性藥物過敏。",
      "flashcard_summary": "Abacavir與HLA-B*5701 -> 使用 Abacavir 前需驗 HLA-B*5701 以預防嚴重過敏。"
    },
    {
      "question_id": "110-1_medicine-2_052",
      "question_number": 52,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "青黴素類抗生素之吸收、抗藥性及排泄特徵。",
      "explanation": "Amoxicillin 為廣效性青黴素，其主要抗藥性機制是細菌產生了 β-內醯胺酶（β-lactamase）水解藥物環狀結構，故選項(C)正確。Ampicillin 的口服吸收會受到飲食的明顯抑制，而 Amoxicillin 較不受影響；Dicloxacillin 為耐酸性青黴素；Nafcillin 主要是經由膽汁與肝臟排泄而非腎臟。",
      "flashcard_front": "青黴素類抗生素 / beta-内醯胺酶 / 飲食影響吸收 / Nafcillin排泄",
      "flashcard_back": "Amoxicillin 抗藥性主因是產生 β-lactamase；Nafcillin 主要經膽汁與肝臟排泄。",
      "flashcard_summary": "青黴素類藥物特徵 -> Amoxicillin 抗藥性主因為 β-lactamase，Nafcillin 主要經膽汁排泄。"
    },
    {
      "question_id": "110-1_medicine-2_053",
      "question_number": 53,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "單株抗體抗癌藥物之治療靶點與副作用。",
      "explanation": "Catumaxomab 是一種三功能雙特異性單株抗體，能同時結合腫瘤細胞表面的 EpCAM 抗原以及 T 細胞表面的 CD3 受體，並透過其 Fc 區活化輔助細胞，故(C)選項正確。Alemtuzumab 針對 CD52，會導致嚴重的淋巴球減少症；Bevacizumab 抑制血管新生會影響傷口癒合，手術後不宜立刻投藥；Ramucirumab 阻斷的是 VEGFR2 而非 EGFR。",
      "flashcard_front": "單株抗體抗癌藥 / 雙特異性 / Catumaxomab / Bevacizumab傷口癒合",
      "flashcard_back": "Catumaxomab能同時作用在腫瘤(EpCAM)及T細胞(CD3)上；Bevacizumab因延緩傷口癒合手術後禁用。",
      "flashcard_summary": "抗癌單株抗體機制 -> Catumaxomab 可同時作用於腫瘤及 T 細胞；Bevacizumab 術後不宜即時使用。"
    },
    {
      "question_id": "110-1_medicine-2_054",
      "question_number": 54,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "拓撲異構酶 II 抑制劑之抗癌藥物種類。",
      "explanation": "Idarubicin 屬於小紅莓類（anthracyclines）抗癌抗生素，其主要機制為嵌入 DNA 鹼基對，並藉由抑制第二型拓撲異構酶（topoisomerase II）來阻止 DNA 的複製與轉錄，進而造成 DNA 雙股斷裂。Busulfan 與 Cyclophosphamide 屬於烷化劑；Methotrexate 則為葉酸拮抗劑。",
      "flashcard_front": "抗癌藥物 / 抑制 topoisomerase II / DNA 斷裂 / Idarubicin",
      "flashcard_back": "Idarubicin（蒽環類抗生素）能抑制 topoisomerase II，導致 DNA 斷裂而發揮抗癌作用。",
      "flashcard_summary": "Topoisomerase II 抑制劑 -> Idarubicin 藉由抑制 topoisomerase II 導致癌細胞 DNA 斷裂。"
    },
    {
      "question_id": "110-1_medicine-2_055",
      "question_number": 55,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "CMF 乳癌療法的嘧啶類似物藥物成分。",
      "explanation": "乳癌 CMF 合併療法包含 Cyclophosphamide、Methotrexate 及 5-Fluorouracil。其中 5-Fluorouracil (5-FU) 屬於嘧啶類似物（pyrimidine analog），在體內被代謝為 5-FdUMP，能與 thymidylate synthase 形成共價結合，抑制胸苷酸合成，進而阻斷 DNA 的合成，故(A)選項正確。",
      "flashcard_front": "乳癌 CMF 療法 / pyrimidine 類似物 / 抑制 thymidylate synthase",
      "flashcard_back": "CMF 療法中的 5-Fluorouracil 屬於嘧啶類似物，可抑制 thymidylate synthase。",
      "flashcard_summary": "CMF療法5-FU -> CMF 療法中的 5-FU 為嘧啶類似物，可抑制 thymidylate synthase 以阻斷 DNA 合成。"
    },
    {
      "question_id": "110-1_medicine-2_056",
      "question_number": 56,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "Sumatriptan 治療偏頭痛之作用機轉與禁忌症。",
      "explanation": "Sumatriptan 是一種 5-HT1B/1D 受體「激動劑」（agonist）而非拮抗劑，它藉由活化這些受體來引發腦部血管收縮，並減少發炎性神經胜肽的釋放，從而治療偏頭痛。由於其具血管收縮活性，因此冠狀動脈疾病（如心絞痛、心肌梗塞）患者禁忌使用；與 SSRI 併用可能引發血清素症候群。",
      "flashcard_front": "偏頭痛藥物 / Sumatriptan / 5-HT1B/1D / 冠狀動脈疾病禁忌",
      "flashcard_back": "Sumatriptan 為 5-HT1B/1D 受體激動劑，具收縮血管活性，冠狀動脈疾病患者禁用。",
      "flashcard_summary": "Sumatriptan機制與禁忌 -> Sumatriptan 為 5-HT1B/1D 激動劑（非拮抗劑），冠心病患者禁用。"
    },
    {
      "question_id": "110-1_medicine-2_057",
      "question_number": 57,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "Fenofibrate 活化 PPAR-α 與 脂蛋白脂酶 之降血脂機制。",
      "explanation": "Fenofibrate 屬於纖維酸類（fibrates）降血脂藥物，其作用機轉是活化過氧化體增殖劑活化受體-α（PPAR-α），進而「活化」（而非抑制）脂蛋白脂酶（lipoprotein lipase, LPL）的活性，加速富含甘油三酯的脂蛋白清除，故(D)選項錯誤。該藥物能活化肝臟脂肪酸氧化，主要副作用包括肌肉病變及肝功能異常。",
      "flashcard_front": "降血脂藥 / Fenofibrate / PPAR-alpha / 脂蛋白脂酶 (LPL)",
      "flashcard_back": "Fenofibrate 活化 PPAR-α，進而活化（而非抑制）LPL 以降低甘油三酯。",
      "flashcard_summary": "Fenofibrate機轉 -> Fenofibrate 活化 PPAR-α 並活化 LPL 活性，促使甘油三酯下降。"
    },
    {
      "question_id": "110-1_medicine-2_058",
      "question_number": 58,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "EPO 促紅血球生成素的訊息傳遞路徑與副作用。",
      "explanation": "紅血球生成素（EPO）的受體屬於第一型細胞激素受體家族，其配體結合後主要透過活化關聯的非受體酪胺酸激酶 JAK2，進而引發下游的 JAK2-STAT5 訊息傳遞路徑，此為其最主要的訊息傳遞機制，故選項(C)為錯誤描述。Darbepoetin alfa 為其長效類似物；EPO 常見副作用為高血壓及血栓症。",
      "flashcard_front": "EPO 禁藥篩檢 / JAK2-STAT5 / 紅血球分化 / 高血壓血栓副作用",
      "flashcard_back": "EPO 受體活化後主要傳導 JAK2-STAT5 訊息路徑，而非以 ERK 為主；常見副作用為高血壓與血栓。",
      "flashcard_summary": "EPO訊息傳導與副作用 -> EPO 受體主要活化 JAK2-STAT5 路徑，常見副作用為高血壓與血栓。"
    },
    {
      "question_id": "110-1_medicine-2_059",
      "question_number": 59,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "Desmopressin 促進內皮細胞釋放凝血因子之機轉。",
      "explanation": "Desmopressin（DDAVP）是血管加壓素（vasopressin）的合成類似物，能選擇性活化 V2 受體。在凝血功能方面，它能刺激血管內皮細胞釋放儲存的第八凝血因子（Factor VIII）與溫韋伯氏因子（vWF）進入血液，常用於輕度甲型血友病及類血友病患者。它不會活化 ADP 受體或促進纖溶酶原活化。",
      "flashcard_front": "Desmopressin (DDAVP) / 血管內皮細胞 / Factor VIII / vWF釋放",
      "flashcard_back": "Desmopressin 能調節並促進血管內皮細胞釋放第八凝血因子(Factor VIII)與 vWF。",
      "flashcard_summary": "Desmopressin凝血機轉 -> Desmopressin 能促進血管內皮細胞釋放第八凝血因子及 vWF。"
    },
    {
      "question_id": "110-1_medicine-2_060",
      "question_number": 60,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "Levothyroxine 用於甲狀腺機能低下之禁忌與甲亢治療藥物。",
      "explanation": "Levothyroxine 是一種合成的甲狀腺素（T4），臨床上用於治療「甲狀腺機能低下」，若給予甲狀腺機能庫進的患者會使其症狀（如心悸、手抖）進一步惡化，因此最不適合。Propylthiouracil（PTU）為抗甲狀腺藥物，Lugol's solution 可抑制甲狀腺素釋放，Propranolol 則可緩解甲亢造成的心悸、手抖等交感神經亢進症狀。",
      "flashcard_front": "甲狀腺機能亢進 / Levothyroxine / PTU / Propranolol",
      "flashcard_back": "Levothyroxine 為甲狀腺素補充劑（用於甲低），甲亢患者禁用。",
      "flashcard_summary": "甲亢藥物禁忌 -> Levothyroxine 為補充甲狀腺素之藥物，甲亢患者不適合使用。"
    },
    {
      "question_id": "110-1_medicine-2_061",
      "question_number": 61,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "第一型糖尿病必須使用胰島素替代療法。",
      "explanation": "第一型糖尿病（T1DM）的主要病生理機轉為胰臟 β 細胞遭受自體免疫破壞，導致內源性胰島素絕對缺乏。因此，外源性胰島素（insulin）替代療法是第一型糖尿病患者控制血糖唯一且必須的藥物治療方式。口服降血糖藥如 Glipizide 或 Sitagliptin 皆高度依賴尚存的 β 細胞功能，因此不適用。",
      "flashcard_front": "第一型糖尿病 / 胰臟beta細胞破壞 / 胰島素 / 口服降血糖藥不適用",
      "flashcard_back": "第一型糖尿病為胰島素絕對缺乏，治療必須且只能使用胰島素(insulin)替代療法。",
      "flashcard_summary": "第一型糖尿病治療 -> 第一型糖尿病患者胰島素絕對缺乏，最適合且必須使用胰島素治療。"
    }
  ]
}

# ==================== BATCH 005 ====================
batches_data["110-1_medicine-2_batch-005"] = {
  "dataset_id": "110-1_medicine-2",
  "batch_id": "110-1_medicine-2_batch-005",
  "items": [
    {
      "question_id": "110-1_medicine-2_062",
      "question_number": 62,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "類固醇對胃黏膜之損害與消化性潰瘍之用藥禁忌。",
      "explanation": "糖皮質激素（類固醇）會抑制前列腺素的合成，進而減少胃黏液分泌、增加胃酸分泌，並損害胃黏膜保護屏障，極易誘發或惡化消化性潰瘍（peptic ulcer）及胃出血，因此最不適合使用。愛迪生氏病為腎上腺皮質功能低下，需使用類固醇進行補充治療；發炎性腸道疾病及氣喘皆屬於發炎或自體免疫性疾病，類固醇是其重要的抗發炎治療藥物。",
      "flashcard_front": "類固醇 / 糖皮質激素 / 前列腺素抑制 / 消化性潰瘍禁忌",
      "flashcard_back": "類固醇會抑制前列腺素合成，損害胃黏膜屏障，消化性潰瘍患者較不適合使用。",
      "flashcard_summary": "類固醇與消化性潰瘍 -> 類固醇抑制前列腺素合成並損害胃黏膜，消化性潰瘍患者應避免使用。"
    },
    {
      "question_id": "110-1_medicine-2_063",
      "question_number": 63,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "Fenoldopam 作為 D1 多巴胺受體致效劑之降血壓機制。",
      "explanation": "Fenoldopam 是一種選擇性多巴胺第一型受體（D1 receptor）的強效致效劑，能引發腎血管及周邊血管擴張，主要用於治療高血壓急症（hypertensive emergencies）。Clonidine 為 α2 受體致效劑；Diazoxide 為鉀離子通道開放劑；Ketanserin 則為 5-HT2 受體拮抗劑。",
      "flashcard_front": "D1-dopamine receptor agonist / 血管擴張 / 腎血管流量 / Fenoldopam",
      "flashcard_back": "Fenoldopam 屬於 D1 多巴胺受體致效劑，能擴張腎血管並作為降血壓藥物。",
      "flashcard_summary": "D1多巴胺受體致效劑 -> Fenoldopam 為 D1 受體致效劑，具血管擴張作用，可用於降血壓。"
    },
    {
      "question_id": "110-1_medicine-2_064",
      "question_number": 64,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "Acetazolamide 碳酸酐酶抑制劑之利尿位置與青光眼治療。",
      "explanation": "Acetazolamide 是一種碳酸酐酶抑制劑（carbonic anhydrase inhibitor），作用於近曲小管，藉由減少重碳酸根離子的重吸收來達到利尿效果。由於房水生成高度依賴碳酸酐酶，因此該藥物能有效減少房水分泌，用於降低眼壓以治療青光眼。該藥物容易引發低血鉀與代謝性酸中毒，但沒有耳毒性（耳毒性為環利尿劑 loop diuretics 如 furosemide 的特點）。",
      "flashcard_front": "Acetazolamide / 碳酸酐酶抑制劑 / 近曲小管 / 青光眼治療",
      "flashcard_back": "Acetazolamide 作用於近曲小管，抑制碳酸酐酶，臨床上可用於治療青光眼。",
      "flashcard_summary": "Acetazolamide作用與臨床 -> Acetazolamide 為碳酸酐酶抑制劑，作用於近曲小管，可用於治療青光眼。"
    },
    {
      "question_id": "110-1_medicine-2_065",
      "question_number": 65,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "交感神經 alpha-1 受體活化之平滑肌收縮反應與膀胱排尿調控。",
      "explanation": "活化 α1 受體會使平滑肌收縮，在泌尿系統中會導致「膀胱括約肌（sphincter）」及「膀胱頸」平滑肌收縮，進而阻止排尿，而膀胱逼尿肌（detrusor muscle）的收縮主要由副交感神經的 M3 受體活化所控制。其餘選項中，豎毛肌收縮（引發雞皮疙瘩）、骨骼肌血管收縮以及心肌收縮力增強（透過 Gq 蛋白路徑增加細胞內鈣離子）均為 α1 受體活化後的正確生理反應。",
      "flashcard_front": "alpha-1 交感受體 / 膀胱逼尿肌 / 膀胱括約肌 / 平滑肌收縮",
      "flashcard_back": "活化 α1 受體會收縮膀胱括約肌與尿道，而膀胱逼尿肌的收縮由副交感 M3 受體調控。",
      "flashcard_summary": "alpha-1與逼尿肌調控 -> α1 受體活化不導致逼尿肌收縮（逼尿肌收縮由副交感M3控制，α1收縮的是括約肌）。"
    },
    {
      "question_id": "110-1_medicine-2_066",
      "question_number": 66,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "長效吸入型抗膽鹼藥物 Tiotropium 之理化性質與臨床應用。",
      "explanation": "Tiotropium 是一種具季銨結構（quaternary ammonium）的抗膽鹼藥物，帶電荷的極性使其極難通過血腦屏障，因此吸入後主要作用在肺部局部，中樞副作用極少。Tiotiotropium 與蕈毒鹼受體（M3）結合後的解離速度極慢，提供長達25小時以上的半衰期，為每日一次的長效吸入劑（LAMA）。Ipratropium 亦為季銨結構但屬於短效劑型（半衰期約2小時）；Tropicamide 主要用於散瞳；Benztropine 為三級胺，易進腦部，常用於治療巴金森氏症或藥物引起的錐體外症候群（EPS）。",
      "flashcard_front": "季銨結構 / 不過血腦屏障 / COPD氣管舒張 / 半衰期25小時 / M3受體解離慢",
      "flashcard_back": "Tiotropium 具有極性季銨結構不過 BBB，且與 M3 受體結合解離慢，半衰期達25小時。",
      "flashcard_summary": "Tiotropium理化特性 -> Tiotropium 不易過 BBB，半衰期長達25小時，為COPD長效舒張劑。"
    },
    {
      "question_id": "110-1_medicine-2_067",
      "question_number": 67,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "短效 β2 接受體激動劑 Albuterol 之臨床特徵。",
      "explanation": "Albuterol（沙丁胺醇）為短效型 β2 受體激動劑（SABA），利用計量吸入器（MDI）給藥時，藥物會直接作用於肺部支氣管平滑肌以達到迅速舒張氣管的效果，且因經吸入途徑被吞入胃部的部分大多在肝臟被首渡效應代謝，導致其全身性生體可用率極低。Montelukast 為口服白三烯受體拮抗劑；Flunisolide 屬於吸入型類固醇；Tiotropium 為長效抗膽鹼藥物而非短效。",
      "flashcard_front": "短效 β2 激動劑 / MDI / 幾乎無生體可用率 / 支氣管擴張",
      "flashcard_back": "Albuterol 為短效 β2 受體激動劑，吸入後主要作用在肺部且幾乎無全身性生體可用率。",
      "flashcard_summary": "Albuterol吸入特徵 -> Albuterol 為短效 β2 激動劑，吸入給藥幾乎無全身生體可用率。"
    },
    {
      "question_id": "110-1_medicine-2_068",
      "question_number": 68,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "組織胺第二型受體拮抗劑之抑酸強度比較。",
      "explanation": "在常用的組織胺第二型受體拮抗劑（H2RAs）中，Famotidine 的抑酸作用強度（potency）是所有同類藥物中最強的（其強度約為 Ranitidine 的 7.5 倍，Cimetidine 的 20 到 50 倍）。Cimetidine 的強度最弱，且具有較強的細胞色素 P450（CYP450）抑制作用與抗雄性素副作用。Ranitidine 與 Nizatidine 的作用強度則介於兩者之間。",
      "flashcard_front": "H2受體拮抗劑 / 抑制胃酸 / 作用強度 (potency) 最強 / Cimetidine",
      "flashcard_back": "Famotidine 是 H2 受體拮抗劑中抑制胃酸分泌作用強度(potency)最強的藥物。",
      "flashcard_summary": "H2受體拮抗劑強度 -> H2受體拮抗劑中以 Famotidine 的作用強度(potency)為最強。"
    },
    {
      "question_id": "110-1_medicine-2_069",
      "question_number": 69,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "褪黑激素受體 MT1/MT2 致效劑之治療應用。",
      "explanation": "Tasimelteon 是一種選擇性褪黑激素受體第一型（MT1）和第二型（MT2）的致效劑，主要用於治療非24小時睡醒週期障礙（Non-24-hour sleep-wake disorder，常見於全盲患者）。Sumatriptan 用於治療偏頭痛；Repinotan 是一種 5-HT1A 激動劑；Orlistat 則為抑制腸胃道脂肪酶的減重藥物。",
      "flashcard_front": "睡眠失調 / MT1與MT2受體 / 褪黑激素致效劑 / Tasimelteon",
      "flashcard_back": "Tasimelteon 是一種 MT1 和 MT2 受體致效劑，臨床上可用於治療特定的睡眠失調。",
      "flashcard_summary": "褪黑激素受體致效劑 -> Tasimelteon 為 MT1/MT2 受體致效劑，用於治療特定睡眠失調。"
    },
    {
      "question_id": "110-1_medicine-2_070",
      "question_number": 70,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "前列腺素 F2α 類似物在青光眼治療之應用。",
      "explanation": "Latanoprost 是一種前列腺素 F2α 類似物（PGF2α analog）的酯類前驅藥，能增加房水經由葡萄膜鞏膜路徑（uveoscleral pathway）的排出量，進而降低眼壓，是治療隅角開放性青光眼的首選第一線藥物。Alprostadil（PGE1）臨床用於維持新生兒動脈導管開放或治療勃起功能障礙；Misoprostol（PGE1 類似物）用於預防 NSAIDs 引起的胃潰瘍及引產；Dinoprostone（PGE2）主要用於子宮頸催熟引產。",
      "flashcard_front": "隅角開放性青光眼 / 前列腺素F2alpha類似物 / 增加葡萄膜鞏膜排出 / Latanoprost",
      "flashcard_back": "Latanoprost 為前列腺素 F2α 類似物，藉由增加房水葡萄膜鞏膜路徑排出以治療青光眼。",
      "flashcard_summary": "Latanoprost與青光眼 -> Latanoprost 為前列腺素 F2α 類似物，能增加房水葡萄膜鞏膜路徑排出以降眼壓。"
    },
    {
      "question_id": "110-1_medicine-2_071",
      "question_number": 71,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "非嘌呤類黃嘌呤氧化酶抑制劑治療高尿酸血症。",
      "explanation": "Febuxostat 是一種非嘌呤類的黃嘌呤氧化酶抑制劑（non-purine selective inhibitor of xanthine oxidase），可藉由抑制尿酸生成的關鍵酶來有效降低血中尿酸濃度，適用於慢性高尿酸血症及痛風的長期控制。Tramadol 屬於鴉片類止痛藥；Ketorolac 為強效非類固醇抗發炎藥（NSAID），用於急性期止痛；Rilonacept 為 IL-1 抑制劑，主要用於預防痛風急性發作時的發炎反應。",
      "flashcard_front": "慢性高尿酸血症 / 黃嘌呤氧化酶抑制劑 / 非嘌呤類 / Febuxostat",
      "flashcard_back": "Febuxostat 屬於非嘌呤類黃嘌呤氧化酶抑制劑，能有效降低尿酸以治療慢性高尿酸血症。",
      "flashcard_summary": "Febuxostat與高尿酸血症 -> Febuxostat 為非嘌呤類黃嘌呤氧化酶抑制劑，用於慢性高尿酸血症之治療。"
    },
    {
      "question_id": "110-1_medicine-2_072",
      "question_number": 72,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "抗精神病藥物之 D2 拮抗強度與錐體外症候群副作用。",
      "explanation": "Haloperidol 屬於第一代（典型）抗精神病藥物，因對腦部黑質紋狀體路徑的多巴胺 D2 受體具有極高的親和力與拮抗作用，因此引發錐體外症候群（EPS，如急性肌張力不全、靜坐不能、類巴金森氏症）的副作用在所有抗精神病藥中最為顯著。Clozapine、Olanzapine 及 Aripiprazole 則屬於第二代（非典型）抗精神病藥物，其對 D2 受體的親和力較低，或是為 D2 受體的部分激動劑，因而引發 EPS 的風險大幅降低。",
      "flashcard_front": "思覺失調症 / 典型抗精神病藥 / 阻斷D2受體 / 錐體外症候群 (EPS) / Haloperidol",
      "flashcard_back": "Haloperidol 具強效 D2 拮抗作用，在所有抗精神病藥中引發 EPS 的副作用最為顯著。",
      "flashcard_summary": "Haloperidol與EPS -> Haloperidol 阻斷多巴胺 D2 受體力道強，引發錐體外症候群之風險最高。"
    },
    {
      "question_id": "110-1_medicine-2_073",
      "question_number": 73,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "Naloxone 作為鴉片受體純拮抗劑之成癮性與臨床應用。",
      "explanation": "Naloxone 是一種純粹的鴉片受體拮抗劑（mu-opioid receptor antagonist），本身不具任何內在活性或令人愉悅的效應，臨床上主要用於逆轉鴉片類藥物過量所致的呼吸抑制，因此逆轉不會造成精神依賴性（心癮）。Cocaine（可卡因）為強烈的中樞神經興奮劑，Ketamine（K他命）為解離性麻醉劑，Psilocybin（裸蓋菇素）為致幻劑，此三者皆有造成精神依賴性或濫用的高度風險。",
      "flashcard_front": "精神依賴性 / 鴉片受體拮抗劑 / 解毒劑 / Naloxone",
      "flashcard_back": "Naloxone 為純鴉片受體拮抗劑，不具內在活性，絕不易造成精神依賴性。",
      "flashcard_summary": "Naloxone依賴性 -> Naloxone 為鴉片受體拮抗劑，無內在活性，不易造成精神依賴性。"
    },
    {
      "question_id": "110-1_medicine-2_074",
      "question_number": 74,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "非苯二氮平類抗焦慮藥物 Buspirone 之作用機制與特徵。",
      "explanation": "Buspirone 是一種非苯二氮平類的抗焦慮藥物，其主要作用機轉為腦部血清素 5-HT1A 受體的部分致效劑（partial agonist），而非作用於 GABA_A 受體，故(B)敘述錯誤。因為其不作用在 GABA 系統，所以不像苯二氮平類（Benzodiazepines）藥物那般具有抗痙攣、肌肉鬆弛或鎮靜安眠的作用，也不會產生加成酒精的抑制作作用。此外，Buspirone 的療效通常需要連續服用 2 到 4 週後才會逐漸顯現，不適合用於急性焦慮發作。",
      "flashcard_front": "抗焦慮藥 / 5-HT1A部分致效劑 / 無肌肉鬆弛與安眠作用 / 需服藥數週顯現",
      "flashcard_back": "Buspirone 主要作用於 5-HT1A 受體（非 GABA 受體），無鎮靜安眠與肌肉鬆弛作用。",
      "flashcard_summary": "Buspirone機轉與作用 -> Buspirone 為 5-HT1A 部分致效劑而非作用於GABA受體，無肌肉鬆弛作用。"
    },
    {
      "question_id": "110-1_medicine-2_075",
      "question_number": 75,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "藥理學",
      "category_confidence": "high",
      "key_point": "升糖素（Glucagon）作為 beta 受體阻斷劑中毒之解毒劑機制。",
      "explanation": "升糖素（Glucagon）是 β 受體阻斷劑（如 propranolol）過量中毒時的首選解毒劑。它能繞過被阻斷的 β 受體，直接活化心肌細胞表面的升糖素受體，透過 Gs 蛋白路徑刺激腺苷酸環化酶，增加細胞內 cAMP 的濃度，進而產生正性的變力與變時作用。Atropine 雖為抗膽鹼藥但對嚴重的 β 阻斷劑中毒提升心率的效果有限，而 Digoxin 及 Pralidoxime 則與此治療無關。",
      "flashcard_front": "propranolol 中毒 / 低血壓心跳過慢 / 首選解毒劑 / 增加 cAMP",
      "flashcard_back": "升糖素(Glucagon)能繞過 β 受體直接增加 cAMP，是 β 阻斷劑中毒的最佳解毒劑。",
      "flashcard_summary": "beta阻斷劑中毒解毒劑 -> 升糖素為 β 阻斷劑中毒首選解毒劑，可繞過 β 受體直接提升 cAMP。"
    },
    {
      "question_id": "110-1_medicine-2_076",
      "question_number": 76,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "類纖維蛋白性壞死與血管炎之病理特徵。",
      "explanation": "類纖維蛋白性壞死（fibrinoid necrosis）是一種常見於免疫反應（如血管炎、免疫複合物沉積）或惡性高血壓的病理變化，其特徵為抗原-抗體複合物與滲出的纖維蛋白沉積在血管壁中，在 H&E 染色下呈現亮粉紅色的無結構外觀。結核病的壞死屬於乾酪性壞死；腦梗塞屬於液化性壞死；急性胰臟炎則常伴隨脂肪壞死。",
      "flashcard_front": "壞死類型 / 血管炎 / 免疫複合物沉積 / 亮粉紅無結構血管壁",
      "flashcard_back": "類纖維蛋白性壞死(fibrinoid necrosis)最常出現於血管炎，因免疫複合物與纖維蛋白沉積於血管壁。",
      "flashcard_summary": "類纖維蛋白性壞死與血管炎 -> 類纖維蛋白性壞死是血管炎的典型特徵，因免疫複合物沉積血管壁所致。"
    }
  ]
}

# ==================== BATCH 006 ====================
batches_data["110-1_medicine-2_batch-006"] = {
  "dataset_id": "110-1_medicine-2",
  "batch_id": "110-1_medicine-2_batch-006",
  "items": [
    {
      "question_id": "110-1_medicine-2_077",
      "question_number": 77,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "肉芽組織之組織學構成特徵。",
      "explanation": "肉芽組織（granulation tissue）是傷口癒合與修復過程中的特徵性組織，由新生毛細血管、增生的纖維母細胞及浸潤的發炎細胞共同構成。肉芽腫（granuloma）則是由上皮樣組織細胞（epithelioid histiocytes）聚集成團的一種慢性發炎結節；蟹足腫（keloid）是大量排列紊亂的厚重膠原纖維沉積；類澱粉為細胞外無結構性蛋白質沉積。",
      "flashcard_front": "傷口修復 / 疏鬆間質 / 纖維母細胞與微血管增生 / 發炎細胞浸潤",
      "flashcard_back": "受傷後增生的疏鬆微血管、纖維母細胞與發炎細胞混合物稱為肉芽組織(granulation tissue)。",
      "flashcard_summary": "肉芽組織組織學 -> 受傷後纖維母細胞與微血管增生並混合發炎細胞，為肉芽組織之特徵。"
    },
    {
      "question_id": "110-1_medicine-2_078",
      "question_number": 78,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "全身性紅斑性狼瘡之血管與皮膚病理特徵。",
      "explanation": "全身性紅斑性狼瘡（SLE）患者的急性血管炎常伴有血管壁出現類纖維蛋白性壞死（fibrinoid necrosis），此為其經典的病理特徵，故選項(B)正確。選項A中腎絲球病變主要由免疫複合物沉積（III型超敏反應）引起，對抗基底膜的抗體是 Goodpasture 症候群的特徵；選項C中自體抗體沉積在鱗狀上皮細胞膜周圍是尋常型天皰瘡的表現，SLE 則是沉積於表皮-真皮交界處；選項D的「鐵絲環」（wire-loop）構造主要見於第四型發炎，而非第五型。",
      "flashcard_front": "全身性紅斑性狼瘡 (SLE) / 急性血管炎 / 類纖維蛋白性壞死 / wire-loop / lupus band",
      "flashcard_back": "SLE 急性血管炎常伴隨血管壁類纖維蛋白性壞死；皮膚病變抗體沉積於表皮真皮交界處。",
      "flashcard_summary": "SLE病理特徵 -> SLE 急性血管炎伴血管壁類纖維蛋白性壞死；皮膚自體抗體沉積在表皮真皮交界。"
    },
    {
      "question_id": "110-1_medicine-2_079",
      "question_number": 79,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "鏈球菌感染之常見臨床病變與壞死性腸炎之致病源。",
      "explanation": "鏈球菌屬（Streptococcus）可引起多種人類感染：如肺炎鏈球菌常引起大葉性肺炎；A群鏈球菌（GAS）釋放毒素可導致猩紅熱，或引起感染後的免疫反應如急性腎小球腎炎。相較之下，壞死性腸炎（necrotizing enterocolitis）主要與早產、缺氧、配方奶餵養或艱難梭菌、產氣莢膜梭菌等腸道細菌過度繁殖有關，極少由鏈球菌直接引起。",
      "flashcard_front": "鏈球菌屬 / 大葉性肺炎 / 猩紅熱 / 腎小球腎炎 / 壞死性腸炎",
      "flashcard_back": "鏈球菌感染可引起肺炎、猩紅熱與腎炎，但極少直接引起壞死性腸炎。",
      "flashcard_summary": "鏈球菌感染病變 -> 鏈球菌可致大葉性肺炎、猩紅熱及腎炎，但不常致壞死性腸炎。"
    },
    {
      "question_id": "110-1_medicine-2_080",
      "question_number": 80,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "黃麴毒素引導 TP53 抑癌基因特異性突變之機制。",
      "explanation": "黃麴毒素 B1（Aflatoxin B1）是一種強烈的肝致癌物，其主要分子致癌機制是造成腫瘤抑制基因 TP53 的第 249 密碼子（codon 249）發生特異性的 G 轉變為 T（G-to-T transversion，導致精氨酸變為絲氨酸）的突變，進而使 p53 蛋白失去抑癌功能。此突變特徵在黃麴毒素污染嚴重的地區所發生的肝細胞癌中非常普遍。",
      "flashcard_front": "黃麴毒素 (Aflatoxin B1) / 肝細胞癌 / 抑癌基因突變 / codon 249",
      "flashcard_back": "黃麴毒素致癌機制主要是造成腫瘤抑制基因 TP53 的特異性突變（尤其是 codon 249）。",
      "flashcard_summary": "黃麴毒素與TP53 -> 黃麴毒素致癌主要造成 TP53 基因的特異性突變而失去抑癌能力。"
    },
    {
      "question_id": "110-1_medicine-2_081",
      "question_number": 81,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "造血系統惡性腫瘤中最常見的致癌基因活化染色體改變。",
      "explanation": "在造血系統惡性腫瘤（如白血病、淋巴瘤）中，最常見且具特異性的致癌基因活化機制是染色體轉位（translocation），例如慢性骨髓性白血病（CML）的 t(9;22) 形成 BCR-ABL 融合基因，或 Burkitt 淋巴瘤的 t(8;14) 導致 MYC 基因過度表現。基因缺失通常用於失活抑癌基因；基因擴增多見於實體癌；非整倍體雖常見但非特異性活化致癌基因的主要機制。",
      "flashcard_front": "造血系統腫瘤 / 致癌基因活化 / 染色體核型改變 / BCR-ABL / t(9;22)",
      "flashcard_back": "造血系統惡性腫瘤中最常見且特異性的致癌基因活化機制是染色體轉位(translocation)。",
      "flashcard_summary": "造血系統腫瘤核型改變 -> 染色體轉位(translocation)是造血系統腫瘤活化致癌基因最常見的機制。"
    },
    {
      "question_id": "110-1_medicine-2_082",
      "question_number": 82,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "乳糜胸的診斷特徵與淋巴管阻塞之病因。",
      "explanation": "胸水呈現乳白色混濁且含有高濃度三酸甘油脂，是典型「乳糜胸」（chylothorax）的表現。這主要是因為胸腔內的淋巴總管（胸管）受到外傷、手術破壞或因腫瘤（如淋巴瘤）引起淋巴管阻塞與破裂，使得富含乳糜微粒的淋巴液流入胸膜腔所致。心臟衰竭及下腔靜脈阻塞引起的胸水主要為漏出液，呈現清澈淡黃色且脂質含量低；肺梗塞則常引起滲出性或血色胸水。",
      "flashcard_front": "乳白色胸水 / 三酸甘油脂高 / 乳糜胸 / 淋巴管",
      "flashcard_back": "胸水呈乳白色且含高濃度三酸甘油脂代表乳糜胸，主因是淋巴管（胸管）阻塞或受損。",
      "flashcard_summary": "乳糜胸與淋巴阻塞 -> 乳白色高甘油三酯胸水為乳糜胸，常因淋巴管受損或阻塞所致。"
    },
    {
      "question_id": "110-1_medicine-2_083",
      "question_number": 83,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "退行性二尖瓣鈣化之病理受累位置與併發症。",
      "explanation": "退行性二尖瓣鈣化（mitral annular calcification）主要累及二尖瓣的環狀纖維支撐結構（即瓣環），而非瓣膜連合處（commissure，連合處鈣化與融合是風濕性心臟病的特徵），因此選項(A)為錯誤敘述。此退行性病變通常不影響瓣膜功能（少數人可見輕度逆流或狹窄），但鈣化的粗糙表面會使細菌易於附著，增加感染性心內膜炎的風險，也容易形成局部血栓並導致中風。",
      "flashcard_front": "退行性瓣膜鈣化 / 二尖瓣環 / 瓣膜連合處 / 感染性心內膜炎",
      "flashcard_back": "退行性二尖瓣鈣化主要影響瓣環而非瓣膜連合處；連合處鈣化融合是風濕性心臟病的特徵。",
      "flashcard_summary": "二尖瓣鈣化定位 -> 退行性二尖瓣鈣化主要發生在二尖瓣環而非二尖瓣連合處。"
    },
    {
      "question_id": "110-1_medicine-2_084",
      "question_number": 84,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "慢性免疫性血小板減少性紫斑症之抗體與骨髓特徵。",
      "explanation": "慢性免疫性血小板減少性紫斑症（ITP）的主要發病機制是患者血漿中產生了針對血小板膜醣蛋白（如 GPIIb/IIIa 或 GPIb/IX）的自體抗體，導致血小板在脾臟中被加速吞噬破壞。該病好發於育齡期（40歲以下）女性；骨髓切片中因補償性反應，巨核細胞（megakaryocytes）數量通常是正常或增加而非減少；臨床上，大多數患者對第一線的醣皮質素（類固醇）治療有良好的初期反應。",
      "flashcard_front": "慢性 ITP / 膜醣蛋白抗體 / 巨核細胞 (megakaryocytes) / 類固醇反應",
      "flashcard_back": "ITP 病人血漿中有針對血小板膜的自體抗體，骨髓切片中巨核細胞數量正常或增加。",
      "flashcard_summary": "ITP自體抗體與骨髓 -> ITP 由抗血小板自體抗體介導，骨髓內巨核細胞呈代償性正常或增加。"
    },
    {
      "question_id": "110-1_medicine-2_085",
      "question_number": 85,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "慢性淋巴球性白血病之細胞來源與免疫表現型。",
      "explanation": "慢性淋巴球性白血病（CLL）是一種 B 淋巴球（而非 T 淋巴球）的惡性腫瘤，典型表現為 CD19、CD20、CD5（原本是 T 細胞的標記，但在 CLL 中會異常表現）以及 CD23 的共同表現。該病好發於老年人（中位年齡約70歲），在20歲以下極為罕見。BCL2 的轉位 t(14;18) 是濾泡性淋巴瘤（follicular lymphoma）的特徵，雖然 CLL 會過度表現 BCL2，但其機制主要是 microRNA 缺失而非轉位。",
      "flashcard_front": "CLL / B細胞惡性腫瘤 / CD5與CD23表現 / BCL2轉位",
      "flashcard_back": "CLL 典型表現為 CD20、CD5 及 CD23 的共同表現；其 BCL2 過度表現非因轉位引起。",
      "flashcard_summary": "CLL免疫標記 -> CLL 為 B 細胞腫瘤，典型表現 CD20、CD5 及 CD23，BCL2 過度表現非轉位所致。"
    },
    {
      "question_id": "110-1_medicine-2_086",
      "question_number": 86,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "鼻咽癌病理分類與放射治療預後之關係。",
      "explanation": "鼻咽癌（NPC）中，角化型鱗狀上皮細胞癌（keratinizing type）與 EBV 的關聯性較低，且相較於非角化型（non-keratinizing type），它對放射治療的敏感性較差，預後也較為不良。選項A中 WHO 分類並不包含腺癌；選項B中 EBER-1 原位雜交偵測的是 EB 病毒轉錄的 RNA（EBER）而非 DNA；選項C中組織型態與患者的預後和治療敏感度高度相關。",
      "flashcard_front": "鼻咽癌 (NPC) / 角化型與非角化型 / 放射治療反應 / EBER原位雜交",
      "flashcard_back": "鼻咽癌中，角化型鱗狀上皮細胞癌對放射治療的敏感性較差，預後也比非角化型差。",
      "flashcard_summary": "鼻咽癌角化型預後 -> 鼻咽癌中角化型鱗狀細胞癌對放射治療敏感度較差，預後最差。"
    },
    {
      "question_id": "110-1_medicine-2_087",
      "question_number": 87,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "肺氣腫病理機制中釋放彈性蛋白酶之細胞源。",
      "explanation": "肺氣腫的發病機制中，主要是吸入的煙霧或污染物刺激肺部，招募並活化「嗜中性白血球」（neutrophils）及肺泡巨噬細胞，使其釋放大量的彈性蛋白酶（elastase）等蛋白水解酶。當體內的抗蛋白酶（如 alpha-1-antitrypsin）防禦機制不足以拮抗這些蛋白酶時，肺泡壁的彈性纖維（elastin）就會遭到破壞，導致肺泡腔異常擴張。其餘淋巴球或嗜酸性/嗜鹼性白血球並非釋放該破壞性彈性蛋白酶的主要來源。",
      "flashcard_front": "肺氣腫 (emphysema) / 彈性蛋白酶 (elastase) / 彈性纖維 (elastin) / 細胞來源",
      "flashcard_back": "破壞肺泡壁彈性纖維以致肺氣腫的彈性蛋白酶主要釋放自活化的嗜中性白血球。",
      "flashcard_summary": "肺氣腫蛋白酶來源 -> 破壞肺泡彈性纖維的彈性蛋白酶主要來自嗜中性白血球。"
    },
    {
      "question_id": "110-1_medicine-2_088",
      "question_number": 88,
      "correct_answer": "",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "原發性纖毛運動障礙與呼吸道慢性病變之因果關係。",
      "explanation": "本題官方公佈之更正答案為(A)或(B)皆給分。原發性纖毛運動障礙（PCD）患者因黏液纖毛清除功能異常，極易造成呼吸道黏液積聚與反覆感染，臨床上會引起慢性咳嗽與多痰等慢性支氣管炎(A)的表現；且長期的反覆發炎破壞支氣管壁結構，最典型且嚴重的後遺症即是引發支氣管擴張症(B)。氣喘與肺氣腫則非 PCD 的直接病理結果。",
      "flashcard_front": "原發性纖毛運動障礙 (PCD) / 黏液清除受損 / 支氣管擴張 / 慢性支氣管炎",
      "flashcard_back": "PCD 因黏液滯留與反覆感染，易引起慢性支氣管炎或進一步導致支氣管擴張。",
      "flashcard_summary": "PCD與肺部病變 -> PCD 常因黏液堆積與反覆感染，引起慢性支氣管炎與支氣管擴張。"
    },
    {
      "question_id": "110-1_medicine-2_089",
      "question_number": 89,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "常見肝炎病毒中唯一之 DNA 病毒。",
      "explanation": "在常見的肝炎病毒中，僅有B型肝炎病毒（HBV）屬於去氧核醣核酸（DNA）病毒（具部分雙股環狀 DNA 的 Hepadnaviridae 家族）。其餘如A型肝炎病毒（HAV，微小RNA病毒）、C型肝炎病毒（HCV，黃病毒家族）及D型肝炎病毒（HDV，缺陷型RNA病毒）均屬於核醣核酸（RNA）病毒。",
      "flashcard_front": "肝炎病毒 / DNA病毒 / 雙股環狀 / HAV / HBV / HCV / HDV",
      "flashcard_back": "常見肝炎病毒中，只有 B 型肝炎病毒(HBV)屬於 DNA 病毒，其餘皆為 RNA 病毒。",
      "flashcard_summary": "肝炎病毒核酸類型 -> B 型肝炎病毒是常見肝炎病毒中唯一的 DNA 病毒。"
    },
    {
      "question_id": "110-1_medicine-2_090",
      "question_number": 90,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "微生物免疫學",
      "category_confidence": "high",
      "key_point": "偽膜性腸炎之臨床診斷金標準。",
      "explanation": "偽膜性腸炎（pseudomembranous colitis）的診斷主要依據臨床症狀與大便中的艱難梭菌毒素（Toxin A and B）檢測（如 ELISA 或 PCR 檢測毒素基因），而非依靠耗時且敏感度較低的常規細菌培養，因此選項D為錯誤描述。該病通常因廣效性抗生素使用破壞腸道菌相平衡，導致艱難梭菌（C. difficile）異常繁殖並釋放毒素所致，病理特徵為黏膜表面覆蓋著由壞死細胞、黏液與嗜中性白血球構成的火山噴發狀「偽膜」。",
      "flashcard_front": "偽膜性腸炎 / 艱難梭菌 / 抗生素誘發 / 毒素檢測與細菌培養",
      "flashcard_back": "偽膜性腸炎的診斷主要依靠糞便毒素檢測(ELISA/PCR)，而非細菌培養。",
      "flashcard_summary": "偽膜性腸炎診斷 -> 偽膜性腸炎診斷主要依賴艱難梭菌毒素檢測，而非依靠細菌培養。"
    },
    {
      "question_id": "110-1_medicine-2_091",
      "question_number": 91,
      "correct_answer": "C",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "Lauren 分類中不同胃癌型別與幽門螺旋桿菌之關聯。",
      "explanation": "在 Lauren 分類法中，腸型胃癌（intestinal type）與環境因素（如高鹽飲食、抽煙）以及幽門螺旋桿菌（H. pylori）引起的慢性萎縮性胃炎與腸上皮化生有極密切的關聯；相較之下，瀰漫型胃癌（diffuse type）主要與遺傳突變（如 E-cadherin/CDH1 基因突變）相關，與幽門螺旋桿菌的關聯性較小，故選項C敘述為錯誤。胃癌在東亞（如日本）的發生率確實遠高於北美；特定促發炎因子（如 IL-1β、TNF）的基因多型性亦被證實會增加胃癌風險。",
      "flashcard_front": "胃癌 / 腸型與瀰漫型 / 幽門螺旋桿菌 / CDH1突變",
      "flashcard_back": "腸型胃癌與幽門螺旋桿菌感染關係密切；瀰漫型胃癌則主要與 CDH1 基因突變相關。",
      "flashcard_summary": "胃癌分類與幽門桿菌 -> 腸型胃癌與幽門螺旋桿菌感染高度相關，瀰漫型胃癌則主要與遺傳/CDH1突變相關。"
    }
  ]
}

# ==================== BATCH 007 ====================
batches_data["110-1_medicine-2_batch-007"] = {
  "dataset_id": "110-1_medicine-2",
  "batch_id": "110-1_medicine-2_batch-007",
  "items": [
    {
      "question_id": "110-1_medicine-2_092",
      "question_number": 92,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "外因性皮質醇增多症對腎上腺皮質結構之影響。",
      "explanation": "外因性皮質醇增多症（如長期服用外源性類固醇）會經由負回饋機制抑制下視丘分泌 CRH 與腦下垂體分泌 ACTH。缺乏 ACTH 的促腎上腺皮質作用後，會導致雙側腎上腺皮質出現萎縮（cortical atrophy），尤其是束狀帶和網狀帶。而雙側瀰漫性或結節性增生則是內因性 ACTH 依賴型庫欣氏病或異位 ACTH 症候群的病理特徵。",
      "flashcard_front": "外因性庫欣氏症候群 / 類固醇負回饋 / ACTH低下 / 腎上腺病理",
      "flashcard_back": "外因性皮質醇增多症因抑制 ACTH 分泌，會導致雙側腎上腺皮質出現萎縮。",
      "flashcard_summary": "外因性皮質醇與腎上腺 -> 外源性類固醇負回饋會抑制 ACTH，引發腎上腺皮質雙側萎縮。"
    },
    {
      "question_id": "110-1_medicine-2_093",
      "question_number": 93,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "黃色肉芽腫性腎盂腎炎之最常見致病原。",
      "explanation": "黃色肉芽腫性腎盂腎炎（xanthogranulomatous pyelonephritis, XGP）是一種罕見的慢性腎臟發炎，常伴隨尿路阻塞與反覆尿路感染。其最常見的致病菌為變形桿菌屬（Proteus mirabilis）和大腸桿菌（E. coli）。變形桿菌能產生尿素酶（urease）使尿液鹼化，極易導致鳥糞石（struvite）結石的形成，進一步加重尿路阻塞與 XGP 的病理進程。",
      "flashcard_front": "黃色肉芽腫性腎盂腎炎 / 尿路阻塞結石 / 最常見致病菌 / 變形桿菌",
      "flashcard_back": "黃色肉芽腫性腎盂腎炎(XGP)最常見的致病菌為變形桿菌屬(Proteus)與大腸桿菌。",
      "flashcard_summary": "XGP致病菌 -> 黃色肉芽腫性腎盂腎炎(XGP)最常見的致病菌為變形桿菌屬(Proteus)。"
    },
    {
      "question_id": "110-1_medicine-2_094",
      "question_number": 94,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "甲狀腺髓質癌之細胞來源與間質沉積特徵。",
      "explanation": "甲狀腺髓質癌（medullary thyroid carcinoma, MTC）起源於分泌降鈣素（calcitonin）的甲狀腺旁濾泡細胞（又稱 C 細胞，C-cells）。其病理切片上的典型特徵為腫瘤細胞釋放的降鈣素前驅物沉積在細胞間質中，形成局部的「類澱粉沉積」（amyloid deposits），在剛果紅染色下呈現蘋果綠雙折光。砂樣小體（psammoma bodies）則是甲狀腺乳頭狀癌（papillary thyroid carcinoma）的經典病理特徵。",
      "flashcard_front": "甲狀腺髓質癌 / 腫瘤細胞來源 / 間質沉積 / calcitonin",
      "flashcard_back": "甲狀腺髓質癌源於甲狀腺 C 細胞，典型病理表現為間質出現類澱粉沉積(amyloid deposits)。",
      "flashcard_summary": "甲狀腺髓質癌特徵 -> 甲狀腺髓質癌起源於 C 細胞，且腫瘤細胞間常有類澱粉沉積。"
    },
    {
      "question_id": "110-1_medicine-2_095",
      "question_number": 95,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "成人型顆粒細胞瘤之惡性度分類與臨床特性。",
      "explanation": "成人型顆粒細胞瘤（adult granulosa cell tumor）雖生長緩慢，但本質上被歸類為「具有低度惡性潛能」（low-grade malignant）的腫瘤，在診斷數年甚至數十年後仍可能發生復發或遠端轉移，因此描述其為良性腫瘤是不正確的。顆粒細胞瘤常因分泌大量動情激素而引發子宮內膜增生或異常出血；支持間質細胞瘤（Sertoli-Leydig cell tumor）則常分泌雄性素導致男性化特徵，且超過一半的患者有 DICER1 基因的體細胞突變。",
      "flashcard_front": "卵巢性索間質瘤 / 成人型顆粒細胞瘤 / 良惡性判斷 / 動情激素",
      "flashcard_back": "成人型顆粒細胞瘤並非良性腫瘤，而是被歸類為具有低度惡性潛能的腫瘤。",
      "flashcard_summary": "顆粒細胞瘤惡性度 -> 成人型顆粒細胞瘤為具有低度惡性潛能之腫瘤，而非單純良性。"
    },
    {
      "question_id": "110-1_medicine-2_096",
      "question_number": 96,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "結核、淋病與梅毒在睪丸及附睪侵犯順序之比較。",
      "explanation": "泌尿生殖系統結核（tuberculosis）感染在陰囊內通常是最先波及「附睪」（epididymis），隨後才可能蔓延至睪丸（testis）。因此，選項B敘述結核病引起之發炎最先起於睪丸是錯誤的。一般而言，附睪炎比睪丸炎更為常見，淋病引起的尿路逆行性感染也是最先影響附睪；而梅毒（syphilis）感染引起的睪丸炎（gumma 或間質發炎）則最先侵犯睪丸，附睪較少受累。",
      "flashcard_front": "睪丸與附睪發炎 / 結核病侵犯部位 / 淋病與梅毒 / 感染起源",
      "flashcard_back": "結核與淋病感染最先侵犯附睪；而梅毒與腮腺炎感染最先侵犯睪丸。",
      "flashcard_summary": "睪丸附睪炎起點比較 -> 結核與淋病感染先起於附睪，梅毒感染則先起於睪丸。"
    },
    {
      "question_id": "110-1_medicine-2_097",
      "question_number": 97,
      "correct_answer": "B",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "嬰幼兒最常見之睪丸生殖細胞腫瘤。",
      "explanation": "卵黃囊瘤（yolk sac tumor，又稱內胚竇瘤 endodermal sinus tumor）是嬰幼兒及三歲以下兒童最常見的睪丸生殖細胞腫瘤，在病理上常可見到經典的 Schiller-Duval bodies，且血清中的甲型胎兒蛋白（AFP）會顯著升高。精細胞瘤（seminoma）則多見於 30 至 40 歲的中年男性；絨毛癌與胚胎癌在幼兒期非常罕見。",
      "flashcard_front": "3歲以下小孩 / 最常見睪丸腫瘤 / Schiller-Duval bodies / AFP升高",
      "flashcard_back": "3歲以下小孩最常見的睪丸腫瘤為卵黃囊瘤(yolk sac tumor)；精細胞瘤多見於中年人。",
      "flashcard_summary": "幼兒睪丸腫瘤 -> 卵黃囊瘤為3歲以下幼兒最常見之睪丸生殖細胞腫瘤。"
    },
    {
      "question_id": "110-1_medicine-2_098",
      "question_number": 98,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "低惡性度骨肉瘤 12q13-q15 擴增所涉之抑癌與癌基因。",
      "explanation": "在低惡性度骨肉瘤（low-grade osteosarcoma）中，常見的染色體 12q13-q15 區域擴增包含了 MDM2 與 CDK4 基因，導致這兩個關鍵蛋白的過度表現（可用於與良性骨病變鑑別），而非 MYC（MYC 位於第 8 對染色體 8q24 區），故選項A為錯誤描述。原發性骨肉瘤在青少年中發病率最高，且遺傳性 TP53 突變（Li-Fraumeni 症候群）患者有極高的骨肉瘤風險，其確診的病理學金標準為觀察到惡性間質細胞直接產生類骨質（osteoid）。",
      "flashcard_front": "低惡性度骨肉瘤 / 12q13-q15 擴增 / MDM2 與 CDK4 / MYC",
      "flashcard_back": "低惡性度骨肉瘤之 12q13-q15 擴增包含 MDM2 與 CDK4 基因，不包含 MYC。",
      "flashcard_summary": "骨肉瘤基因擴增 -> 低惡性度骨肉瘤之 12q13-q15 擴增導致 MDM2/CDK4 過度表現，非 MYC。"
    },
    {
      "question_id": "110-1_medicine-2_099",
      "question_number": 99,
      "correct_answer": "A",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "阿茲海默症大腦核心之兩大病理特徵。",
      "explanation": "阿茲海默症（Alzheimer's disease）的兩大核心病理特徵為：由細胞外類澱粉樣蛋白（beta-amyloid）堆積形成的「老年斑/神經原斑」（neuritic plaques / senile plaques），以及在神經細胞內由過度磷酸化 Tau 蛋白形成的「神經原纖維纏結」（neurofibrillary tangles）。Nemaline rods 是線狀肌肉病變的特徵；Lewy bodies（路易氏體）則是巴金森氏症與路易氏體失智症的典型病理變化。",
      "flashcard_front": "阿茲海默症 / 類澱粉樣蛋白 / Tau蛋白磷酸化 / 大腦核心病理",
      "flashcard_back": "阿茲海默症兩大核心病理為細胞外的神經原斑(neuritic plaque)與細胞內的神經原纖維纏結(tangle)。",
      "flashcard_summary": "阿茲海默症病理 -> 阿茲海默症的核心病理變化為 neuritic plaque 與 neurofibrillary tangle。"
    },
    {
      "question_id": "110-1_medicine-2_100",
      "question_number": 100,
      "correct_answer": "D",
      "category_group": "醫學（二）",
      "category": "病理學",
      "category_confidence": "high",
      "key_point": "單純疱疹病毒腦炎之病理特徵與肉芽腫鑑別。",
      "explanation": "第一型單純疱疹病毒（HSV-1）腦炎是一種急性病毒性壞死性腦炎。在病理學上，可觀察到受病毒感染細胞核內的 Cowdry A 型核內包涵體、血管周圍有淋巴球浸潤呈袖套狀，以及微膠細胞增生形成的微膠細胞結節。而乾酪性壞死性肉芽腫（caseous necrotizing granuloma）是結核桿菌或某些真菌感染引起的慢性肉芽腫性發炎特徵，不會在急性病毒性腦炎中觀察到。",
      "flashcard_front": "HSV-1 腦炎 / 急性壞死 / Cowdry A 包涵體 / 乾酪性肉芽腫",
      "flashcard_back": "HSV-1 腦炎可見 Cowdry A 包涵體及微膠細胞結節，但不具乾酪性壞死性肉芽腫。",
      "flashcard_summary": "HSV-1腦炎病理 -> HSV-1 腦炎不具乾酪性壞死性肉芽腫，後者主要為結核或真菌感染特徵。"
    }
  ]
}

# Write output files and validate
output_dir = "reports/gemini_outputs"
os.makedirs(output_dir, exist_ok=True)

all_ok = True
validation_results = {}

for batch_id, data in batches_data.items():
    output_path = os.path.join(output_dir, f"{batch_id}.json")
    
    # Save the data directly as JSON (no markdown wrapper, raw format)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Wrote {output_path}")
    
    # Validation checks
    errors = []
    
    # Check outermost fields
    if data.get('dataset_id') != "110-1_medicine-2":
        errors.append("dataset_id mismatch")
    if data.get('batch_id') != batch_id:
        errors.append("batch_id mismatch")
        
    items = data.get('items', [])
    
    # Define allowed categories
    allowed_categories = ["微生物免疫學", "寄生蟲學", "藥理學", "病理學", "公共衛生學", "其他"]
    
    for i, item in enumerate(items):
        qid = item.get('question_id')
        qnum = item.get('question_number')
        
        # Verify no dataset_id or batch_id in item
        if 'dataset_id' in item or 'batch_id' in item:
            errors.append(f"item {i} (Q{qnum}) contains dataset_id or batch_id")
            
        required_fields = ['question_id', 'question_number', 'correct_answer', 'category_group', 'category', 'category_confidence', 'key_point', 'explanation', 'flashcard_front', 'flashcard_back', 'flashcard_summary']
        for field in required_fields:
            if not item.get(field) and field != 'correct_answer': # correct_answer can be empty string in Q88
                errors.append(f"item {i} (Q{qnum}) missing required field '{field}'")
            elif field == 'correct_answer' and item.get(field) is None:
                errors.append(f"item {i} (Q{qnum}) missing required field 'correct_answer'")
                
        # Check category
        cat = item.get('category')
        if cat not in allowed_categories:
            errors.append(f"item {i} (Q{qnum}) has invalid category: '{cat}'")
            
        # Check category confidence
        conf = item.get('category_confidence')
        if conf not in ['high', 'medium', 'low']:
            errors.append(f"item {i} (Q{qnum}) has invalid confidence: '{conf}'")
            
        # Check explanation length (2 to 5 sentences)
        exp = item.get('explanation', '')
        sentence_count = exp.count('。') + exp.count('？') + exp.count('！')
        if sentence_count < 2 or sentence_count > 5:
            print(f"Warning: {qid} explanation has {sentence_count} sentences: '{exp}'")
            
        # Check flashcard summary format (關鍵字 / 線索 -> 知識點 / 判斷規則)
        sum_str = item.get('flashcard_summary', '')
        if ' -> ' not in sum_str:
            errors.append(f"item {i} (Q{qnum}) flashcard_summary format mismatch: '{sum_str}'")
            
    if errors:
        all_ok = False
        validation_results[batch_id] = errors
    else:
        validation_results[batch_id] = ["OK"]

print("\n--- Validation Results ---")
for bid, res in validation_results.items():
    print(f"{bid}: {', '.join(res)}")
    
if all_ok:
    print("All batches processed and validated successfully!")
    sys.exit(0)
else:
    print("Validation failed!")
    sys.exit(1)
