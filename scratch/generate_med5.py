# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure outputs directory exists
os.makedirs("reports/gemini_outputs", exist_ok=True)

batches_data = {}

# ----------------------------------------------------
# 109-1_medicine-5_batch-003 (Q31-Q45)
# ----------------------------------------------------
batches_data["109-1_medicine-5_batch-003"] = {
  "dataset_id": "109-1_medicine-5",
  "batch_id": "109-1_medicine-5_batch-003",
  "items": [
    {
      "question_id": "109-1_medicine-5_031",
      "question_number": 31,
      "correct_answer": "A",
      "category_group": "醫學（五）",
      "category": "一般外科",
      "category_confidence": "high",
      "key_point": "甲狀腺全切除術的併發症與術後管理。",
      "explanation": "甲狀腺全切除術相較於單側或部分切除，會增加副甲狀腺功能低下（低血鈣）及喉返神經受損（聲音沙啞）等手術併發症的風險，而非減少，故A選項敘述錯誤。術後由於甲狀腺組織已被全部切除，血清甲狀腺球蛋白（Tg）可用於追蹤腫瘤是否復發；全切除能清除所有甲狀腺組織，提高後續碘-131治療效果；且因無甲狀腺分泌荷爾蒙，患者必須終生服用甲狀腺素。",
      "flashcard_front": "甲狀腺全切除術 / 併發症 / 術後追蹤 / 碘-131",
      "flashcard_back": "全切除會增加副甲狀腺低下及喉返神經損傷風險；術後需終生補充甲狀腺素，並以甲狀腺球蛋白（Tg）作為復發追蹤指標。",
      "flashcard_summary": "甲狀腺全切除術 -> 增加副甲狀腺低下與喉返神經損傷風險，術後需終生服藥並以Tg追蹤。"
    },
    {
      "question_id": "109-1_medicine-5_032",
      "question_number": 32,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "一般外科",
      "category_confidence": "high",
      "key_point": "甲狀腺風暴的忌用藥物與治療原則。",
      "explanation": "Amiodarone是一種含有高濃度碘的抗心律不整藥物，在甲狀腺風暴患者中使用會引發碘負荷增加，進而可能加重甲狀腺毒症（Jod-Basedow效應），因此不宜給予。甲狀腺風暴的標準治療包括：使用Beta阻斷劑控制交感神經過度興奮；使用Propylthiouracil（PTU）抑制甲狀腺素合成及外周T4轉化為T3；以及使用腎上腺皮質素（Corticosteroids）抑制甲狀腺素釋放與外周轉化。",
      "flashcard_front": "甲狀腺風暴 / 忌用藥物 / Amiodarone / 碘負荷",
      "flashcard_back": "Amiodarone含高量碘，會加重甲狀腺毒症，故甲狀腺風暴禁用；治療應給予Beta阻斷劑、PTU及類固醇。",
      "flashcard_summary": "甲狀腺風暴禁用藥物 -> Amiodarone含高量碘會加重病情而禁用，應使用Beta阻斷劑、PTU及類固醇治療。"
    },
    {
      "question_id": "109-1_medicine-5_033",
      "question_number": 33,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "一般外科",
      "category_confidence": "high",
      "key_point": "甲狀腺結節的臨床評估流程與檢查選擇。",
      "explanation": "正子攝影（PET scan）價格昂貴且對良惡性甲狀腺結節的鑑別特異性不足，在甲狀腺結節的常規臨床評估中不列為優先或常規檢查。評估甲狀腺結節的首選是超音波及細針穿刺細胞學檢查（FNAC）；當結節延伸至胸骨下時，電腦斷層（CT）或磁振造影（MRI）有助於評估解剖關係與壓迫程度；若TSH偏低，可安排核醫甲狀腺掃描以評估是否為功能性結節。",
      "flashcard_front": "甲狀腺結節 / 評估首選 / 延伸胸骨下 / 正子攝影",
      "flashcard_back": "甲狀腺結節首選超音波與細針穿刺，胸骨下結節可用CT/MRI評估；正子攝影不具特異性且昂貴，不列為優先檢查。",
      "flashcard_summary": "甲狀腺結節檢查優先順序 -> 首選為超音波與細針穿刺，不優先考慮不具特異性的正子攝影。"
    },
    {
      "question_id": "109-1_medicine-5_034",
      "question_number": 34,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "一般外科",
      "category_confidence": "high",
      "key_point": "乳癌輔助性化學治療決策的必要病理因子。",
      "explanation": "在決定乳癌患者是否需要接受輔助性化學治療時，腫瘤大小（影響T分期）、淋巴結是否有轉移（影響N分期）以及荷爾蒙接受器（ER/PR）與HER2的表現狀況是關鍵的決策因子。腫瘤在乳房中的解剖位置（內側或外側）並非決定是否進行輔助化療的必要因子。因此，必要因子為1、2、4，故選C。",
      "flashcard_front": "乳癌輔助化療 / 病理決定因子 / 腫瘤大小 / 淋巴轉移 / 荷爾蒙接受器",
      "flashcard_back": "乳癌輔助化療決策依賴腫瘤大小、淋巴轉移及荷爾蒙接受器狀態（ER/PR/HER2），腫瘤的解剖位置並非決定因子。",
      "flashcard_summary": "乳癌輔助化療決定因子 -> 依賴腫瘤大小、淋巴結轉移及荷爾蒙接受器狀態，與腫瘤解剖位置無關。"
    },
    {
      "question_id": "109-1_medicine-5_035",
      "question_number": 35,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "一般外科",
      "category_confidence": "high",
      "key_point": "乳癌的臨床表徵與理學檢查特徵。",
      "explanation": "乳癌患者早期可能僅有單純的無痛性腫塊，並非所有乳癌都會出現皮膚凹陷，因此沒有皮膚凹陷絕對不能排除乳癌的可能性，B選項敘述錯誤。皮膚凹陷的發生是由於腫瘤侵犯並牽拉Cooper's ligament（乳房懸韌帶）所致，其對乳癌診斷的陽性預測值相當高；若伴隨腋下淋巴結腫大，則罹患乳癌或已發生轉移的可能性會顯著增加。",
      "flashcard_front": "乳房腫塊 / 皮膚凹陷 / Cooper's ligament / 排除乳癌",
      "flashcard_back": "皮膚凹陷與Cooper's ligament受侵犯有關，具高陽性預測值；但無皮膚凹陷絕不可排除乳癌之可能。",
      "flashcard_summary": "皮膚凹陷與乳癌診斷 -> 凹陷與Cooper's ligament有關，但無凹陷不能排除乳癌。"
    },
    {
      "question_id": "109-1_medicine-5_036",
      "question_number": 36,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "一般外科",
      "category_confidence": "high",
      "key_point": "腋下淋巴結廓清術易受損神經及其支配範圍。",
      "explanation": "肋間臂神經（Intercostobrachial nerve）穿過腋窩並支配上臂內側及腋下的皮膚感覺，在進行腋下淋巴結廓清術時若不慎將其切斷，會導致病人術後出現上臂內側感覺麻木或慢性疼痛，故選C。相較之下，長胸神經受損會導致翼狀肩胛；胸背神經受損會影響背闊肌功能；胸內側神經則支配胸小肌與胸大肌。",
      "flashcard_front": "腋下淋巴結廓清 / 上臂內側麻木 / 肋間臂神經",
      "flashcard_back": "肋間臂神經負責上臂內側感覺，廓清術中切斷會導致該區麻木或疼痛；長胸神經受損則造成翼狀肩胛。",
      "flashcard_summary": "肋間臂神經受損 -> 腋下淋巴結廓清時切斷肋間臂神經，會導致上臂內側麻木或疼痛。"
    },
    {
      "question_id": "109-1_medicine-5_037",
      "question_number": 37,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "一般外科",
      "category_confidence": "high",
      "key_point": "乳房腫塊的臨床評估步驟。",
      "explanation": "對於45歲摸到乳房腫塊的女性，最恰當的初步處置是安排乳房超音波或乳房攝影等影像學檢查來評估腫塊性質。單憑理學檢查正常不足以排除惡性腫瘤，仍需影像學輔助，故A錯誤；在未經影像評估前直接進行手術切除切片不符合診斷步驟，故B錯誤；血清腫瘤標記CA15-3不適用於乳癌的早期篩檢或診斷，故D錯誤。",
      "flashcard_front": "乳房腫塊評估 / 45歲女性 / 影像檢查首選 / CA15-3",
      "flashcard_back": "發現乳房腫塊應首選乳房超音波或攝影評估；理學檢查正常不可直接排除，且CA15-3不適用於早期篩檢。",
      "flashcard_summary": "乳房腫塊初步處置 -> 發現乳房腫塊應安排乳房超音波或乳房攝影，而非單靠理學檢查或直接手術。"
    },
    {
      "question_id": "109-1_medicine-5_038",
      "question_number": 38,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "小兒外科",
      "category_confidence": "high",
      "key_point": "新生兒先天性腸胃道阻塞的X光特徵。",
      "explanation": "Double-bubble sign（雙氣泡徵）是新生兒十二指腸閉鎖（Duodenal atresia）在腹部X光上的經典影像表現，代表胃與近端十二指腸因阻塞而擴張積氣。幽門狹窄通常表現為單氣泡（胃擴張積氣）；小腸閉鎖則常呈現多個氣泡與腸段擴張；肛門閉鎖則會導致低位腸阻塞及廣泛結腸擴張。",
      "flashcard_front": "double-bubble sign / 新生兒 / 十二指腸閉鎖",
      "flashcard_back": "雙氣泡徵（Double-bubble sign）為十二指腸閉鎖的典型影像特徵，由擴張的胃與近端十二指腸積氣所造成。",
      "flashcard_summary": "double-bubble sign -> 十二指腸閉鎖的典型影像特徵，由胃與近端十二指腸積氣膨脹形成。"
    },
    {
      "question_id": "109-1_medicine-5_039",
      "question_number": 39,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "小兒外科",
      "category_confidence": "high",
      "key_point": "氣管食道瘻管及食道閉鎖的臨床特徵。",
      "explanation": "新生兒出生後若口吐泡沫唾液（唾液無法下嚥），且上腹部微脹（氣體通過遠端瘻管進入胃腸道），最經典的診斷為食道閉鎖合併遠端氣管食道瘻管（Type C）。十二指腸閉鎖主要表現為膽汁性嘔吐及雙氣泡徵；中腸扭結好發於出生數天至數週後，以急性膽汁性嘔吐與腹痛為主；橫膈膜疝氣則常伴隨嚴重的呼吸窘迫與舟狀腹。",
      "flashcard_front": "吐泡沫唾液 / 上腹微脹 / 氣管食道瘻管 (TEF) / 食道閉鎖",
      "flashcard_back": "吐泡沫唾液提示食道閉鎖，氣體經遠端瘻管（distal TEF）進入胃腸會導致上腹微脹。",
      "flashcard_summary": "吐泡沫與上腹脹 -> 提示食道閉鎖合併遠端氣管食道瘻管（Type C）。"
    },
    {
      "question_id": "109-1_medicine-5_040",
      "question_number": 40,
      "correct_answer": "D",
      "category_group": "醫學（五）",
      "category": "小兒外科",
      "category_confidence": "high",
      "key_point": "新生兒畸胎瘤的常見好發部位。",
      "explanation": "薦尾椎部畸胎瘤（Sacrococcygeal teratoma）是新生兒及嬰幼兒期最常見的先天性生殖細胞腫瘤，也是畸胎瘤最好發的部位。雖然畸胎瘤也可能發生於縱隔腔、卵巢或睪丸，但這些部位在新生兒期的發生率皆顯著低於薦尾椎部。",
      "flashcard_front": "新生兒 / 畸胎瘤 (teratoma) / 最常見部位",
      "flashcard_back": "薦尾椎部是新生兒畸胎瘤最常見的好發部位，多數為良性但有轉變惡性風險，需儘早切除。",
      "flashcard_summary": "新生兒畸胎瘤部位 -> 薦尾椎部為新生兒畸胎瘤最常見之好發部位。"
    },
    {
      "question_id": "109-1_medicine-5_041",
      "question_number": 41,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "小兒外科",
      "category_confidence": "high",
      "key_point": "兒童腸套疊的臨床特徵與治療原則。",
      "explanation": "大多數兒童腸套疊首選以生理食鹽水、空氣或鋇劑進行引導下灌腸復位，成功率高，並非大多數都需要手術治療，故B選項錯誤。腸套疊好發於3個月到2歲的嬰幼兒，以迴腸套入盲腸最為常見；但若病童已出現腸壞死、穿孔或腹膜炎跡象，則為灌腸禁忌症，必須立即安排手術治療。",
      "flashcard_front": "兒童腸套疊 / 灌腸復位 / 腹膜炎 / 手術適應症",
      "flashcard_back": "大多數兒童腸套疊可先以空氣或食鹽水灌腸復位成功；僅在復位失敗或合併腹膜炎/穿孔時才需手術治療。",
      "flashcard_summary": "兒童腸套疊治療 -> 首選空氣或液體灌腸復位，非首選手術；合併腹膜炎時才須手術。"
    },
    {
      "question_id": "109-1_medicine-5_042",
      "question_number": 42,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "小兒外科",
      "category_confidence": "high",
      "key_point": "早產兒壞死性腸炎（NEC）的治療原則與手術指徵。",
      "explanation": "早產兒壞死性腸炎（NEC）的初步處置以內科支持療法為主，包括禁食、放置口胃管減壓、補充水分與電解質，以及給予廣效性抗生素，約有70-80%的病患可透過保守治療痊癒，並非所有病患均需接受手術治療，故C選項錯誤。手術治療僅適用於出現腸穿孔（腹部放射線檢查顯示氣腹）或內科治療無效、病情持續惡化的病患。",
      "flashcard_front": "壞死性腸炎 (NEC) / 支持療法 / 腸穿孔 / 手術指徵",
      "flashcard_back": "NEC初步處置為禁食、減壓及抗生素等保守治療，僅在內科治療無效或出現腸穿孔（氣腹）時才需要手術。",
      "flashcard_summary": "壞死性腸炎治療 -> 初步採禁食、減壓等內科支持療法，僅在穿孔或治療惡化時手術。"
    },
    {
      "question_id": "109-1_medicine-5_043",
      "question_number": 43,
      "correct_answer": "A",
      "category_group": "醫學（五）",
      "category": "大腸直腸科",
      "category_confidence": "high",
      "key_point": "發炎性腸疾（UC與CD）的流行病學、病理及臨床特徵。",
      "explanation": "發炎性腸疾（IBD）在西方國家（如北歐、美國）的發生率與盛行率顯著高於亞洲地區，雖然近年來亞洲的病例數在上升，但整體而言仍以歐美地區的發生率較高，故A選項敘述錯誤。潰瘍性結腸炎主要波及黏膜與黏膜下層，病變連續；克隆氏症則為跳躍式、侵犯腸壁全層且可波及消化道任何部位；兩者皆常伴隨腸外表現如關節炎、虹膜炎、皮膚病變及硬化性膽管炎等。",
      "flashcard_front": "發炎性腸疾 (IBD) / 流行病學 / 腸外表現 / UC與CD病理",
      "flashcard_back": "IBD好發於歐美而非亞洲。UC侵犯黏膜層且連續；CD為全壁式且呈跳躍性；兩者皆有虹膜炎、關節炎等腸外表現。",
      "flashcard_summary": "IBD特徵與流行病學 -> 好發於歐美，UC為黏膜層連續病變，CD為跳躍式全壁發炎。"
    },
    {
      "question_id": "109-1_medicine-5_044",
      "question_number": 44,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "一般外科",
      "category_confidence": "high",
      "key_point": "急性闌尾炎的典型臨床特徵與鑑別診斷。",
      "explanation": "此病患的症狀為典型的轉移性右下腹痛（從肚臍周圍開始不適，隨後轉移至右下腹McBurney's point），這是急性闌尾炎的經典臨床表現。急性膽囊炎主要表現為右上腹痛且常放射至右肩（Murphy's sign陽性）；乙狀結腸憩室炎在西方人多表現為左下腹痛；消化性潰瘍穿孔則常表現為突發性全腹劇痛與板狀腹。",
      "flashcard_front": "轉移性右下腹痛 / 肚臍周圍不適 / 急性闌尾炎",
      "flashcard_back": "肚臍周圍痛隨後轉移至右下腹為典型急性闌尾炎表現；需與膽囊炎（右上腹）或憩室炎相鑑別。",
      "flashcard_summary": "轉移性右下腹痛 -> 典型急性闌尾炎特徵，腹痛由臍周轉移至右下腹。"
    },
    {
      "question_id": "109-1_medicine-5_045",
      "question_number": 45,
      "correct_answer": "A",
      "category_group": "醫學（五）",
      "category": "大腸直腸科",
      "category_confidence": "high",
      "key_point": "全直腸繫膜切除術（TME）的臨床效益與神經保留。",
      "explanation": "全直腸繫膜切除術（TME）是直腸癌手術的金標準。TME強調在直視下沿著胚胎解剖平面進行銳性分離，不僅能完整切除直腸及其周圍淋巴結，還能有效保留盆腔自主神經，因此與傳統手術相比，它顯著減少了術後性功能障礙（性無能）和排尿功能異常的機率，且能降低局部復發率並改善患者的長期預後，故A選項敘述錯誤。",
      "flashcard_front": "TME / 直腸癌 / 自主神經保留 / 術後性功能",
      "flashcard_back": "TME可精準保留盆腔自主神經，減少術後性無能及排尿障礙的機率，同時能降低復發率並改善長期預後。",
      "flashcard_summary": "TME的效益 -> 精準保留盆腔自主神經，降低性無能與排尿障礙風險，減少復發。"
    }
  ]
}

