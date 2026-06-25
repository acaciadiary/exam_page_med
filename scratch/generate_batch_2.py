import json
from pathlib import Path

updates = [
  {
    "question_id": "114-1_medicine-4_011",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "幼兒急性高燒與黏液血便（痢疾樣腹瀉）的致病菌鑑別診斷。",
    "explanation": "【題幹解析】\n3歲男童表現為高燒（40.2°C）、陣發性腹痛、頻繁水瀉，並排出「含有血絲黏糊便」（黏液血便/膿血便，痢疾樣表現），且無嘔吐、無服用抗生素史。此為侵襲性細菌性腸炎的典型臨床特徵。\n\n【選項詳解】\n- A. 不可能。輪狀病毒主要引起嬰幼兒嚴重的「水瀉」與嘔吐，通常不出現大量血絲黏糊便，且多見於秋冬季。\n- B. 不可能。諾羅病毒主要引起以「嘔吐」為主的急性腸胃炎，伴隨水瀉，極少造成黏液血便。\n- C. 最有可能。志賀氏桿菌（Shigella）是引起細菌性痢疾（bacillary dysentery）的經典病原，典型表現為高燒、劇烈絞痛、裏急後重及含有血絲與黏液的糞便（mucosanguineous stool）。\n- D. 不可能。困難梭狀桿菌（C. difficile）感染多與「使用抗生素」後造成腸道菌相失衡有關，題幹已明確說明「無服用抗生素」。\n\n【核心考點】\n志賀氏桿菌（Shigella）感染引發典型細菌性痢疾，特徵為高燒、絞痛與黏液血絲便。輪狀與諾羅病毒以水瀉為主；困難梭狀桿菌通常與抗生素使用史相關。",
    "flashcard_front": "幼兒高燒 / 陣發性腹痛 / 黏液血絲便(無抗生素史) / 最可能致病菌",
    "flashcard_back": "最可能為志賀氏桿菌(Shigella)感染，其引發細菌性痢疾，以高燒、劇烈腹痛及黏液血便為特徵。",
    "flashcard_summary": "幼兒黏液血便致病菌 -> 最可能為志賀氏桿菌(Shigella)感染。"
  },
  {
    "question_id": "114-1_medicine-4_012",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "自體顯性多囊腎(ADPKD)與自體隱性多囊腎(ARPKD)的致病基因與臨床特徵區分。",
    "explanation": "【題幹解析】\n本題考查 ADPKD 與 ARPKD 的遺傳基因缺陷及臨床併發症。\n\n【選項詳解】\n- A. 正確。ADPKD 是一種系統性疾病，除了腎臟囊腫外，囊泡亦常見於肝臟（最常見，約70%）、脾臟、胰臟與卵巢等器官。\n- B. 正確。ARPKD 典型於新生兒期發病。巨大腎臟壓迫常伴有羊水過少（因胎兒尿量減少），進而引起肺部發育不全（Potter sequence）。\n- C. 正確。兩者因腎實質受損與 RAA 系統活化，皆會出現血尿、高血壓及進行性腎衰竭等併發症。\n- D. 錯誤。大部分的 ADPKD 是因位於第 16 對染色體上的 PKD1 基因（約 85%）或第 4 對染色體上的 PKD2 基因（約 15%）突變所致。而 ARPKD 的致病基因 PKHD1 才是位於第 6 對染色體上。\n\n【核心考點】\nADPKD 致病基因在第 16 對(PKD1)或第 4 對(PKD2)染色體上；ARPKD 的 PKHD1 基因位於第 6 對染色體上。ARPKD 易合併羊水過少與肺發育不全。",
    "flashcard_front": "多囊腎 / ADPKD vs ARPKD / 基因缺陷染色體定位",
    "flashcard_back": "ADPKD基因突變主要在第16對(PKD1)或第4對(PKD2)染色體；ARPKD(PKHD1)則在第6對染色體。",
    "flashcard_summary": "ADPKD與ARPKD染色體定位 -> ADPKD在第16或4對，ARPKD在第6對。"
  },
  {
    "question_id": "114-1_medicine-4_013",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "急性鏈球菌感染後腎炎（APSGN）的好發年齡、潛伏期、補體變化及抗生素預防效果。",
    "explanation": "【題幹解析】\n本題考查急性鏈球菌感染後腎炎（APSGN）的流行病學、臨床特徵、免疫學變化與治療原則。\n\n【選項詳解】\n- A. 錯誤。APSGN 最常發生於 5 至 12 歲的學齡兒童，3 歲以下或 2 歲以下的幼兒極為罕見。\n- B. 錯誤。咽喉炎感染後的潛伏期通常為 1 到 2 週（7-14天），皮膚感染後則為 3 到 6 週。若在咽喉炎後 1-3 天內即出現血尿（synpharyngitic hematuria），應高度懷疑 IgA 腎病變（IgA nephropathy），而非 APSGN。\n- C. 錯誤。APSGN 主要經由替代途徑（alternative pathway）活化補體，因此 90% 病童會表現為血清補體 C3 與 CH50 明顯下降，但 C4 數值通常維持正常或僅輕微下降。\n- D. 正確。在鏈球菌感染早期使用抗生素治療，雖然能有效預防急性風濕熱（rheumatic fever）的發生，但並不能減少急性鏈球菌感染後腎炎（APSGN）的發生率。\n\n【核心考點】\n早期抗生素治療無法預防 APSGN。APSGN 潛伏期通常大於 1 週（咽喉炎）或 3 週（皮膚炎）；補體變化主要為 C3 下降而 C4 正常；好發於學齡兒童。",
    "flashcard_front": "急性鏈球菌感染後腎炎(APSGN) / 早期抗生素預防效果 / 補體與潛伏期特徵",
    "flashcard_back": "早期使用抗生素無法預防APSGN。APSGN潛伏期通常>7天，補體表現為C3下降但C4通常正常。",
    "flashcard_summary": "APSGN特徵 -> 早期抗生素無法預防；潛伏期>7天；C3下降且C4正常。"
  },
  {
    "question_id": "114-1_medicine-4_014",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "急性大葉性腎盂腎炎（acute lobar nephronia）的臨床表現與CT影像診斷特徵。",
    "explanation": "【題幹解析】\n5歲女童高燒、膿尿，使用經驗性抗生素3天後高燒仍未改善。電腦斷層（CT）顯示腎臟有局灶性、楔形（wedge-shaped）的顯影不良區，但無明顯帶有厚壁增強的液化空腔。此為急性大葉性腎盂腎炎的典型表現。\n\n【選項詳解】\n- A. 錯誤。急性腎絲球腎炎主要表現為血尿、蛋白尿、水腫及高血壓，CT 不會出現侷限性的楔形顯影不良病灶。\n- B. 正確。急性大葉性腎盂腎炎（acute lobar nephronia，又稱急性局灶性細菌性腎炎）是介於急性腎盂腎炎與腎膿瘍之間的間質性腎臟感染。CT 特徵為腎實質內局部楔形或圓形顯影不良區，且無液化（liquefaction），常需要較長期的抗生素治療且退燒較慢。\n- C. 錯誤。急性腎膿瘍（renal abscess）在 CT 上會表現為邊緣環狀顯影增強，內部呈現低密度的液化空腔（fluid collection with rim enhancement），本題影像尚無液化病灶。\n- D. 錯誤。急性腎梗塞（renal infarction）在 CT 亦呈楔形無顯影區，但多有栓塞來源且常無膿尿，亦不會以發燒膿尿、抗生素治療無效的感染病程為主訴。\n\n【核心考點】\n急性大葉性腎盂腎炎（Acute lobar nephronia）在 CT 表現為局灶楔形顯影不良且無液化壞死。其病程介於急性腎盂腎炎與腎膿瘍之間，對抗生素退燒反應較慢。",
    "flashcard_front": "兒童發燒膿尿 / CT示局灶楔形顯影不良(無液化) / 最可能診斷",
    "flashcard_back": "最可能為急性大葉性腎盂腎炎(acute lobar nephronia)，影像特徵為局部楔形低密度區且無液化，對抗生素退燒較慢。",
    "flashcard_summary": "急性大葉性腎盂腎炎影像 -> CT表現為局灶楔形低密度區且無液化。"
  },
  {
    "question_id": "114-1_medicine-4_015",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "過敏性紫斑症（HSP）的病理生理特徵、臨床紫斑特徵與血小板變化。",
    "explanation": "【題幹解析】\n本題考查過敏性紫斑症（Henoch-Schönlein purpura, HSP，現稱 IgA 血管炎）的臨床症狀、實驗室檢查與病理診斷。\n\n【選項詳解】\n- A. 錯誤。HSP 的紫斑為可觸摸的出血性紫斑（palpable purpura），主要對稱性分布於雙下肢（小腿、足踝）及臀部等重力承受處，較少主要出現在上肢或軀幹。\n- B. 錯誤。HSP 屬於「非血小板低下性紫斑」（non-thrombocytopenic purpura），抽血檢查其血小板計數通常正常，甚至可能因發炎反應呈反應性上升。\n- C. 正確。HSP 的病理特徵是小血管白血球碎裂性血管炎（leukocytoclastic vasculitis），切片可見小血管壁有免疫球蛋白 IgA 及補體沉積。\n- D. 錯誤。約有 30-50% 的患者會合併腎臟受累（HSP 腎炎），並非大部分；且類固醇主要用於緩解嚴重關節痛與腸胃道症狀，並無法預防腎炎的發生，輕度腎炎不需急於給予類固醇。\n\n【核心考點】\nHSP 病理為 IgA 沉積的小血管炎；血小板數量正常（非血小板低下性）；紫斑分布於雙下肢與臀部。",
    "flashcard_front": "過敏性紫斑症(HSP) / 紫斑分布與血小板計數 / 病理沉積物",
    "flashcard_back": "HSP為非血小板低下性紫斑，紫斑分布於雙下肢與臀部；病理特徵為小血管炎伴隨IgA沉積。",
    "flashcard_summary": "HSP特徵 -> 非血小板低下性；紫斑好發下肢與臀部；病理見IgA沉積。"
  },
  {
    "question_id": "114-1_medicine-4_016",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "兒童特發性關節炎（JIA）的定義、併發症及生物製劑治療藥物。",
    "explanation": "【題幹解析】\n本題考查兒童特發性關節炎（Juvenile Idiopathic Arthritis, JIA）的診斷準則、最常見慢性風濕病地位、眼部併發症及藥物治療。\n\n【選項詳解】\n- A. 正確。JIA 的定義為：發病年齡在 16 歲以下，出現一個或多個關節發炎（腫、痛、活動受限）且持續至少 6 週以上，並排除其他已知關節疾病。\n- B. 正確。JIA 確實是兒童期最常見的慢性結締組織/風濕性關節疾病。\n- C. 正確。特別是少關節型（Oligoarticular）且抗核抗體（ANA）陽性的病童，併發慢性無症狀前虹彩炎（anterior uveitis）的機率極高，可導致失明，需長期以眼科裂隙燈追蹤。\n- D. 錯誤。Omalizumab 是一種抗 IgE 單株抗體，主要用於治療嚴重過敏性氣喘或慢性自發性蕁麻疹。治療嚴重 JIA 的常用生物製劑為抗 TNF-α 製劑（如 Etanercept、Adalimumab）或抗 IL-6 製劑（如 Tocilizumab）等，而非 Omalizumab。\n\n【核心考點】\nJIA 嚴重患者使用抗 TNF-α 或抗 IL-6 等生物製劑治療，Omalizumab（抗IgE）不用於 JIA。ANA 陽性的少關節型 JIA 需定期篩檢前虹彩炎。",
    "flashcard_front": "兒童特發性關節炎(JIA) / ANA陽性併發症 / 嚴重者生物製劑選擇",
    "flashcard_back": "ANA陽性少關節型JIA需定期追蹤前虹彩炎；JIA治療使用抗TNF-a或抗IL-6生物製劑，Omalizumab(抗IgE)無效。",
    "flashcard_summary": "JIA併發症與治療 -> ANA陽性防前虹彩炎；使用抗TNF-a/抗IL-6製劑而非Omalizumab。"
  },
  {
    "question_id": "114-1_medicine-4_017",
    "category": "皮膚科",
    "category_confidence": "high",
    "key_point": "慢性蕁麻疹的定義、自體免疫相關性及治療劑量調整原則。",
    "explanation": "【題幹解析】\n本題考查慢性蕁麻疹的臨床定義、自體免疫病因相關性、臨床檢查及治療指引。\n\n【選項詳解】\n- A. 錯誤。慢性蕁麻疹是指風疹塊（wheals）與血管性水腫反覆發作持續「6 週以上」（42天），而非 14 天。\n- B. 正確。慢性蕁麻疹常與自體免疫疾病（尤其是自體免疫甲狀腺疾病，如 Hashimoto's 或 Graves' disease）相關聯，可能是這些自體免疫疾病的先期表現。\n- C. 錯誤。慢性蕁麻疹多為自發性（chronic spontaneous urticaria），而非外在過敏原引起，因此血清特異性 IgE 檢驗並不作為常規首選檢測項目。\n- D. 錯誤。對於標準劑量第二代抗組織胺治療效果不佳的慢性蕁麻疹患者，臨床指引建議可將第二代抗組織胺劑量提高至最多 4 倍，而非不宜增加劑量。\n\n【核心考點】\n慢性蕁麻疹定義為反覆發作 6 週以上；與自體免疫（特別是甲狀腺疾病）有相關性；治療上抗組織胺劑量在無效時可調高至 4 倍。",
    "flashcard_front": "慢性蕁麻疹 / 定義發作時間 / 自體免疫關聯與抗組織胺調量",
    "flashcard_back": "慢性蕁麻疹定義為發作>6週；常與自體免疫甲狀腺疾病相關；治療無效時第二代抗組織胺可調高至4倍劑量。",
    "flashcard_summary": "慢性蕁麻疹 -> 定義>6週；常聯結自體免疫甲狀腺疾病；抗組織胺可增至4倍劑量。"
  },
  {
    "question_id": "114-1_medicine-4_018",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "新生兒血液學的生理性變化，包含紅血球大小、凝血因子與抗凝血蛋白的成熟度差異。",
    "explanation": "【題幹解析】\n本題考查剛出生健康足月新生兒的血液學與凝血因子生理特徵。\n\n【選項詳解】\n- A. 錯誤。與學齡兒童相比，新生兒剛出生時紅血球體積（MCV 95-115 fL）較大，血紅素（Hb 14-20 g/dL）也較高。生理性貧血（physiologic anemia）通常在出生後 8-12 週因促紅血球生成素減少等因素才發生。\n- B. 正確。新生兒肝臟發育尚未完全，多數由肝臟合成的凝血因子（如 II, VII, IX, X, XI, XII）在出生時均較成人低。但由血管內皮細胞產生的「第八因子（Factor VIII）」與 vWF，以及第五因子，在出生時的濃度已接近或高於成人。\n- C. 錯誤。新生兒體內抗凝血蛋白（Protein C, Protein S）活性與數值顯著「低於」學齡兒童與成人，使其在出生初期呈相對易栓狀態。\n- D. 錯誤。新生兒的血小板數量雖正常，但其血小板對外來刺激（如 collagen、ADP）的聚集與釋放功能在出生初期是較學齡兒童「差/降低」的。\n\n【核心考點】\n新生兒剛出生時紅血球大且血紅素高。凝血因子中，第八因子（Factor VIII）濃度接近成人，其他多數肝臟合成的凝血因子與抗凝血蛋白（Protein C, S）皆較成人低。",
    "flashcard_front": "新生兒血液學 / 紅血球大小與血紅素 / 凝血因子成熟度",
    "flashcard_back": "新生兒出生時紅血球體積大且Hb高；多數凝血因子及Protein C/S均較成人低，但第八因子(FVIII)濃度接近成人。",
    "flashcard_summary": "新生兒血液學 -> 紅血球大且Hb高；第八因子接近成人，其餘凝血因子及Protein C/S偏低。"
  },
  {
    "question_id": "114-1_medicine-4_019",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "兒童癌症的流行病學特徵、發病機制（偶發性為主）及青少年好發癌症類型。",
    "explanation": "【題幹解析】\n本題考查兒童癌症的發病因、好發類型及疫苗預防效果。\n\n【選項詳解】\n- A. 錯誤。兒童癌症絕大多數（90%以上）都是偶發性（sporadic）的基因突變引起，僅有少數（約 5-10%）與遺傳性基因缺陷或先天性症候群（如 Down syndrome）有關。選項敘述剛好相反。\n- B. 正確。在台灣與美國，白血病（Leukemia）都是最常見的兒童癌症，約佔所有兒童癌症的 30% 以上，其次為腦瘤。\n- C. 正確。全面接種 B 型肝炎疫苗能降低 B 肝帶原率，進而有效預防兒童及青少年期肝細胞癌（HCC）的發生。\n- D. 正確。骨癌（如骨肉瘤）、何杰金氏淋巴瘤、性腺癌（如卵巢癌或睪丸癌）及上皮癌等，確實在青少年時期（Adolescents）的發生率顯著高於幼童期。\n\n【核心考點】\n兒童癌症多數為偶發性（>90%），少數與遺傳相關。白血病是兒童最常見癌症。B肝疫苗能降低兒童肝細胞癌發生率。骨癌、何杰金氏淋巴瘤好發於青少年。",
    "flashcard_front": "兒童癌症 / 遺傳與偶發比例 / 最常見癌症 / 青少年好發類型",
    "flashcard_back": "兒童癌症90%以上為偶發性，僅少數與遺傳相關；白血病最常見；骨癌與何杰金氏淋巴瘤好發於青少年。",
    "flashcard_summary": "兒童癌症 -> 90%以上為偶發性而非遺傳；白血病最常見；骨癌好發於青少年。"
  },
  {
    "question_id": "114-1_medicine-4_020",
    "category": "小兒科",
    "category_confidence": "high",
    "key_point": "神經母細胞瘤（Neuroblastoma）骨髓轉移的經典病理特徵（Homer Wright pseudorosette）。",
    "explanation": "【題幹解析】\n3歲男童發燒、貧血，骨髓抽吸抹片見多處腫瘤細胞叢集（clumps）呈薔薇狀構造（rosette formation）且圍繞著纖維狀物質。此為 Homer Wright pseudorosette，是神經母細胞瘤（Neuroblastoma）轉移至骨髓的經典病理表現。\n\n【選項詳解】\n- A. 最有可能。神經母細胞瘤為兒童常見的實體腫瘤，易早期轉移至骨髓。在骨髓抹片中，小圓藍色腫瘤細胞會聚集並圍繞著中央的嗜酸性神經原纖維（neuropil），形成經典的 Homer Wright 偽薔薇花結（pseudorosette）。\n- B. 錯誤。急性淋巴性白血病（ALL）在骨髓中可見大量單個散在的淋巴芽細胞（blasts），不會形成圍繞神經纖維的 clumps 及 rosette。\n- C. 錯誤。感染性單核球增多症為 EBV 感染，骨髓中可見淋巴球增生，但無腫瘤細胞結節或 rosette 結構。\n- D. 錯誤。高雪氏症（Gaucher disease）骨髓中可見 Gaucher cells，即胞漿呈現如皺摺紙樣（wrinkled paper）的巨大吞噬細胞，而非 rosette。\n\n【核心考點】\n骨髓抹片中出現細胞叢集圍繞纖維物質形成薔薇花結（Homer Wright pseudorosette），是神經母細胞瘤（Neuroblastoma）骨髓轉移的特徵。Gaucher cell 具皺摺紙樣胞漿特徵。",
    "flashcard_front": "兒童骨髓抹片 / 腫瘤細胞叢集呈薔薇狀(rosette)圍繞纖維物 / 最可能診斷",
    "flashcard_back": "為神經母細胞瘤(Neuroblastoma)轉移，其經典病理為Homer Wright pseudorosette（小圓藍細胞圍繞神經纖維）。",
    "flashcard_summary": "神經母細胞瘤骨髓轉移 -> 骨髓見Homer Wright pseudorosette（小圓藍細胞圍繞神經纖維）。"
  }
]

out_dir = Path("scratch")
out_dir.mkdir(parents=True, exist_ok=True)
Path("scratch/updates_1141_med4_batch2.json").write_text(json.dumps(updates, ensure_ascii=False, indent=2), encoding="utf-8")
print("Batch 2 updates generated.")
