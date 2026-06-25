import json
from pathlib import Path

updates = [
  {
    "question_id": "114-1_medicine-4_031",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "威爾森氏症（Wilson disease）的發病年齡與臨床症狀分布特徵（兒童期以肝臟表現為主）。",
    "explanation": "【題幹解析】\n本題考查威爾森氏症（Wilson's disease）的遺傳模式、致病基因、臨床表現及實驗室診斷指標。\n\n【選項詳解】\n- A. 錯誤。威爾森氏症在「10 歲以前發病（兒童期）」者，最常以「肝臟症狀」（如肝指數上升、慢性肝炎、肝硬化甚至急性肝衰竭）為首發或主要表現。而「神經學症狀」（如吞嚥困難、口齒不清、震顫等）通常要在「青少年期或成年早期（通常 > 10 歲，特別是 15 歲後）」發病者才較為常見，且癲癇在威爾森氏症的神經學表現中本就少見。\n- B. 正確。威爾森氏症屬於體染色體隱性遺傳疾病，致病原因為第 13 對染色體上的 ATP7B 基因突變，導致膽汁排銅功能障礙。\n- C. 正確。除神經精神系統受累外，肝臟受損（如慢性肝硬化、急性肝衰竭及因肝合成不足所致之凝血功能異常）是常見的神經學外表現。\n- D. 正確。血清藍斑蛋白（ceruloplasmin）濃度 < 20 mg/dL 支持診斷，但不能單憑其確立或排除。因為 ceruloplasmin 為急性期反應蛋白，在急性發炎、懷孕或服用雌激素時可能反應性升高而掩蓋病情；而嚴重蛋白流失或營養不良亦可能導致其偏低。\n\n【核心考點】\n威爾森氏症兒童期發病（<10歲）以肝臟表現為主，青少年/成人發病以神經學表現為主。致病基因為13對染色體上的ATP7B（隱性遺傳）。Ceruloplasmin受多種後天因素影響，需綜合評估。",
    "flashcard_front": "威爾森氏症(Wilson) / 兒童期發病特徵 / 基因與染色體 / 藍斑蛋白限制",
    "flashcard_back": "兒童期(<10歲)發病以肝臟症狀為主，青少年期後才以神經症狀為主；致病基因為第13對染色體上的ATP7B；藍斑蛋白易受發炎或懷孕影響而升高。",
    "flashcard_summary": "威爾森氏症發病特徵 -> 10歲前以肝臟表現為主，青少年後以神經學為主；基因在13p(ATP7B)。"
  },
  {
    "question_id": "114-1_medicine-4_032",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "兒科急診初步評估（PAT）內容、低血壓下限標準與急救處置順序。",
    "explanation": "【題幹解析】\n本題考查小兒高級生命支持（PALS）的評估指引，包括兒童評估三角（PAT）、低血壓判定標準及急救優先順序。\n\n【選項詳解】\n- A. 錯誤。初步評估的「兒童評估三角（PAT）」著重於視覺與聽覺的外觀快速評估，其三要素為：外觀（Appearance）、呼吸功（Work of breathing）與皮膚循環（Circulation to skin）。呼吸道（Airway）、呼吸（Breathing）、循環（Circulation）是屬於「初級評估（Primary assessment）」的 ABCDE 流程。\n- B. 錯誤。若 PAT 評估發現病童處於心肺衰竭或休克等危急狀態，必須立即給予生命支持與搶救（如插管、給氧、建立點滴），絕不能等做完初、次、三級評估後才進行緊急處理。\n- C. 正確。根據 PALS 指引，1 歲以上兒童低血壓（收縮壓最低標準下限）定義為：1-10 歲低於「70 mmHg + 年齡(歲) × 2」，10 歲以上低於 90 mmHg。故收縮壓最低標準需高於或等於此公式值。\n- D. 錯誤。次級評估（Secondary assessment）包括焦點式病史詢問（SAMPLE 記憶法）及詳細身體診察。三級評估（Tertiary assessment）則指實驗室與影像學檢查。\n\n【核心考點】\nPALS初級評估中1-10歲低血壓下限為 70 + 2×年齡，10歲以上為90 mmHg。PAT要素為外觀、呼吸功、皮膚循環。急救處理應在發現危急時立即進行。",
    "flashcard_front": "兒科低血壓定義 / PALS初級評估 SBP 下限公式 / 1-10歲與10歲以上",
    "flashcard_back": "1-10歲收縮壓下限為「70 + 年齡×2」mmHg，10歲以上為90 mmHg，低於此值即為低血壓（Hypotension）。",
    "flashcard_summary": "兒科低血壓定義 -> 1-10歲 SBP 下限為 70+2*年齡；10歲以上為 90 mmHg。"
  },
  {
    "question_id": "114-1_medicine-4_033",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "遺傳諮詢的臨床指引適應症辨識。",
    "explanation": "【題幹解析】\n本題考查需要接受產前或遺傳諮詢的臨床適應症。遺傳諮詢主要針對具遺傳性病因風險、染色體異常風險、或先天畸形風險的患者。\n\n【選項詳解】\n- A. 需要。35 歲以上高齡孕婦，胎兒染色體異常（如 Trisomy 21）的發生率隨年齡顯著上升，是產前遺傳諮詢與篩檢的強適應症。\n- B. 需要。上一胎有先天性異常的父母，為評估該異常是否具遺傳性及評估下一胎的再發風險（recurrence risk），需要進行遺傳諮詢。\n- C. 需要。經歷重複流產（習慣性流產）的婦女，染色體異常（如夫妻平衡易位）是常見原因，雙方應進行遺傳諮詢與核型分析。\n- D. 最不需要。缺鐵性貧血（Iron deficiency anemia）是後天營養攝取不足、吸收不良或慢性失血（如月經過多）所致的疾病，不具遺傳性，最不需要遺傳諮詢。\n\n【核心考點】\n遺傳諮詢適用於高齡產婦（>=35歲）、重複流產、前胎先天畸形、已知家族遺傳病等情況。缺鐵性貧血為後天營養或失血性疾病，無遺傳諮詢指徵。",
    "flashcard_front": "遺傳諮詢 / 臨床指引適應症 / 排除非遺傳疾病",
    "flashcard_back": "高齡產婦(>=35歲)、前胎畸形、習慣性流產均需遺傳諮詢；後天營養性/失血性疾病（如缺鐵性貧血）不需要。",
    "flashcard_summary": "遺傳諮詢指徵 -> 高齡產婦、重複流產、前胎畸形需要；缺鐵性貧血不需要。"
  },
  {
    "question_id": "114-1_medicine-4_034",
    "category": "皮膚科",
    "category_confidence": "high",
    "key_point": "多型性紅斑（Erythema multiforme）的靶心狀皮疹與多黏膜受累特徵。",
    "explanation": "【題幹解析】\n30歲女性，軀幹四肢出現「靶心狀（targetoid/target）病灶」與水疱，並合併多個黏膜受累（口腔糜爛、眼結膜紅腫、會陰部糜爛），為典型重型多型性紅斑（Erythema multiforme major）的表現。\n\n【選項詳解】\n- A. 最有可能。靶心狀紅斑（Target lesion）是多型性紅斑（Erythema multiforme, EM）的病理特徵。當 EM 侵犯多處黏膜時，稱為重型多型性紅斑（EM major），典型症狀包括眼、口、生殖器黏膜破裂與糜爛。\n- B. 不可能。二期梅毒皮疹雖然形態多樣（斑丘疹常見於手掌腳底），但不會表現為典型靶心狀水疱，且不常伴隨多個黏膜嚴重的急性糜爛與眼結膜紅腫。\n- C. 不可能。汗疱疹（Pompholyx）為好發於手掌、腳掌與指側的深在性小水疱，不會分布於軀幹，亦不會引起黏膜糜爛。\n- D. 不可能。結節性紅斑（Erythema nodosum）是一種主要發生在雙側小腿前側、有壓痛的紅色皮下結節，不伴有靶心狀皮疹與黏膜受累。\n\n【核心考點】\n靶心狀皮疹（targetoid lesions）是多型性紅斑（EM）的特異性診斷特徵；重型多型性紅斑（EM major）常伴隨口、眼、外生殖器等多處黏膜受累。",
    "flashcard_front": "靶心狀紅斑 / 多處黏膜糜爛(口、眼、會陰) / 最可能診斷",
    "flashcard_back": "最可能為多型性紅斑(erythema multiforme)，尤其是重型(EM major)，其特徵為四肢軀幹靶心狀病灶伴隨多黏膜糜爛。",
    "flashcard_summary": "多型性紅斑 -> 靶心狀病灶伴隨多處黏膜（口、眼、會陰）糜爛。"
  },
  {
    "question_id": "114-1_medicine-4_035",
    "category": "皮膚科",
    "category_confidence": "high",
    "key_point": "乾癬（Psoriasis）核心免疫機制（Th17/Th23 軸）與無效標靶細胞激素辨識。",
    "explanation": "【題幹解析】\n乾癬（Psoriasis）的核心病理生理機制為 Th17/Th22 細胞介導的自體免疫發炎反應，其最重要的細胞激素軸為 IL-23 / IL-17 軸，且 TNF-α 在其中扮演關鍵的促炎增強角色。\n\n【選項詳解】\n- A. 有效。TNF-α 為乾癬斑塊形成的重要上游促炎細胞激素，抗 TNF-α 單株抗體（如 Adalimumab）在乾癬治療中被廣泛應用且療效明確。\n- B. 有效。IL-17A 是 Th17 細胞分泌的核心致病細胞激素，抗 IL-17A 生物製劑（如 Secukinumab, Ixekizumab）是目前治療中重度乾癬效果最優異的藥物之一。\n- C. 無效。IL-4 是引導 Th2 細胞分化的重要細胞激素，主要參與第二型過敏發炎反應（如異位性皮膚炎，異位性皮膚炎的治療藥物 Dupilumab 即阻斷 IL-4/IL-13 途徑）。乾癬屬於 Th1/Th17 介導的發炎反應，阻斷 IL-4 無法有效治療乾癬，甚至可能誘發乾癬樣皮疹。\n- D. 有效。IL-23 負責維持 Th17 細胞的生存與活化，抗 IL-23 p19 單株抗體（如 Guselkumab）能有效阻斷乾癬的致病瀑布反應。\n\n【核心考點】\n乾癬的發炎反應由 Th1/Th17 途徑驅動，關鍵細胞激素包括 TNF-α、IL-23、IL-17A。IL-4 是 Th2 途徑的細胞激素，主要與異位性皮膚炎相關，阻斷它對乾癬無效。",
    "flashcard_front": "乾癬(Psoriasis) / 標靶治療生物製劑 / 關鍵細胞激素與無效因子",
    "flashcard_back": "乾癬由Th17/IL-23軸介導，阻斷TNF-a、IL-23或IL-17A均有效；IL-4屬於Th2免疫反應，阻斷IL-4對乾癬治療無效。",
    "flashcard_summary": "乾癬標靶細胞激素 -> 阻斷TNF-a/IL-23/IL-17A有效；阻斷IL-4無效。"
  },
  {
    "question_id": "114-1_medicine-4_036",
    "category": "皮膚科",
    "category_confidence": "high",
    "key_point": "脂漏性皮膚炎的加重因素（HIV、帕金森氏症）與頑固性病例的鑑別診斷（乾癬）。",
    "explanation": "【題幹解析】\n本題考查脂漏性皮膚炎（Seborrheic dermatitis）的病因、系統性伴隨疾病及臨床鑑別診斷。\n\n【選項詳解】\n- A. 錯誤。脂漏性皮膚炎的病因與皮膚共生真菌——皮屑芽孢菌（Malassezia furfur，舊稱 Pityrosporum ovale）的代謝產物刺激以及宿主免疫反應高度相關。\n- B. 錯誤。HIV 感染（愛滋病）患者常出現極為嚴重、廣泛且對治療反應差的脂漏性皮膚炎，這常是 HIV 感染的重要皮膚指標。\n- C. 正確。乾癬（Psoriasis）在早期侵犯頭皮或臉部時，外觀極像脂漏性皮膚炎。若遇到極難控制、臨床治療反應不佳的脂漏性皮膚炎患者，臨床醫師必須高度警惕其是否可能為潛在的乾癬（或稱為乾癬樣脂漏性皮炎 sebopsoriasis）。\n- D. 錯誤。帕金森氏症（Parkinson's disease）等神經系統疾病患者，常因皮脂分泌過度或自主神經調節異常，顯著加重脂漏性皮膚炎的嚴重度。\n\n【核心考點】\n脂漏性皮膚炎與馬拉色菌（Malassezia）增殖及免疫反應相關；HIV與帕金森氏症均會顯著加重其症狀。頑固難治的脂漏性皮膚炎需鑑別診斷乾癬。",
    "flashcard_front": "脂漏性皮膚炎 / 馬拉色菌 / 加重因(HIV、帕金森) / 頑固型鑑別診斷",
    "flashcard_back": "馬拉色菌參與其發病；HIV與帕金森氏症會加重病情；難以控制的頑固型病患需考慮乾癬的可能性。",
    "flashcard_summary": "脂漏性皮膚炎 -> 馬拉色菌參與發病；HIV/帕金森會加重；頑固病例需排除乾癬。"
  },
  {
    "question_id": "114-1_medicine-4_037",
    "category": "皮膚科",
    "category_confidence": "high",
    "key_point": "皮膚病毒感染（Parvovirus B19、VZV、Enterovirus、HPV）的臨床特徵與疫苗突破性感染。",
    "explanation": "【題幹解析】\n本題考查常見皮膚病毒感染的病因、傳播途徑與疫苗保護力的局限性。\n\n【選項詳解】\n- A. 正確。感染性紅斑（Erythema infectiosum，又稱第五病）由人類微小病毒 B19（Parvovirus B19）感染引起，典型特徵為臉部出現如被掌摑的紅疹（slapped cheek）。\n- B. 錯誤。水痘疫苗（Varicella vaccine）雖然保護效力佳，但並非 100% 免疫。接種過水痘疫苗的個案仍可能發生「突破性感染（breakthrough infection）」而長出水痘，只是其臨床症狀（水疱數、發燒、病程）通常較未接種者輕微得多。\n- C. 正確。手足口病（Hand-foot-mouth disease）主要由腸病毒（如 CVA16, EV71）引起，其主要傳播方式為經由糞口途徑，或飛沫、接觸病灶分泌物傳染。\n- D. 正確。生殖器疣（尖圭濕疣/菜花）主要由低危險型人類乳突病毒 HPV-6 和 HPV-11 感染所致（佔 90% 以上）。\n\n【核心考點】\n接種水痘疫苗後仍有發生突破性感染而長水痘的可能。Parvovirus B19 引起 slapped cheek 臉部紅疹。手足口病主要經糞口傳播。尖圭濕疣主因為 HPV-6, 11 感染。",
    "flashcard_front": "皮膚病毒感染 / 水痘疫苗突破性感染 / 微小病毒B19 / 尖圭濕疣病原",
    "flashcard_back": "接種水痘疫苗後仍可能發生VZV突破性感染而長水痘；Parvovirus B19造成臉部被掌摑樣紅疹；尖圭濕疣主因為HPV-6, 11。",
    "flashcard_summary": "皮膚病毒感染 -> 水痘疫苗打後仍可有突破性感染；Parvovirus B19致slapped cheek；尖圭濕疣為HPV-6, 11。"
  },
  {
    "question_id": "114-1_medicine-4_038",
    "category": "皮膚科",
    "category_confidence": "high",
    "key_point": "凹陷性角質溶解症（Pitted keratolysis）的臨床表現（穿靴、腳臭、凹陷小孔）與致病菌。",
    "explanation": "【題幹解析】\n25歲年輕士兵，因長期穿著不透氣軍靴，腳底潮濕悶熱，臨床表現為腳底散發惡臭，且腳掌壓力承受處（如前腳掌、腳跟）出現許多密集、多孔狀、火山口樣的圓形凹陷小孔（pitted erosions），此為經典的凹陷性角質溶解症（Pitted keratolysis）。\n\n【選項詳解】\n- A. 錯誤。足癬（香港腳）由皮癬菌（黴菌）感染引起，主要表現為趾縫糜爛脫皮、水疱或腳底角化脫屑，常伴劇癢，但無密集的細小角質層凹陷小孔，且惡臭程度不像本病特異。\n- B. 錯誤。異汗性濕疹（汗疱疹）是發生在手掌、腳掌或指側的深在性小水疱，乾涸後脫皮，無密集小孔與細菌性臭味。\n- C. 正確。凹陷性角質溶解症是因微小棒狀桿菌（Corynebacterium）、Kytococcus sedentarius 等細菌在潮濕悶熱的足底過度繁殖，產生蛋白分解酶溶解足底角質層，使角質層出現多個小凹陷孔洞，並釋放含硫化合物產生嚴重惡臭。治療上應使用外用抗生素（如 Clindamycin, Erythromycin 藥膏）及保持乾燥。\n- D. 錯誤。掌蹠膿疱症表現為反覆發作、無菌性的掌蹠部膿疱，伴隨結痂與脫皮，不表現為角質溶解之細小孔洞。\n\n【核心考點】\n凹陷性角質溶解症（Pitted keratolysis）的特徵是長期穿包鞋、腳部潮濕、極度惡臭，且足底出現密集圓形角質溶解小孔。致病菌為棒狀桿菌等細菌，首選外用抗生素治療。",
    "flashcard_front": "穿軍靴 / 腳底極臭 / 密集圓形凹陷小孔 / 最可能診斷與治療",
    "flashcard_back": "診斷為凹陷性角質溶解症(pitted keratolysis)，細菌分解角質所致，治療需使用外用抗生素(如 Clindamycin)並保持足部乾燥。",
    "flashcard_summary": "凹陷性角質溶解症 -> 長期穿靴、腳臭、足底密集凹陷小孔；治療使用外用抗生素。"
  },
  {
    "question_id": "114-1_medicine-4_039",
    "category": "皮膚科",
    "category_confidence": "high",
    "point": "增加皮膚鱗狀上皮細胞癌（SCC）風險的遺傳性症候群辨識。",
    "explanation": "【題幹解析】\n某些遺傳性症候群因 DNA 修復障礙或黑色素防禦功能缺失，在暴露於紫外線時極易發生 DNA 損傷累積，進而使皮膚鱗狀細胞癌（SCC）、基底細胞癌（BCC）及黑色素瘤的風險大幅增加。\n\n【選項詳解】\n- A. 增加。著色性乾皮症（Xeroderma pigmentosum, XP）是因核苷酸切除修復（NER）路徑缺陷導致無法修復 UV 引起的 DNA 損傷，患者在童年起即極易多發皮膚癌（包括 SCC）。\n- B. 增加。韋爾納症候群（Werner syndrome）為 WRN 基因（解旋酶）突變所致之早衰症，基因組不穩定性大幅升高，患者發生 SCC 等惡性上皮腫瘤的風險顯著高於常人。\n- C. 不包括。史特基–韋伯氏症候群（Sturge-Weber syndrome）是一種先天性神經皮膚血管瘤病（面部葡萄酒色斑、軟腦膜血管瘤、青光眼），屬於毛細血管血管畸形疾病，並不會增加皮膚鱗狀細胞癌（SCC）的風險。\n- D. 增加。眼皮膚白化症（Oculocutaneous albinism, OCA）因黑色素合成障礙，皮膚完全缺乏黑色素對紫外線的屏障與保護，極易發生日光性損傷並誘發皮膚鱗狀細胞癌。\n\n【核心考點】\n著色性乾皮症、眼皮膚白化症及 Werner 症候群均因 DNA 修復受損或光防禦缺乏而顯著增加皮膚鱗狀細胞癌（SCC）風險。Sturge-Weber 症候群為毛細血管畸形病變，不增加皮膚癌風險。",
    "flashcard_front": "遺傳性症候群 / 皮膚鱗狀細胞癌(SCC)風險 / 著色性乾皮症 vs Sturge-Weber",
    "flashcard_back": "著色性乾皮症、白化症因修復DNA障礙或缺黑色素使SCC風險暴增；Sturge-Weber為毛細血管畸形症候群，不增加皮膚癌風險。",
    "flashcard_summary": "皮膚SCC高風險症候群 -> 著色性乾皮症/白化症/Werner增加 risk；Sturge-Weber不增加。"
  },
  {
    "question_id": "114-1_medicine-4_040",
    "category": "皮膚科",
    "category_confidence": "high",
    "key_point": "蕈狀肉芽腫（Mycosis fungoides）的臨床病程（斑塊到結節/腫瘤期）與表皮趨向性（epidermotropism）病理特徵。",
    "explanation": "【題幹解析】\n55歲中老年男性，兩年內軀幹四肢陸續出現無症狀紅色斑塊伴輕度脫屑，KOH黴菌檢查陰性，近期部分病灶形成結節。皮膚切片病理顯示表皮內有許多異型細胞浸潤（表皮趨向性 epidermotropism）。此為原發皮膚 T 細胞淋巴瘤中最常見的「蕈狀肉芽腫（Mycosis fungoides, MF）」的典型表現。\n\n【選項詳解】\n- A. 最有可能。蕈狀肉芽腫（MF）臨床病程慢，會經歷紅斑期（patch）、斑塊期（plaque）到結節/腫瘤期（tumor）。其病理特徵是 CD4+ 輔助 T 細胞表現出表皮趨向性（epidermotropism），浸潤表皮並可形成普特里埃微膿瘍（Pautrier microabscess）。\n- B. 錯誤。類肉瘤（Sarcoidosis）的皮膚切片特徵是真皮層內出現「非乾酪樣壞死肉芽腫（non-caseating granuloma）」，主要由上皮樣組織細胞和巨細胞構成，無異型淋巴球表皮浸潤。\n- C. 錯誤。蟹足腫（Keloid）為真皮內膠原纖維（主要是 I 型和 III 型）大量增生及排列紊亂，無細胞異型性與上皮浸潤。\n- D. 錯誤。結節性癢疹（Prurigo nodularis）為反覆搔抓引起的表皮顯著增厚與表皮下神經增生，無表皮內異型 T 淋巴球浸潤。\n\n【核心考點】\n蕈狀肉芽腫（Mycosis fungoides）是皮膚 T 細胞淋巴瘤，病程包含斑塊與結節期；病理具特異性的表皮趨向性（epidermotropism，非典型淋巴球浸潤表皮）。",
    "flashcard_front": "慢性紅斑脫屑 / 黴菌陰性 / 形成結節 / 表皮內見異型淋巴球浸潤(epidermotropism) / 最可能診斷",
    "flashcard_back": "最可能為蕈狀肉芽腫(mycosis fungoides)，是皮膚T細胞淋巴瘤，病理特徵為非典型T淋巴球浸潤表皮形成Pautrier微膿瘍。",
    "flashcard_summary": "蕈狀肉芽腫 -> 慢性斑塊結節；病理可見異型淋巴球侵犯表皮(epidermotropism)。"
  }
]

out_dir = Path("scratch")
out_dir.mkdir(parents=True, exist_ok=True)
Path("scratch/updates_1141_med4_batch4.json").write_text(json.dumps(updates, ensure_ascii=False, indent=2), encoding="utf-8")
print("Batch 4 updates generated.")