# ----------------------------------------------------
# 109-1_medicine-5_batch-004 (Q46-Q60)
# ----------------------------------------------------
batches_data["109-1_medicine-5_batch-004"] = {
  "dataset_id": "109-1_medicine-5",
  "batch_id": "109-1_medicine-5_batch-004",
  "items": [
    {
      "question_id": "109-1_medicine-5_046",
      "question_number": 46,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "神經外科",
      "category_confidence": "high",
      "key_point": "脊髓內腫瘤的流行病學與常見病理類型。",
      "explanation": "最常見的脊髓內腫瘤（intramedullary spinal cord tumor）是室管膜瘤（ependymoma）和星狀細胞瘤（astrocytoma），而轉移性脊髓內腫瘤（intramedullary metastasis）臨床上非常罕見，僅占不到2%，因此C選項敘述錯誤。脊髓內腫瘤約占所有脊椎腫瘤的5-10%；原發性脊髓內淋巴瘤極其罕見；黏液乳突狀室管膜瘤通常好發於脊髓圓錐與終絲處，即腰薦椎部位。",
      "flashcard_front": "脊髓內腫瘤 / 最常見 / 轉移性 / 黏液乳突狀室管膜瘤",
      "flashcard_back": "最常見脊髓內腫瘤為室管膜瘤及星狀細胞瘤，轉移癌極罕見；黏液乳突狀室管膜瘤好發於腰薦椎（脊髓圓錐/終絲）。",
      "flashcard_summary": "脊髓內腫瘤特徵 -> 最常見為室管膜瘤及星狀細胞瘤，轉移癌罕見，黏液乳突狀者好發於腰薦椎。"
    },
    {
      "question_id": "109-1_medicine-5_047",
      "question_number": 47,
      "correct_answer": "D",
      "category_group": "醫學（五）",
      "category": "心臟外科",
      "category_confidence": "high",
      "key_point": "心臟移植的適應症與禁忌症。",
      "explanation": "對於複雜的先天性心臟病，如果可以使用傳統手術矯正，應優先選擇重建或矯正手術，而非直接進行心臟移植，因此D不適合做心臟移植。心臟移植的適應症包括：內科藥物治療無效的末期心臟衰竭（如LVEF < 20%且反覆住院者）、無法行冠狀動脈繞道手術的嚴重心肌缺血、以及已裝設ECMO或心室輔助器且無法脫離的患者。",
      "flashcard_front": "心臟移植 / 適應症 / 先天性心臟病 / 替代治療",
      "flashcard_back": "末期心衰竭、無法行血運重建的缺血或無法脫離輔助器者為心臟移植適應症；若能以傳統矯正手術治療者，不應行心臟移植。",
      "flashcard_summary": "心臟移植適應症 -> 適用於末期心衰竭或無法脫離輔助器者，若可由常規手術矯正則不適用。"
    },
    {
      "question_id": "109-1_medicine-5_048",
      "question_number": 48,
      "correct_answer": "D",
      "category_group": "醫學（五）",
      "category": "一般外科",
      "category_confidence": "high",
      "key_point": "Calot氏三角（Triangle of Calot）的解剖邊界。",
      "explanation": "Calot氏三角（膽囊三角）的解剖學邊界包括：上方為肝臟下緣（右肝下緣），內側為總肝管，外側為膽囊管。右門靜脈並不屬於Calot氏三角的邊界構造，故D為正確答案。Calot氏三角內含膽囊動脈及Lund's淋巴結，是膽囊切除術中防範膽管損傷極為重要的解剖地標。",
      "flashcard_front": "Calot氏三角 / 解剖邊界 / 膽囊切除 / 內容物",
      "flashcard_back": "Calot氏三角的邊界為肝臟下緣、總肝管及膽囊管；三角內有膽囊動脈通過，是手術防範膽管損傷的關鍵地標。",
      "flashcard_summary": "Calot氏三角邊界 -> 肝下緣、總肝管、膽囊管，內有膽囊動脈，右門靜脈不屬於邊界。"
    },
    {
      "question_id": "109-1_medicine-5_049",
      "question_number": 49,
      "correct_answer": "A",
      "category_group": "醫學（五）",
      "category": "外科概論",
      "category_confidence": "high",
      "key_point": "高鉀血症的心電圖特徵。",
      "explanation": "高鉀血症（血鉀 > 5.5 mmol/L）的早期心電圖特徵是出現對稱且高尖的T波（tall peaked T-waves），故A為正確答案。隨著血鉀持續升高，會陸續出現PR間期延長、P波變平甚至消失、QRS波變寬（非縮短）等變化，最後甚至呈現正弦波並引發心室顫動。 depressed T-waves 和 U-waves 則是低鉀血症的特徵。",
      "flashcard_front": "高鉀血症 / 心電圖 (ECG) / 高尖T波 / 寬QRS",
      "flashcard_back": "高鉀血症早期表現為高尖T波（tall peaked T-wave）；嚴重時出現QRS變寬、P波消失；低鉀血症則表現為T波扁平及U波。",
      "flashcard_summary": "高鉀血症與心電圖 -> 早期表現為高尖T波，嚴重時QRS變寬；低鉀血症則出現U波。"
    },
    {
      "question_id": "109-1_medicine-5_050",
      "question_number": 50,
      "correct_answer": "D",
      "category_group": "醫學（五）",
      "category": "外科概論",
      "category_confidence": "high",
      "key_point": "急性高鉀血症治療藥物的作用時間與機轉。",
      "explanation": "給與腸胃道排鉀陽離子交換樹脂（如Kayexalate）需要經由腸道作用，其發揮效果通常需要數小時，是在所有急性高鉀血症治療中效果最慢的方法。相對地，靜脈注射鈣離子在數分鐘內即可發揮穩定心肌細胞膜的作用；使用胰島素加葡萄糖或碳酸氫鈉則能在30分鐘內促使細胞外的鉀離子暫時轉移至細胞內，達到快速降低血鉀的效果。",
      "flashcard_front": "急性高鉀血症治療 / 鈣離子 / 胰島素 / 排鉀樹脂 (Kayexalate)",
      "flashcard_back": "鈣離子最快發揮作用（穩定心肌膜，不降血鉀）；胰島素促鉀入細胞（30分鐘內起效）；腸胃道排鉀樹脂起效最慢（需數小時）。",
      "flashcard_summary": "高鉀血症治療速度 -> 鈣離子最快（穩定心肌），胰島素次之（促鉀移入），腸道排鉀樹脂最慢（真正排鉀）。"
    },
    {
      "question_id": "109-1_medicine-5_051",
      "question_number": 51,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "心臟外科",
      "category_confidence": "high",
      "key_point": "左至右分流先天性心臟病的手術治療原則。",
      "explanation": "根據題意，病童為左至右分流（非發紺型）且伴隨肺高壓與心衰竭表現，常見於大型心室中隔缺損（VSD）。對於此類肺血流過多引起的左至右分流疾病，手術治療可選擇進行完全矯正手術直接修補缺損，或是先進行肺動脈環縮術（PA banding）以減少肺部血流量、降低肺動脈壓並改善心衰竭。Blalock-Taussig分流手術是增加肺血流的手術，適用於發紺型先天性心臟病，在此病人會加重肺充血；肺動脈瓣切開術適用於肺動脈瓣狹窄，非此症處置。因此對病患有幫助的是2與3，選B。",
      "flashcard_front": "左至右分流 / 肺高壓 / 完全矯正 / 肺動脈環縮術 (PA banding) / B-T shunt",
      "flashcard_back": "左至右分流伴肺血流過多者，治療應採完全修補或PA banding（限制肺血流）；B-T shunt會增加肺血流，僅用於發紺型心臟病。",
      "flashcard_summary": "左至右分流手術選擇 -> 適用完全矯正或PA banding；發紺型（肺血流少）才用B-T shunt。"
    },
    {
      "question_id": "109-1_medicine-5_052",
      "question_number": 52,
      "correct_answer": "A",
      "category_group": "醫學（五）",
      "category": "心臟外科",
      "category_confidence": "high",
      "key_point": "艾森門格症候群的病理生理學機轉。",
      "explanation": "當左至右分流的先天性心臟病長期未接受手術治療時，肺部血流量長期過多會導致肺動脈小血管內皮受損及平滑肌增生肥厚，進而引起肺動脈血管壁硬化與肺血管阻力顯著上升。當肺動脈壓超過體循環壓力時，分流方向會轉變為右至左分流，病童因而出現發紺及缺氧現象，此病理生理學改變稱為艾森門格症候群（Eisenmenger syndrome），故選A。",
      "flashcard_front": "艾森門格症候群 / Eisenmenger syndrome / 左至右轉右至左 / 肺動脈阻力",
      "flashcard_back": "長期左至右分流導致肺動脈硬化、阻力增加，最終壓力反轉形成右至左分流並出現發紺，此時已不可行單純缺損修補。",
      "flashcard_summary": "艾森門格症候群機轉 -> 長期左至右分流致肺血管阻力增高，反轉為右至左分流且發紺。"
    },
    {
      "question_id": "109-1_medicine-5_053",
      "question_number": 53,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "心臟外科",
      "category_confidence": "high",
      "key_point": "艾森門格症候群的終末期手術治療選擇。",
      "explanation": "一旦患者發展為艾森門格症候群，此時若單純修補心室中隔缺損會導致右心室因無法承受極高的肺血管阻力而發生急性衰竭，因此已失去單純缺損修補的手術時機。此時唯一能根治的方法是進行心肺移植手術（heart-lung transplantation），或是在心室中隔缺損不修補的前提下進行單純肺移植，故B為最適當選項。",
      "flashcard_front": "艾森門格症候群 / 終末期治療 / 心肺移植 / 缺損修補禁忌",
      "flashcard_back": "發展為艾森門格症候群後，單純修補VSD為禁忌症；此時唯一根治手術是心肺移植。",
      "flashcard_summary": "艾森門格症候群治療 -> 已無法進行單純缺損修補，終末期需行心肺移植。"
    },
    {
      "question_id": "109-1_medicine-5_054",
      "question_number": 54,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "胸腔外科",
      "category_confidence": "high",
      "key_point": "胸腔出口症候群的流行病學與診治原則。",
      "explanation": "胸腔出口症候群（TOS）是指臂神經叢或鎖骨下血管在胸腔出口處受壓迫所產生的症狀，臨床上以「年輕至中年女性」患者居多（男女比例約1:3至1:4），而非中年男性，故C選項錯誤。大多數TOS患者（超過90%）是由於神經受壓迫（神經型TOS），且初步治療首選物理治療與保守非手術療法。",
      "flashcard_front": "胸腔出口症候群 (TOS) / 流行病學 / 壓迫來源 / 保守治療",
      "flashcard_back": "TOS因神經叢或鎖骨下血管受壓所致，以女性居多，症狀以神經壓迫為主，治療首選保守物理治療。",
      "flashcard_summary": "胸腔出口症候群特徵 -> 壓迫神經叢或血管所致，好發於女性，首選保守治療。"
    },
    {
      "question_id": "109-1_medicine-5_055",
      "question_number": 55,
      "correct_answer": "D",
      "category_group": "醫學（五）",
      "category": "胸腔外科",
      "category_confidence": "high",
      "key_point": "胸腔出口症候群的特殊理學檢查方法。",
      "explanation": "臨床上常用於評估胸腔出口症候群（TOS）的特殊理學檢查包括：Adson test（斜角肌測試，轉頭並深呼吸）、Halsted test（肋鎖測試，肩向後向下擺動）及Wright test（過度外展測試，手臂外展）。Breath test（呼吸試驗）通常用於診斷幽門螺桿菌感染或乳糖不耐症，並非檢查TOS的方法，故選D。",
      "flashcard_front": "TOS / 理學檢查 / Adson / Halsted / Wright / Breath test",
      "flashcard_back": "Adson test、Halsted test及Wright test皆為診斷TOS的理學檢查；Breath test與此無關。",
      "flashcard_summary": "TOS理學檢查 -> Adson、Halsted、Wright test為常用TOS檢查，Breath test非TOS檢查。"
    },
    {
      "question_id": "109-1_medicine-5_056",
      "question_number": 56,
      "correct_answer": "A",
      "category_group": "醫學（五）",
      "category": "骨科",
      "category_confidence": "high",
      "key_point": "常見骨生成腫瘤的臨床病理特徵。",
      "explanation": "骨肉瘤是惡性度極高的骨生成腫瘤，在初次診斷時，約有10%至20%的患者已經存在微小轉移，其中最常見的轉移部位是肺部，故A選項最正確。骨軟骨瘤是常見的良性骨腫瘤，惡變率極低，通常無症狀者只需追蹤即可，不需均切除（B錯誤）；骨母細胞瘤通常比骨樣骨瘤大且具破壞性，藥物不易完全緩解，多需手術刮除（C錯誤）；骨樣骨瘤好發於長骨骨幹或幹骺端，而非骨骺（D錯誤）。",
      "flashcard_front": "骨肉瘤 / 肺轉移 / 骨樣骨瘤 / 骨軟骨瘤",
      "flashcard_back": "骨肉瘤初診時常已伴隨肺部微小轉移；骨樣骨瘤好發於骨幹而非骨骺；骨軟骨瘤為良性，非皆需切除。",
      "flashcard_summary": "骨生成腫瘤特徵 -> 骨肉瘤診斷時常已有肺轉移，骨樣骨瘤好發於骨幹，骨軟骨瘤多追蹤即可。"
    },
    {
      "question_id": "109-1_medicine-5_057",
      "question_number": 57,
      "correct_answer": "D",
      "category_group": "醫學（五）",
      "category": "骨科",
      "category_confidence": "high",
      "key_point": "頸椎外傷中電腦斷層雙腔影像的解讀。",
      "explanation": "在頸椎電腦斷層的軸向影像中，若看到第六、七頸椎處出現「雙腔影像（double-lumen sign）」，代表兩者之間發生嚴重的前後移位，使椎管在同一個切面上重疊顯影。此為頸椎脫位（dislocation）或小面關節鎖定的特徵性影像表現。因此，D選項為最適當的診斷。",
      "flashcard_front": "頸椎損傷 / 雙腔影像 / double-lumen sign / 脫位",
      "flashcard_back": "電腦斷層軸向影像中的雙腔影像（double-lumen sign）是椎骨嚴重移位、椎管重疊所致，提示頸椎脫位（dislocation）。",
      "flashcard_summary": "頸椎雙腔影像 -> 電腦斷層軸向切面呈現雙腔影像（double-lumen sign）提示頸椎脫位。"
    },
    {
      "question_id": "109-1_medicine-5_058",
      "question_number": 58,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "骨科",
      "category_confidence": "high",
      "key_point": "膝關節後十字韌帶斷裂的受傷機轉與臨床表現。",
      "explanation": "當膝關節正面遭受撞擊（如膝蓋撞擊機車前擋板，稱為儀表板損傷），會迫使脛骨相對於股骨向後移位，此為造成後十字韌帶（PCL）斷裂的典型受傷機轉。PCL的主要功能是限制脛骨後移，斷裂後在下樓梯時，常會出現膝蓋瞬間軟腳（giving way）、無法支撐的無力感。前十字韌帶（ACL）斷裂則多在急停、轉身時發生，且受傷當下常有劇烈腫脹。",
      "flashcard_front": "儀表板損傷 / 下樓梯軟腳 / 脛骨後移 / 後十字韌帶 (PCL)",
      "flashcard_back": "膝關節正面撞擊（脛骨後移）易導致後十字韌帶（PCL）斷裂；其典型症狀為走下樓梯時膝關節軟弱無力。",
      "flashcard_summary": "後十字韌帶斷裂 -> 膝蓋正面撞擊致PCL斷裂，臨床特徵為下樓梯時膝蓋軟弱無力。"
    },
    {
      "question_id": "109-1_medicine-5_059",
      "question_number": 59,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "骨科",
      "category_confidence": "high",
      "key_point": "橈骨近端骨折可能合併的神經損傷。",
      "explanation": "橈神經深支穿過旋後肌的Frohse弓後，改稱為後骨間神經（PIN）。由於PIN解剖位置緊貼著橈骨頸部外側繞行，因此在橈骨近端或橈骨頸骨折時，極易因骨折移位或術中牽拉而受損，導致病人出現垂指症（指骨間關節無法伸展，但手腕伸展功能多保留，因橈側伸腕肌受橈神經主幹支配），故選B。",
      "flashcard_front": "橈骨頸骨折 / 旋後肌 / 垂指症 / 後骨間神經 (PIN)",
      "flashcard_back": "後骨間神經（PIN）環繞橈骨頸部，橈骨近端骨折時易受損，導致手指無法伸展（垂指），但手腕伸展功能多保留。",
      "flashcard_summary": "橈骨頸骨折與神經損傷 -> 易合併後骨間神經（PIN）受損，引起垂指症。"
    },
    {
      "question_id": "109-1_medicine-5_060",
      "question_number": 60,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "骨科",
      "category_confidence": "high",
      "key_point": "脊椎轉移性腫瘤的治療原則與手術適應症。",
      "explanation": "對於沒有明顯神經壓迫症狀、大小便功能正常且脊椎穩定的脊椎轉移性腫瘤患者，不應直接安排脊椎減壓及固定手術，C選項錯誤。此時的首選治療通常是局部放射線治療與內科系統性抗癌治療；手術減壓固定僅適用於脊椎不穩定、出現神經壓迫症狀（如肢體無力、馬尾症候群）或放療無效的背痛患者。",
      "flashcard_front": "脊椎轉移瘤 / 無神經壓迫 / 放射治療 / 手術指徵",
      "flashcard_back": "脊椎轉移瘤若無神經壓迫且結構穩定，首選放療而非手術；手術主要用於脊椎不穩、神經壓迫或放療無效之劇痛。",
      "flashcard_summary": "脊椎轉移瘤處置 -> 無神經壓迫時首選放射治療與內科治療，不可盲目進行減壓固定手術。"
    }
  ]
}

