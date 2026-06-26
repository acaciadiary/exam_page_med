import json
from pathlib import Path

updates = [
  {
    "id": "112-1_medicine-5_021",
    "category": "心臟外科",
    "key_point": "下肢動脈阻塞（PAD）的 Fontaine 分類中，Stage III 代表缺血性靜息痛（ischemic rest pain）。",
    "explanation": "【題幹解析】\n下肢慢性動脈阻塞疾病（PAD/PAOD）的 Fontaine 分類法是評估肢體缺血嚴重度的經典指標，共分為四個階段（Stage I 至 IV）。\n\n【選項詳解】\n- A. 錯誤。組織喪失（Tissue loss，包括潰瘍與壞死）屬於最嚴重的「Stage IV」，而非 Stage I。\n- B. 錯誤。壞死（Gangrene）同樣屬於「Stage IV」，而非 Stage II。\n- C. 正確。Fontaine 分類的定義如下：\n  - Stage I：無症狀（Asymptomatic）或輕微感覺異常。\n  - Stage II：間歇性跛行（Intermittent claudication）。\n  - Stage III：缺血性靜息痛（Ischemic rest pain，躺下時尤甚，因失去重力輔助灌流）。\n  - Stage IV：潰瘍或壞死（Ulceration / Gangrene / Tissue loss）。\n- D. 錯誤。間歇性跛行（Claudication）屬於「Stage II」，而非 Stage IV。\n\n【核心考點】\n下肢動脈硬化阻塞症（PAOD）的 Fontaine 分期標準：I期無症狀、II期跛行、III期靜息痛、IV期潰瘍壞死。",
    "flashcard_front": "下肢動脈阻塞 / Fontaine 分期 / 靜息痛分期 / 壞死與跛行分期",
    "flashcard_back": "Fontaine 分期：I無症狀、II間歇性跛行、III為「靜息痛」、IV為「潰瘍或壞死（組織喪失）」。",
    "flashcard_summary": "Fontaine分期 -> I無症狀，II跛行，III靜息痛，IV潰瘍壞死。"
  },
  {
    "id": "112-1_medicine-5_022",
    "category": "心臟外科",
    "key_point": "馬凡氏症（Marfan syndrome）是由於第15號染色體上編碼微纖維蛋白-1（fibrillin-1）的基因突變所致。",
    "explanation": "【題幹解析】\n馬凡氏症（Marfan syndrome）是一種自體顯性遺傳的結締組織疾病，臨床特徵包括骨骼畸形（高瘦、指距長）、眼部晶體脫位，以及最致命的心血管病變（主動脈瘤、主動脈剝離、二尖瓣脫垂）。\n\n【選項詳解】\n- A. 錯誤。彈性蛋白（Elastin）是結締組織中的重要成分，但在馬凡氏症中並非直接突變異常的蛋白質（雖然微纖維蛋白結構異常會影響彈性纖維的組裝）。\n- B. 錯誤。基質金屬蛋白酶（Metalloproteinase, MMP）在主動脈壁重塑中扮演角色，但在馬凡氏症中其活性增加是繼發性的，而非基因突變的直接產物。\n- C. 錯誤。膠原蛋白（Collagen）異常與埃勒斯-當洛二氏症候群（Ehlers-Danlos syndrome）及骨生成不全症（Osteogenesis imperfecta）有關，非馬凡氏症的主因。\n- D. 正確。馬凡氏症的致病基因是位於第 15 號染色體長臂的 FBN1 基因，該基因編碼「微纖維蛋白-1（fibrillin-1）」。此蛋白質是細胞外基質微原纖維（microfibrils）的主要成分，異常會導致結締組織失去張力並引發TGF-beta信號通路過度活化。\n\n【核心考點】\n馬凡氏症的分子遺傳學病因：FBN1 基因突變導致微纖維蛋白-1（fibrillin-1）缺陷；心血管主要風險為升主動脈瘤與剝離。",
    "flashcard_front": "馬凡氏症 / 遺傳與突變蛋白 / 心血管併發症 / FBN1 基因",
    "flashcard_back": "是由於「微纖維蛋白-1 (fibrillin-1)」基因（FBN1）異常所致，常導致「升主動脈根部擴張與剝離」，屬自體顯性遺傳。",
    "flashcard_summary": "馬凡氏症病因 -> FBN1基因突變導致微纖維蛋白-1（fibrillin-1）異常，易引發主動脈剝離。"
  },
  {
    "id": "112-1_medicine-5_023",
    "category": "心臟外科",
    "key_point": "全肺靜脈異常（TAPVC）根治手術中，標準做法是截斷或結紮垂直靜脈（vertical vein），以防血液分流與右心負荷過重。",
    "explanation": "【題幹解析】\n全肺靜脈回流異常（TAPVC）是一種發紺型先天性心臟病，所有肺靜脈不回流至左心房，而是經由異常交通管道（如垂直靜脈 vertical vein）回流至右心房系統。手術重建的目標是將肺靜脈總腔與左心房吻合，使肺靜脈血順利流入左心房。\n\n【選項詳解】\n- A. 正確（敘述錯誤）。在進行 TAPVC 的根治手術時，標準處置是「結紮並切斷（ligate and divide）垂直靜脈（vertical vein）」，強制所有肺靜脈血經由新做的吻合口回流至左心房。若保留垂直靜脈不截斷，術後血液仍會經由該血管流入右心系統，形成左向右分流（Left-to-right shunt），無法達到完全矯正的效果。\n- B. 錯誤（敘述正確）。無論是否有合併肺靜脈阻塞，單純性 TAPVC 患者一旦確診均應進行手術矯正。合併阻塞者（如 infracardiac type）為新生兒外科急症，需立即手術；無阻塞者也因右心負荷過重與發紺，需在數月內安排手術。\n- C. 錯誤（敘述正確）。無縫修復法（Sutureless repair）是在吻合口外圍進行縫合，可避免吻合口邊緣纖維化收縮，特別適合用於解決 TAPVC 術後再次發生肺靜脈狹窄（postoperative pulmonary vein stenosis）的棘手病患。\n- D. 錯誤（敘述正確）。目前超音波心圖（Echocardiography）及電腦斷層造影（CT angiography）已能提供極清晰的解剖構造，因此心導管（Cardiac catheterization）檢查在診斷 TAPVC 時已非必要，可避免侵入性檢查的風險。\n\n【核心考點】\nTAPVC的手術原理（吻合肺靜脈至左房，並結紮垂直靜脈）；分型（Supracardiac, Cardiac, Infracardiac）；術後再狹窄的無縫修復法（Sutureless repair）。",
    "flashcard_front": "TAPVC 手術 / 垂直靜脈處置 / 術後再狹窄修補 / 診斷工具選擇",
    "flashcard_back": "TAPVC 矯正術中，必須「結紮/截斷」垂直靜脈以防止術後左向右分流；術後再狹窄首選「無縫修復法 (Sutureless repair)」。",
    "flashcard_summary": "TAPVC手術處置 -> 必須結紮/截斷垂直靜脈；術後再狹窄使用無縫修復法。"
  },
  {
    "id": "112-1_medicine-5_024",
    "category": "心臟外科",
    "key_point": "動脈下心室中隔缺損（subarterial type VSD）最易因文氏效應（Venturi effect）吸附主動脈瓣葉，造成主動脈瓣脫垂與逆流。",
    "explanation": "【題幹解析】\n心室中隔缺損（VSD）依解剖位置分為四型：動脈下型（Subarterial, Type I）、膜底部型（Perimembranous, Type II）、流入道型（Inlet, Type III）與肌肉型（Muscular, Type IV）。其中某型與主動脈瓣關閉不全（AR）有著高度病理關聯。\n\n【選項詳解】\n- A. 錯誤。小的膜底部 VSD 有自行癒合可能，極少合併主動脈瓣脫垂。\n- B. 錯誤。大的膜底部 VSD 雖會導致左向右分流大與心衰竭，但與主動脈瓣脫垂的直接力學關聯性不及動脈下型高。\n- C. 正確。動脈下型 VSD（Subarterial type，又稱幹下型、supracristal 或 double committed VSD）緊鄰主動脈瓣及肺動脈瓣下方。在心臟收縮期，血液經此缺鎖高速噴射流入右心室，在主動脈瓣下方產生局部低壓（文氏效應 Venturi effect），進而將主動脈瓣（通常是右冠狀瓣葉 right coronary cusp）往缺損處牽拉吸附，導致主動脈瓣脫垂（aortic valve prolapse）與進行性主動脈瓣逆流（aortic regurgitation, AR）。此型一旦發現，即使分流量小，也應儘早手術修補以保護主動脈瓣。\n- D. 錯誤。肌肉型 VSD 四周皆為肌肉組織包繞，遠離主動脈瓣，不會造成主動脈瓣脫垂。\n\n【核心考點】\nSubarterial VSD (Type I) 的血流力學與併發症：藉由 Venturi 效應吸附主動脈瓣，極易引發主動脈瓣脫垂與主動脈瓣逆流（AR），為早期手術指徵。",
    "flashcard_front": "心室中隔缺損 (VSD) / 主動脈瓣脫垂 / 逆流併發症 / 文氏效應",
    "flashcard_back": "「動脈下型 VSD (Subarterial, Type I)」最易因 Venturi 效應導致「主動脈瓣脫垂與逆流 (AR)」，一旦發現應盡早手術修補。",
    "flashcard_summary": "VSD與AR -> 動脈下型（Type I）VSD最易合併主動脈瓣脫垂及逆流，需早期手術。"
  },
  {
    "id": "112-1_medicine-5_025",
    "category": "胸腔外科",
    "key_point": "胃食道逆流（GERD）可引起氣喘等食道外症狀；其首選治療為藥物而非手術，且不具食道弛緩症的巨大食道病變。",
    "explanation": "【題幹解析】\n胃食道逆流疾病（GERD）的臨床表現（包括典型胸口灼熱與食道外症狀如氣喘、咳嗽）、治療原則及與食道弛緩症（Achalasia）的鑑別診斷。\n\n【選項詳解】\n- A. 錯誤。胃食道逆流的「最優先且最佳」治療首選是「內科藥物治療」（如質子幫浦抑制劑 PPI）與生活飲食習慣調整。微創手術（如 Nissen 反折術）僅保留給藥物療效不佳、無法耐受藥物副作用或合併巨大食道裂孔疝氣的特定患者，絕非最優先選擇。\n- B. 正確。胃食道逆流的胃酸與胃內容物微量吸入呼吸道，會刺激迷走神經並引發支氣管痙攣，臨床上常導致患者出現慢性咳嗽、咽喉炎甚至「氣喘（asthma）」症狀，此為常見的食道外表現（extraesophageal manifestations）。\n- C. 錯誤。胸口灼熱（heartburn，俗稱「燒心」）是胃食道逆流「最經典、最常見」的症狀，亦需與心肌梗塞的胸痛進行鑑別診斷，但並非很少發生在 GERD 患者身上。\n- D. 錯誤。食道弛緩症（Achalasia）因下食道括約肌（LES）無法放鬆且食道失去蠕動，導致食物長期淤積於食道，進而發生嚴重的病理性擴張，稱為巨大食道（megaesophagus）。而 GERD 主要是 LES 鬆弛導致胃酸逆流，雖然長期可導致食道發炎或狹窄，但「不會」產生如食道弛緩症那樣的巨大食道。\n\n【核心考點】\nGERD 的食道外表現（氣喘、慢性咳）；首選治療（內科 PPI 藥物）；典型症狀（heartburn）；與 Achalasia（巨大食道、鳥嘴徵）的鑑別診斷。",
    "flashcard_front": "胃食道逆流 (GERD) / 首選治療 / 食道外症狀 / 巨大食道鑑別",
    "flashcard_back": "GERD 首選「藥物 (PPI) 治療」而非手術；可引發「氣喘/慢性咳嗽」等食道外症狀；「巨大食道」為食道弛緩症 (Achalasia) 之特徵而非 GERD。",
    "flashcard_summary": "GERD臨床處置 -> 藥物為首選治療，可引起氣喘，無巨大食道表現。"
  },
  {
    "id": "112-1_medicine-5_026",
    "category": "胸腔外科",
    "key_point": "食道鋇劑攝影呈現鳥嘴徵（bird's beak sign）是食道弛緩症（achalasia）的特徵，而非食道癌的診斷標準。",
    "explanation": "【題幹解析】\n評估食道癌的診斷流程、影像學表現、早期內視鏡治療策略，以及吞嚥困難的臨床警訊。\n\n【選項詳解】\n- A. 正確。胃食道鏡檢（panendoscopy）併病理切片（biopsy）是確認食道癌診斷的黃金標準。\n- B. 錯誤。在食道鋇劑攝影檢查中，發現下食道呈對稱性狹窄、上段食道擴張，呈現平滑的「鳥嘴徵（bird's beak sign）」，是「食道弛緩症（achalasia）」的特徵性影像表現。食道癌在鋇劑攝影上典型呈現為不規則的充盈缺損（filling defect）、黏膜破壞或「蘋果芯徵（apple-core sign）」。\n- C. 正確。對於侷限於黏膜層（T1a）的早期食道癌，施行內視鏡黏膜切除術（EMR）或內視鏡黏膜下剝離術（ESD）不僅是切除治療，切下的完整標本亦能提供精確的病理分級與腫瘤侵犯深度評估。\n- D. 正確。即使鋇劑攝影提示可能是功能性的食道蠕動異常（如 achalasia 或痙攣），但只要病人主訴有吞嚥困難（dysphagia，特別是進行性加重的固體食物吞嚥困難），必須安排胃鏡檢查以排除實體腫瘤（食道癌）壓迫阻塞的可能性。\n\n【核心考點】\n食道癌與食道弛緩症（Achalasia）的影像學鑑別（鳥嘴徵屬 Achalasia）；食道癌的內視鏡確診與早期 EMR/ESD 處置；吞嚥困難的鑑別診斷原則。",
    "flashcard_front": "食道鋇劑攝影 / 鳥嘴徵診斷 / 食道癌影像 / 吞嚥困難胃鏡指征",
    "flashcard_back": "鋇劑攝影「鳥嘴徵 (bird's beak)」為「食道弛緩症」特徵；食道癌呈不規則狹窄或充盈缺損；吞嚥困難者必做胃鏡排除癌症。",
    "flashcard_summary": "食道疾病影像 -> 鳥嘴徵為食道弛緩症之特徵；食道癌確診靠胃鏡切片。"
  },
  {
    "id": "112-1_medicine-5_027",
    "category": "胸腔外科",
    "key_point": "肺腺癌好發於女性與非吸菸者，易早期發生血行轉移（如腦轉移），機率顯著高於肺鱗狀細胞癌。",
    "explanation": "【題幹解析】\n比較肺癌主要病理類型（腺癌 adenocarcinoma 與鱗狀細胞癌 squamous cell carcinoma）的解剖學分佈、細胞來源與轉移傾向。\n\n【選項詳解】\n- A. 正確。肺腺癌（Adenocarcinoma）是目前台灣及全球最常見的肺癌組織型態，約佔所有肺癌的一半以上。\n- B. 正確。肺腺癌源自於支氣管及細支氣管上皮的黏液分泌細胞（mucus-producing / gland-forming cells），病理上常呈現腺體結構。\n- C. 正確。與多位於中央支氣管的鱗狀細胞癌與小細胞癌不同，肺腺癌大多位於肺部的「周邊（peripherally located）」，常侵犯胸膜。\n- D. 錯誤。肺腺癌在病程早期即極易經由血液循環發生遠端轉移，其中「腦轉移（brain metastasis）」的機率顯著高於肺鱗狀細胞癌（後者多呈局部侵犯，血行轉移較晚且較少）。\n\n【核心考點】\n肺腺癌的病理生理特徵：最常見、多周邊型、黏液分泌細胞來源、極易早期發生血行轉移（腦、骨、肝、腎上腺）。",
    "flashcard_front": "肺腺癌 / 解剖位置 / 轉移傾向 / 與鱗狀細胞癌對比",
    "flashcard_back": "肺腺癌多位於「周邊」，為最常見類型；與鱗狀細胞癌相比，較「容易」發生血行轉移至腦部、骨骼等器官。",
    "flashcard_summary": "肺腺癌特點 -> 好發於周邊，極易早期發生血行轉移（如腦轉移），高於鱗狀細胞癌。"
  },
  {
    "id": "112-1_medicine-5_028",
    "category": "胸腔外科",
    "point": "肺部類癌（carcinoid）整體預後佳，但因其 vasoactive 物質會被肺/肝臟代謝，故類癌症候群在典型類癌中極為罕見（<5%）。",
    "explanation": "【題幹解析】\n肺部類癌（Bronchopulmonary carcinoid）屬於神經內分泌腫瘤（NET），分為典型類癌（Typical carcinoid，低惡性度）與非典型類癌（Atypical carcinoid，中惡性度）。\n\n【選項詳解】\n- A. 正確。典型類癌分化良好，無壞死且有絲分裂極少，術後5年存活率大於90-95%，預後在所有肺部神經內分泌腫瘤中最佳。\n- B. 錯誤。雖然類癌細胞會分泌血清素（serotonin）等血管活性物質，但肺部類癌釋放的物質進入體循環前，常在肺部或經由肝臟首渡效應被代謝清除。因此，類癌症候群（Carcinoid syndrome，如面部潮紅、腹瀉、支氣管痙攣）在「典型類癌（Typical carcinoid）」中「極其罕見」（發生率<2-5%），多僅在有廣泛肝臟轉移的病例中才見到。\n- C. 正確。非典型類癌惡性度較高（可見局部壞死與較多有絲分裂），具有侵襲性，約有20-50%的病例會發生淋巴結或遠端轉移。\n- D. 正確。無論是典型或非典型類癌，主要且首選的根治性治療方式均為手術切除（如肺葉切除併淋巴結廓清）。\n\n【核心考點】\n肺部神經內分泌腫瘤分類與預後（典型最佳，非典型易轉移）；類癌症候群的發生率極低（因肝肺代謝）；手術為主要切除手段。",
    "flashcard_front": "肺類癌 / 典型 vs 非典型 / 類癌症候群發生率 / 首選治療",
    "flashcard_back": "典型類癌預後極佳，但「類癌症候群」在其「極罕見」（<5%）；非典型類癌惡性度高易轉移；兩者皆以「手術切除」為主。",
    "flashcard_summary": "肺部類癌 -> 典型類癌預後好但類癌症候群罕見；非典型惡性度高；首選手術。"
  },
  {
    "id": "112-1_medicine-5_029",
    "category": "胸腔外科",
    "key_point": "肺臟創傷手術中，縫合深部裂傷有空氣栓塞死亡風險；肺段開通術（tractotomy）為保留肺組織的首選，應避免全肺切除。",
    "explanation": "【題幹解析】\n評估嚴重肺臟外傷之外科處置原則，包含氣體栓塞防範、肺組織保留策略（Tractotomy）與全肺切除術（Pneumonectomy）的預後與定位。\n\n【選項詳解】\n- A. 正確。在縫合深部肺部穿刺傷或裂傷時，若肺泡/細支氣管與受損的肺靜脈分支交通未被妥善阻斷，正壓通氣會將氣體強行壓入肺靜脈，氣體隨後回流至左心房與左心室，造成「全身性空氣栓塞（systemic air embolism）」，引發腦栓塞、冠狀動脈栓塞而導致術中或術後猝死。\n- B. 錯誤。肺臟創傷病人若接受全肺切除術（Pneumonectomy），由於急性肺血管阻力驟增、右心衰竭及嚴重低氧，死亡率極高（通常高達 50%~80%），因此全肺切除「會顯著降低存活率」，在創傷外科中被視為逼不得已的最後手段，而非用來增加存活率。\n- C. 錯誤。肺段開通術（Pulmonary tractotomy）是利用線性切割縫合器將貫穿傷通道直接切開，使隱蔽的出血血管與漏氣氣管完全暴露並予以精確結紮。這是一種非常有效且能最大程度保留肺組織的術式，可有效避免全肺切除術。\n- D. 錯誤。如前所述，全肺切除術死亡率極高，在肺外傷手術中是「最不常用、最應盡量避免」的術式。最常用的術式是局部縫合、部分肺切除（wedge resection）或肺段開通術（tractotomy）。\n\n【核心考點】\n肺創傷手術的致命併發症（空氣栓塞）；肺臟保留手術觀念（肺段開通術 tractotomy 的應用）；全肺切除術（pneumonectomy）在高死亡率創傷中的最後防線定位。",
    "flashcard_front": "肺外傷手術 / 空氣栓塞風險 / 肺段開通術 (Tractotomy) / 全肺切除預後",
    "flashcard_back": "縫合深部肺裂傷時，正壓呼吸易引發致命的「系統性空氣栓塞」；「肺段開通術」能有效止血並保留肺功能；應極力避免「全肺切除」（死亡率極高）。",
    "flashcard_summary": "肺外傷手術處置 -> 深部縫合防空氣栓塞；首選肺段開通術保留組織，避開全肺切除。"
  },
  {
    "id": "112-1_medicine-5_030",
    "category": "胸腔外科",
    "key_point": "縱隔腔惡性生殖細胞瘤（如精原細胞瘤與非精原細胞瘤）具有極強的男性好發傾向（佔9成以上）。",
    "explanation": "【題幹解析】\n成人縱隔腔腫瘤（Mediastinal tumors）的解剖定位、病理分類、性別差異與治療敏感性。\n\n【選項詳解】\n- A. 正確。良性畸胎瘤（Benign teratoma，多位於前縱隔）若因緊鄰大血管或心包膜而無法做到顯微鏡下完全切除，僅行肉眼下的部分切除（subtotal resection）以解除壓迫症狀，術後也「鮮少復發」，預後良好。\n- B. 正確。後縱隔（Posterior mediastinum）最常見的腫瘤為神經源性腫瘤（Neurogenic tumors，如 Schwannoma, Neurofibroma, Ganglioneuroma）。\n- C. 正確。精原細胞瘤（Seminoma，前縱隔常見惡性生殖細胞瘤）對放射治療（Radiotherapy）與化學治療（Chemotherapy，以順鉑為基礎的療程）高度敏感，預後在惡性生殖細胞瘤中相對較好。\n- D. 錯誤。原發性縱隔腔惡性生殖細胞瘤（Primary mediastinal malignant GCTs）表現出極為顯著的性別差異，「幾乎完全發生於男性」（男女比例約為 9:1 甚至更高），女性極為罕見。因此「沒有性別差異」的敘述錯誤。\n\n【核心考點】\n縱隔腔腫瘤的臨床特點：後縱隔以神經源性為主；良性畸胎瘤部分切除亦不易復發；精原細胞瘤放化療敏感；惡性生殖細胞瘤極度好發於男性。",
    "flashcard_front": "縱隔腔腫瘤 / 後縱隔常見 / 精原細胞瘤治療 / 惡性生殖細胞瘤性別",
    "flashcard_back": "後縱隔最常見為「神經源性腫瘤」；精原細胞瘤對「放化療極敏感」；原發縱隔惡性生殖細胞瘤「極度好發於男性」（無性別差異為錯）。",
    "flashcard_summary": "縱隔腔腫瘤 -> 後縱隔最常見神經源性腫瘤；惡性生殖細胞瘤好發於男性。"
  }
]

# Write to temp updates file
scratch_dir = Path(r"C:\Users\User\.gemini\antigravity\brain\285f77f1-a3ad-46dc-8c67-e0efdabe0a2f\scratch")
scratch_dir.mkdir(parents=True, exist_ok=True)
updates_file = scratch_dir / "updates_3.json"
updates_file.write_text(json.dumps(updates, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Written updates to {updates_file}")
