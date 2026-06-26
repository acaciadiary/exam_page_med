import sys
sys.path.append("scratch")
from apply_updates import apply

updates = [
  {
    "id": "111-2_medicine-6_021",
    "category": "耳鼻喉科",
    "key_point": "巴特氏額頭膨腫（Pott's puffy tumor）的病因與早期臨床表徵。",
    "explanation": "【題幹解析】\n本題考查巴特氏額頭膨腫（Pott's puffy tumor）的病理生理機制與臨床表現特徵。解答此題需要了解該併發症所侵犯的解剖構造、好發族群及臨床特點。\n\n【選項詳解】\n- A. 病因是篩骨(ethmoid bone)的骨膜下膿瘍(subperiosteal abscess)及骨髓炎(osteomyelitis)：錯誤。巴特氏額頭膨腫的病因主要是「額竇炎（frontal sinusitis）」擴散，引發「額骨（frontal bone）」的骨髓炎及額骨前壁骨膜下膿瘍，而非篩骨。\n- B. 常侵犯老年人：錯誤。Pott's puffy tumor 好發於「青少年與年輕族群」，這與此年齡段額竇正在快速發育、血流供應豐富以及前額部板障靜脈（diploic veins）血栓性靜脈炎易於擴散有關，老年人反而罕見。\n- C. 常侵犯具有自體免疫性疾病(autoimmune disease)的病人：錯誤。此病主要是額竇感染擴散所致的急性/亞急性併發症，並非與自體免疫性疾病有特異性強相關，任何健康的青少年在罹患嚴重額竇炎時皆可能發生。\n- D. 早期症狀可能只有輕微的局部軟組織硬化(induration)：正確。在疾病早期，可能僅表現為額部皮膚輕微的發紅、腫脹與局部軟組織硬化（induration）或波動感，容易被誤認為一般的軟組織蜂窩性組織炎，若未及時行影像學檢查（如頭部 CT），極易延誤診斷。\n\n【核心考點】\n巴特氏額頭膨腫（Pott's puffy tumor）之病理定位（額骨骨髓炎伴骨膜下膿瘍，非篩骨）、好發族群（青少年）及早期隱匿的臨床症狀（局部軟組織硬化）。",
    "flashcard_front": "巴特氏額頭膨腫 (Pott's puffy tumor) / 額骨骨髓炎 / 額竇炎 / 青少年 / 軟組織硬化",
    "flashcard_back": "Pott's puffy tumor 是額竇炎擴散引起的「額骨」骨髓炎與骨膜下膿瘍，好發於青少年，早期可能僅有輕微額部軟組織硬化。",
    "flashcard_summary": "Pott's puffy tumor 定位與好發 -> 額骨骨髓炎（非篩骨） & 青少年 & 早期軟組織硬化"
  },
  {
    "id": "111-2_medicine-6_022",
    "category": "耳鼻喉科",
    "key_point": "過敏性鼻炎（Allergic Rhinitis）的第一線治療藥物與免疫治療（減敏治療）的臨床定位。",
    "explanation": "【題幹解析】\n本題考查過敏性鼻炎（allergic rhinitis）的藥物治療指引。題目詢問下列何者「不屬於」第一線選項。解題關鍵在於區分一般症狀控制藥物與特異性免疫療法（減敏療法）的臨床定位。\n\n【選項詳解】\n- A. 抗組織胺(antihistamine)：屬於第一線（非本題答案）。口服第二代抗組織胺或鼻噴抗組織胺是控制流鼻水、打噴嚏與眼癢的經典第一線藥物。\n- B. 去充血劑(decongestant)：屬於第一線（非本題答案）。口服去充血劑（如 pseudoephedrine）或局部去充血劑鼻噴劑（如 oxymetazoline，但需限制連續使用在3–5天內以防藥物性鼻炎）是快速緩解嚴重鼻塞的第一線藥物。\n- C. 類固醇鼻噴劑(intranasal steroid)：屬於第一線（非本題答案）。新型類固醇鼻噴劑是目前過敏性鼻炎「最有效」的控制藥物，能全面緩解包括鼻塞、流鼻水、打噴嚏在內的所有症狀，為第一線首選。\n- D. 免疫治療(immunotherapy)：不屬於第一線（為本題答案）。特異性免疫治療（減敏治療，包括皮下注射 SCIT 或舌下含服 SLIT）療程極長（通常需3–5年），且存在引發嚴重全身性過敏反應（anaphylaxis）的風險，因此臨床上僅保留給對第一線藥物治療反應不佳、無法耐受藥物副作用或合併嚴重氣喘的特定病人，不作為第一線常規選項。\n\n【核心考點】\n過敏性鼻炎藥物治療指引：第一線藥物包括類固醇鼻噴劑、抗組織胺及去充血劑；減敏免疫療法為二線或後線特殊治療。",
    "flashcard_front": "過敏性鼻炎治療 / 第一線藥物 / 類固醇鼻噴劑 / 減敏治療 (Immunotherapy)",
    "flashcard_back": "類固醇鼻噴劑、抗組織胺及去充血劑為過敏性鼻炎的第一線治療；免疫治療（減敏）因療程長且有過敏風險，列為後線。",
    "flashcard_summary": "過敏性鼻炎治療分級 -> 類固醇鼻噴劑/抗組織胺為一線；免疫療法為後線"
  },
  {
    "id": "111-2_medicine-6_023",
    "category": "耳鼻喉科",
    "key_point": "鼻出血（Epistaxis）的解剖學特徵與緊急處置原則（壓迫前鼻中隔）。",
    "explanation": "【題幹解析】\n題幹詢問關於流鼻血（epistaxis）的治療處置，何者最為適當。需要結合鼻腔出血的常見解剖位置（Kiesselbach's plexus）與標準物理加壓止血的手法。\n\n【選項詳解】\n- A. 加壓鼻骨(nasal bone)處10~15 分鐘：錯誤。鼻骨位於鼻樑上段，為硬質骨性構造，而九成以上的流鼻血源自鼻腔前下方的軟骨部（鼻中隔前下區）。壓迫硬骨無法對出血點產生壓迫效果。\n- B. 膠原蛋白凝膠基質(collagen gel matrix)或氧化纖維素(oxidized cellulose)敷料對控制出血無效益：錯誤。這些屬於生物可吸收性填塞物，能促進血小板聚集與凝血反應，對於控制局部小血管出血及避免撕裂粘膜極有臨床效益。\n- C. 加壓前鼻中隔(anterior nasal septum)或鼻填塞(nasal packing)：正確。超過 90% 的鼻出血發生於前鼻中隔的 Kiesselbach's plexus（Little's area）。最基本且有效的止血手法是捏住兩側鼻翼軟骨（即壓迫前鼻中隔）並使頭微前傾，加壓 10–15 分鐘。若無法止血，則可給予前鼻填塞（nasal packing）。\n- D. 前篩動脈結紮(anterior ethmoidal artery ligation)：錯誤。動脈結紮手術（包括前篩動脈或蝶腭動脈結紮）屬於侵入性治療，僅在反覆嚴重出血、多輪鼻填塞失敗後才考慮的後線手術選項。\n\n【核心考點】\n流鼻血之好發部位（Kiesselbach's plexus）與第一線物理壓迫止血手法（捏兩側鼻翼軟骨壓迫前鼻中隔，非壓迫鼻骨）。",
    "flashcard_front": "流鼻血 (Epistaxis) / 壓迫止血部位 / 鼻中隔前下區 (Kiesselbach's plexus) / 前鼻填塞",
    "flashcard_back": "九成流鼻血源自 Kiesselbach's plexus，止血應加壓兩側鼻翼（前鼻中隔）10-15分鐘，非加壓鼻骨。",
    "flashcard_summary": "流鼻血處置 -> 加壓前鼻中隔（捏鼻翼），非壓鼻骨"
  },
  {
    "id": "111-2_medicine-6_024",
    "category": "耳鼻喉科",
    "key_point": "原因不明之聲門下狹窄（iSGS）的臨床特點與病理爭議（雌激素受體與胃蛋白酶之探討）。",
    "explanation": "【題幹解析】\n本題考查成人原因不明之聲門下狹窄（idiopathic subglottic stenosis, iSGS）的病生理機制與臨床特徵。由於該疾病在學術界的致病機轉（特別是女性荷爾蒙受體與胃食道逆流的關聯性）研究結論不一，考選部更正此題為「一律給分」。以下詳解各選項涉及的醫學概念與學術現況。\n\n【選項詳解】\n- A. 多發生於生育年齡層之女性：臨床特徵。iSGS 的一項顯著流行病學特點是：幾乎排他性地發生於女性，特別是生育年齡層的女性（約占 95% 以上），且患者通常無氣管插管、外傷或系統性自體免疫疾病史。\n- B. 與女性荷爾蒙相關,在聲門下檢體中可發現有較多的雌激素受體(estrogen receptor)：爭議點。由於該病極度好發於生育期女性，部分假說認為女性荷爾蒙（如雌激素）在異常纖維增生中扮演核心角色，且有研究報導聲門下狹窄組織中存有雌激素受體（ER）的表達；然而，後續亦有其他研究未能重複此發現，故此點在學術上仍有爭議。\n- C. 與逆流性咽喉炎(laryngopharyngeal reflux)相關：爭議點。許多學者推測，胃酸與胃蛋白酶的反覆微量吸入刺激是引發黏膜發炎與瘢痕化狹窄的慢性誘因（即咽喉逆流 LPR）。\n- D. 在病人的聲門下瘢痕組織中有可能檢出胃蛋白酶(pepsin)：爭議點。為支持 LPR 假說，部分研究確實在狹窄瘢痕組織中檢測出胃蛋白酶（pepsin），但也有些研究未能證實胃蛋白酶的特異性致病作用。\n\n【核心考點】\n原因不明聲門下狹窄（iSGS）之高度女性好發性，以及學術界對其可能與女性荷爾蒙（ER受體）及咽喉逆流（胃蛋白酶 pepsin）相關之致病機轉爭議。",
    "flashcard_front": "原因不明聲門下狹窄 (iSGS) / 好發族群 / 雌激素受體 / 胃蛋白酶 / 咽喉逆流",
    "flashcard_back": "iSGS 極度好發於生育期女性；其致病機轉是否與女性荷爾蒙（ER）及胃食道逆流（胃蛋白酶）具因果關係，在學術上仍存有爭議（本題一律給分）。",
    "flashcard_summary": "iSGS 病因爭議 -> 好發於生育期女性，女性荷爾蒙與逆流機轉仍有爭議"
  },
  {
    "id": "111-2_medicine-6_025",
    "category": "耳鼻喉科",
    "key_point": "早期喉癌（T1, T2）的手術（雷射切除）與放射線治療效果與喉保存率比較。",
    "explanation": "【題幹解析】\n題幹針對早期喉癌（T1, T2 期，主要是聲帶癌）的兩種主要治療方式——經口雷射微創手術（Transoral laser microsurgery, TLM）與放射線治療（Radiation therapy, RT）進行比較，並詢問何者敘述錯誤。\n\n【選項詳解】\n- A. 放射線治療所需要的時間較長,成本也較手術治療為高：正確。放射線治療通常需要每日照射、連續進行 6 至 7 週（約 30–35 次療程），時間跨度長，且放療設備與多次就醫的累積醫療成本普遍高於一次性的局部微創手術。\n- B. 就局部腫瘤的控制,或治癒率、存活率而言,兩種治療方式不相上下：正確。多項大型臨床研究證實，對於 T1 及 T2 早期喉癌，不論是局部控制率、5年生存率還是無病生存率，RT 與 TLM 的療效皆高度相似，均可達 85%–90% 以上。\n- C. 就長期的喉保存(laryngeal preservation)而言,手術的結果較差：錯誤（為本題答案）。早期喉癌的局部手術主要是利用雷射進行「聲帶部分切除術（cordectomy）」，保留了喉部的基本解剖框架，並不需要全喉切除。在長期的喉保存率（laryngeal preservation rate，即不需要接受全喉切除的比例）上，手術與放射治療的效果同樣優異，並無手術結果較差的情況。\n- D. 某些腫瘤因生長部位,不易以內視鏡方式切除,可考慮以經口機器人手術(transoral robotic surgery)或放射 線治療：正確。如果腫瘤位置較偏或暴露困難（例如喉前連合 anterior commissure 暴露不佳），傳統內視鏡雷射手術較難完整切除時，可藉由經口機器人手術（TORS，具備多角度關節與立體視野）或直接採用放射線治療。\n\n【核心考點】\n早期喉癌（T1, T2）的治療原則：手術（經口雷射/機器人）與放療的存活率與喉保存率相當；放療療程長、成本高；手術適應症受限於內視鏡暴露視野。",
    "flashcard_front": "早期喉癌 (T1, T2) / 經口雷射微創手術 / 放射線治療 / 喉保存率 / 存活率",
    "flashcard_back": "早期喉癌的手術與放療在生存率與喉保存率上「不相上下」；放療時間較長且成本較高。",
    "flashcard_summary": "早期喉癌治療比較 -> 手術與放療局部控制及喉保存率相當，手術無劣勢"
  },
  {
    "id": "111-2_medicine-6_026",
    "category": "耳鼻喉科",
    "key_point": "唾液腺結石（Sialolithiasis）最常見的發生腺體（下頷腺）與其解剖病理因素。",
    "explanation": "【題幹解析】\n本題考查唾液腺結石（sialolithiasis）的好發部位及其生理與解剖成因。\n\n【選項詳解】\n- A. 下頷腺(submandibular gland)：正確。唾液腺結石最常發生於「下頷腺」（約占所有唾液腺結石病例的 80% 至 90%）。這主要歸因於三個因素：1. 下頷腺導管（Wharton's duct）的走行長且迂迴，且在口底是由下往上逆重力流動，易造成唾液淤積；2. 下頷腺分泌的唾液偏鹼性，鈣、磷酸鹽等無機離子濃度顯著高於腮腺；3. 其分泌液含高濃度的黏蛋白（mucopolysaccharides），較為黏稠，易形成結石的有機核心。\n- B. 腮腺(parotid gland)：錯誤。腮腺結石僅佔約 10%–20%。腮腺導管（Stensen's duct）較短且呈水平走行，其分泌的主要是阻薄的漿液（serous saliva），不易淤積沉澱。\n- C. 舌下腺(sublingual gland)：錯誤。舌下腺結石極為罕見。\n- D. 小唾液腺(minor salivary gland)：錯誤。小唾液腺結石極為罕見，若發生多為黏液栓塞，少有真正鈣化結石。\n\n【核心考點】\n唾液腺結石（Sialolithiasis）之好發位置（下頷腺最常見）與其解剖構造（Wharton's duct 長且逆流）及唾液成分（鹼性、黏稠、鈣離子高）的關聯。",
    "flashcard_front": "唾液腺結石 (Sialolithiasis) / 下頷腺 (Submandibular gland) / 腮腺 (Parotid gland) / Wharton's duct",
    "flashcard_back": "唾液腺結石最常發生於下頷腺（佔80%–90%），因 Wharton's duct 長且走行逆重力，且下頷腺唾液黏稠、偏鹼性、鈣離子高。",
    "flashcard_summary": "唾液腺結石好發腺體 -> 下頷腺最常見（解剖逆流、唾液黏稠偏鹼）"
  },
  {
    "id": "111-2_medicine-6_027",
    "category": "耳鼻喉科",
    "key_point": "甲狀腺髓質癌（Medullary Thyroid Carcinoma）的起源、遺傳比例與腫瘤標記。",
    "explanation": "【題幹解析】\n本題考查甲狀腺髓質癌（medullary thyroid carcinoma, MTC）的病理起源、遺傳流行病學、淋巴轉移傾向及特異性腫瘤標記。題目詢問何者敘述錯誤。\n\n【選項詳解】\n- A. 腫瘤細胞起源於parafollicular C cell：正確。甲狀腺髓質癌是由神經脊（neural crest）衍生的「濾泡旁 C 細胞（parafollicular C cells）」所發育而來的神經內分泌腫瘤，這與源自濾泡上皮細胞的乳突癌或濾泡癌不同。\n- B. 大部分為家族遺傳型(familial),少部分為偶發型(sporadic)：錯誤（為本題答案）。甲狀腺髓質癌大部分（約 75%–80%）是「偶發型（sporadic）」，僅有約 20%–25% 屬於「家族遺傳型」（包括 MEN 2A、MEN 2B 及家族性非 MEN 髓質癌，皆與 RET 原癌基因突變相關）。\n- C. 頸部淋巴轉移相當常見：正確。MTC 具有高度侵襲性，極易在疾病早期發生頸部淋巴結轉移（診斷時約有 50%–70% 的患者已伴隨淋巴結受累），因此治療時常需安排預防性或治療性頸部淋巴結廓清術。\n- D. 血液中calcitonin 可做為追蹤的有效腫瘤標記：正確。由於 C 細胞的主要生理功能是分泌降鈣素（calcitonin），髓質癌患者血中降鈣素數值會異常升高，是診斷、術後評估及長期追蹤復發最敏感且特異的腫瘤標記。此外，癌胚抗原（CEA）亦是常用的輔助追蹤指標。\n\n【核心考點】\n甲狀腺髓質癌（MTC）之病生理：起源於濾泡旁 C 細胞（分泌 calcitonin）；以偶發型為主（75%–80%）；極易發生早期頸部淋巴結轉移；與 RET 基因突變相關。",
    "flashcard_front": "甲狀腺髓質癌 (MTC) / 濾泡旁 C 細胞 / 降鈣素 (Calcitonin) / 偶發型與遺傳型比例 / RET 基因",
    "flashcard_back": "甲狀腺髓質癌源自 C 細胞，血清降鈣素為其特異腫瘤指標；其流行病學以偶發型（約80%）為主，家族遺傳型僅佔約20%。",
    "flashcard_summary": "甲狀腺髓質癌特點 -> C 細胞來源 & 偶發型佔 80% & 降鈣素為標記"
  },
  {
    "id": "111-2_medicine-6_028",
    "category": "婦產科",
    "key_point": "類男性型骨盆（Android Pelvis）的解剖特徵與產道阻礙。",
    "explanation": "【題幹解析】\n本題考查骨盆腔解剖分類（Caldwell-Moloy 分類）中的「類男性型骨盆（android pelvis）」之解剖特徵，並詢問何者敘述錯誤。需比較女型（gynecoid）與類男型（android）骨盆的徑線與構造特徵。\n\n【選項詳解】\n- A. 會聚的側壁(convergent sidewalls)：正確。Android 型骨盆的側壁自上而下向內收窄（會聚），使骨盆腔呈現漏斗狀，會增加胎頭下降的阻力。\n- B. 明顯的坐骨棘(ischial spines)：正確。Android 型的坐骨棘通常較為尖銳且向內突起，會顯著縮小中骨盆的橫徑（interspinous diameter）。\n- C. 狹窄的恥骨弓(pubic arch)：正確。Android 型骨盆的恥骨弓角度通常小於 90 度，呈尖角狀（狹窄），這不利於胎頭在分娩時枕骨向前旋轉與滑出。\n- D. 骨盆出口的橫徑(transverse diameter of pelvic outlet)>10 cm：錯誤（為本題答案）。骨盆出口的橫徑（即坐骨結節間徑 intertuberous diameter）在正常的女性型骨盆（gynecoid pelvis）通常大於 10 cm，以容許胎兒分娩。而在類男性型（android）骨盆中，由於側壁會聚及恥骨弓狹窄，出口橫徑通常「小於 10 cm」，導致分娩困難。\n\n【核心考點】\n骨盆腔解剖分類（Android 型）：特徵為漏斗狀、側壁會聚、坐骨棘尖銳突起、恥骨弓角度狹窄、出口橫徑小於 10 cm（易導致難產與枕後位 fetal occiput posterior position）。",
    "flashcard_front": "類男性型骨盆 (Android pelvis) / 骨盆腔特徵 / 恥骨弓角度 / 坐骨棘 / 出口橫徑",
    "flashcard_back": "Android 型骨盆特徵為側壁會聚、坐骨棘明顯、恥骨弓狹窄，其出口橫徑「小於 10 cm」，極易引發難產。",
    "flashcard_summary": "Android 骨盆特徵 -> 側壁會聚、坐骨棘突出、恥骨弓狹窄、出口橫徑 < 10 cm"
  },
  {
    "id": "111-2_medicine-6_029",
    "category": "婦產科",
    "key_point": "妊娠期間母體血清荷爾蒙（estradiol, estriol, hCG, hPL）的動態變化規律。",
    "explanation": "【題幹解析】\n題幹詢問懷孕全程中，母親血液中的何種荷爾蒙濃度「並不會」隨著妊娠週數增加而持續增加。需掌握四大主要妊娠荷爾蒙在懷孕不同階段的增長曲線。\n\n【選項詳解】\n- A. 雌二醇(estradiol)：錯誤（會持續增加）。雌二醇在懷孕期間主要由胎盤合成，其濃度會隨著妊娠週數的進展與胎盤的增大而穩定持續上升，直到足月生產前達到高峰。\n- B. 雌三醇(estriol)：錯誤（會持續增加）。雌三醇（E3）需要胎兒腎上腺與肝臟合成的前驅物，再經胎盤代謝產生，是評估「胎兒-胎盤單元（fetal-placental unit）」功能的重要指標，其濃度在孕期會隨著胎兒發育而持續穩定上升。\n- C. 人類絨毛膜刺激激素(human chorionic gonadotropin)：正確（為本題答案，不會持續增加）。hCG 主要由合體滋胚層（syncytiotrophoblast）分泌。在懷孕早期，其濃度每 2–3 天即會翻倍，約在懷孕第 8 至 10 週（第一孕期末）達到最高峰（約 100,000 mIU/mL），之後開始顯著下降，至懷孕第 20 週左右降至最低點並維持一個低水平的平台期，直至分娩，並不會全程持續增加。\n- D. 人類胎盤催乳激素(human placental lactogen)：錯誤（會持續增加）。hPL（亦稱人類絨毛膜促乳生長激素 hCS）由胎盤分泌，其分泌量與胎盤質量（placental mass）成正比，因此在懷孕全程會隨著胎盤長大而持續上升，直到接近足月。\n\n【核心考點】\n懷孕期關鍵荷爾蒙之分泌規律：hCG 在懷孕 8-10 週達高峰後下降維持平台期；Estradiol, Estriol, hPL 則隨孕期持續上升至足月。",
    "flashcard_front": "妊娠荷爾蒙曲線 / hCG 高峰 / 雌三醇 (Estriol) / 胎盤催乳素 (hPL) / 雌二醇",
    "flashcard_back": "雌二醇、雌三醇及 hPL 隨孕期持續上升至足月；hCG 則在孕期 8-10 週達最高峰後下降，中後期維持在低平台期。",
    "flashcard_summary": "孕期荷爾蒙動態 -> hCG 在 8-10 週達峰後下降；其他（雌激素、hPL）持續上升至足月"
  },
  {
    "id": "111-2_medicine-6_030",
    "category": "婦產科",
    "key_point": "胎兒羊水（Amnionic Fluid）體積調控的主要來源與清除途徑（胎兒尿液與胎兒吞嚥）。",
    "explanation": "【題幹解析】\n題幹詢問除了胎兒尿液之外，何者在胎兒羊水體積調控中佔最大宗。由於本題在題意表述上（「調控...除尿液外最多」，可能指最大來源或最大清除途徑，各教科書之具體流量數據界定亦有細微差異）存在爭議，官方更正為「一律給分」。以下詳解羊水體積調控的主要生理途徑及數據。\n\n【選項詳解】\n- A. 胎兒吞嚥(fetal swallowing)：主要清除途徑（若問清除量為最多）。在懷孕中後期，胎兒每日吞嚥的羊水量約為 500 至 1000 mL。這是羊水最主要的「清除與重吸收」途徑，用以調節羊水量的平衡。若胎兒因無腦症、食道閉鎖等原因無法吞嚥，會導致嚴重的羊水過多（polyhydramnios）。\n- B. 胎兒肺部分泌(fetal lung fluid secretion)：次要來源。胎兒肺部每日約分泌 300 至 400 mL 的液體，其中一部分流入羊膜腔，為羊水的次要來源。\n- C. 胎盤表面經膜內胎兒血管流入(intramembranous flow across fetal vessels on the placental surface)：主要交換途徑（若問吸收調控則與吞嚥相當）。膜內途徑是指羊水與胎盤表面的胎兒血管直接進行液體交換，每日交換量可達 200 至 400 mL。\n- D. 母體循環經羊膜流入(transmembranous flow across amnionic membrane)：次要途徑（經羊膜途徑）。此途徑在懷孕早期（胎兒皮膚尚未角質化前）是主要途徑，但在中後期其液體交換量顯著變小，每日僅約 10 mL。\n\n【核心考點】\n中後期羊水體積平衡的生理機轉：主要生成來源為胎兒排尿（fetal urination，約 600–1200 mL/day）；主要清除途徑為胎兒吞嚥（fetal swallowing，約 500–1000 mL/day）；膜內途徑（intramembranous pathway）為重要調控交換方式。",
    "flashcard_front": "羊水體積平衡 / 胎兒尿液 / 胎兒吞嚥 / 膜內途徑 / 羊水清除",
    "flashcard_back": "中後期羊水的主要來源為胎兒尿液（排尿）；最主要的清除途徑為胎兒吞嚥（每日約500-1000 mL），膜內途徑亦參與重要液體交換。",
    "flashcard_summary": "羊水生成與清除 -> 生成以尿液為主，清除以吞嚥為主"
  }
]

apply(updates)
