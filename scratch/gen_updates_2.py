import json
from pathlib import Path

updates = [
  {
    "id": "112-1_medicine-5_011",
    "category": "骨科",
    "key_point": "腰椎管狹窄與滑脫首選保守治療；若出現進行性神經損傷或馬尾症候群（如小便困難）則需緊急手術。",
    "explanation": "【題幹解析】\n評估腰椎退化性病變（如腰椎管狹窄、椎體滑脫）的臨床症狀特徵、機械性緩解因應，以及手術治療的絕對適應症。\n\n【選項詳解】\n- A. 錯誤。腰椎管狹窄症（Lumbar Spinal Stenosis, LSS）的典型症狀為「神經性跛行」（neurogenic claudication），即站立或行走一段距離後出現下肢酸麻痛，但「騎腳踏車」或「坐姿」（腰椎處於屈曲 flexion 狀態，使椎管容積增大）通常可以明顯緩解症狀。因此「無法騎腳踏車和久坐」與典型症狀不符。\n- B. 錯誤。當病患站立或腰椎挺起（extension）時，黃韌帶會皺褶且椎管容積進一步變小，進而加劇壓迫，症狀會「惡化」而非緩解。反之，向前彎腰（flexion）才會使症狀緩解。\n- C. 錯誤。若第五腰椎的 pars interarticularis（椎弓峽部）發生退化性斷裂（峽部裂 spondylolysis），最常造成的是「第五腰椎對第一薦椎（L5-S1）」的滑脫，而非第4~5節（L4-5）。\n- D. 正確。腰椎狹窄與滑脫應首選保守治療（復健、藥物、姿勢調整）。但若保守治療無效，神經症狀持續加劇，或出現馬尾症候群（Cauda equina syndrome，如小便困難、鞍區感覺喪失），則為緊急手術的絕對指徵。\n\n【核心考點】\n腰椎管狹窄症的症狀特徵（前彎/坐姿緩解，後仰/行走惡化）；椎弓峽部裂滑脫好發部位；手術適應症（馬尾症候群為急症）。",
    "flashcard_front": "腰椎狹窄與滑脫 / 症狀誘發與緩解 / 峽部裂滑脫部位 / 手術指徵",
    "flashcard_back": "症狀隨前彎/騎車/坐姿「緩解」，後仰/站立「惡化」；L5峽部裂引起L5-S1滑脫；出現馬尾症候群（排尿障礙）需「緊急手術」。",
    "flashcard_summary": "腰椎管狹窄症 -> 前彎緩解、後伸惡化，出現排尿困難（馬尾症候群）需立即手術。"
  },
  {
    "id": "112-1_medicine-5_012",
    "category": "骨科",
    "key_point": "Jefferson fracture 是第一頸椎（C1）爆裂性骨折，由軸向重壓引起，若橫韌帶斷裂會造成C1-C2不穩定性脫位。",
    "explanation": "【題幹解析】\n傑佛遜氏骨折（Jefferson fracture）是指第一頸椎（C1，寰椎寰椎環）的爆裂性骨折，常涉及前弓和後弓的雙側骨折。\n\n【選項詳解】\n- A. 錯誤。Jefferson fracture 主要是由於第一頸椎受到「軸向垂直壓縮外力」（axial loading / compression），如跳水頭部頂地或車禍撞擊頭頂所致，而非前屈外力（flexion）。\n- B. 錯誤。由於 C1 環狀結構在骨折時向外爆裂、椎管容積反而相對擴大，且此處椎管空間較大，因此大部分 Jefferson fracture 患者「較少」伴隨嚴重的脊髓或神經功能損傷，除非合併嚴重的C1-C2位移或橫韌帶斷裂。\n- C. 錯誤。診斷 Jefferson fracture 首選且最具診斷價值的影像檢查是「電腦斷層掃描（CT scan）」（尤其是冠狀位與軸向重建），能清晰呈現骨折線。核磁共振（MRI）主要用於評估橫韌帶（transverse ligament）等軟組織受損情況。\n- D. 正確。寰椎橫韌帶（transverse ligament of atlas）是穩定 C1-C2（寰樞關節）的最重要結構。如果 Jefferson 骨折合併橫韌帶斷裂，會失去對齒狀突的約束，進而引發嚴重的第一、二頸椎不穩定性脫位，有壓迫高位脊髓的致命風險。\n\n【核心考點】\nJefferson fracture 的受力機制（軸向壓縮）、解剖特徵（爆裂往外，神經損傷少）、首選診斷（CT）以及橫韌帶斷裂對穩定性的影響。",
    "flashcard_front": "Jefferson fracture / C1 爆裂骨折 / 機轉與診斷 / 橫韌帶斷裂後果",
    "flashcard_back": "為 C1 爆裂骨折，由「垂直軸向重壓」引起，神經受損罕見；CT為首選診斷；橫韌帶斷裂會導致「C1-C2 不穩定脫位」。",
    "flashcard_summary": "Jefferson骨折 -> C1垂直壓縮爆裂骨折，神經受損少，橫韌帶斷裂致C1-C2不穩定。"
  },
  {
    "id": "112-1_medicine-5_013",
    "category": "神經外科",
    "key_point": "顱骨骨折合併嚴重腦出血（體積大、中線偏移顯著及神智改變）需立即開顱手術，而單純腦脊髓液鼻漏或面神經麻痺首選保守治療。",
    "explanation": "【題幹解析】\n評估頭部外傷、顱骨骨折之合併症（如面神經受損、CSF鼻漏、腦內出血與質塊效應）的緊急手術手術指徵。\n\n【選項詳解】\n- A. 錯誤。顳骨骨折引起的顏面神經麻痺，若非剛受傷時立即發生且證實神經完全斷裂，通常首選藥物保守治療（如類固醇），不需「馬上」進行手術治療。\n- B. 錯誤。前顱窩骨折引發的腦脊髓液鼻漏（CSF rhinorrhea），絕大多數（約85%以上）在保守治療（床頭抬高、避免擤鼻涕與用力、密切觀察）下，會在1~2週內自行癒合，不需立即手術，除非持續漏水超過2週或合併反覆腦膜炎。\n- C. 錯誤。顳骨骨折導致的腦脊髓液鼻漏同樣首選保守治療，且顳骨骨折更常引發耳漏（CSF otorrhea）或經耳咽管流至鼻腔的鼻漏，初期處置相同。\n- D. 正確。腦實質出血量達 35 mL，且影像上中線偏移（midline shift）已大於 1 cm，並伴隨神智改變，代表大腦已經受到嚴重壓迫、有腦疝脫（brain herniation）之危險，屬於危及生命的急症，必須立即進行手術清除血塊與去骨瓣減壓術。\n\n【核心考點】\n顱內出血手術指徵（體積 >30 mL，中線偏移 >5 mm，神智變差）；腦脊髓液漏與外傷性面神經麻痺的初期保守治療原則。",
    "flashcard_front": "頭部外傷 / 腦脊髓液鼻漏 / 面神經麻痺處置 / 開顱手術指征",
    "flashcard_back": "CSF 鼻漏與外傷性面神經麻痺首選「保守治療」；腦實質出血 >30 mL 且中線偏移 >1 cm 併神智改變需「緊急手術」。",
    "flashcard_summary": "開顱手術指針 -> 腦出血>30ml且中線偏移顯著需立即手術；CSF漏與面神經麻痺先保守治療。"
  },
  {
    "id": "112-1_medicine-5_014",
    "category": "整形外科",
    "key_point": "先天性黑色素細胞痣（CMN）的尺寸分類與惡性黑色素瘤及軟腦膜黑色素細胞增生症的臨床關聯。",
    "explanation": "【題幹解析】\n先天性黑色素細胞痣（Congenital melanocytic nevus, CMN）是出生時即存在的色素痣。其臨床重要性在於病灶大小與惡性黑色素瘤（Melanoma）及神經皮膚黑色素細胞增生症（Neurocutaneous melanocytosis）的發生風險正相關。\n\n【選項詳解】\n- 敘述1. 正確。CMN的尺寸以預估至成人時的最大直徑來分類：小型（<1.5 cm）、中型（1.5-19.9 cm）、大型（20-49.9 cm）及巨大（giant，>= 50 cm）。\n- 敘述2. 正確。大型和巨大CMN發展成惡性黑色素細胞瘤（Melanoma）的機率顯著高於小型CMN，巨大CMN的惡變風險可達2%至5%。\n- 敘述3. 正確。大型或巨大CMN（特別是位於中軸如頭頸部、脊椎者）患者，發生軟腦膜黑色素細胞異常增生（Leptomeningeal involvement/melanocytosis）的風險較高，需藉由腦部/脊髓 MRI（T1高訊號）來診斷。\n- 敘述4. 正確。小型CMN若不幸惡變為黑色素瘤，大多發生在青春期（puberty）之後，因此在孩童期通常可密切追蹤觀察，不需常規緊急切除。\n因此，所有敘述（1234）皆正確。\n\n【核心考點】\n先天性黑色素細胞痣（CMN）的尺寸界定、大型/巨大CMN與黑色素瘤及中樞神經黑色素細胞增生症（MRI診斷）的關聯，以及小型CMN的惡變時機。",
    "flashcard_front": "先天性黑色素細胞痣 (CMN) / 巨大痣定義 / 軟腦膜受累 / 惡變年齡",
    "flashcard_back": "大型為 20-49.9cm，巨大為 >=50cm；大/巨大者易合併「軟腦膜黑色素增生」（MRI診斷）及高惡變率；小痣惡變多在「青春期後」。",
    "flashcard_summary": "CMN臨床特徵 -> 巨大痣(>=50cm)易惡變且可伴軟腦膜黑色素增生，小痣惡變在青春期後。"
  },
  {
    "id": "112-1_medicine-5_015",
    "category": "整形外科",
    "key_point": "顯微自由皮瓣移植中，骨骼肌對熱缺血最為敏感，耐受極限僅為2-3小時，超過可導致不可逆壞死與再灌流損傷。",
    "explanation": "【題幹解析】\n顯微血管自由皮瓣移植（Free Flap）中，不同組織對於熱缺血時間（warm ischemia time，指無血流且在常溫下的時間）的耐受度不同。本題考查各組織耐受力、血管接合方式及預防血管痙攣的處置。\n\n【選項詳解】\n- A. 錯誤。骨骼肌（Muscle）對缺氧極其敏感。肌肉組織可以忍受的熱缺血極限時間僅為「2~3小時」（超過此時間會發生嚴重的不可逆壞死、橫紋肌溶解與再灌流損傷）。4~6小時是皮膚（Skin）或脂肪組織的耐受極限。\n- B. 正確。臨床文獻與實務證實，不論是端對端（end-to-end）或端對側（end-to-side）的動脈吻合，只要技術正確，其血管通暢率（patency rate）和皮瓣存活率在統計學上並沒有顯著差異。\n- C. 正確。當受體血管（recipient vessel）與皮瓣供體血管（donor vessel）粗細相差較大時，採用端對側吻合（end-to-side anastomoses）可以有效解決口徑不匹配的問題，且能保留受體主幹血管的遠端血流。\n- D. 正確。血管外膜（Tunica adventitia）富含交感神經纖維。在吻合前將血管末端的外膜剝除（adventitial stripping），可以切斷交感神經傳導，從而有效預防和降低顯微手術中血管痙攣（vasospasm）的發生率。\n\n【核心考點】\n顯微皮瓣不同組織的熱缺血耐受力（肌肉最差，僅2-3小時）；端對端與端對側吻合的適用情境；剝除外膜防血管痙攣的原理。",
    "flashcard_front": "顯微自由皮瓣 / 肌肉熱缺血時間 / 血管吻合方式 / 剝除外膜防血管痙攣",
    "flashcard_back": "「骨骼肌」熱缺血耐受極限僅為「2~3小時」（非4~6小時）；血管粗細不一時首選端對側吻合；剝除外膜可減交感神經刺激防痙攣。",
    "flashcard_summary": "顯微皮瓣缺血耐受 -> 肌肉熱缺血耐受僅2-3小時，剝除血管外膜可預防血管痙攣。"
  },
  {
    "id": "112-1_medicine-5_016",
    "category": "整形外科",
    "key_point": "手部魚際肌群中，拇指內收肌（adductor pollicis）是由尺神經深支支配，而非正中神經支配。",
    "explanation": " = \"【題幹解析】\n手部內在肌群（intrinsic muscles）的運動神經支配分布規律：正中神經（Median nerve）在手部支配五條肌肉（簡稱 LOAF：L 代表第 1, 2 蚓狀肌 lumbricals；O 代表拇指對掌肌 opponens pollicis；A 代表拇指外展短肌 abductor pollicis brevis；F 代表拇指屈短肌 flexor pollicis brevis 的淺頭）。其餘手部內在肌均由尺神經（Ulnar nerve）支配。\n\n【選項詳解】\n- A. 錯誤（由正中神經支配）。拇指外展短肌（Abductor pollicis brevis）是魚際肌（thenar muscles）最表淺的肌肉，由正中神經返支支配。\n- B. 正確（非正中神經支配）。拇指內收肌（Adductor pollicis）雖然位於大魚際區，但在解剖與神經支配上，它是由「尺神經深支（deep branch of ulnar nerve）」所支配。若正中神經受損，此肌功能仍可保留。\n- C. 錯誤（由正中神經支配）。拇指屈短肌（Flexor pollicis brevis）的淺頭（superficial head）由正中神經支配（深頭由尺神經支配，但大考通常將此肌整體視為正中神經支配）。\n- D. 錯誤（由正中神經支配）。拇指對掌肌（Opponens pollicis）是魚際肌群的深層肌肉，由正中神經返支支配，負責拇指對掌動作。\n\n【核心考點】\n手部肌肉的神經支配：正中神經支配 LOAF（拇指外展短、對掌、屈短淺頭、第1-2蚓狀肌）；拇指內收肌（adductor pollicis）與所有骨間肌皆由「尺神經」支配。",
    "flashcard_front": "手部內在肌 / 正中神經支配 (LOAF) / 拇指內收肌 / 尺神經支配",
    "flashcard_back": "正中神經支配「LOAF」肌肉（含外展短、對掌、屈短淺頭）；「拇指內收肌（Adductor pollicis）」由「尺神經」支配。",
    "flashcard_summary": "手部神經支配 -> 拇指內收肌由尺神經支配；正中神經支配LOAF肌群。"
  },
  {
    "id": "112-1_medicine-5_017",
    "category": "一般外科",
    "key_point": "腺樣囊狀癌（adenoid cystic carcinoma）中以管狀（tubular）預後最佳，實質性（solid）預後最差。",
    "explanation": "【題幹解析】\n評估唾液腺腫瘤（Salivary gland tumors）的發病率、好發部位、常見病理分型與其預後因應。\n\n【選項詳解】\n- A. 正確。唾液腺腫瘤較為罕見，僅佔所有頭頸部腫瘤的不到 2%。\n- B. 正確。約 80% 的唾液腺腫瘤發生在腮腺（parotid gland），其中以多形性腺瘤（Pleomorphic adenoma，又稱良性混合瘤）為最常見的良性腫瘤。\n- C. 錯誤。腺樣囊狀癌（Adenoid cystic carcinoma, ACC）在病理切片下有三種主要生長模式：篩狀（cribriform）、管狀（tubular）和實質性（solid）。其中以「管狀（tubular pattern）」的細胞分化較好，預後「最佳」（5年及10年存活率最高）；而「實質性（solid pattern）」則預後「最差」，易早期轉移。\n- D. 正確。黏液表皮樣癌（Mucoepidermoid carcinoma）是兒童與成人最常見的唾液腺惡性腫瘤。其病理組成中，High grade 惡性度高，常以表皮樣細胞（epidermoid cells）為主；Low grade 惡性度低，常以黏液分泌細胞（mucinous cells）為主。\n\n【核心考點】\n唾液腺腫瘤流行病學；腮腺多形性腺瘤特點；腺樣囊狀癌病理分型與預後（管狀最佳，實質最差）；黏液表皮樣癌分級特徵。",
    "flashcard_front": "唾液腺腫瘤 / 腮腺良性首選 / 腺樣囊狀癌預後分型 / 黏液表皮樣癌特徵",
    "flashcard_back": "最常見良性為腮腺「多形性腺瘤」；腺樣囊狀癌中「管狀（tubular）」預後最佳，「實質性（solid）」最差；最常見惡性為黏液表皮樣癌。",
    "flashcard_summary": "唾液腺腫瘤 -> 最常見良性為多形性腺瘤，最常見惡性為黏液表皮樣癌；腺樣囊狀癌管狀預後最好。"
  },
  {
    "id": "112-1_medicine-5_018",
    "category": "一般外科",
    "key_point": "乳房 Paget's disease 表現為乳頭乳暈處的濕疹樣病變，常合併潛在的乳腺導管原位癌或侵襲癌。",
    "explanation": "【題幹解析】\n乳房表面出現慢性濕疹樣、紅斑脫屑、糜爛或帶滲出物的病灶，且局限於乳頭及乳暈區域，為典型乳房柏哲德氏病（Paget's disease of the breast）的臨床表現，此病實為惡性腫瘤細胞（Paget cells）浸潤乳頭表皮。\n\n【選項詳解】\n- A. 錯誤。Mondor's disease 是指乳房或前胸壁的「表淺血栓性靜脈炎」（superficial thrombophlebitis），臨床表現為胸壁拉扯感、皮下可觸及條索狀（cord-like）壓痛硬塊，表面皮膚完好，無濕疹糜爛。\n- B. 正確。Paget's disease 典型表現為乳頭和乳暈皮膚的「慢性濕疹樣改變」（紅斑、脫屑、搔癢、糜爛或潰瘍），常被誤診為一般皮膚炎。其背後幾乎 95% 以上合併有潛在的乳腺導管原位癌（DCIS）或浸潤性導管癌（IDC）。\n- C. 錯誤。乳管擴張症（Duct ectasia）為良性乳腺疾病，好發於經期後或中年女性，主訴為乳頭黏稠、乾酪樣或血性分泌物，常伴隨乳暈旁腫塊或乳頭凹陷，但乳頭表皮不會出現廣泛的濕疹性剝落糜爛。\n- D. 錯誤。急性乳腺炎（Acute mastitis）多見於哺乳期婦女，表現為乳房紅、腫、熱、痛，常伴有發燒及白血球升高，病灶範圍較廣，非局限於乳頭表皮的慢性濕疹樣病變。\n\n【核心考點】\nPaget's disease of the breast 的臨床特徵（乳頭乳暈濕疹樣變、脫屑糜爛）及其與潛在乳腺癌的關聯；與乳壁靜脈炎（Mondor's）及乳管擴張的鑑別診斷。",
    "flashcard_front": "乳頭乳暈濕疹樣變 / Mondor's 條索硬塊 / 乳管擴張分泌物 / Paget's disease",
    "flashcard_back": "乳頭乳暈出現紅斑、脫屑、糜爛如濕疹時，診斷首選「Paget's disease」，高度合併潛在乳腺癌；Mondor's 為表淺血栓性靜脈炎。",
    "flashcard_summary": "乳房Paget氏病 -> 乳頭乳暈慢性濕疹樣變，為惡性腫瘤表現，需切片檢查。"
  },
  {
    "id": "112-1_medicine-5_019",
    "category": "心臟外科",
    "key_point": "體外循環（CPB）在深低溫（20°C）時，代謝率極低，所需灌流流量應降至 1.2-1.6 L/min/m²，而非維持常溫流量。",
    "explanation": "【題幹解析】\n體外循環（Cardiopulmonary bypass, CPB）的運作生理、置管位置、併發症，以及體溫與灌流流量的調控規律。\n\n【選項詳解】\n- A. 正確。體外循環的動脈導管（Arterial cannula，回輸血液至全身）常用位置包括升主動脈（ascending aorta，最常用）、無名動脈、腋動脈（axillary artery）或股動脈（femoral artery）。\n- B. 錯誤。在正常體溫（37°C）下，體外循環的標準灌流流量（flow rate）約為 2.4 L/min/m²。但當使用低溫（Hypothermia）保護時，組織代謝率與氧耗量會大幅下降（溫度每下降1°C，代謝率下降約7%）。當體溫降至中度至深度低溫（如 20°C）時，流量應相應調低至 「1.2 ~ 1.6 L/min/m²」（甚至更低），以減少對血液成分的破壞並降低手術野的出血。\n- C. 正確。血液接觸人工管道會激活補體與白血球，造成全身性發炎反應症候群（SIRS）、凝血因子消耗與血小板破壞（出血傾向）、微氣泡或微血栓栓塞，以及因灌流壓不足造成的灌流器官功能障礙。\n- D. 正確。當體外循環完全接管心肺功能，心臟停跳且人工肺（Oxygenator）完全負責氣體交換時，患者的肺部不需通氣，呼吸器可以完全暫停以穩定手術視野。\n\n【核心考點】\n體外循環（CPB）的病理生理學：低溫能降低組織氧耗，因此灌流流量需調低；CPB 常見血管通路與併發症（發炎反應、凝血異常）。",
    "flashcard_front": "體外循環 (CPB) / 20°C 流量調控 / 動脈管路位置 / 呼吸器暫停條件",
    "flashcard_back": "常溫 CPB 流量為 2.4 L/min/m²；深低溫（20°C）因代謝降低，流量應降至「1.2-1.6 L/min/m²」；CPB運作時呼吸器可暫停。",
    "flashcard_summary": "體外循環流量 -> 低溫時組織代謝下降，灌流流量應相應降低，非維持常溫流量。"
  },
  {
    "id": "112-1_medicine-5_020",
    "category": "心臟外科",
    "key_point": "慢性下腔靜脈完全阻塞已無栓子脫落至肺部的通路，不需且無法放置下腔靜脈過濾器（IVC filter）。",
    "explanation": " = \"【題幹解析】\n下腔靜脈過濾器（IVC filter）放置的主要目的在於攔截來自下肢深層靜脈（DVT）脫落的血栓，防止其流回右心並引發致命的急性肺栓塞（PE）。其主要適應症包括：抗凝血劑禁忌、抗凝血劑療效不佳（用藥仍復發）、或面臨極高危肺栓塞且心肺代償極差的患者。\n\n【選項詳解】\n- A. 正確（不需要放置）。若患者下腔靜脈已發生「慢性完全阻塞」（Chronic complete occlusion），血流已改走側支循環，且主幹已被完全堵死，下肢的血栓「不可能」再經由下腔靜脈主幹向上游移至肺動脈，此時放置過濾器既無必要，在技術上也無法穿過阻塞處進行置放。\n- B. 錯誤（需要放置）。有絕對禁忌症（如近期活動性大出血、剛接受重大手術）而無法使用抗凝血劑的 DVT 患者，是置放 IVC filter 的首要絕對指徵，以預防急性 PE。\n- C. 錯誤（需要放置）。若患者在接受足夠劑量且達標的抗凝血治療下，仍反覆發作 DVT 或新發肺栓塞，說明藥物控制失敗，需置放過濾器進行物理性攔截。\n- D. 錯誤（需要放置）。慢性肺栓塞合併重度肺高壓患者，其心肺儲備功能極差，此時若再發生一次微小的肺栓塞都可能是致命的，因此需要放置 IVC filter 進行保護。\n\n【核心考點】\n下腔靜脈過濾器（IVC filter）的臨床指徵：抗凝血劑禁忌、抗凝血失敗、極差心肺代償；下腔靜脈已完全閉塞者為置放禁忌/無必要性。",
    "flashcard_front": "IVC 過濾器指徵 / 抗凝血劑禁忌 / 慢性IVC完全阻塞 / 肺高壓保護",
    "flashcard_back": "「下腔靜脈已慢性完全阻塞」者不需要且無法放置過濾器；抗凝血禁忌、藥物治療失敗、重度肺高壓患者為置放指徵。",
    "flashcard_summary": "IVC過濾器適應症 -> 慢性下腔靜脈完全阻塞不需置放；抗凝血禁忌或失敗者為主要指徵。"
  }
]

# Write to temp updates file
scratch_dir = Path(r"C:\Users\User\.gemini\antigravity\brain\285f77f1-a3ad-46dc-8c67-e0efdabe0a2f\scratch")
scratch_dir.mkdir(parents=True, exist_ok=True)
updates_file = scratch_dir / "updates_2.json"
updates_file.write_text(json.dumps(updates, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Written updates to {updates_file}")
