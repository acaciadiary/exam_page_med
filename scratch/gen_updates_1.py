import json
from pathlib import Path

updates = [
  {
    "id": "112-1_medicine-5_001",
    "category": "外科概論",
    "key_point": "外傷緊急大量輸血且血型未知時，首選輸入O型紅血球以恢復攜氧能力並降低溶血風險。",
    "explanation": "【題幹解析】\n外傷大出血且血型未明時，急診急救的首要目標是快速恢復患者的組織灌流與攜氧能力。在無法等待血型鑑定完成時，必須使用能安全輸入且不引發嚴重急性溶血反應的血品。\n\n【選項詳解】\n- A. 錯誤。O型全血（Whole blood）中含有O型血漿，其內含抗A與抗B抗體，若輸給非O型的受血者（例如A型、B型或AB型），這些抗體會與受血者紅血球上的A或B抗原結合，引發嚴重的急性溶血反應。因此緊急時不宜隨意輸入未去血漿的O型全血。\n- B. 正確。O型紅血球（Packed RBCs）已去除大部分含有抗體的血漿，且紅血球表面不具A與B抗原，故輸入任何血型的受血者體內皆不易引起急性抗原抗體溶血反應，為急診未知血型時的緊急首選血品。\n- C. 錯誤。O型血漿中富含抗A及抗B抗體，會與非O型受血者的紅血球產生溶血反應。血漿的萬能捐血者是AB型血漿（不含抗A與抗B抗體），而非O型。\n- D. 錯誤。若病人因出血性休克處於垂死狀態，盲目等待血型交叉配合試驗（通常需要30-45分鐘）會延誤搶救黃金時間，應立即啟動緊急輸血流程（輸入未交叉配合的O型紅血球）。\n\n【核心考點】\n緊急未知血型時的輸血原則：紅血球首選O型，血漿首選AB型；搶救生命重於等待常規血型鑑定。",
    "flashcard_front": "外傷大出血 / 血型未知 / 緊急輸血 / 紅血球與血漿選擇",
    "flashcard_back": "紅血球首選「O型」（無A、B抗原），血漿首選「AB型」（無抗A、抗B抗體），不可輸入O型全血或O型血漿以防溶血。",
    "flashcard_summary": "緊急未知血型輸血 -> 紅血球用O型，血漿用AB型，避免溶血反應。"
  },
  {
    "id": "112-1_medicine-5_002",
    "category": "外科概論",
    "key_point": "兒童肋骨富彈性不易骨折，但鈍傷易造成嚴重肺挫傷；氣胸患者轉院時不論大小皆應預防性置放胸管。",
    "explanation": "【題幹解析】\n評估胸部外傷（包含兒童與成人的解剖生理差異）以及氣胸的臨床處置與轉送安全指引。\n\n【選項詳解】\n- A. 正確。第9至12節肋骨（低部位肋骨）下方緊鄰腹腔臟器。右側折斷易傷及肝臟，左側折斷易傷及脾臟。因此低位肋骨骨折患者應高度懷疑腹內器官損傷，需考慮進行腹部電腦斷層（CT）評估。\n- B. 錯誤。兒童的骨骼尚未完全鈣化，肋骨具有極佳的彈性與軟骨成分，遭受鈍力創傷時傾向於彎曲變形而非直接折斷。因此，與成人相比，兒童較不易發生肋骨骨折，但也正因如此，外力更容易直接傳導至胸腔內，造成嚴重的肺挫傷（pulmonary contusion）或氣胸，卻無明顯肋骨骨折表現。\n- C. 正確。兒童的縱隔腔（mediastinum）活動度與可移動性較成人大，一旦發生氣胸，積氣易將縱隔腔及心臟推向健側，極易迅速發展成張力性氣胸（tension pneumothorax），壓迫大靜脈回流。\n- D. 正確。雖然少量氣胸（<10%）在密切觀察下可自行吸收，但若病人需要轉院，可能在途中面臨氣壓改變（如航空轉運）或因呼吸衰竭需使用正壓通氣（positive pressure ventilation），這會使微小氣胸迅速演變成張力性氣胸。因此轉院前應放置胸管以策安全。\n\n【核心考點】\n小兒胸創特點（肋骨易彎不易折、易肺挫傷及張力性氣胸）與氣胸患者在正壓呼吸或轉院前的胸管放置指引。",
    "flashcard_front": "兒童胸部鈍傷 / 肋骨骨折率 / 氣胸轉運 / 低位肋骨骨折併發症",
    "flashcard_back": "兒童肋骨富彈性不易骨折，但外力易直達肺部造成肺挫傷；少量氣胸患者轉院或接受正壓通氣前，必須預防性放置胸管。",
    "flashcard_summary": "胸部外傷處置 -> 兒童肋骨不易折但易內傷；轉院氣胸患者必置胸管。"
  },
  {
    "id": "112-1_medicine-5_003",
    "category": "一般外科",
    "key_point": "胰頭十二指腸切除術（Whipple procedure）後重建中，胰空腸吻合處因胰液腐蝕性及胰腺脆弱，最易發生滲漏（胰漏）。",
    "explanation": "【題幹解析】\n胰頭十二指腸切除術（Whipple procedure）是治療胰臟頭部癌、壺腹周圍癌等的主要術式。切除後需重建消化道，一般順序為：胰腺空腸吻合（Pancreaticojejunostomy）、膽管空腸吻合（Choledochojejunostomy）及胃（或十二指腸）空腸吻合（Gastrojejunostomy）。本題考查各吻合處術後滲漏機率之比較。\n\n【選項詳解】\n- A. 錯誤。胃部空腸吻合（Gastrojejunostomy）的血循通常非常豐富，且胃壁與空腸壁較厚，癒合能力佳，其滲漏率在三者中最低（通常<1-2%）。\n- B. 錯誤。膽管空腸吻合（Choledochojejunostomy）的滲漏率（膽漏）稍高，但膽汁對組織的腐蝕性及吻合難度仍小於胰腺吻合（通常發生率在2-5%左右）。\n- C. 正確。胰腺質地通常較為柔軟脆弱，且胰液中含有大量強效的消化酶（若被活化會消化自身組織）。胰體空腸吻合（Pancreaticojejunostomy）在技術上難度最高，是臨床上最常見且最危險的吻合口滲漏（胰漏，Pancreatic fistula，發生率可達10-20%以上），是Whipple術後病人死亡與嚴重併發症的主要原因。\n- D. 錯誤。各吻合處因組織特性、分泌物腐蝕性及血循不同，其滲漏機率有明顯差異，胰體空腸吻合的滲漏率顯著最高。\n\n【核心考點】\nWhipple 術後消化道重建的三個吻合口中，以「胰空腸吻合」滲漏率最高、危害最重，需密切監測引流液澱粉酶（amylase）數值。",
    "flashcard_front": "Whipple 手術 / 消化道重建 / 吻合口滲漏 / 胰漏風險",
    "flashcard_back": "消化道重建三吻合口中，「胰體空腸吻合（Pancreaticojejunostomy）」滲漏率最高。主因胰腺脆弱及胰液具高度腐蝕性。",
    "flashcard_summary": "Whipple重建滲漏 -> 胰體空腸吻合（胰漏）發生率最高且預後最危險。"
  },
  {
    "id": "112-1_medicine-5_004",
    "category": "一般外科",
    "key_point": "肝細胞癌BCLC分期中，經導管動脈化學栓塞（TACE）屬於緩和性治療，並非根治性治療方式。",
    "explanation": "【題幹解析】\n巴塞隆納肝癌分期（BCLC staging system）是目前臨床評估肝細胞癌（HCC）治療策略的核心指引，將患者依腫瘤狀態、肝功能（Child-Pugh）及病人體能狀態（ECOG PS）進行分類並提供治療建議。\n\n【選項詳解】\n- A. 正確。BCLC分期分為 Stage 0 (Very early)、Stage A (Early)、Stage B (Intermediate)、Stage C (Advanced)、Stage D (Terminal)。\n- B. 正確。分期依據主要整合三大維度：腫瘤狀況（個數、大小、是否有血管侵犯或肝外轉移）、肝臟功能狀態（主要是Child-Pugh分期評估）及患者日常活動體能表現（Performance status, ECOG）。\n- C. 錯誤。經導管動脈化學栓塞（TACE/Chemoembolization）是BCLC Stage B（中期多發性且無血管侵犯的肝癌）的首選治療，屬於非根治性、緩和性治療（Palliative treatment）。根治性治療（Curative treatment）包括：手術切除（Surgical resection）、肝移植（Liver transplantation）及局部消融（Radiofrequency ablation, RFA）。\n- D. 正確。BCLC Stage C 為晚期肝癌（已伴隨門靜脈侵犯或肝外轉移，但體能尚可、肝功能佳者），首選全身性治療，可使用標靶藥物（如Sorafenib、Lenvatinib）或免疫合併治療。\n\n【核心考點】\nBCLC分期與對應治療策略：根治性治療（切除、移植、消融）適用於Stage 0/A；TACE適用於Stage B（非根治性）；標靶/免疫適用於Stage C。",
    "flashcard_front": "肝細胞癌 / BCLC 分期與治療 / 根治性 vs 緩和性治療 / TACE 定位",
    "flashcard_back": "根治性治療為「切除、移植、RFA消融」（Stage 0/A）；TACE（Stage B）屬於緩和性治療；標靶藥物（如 Sorafenib）為 Stage C 首選。",
    "flashcard_summary": "BCLC治療分類 -> 根治性治療不含TACE（TACE為Stage B緩和治療）；Stage C用標靶/免疫。"
  },
  {
    "id": "112-1_medicine-5_005",
    "category": "外科概論",
    "key_point": "理想的傷口敷料應維持傷口「濕潤」而非乾燥，以利上皮細胞移行與癒合。",
    "explanation": "【題幹解析】\n現代傷口護理的核心觀念是「濕潤癒合理論」（Moist wound healing）。理想的敷料應提供合適的微環境以加速肉芽組織生長及上皮化，同時避免外部分子感染。\n\n【選項詳解】\n- A. 正確。敷料必須具備優良的阻絕屏障功能，防止外界細菌或病毒通透，以降低傷口感染機率。\n- B. 錯誤。根據「濕潤癒合」原則，傷口維持適度的濕潤環境能促進細胞生長因子釋放、加速表皮細胞游移與增殖，且能減輕疼痛、防禦結痂。因此「創造乾燥清爽環境」並非理想敷料的特性，相反地，過度乾燥會延緩癒合。\n- C. 正確。敷料應提供適當的緩衝，防止外力摩擦與碰撞造成的機械性二次傷害。\n- D. 正確。敷料應易於操作、貼附及移除，避免換藥時對新生的肉芽組織造成撕扯與二次傷害。\n\n【核心考點】\n傷口濕潤癒合觀念：適當濕潤可加速癒合，乾燥環境易結痂並阻礙上皮移行。",
    "flashcard_front": "傷口敷料特性 / 濕潤癒合理論 / 理想敷料要求 / 傷口微環境",
    "flashcard_back": "理想敷料應維持傷口「適度濕潤」以促進癒合，而非「乾燥清爽」；並應兼具防菌、保護與易操作性。",
    "flashcard_summary": "理想敷料環境 -> 維持適度濕潤（moist）而非乾燥，防止微生物侵入並保護新生組織。"
  },
  {
    "id": "112-1_medicine-5_006",
    "category": "移植外科",
    "key_point": "活動性/未受控制的感染（如開放性肺結核）是腎臟移植的絕對禁忌症；病情控制穩定的HIV感染已非禁忌症。",
    "explanation": "【題幹解析】\n腎臟移植需要長期使用免疫抑制劑，因此在術前必須排除可能因免疫抑制而迅速惡化、威脅生命或導致移植失敗的絕對禁忌症。\n\n【選項詳解】\n- A. 正確。開放性肺結核（Active tuberculosis）屬於未控制的活動性傳染病。若在此狀態下進行移植並給予免疫抑制劑，會引發結核菌全身性擴散，導致嚴重感染死亡，故為「絕對禁忌症」。必須完整抗結核治療並確認痊癒後方可考慮移植。\n- B. 錯誤。隨著高效抗愛滋病療法（HAART）的普及，若愛滋病（HIV）帶原者接受定期治療、病毒量測不到且CD4+ T細胞數量穩定，其存活率與非HIV者相近，目前已非移植之絕對禁忌症，可安全接受移植。\n- C. 錯誤。高齡（>70歲）是相對禁忌症或需評估生理年齡與共病，若患者心肺功能健全且評估可耐受手術，並非絕對禁忌症。\n- D. 錯誤。惡性腫瘤患者若經過適當治療，且無復發追蹤期已足夠長（如大腸癌大於5年無復發），體內被認為已無癌細胞，則可安全接受腎移植，非絕對禁忌症。\n\n【核心考點】\n腎移植禁忌症評估：活動性感染、未控制的惡性腫瘤為絕對禁忌症。控制良好的慢性傳染病（如HIV、B/C肝）與已治癒的癌症（無復發期足夠）均已排除在絕對禁忌症之外。",
    "flashcard_front": "腎臟移植 / 絕對禁忌症 / HIV 感染者移植 / 癌症患者移植條件",
    "flashcard_back": "「未控制之活動性感染（如開放性肺結核）」為絕對禁忌症；病情穩定的HIV患者、或已治癒大於5年無復發的癌症患者，皆可接受移植。",
    "flashcard_summary": "腎移植禁忌症 -> 活動性感染為絕對禁忌，控制良好的HIV與治癒5年以上癌症非禁忌。"
  },
  {
    "id": "112-1_medicine-5_007",
    "category": "一般外科",
    "key_point": "盲環症候群（blind loop syndrome）因細菌過度孳生消耗維生素B12，導致大紅血球性貧血而非小紅血球性貧血。",
    "explanation": "【題幹解析】\n盲環症候群（Blind loop syndrome，又稱Stagnant loop syndrome）多因胃腸道手術後（如Billroth II）形成停滯的腸段，或小腸憩室、狹窄處導致腸內容物停滯，引發小腸內細菌過度孳生（SIBO）。\n\n【選項詳解】\n- A. 正確。小腸內過度孳生的細菌會將結合型膽鹽（conjugated bile salts）去結合（deconjugate），使其失去乳化脂肪的功能，進而阻礙脂肪在小腸的吸收，引發脂肪瀉（steatorrhea）。\n- B. 正確。孳生的細菌會大量消耗食物中的維生素B12。雖然患者攝取充足，但體內可吸收的維生素B12嚴重不足，因此需要外源性補充。\n- C. 正確。本病的根本機轉即是結構畸形或蠕動異常導致腸道內容物滯留，造成小腸內細菌過度孳生。\n- D. 錯誤。維生素B12缺乏會導致去氧核糖核酸（DNA）合成受阻，使得紅血球發育異常、體積變大，臨床上表現為「大紅血球性貧血」（macrocytic / megaloblastic anemia），而非缺鐵引起的小紅血球性貧血（microcytic anemia）。\n\n【核心考點】\n盲環症候群的病理生理機轉：小腸細菌過度孳生（SIBO） -> 膽鹽去結合（導致脂肪瀉與脂溶性維生素吸收不良）與維生素B12被細菌消耗（導致巨紅血球性貧血）。",
    "flashcard_front": "盲環症候群 / 臨床機轉 / 脂肪瀉成因 / 貧血類型與維生素",
    "flashcard_back": "盲環症候群因「細菌過度孳生」消耗維生素B12，導致「大紅血球性貧血（Macrocytic anemia）」；且因去結合膽鹽造成「脂肪瀉」。",
    "flashcard_summary": "盲環症候群生理 -> 細菌過度孳生消耗B12引發大紅血球性貧血，破壞膽鹽引起脂肪瀉。"
  },
  {
    "id": "112-1_medicine-5_008",
    "category": "神經外科",
    "key_point": "星狀細胞瘤WHO I、II級為低惡性度；III、IV級為高惡性度，僅IV級稱為GBM；手術切除是主要的基礎治療。",
    "explanation": "【題幹解析】\n腦部星狀細胞瘤（Astrocytoma）的WHO分級與臨床特徵：\n- Grade I: 毛狀星狀細胞瘤 (Pilocytic astrocytoma)，良性，預後極佳。\n- Grade II: 瀰漫性星狀細胞瘤 (Diffuse astrocytoma)，低惡性度，進展緩慢。\n- Grade III: 間變性星狀細胞瘤 (Anaplastic astrocytoma)，高惡性度。\n- Grade IV: 多形性膠質母細胞瘤 (Glioblastoma multiforme, GBM)，極高惡性度。\n\n【選項詳解】\n- A. 正確。WHO Grade I 與 Grade II 屬於低惡性度膠質瘤（Low-grade gliomas），細胞增殖慢，預後相對較佳。\n- B. 錯誤。高惡性度（High-grade gliomas）包含 Grade III 與 Grade IV。但只有「Grade IV」的星狀細胞瘤才會被稱為膠質母細胞瘤（Glioblastoma, GBM）。Grade III 稱為間變性星狀細胞瘤（Anaplastic astrocytoma）。\n- C. 錯誤。Grade I 與 II 預後相對較好，中位生存期（median survival）通常可以超過5年甚至10年以上（特別是Grade I可達治癒）；只有高惡性度（尤其是GBM，中位生存期約12-15個月）預後極差。\n- D. 錯誤。手術切除（Surgical resection）是星狀細胞瘤最主要的治療基石，目的在於最大程度減壓、取得病理診斷，並為後續化療/放療創造條件。並非以化療及放療為主而放棄手術。\n\n【核心考點】\n星狀細胞瘤的WHO分級特徵：I/II級低惡性，III/IV級高惡性（IV級為GBM）；手術最大化切除是標準首選策略。",
    "flashcard_front": "星狀細胞瘤 / WHO 分級 / GBM 定義 / 首選治療策略",
    "flashcard_back": "WHO I、II級屬低惡性（預後較佳）；僅「IV級」稱為GBM；治療以「手術最大程度切除」為首要關鍵，輔以放化療。",
    "flashcard_summary": "星狀細胞瘤分級 -> I-II級低惡性；僅IV級為GBM；手術切除為核心治療。"
  },
  {
    "id": "112-1_medicine-5_009",
    "category": "神經外科",
    "key_point": "自發性腦出血（如腦橋或小腦出血）常以高血壓為核心危險因子，急性期需適度降壓以防血塊擴大。",
    "explanation": "【題幹解析】\n病歷線索：68歲男性，急性昏迷（GCS E1V1M4），極高血壓（196/103 mmHg），枕頭與嘴邊有嘔吐物，暗示有高顱壓（IICP）伴隨腦幹受壓。CT（提示為後顱窩出血，如橋腦或小腦出血，常引發迅速昏迷與嘔吐）。\n\n【選項詳解】\n- A. 錯誤。後顱窩出血（如小腦或腦橋出血）或大面積腦幹出血，典型表現為早期神智改變（昏迷）、雙側瞳孔縮小（pinpoint pupils，橋腦出血）、去大腦皮質/去大腦強直或呼吸抑制，而非典型的大腦半球病變所致之「單側/半側肢體無力（hemiparesis）」。\n- B. 錯誤。急性自發性腦出血時，極高血壓（收縮壓 >150-220 mmHg）會增加血塊擴大（hematoma expansion）的風險。在維持腦灌流壓（CPP）的前提下，應使用靜脈降壓藥物將收縮壓控制在適當範圍（如140 mmHg左右），而非「不可以降血壓」。\n- C. 錯誤。此病人的臨床表現（無外傷痕跡、高齡、極高血壓、突發昏迷與嘔吐）為典型的自發性腦出血（spontaneous ICH）表現，不應無依據地懷疑是外傷受虐或謊報病史。\n- D. 正確。高血壓（Hypertension）與微血管瘤（Charcot-Bouchard aneurysms）形成及動脈硬化（與冠心病相關）密切相關，是自發性腦出血最主要的危險因子。\n\n【核心考點】\n自發性腦出血的危險因子（高血壓、血管硬化）與急性期血壓管理原則（適度降壓防止血塊擴大）。",
    "flashcard_front": "自發性腦出血 / 急性昏迷伴極高血壓 / 降壓目標 / 病史關聯",
    "flashcard_back": "高血壓為自發性腦出血主因；急性期（收縮壓高於150 mmHg時）需適度降壓（目標約140 mmHg）以防止血塊持續擴大。",
    "flashcard_summary": "自發性腦出血高血壓 -> 核心病因為高血壓與動脈硬化，急性期應適度降壓防止血塊擴大。"
  },
  {
    "id": "112-1_medicine-5_010",
    "category": "神經外科",
    "key_point": "急性腦出血禁用類固醇降低腦水腫，大血塊引發腦幹壓迫或水腦時需積極手術處置。",
    "explanation": " = \"【題幹解析】\n本題承接上題，考查後顱窩/自發性腦出血的急症處置原則、藥物治療禁忌與手術適應症。\n\n【選項詳解】\n- A. 正確。若出血位於小腦或腦幹，血塊常會壓迫第四腦室，阻礙腦脊髓液（CSF）流通，進而引發急性「阻塞性水腦症」（obstructive hydrocephalus），此時需緊急施行腦室外引流術（EVD）以降低顱內壓。\n- B. 錯誤。對於腦中風（包含腦出血或缺血性腦中風）引起的腦水腫，臨床實證已證實使用類固醇（Steroids）不僅「無效」，且會顯著增加全身性感染、高血糖及胃腸道出血等併發症，屬於治療禁忌。此外，若為小腦出血且直徑 >3 cm 或已造成腦幹壓迫，必須採取緊急手術移除血塊，而非僅行保守治療。\n- C. 正確。後顱窩容積狹小，出血若進一步擴大，會形成小腦扁桃體疝脫（tonsillar herniation），直接壓迫延腦（呼吸與循環中樞），造成患者猝死。\n- D. 正確。高血壓性自發性腦出血最常見的部位包括：殼核（putamen）、丘腦（thalamus）、小腦（cerebellum）及橋腦（pons）。本題為常見自發性出血區域。\n\n【核心考點】\n腦出血急性期治療原則：禁用類固醇消水腫；小腦出血 >3 cm 合併神智改變需緊急手術；阻塞性水腦需放置EVD。",
    "flashcard_front": "急性腦出血 / 類固醇使用 / 阻塞性水腦症 / 小腦出血手術指引",
    "flashcard_back": "腦出血急性期「禁用類固醇」消水腫（無效且增感染率）；小腦出血>3cm或壓迫腦幹需「緊急手術移除血塊」，合併水腦行EVD。",
    "flashcard_summary": "腦出血治療原則 -> 禁用類固醇；小腦出血大於3cm需手術，合併水腦症做EVD。"
  }
]

# Write to temp updates file
scratch_dir = Path(r"C:\Users\User\.gemini\antigravity\brain\285f77f1-a3ad-46dc-8c67-e0efdabe0a2f\scratch")
scratch_dir.mkdir(parents=True, exist_ok=True)
updates_file = scratch_dir / "updates_1.json"
updates_file.write_text(json.dumps(updates, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Written updates to {updates_file}")
