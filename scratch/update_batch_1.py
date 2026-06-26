import sys
sys.path.append("scratch")
from apply_updates import apply

updates = [
  {
    "id": "111-2_medicine-6_001",
    "category": "麻醉科",
    "key_point": "比較口咽與鼻咽人工氣道的適應症、禁忌症及常見併發症。",
    "explanation": "【題幹解析】\n題幹提及氣道輔助工具（鼻咽人工氣道 NPA 與口咽人工氣道 OPA），並詢問何者敘述錯誤。解答此題需釐清兩種人工氣道的生理反應（如嘔吐反射）、病人意識狀態的耐受度以及相關解剖構造禁忌。\n\n【選項詳解】\n- A. 清醒的病人優先使用口咽人工氣道：錯誤。口咽人工氣道（OPA）置入後會直接刺激舌根與咽部，容易誘發強烈的嘔吐反射（gag reflex），甚至引發喉部痙攣。因此，清醒或半清醒且保有咽喉反射的病人禁忌使用 OPA，應優先使用耐受性較佳的鼻咽人工氣道（NPA）。\n- B. 誘發嘔吐是口咽人工氣道的潛在性風險：正確。OPA 會刺激咽喉後壁，對未完全喪失反射的病人容易誘發嘔吐，造成吸入性肺炎的風險。\n- C. 顱骨底骨折是鼻咽人工氣道的禁忌：正確。懷疑或確認有顱骨底骨折（basilar skull fracture）或篩骨板（cribriform plate）骨折的病人，置入 NPA 時導管有可能誤入顱腔造成嚴重腦部損傷，屬於絕對禁忌症。\n- D. 鼻出血是鼻咽人工氣道的潛在性併發症：正確。NPA 需通過狹窄且血管豐富的鼻道，若置入時力量過大、潤滑不足或導管過大，極易損傷鼻黏膜導致鼻出血。\n\n【核心考點】\n氣道管理中口咽人工氣道（OPA）與鼻咽人工氣道（NPA）的臨床選擇原則、意識狀態要求、禁忌症（如顱骨底骨折為 NPA 禁忌）與併發症（如 OPA 易致嘔吐、NPA 易致鼻出血）。",
    "flashcard_front": "口咽人工氣道 / 鼻咽人工氣道 / 意識清醒 / 顱骨底骨折 / 咽喉反射",
    "flashcard_back": "清醒病人因保有咽喉反射禁忌使用口咽氣道（OPA），而顱骨底骨折病人禁忌使用鼻咽氣道（NPA）。",
    "flashcard_summary": "清醒病人 & 顱骨底骨折 -> 禁置OPA，禁置NPA"
  },
  {
    "id": "111-2_medicine-6_002",
    "category": "麻醉科",
    "key_point": "評估重症與麻醉心血管監測指標（SvO2、TEE、PPV、CVP）的臨床應用與正常值。",
    "explanation": "【題幹解析】\n本題考查心血管監測在麻醉及重症醫學中的臨床運用。題目詢問何者敘述錯誤。需要了解 SvO2（混合靜脈血氧飽和度）的正常範圍、食道超音波（TEE）的應用範疇、前負荷（preload）動態與靜態指標的預測能力，以及中心靜脈壓（CVP）與肺動脈導管監測的常見臨床陷阱。\n\n【選項詳解】\n- A. 在肺動脈導管(pulmonary artery catheter)監測mixed venous hemoglobin oxygen saturation(SvO2),目的是測量 心輸出量與全身血氧供應量是否足夠。正常的SvO2數值約30%~50%：錯誤。正常的 SvO2 數值一般為 60% 至 80%（臨床常以 65%–75% 作為正常值）。SvO2 數值若降至 30%–50% 代表組織氧供極度不足或氧耗過高，為嚴重的組織缺氧狀態。\n- B. 經食道超音波(transesophageal echocardiography)對心臟功能、瓣膜功能、心室內血量、導管位置都有良好的 監測效果,也可以使用在非開心手術的病人監測：正確。TEE 探頭置於食道內，緊鄰心臟後方，能提供高品質的即時影像，除了開心手術外，也常用於非開心手術中高風險病人的心功能及血容量監測。\n- C. 若要監測心臟前負荷(cardiac preload),動態測量(如pulse pressure variation)較靜態測量(如pulmonary capillary wedge pressure)更能預測血管內容積的反應性(intravascular volume responsiveness)：正確。動態指標如脈壓變異度（PPV）或每搏輸出量變異度（SVV）利用心肺交互作用，評估輸液後心輸出量是否能增加，其預測輸液反應性的準確度顯著優於靜態指標如 PCWP 或 CVP。\n- D. 使用CVP(central venous pressure)和肺動脈導管監測最常見的後遺症是對數值的誤用與誤判：正確。CVP 與肺動脈導管所測得的壓力數值易受到病人呼吸器設定（如 PEEP）、體位、心臟順應性（compliance）等多種因素影響，臨床上最常見的問題是醫師對數據的過度解減、誤判或機械性盲從。\n\n【核心考點】\n心血管監測指標之正常生理數值（SvO2 應為 60%–80%）、前負荷監測的動態指標（PPV）與靜態指標（PCWP/CVP）預測容積反應性的差異，以及 TEE 的臨床適應症。",
    "flashcard_front": "混合靜脈血氧飽和度 (SvO2) / 脈壓變異度 (PPV) / 食道超音波 (TEE) / 輸液反應性",
    "flashcard_back": "正常 SvO2 約為 60%–80%；動態測量指標（如 PPV）預測輸液反應性（volume responsiveness）顯著優於靜態指標。",
    "flashcard_summary": "正常 SvO2 範圍 & 輸液反應性評估 -> 60%–80% & 動態指標（PPV）優於靜態指標"
  },
  {
    "id": "111-2_medicine-6_003",
    "category": "麻醉科",
    "key_point": "術中腎功能監測與腎臟保護的最佳臨床策略。",
    "explanation": "【題幹解析】\n本題詢問術中關於腎臟功能監測與處理的正確敘述。解題需瞭解尿量（urine output）與肌酸酐（creatinine）在術中急性評估上的侷限性，以及維持腎灌流壓（血液動力學）對於預防術後急性腎損傷（AKI）的重要性。\n\n【選項詳解】\n- A. 術中尿排出量(urine output)為術中最常用的監測,可以監測腎絲球過濾(glomerular filtration)與腎功能：錯誤。術中尿量雖然是常用指標，但極易受到麻醉藥物引起的抗利尿激素（ADH）分泌、交感神經興奮及術中輸液狀態的干擾，並不能精確且即時地反映腎絲球過濾率（GFR）或腎功能的實質受損。\n- B. creatinine 升高與GFR(glomerular filtration rate)降低成線性正比關係：錯誤。血清肌酸酐（creatinine）與 GFR 呈「反比的非線性雙曲線關係」。在腎功能衰退早期（GFR 還算高時），即使 GFR 已經大幅下降，creatinine 可能只微幅上升；通常要到 GFR 減半或降至 50% 以下時，creatinine 才會顯著升高，因此 creatinine 存在嚴重的偵測延遲。\n- C. 麻醉中為確保腎功能,最有效的方式是監測及維持hemodynamics,確保心臟功能、血管內血量及足夠的組織 灌流：正確。維持全身血液動力學穩定，確保腎臟有足夠的血流灌流（Renal perfusion pressure），是預防手術期間發生急性腎損傷（AKI）最核心且最有效的方法。\n- D. 腎功能受損的biomarker 介白素(interleukin-18)與腎小管壓力反應並無相關：錯誤。Interleukin-18 (IL-18) 是一種促發炎細胞激素，在腎小管上皮細胞受到缺血、毒性或壓力損傷時會釋放，是早期診斷急性腎小管損傷的敏感 biomarker。\n\n【核心考點】\n術中腎臟保護的核心在於維持血液動力學與組織灌流；血清肌酸酐與 GFR 呈非線性關係且有滯後性；術中尿量受多種神經內分泌因子影響，非評估 GFR 的金標準。",
    "flashcard_front": "術中腎臟保護 / 肌酸酐與 GFR 關係 / 術中尿量侷限性 / 血液動力學",
    "flashcard_back": "預防術後急性腎損傷最有效的方法是維持血液動力學穩定以確保腎灌流；肌酸酐與 GFR 呈非線性反比關係。",
    "flashcard_summary": "術中腎保護最佳方式 & 肌酸酐與GFR關係 -> 維持血液動力學灌流 & 非線性反比關係"
  },
  {
    "id": "111-2_medicine-6_004",
    "category": "麻醉科",
    "key_point": "鴉片類藥物過量所致呼吸抑制的專一性拮抗劑 naloxone。",
    "explanation": "【題幹解析】\n題幹描述「使用鴉片類藥物作術後止痛」，並詢問哪一種藥物具有「鴉片類藥物受體專一性拮抗作用」，能競爭中樞神經受體以逆轉呼吸抑制副作用。\n\n【選項詳解】\n- A. naloxone：正確。Naloxone 是一種純粹的鴉片類受體拮抗劑（pure opioid antagonist），對 μ, κ, δ 受體均有競爭性拮抗作用，能迅速逆轉鴉片類藥物引起的呼吸抑制、鎮靜與低血壓，是鴉片類藥物中毒或過量的首選解毒劑。\n- B. flumazenil：錯誤。Flumazenil 是苯二氮平類（benzodiazepines，如 midazolam, diazepam）的專一性拮抗劑，競爭性結合 GABA_A 受體，對鴉片類藥物無效。\n- C. dexmedetomidine：錯誤。Dexmedetomidine 是一種高選擇性的 α2 腎上腺素受體致效劑（alpha-2 agonist），臨床上用於鎮靜與輔助止痛，不具拮抗鴉片受體的作用。\n- D. ketamine：錯誤。Ketamine 是一種 NMDA 受體拮抗劑，主要用於誘導麻醉、止痛及解離麻醉，並非鴉片受體的拮抗劑。\n\n【核心考點】\n麻醉與止痛藥物之拮抗劑配對：鴉片類藥物過量用 naloxone 拮抗；Benzodiazepine 類藥物過量用 flumazenil 拮抗。",
    "flashcard_front": "鴉片類藥物過量 / 呼吸抑制 / 專一性拮抗劑 / Naloxone / Flumazenil",
    "flashcard_back": "Naloxone 是鴉片類受體的專一性拮抗劑；Flumazenil 則是 Benzodiazepine 類的專一性拮抗劑。",
    "flashcard_summary": "鴉片類拮抗劑 & BZD拮抗劑 -> Naloxone & Flumazenil"
  },
  {
    "id": "111-2_medicine-6_005",
    "category": "麻醉科",
    "key_point": "靜脈麻醉劑（Barbiturates、Propofol、Benzodiazepines）的作用機轉與臨床特性。",
    "explanation": "【題幹解析】\n本題考查常見靜脈麻醉劑（intravenous anesthetics）的藥理機轉與副作用。題目詢問何者敘述錯誤。需要區分 Barbiturates（巴比妥類）、Propofol（丙泊酚）、Benzodiazepines（苯二氮平類）的受體作用位點及臨床特性。\n\n【選項詳解】\n- A. benzodiazepine 可能導致呼吸暫停(apnea)：正確。Benzodiazepines（如 midazolam）具有中樞性呼吸抑制作用，當快速靜脈注射或與其他麻醉劑/鴉片類藥物併用時，極可能導致暫時性呼吸暫停。\n- B. propofol 製劑有助於細菌的生長：正確。Propofol（丙泊酚）不溶於水，乳劑配方中含有 10% 大豆油、1.2% 純化卵磷脂和 2.25% 甘油，這些高脂營養成分非常利於細菌繁殖，因此臨床使用時要求嚴格無菌操作，且開封後需在規定時間內用畢。\n- C. barbiturate 抑制腦幹中的reticular activating system：正確。Barbiturates（如 thiopental）主要透過加強 GABA_A 受體介導的抑制性傳導，抑制腦幹網狀激活系統（reticular activating system, RAS），從而產生誘導麻醉與鎮靜作用。\n- D. barbiturate 經由與NMDA 受體結合而起作用：錯誤。Barbiturates 主要作用於 GABA_A 受體，透過結合在受體的特定位點，延長氯離子通道的開啟時間（prolong the open duration），造成神經元超極化而產生抑制效果。而結合並拮抗 NMDA 受體起作用的靜脈麻醉劑主要是 Ketamine。\n\n【核心考點】\n靜脈麻醉藥之藥理機轉與特性：Barbiturates 與 GABA_A 受體結合（非 NMDA 受體）；Ketamine 作用於 NMDA 受體；Propofol 乳劑富含油脂易滋生細菌；Benzodiazepines 的呼吸抑制風險。",
    "flashcard_front": "巴比妥類 (Barbiturates) / 作用受體 / 丙泊酚 (Propofol) / 氯離子通道",
    "flashcard_back": "Barbiturates 主要作用於 GABA_A 受體（延長氯離子通道開啟）；NMDA 受體則是 Ketamine 的主要作用標的。",
    "flashcard_summary": "Barbiturates 作用受體 & Ketamine 作用受體 -> GABA_A 受體 & NMDA 受體"
  },
  {
    "id": "111-2_medicine-6_006",
    "category": "麻醉科",
    "key_point": "處理面罩通氣困難時的正確物理操作與手法原則。",
    "explanation": "【題幹解析】\n題幹描述在麻醉誘導進行面罩通氣（mask ventilation）時發現通氣困難，詢問哪一項處置的改善效果最差（或可能加重阻塞）。解題需瞭解面罩通氣時氣道阻塞的主要生理機轉（通常為舌後墜或咽部軟組織塌陷）以及正確的徒手開通氣道手法。\n\n【選項詳解】\n- A. 用力往下壓緊面罩：正確，為本題答案（改善效果最差）。在面罩通氣困難時，若一味用力向下壓緊面罩，會將下頜骨（mandible）與周圍軟組織往後推，進一步壓迫咽部，反而加重舌後墜與呼吸道阻塞。正確的手法應是使用「E-C clamp」技術，用第三、四、五指扣住下頜骨角，向上、向外提拉下頜骨使其貼合面罩。\n- B. 放置口咽呼吸道(oral airway)：錯誤，非最差（能有效改善）。OPA 能將後墜的舌根頂起，使其與咽後壁分離，是解決舌後墜引起通氣困難的極佳輔助工具。\n- C. 放置鼻咽呼吸道(nasal airway)：錯誤，非最差（能有效改善）。NPA 通過鼻腔進入咽部，也能繞過後墜的舌頭，為氣體流動提供通道。\n- D. 壓額抬下巴(head tilt and chin lift)：錯誤，非最差（能有效改善）。壓額抬下巴法是基礎心肺復甦術與氣道管理的基本手法，能將氣道軸線拉直，拉開咽部軟組織以暢通氣道。\n\n【核心考點】\n面罩通氣困難的排除手法：E-C 手法中應「拉起下頷（jaw thrust / chin lift）」而非「向下壓緊面罩」；口咽/鼻咽人工氣道的放置時機。",
    "flashcard_front": "面罩通氣困難 / E-C clamp / 壓緊面罩 / 舌後墜 / 下頜提拉",
    "flashcard_back": "面罩通氣困難時，用力往下壓面罩會加重舌後墜阻塞氣道；應向上提拉下頜骨貼合面罩，並視情況置入口咽/鼻咽管。",
    "flashcard_summary": "面罩通氣困難處置 -> 向上提拉下頜貼合面罩，不可用力下壓面罩"
  },
  {
    "id": "111-2_medicine-6_007",
    "category": "麻醉科",
    "key_point": "經食道超音波（TEE）的臨床功能與局限性（冠狀動脈病變評估）。",
    "explanation": "【題幹解析】\n本題考查經食道超音波（transesophageal echocardiography, TEE）在術中或重症監測時能獲得的資訊，並詢問何者「不是」能直接精確獲得的資訊。需了解 TEE 的成像原理及空間解析度對於心臟大構造（心室、瓣膜）與極微細構造（冠狀動脈分支）評估的差異。\n\n【選項詳解】\n- A. 左心室舒張功能：錯誤。TEE 可利用二尖瓣流入血流都卜勒（mitral inflow Doppler）及組織都卜勒（tissue Doppler imaging, TDI）精確測量 E/A 比值與 e'，用以評估左心室舒張功能。\n- B. 心輸出量(cardiac output)：錯誤。TEE 可透過測量左心室流出道（LVOT）的直徑以及都卜勒血流時間積分（TVI），計算出每搏輸出量（SV），再乘以心率得到心輸出量。\n- C. 主動脈瓣膜狹窄程度：錯誤。TEE 對於主動脈瓣的形態（如二葉瓣、三葉瓣、鈣化）有極佳的顯像能力，並可透過連續波都卜勒（CW Doppler）測量主動脈瓣口最高血流速度與壓力差，估算主動脈瓣面積。\n- D. 冠狀動脈狹窄程度：正確，為本題答案（無法獲得此資訊）。雖然 TEE 有時可以觀察到冠狀動脈的開口（Ostium）或近端血流，但因為冠狀動脈管徑非常細小（通常僅數毫米）且行程迂迴，TEE 的解析度與音波角度限制無法用來精確定量冠狀動脈各分支的狹窄程度。臨床上評估冠狀動脈狹窄仍需依賴侵入性冠狀動脈攝影（Coronary angiography, CAG）或電腦斷層冠狀動脈攝影（CCTA）。\n\n【核心考點】\n經食道超音波（TEE）之適應症與功能限制：可測量瓣膜病變、心室收縮與舒張功能、心輸出量，但無法用以精確診斷冠狀動脈各分支的狹窄程度。",
    "flashcard_front": "經食道超音波 (TEE) / 冠狀動脈狹窄 / 瓣膜病變 / 組織都卜勒 / 心輸出量",
    "flashcard_back": "TEE 可監測心臟結構、瓣膜病變及心室舒縮功能，但受解析度限制，無法精確評估冠狀動脈狹窄程度。",
    "flashcard_summary": "TEE 限制 -> 無法精確診斷冠狀動脈狹窄程度"
  },
  {
    "id": "111-2_medicine-6_008",
    "category": "麻醉科",
    "key_point": "慢性疼痛之硬脊膜外腔注射（Epidural Injection）的適應症與安全性。",
    "explanation": "【題幹解析】\n本題詢問關於慢性疼痛使用硬脊膜外腔注射（epidural injection）的錯誤敘述。解題需瞭解硬脊膜外注射在不同脊椎節段（腰椎、頸椎）的臨床使用現況、影像導引的必要性、以及藥物搭配的療效。\n\n【選項詳解】\n- A. 適用於治療輕度神經根壓迫(nerve root compression)所造成的radicular pain：正確。硬脊膜外注射常用於治療因椎間盤突出或脊椎管狹窄引起的輕度至中度神經根壓迫，將藥物直接送達受壓迫神經周圍以緩解放射痛（radicular pain）。\n- B. 通常需要有影像的導引(image guidance),最常用的是X 光透視導引(fluoroscopic guidance)：正確。為確保針尖精確位於硬脊膜外腔並避免傷及神經與脊髓，目前臨床上多在 X 光透視（fluoroscopy）或超音波導引下進行，以大幅提高安全度與精準度。\n- C. 合併使用類固醇加局部麻醉藥較單獨使用局部麻醉藥注射效果好：正確。類固醇具有強效的抗發炎作用，能減輕神經根的水腫與發炎反應；局部麻醉藥則可提供即時的止痛與阻斷痛覺傳導。兩者併用能提供更持久且顯著的止痛效果。\n- D. 頸椎epidural injection 的風險太高,臨床上並未使用：錯誤（為本題答案）。雖然頸椎硬脊膜外注射因靠近頸髓與重要血管，其發生嚴重併發症（如高位硬脊膜外麻醉、脊髓損傷、椎動脈誤入）的風險確實高於腰椎，但在經驗豐富的專科醫師操作下，並在影像導引與造影劑確認的輔助下，臨床上仍常用於治療嚴重的頸椎椎間盤突出或頸部神經根痛。\n\n【核心考點】\n硬脊膜外注射（Epidural injection）之治療原則：影像導引的重要性、藥物組合（類固醇＋局部麻醉藥）的療效，以及頸椎硬脊膜外注射在臨床上仍被妥善使用（非禁用）。",
    "flashcard_front": "硬脊膜外注射 / 頸椎硬脊膜外注射 / 類固醇加局部麻醉藥 / 放射痛 (Radicular pain)",
    "flashcard_back": "頸椎硬脊膜外注射風險雖高，但臨床上在影像導引下仍會用於治療頸部放射痛，並非未使用。",
    "flashcard_summary": "頸椎硬脊膜外注射 -> 臨床有使用（需影像導引，非禁用）"
  },
  {
    "id": "111-2_medicine-6_009",
    "category": "麻醉科",
    "key_point": "敗血性休克引發的多重器官併發症與代射改變（高血糖與胰島素抗性）。",
    "explanation": "【題幹解析】\n本題屬於麻醉/重症科。題幹描述敗血性休克常併發多重器官的問題，詢問何者敘述錯誤。需要瞭解敗血症在血液系統（血小板低下、DIC）、消化系統（壓力性潰瘍）以及內分泌代謝系統（胰島素抗性與血糖變化）的病理生理變化。\n\n【選項詳解】\n- A. 產生胰島素抗性(insulin resistance),常導致低血糖：錯誤。敗血症與敗血性休克會引起人體劇烈的壓力反應，釋放大量升糖素、皮質醇、生長激素與兒茶酚胺，並產生顯著的胰島素抗性。這些變化會導致「高血糖」（stress-induced hyperglycemia），而非低血糖。\n- B. 因為血小板的活化與凝集,常導致血小板低下,是敗血症的早期病徵之一：正確。敗血症時，發炎反應會活化血管內皮並引發凝血反應，使血小板在微血管內大量活化與凝集，進而造成外周血小板數值下降，是敗血症早期非常具指標性的病徵。\n- C. 常併發瀰漫性血管內凝血(disseminated intravascular coagulation)：正確。敗血症常藉由組織因子（tissue factor）活化外源性凝血路徑，導致微血管內廣泛血栓形成，最終因消耗凝血因子與血小板而引發瀰漫性血管內凝血（DIC）。\n- D. 因為胃黏膜的壓力性潰瘍,常導致上消化道出血：正確。休克時，人體為了維持心腦灌流，會造成內臟（包括胃腸道）血流灌流極度不足，胃黏膜屏障受損，極易引發急性壓力性潰瘍（stress ulcer）並導致上消化道出血。\n\n【核心考點】\n敗血性休克的病理生理學：嚴重的壓力反應引發「高血糖」而非低血糖；血小板低下與 DIC 的機制；腸胃道灌流不足引起壓力性潰瘍與出血。",
    "flashcard_front": "敗血性休克 / 胰島素抗性 / 壓力性高血糖 / 瀰漫性血管內凝血 (DIC) / 血小板低下",
    "flashcard_back": "敗血性休克因劇烈壓力反應與胰島素抗性，常導致高血糖（而非低血糖）；血小板低下為其早期病徵之一。",
    "flashcard_summary": "敗血性休克血糖變化 -> 壓力反應與胰島素抗性導致高血糖"
  },
  {
    "id": "111-2_medicine-6_010",
    "category": "眼科",
    "key_point": "老年黃斑部病變（AMD）使用 anti-VEGF 治療的臨床指徵（脈絡膜新生血管 CNV）。",
    "explanation": "【題幹解析】\n本題考查老年黃斑部病變（Age-related Macular Degeneration, AMD）的治療原則。題目詢問病患若出現何種病徵，最適宜使用「血管內皮生長因子拮抗劑（anti-VEGF agents）」進行治療。\n\n【選項詳解】\n- A. 玻璃膜疣(drusen)：錯誤。Drusen 是視網膜色素上皮（RPE）下方的代謝廢物堆積，為乾性老年黃斑部病變（dry AMD）的典型早期表徵，此時通常只需追蹤或服用葉黃素等營養品，不適用 anti-VEGF 治療。\n- B. 視網膜色素上皮萎縮(RPE atrophy)：錯誤。RPE 萎縮代表乾性黃斑部病變進展至晚期的地理狀萎縮（geographic atrophy），此時視網膜細胞已退化，無法使用 anti-VEGF 逆轉。\n- C. 脈絡膜新生血管(choroidal neovascularization)：正確。脈絡膜新生血管（CNV）是濕性（滲出性）老年黃斑部病變（wet AMD）的核心病理特徵。這些新生血管管壁脆弱，極易滲漏出血，導致黃斑部水腫與急遽視力喪失。由於 VEGF 在 CNV 的形成與滲漏中扮演關鍵角色，因此眼內注射 anti-VEGF 藥物為濕性 AMD 的黃金標準治療。\n- D. 盤狀疤痕(disciform scarring)：錯誤。盤狀疤痕是 CNV 長期未治療或病變晚期機化後形成的纖維化疤痕，此時感光細胞已永久受損且新生血管已消退，使用 anti-VEGF 治療並無效果。\n\n【核心考點】\n老年黃斑部病變（AMD）的分類與治療：乾性 AMD（drusen、RPE 萎縮）與濕性 AMD（CNV、盤狀疤痕）；anti-VEGF 僅適用於活動性「脈絡膜新生血管（CNV）」，晚期盤狀疤痕則不適用。",
    "flashcard_front": "老年黃斑部病變 (AMD) / anti-VEGF / 脈絡膜新生血管 (CNV) / 玻璃膜疣 (Drusen) / 盤狀疤痕",
    "flashcard_back": "anti-VEGF 藥物主要用於治療濕性黃斑部病變的「脈絡膜新生血管 (CNV)」，對乾性病變及晚期纖維化盤狀疤痕無效。",
    "flashcard_summary": "anti-VEGF 治療黃斑部病變指徵 -> 脈絡膜新生血管 (CNV)"
  }
]

apply(updates)