# ----------------------------------------------------
# 109-1_medicine-5_batch-005 (Q61-Q75)
# ----------------------------------------------------
batches_data["109-1_medicine-5_batch-005"] = {
  "dataset_id": "109-1_medicine-5",
  "batch_id": "109-1_medicine-5_batch-005",
  "items": [
    {
      "question_id": "109-1_medicine-5_061",
      "question_number": 61,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "骨科",
      "category_confidence": "high",
      "key_point": "髖關節後脫位的典型臨床畸形表現。",
      "explanation": "在車禍撞擊中（如膝蓋撞擊儀表板），股骨幹被迫向後推擠，最容易導致髖關節後脫位（posterior hip dislocation）。髖關節後脫位患者的下肢會呈現典型的畸形外觀：肢體變短，且髖關節處於屈曲（flexion）、內收（adduction）及內旋（internal rotation）狀態，故選B。相對地，前脫位則會呈現外展及外旋狀態。",
      "flashcard_front": "髖關節後脫位 / 典型畸形 / 屈曲、內收、內旋 / 變短",
      "flashcard_back": "髖關節後脫位特徵為患肢變短、屈曲、內收及內旋；前脫位則呈現外展及外旋狀態。",
      "flashcard_summary": "髖關節後脫位特徵 -> 患肢變短、屈曲、內收、內旋；前脫位則為外展、外旋。"
    },
    {
      "question_id": "109-1_medicine-5_062",
      "question_number": 62,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "骨科",
      "category_confidence": "high",
      "key_point": "兒童股骨頭缺血性壞死（LCPD）的預後評估指標。",
      "explanation": "兒童股骨頭部缺血性壞死症（LCPD）的預後與發病年齡密切相關，發病時年齡越輕（特別是小於5歲），由於股骨頭重塑（remodeling）的潛力較大，其預後通常較好。因此，發病年紀較輕是預後良好的指標，非預後不好徵象，故選C。Catterall預後不良徵象包括：股骨頭外側放射線通透性增加、生長板呈水平向、壞死範圍廣泛（如達80%）以及股骨頭外側半脫位等。",
      "flashcard_front": "LCPD / 兒童股骨頭壞死 / 預後好壞 / 發病年齡",
      "flashcard_back": "LCPD發病年齡越輕（<5歲）重塑能力強，預後越好；股骨頭外側壞死、水平生長板及壞死面積大（>50%）提示預後不良。",
      "flashcard_summary": "LCPD預後指標 -> 年齡越小（<5歲）預後越好；外側受波及或壞死面積大則預後差。"
    },
    {
      "question_id": "109-1_medicine-5_063",
      "question_number": 63,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "骨科",
      "category_confidence": "high",
      "key_point": "痛風的臨床特徵、診斷與急性期治療。",
      "explanation": "痛風急性發作時的第一線治療為使用非類固醇消炎藥（NSAIDs）、秋水仙素（colchicine）或類固醇以緩解發炎與疼痛，故B選項正確。急性痛風發作時，約有30%以上的患者其血清尿酸值可能在正常範圍內，因此不能單憑尿酸正常排除診斷（A錯誤）；軟骨鈣質沉著病是焦磷酸鈣結晶沉積（假性痛風）的X光表現，而非痛風（C錯誤）；痛風的尿酸鈉結晶在偏光顯微鏡下呈現陰性雙折射的針狀結晶，陽性雙折射是假性痛風的特徵（D錯誤）。",
      "flashcard_front": "痛風急性發作 / 尿酸值 / 偏光顯微鏡 / 陰性雙折射",
      "flashcard_back": "急性痛風首選NSAIDs或秋水仙素；發作時血尿酸可正常，關節液偏光顯微鏡呈陰性雙折射針狀結晶（假性痛風呈陽性雙折射）。",
      "flashcard_summary": "痛風診斷與治療 -> 急性期使用NSAIDs或秋水仙素，尿酸結晶呈陰性雙折射，發作時血尿酸可能正常。"
    },
    {
      "question_id": "109-1_medicine-5_064",
      "question_number": 64,
      "correct_answer": "A",
      "category_group": "醫學（五）",
      "category": "泌尿科",
      "category_confidence": "high",
      "key_point": "尿路結石（含鈣結石）的成因與生化促進/抑制因子。",
      "explanation": "形成含鈣尿路結石（如草酸鈣結石）的促進因子包括：尿中鈣離子濃度上升（高尿鈣）、尿中草酸鹽濃度上升（高草酸尿）以及尿中尿酸濃度上升（高尿酸尿可作為結晶核），因此1、2、3皆是形成結石的常見病因。相反地，尿中的檸檬酸鹽（citrate）能與鈣離子結合形成高溶解性的檸檬酸鈣，從而抑制草酸鈣結晶的形成，因此尿中檸檬酸鹽上升是預防結石的保護因子，故4非結石原因，選A。",
      "flashcard_front": "含鈣腎結石 / 高尿鈣 / 高草酸 / 檸檬酸鹽 / 促進與抑制",
      "flashcard_back": "高尿鈣、高草酸與高尿酸會促進含鈣結石形成；而檸檬酸鹽為結石抑制因子，濃度上升可減少結石。",
      "flashcard_summary": "含鈣結石成因 -> 尿鈣、草酸、尿酸上升促成結石；檸檬酸鹽上升則會抑制結石。"
    },
    {
      "question_id": "109-1_medicine-5_065",
      "question_number": 65,
      "correct_answer": "D",
      "category_group": "醫學（五）",
      "category": "泌尿科",
      "category_confidence": "high",
      "key_point": "腎上腺意外瘤的處理原則與手術指徵。",
      "explanation": "腎上腺意外瘤（incidentaloma）如果發現其不具分泌功能，但其直徑大於4公分，或者影像特徵高度懷疑惡性時，由於皮質癌的風險高，仍強烈建議接受手術切除，而非皆不需手術，故D選項錯誤。大部分腎上腺腫瘤是健康檢查或其他原因檢查時意外發現；腹腔鏡腎上腺切除術是目前標準術式；凡是具功能性（如庫欣氏症、原發醛固酮症）或體積大於5公分者均應手術。",
      "flashcard_front": "腎上腺意外瘤 / 手術指徵 / 無功能腫瘤 / 腫瘤大小",
      "flashcard_back": "腎上腺腫瘤大於4-5公分或具分泌功能者均需手術切除；無功能但體積大者因有惡性風險，仍須切除。",
      "flashcard_summary": "腎上腺腫瘤手術指徵 -> 具分泌功能或體積大於4-5公分者皆須手術，非無功能即可不切除。"
    },
    {
      "question_id": "109-1_medicine-5_066",
      "question_number": 66,
      "correct_answer": "D",
      "category_group": "醫學（五）",
      "category": "泌尿科",
      "category_confidence": "high",
      "key_point": "睪丸癌的病理分類、腫瘤標記與治療原則。",
      "explanation": "早期（Stage I）的睪丸精原細胞瘤（seminoma）在接受根治性睪丸切除術後，其主要治療與追蹤策略是進行密切追蹤（surveillance）或局部放射線治療，而非以化學治療為主，化療主要用於晚期或復發的患者，故D錯誤。睪丸惡性腫瘤中95%以上為生殖細胞瘤（germ cell tumor）；老年人最常見的續發性睪丸癌是淋巴瘤；而單純的精原細胞瘤患者其血清AFP絕對不會升高。",
      "flashcard_front": "睪丸癌 / 早期Seminoma / 治療首選 / AFP標記",
      "flashcard_back": "早期精原細胞瘤（seminoma）術後以追蹤或放療為主，非首選化療；pure seminoma之AFP絕對不會上升。",
      "flashcard_summary": "睪丸精原細胞瘤治療 -> 早期術後採追蹤或放療為主；pure seminoma之AFP不升高。"
    },
    {
      "question_id": "109-1_medicine-5_067",
      "question_number": 67,
      "correct_answer": "A",
      "category_group": "醫學（五）",
      "category": "泌尿科",
      "category_confidence": "high",
      "key_point": "遠處轉移至膀胱之原發癌症來源。",
      "explanation": "雖然膀胱繼發性（轉移性）腫瘤臨床上並不常見，但在發生遠處轉移至膀胱的非鄰近器官癌症中，惡性黑色素瘤（melanoma）是最常見的原發癌症來源，故A為正確答案。乳癌、胃癌和肺癌也可能發生膀胱轉移，但發生率相對較低（鄰近器官的直接侵犯如前列腺癌、子宮頸癌、大腸直腸癌則屬於局部浸潤，非遠處轉移）。",
      "flashcard_front": "膀胱轉移癌 / 遠處轉移 / 黑色素瘤 / 原發來源",
      "flashcard_back": "遠處轉移至膀胱的非鄰近器官癌症中，以惡性黑色素瘤（melanoma）為最常見的原發腫瘤。",
      "flashcard_summary": "膀胱轉移癌來源 -> 遠處轉移至膀胱之癌症中，最常見原發灶為惡性黑色素瘤。"
    },
    {
      "question_id": "109-1_medicine-5_068",
      "question_number": 68,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "泌尿科",
      "category_confidence": "high",
      "key_point": "神經性膀胱的病變定位。",
      "explanation": "弛緩型神經性膀胱（flaccid neuropathic bladder，下運動神經元受損）是由於薦椎排尿中樞（S2-S4）或其周邊傳出神經受損，導致逼尿肌失去張力。頸椎受傷（高於T12，屬於上運動神經元受損）會保留薦椎反射弧，導致痙攣型神經性膀胱及逼尿肌-外尿道括約肌失調（DSD），因此不會造成弛緩型膀胱，故選B。S2-S4脊髓損傷、脊髓發育不良及小兒麻痺病毒破壞脊髓前角細胞，皆會破壞反射弧的下運動神經元，導致弛緩型膀胱。",
      "flashcard_front": "弛緩型膀胱 / flaccid bladder / 頸椎受傷 / 薦椎排尿中樞",
      "flashcard_back": "薦椎排尿中樞（S2-S4）或其下神經元受損導致弛緩型膀胱；頸椎等高位脊髓受傷（上運動神經元損害）則引起痙攣型膀胱。",
      "flashcard_summary": "弛緩與痙攣型膀胱定位 -> 薦椎（S2-S4）以下受損致弛緩型膀胱，高位脊髓（如頸椎）受損致痙攣型膀胱。"
    },
    {
      "question_id": "109-1_medicine-5_069",
      "question_number": 69,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "泌尿科",
      "category_confidence": "high",
      "key_point": "間質性膀胱炎的臨床表現與尿液常規特徵。",
      "explanation": "間質性膀胱炎是一種非感染性的慢性膀胱發炎疾病。典型的尿液常規檢查通常是完全正常的（即無明顯血尿與膿尿），臨床診斷前必須先排除泌尿道感染或膀胱癌，因此B選項敘述錯誤。此病好發於40歲以上女性，典型症狀為頻尿、急尿及脹尿時的恥骨上疼痛（排尿後可緩解），因長期憋尿疼痛導致膀胱容積縮小。",
      "flashcard_front": "間質性膀胱炎 / 尿常規 / 脹尿痛 / 診斷排查",
      "flashcard_back": "間質性膀胱炎之尿常規檢查通常為陰性（無感染及膿尿）；典型表現為脹尿時恥骨上疼痛，排尿後緩解。",
      "flashcard_summary": "間質性膀胱炎特徵 -> 尿常規檢查通常正常，特徵為脹尿時恥骨上疼痛。"
    },
    {
      "question_id": "109-1_medicine-5_070",
      "question_number": 70,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "泌尿科",
      "category_confidence": "high",
      "key_point": "兒童反覆性尿路感染（UTI）的誘因與處置。",
      "explanation": "在反覆性尿路感染（UTI）的兒童中，憋尿、少喝水以及慢性便秘（會壓迫膀胱頸並影響排空）是極為常見的行為與生理誘因，故B選項正確。反覆尿路感染的女孩多數解剖結構是正常的（A錯誤）；無發燒的尿路感染仍需適當使用抗生素治療以防止逆行性感染（C錯誤）；膀胱輸尿管逆流（VUR）是引起反覆性腎盂腎炎和尿路感染的重要原因（D錯誤）。",
      "flashcard_front": "兒童反覆UTI / 行為誘因 / 便秘 / 膀胱輸尿管逆流 (VUR)",
      "flashcard_back": "兒童反覆尿路感染與憋尿、少喝水及便秘密切相關；VUR是常見原因，且不論有無發燒之UTI皆需治療。",
      "flashcard_summary": "兒童反覆UTI誘因 -> 常伴有憋尿、少喝水及便秘；VUR是重要病因，感染皆需治療。"
    },
    {
      "question_id": "109-1_medicine-5_071",
      "question_number": 71,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "泌尿科",
      "category_confidence": "high",
      "key_point": "前列腺癌根除術後勃起功能障礙的神經解剖因素。",
      "explanation": "海綿體神經（Cavernous nerve）為源自骨盆腔神經叢的副交感神經纖維，緊貼於前列腺的外後側走行，負責支配陰莖海綿體的血管舒張以啟動勃起。在前列腺根除手術中，若未能精準保留此神經（非神經保留術式），受損後會導致患者術後發生嚴重的勃起功能障礙（陽痿），故選B。",
      "flashcard_front": "前列腺根除術 / 術後陽痿 / 海綿體神經 / 副交感",
      "flashcard_back": "海綿體神經（副交感神經支）負責控制陰莖勃起，緊貼前列腺走形，根除手術中受損會導致術後無法勃起。",
      "flashcard_summary": "前列腺術後勃起障礙 -> 手術中損傷海綿體神經（副交感）所致。"
    },
    {
      "question_id": "109-1_medicine-5_072",
      "question_number": 72,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "骨科",
      "category_confidence": "high",
      "key_point": "薦椎不足骨折的臨床背景與骨掃描特徵。",
      "explanation": "此病患為接受過子宮/卵巢切除（失去雌激素保護）且經歷骨盆腔放射線治療的女性，這些都是導致骨質流失與骨骼脆弱的危險因子。在核醫骨骼掃描中呈現經典的薦椎「H型」或蝶形吸附增加（Honda sign），這是薦椎不足骨折（sacral insufficiency fracture）的特徵性影像表現，而非骨轉移或腫瘤復發，故選B。",
      "flashcard_front": "骨盆腔放療 / 術後下背痛 / H型骨吸附 (Honda sign) / 不足骨折",
      "flashcard_back": "骨盆腔放療及停經女性易發生薦椎不足骨折（insufficiency fracture），骨掃描呈現特徵性的H型吸附。",
      "flashcard_summary": "薦椎不足骨折 -> 骨盆腔放療後下背痛，骨掃描呈特徵性H型吸附（Honda sign）。"
    },
    {
      "question_id": "109-1_medicine-5_073",
      "question_number": 73,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "泌尿科",
      "category_confidence": "high",
      "key_point": "急性腎絞痛之電腦斷層診斷。",
      "explanation": "在未注射對比劑（non-contrast）的腹部電腦斷層中，可以清楚觀察到高密度的結石顯影（通常位於輸尿管或腎臟內），且病患臨床表現為陣發性腹痛（典型腎絞痛）且生命徵象穩定，此時最恰當的診斷為腎結石，故選C。無對比劑CT是診斷急性尿路結石的首選且最具敏感性與特異性的檢查。",
      "flashcard_front": "陣發腹痛 / 未施打對比劑CT / 高密度顯影 / 腎結石",
      "flashcard_back": "診斷急性尿路/腎結石首選無對比劑電腦斷層（NCCT），可見輸尿管或腎臟內的高密度結石影。",
      "flashcard_summary": "腎結石CT診斷 -> 陣發腹痛患者接受無對比劑CT檢查，可見高密度影，診斷為腎/尿路結石。"
    },
    {
      "question_id": "109-1_medicine-5_074",
      "question_number": 74,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "骨科",
      "category_confidence": "high",
      "key_point": "兒童與青少年骨肉瘤的臨床表現與好發部位。",
      "explanation": "13歲青少年好發於膝關節附近，出現夜間疼痛明顯（夜間痛是惡性骨腫瘤的警訊特徵），且X光呈現骨皮質破壞與骨生成性病變，最典型的診斷為骨肉瘤（osteosarcoma），故選C。骨肉瘤是兒童與青少年最常見的原發性惡性骨腫瘤，X光常可見骨膜反應如Codman三角或日光放射狀（sunburst）外觀。",
      "flashcard_front": "13歲青少年 / 膝關節痛 / 夜間痛明顯 / 骨肉瘤 (osteosarcoma)",
      "flashcard_back": "青少年膝關節附近夜間隱痛，X光呈溶骨/成骨骨質破壞與骨膜反應，應高度懷疑骨肉瘤。",
      "flashcard_summary": "骨肉瘤特徵 -> 青少年好發於膝關節，有夜間痛，X光呈溶骨性與成骨性骨質破壞。"
    },
    {
      "question_id": "109-1_medicine-5_075",
      "question_number": 75,
      "correct_answer": "D",
      "category_group": "醫學（五）",
      "category": "一般外科",
      "category_confidence": "high",
      "key_point": "消化道出血的解剖定義與臨床特性。",
      "explanation": "解剖學上，下消化道（LGI）出血是指Treitz韌帶遠端的消化道出血，其中包括空腸、迴腸、結腸及直腸，因此下消化道出血確實可能來自空腸，D選項說法最適當。上消化道出血通常比下消化道出血更具急性生命危險（A錯誤）；高齡是上消化道出血及預後不良的重要危險因子（B錯誤）；臨床上約有80%的急性消化道出血會自行停止流血（C錯誤）。",
      "flashcard_front": "消化道出血 / Treitz韌帶 / 空腸 / 自行止血",
      "flashcard_back": "下消化道出血定義為Treitz韌帶遠端（含空腸、迴腸及大腸）出血；大多數（約80%）急性消化道出血可自行停止。",
      "flashcard_summary": "消化道出血特徵 -> Treitz韌帶遠端（含空腸）為下消化道，多數急性出血可自行停止。"
    }
  ]
}

