import json

updates = [
  {
    "id": "112-1_medicine-4_011",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "嬰兒膽汁滯留症（cholestasis）中肝內與肝外病因之臨床分類與診斷。",
    "explanation": "【題幹解析】\n嬰兒膽汁滯留症（cholestasis）依病變位置可劃分為「肝內（intrahepatic）」與「肝外（extrahepatic）」兩大類。臨床上區分這兩者對於評估是否需進行外科手術（如葛西手術 Kasai portal enterostomy）至關重要。\n\n【選項詳解】\n- A. 說明：膽道閉鎖（biliary atresia）是由於肝外大膽管發生進行性、發炎性纖維化與阻塞，為最常見且最具代表性的肝外膽汁滯留症，需儘快接受葛西手術，故選 A。\n- B. 說明：拜勒病（Byler disease，即進行性家族性肝內膽汁滯留症第1型 PFIC-1）是由於 ATP8B1 基因突變導致毛細膽管膜蛋白異常，膽汁排出受阻，屬於肝內膽汁滯留症。\n- C. 說明：阿拉吉歐症候群（Alagille syndrome）為體染色體顯性遺傳病（多涉及 JAG1 基因突變），其組織學典型特徵是肝內小膽管稀少（bile duct paucity），屬於肝內膽汁滯留症。\n- D. 說明：新生兒肝炎（neonatal hepatitis）為多種病毒感染或代謝異常引發的肝細胞發炎與膽汁鬱積，病變位於肝實質內，屬於肝內膽汁滯留症。\n\n【核心考點】\n新生兒膽汁滯留症之分類（膽道閉鎖為肝外膽汁滯留；阿拉吉歐症候群、PFIC與新生兒肝炎為肝內膽汁滯留）。",
    "flashcard_front": "嬰兒膽汁滯留 (cholestasis) / 肝外 (extrahepatic) 典型代表疾病 / 肝內與肝外分類",
    "flashcard_back": "膽道閉鎖（biliary atresia）屬於肝外膽汁滯留；阿拉吉歐症候群（肝內小膽管稀少）與拜勒病則為肝內膽汁滯留。",
    "flashcard_summary": "嬰兒膽汁滯留分類 -> 膽道閉鎖為肝外膽汁滯留；阿拉吉歐症候群與拜勒病屬肝內膽汁滯留。"
  },
  {
    "id": "112-1_medicine-4_012",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "SIADH 的診斷標準、實驗室數據特徵與稀釋性效應影響。",
    "explanation": "【題幹解析】\n抗利尿激素不適當分泌症候群（SIADH）是由於 ADH 不當且過度分泌，導致體內水分過度重吸收，進而引發稀釋性低血鈉、低血液滲透壓、尿滲透壓不適當升高，以及細胞外液容積擴張（等容性低血鈉）。\n\n【選項詳解】\n- A. 說明：診斷 SIADH 前，必須先排除其他會導致水腫或有效循環血容積降低的疾病（如腎病症候群、肝硬化、心衰竭），以及內分泌功能低下（甲狀腺、腎上腺皮質功能低下）、利尿劑使用或真性脫水等引發低血鈉的病因，此敘述正確。\n- B. 說明：在低血液滲透壓（< 275 mOsm/kg H2O）的生理狀態下，人體正常應最大稀釋尿液；但 SIADH 患者因 ADH 持續作用，尿液無法適當稀釋，尿液滲透壓通常仍高於 100 mOsm/kg，此敘述正確。\n- C. 說明：SIADH 的根本問題在於「水分滯留」，故第一線治療為嚴格「限制水分攝取」（水限制）。因為體內鈉總量並未減少且處於相對多水狀態，通常不需常規限制鈉鹽的攝取，此敘述正確。\n- D. 說明：因 ADH 導致水分在體內大量滯留，血液被顯著稀釋，加上腎小球濾過率與近端腎小管對尿酸等物質的重吸收受稀釋效應與容量擴張影響，患者血液中的尿素氮（BUN）與尿酸（uric acid）數值通常會「偏低」（常呈 extreme washout），而非偏高，故此選項敘述最不適當，為正確答案。\n\n【核心考點】\nSIADH 的實驗室數據特徵（低血鈉、低血液滲透壓、高尿滲透壓、低 BUN 與低尿酸）。",
    "flashcard_front": "SIADH / 實驗室診斷指標 / 血液稀釋效應 (BUN、尿酸) / 尿滲透壓表現",
    "flashcard_back": "SIADH 因水分滯留使血液稀釋，BUN 與尿酸濃度常「偏低」；低血鈉與低血滲透壓下，尿液滲透壓仍 > 100 mOsm/kg（不適當升高）。",
    "flashcard_summary": "SIADH 實驗室特徵 -> 因水分滯留稀釋，BUN與尿酸數值偏低，尿液滲透壓在低血鈉下仍大於 100 mOsm/kg。"
  },
  {
    "id": "112-1_medicine-4_013",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "兒童重度高鈉性脫水之急救原則與降鈉安全速度限制。",
    "explanation": "【題幹解析】\n5 歲病童高熱、嚴重嘔吐腹瀉 4 天且無法進食，呈現低血壓休克（72/50 mmHg）以及重度高鈉血症（175 mEq/L）。急救須先穩定生命徵象，隨後必須極度小心、緩慢地矯正高血鈉，以防止腦細胞滲透壓失衡引發的嚴重神經併發症。\n\n【選項詳解】\n- A. 說明：重度高血鈉時，大腦細胞會產生特異性有機溶質（idiogenic osmole）以維持細胞體積防止萎縮。此時若在 24 小時內過快將血鈉降至正常，會導致大腦外部滲透壓驟降，水分快速移入大腦細胞，引發嚴重腦水腫與癲癇發作。血鈉矯正通常需維持在 48 至 72 小時內緩慢下降（降速限制：每小時降幅不超過 0.5 mEq/L，或每天不超過 10-12 mEq/L），故此選項極度不適當且危險，為正確答案。\n- B. 說明：病童已呈低血壓休克狀態，急救首要步驟是立即給予等張晶體溶液（生理食鹽水 20 mL/kg）於 10 至 20 分鐘內快速輸注，以重建循環容量、保護重要器官灌流，此處置適當。\n- C. 說明：在循環灌流穩定後，後續的維持液與脫水矯正應使用低張溶液（如 5% dextrose + half-normal saline），使其血鈉能以安全、緩慢的速度逐漸下降，此處置適當。\n- D. 說明：高鈉血症在過快矯正時，水分快速向腦細胞內轉移，最嚴重的併發症即為致命性腦水腫（brain edema）、癲癇（seizure）甚至昏迷，此敘述正確。\n\n【核心考點】\n高鈉性脫水（hypernatremic dehydration）的補水矯正原則（休克先給等張生理食鹽水，後續緩慢降鈉，降速限於 48-72 小時內）。",
    "flashcard_front": "兒童重度高鈉性脫水 / 降血鈉安全速度與時間 / 快速矯正之致命併發症",
    "flashcard_back": "休克先給等張生理食鹽水；穩定後應於 48-72 小時緩慢降鈉（每天 < 10-12 mEq/L），過快矯正（24小時內降至正常）會引發致命性腦水腫與癲癇。",
    "flashcard_summary": "高鈉性脫水矯正 -> 須於 48-72 小時內緩慢降鈉，避免 24 小時內快速降至正常以防腦水腫與癲癇。"
  },
  {
    "id": "112-1_medicine-4_014",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "兒童腎臟移植後原發疾病於移植腎的復發率比較。",
    "explanation": "【題幹解析】\n兒童因末期腎臟病進行腎臟移植後，原發疾病可能在供體腎（移植腎）中復發，嚴重影響移植物存活率。理解不同原發疾病的復發風險有助於術前評估與術後監測。\n\n【選項詳解】\n- A. 說明：先天性腎病症候群（congenital nephrotic syndrome，如芬蘭型）主要是由基因突變（如編碼足細胞蛋白 nephrin 的 NPHS1 基因突變）引起。由於移植的供體腎本身不具備該基因突變，其足細胞結構蛋白完全正常，因此該病在移植腎復發的機率極低（幾近為零），故選 A。\n- B. 說明：局部腎絲球硬化症（FSGS）的復發率相當高，特別是在特發性（idiopathic）或有循環因子（circulating permeability factor）作用的患者中，移植後復發率約 30% 至 50%。\n- C. 說明：第二型膜增生性腎小球腎炎（MPGN type II，又稱緻密沉積物病 Dense Deposit Disease）與補體替代途徑異常調節密切相關，移植後的復發率極高，接近 80% 至 100%。\n- D. 說明：IgA 腎病變（IgA nephropathy）在移植後也有相當高的復發率（約 30% 至 40%），常伴隨系膜區 IgA 免疫複合物的再次沉積。\n\n【核心考點】\n兒童腎移植後疾病復發率（基因缺陷型疾病如先天性腎病症候群復發率最低，而 MPGN II 與 FSGS 等體液因子/免疫介導疾病復發率高）。",
    "flashcard_front": "兒童腎移植後復發率 / 遺傳基因缺陷型 vs 免疫體液型疾病 / 復發率最低疾病",
    "flashcard_back": "芬蘭型先天性腎病症候群由基因突變所致，移植正常腎不具該突變，故復發率最低；MPGN II（80-100%）與 FSGS（30-50%）復發率高。",
    "flashcard_summary": "腎移植後復發率 -> 基因突變之先天性腎病症候群復發率最低，MPGN II 及 FSGS 復發率高。"
  },
  {
    "id": "112-1_medicine-4_015",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "貝塞特氏病（Behçet's disease）的臨床特徵（潰瘍瘢痕特點、針刺反應與最常見眼部病變）。",
    "explanation": "【題幹解析】\n貝塞特氏病（Behçet's disease）是一種全身性慢性血管炎，典型表現為反覆性口腔潰瘍、生殖器潰瘍、眼部病變（葡萄膜炎）與皮膚病變，病因涉及中性粒細胞過度活化與血管發炎。\n\n【選項詳解】\n- A. 說明：貝塞特氏病的口腔潰瘍（oral ulcer）多為痛性，通常在 3-10 天內會自然修復癒合，且癒合後通常「不會留下疤痕（結痂）」，此敘述正確。\n- B. 說明：相較於口腔潰瘍，生殖器潰瘍（genital ulcer）通常侵犯較深、病灶較大，癒合過程較慢，且極容易留下白色瘢痕（疤痕），此敘述正確。\n- C. 說明：貝塞特氏病眼部受累會造成葡萄膜炎（uveitis）。在臨床上，最常累及整隻眼睛，表現為「全葡萄膜炎（panuveitis）」（包括前房積膿與視網膜血管炎），而非單純或最常見的「後葡萄膜炎」，故此選項敘述最不適當，為正確答案。\n- D. 說明：針刺試驗（pathergy test）為本病高度特異性診斷工具，做法是用無菌細針斜刺前臂皮膚，若在 24 至 48 小時後，刺入點出現無菌性丘疹或膿皰反應（pustular reaction），即判定為陽性，此敘述正確。\n\n【核心考點】\n貝塞特氏病眼部最常見病變為全葡萄膜炎（panuveitis）、黏膜潰瘍癒合特徵（生殖器易留疤，口腔不留疤）與針刺反應之診斷方法。",
    "flashcard_front": "貝塞特氏病 (Behçet's) / 眼部葡萄膜炎最常見類型 / 口腔與生殖器潰瘍留疤差異 / 針刺試驗 (pathergy test)",
    "flashcard_back": "最常見眼部病變為「全葡萄膜炎（panuveitis）」；口腔潰瘍不留疤，生殖器潰瘍易留疤；針刺試驗陽性指針刺後 24-48 小時出膿皰。",
    "flashcard_summary": "貝塞特氏病臨床特徵 -> 最常見眼病變為全葡萄膜炎；生殖器潰瘍留疤，口腔潰瘍不留疤；針刺試驗 24-48 小時內出膿皰。"
  },
  {
    "id": "112-1_medicine-4_016",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "Bruton 氏無球蛋白血症（XLA）的遺傳模式、臨床特徵與治療方案。",
    "explanation": "【題幹解析】\nBruton 氏無球蛋白血症（X-linked agammaglobulinemia, XLA）是由於 BTK 基因突變，導致 B 細胞發育在原 B 細胞（pro-B）階段受阻，無法分化為成熟 B 細胞，進而造成體內缺乏各類免疫球蛋白。\n\n【選項詳解】\n- A. 說明：本病為典型的 B 細胞先天性液體免疫缺失症，B 淋巴球發育完全停滯，外周血中幾乎測不到 B 細胞（CD19+ B cells < 1%），此敘述正確。\n- B. 說明：本病遺傳模式為「X 聯鎖隱性遺傳」（X-linked recessive），其致病基因位於 X 染色體上，因此幾乎均為男性發病，女性多為無症狀攜帶者，男女得病比例絕對非 1:1，故此選項敘述最不適當，為正確答案。\n- C. 說明：新生兒在出生後的頭幾個月內，體內有來自母體的 IgG 抗體保護。通常在出生後 6 至 9 個月，母體抗體衰退至極低水平時，患兒才開始出現反覆的中耳炎、鼻竇炎、肺炎等細菌性感染症狀，此敘述正確。\n- D. 說明：由於患兒自身完全無法產生抗體，定期（通常每 3 至 4 週）輸注靜脈注射免疫球蛋白（IVIG）以維持體內 IgG 水平是預防感染、最主要且有效的治療方法，此敘述正確。\n\n【核心考點】\nX 聯鎖隱性遺傳疾病的遺傳特徵（主要累及男性）以及 Bruton 氏無球蛋白血症發病時機與 IVIG 治療。",
    "flashcard_front": "Bruton 氏無球蛋白血症 (XLA) / 遺傳方式與好發性別 / 發病時機與生理抗體變化 / 治療策略",
    "flashcard_back": "XLA 屬 X 聯鎖隱性遺傳，幾乎全為男性發病（非男女 1:1）；多在生後 6-9 個月母體抗體消失後發病，定期輸注 IVIG 為主治療。",
    "flashcard_summary": "Bruton 無球蛋白血症 -> 屬X聯鎖隱性遺傳且主要累及男性，生後 6-9 個月發病，治療為定期輸注 IVIG。"
  },
  {
    "id": "112-1_medicine-4_017",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "氣喘急性發作（阻塞性肺病）在肺功能檢查中的各項指標變化特徵。",
    "explanation": "【題幹解析】\n氣喘發作是典型的急性氣道炎症與可逆性氣道阻塞（obstruction）。在肺功能檢查（PFT）中，主要影響氣體「呼出」的流速，而非肺部的絕對容積。\n\n【選項詳解】\n- A. 說明：尖峰呼氣流速（PEF）反映了大氣道的呼氣流速，在氣道痙攣與阻塞時會顯著降低，是居家監測氣喘發作的指標，此數值會降低。\n- B. 說明：第一秒用力呼氣量（FEV1）反映了呼氣第一秒內排出的氣體總量，是評估氣道阻塞嚴重度的金標準，在氣喘發作時會顯著降低，此數值會降低。\n- C. 說明：第一秒流速容積比（FEV1/FVC）是診斷阻塞性肺病的關鍵指標，在氣喘急性發作時，因 FEV1 的下降幅度大於用力肺活量（FVC），該比例會明顯降低（通常 < 70%-75%），此數值會降低。\n- D. 說明：肺總容量（total lung capacity, TLC）指最大吸氣後肺內所含的氣體量。在氣喘急性發作時，由於支氣管痙攣和黏液阻塞，氣體無法順利呼出，會造成嚴重的「空氣滯留（air trapping）」，進而導致肺殘氣量（RV）與肺總容量（TLC）呈現代償性「增加或維持正常」，絕不可能降低，故選 D。\n\n【核心考點】\n阻塞性肺病（如氣喘發作）之肺功能特徵：呼氣流速指標（FEV1, PEF, FEV1/FVC）降低；殘氣量與肺總容量（RV, TLC）正常或增加。",
    "flashcard_front": "氣喘急性發作 / 阻塞性肺功能變化 / 呼氣流速 (FEV1/FVC) vs 肺容積 (TLC)",
    "flashcard_back": "氣喘急性發作時，FEV1、PEF、FEV1/FVC 均降低；肺總容量（TLC）與殘氣量（RV）會因空氣滯留而「正常或升高」，絕不降低。",
    "flashcard_summary": "氣喘發作肺功能指標 -> FEV1、PEF 與 FEV1/FVC 降低；肺總容量（TLC）因空氣滯留而正常或增加，不降低。"
  },
  {
    "id": "112-1_medicine-4_018",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "常見遺傳性血液與代謝疾病之遺傳模式辨識（性聯遺傳 vs 體染色體遺傳）。",
    "explanation": "【題幹解析】\n本題考查臨床常見遺傳性疾病的傳遞方式。考生需熟悉哪些疾病為 X 聯鎖（性聯）遺傳，哪些為體染色體遺傳。\n\n【選項詳解】\n- A. 說明：A 型血友病（hemophilia A）是由於第八凝血因子（factor VIII）缺陷引起，屬於經典的 X 聯鎖隱性遺傳（X-linked recessive）疾病。\n- B. 說明：遺傳性球形紅血球增多症（hereditary spherocytosis, HS）最常累及紅血球膜蛋白（如 ankyrin-1 或 spectrin）的基因異常。其遺傳模式主要是「體染色體顯性遺傳（autosomal dominant, AD）」，約佔 75%，少數為體染色體隱性遺傳（AR），並不屬於性聯遺傳，故選 B。\n- C. 說明：蠶豆症（G6PD deficiency）是由於 G6PD 基因突變所致，是台灣最常見的 X 聯鎖隱性遺傳疾病之一。\n- D. 說明：法布瑞氏症（Fabry disease）是由於 GLA 基因突變導致 α-galactosidase A 酵素活性缺乏，屬於 X 聯鎖隱性遺傳的溶小體儲積症，近年在台灣已有新生兒全面篩檢。\n\n【核心考點】\n常見疾病之遺傳模式（HS 為體染色體顯性/隱性；血友病A、蠶豆症、法布瑞氏症為性聯遺傳）。",
    "flashcard_front": "常見血液與代謝疾病遺傳模式 / 性聯遺傳 (X-linked) 疾病代表 / 遺傳性球形紅血球症 (HS)",
    "flashcard_back": "A 型血友病、G6PD 缺乏症、法布瑞氏症均為性聯遺傳（X-linked）；遺傳性球形紅血球增多症（HS）為體染色體遺傳（多為 AD）。",
    "flashcard_summary": "遺傳模式辨識 -> 血友病 A、蠶豆症、法布瑞氏症為性聯遺傳；遺傳性球形紅血球症（HS）為體染色體遺傳。"
  },
  {
    "id": "112-1_medicine-4_019",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "兒童缺鐵性貧血（IDA）實驗室診斷數據特徵與鐵劑補充初期反應。",
    "explanation": "【題幹解析】\n本題考查缺鐵性貧血（iron deficiency anemia, IDA）的病生理特徵、鐵代謝實驗室指標（ferritin、TIBC、transferrin saturation）以及給予鐵劑治療後的血液動力學反應。\n\n【選項詳解】\n- A. 說明：新生兒延遲斷臍（delayed cord clamping）1 至 3 分鐘，可使胎盤血流充分流入新生兒體內，能增加其體內鐵儲存量（增加儲存鐵約 40-50 mg/kg），進而顯著降低嬰兒期缺鐵性貧血的發生率，此敘述正確。\n- B. 說明：青春期女性由於月經週期的經血流失，加上生長發育快速（成長衝刺期對鐵需求量增加）與飲食攝取可能不均衡，是缺鐵性貧血的高好發族群，此敘述正確。\n- C. 說明：缺鐵性貧血時，體內儲存鐵耗竭，故血清鐵蛋白（ferritin）顯著降低。同時，因運鐵蛋白（transferrin）代償性上升，且血清鐵（serum iron）低下，會導致運鐵蛋白飽和度（transferrin saturation = serum iron / TIBC）「降低」（通常小於 16%），而非高飽和度，故此選項敘述最不適當，為正確答案。\n- D. 說明：開始口服或靜脈鐵劑補充後，骨髓造血系統被活化，約 2 至 3 天後外周血即可觀察到網狀紅血球（reticulocyte）數量開始顯著增多，約在 5-10 天達到高峰，此為鐵劑治療反應良好的早期敏感指標，此敘述正確。\n\n【核心考點】\n缺鐵性貧血（IDA）實驗室診斷（ferritin 降低、TIBC 升高、運鐵蛋白飽和度降低）與鐵劑治療早期指標（網狀紅血球上升）。",
    "flashcard_front": "缺鐵性貧血 (IDA) / 鐵蛋白 (ferritin) 與運鐵蛋白飽和度 (TSAT) 變化 / 鐵劑療效早期指標",
    "flashcard_back": "IDA 的 ferritin 降低，運鐵蛋白飽和度（TSAT）降低；口服鐵劑後，網狀紅血球（Reticulocyte）會在 2-3 天內增加，為最早的療效指標。",
    "flashcard_summary": "IDA 診斷與療效指標 -> 實驗室顯示 ferritin 與運鐵蛋白飽和度降低；補充鐵劑 2-3 天後網狀紅血球會增多。"
  },
  {
    "id": "112-1_medicine-4_020",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "常用化療藥物及其典型特異性器官毒性副作用配對與禁忌。",
    "explanation": "【題幹解析】\n小兒血液腫瘤科的化學治療中，各類藥物因其化學結構與作用機轉不同，具有特定的器官毒性（organ-specific toxicity）。臨床醫師需熟悉這些副作用以進行適時的監測與預防。\n\n【選項詳解】\n- A. 說明：小紅莓類藥物 doxorubicin 具有累積性心臟毒性（cardiotoxicity），可引起擴大性心肌病變與心衰竭，臨床需定期監測心臟超音波，此配對正確。\n- B. 說明：出血性膀胱炎（hemorrhagic cystitis）是烷基化劑環磷醯胺（cyclophosphamide）或異環磷醯胺（ifosfamide）的典型特異性毒性，是由於其代謝產物丙烯醛（acrolein）直接刺激膀胱黏膜所致。而長春新鹼（vincristine）的限制性毒性主要為「周邊神經毒性」（例如便秘、深部腱反射減弱、垂足等）與抗利尿激素分泌異常（SIADH），並非出血性膀胱炎，故此組合較不相關，為正確答案。\n- C. 說明：博來黴素 bleomycin 具有肺部毒性，易引發間質性肺炎與不可逆的肺部纖維化（pulmonary fibrosis），特別在接受高濃度氧氣治療時易惡化，此配對正確。\n- D. 說明：L-asparaginase（天門冬醯胺酶）會干擾蛋白質合成，其典型副作用包括急性胰臟炎（pancreatitis）、凝血因子缺乏引發血栓或出血、以及高血糖，此配對正確。\n\n【核心考點】\n經典化療藥物之特異性毒性（Cyclophosphamide -> 出血性膀胱炎；Vincristine -> 周邊神經毒性；Doxorubicin -> 心臟毒性；Bleomycin -> 肺纖維化）。",
    "flashcard_front": "化療藥物特異性毒性 / 出血性膀胱炎致病藥物 / Vincristine 限制性毒性 / 心肺毒性藥物配對",
    "flashcard_back": "出血性膀胱炎由 cyclophosphamide/ifosfamide 引起的 acrolein 毒性所致；vincristine 的限制性毒性為周邊神經毒性，而非膀胱炎。",
    "flashcard_summary": "化療藥物毒性配對 -> cyclophosphamide 可致出血性膀胱炎；vincristine 具周邊神經毒性；doxorubicin 具心臟毒性，bleomycin 具肺纖維化。"
  }
]

with open("scratch/updates_2.json", "w", encoding="utf-8") as f:
    json.dump(updates, f, ensure_ascii=False, indent=2)

print("Generated scratch/updates_2.json successfully.")