# ----------------------------------------------------
# 109-1_medicine-5_batch-006 (Q76-Q80)
# ----------------------------------------------------
batches_data["109-1_medicine-5_batch-006"] = {
  "dataset_id": "109-1_medicine-5",
  "batch_id": "109-1_medicine-5_batch-006",
  "items": [
    {
      "question_id": "109-1_medicine-5_076",
      "question_number": 76,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "外科概論",
      "category_confidence": "high",
      "key_point": "腹部外傷（鈍傷與穿透傷）最易受損器官的流行病學。",
      "explanation": "腹部外傷中，受傷器官隨受傷機轉而異。鈍性腹部創傷（如車禍撞擊）最常受損的實質器官是脾臟，其次是肝臟；而穿透性槍擊傷由於子彈在腹腔內的路徑長且小腸佔據腹腔最大空間，最常受損的器官是小腸，其次是結腸和肝臟。因此，鈍傷時為脾臟，槍擊傷時是小腸，選C。",
      "flashcard_front": "腹部外傷 / 最常受傷器官 / 鈍傷 / 槍擊傷",
      "flashcard_back": "腹部外傷中，鈍傷最易損害脾臟；穿透性槍擊傷則最易造成小腸損傷。",
      "flashcard_summary": "腹部外傷器官損害 -> 鈍傷最常傷及脾臟，槍擊傷最常傷及小腸。"
    },
    {
      "question_id": "109-1_medicine-5_077",
      "question_number": 77,
      "correct_answer": "D",
      "category_group": "醫學（五）",
      "category": "外科概論",
      "category_confidence": "high",
      "key_point": "腹部外傷評估工具的特異性比較。",
      "explanation": "對於血流動力學穩定的腹部鈍傷患者，腹部電腦斷層掃描（CT scan）是定位與評估實質器官損傷（如脾、肝撕裂傷及後腹腔出血）最具特異性與敏感性的影像檢查，故選D。腹部超音波（FAST）主要優點是快速、非侵入性，但對實質器官損傷特異性較低；診斷性腹腔灌洗術（DPL）極具敏感度但特異性差（無法區分非致命的微量出血），且現已多被FAST與CT取代。",
      "flashcard_front": "腹部鈍傷 / 電腦斷層 (CT) / 超音波 (FAST) / 特異性首選",
      "flashcard_back": "電腦斷層（CT）對腹部鈍傷之實質器官診斷具最高的特異性與敏感性；FAST則用於快速篩檢有無腹腔積液。",
      "flashcard_summary": "腹部鈍傷評估 -> 電腦斷層（CT）具最高特異性，超音波（FAST）用於快速篩檢積液。"
    },
    {
      "question_id": "109-1_medicine-5_078",
      "question_number": 78,
      "correct_answer": "B",
      "category_group": "醫學（五）",
      "category": "其他",
      "category_confidence": "high",
      "key_point": "醫學倫理中利益衝突、回扣與醫療浪費之分析。",
      "explanation": "在此案例中，廠商私下提供回扣給醫師，醫師因金錢利益而過度使用該耗材，這顯然存在嚴重的利益衝突；且這種行為會導致不必要的耗材使用，造成醫療資源的浪費；一旦被揭發，將嚴重損及患者對醫師的信賴。在此事件中，並未涉及患者個人健康資訊的洩露，因此非本案涉及的倫理議題為「違反病人隱私」，故選B。",
      "flashcard_front": "醫師收受回扣 / 利益衝突 / 資源浪費 / 病人隱私",
      "flashcard_back": "醫師收受耗材回扣涉及利益衝突、破壞醫病信賴與浪費醫療資源；但與病人隱私權無關。",
      "flashcard_summary": "回扣與倫理議題 -> 涉及利益衝突、誠信與資源浪費，不涉及病人隱私。"
    },
    {
      "question_id": "109-1_medicine-5_079",
      "question_number": 79,
      "correct_answer": "C",
      "category_group": "醫學（五）",
      "category": "其他",
      "category_confidence": "high",
      "key_point": "患者拒絕維持生命治療的倫理處置。",
      "explanation": "根據病人自主權與知情同意原則，一個具備決定能力的成年患者，在充分了解後果的前提下，有權拒絕維持生命治療（如全靜脈營養）。醫護人員不應違背患者意願、強行進行違反病人意願的侵入性強迫治療，故C（不論如何繼續治療）是最不適當的作法。此時最適當的作法是先照會精神科評估患者是否受重度憂鬱影響心智能力，並討論其他緩和醫療選項，若確認心智健全則應尊重其自主權。",
      "flashcard_front": "拒絕維持生命治療 / 自主權 / 強制治療 / 精神評估",
      "flashcard_back": "心智健全的成年患者有權拒絕維持生命治療；醫師強行實施違反意願的治療為不當處置，應先進行精神評估並尊重自主權。",
      "flashcard_summary": "拒過度醫療治療 -> 尊重健全心智患者的拒絕權，不可違背意願強行治療，應先進行精神評估。"
    },
    {
      "question_id": "109-1_medicine-5_080",
      "question_number": 80,
      "correct_answer": "A",
      "category_group": "醫學（五）",
      "category": "其他",
      "category_confidence": "high",
      "key_point": "面對病人要求不合理醫療處置時的溝通與自主權界限。",
      "explanation": "在臨床決策中，醫師應遵循行善與不傷害原則，拒絕提供醫療上無益或非適應症的醫療處置。即使病人主動要求，若專業評估認為不需要，亦不可迎合病人而給予（更不能以健保虛報，故B、C錯誤）；但醫師仍需履行說明與溝通的義務，向病人說明不需使用的原因，而非強行決定、拒絕溝通，因此最適當處理為A。",
      "flashcard_front": "病人要求無益醫療 / 白蛋白 / 拒絕無益處置 / 耐心溝通",
      "flashcard_back": "對於病人要求且無臨床指徵的處置，醫師應秉持專業婉拒，並向病人耐性說明原因，不可盲從要求或拒絕溝通。",
      "flashcard_summary": "處理無益醫療要求 -> 依專業判斷婉拒病人不合理要求，但必須進行充分說明與溝通。"
    }
  ]
}

# Write medicine-5 batches
for b_id in ["109-1_medicine-5_batch-003", "109-1_medicine-5_batch-004", "109-1_medicine-5_batch-005", "109-1_medicine-5_batch-006"]:
    o_path = f"reports/gemini_outputs/{b_id}.json"
    with open(o_path, "w", encoding="utf-8") as f:
        json.dump(batches_data[b_id], f, ensure_ascii=False, indent=2)
    print(f"Wrote {o_path}")
