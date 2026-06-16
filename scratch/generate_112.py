# -*- coding: utf-8 -*-
import json
import os
import sys

# Define batch 1
batch_1 = {
  "dataset_id": "112-2_medicine-4",
  "batch_id": "112-2_medicine-4_batch-001",
  "items": [
    {
      "question_id": "112-2_medicine-4_001",
      "question_number": 1,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握嬰兒玫瑰疹的致病原與臨床特徵。",
      "explanation": "嬰兒玫瑰疹的主要致病原是人類疱疹病毒第六型B（HHV-6B），高峰期為6至9個月大嬰兒。皮疹多從軀幹擴散至面部與四肢，通常持續1至3天或數小時內消退。原發性HHV-6B感染的兒童中，僅約10%至15%發燒會持續6天或以上，因此「50%持續6天或更長」的敘述並不恰當。",
      "flashcard_front": "嬰兒玫瑰疹 / 致病原 / 好發年齡 / 發燒天數 / 皮疹分布",
      "flashcard_back": "主要致病原為 HHV-6B，高峰期在6-9個月大，發燒持續6天以上者僅佔少數（約10-15%），皮疹自軀幹蔓延至面部及四肢。",
      "flashcard_summary": "嬰兒玫瑰疹臨床特徵 -> 主要致病原為 HHV-6B，高峰期在6-9個月大，發燒持續6天以上者僅佔少數（約10-15%），皮疹自軀幹蔓延至面部及四肢。"
    },
    {
      "question_id": "112-2_medicine-4_002",
      "question_number": 2,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握嬰幼兒生長曲線的判讀與轉介指引。",
      "explanation": "嬰幼兒的體重落在第15百分位屬於正常範圍，不需要立即轉介，且表示在100名同齡男嬰中其體重大約從最輕排起是第15位（排在前第85位）。若一個月大時體重6公斤，至六個月大時僅7公斤，生長曲線走勢在短期內掉了兩個主要曲線區間，表示有生長遲緩或成長不良的疑慮，應立即轉介評估。",
      "flashcard_front": "6個月大男嬰 / 體重百分位 / 生長曲線掉兩個區間 / 轉介指引 / 成長評估",
      "flashcard_back": "生長曲線指標介於第3至97百分位皆屬正常，但若生長軌跡在短時間內下降達兩個主要曲線區間，則須立即轉介評估。",
      "flashcard_summary": "生長曲線判讀與轉介 -> 生長曲線指標介於第3至97百分位皆屬正常，但若生長軌跡在短時間內下降達兩個主要曲線區間，則須立即轉介評估。"
    },
    {
      "question_id": "112-2_medicine-4_003",
      "question_number": 3,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握先天性橫膈膜疝氣的臨床表徵。",
      "explanation": "先天性橫膈膜疝氣（CDH）是由於橫膈膜缺損導致腹腔臟器疝入胸腔，壓迫肺部造成新生兒出生後立即發生呼吸窘迫與發紺。其典型身體檢查特徵包括腹部扁平（因腹腔器官移位）以及縱膈腔移位導致最強心尖搏動點移至右胸。食道閉鎖、後鼻孔閉鎖或胃扭轉不會同時出現腹部扁平及心尖搏動點右移的臨床表現。",
      "flashcard_front": "新生兒呼吸窘迫 / 腹部扁平 / 最強心尖搏動點在右胸 / 先天性橫膈膜疝氣",
      "flashcard_back": "出生後立即發紺、腹部呈扁平狀且心尖搏動點右移，是先天性橫膈膜疝氣（CDH）壓迫縱膈腔移位的典型表現。",
      "flashcard_summary": "先天性橫膈膜疝氣表徵 -> 出生後立即發紺、腹部呈扁平狀且心尖搏動點右移，是先天性橫膈膜疝氣（CDH）壓迫縱膈腔移位的典型表現。"
    },
    {
      "question_id": "112-2_medicine-4_004",
      "question_number": 4,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握新生兒呼吸窘迫症候群的病因與臨床特徵。",
      "explanation": "呼吸窘迫症候群（RDS）主要起因於肺泡表面張力素缺乏，導致肺泡塌陷。其呼吸窘迫症狀通常隨時間逐漸加重，並在出生後24至72小時內達到高峰，若無積極治療（如給予表面張力素）通常無法在短期內自行恢復；這與新生兒暫時性呼吸過速（TTN）在出生後立即最嚴重並在24至72小時內消退的特徵不同。X光上典型呈現低肺容積、瀰漫性網狀細顆粒陰影及支氣管充氣徵。",
      "flashcard_front": "新生兒呼吸窘迫症候群 (RDS) / 症狀高峰時間 / 肺泡表面張力素 / X光特徵 / TTN鑑別",
      "flashcard_back": "RDS 症狀通常在出生後 24-72 小時內達高峰且需積極治療，而非剛出生最嚴重且在 72 小時內自癒（此為 TTN 特徵）。",
      "flashcard_summary": "RDS與TTN臨床鑑別 -> RDS 症狀通常在出生後 24-72 小時內達高峰且需積極治療，而非剛出生最嚴重且在 72 小時內自癒（此為 TTN 特徵）。"
    },
    {
      "question_id": "112-2_medicine-4_005",
      "question_number": 5,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握新生兒壞死性腸炎的風險因子。",
      "explanation": "壞死性腸炎（NEC）主要發生於早產兒，且妊娠週數越低風險越高。哺餵母乳相較於哺餵配方乳，能夠顯著降低新生兒發生壞死性腸炎的機會，因此「母乳哺餵較容易發生NEC」的說法錯誤。足月兒發生NEC通常有次發性誘因，如先天性心臟病引起的腸道灌流不足，且腸道菌叢失衡也被證實與其發生密切相關。",
      "flashcard_front": "壞死性腸炎 (NEC) / 哺餵方式 / 早產兒週數 / 腸道菌叢 / 足月兒前置因子",
      "flashcard_back": "母乳對 NEC 具有保護作用，配方奶餵食者發生風險較高；妊娠週數越低或有先天性心臟病等足月兒風險亦高。",
      "flashcard_summary": "壞死性腸炎風險因子 -> 母乳對 NEC 具有保護作用，配方奶餵食者發生風險較高；妊娠週數越低或有先天性心臟病等足月兒風險亦高。"
    },
    {
      "question_id": "112-2_medicine-4_006",
      "question_number": 6,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "區分功能性心雜音與病理性心雜音的特徵。",
      "explanation": "功能性（無害性）心雜音通常是中等音高的收縮期雜音，其音量會隨著呼吸或姿勢改變而有明顯起伏，例如輕壓頸靜脈可使靜脈哼聲（venous hum）變小聲。然而，全收縮期雜音（pansystolic murmur）或強度達第三級（Grade 3）以上的雜音，在臨床上幾乎均暗示為病理性心臟異常（如心室中隔缺損或二尖瓣逆流），不屬於功能性心雜音。",
      "flashcard_front": "功能性心雜音 (innocent murmur) / 全收縮期雜音 / 雜音分級 / 姿勢與呼吸影響 / 頸靜脈壓迫",
      "flashcard_back": "功能性心雜音多為 Grade 1-2 的中音頻收縮期雜音，會隨姿勢或呼吸改變；全收縮期或 Grade 3 雜音多為病理性。",
      "flashcard_summary": "功能性與病理性心雜音 -> 功能性心雜音多為 Grade 1-2 的中音頻收縮期雜音，會隨姿勢或呼吸改變；全收縮期或 Grade 3 雜音多為病理性。"
    },
    {
      "question_id": "112-2_medicine-4_007",
      "question_number": 7,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握川崎氏症的診斷要件與特徵。",
      "explanation": "此男嬰具備川崎氏症（Kawasaki disease）的典型臨床表現，包括發燒持續5天以上，以及卡介苗接種處紅腫（台灣兒童特有的高特異性特徵）、草莓舌、非化膿性雙側結膜炎（無分泌物）與多形性皮膚紅疹。這些特徵與咽結膜熱、敗血症或風濕熱等疾病的典型表現不符，因此最可能的診斷為川崎氏症。",
      "flashcard_front": "男嬰持續高燒5天 / 卡介苗紅腫 / 草莓舌 / 無分泌物結膜炎 / 川崎氏症",
      "flashcard_back": "發燒5天以上伴隨卡介苗接種處紅腫、草莓舌及無眼屎的結膜充血，高度暗示川崎氏症（Kawasaki disease）。",
      "flashcard_summary": "川崎氏症典型症狀 -> 發燒5天以上伴隨卡介苗接種處紅腫、草莓舌及無眼屎的結膜充血，高度暗示川崎氏症（Kawasaki disease）。"
    },
    {
      "question_id": "112-2_medicine-4_008",
      "question_number": 8,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握新生兒發紺型心臟病與非發紺型心臟病的鑑別診斷。",
      "explanation": "在出生僅一週的新生兒中，由於肺血管阻力（PVR）仍相對較高，左向右分流的非發紺型心臟病如心室中隔缺損（VSD），通常此時分流量不大，不會在此階段引起明顯的全身發紺或顯著的肺部充血。相對地，全肺靜脈回流異常、三尖瓣閉鎖或動脈幹異常等發紺型先天性心臟病，在出生早期即容易呈現嚴重的發紺與肺充血。",
      "flashcard_front": "1週大新生兒 / 發紺與肺部充血 / 心室中隔缺損 / 全肺靜脈回流異常 / 發紺型心臟病",
      "flashcard_back": "新生兒早期（一週內）發紺伴肺部充血，應先考慮發紺型心臟病；非發紺型的 VSD 在此時因肺阻力仍高，不易表現此症狀。",
      "flashcard_summary": "新生兒發紺心臟病鑑別 -> 新生兒早期（一週內）發紺伴肺部充血，應先考慮發紺型心臟病；非發紺型的 VSD 在此時因肺阻力仍高，不易表現此症狀。"
    },
    {
      "question_id": "112-2_medicine-4_009",
      "question_number": 9,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握嬰兒膽道閉鎖的診斷與治療要點。",
      "explanation": "膽道閉鎖（biliary atresia）的肝切片組織病理特徵為小膽管增生、門脈區纖維化及膽栓形成，若顯示「廣泛發炎細胞浸潤、肝細胞壞死、肝內膽管無明顯異常」，則較符合新生兒肝炎的特點，無法確診膽道閉鎖。診斷黃金標準為剖腹探查及膽道攝影，治療應於出生後8週內進行葛西氏手術（Kasai procedure），以獲得較佳預後。",
      "flashcard_front": "嬰兒持續黃疸 / 灰白便 / 膽道閉鎖 (BA) / 肝切片病理 / 葛西氏手術時機",
      "flashcard_back": "膽道閉鎖切片典型呈現小膽管增生與膽栓，而非肝內膽管無異常；確診需靠膽道攝影，手術黃金期為8週內。",
      "flashcard_summary": "膽道閉鎖病理與治療 -> 膽道閉鎖切片典型呈現小膽管增生與膽栓，而非肝內膽管無異常；確診需靠膽道攝影，手術黃金期為8週內。"
    },
    {
      "question_id": "112-2_medicine-4_010",
      "question_number": 10,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握四環黴素類藥物引起的藥物性食道炎特徵。",
      "explanation": "15歲男孩服用治療青春痘的藥物 doxycycline（四環黴素類）後，若睡前服藥且配水量不足，易使藥錠卡在食道中段釋放酸性物質，導致藥物引發的食道炎（pill-induced esophagitis）。其內視鏡表現通常是局限性、邊界清晰的食道潰瘍，而非廣泛性的食道潰瘍。治療以支持性療法為主，包含流質飲食與抑酸劑。",
      "flashcard_front": "青春痘治療 / doxycycline / 吞嚥疼痛 / 藥物性食道炎 / 內視鏡潰瘍表現",
      "flashcard_back": "青春痘用藥 doxycycline 易因飲水不足卡在食道引起潰瘍，內視鏡呈局限性深潰瘍而非廣泛性食道炎。",
      "flashcard_summary": "Doxycycline食道炎特徵 -> 青春痘用藥 doxycycline 易因飲水不足卡在食道引起潰瘍，內視鏡呈局限性深潰瘍而非廣泛性食道炎。"
    },
    {
      "question_id": "112-2_medicine-4_011",
      "question_number": 11,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握兒童無痛性血便最常見原因及檢查。",
      "explanation": "1歲半男童在無發燒、腹痛或皮膚疹的情況下解大量無痛性褐紅色血便，最常見的診斷是梅克爾憩室（Meckel's diverticulum）。梅克爾憩室內常含有異位性胃黏膜，會分泌胃酸導致鄰近迴腸黏膜潰瘍出血。確診敏感性最高的檢查是注射西咪替丁（cimetidine）增強的梅克爾核醫閃爍攝影（Meckel scan），而非血管攝影或內視鏡。",
      "flashcard_front": "幼童 / 無痛性大量血便 / 梅克爾憩室 / 異位胃黏膜 / 梅克爾核醫掃描 (Meckel scan)",
      "flashcard_back": "幼童突發無痛性大量血便，應優先懷疑梅克爾憩室；以 Tc-99m 配合 cimetidine 增強的核醫掃描敏感性最高。",
      "flashcard_summary": "梅克爾憩室診斷 -> 幼童突發無痛性大量血便，應優先懷疑梅克爾憩室；以 Tc-99m 配合 cimetidine 增強的核醫掃描敏感性最高。"
    },
    {
      "question_id": "112-2_medicine-4_012",
      "question_number": 12,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "理解腎病症候群患者易受感染的免疫機轉。",
      "explanation": "腎病症候群患者易受感染，主要是因為尿液中流失大量的免疫球蛋白（造成低免疫球蛋白血症）、補體 C3 與 C5，以及替代途徑中的 factor B 與 factor D，導致調理作用障礙。然而，腎病症候群患者的白血球數量通常是正常甚至偏高的，並不會出現低白血球症（leukopenia），因此低白血球症並非其易受感染的原因。",
      "flashcard_front": "腎病症候群 (NS) / 易感染原因 / 尿液流失補體 / 低白血球症 / 替代途徑因子",
      "flashcard_back": "腎病症候群易感染是因尿中流失 IgG、補體及替代途徑因子，其白血球數量正常或增加，無低白血球症。",
      "flashcard_summary": "腎病症候群易感因 -> 腎病症候群易感染是因尿中流失 IgG、補體及替代途徑因子，其白血球數量正常或增加，無低白血球症。"
    },
    {
      "question_id": "112-2_medicine-4_013",
      "question_number": 13,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握小兒夜間遺尿症的評估與治療原則。",
      "explanation": "小兒夜間遺尿症的評估需先排除尿崩症、糖尿病及慢性腎臟病等次發性病因，並可測量禁食尿液滲透壓。治療上，第一線治療應為非藥物性的行為治療（如尿濕警報器、睡前限水），藥物治療（如 desmopressin）雖然短期效果佳，但停藥後復發率極高，因此不應列為首選的一線治療。",
      "flashcard_front": "小兒夜間遺尿症 / 排除次發性病因 / 尿液滲透壓 / 行為治療 / 藥物治療地位",
      "flashcard_back": "小兒夜間遺尿症應先排除內分泌及腎臟疾病；第一線治療為行為治療（如尿濕警報器），而非復發率高的藥物。",
      "flashcard_summary": "夜間遺尿症治療原則 -> 小兒夜間遺尿症應先排除內分泌及腎臟疾病；第一線治療為行為治療（如尿濕警報器），而非復發率高的藥物。"
    },
    {
      "question_id": "112-2_medicine-4_014",
      "question_number": 14,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握兒童紅斑性狼瘡腎炎的分級與治療原則。",
      "explanation": "兒童紅斑性狼瘡（SLE）常合併腎炎，第四級（class IV）為瀰漫增生性腎炎，常伴隨血尿、蛋白尿與急性腎損傷。然而，類固醇脈衝治療與強效免疫抑制劑僅適用於較嚴重的增生性腎炎（如 class III 或 IV），輕微的病變（如 class I 或 II）通常不需要使用此類強效療法。ACEI/ARB 則可有效控制血壓並減少蛋白尿。",
      "flashcard_front": "兒童紅斑性狼瘡腎炎 / Class IV 病理表現 / 類固醇脈衝與免疫抑制劑 / 輕微與嚴重分級治療",
      "flashcard_back": "狼瘡腎炎 Class IV 常有嚴重血尿及腎功能受損；強效免疫抑制與類固醇脈衝不適用於所有級別（輕微者免用）。",
      "flashcard_summary": "狼瘡腎炎治療分級 -> 狼瘡腎炎 Class IV 常有嚴重血尿及腎功能受損；強效免疫抑制與類固醇脈衝不適用於所有級別（輕微者免用）。"
    },
    {
      "question_id": "112-2_medicine-4_015",
      "question_number": 15,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握不同年齡層兒童異位性皮膚炎的好發部位。",
      "explanation": "異位性皮膚炎的好發部位隨年齡而異：嬰幼兒期主要侵犯臉部、頭皮及四肢伸側；青少年及成人期則轉變為侵犯四肢的屈側（如肘窩、膝窩）。值得注意的是，嬰幼兒的「包尿布區域」因為有尿液與尿布的局部濕氣保護，通常不會受到異位性皮膚炎的侵犯，這也是與尿布疹鑑別的重要依據。",
      "flashcard_front": "兒童異位性皮膚炎 / 嬰幼兒好發部位 / 四肢伸側與屈側 / 包尿布區域排除 / 尿布疹鑑別",
      "flashcard_back": "嬰幼兒異位性皮膚炎好發於臉部與伸側，而包尿布區域因局部濕氣保護，極少被侵犯（常用於鑑別診斷）。",
      "flashcard_summary": "異位性皮膚炎好發部位 -> 嬰幼兒異位性皮膚炎好發於臉部與伸側，而包尿布區域因局部濕氣保護，極少被侵犯（常用於鑑別診斷）。"
    }
  ]
}

# Define batch 2
batch_2 = {
  "dataset_id": "112-2_medicine-4",
  "batch_id": "112-2_medicine-4_batch-002",
  "items": [
    {
      "question_id": "112-2_medicine-4_016",
      "question_number": 16,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握過敏反應中 Th2 細胞與先天淋巴細胞（ILCs）的活化機制。",
      "explanation": "Th2 細胞分泌 IL-4、IL-5 與 IL-13，在 IgE 相關過敏性疾病中扮演核心角色。先天淋巴細胞（ILC）可分為 ILC1s、ILC2s 及 ILC3s，其中會被上皮細胞激素（IL-33、IL-25 與 TSLP）活化並分泌 IL-5、IL-13 投發過敏反應的是 ILC2s（第二型先天淋巴細胞），而非負責黏膜免疫防禦的 ILC3s。",
      "flashcard_front": "過敏反應機轉 / Th2 細胞激素 / 先天淋巴細胞 (ILCs) / IL-33、IL-25活化 / ILC2s與ILC3s",
      "flashcard_back": "被上皮細胞激素（IL-33, IL-25, TSLP）活化並誘發過敏反應的是 ILC2s，而非 ILC3s（主要產生 IL-17/22）。",
      "flashcard_summary": "先天淋巴細胞與過敏 -> 被上皮細胞激素（IL-33, IL-25, TSLP）活化並誘發過敏反應的是 ILC2s，而非 ILC3s（主要產生 IL-17/22）。"
    },
    {
      "question_id": "112-2_medicine-4_017",
      "question_number": 17,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "掌握蕁麻疹的定義與臨床分類標準。",
      "explanation": "蕁麻疹的特徵為突發性且隆起於皮膚的風疹塊（wheal），主要由 IgE 媒介所導致。在臨床定義上，蕁麻疹病灶反覆發作且持續時間必須「達到 6 星期以上」才被分類為慢性蕁麻疹（chronic urticaria），而非 4 星期。當慢性蕁麻疹侵犯至較深處的皮膚及黏膜組織時，則會造成腫脹並稱為血管性水腫（angioedema）。",
      "flashcard_front": "蕁麻疹 (urticaria) / 風疹塊與血管性水腫 / 急性與慢性定義 / 持續時間門檻",
      "flashcard_back": "蕁麻疹發作持續時間以「6 星期」為界，超過者定義為慢性蕁麻疹；4 星期仍屬於急性期。",
      "flashcard_summary": "慢性蕁麻疹定義時間 -> 蕁麻疹發作持續時間以「6 星期」為界，超過者定義為慢性蕁麻疹；4 星期仍屬於急性期。"
    },
    {
      "question_id": "112-2_medicine-4_018",
      "question_number": 18,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握兒童特發性血小板減少性紫斑症的臨床特徵與治療原則。",
      "explanation": "兒童特發性血小板減少性紫斑症（ITP）常發生於病毒感染後1至4週，好發於2至5歲幼童。由於此病為單純血小板破壞增加，通常不會合併嚴重貧血（除非有大量出血），且治療上以觀察、IVIG 或類固醇為主，不應以輸血小板為主要手段（因抗體會迅速破壞輸入的血小板，僅在致命性出血時使用）。",
      "flashcard_front": "兒童 ITP / 病毒感染後 / 好發年齡 / 貧血關聯 / 輸血小板時機",
      "flashcard_back": "兒童 ITP 常在病毒感染後 1-4 週發病，以血小板單獨低下為主，一線治療非輸血小板（因抗體會快速破壞）。",
      "flashcard_summary": "兒童ITP特徵與治療 -> 兒童 ITP 常在病毒感染後 1-4 週發病，以血小板單獨低下為主，一線治療非輸血小板（因抗體會快速破壞）。"
    },
    {
      "question_id": "112-2_medicine-4_019",
      "question_number": 19,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握兒童癌症的流行病學與主要治療方式。",
      "explanation": "白血病是兒童最常見的惡性腫瘤，實體腫瘤診斷高度依賴影像與組織學判讀，且特定遺傳疾病如神經纖維瘤會增加罹癌風險。然而，大部分兒童癌症（如白血病、淋巴瘤等）的主要治療手段仍是「化學治療（chemotherapy）」，而非標靶藥物；標靶藥物通常僅用於特定基因突變或難治型個案。",
      "flashcard_front": "兒童癌症 / 白血病盛行率 / 實體腫瘤診斷 / 遺傳疾病風險 / 主要治療手段",
      "flashcard_back": "大多數兒童癌症的主要治療為傳統「化學治療」，標靶藥物雖有應用，但非目前主要或首選的常規治療。",
      "flashcard_summary": "兒童癌症治療手段 -> 大多數兒童癌症的主要治療為傳統「化學治療」，標靶藥物雖有應用，但非目前主要或首選的常規治療。"
    },
    {
      "question_id": "112-2_medicine-4_020",
      "question_number": 20,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "辨識異體造血幹細胞移植的臨床適應症。",
      "explanation": "異體造血幹細胞移植（allogeneic HSCT）常用於治療血液系統重症，如重型地中海型貧血、高風險或復發性急性淋巴性白血病，以及嚴重型再生不良性貧血。系統性紅斑性狼瘡（SLE）屬於自體免疫疾病，治療以類固醇與免疫抑制劑為主，異體造血幹細胞移植並非其常規或適合的適應症。",
      "flashcard_front": "異體造血幹細胞移植 (HSCT) / 地中海型貧血 / 急性淋巴性白血病 / 再生不良性貧血 / 系統性紅斑性狼瘡 (SLE)",
      "flashcard_back": "異體造血幹細胞移植適用於嚴重的血液或骨髓衰竭疾病；系統性紅斑性狼瘡（SLE）非其適應症。",
      "flashcard_summary": "異體造血幹細胞移植適應症 -> 異體造血幹細胞移植適用於嚴重的血液或骨髓衰竭疾病；系統性紅斑性狼瘡（SLE）非其適應症。"
    },
    {
      "question_id": "112-2_medicine-4_021",
      "question_number": 21,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握兒童不同休克型態的病因分類。",
      "explanation": "張力性氣胸會壓迫腔靜脈阻礙回流，屬於阻塞性休克；擴張性心肌病變因心臟收縮無力，屬於心因性休克；腎病症候群因重度蛋白尿導致血管內水分流失，屬於低容積性休克。而心包膜填塞（cardiac tamponade）是由於心包積水壓迫心室充盈，屬於典型的「阻塞性休克（obstructive shock）」，而非分布性休克。",
      "flashcard_front": "兒童休克分類 / 張力性氣胸 / 腎病症候群 / 心包膜填塞 / 阻塞性與分布性休克",
      "flashcard_back": "心包膜填塞與張力性氣胸皆會阻礙心臟充盈或血液回流，屬於「阻塞性休克」，而非分布性休克。",
      "flashcard_summary": "心包膜填塞休克分類 -> 心包膜填塞與張力性氣胸皆會阻礙心臟充盈或血液回流，屬於「阻塞性休克」，而非分布性休克。"
    },
    {
      "question_id": "112-2_medicine-4_022",
      "question_number": 22,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "其他",
      "category_confidence": "high",
      "key_point": "掌握人體對低壓缺氧環境的急性生理順應現象。",
      "explanation": "當人體暴露於高海拔的低壓缺氧環境時，為維持組織氧氣供應，身體會啟動急性代償性順應（acclimatization）反應，包括呼吸加速以增加氣體交換、交感神經興奮導致心跳加速與血壓上升。此外，交感神經興奮亦會使靜脈血管收縮以維持回心血量，此時「血管張力（venous tone）」應該是上升而非下降。",
      "flashcard_front": "低壓缺氧 (hypobaric hypoxia) / 高海拔順應 / 心跳與呼吸 / 血壓變化 / 血管張力 (venous tone)",
      "flashcard_back": "低壓缺氧時，人體交感神經興奮代償，會使呼吸及心跳加速、血壓上升，且靜脈血管張力（venous tone）會上升。",
      "flashcard_summary": "低壓缺氧生理順應 -> 低壓缺氧時，人體交感神經興奮代償，會使呼吸及心跳加速、血壓上升，且靜脈血管張力（venous tone）會上升。"
    },
    {
      "question_id": "112-2_medicine-4_023",
      "question_number": 23,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握引發兒童多尿症狀的常見病因與電解質異常。",
      "explanation": "中樞型尿崩症（缺乏 ADH）、原發性多喝症（飲水過多）與第1型糖尿病（滲透性利尿）都會導致多尿。在電解質異常中，是「高血鈣症（hypercalcemia）」會干擾集尿管對 ADH 的反應而導致多尿；相反地，低血鈣症（hypocalcemia）通常不會引起多尿症狀，因此低血鈣症最不需考慮。",
      "flashcard_front": "兒童多尿 (polyuria) / 尿崩症 / 原發性多喝 / 第1型糖尿病 / 鈣離子異常與多尿",
      "flashcard_back": "高血鈣會導致腎因性尿崩而引發多尿；低血鈣則不會導致多尿，是鑑別多尿病因時最不需考慮的電解質異常。",
      "flashcard_summary": "鈣離子異常與多尿關係 -> 高血鈣會導致腎因性尿崩而引發多尿；低血鈣則不會導致多尿，是鑑別多尿病因時最不需考慮的電解質異常。"
    },
    {
      "question_id": "112-2_medicine-4_024",
      "question_number": 24,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握兒童性早熟的定義、病因及治療原則。",
      "explanation": "兒童性早熟定義為女孩8歲前、男孩9歲前出現第二性徵，並非所有病童都會嚴重影響最終成人身高。男孩性早熟有較高比例為器質性原因所致，須安排腦部影像檢查。在中樞性性早熟治療中，並非所有病童都需要使用 GnRH agonist，只有在骨齡進展過快、預估成人身高嚴重受損或有重大心理適應問題時才建議治療。",
      "flashcard_front": "兒童性早熟 / 定義年齡 / 男孩器質性比例 / GnRH agonist 治療指引",
      "flashcard_back": "中樞性性早熟不一定都需要接受 GnRH agonist 治療，須依骨齡進展速度與最終身高受損風險評估決定。",
      "flashcard_summary": "性早熟治療評估 -> 中樞性性早熟不一定都需要接受 GnRH agonist 治療，須依骨齡進展速度與最終身高受損風險評估決定。"
    },
    {
      "question_id": "112-2_medicine-4_025",
      "question_number": 25,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "鑑別兒童身材矮小與發育遲緩的病因。",
      "explanation": "此13歲男孩身高低於第3百分位，睪丸已發育至4毫升（代表剛進入青春期），骨齡11歲（延遲2年），其父母身高較矮。在此臨床表現下，骨齡延遲且身高極矮（低於第3百分位）可能符合體質性生長遲延，但在鑑別診斷中，若合併多種生長不良表現，必須優先排除腦垂體低能症（hypopituitarism）引起的生長激素缺乏，以避免錯失治療黃金期。",
      "flashcard_front": "13歲男孩矮小 / 骨齡延遲2年 / 睪丸4毫升 / 腦垂體低能症 / 體質性生長遲延",
      "flashcard_back": "嚴重矮小伴骨齡延遲、青春期剛啟動，應優先篩檢並排除腦垂體低能症（hypopituitarism）以防生長激素缺乏。",
      "flashcard_summary": "矮小與骨齡延遲鑑別 -> 嚴重矮小伴骨齡延遲、青春期剛啟動，應優先篩檢並排除腦垂體低能症（hypopituitarism）以防生長激素缺乏。"
    },
    {
      "question_id": "112-2_medicine-4_026",
      "question_number": 26,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握潛在免疫缺陷與特定病原體感染之關聯。",
      "explanation": "無脾症患者缺乏清除包膜菌的功能，易發生肺炎鏈球菌等菌血症；鐮狀細胞病因脾梗塞及骨髓微循環障礙，易發生沙門氏菌骨髓炎；先天性中性球減少症易遭金黃色葡萄球菌或綠膿桿菌感染。而補體缺乏（特別是後段補體 C5-C9 缺乏）最典型是增加「奈瑟氏菌屬（Neisseria）」的感染風險，而非瘧原蟲引起的瘧疾。",
      "flashcard_front": "免疫缺陷與感染 / 無脾症包膜菌 / 鐮狀細胞沙門氏菌 / 補體缺乏 / 奈瑟氏菌與瘧原蟲",
      "flashcard_back": "補體缺陷患者（尤其是晚期補體 C5-C9）易發生奈瑟氏腦膜炎雙球菌感染，與瘧原蟲感染無直接病理關聯。",
      "flashcard_summary": "補體缺陷易感病原 -> 補體缺陷患者（尤其是晚期補體 C5-C9）易發生奈瑟氏腦膜炎雙球菌感染，與瘧原蟲感染無直接病理關聯。"
    },
    {
      "question_id": "112-2_medicine-4_027",
      "question_number": 27,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握水痘與帶狀疱疹的傳染性與潛伏期。",
      "explanation": "3個月大男嬰身上出現水泡樣丘疹且無發燒，符合水痘（varicella）的臨床特徵。水痘的潛伏期通常為10至21天（約2週），且具高度傳染性。因此，男嬰最有可能的感染來源是2週前患有水痘的哥哥。相較之下，玫瑰疹與手足口病不會表現為典型水痘水泡，而媽媽5天前出現帶狀疱疹的時程與水痘潛伏期不符。",
      "flashcard_front": "3個月大嬰兒 / 無發燒水泡丘疹 / 感染源追溯 / 水痘潛伏期 / 帶狀疱疹接觸",
      "flashcard_back": "水痘的潛伏期約為 2 週（10-21 天），因此嬰兒出現水泡病灶，最可能的感染源是 2 週前患有水痘的家屬。",
      "flashcard_summary": "水痘傳染與潛伏期 -> 水痘的潛伏期約為 2 週（10-21 天），因此嬰兒出現水泡病灶，最可能的感染源是 2 週前患有水痘的家屬。"
    },
    {
      "question_id": "112-2_medicine-4_028",
      "question_number": 28,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "區分發燒（fever）與中暑/散熱不良（hyperthermia）的生理機轉。",
      "explanation": "發燒的病理生理機轉是體內的致熱源刺激下視丘，導致體溫調節中樞的「設定點（set-point）調高」，使身體主動增加產熱與減少散熱，而非單純的散熱不良。散熱不良是中暑或熱衰竭（hyperthermia）的特徵，此時設定點正常。發燒時可使用 ibuprofen 降溫，且溫水拭浴僅能輔助散熱，無法改變體溫設定點，退燒藥也無法縮短疾病病程。",
      "flashcard_front": "幼兒發燒處置 / 體溫調節設定點 / 發燒與中暑機轉 / 溫水拭浴限制 / 退燒藥作用",
      "flashcard_back": "發燒是因下視丘體溫設定點調高，使身體主動產熱；而散熱不良則是中暑（hyperthermia）的機轉。",
      "flashcard_summary": "發燒病理生理機轉 -> 發燒是因下視丘體溫設定點調高，使身體主動產熱；而散熱不良則是中暑（hyperthermia）的機轉。"
    },
    {
      "question_id": "112-2_medicine-4_029",
      "question_number": 29,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握單純型熱性痙攣的診斷要件與特徵。",
      "explanation": "單純型熱性痙攣（simple febrile seizure）好發於6個月至5歲孩童（高峰12-18個月），具家族遺傳傾向，通常在發燒24小時內發作且一次病程不超過一次。其發作表現為全身性（generalized），持續時間通常「短於15分鐘」，且不會進展至癲癇重積狀態；發作超過15分鐘或局部性發作者屬於複雜型熱性痙攣。",
      "flashcard_front": "單純型熱性痙攣 / 好發年齡 / 發作時間上限 / 全身性與局部性 / 複雜型區分",
      "flashcard_back": "單純型熱性痙攣持續時間小於 15 分鐘、呈全身性且24小時內僅發作一次；發作超過 15 分鐘則屬複雜型。",
      "flashcard_summary": "單純型熱性痙攣特徵 -> 單純型熱性痙攣持續時間小於 15 分鐘、呈全身性且24小時內僅發作一次；發作超過 15 分鐘則屬複雜型。"
    },
    {
      "question_id": "112-2_medicine-4_030",
      "question_number": 30,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握妥瑞氏症候群的臨床表現、共病與病程發展。",
      "explanation": "妥瑞氏症候群的診斷標準包括同時具備多種動作型及至少一種聲音型抽動（tics），且症狀持續超過一年。此病常合併注意力不足/過動症（ADHD）與強迫症（OCD）。病程發展上，大多數患者的症狀在進入成年期後會逐漸減輕甚至消失，而非越來越明顯。",
      "flashcard_front": "妥瑞氏症候群 (Tourette) / 動作與聲音型抽動 / 共病症 (ADHD/OCD) / 成年期預後",
      "flashcard_back": "妥瑞氏症常合併 ADHD 或 OCD；多數患者的抽動（tics）症狀在進入成年期後會逐漸改善，而非惡化。",
      "flashcard_summary": "妥瑞氏症病程與共病 -> 妥瑞氏症常合併 ADHD 或 OCD；多數患者的抽動（tics）症狀在進入成年期後會逐漸改善，而非惡化。"
    }
  ]
}

# Define batch 3
batch_3 = {
  "dataset_id": "112-2_medicine-4",
  "batch_id": "112-2_medicine-4_batch-003",
  "items": [
    {
      "question_id": "112-2_medicine-4_031",
      "question_number": 31,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握造成嬰兒前囟門早期關閉的疾病。",
      "explanation": "前囟門通常在嬰兒出生後12至18個月大時關閉。顱縫早閉（craniosynostosis）是由於一條或多條顱縫過早融合，會直接導致前囟門早期關閉，並造成頭顱畸形。相反地，軟骨發育不全（achondroplasia）、甲狀腺功能低下症（hypothyroidism）及腦積水（hydrocephalus）均會導致囟門關閉延遲或前囟門過大。",
      "flashcard_front": "前囟門早期關閉 / 顱縫早閉 (craniosynostosis) / 囟門關閉延遲病因 / 甲狀腺低下與腦積水",
      "flashcard_back": "顱縫早閉會導致前囟門過早關閉及頭形畸形；而甲狀腺低下、腦積水與軟骨發育不全則會導致囟門延遲關閉。",
      "flashcard_summary": "前囟門關閉異常 -> 顱縫早閉會導致前囟門過早關閉及頭形畸形；而甲狀腺低下、腦積水與軟骨發育不全則會導致囟門延遲關閉。"
    },
    {
      "question_id": "112-2_medicine-4_032",
      "question_number": 32,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握受虐性腦傷的臨床表徵與診斷思維。",
      "explanation": "一名僅3個月大、尚無自主翻爬能力的嬰兒，被發現頭頂血腫、大腿內側瘀傷（此部位極非此年紀活動易受傷處）且伴有奶量減少與嗜睡等意識改變，高度暗示非意外性創傷。臨床醫師應將受虐性腦傷（abusive head trauma, AHT）列入主要鑑別診斷。此外，腦部電腦斷層（CT）而非核磁共振（MRI）是急性期偵測腦出血的首選初步影像檢查。",
      "flashcard_front": "3個月大嬰兒 / 頭頂血腫與大腿瘀傷 / 嗜睡奶量減少 / 受虐性腦傷 (AHT) / 急性影像首選",
      "flashcard_back": "嬰兒未具活動力卻有不明大腿內側瘀傷與頭部血腫嗜睡，必須懷疑受虐性腦傷；急性出血首選檢查為電腦斷層（CT）。",
      "flashcard_summary": "受虐性腦傷鑑別 -> 嬰兒未具活動力卻有不明大腿內側瘀傷與頭部血腫嗜睡，必須懷疑受虐性腦傷；急性出血首選檢查為電腦斷層（CT）。"
    },
    {
      "question_id": "112-2_medicine-4_033",
      "question_number": 33,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "理解粒線體遺傳的特點與突變形式。",
      "explanation": "粒線體 DNA 主要遺傳自母親（母系遺傳），男女皆可能因遺傳而罹病，變異形式多為缺失或點突變。在健康的一般人身上，通常並不帶有致病性的粒線體基因病變，因此「一般人都帶有母親遺傳之粒線體基因病變」的敘述並不正確。",
      "flashcard_front": "粒線體遺傳 (Mitochondrial) / 母系遺傳 / 突變形式 / 正常人攜帶機率 / 男女發病機會",
      "flashcard_back": "粒線體遺傳呈母系遺傳，突變以點突變或缺失為主，健康的一般人身上通常不帶有此類致病性基因病變。",
      "flashcard_summary": "粒線體遺傳特徵 -> 粒線體遺傳呈母系遺傳，突變以點突變或缺失為主，健康的一般人身上通常不帶有此類致病性基因病變。"
    },
    {
      "question_id": "112-2_medicine-4_034",
      "question_number": 34,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "掌握不同時期異位性皮膚炎的皮損特徵。",
      "explanation": "嬰兒時期的異位性皮膚炎特徵為急性或亞急性濕疹，好發於面部、頭皮及四肢伸側（extensor side），且常伴隨食物過敏；而肢體屈側（flexor side）則是兒童中後期及青少年的典型受侵犯部位，因此「嬰兒期多發生於屈側」的敘述錯誤。成人期的患者則常以慢性手部濕疹或苔癬化皮損為表現。",
      "flashcard_front": "嬰兒期異膚 / 臉部與肢體伸側 / 肢體屈側 / 食物過敏 / 成人期手部濕疹",
      "flashcard_back": "嬰兒期異位性皮膚炎好發於臉部與四肢伸側；四肢屈側（如肘窩膝窩）則是兒童中後期及青少年期的特徵。",
      "flashcard_summary": "嬰幼兒異膚好發部位 -> 嬰兒期異位性皮膚炎好發於臉部與四肢伸側；四肢屈側（如肘窩膝窩）則是兒童中後期及青少年期的特徵。"
    },
    {
      "question_id": "112-2_medicine-4_035",
      "question_number": 35,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "掌握可能誘發或惡化乾癬的常見藥物。",
      "explanation": "許多系統性藥物會誘發或惡化乾癬（psoriasis）的症狀，其中最經典且常見的藥物為乙型受體阻斷劑（Beta-blockers），如用於控制血壓的 propranolol。其他常見易惡化乾癬的藥物還包括鋰鹽、全身性類固醇（停藥後易反彈）及抗瘧藥等；利尿劑 furosemide、甲型阻斷劑 prazosin 及降血脂藥 atorvastatin 則無此明確關聯。",
      "flashcard_front": "乾癬惡化 / 高血壓高血脂用藥 / propranolol / 乙型受體阻斷劑 / 乾癬誘發藥物",
      "flashcard_back": "乙型受體阻斷劑（如 propranolol）是臨床上已知最容易導致乾癬症狀惡化或誘發乾癬的常用降血壓藥物。",
      "flashcard_summary": "乾癬與惡化藥物 -> 乙型受體阻斷劑（如 propranolol）是臨床上已知最容易導致乾癬症狀惡化或誘發乾癬的常用降血壓藥物。"
    },
    {
      "question_id": "112-2_medicine-4_036",
      "question_number": 36,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "辨識頸部扁平疣的臨床皮損特徵。",
      "explanation": "13歲男孩頸部出現多個微隆起、表面扁平且呈膚色或淡褐色的丘疹，此皮損符合扁平疣（verruca plana）的典型表現。扁平疣是由人類乳突病毒（HPV）感染表皮所致，常呈線性排列（Koebner phenomenon）。汗管瘤多見於眼周，類澱粉苔癬呈顆粒狀且極癢，尋常性痤瘡則通常伴有粉刺或發炎性丘疹。",
      "flashcard_front": "頸部皮損 / 扁平微隆起丘疹 / 膚色或淡褐色 / 扁平疣 / 鑑別診斷",
      "flashcard_back": "頸部出現多發、微隆起且表面扁平的膚色或淡褐色丘疹，臨床上應診斷為 HPV 感染引起的扁平疣。",
      "flashcard_summary": "扁平疣診斷 -> 頸部出現多發、微隆起且表面扁平的膚色或淡褐色丘疹，臨床上應診斷為 HPV 感染引起的扁平疣。"
    },
    {
      "question_id": "112-2_medicine-4_037",
      "question_number": 37,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "掌握扁平疣的合適臨床治療手段。",
      "explanation": "扁平疣（verruca plana）是由人類乳突病毒（HPV）所引起，治療上以破壞受感染的表皮細胞或調節局部免疫為主，其中「冷凍治療（cryotherapy）」是臨床上最常用且有效的物理性治療手段。外用抗生素、外用類固醇（可能會抑制局部免疫導致惡化）或手術切除（易留下疤痕）皆不適合作為扁平疣的常規首選治療。",
      "flashcard_front": "扁平疣治療 / 冷凍治療 (liquid nitrogen) / 外用類固醇與抗生素 / 手術切除限制",
      "flashcard_back": "扁平疣治療首選為液態氮冷凍治療，外用類固醇易因局部免疫抑制惡化病情，手術切除則易遺留疤痕。",
      "flashcard_summary": "扁平疣治療選擇 -> 扁平疣治療首選為液態氮冷凍治療，外用類固醇易因局部免疫抑制惡化病情，手術切除則易遺留疤痕。"
    },
    {
      "question_id": "112-2_medicine-4_038",
      "question_number": 38,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "掌握甲下外生骨的臨床與放射線學特徵。",
      "explanation": "甲下外生骨（subungual exostosis）是一種良性的骨性增生物，好發於兒童及青少年的遠端指骨（特別是大腳趾或手指甲下），臨床上會表現為指甲下慢慢變大且伴隨疼痛的硬質結節。X光攝影可見到由遠端指骨背側向外突出的骨性贅生物，此特徵可與甲下病毒疣（無骨性增生）、角化棘皮瘤或血管球瘤（主要以劇烈觸痛及藍紅色斑為主，X光多呈骨壓迫凹陷而非突出）作鑑別。",
      "flashcard_front": "指甲下疼痛增生物 / 遠端指骨背側 / X光骨性突出 / 甲下外生骨 / 鑑別血管球瘤",
      "flashcard_back": "甲下增生物伴隨 X 光呈遠端指骨處骨性突出，為甲下外生骨特徵；血管球瘤 X 光常為皮質壓迫吸收而非突出。",
      "flashcard_summary": "甲下外生骨診斷 -> 甲下增生物伴隨 X 光呈遠端指骨處骨性突出，為甲下外生骨特徵；血管球瘤 X 光常為皮質壓迫吸收而非突出。"
    },
    {
      "question_id": "112-2_medicine-4_039",
      "question_number": 39,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "掌握避免 carbamazepine 誘發嚴重皮膚藥物過敏的篩檢基因。",
      "explanation": "在國內及亞洲地區，使用抗癲癇與三叉神經痛藥物 carbamazepine（卡巴馬平）之前，依法建議必須先進行 HLA-B*1502 基因檢測。若帶有此基因者使用 carbamazepine，會極大幅度增加產生史蒂芬斯-強森症候群（SJS）或毒性表皮壞死解離症（TEN）等致命性皮膚不良反應的風險。Abacavir 則與 HLA-B*5701 相關，allopurinol 則與 HLA-B*5801 相關。",
      "flashcard_front": "HLA-B*1502 檢測 / carbamazepine / SJS與TEN預防 / 藥物不良反應 / 亞洲人群",
      "flashcard_back": "使用 carbamazepine 前篩檢 HLA-B*1502 基因可避免嚴重的 SJS/TEN；allopurinol 則與 HLA-B*5801 相關。",
      "flashcard_summary": "HLA與嚴重藥物疹 -> 使用 carbamazepine 前篩檢 HLA-B*1502 基因可避免嚴重的 SJS/TEN；allopurinol 則與 HLA-B*5801 相關。"
    },
    {
      "question_id": "112-2_medicine-4_040",
      "question_number": 40,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "掌握全身性硬化症不同症狀的治療方式。",
      "explanation": "全身性硬化症（systemic sclerosis）中，皮膚硬化病灶可使用 UVA1 紫外光光療以促進膠原蛋白降解並減輕硬化。手指潰瘍常由於嚴重血管痙攣引起，應給予系統性血管擴張劑而非局部類固醇注射（會加重缺血及妨礙癒合）；微血管擴張非口服類固醇適應症；皮膚鈣化通常對物理治療無反應，主要以外科切除或藥物輔助治療。",
      "flashcard_front": "全身性硬化症 / 皮膚硬化治療 / UVA1光療 / 手指潰瘍禁忌 / 皮膚鈣化處置",
      "flashcard_back": "全身性硬化症的皮膚硬化首選 UVA1 光療；手指潰瘍禁用局部類固醇注射，以防血管收縮加重缺血。",
      "flashcard_summary": "全身性硬化症症狀治療 -> 全身性硬化症的皮膚硬化首選 UVA1 光療；手指潰瘍禁用局部類固醇注射，以防血管收縮加重缺血。"
    },
    {
      "question_id": "112-2_medicine-4_041",
      "question_number": 41,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "掌握不同皮膚疾病對應的特徵性指甲變化。",
      "explanation": "乾癬的指甲變化常見點狀凹痕（pitting）、油滴狀變色與指甲下角質增厚；扁平苔癬可導致嚴重的指甲萎縮、縱向溝紋及甲翼狀贅肉；甲癬則典型表現為指甲下角質增厚與甲床分離。然而，「油滴狀變色（oil spot/salmon spot）」是乾癬（psoriasis）的特徵性表現，在圓禿（alopecia areata）的患者中極不常見，圓禿指甲多呈規則幾何狀凹點（geometric pitting）。",
      "flashcard_front": "指甲病變 / 點狀凹痕與油滴狀變色 / 指甲萎縮 / 乾癬與圓禿指甲鑑別",
      "flashcard_back": "油滴狀變色是乾癬的特徵性指甲變化，圓禿的指甲病變則以幾何狀規則凹痕為主，不常見油滴狀變色。",
      "flashcard_summary": "皮膚病與指甲變化 -> 油滴狀變色是乾癬的特徵性指甲變化，圓禿的指甲病變則以幾何狀規則凹痕為主，不常見油滴狀變色。"
    },
    {
      "question_id": "112-2_medicine-4_042",
      "question_number": 42,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "掌握化膿性汗腺炎的流行病學與病理發展。",
      "explanation": "化膿性汗腺炎（HS）主要對稱發生於頂漿腺分布處如腋下、腹股溝及臀部。流行病學上，此病在「女性中較男性更為常見」（女性約為男性的 3 倍），因此「男性較女性常見」的敘述錯誤。對於廣泛反覆發作的病灶，手術切除合併皮瓣重建是合理的選項；長期慢性發炎的瘻管也有繼發鱗狀上皮細胞癌（SCC）的風險。",
      "flashcard_front": "化膿性汗腺炎 (HS) / 頂漿腺分布 / 性別盛行率 / 手術切除皮瓣 / 鱗狀上皮細胞癌風險",
      "flashcard_back": "化膿性汗腺炎好發於女性（非男性）；病灶呈對稱分布，慢性發炎嚴重者需手術切除，且有演變為 SCC 的風險。",
      "flashcard_summary": "化膿性汗腺炎特徵 -> 化膿性汗腺炎好發於女性（非男性）；病灶呈對稱分布，慢性發炎嚴重者需手術切除，且有演變為 SCC 的風險。"
    },
    {
      "question_id": "112-2_medicine-4_043",
      "question_number": 43,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "皮膚科",
      "category_confidence": "high",
      "key_point": "掌握 Darier disease 的遺傳、臨床特徵與惡化因子。",
      "explanation": "Darier disease（毛囊角化症）是一種體染色體顯性遺傳疾病，其特徵為脂漏區域的角化性丘疹、指甲脆弱伴有紅白相間的縱向條紋，且表皮屏障受損易合併細菌或疱疹病毒感染。由於此病對熱、紫外線及摩擦高度敏感，病灶在「夏季（而非冬季）」由於出汗與日曬更容易惡化。",
      "flashcard_front": "Darier disease / 體染色體顯性 / 季節性惡化 / 指甲紅白縱紋 / 表皮感染風險",
      "flashcard_back": "Darier disease 由於對紫外線、熱及汗水敏感，病灶在「夏季」容易惡化，而非冬季。",
      "flashcard_summary": "Darier disease特徵 -> Darier disease 由於對紫外線、熱及汗水敏感，病灶在「夏季」容易惡化，而非冬季。"
    },
    {
      "question_id": "112-2_medicine-4_044",
      "question_number": 44,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握毛毛樣血管疾病的病理定義。",
      "explanation": "毛毛樣血管疾病（moyamoya disease）是一種慢性進行性腦血管閉塞性疾病，主要病變為雙側內頸動脈末端及其分支慢性進行性狹窄或阻塞，進而代償性地增生出許多纖細的側枝循環小血管。這些增生的微小血管在血管攝影上呈現如「煙霧繚繞（moyamoya）」的外觀，並非由於腦腫瘤或結核性血管炎所致。",
      "flashcard_front": "毛毛樣血管疾病 (moyamoya) / 內頸動脈末端阻塞 / 側枝循環增生 / 煙霧狀血管攝影",
      "flashcard_back": "毛毛樣血管病是指顱內大血管（如內頸動脈末端）進行性阻塞，並代償增生細小側枝血管的病變。",
      "flashcard_summary": "毛毛樣血管病病理 -> 毛毛樣血管病是指顱內大血管（如內頸動脈末端）進行性阻塞，並代償增生細小側枝血管的病變。"
    },
    {
      "question_id": "112-2_medicine-4_045",
      "question_number": 45,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握缺血性腦中風的預防與抗栓塞藥物選擇。",
      "explanation": "對於症狀性顱內大動脈（如中大腦動脈 MCA）嚴重狹窄（>=70%），根據臨床試驗（如 WASID），優先推薦使用雙重抗血小板藥物（DAPT，如阿斯匹靈加 clopidogrel）預防中風復發，其效果優於抗凝血劑（如華法林）且出血風險較低。來源不明之栓塞型中風（ESUS）首選抗血小板藥物；CHA2DS2-VASc 為 0 分之非瓣膜性房顫患者暫不用抗血栓藥物。",
      "flashcard_front": "顱內動脈70%狹窄 / 抗血小板與抗凝血劑 / 來源不明栓塞型中風 (ESUS) / 心房顫動評分",
      "flashcard_back": "症狀性顱內動脈嚴重狹窄預防中風應首選「抗血小板藥物」，而非抗凝血劑（如 warfarin）；後者出血風險較高。",
      "flashcard_summary": "顱內狹窄與中風預防 -> 症狀性顱內動脈嚴重狹窄預防中風應首選「抗血小板藥物」，而非抗凝血劑（如 warfarin）；後者出血風險較高。"
    }
  ]
}

# Define batch 4
batch_4 = {
  "dataset_id": "112-2_medicine-4",
  "batch_id": "112-2_medicine-4_batch-004",
  "items": [
    {
      "question_id": "112-2_medicine-4_046",
      "question_number": 46,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "辨識腦出血的影像學演變與診斷。",
      "explanation": "暗黑的高血壓病史患者，突發右側肢體無力及麻木。急性期無顯影劑電腦斷層（non-contrast CT）呈現左側視丘高密度影，代表急性腦出血（ICH）；5天後腦部磁振造影（MRI）之 FLAIR 與 T1 影像呈現血腫周圍水腫與亞急性出血的訊號演變，符合典型的「高血壓引發腦出血」，可排除腦腫瘤或多發性硬化症。",
      "flashcard_front": "突發右側無力 / 電腦斷層高密度 / 磁振造影5天後變化 / 高血壓腦出血 / 視丘出血",
      "flashcard_back": "突發單側偏癱、CT 呈視丘高密度影，為典型高血壓性腦出血；MRI 可見亞急性期血腫周圍水腫演變。",
      "flashcard_summary": "高血壓腦出血診斷 -> 突發單側偏癱、CT 呈視丘高密度影，為典型高血壓性腦出血；MRI 可見亞急性期血腫周圍水腫演變。"
    },
    {
      "question_id": "112-2_medicine-4_047",
      "question_number": 47,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握兒童夢遊症的臨床與睡眠生理特徵。",
      "explanation": "夢遊症（somnambulism）屬於非快速動眼期（NREM）睡眠異常，通常發生在慢波睡眠的第三期（N3），與夜驚症、覺醒障礙同屬非 REM 醒覺障礙，通常不需藥物治療。而「夢境實演（dream enactment behavior）」是快速動眼期睡眠行為障礙（RBD）的特徵，患者會將 REM 期的夢境動作實演出來，這與夢遊症患者並無清晰夢境的狀態不同。",
      "flashcard_front": "兒童夢遊症 / NREM 第三期 (N3) / 夢境實演 / REM睡眠行為障礙 (RBD) / 藥物治療指引",
      "flashcard_back": "夢遊症發生於 NREM 慢波睡眠期，無夢境實演行為；夢境實演為 REM 睡眠行為障礙（RBD）之特徵。",
      "flashcard_summary": "夢遊症與夢境實演 -> 夢遊症發生於 NREM 慢波睡眠期，無夢境實演行為；夢境實演為 REM 睡眠行為障礙（RBD）之特徵。"
    },
    {
      "question_id": "112-2_medicine-4_048",
      "question_number": 48,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握偏頭痛病理生理機轉中相關的神經傳導物質。",
      "explanation": "偏頭痛的發生與三叉神經血管系統的活化密切相關，其中降鈣素基因相關胜肽（CGRP）、血清素（5-HT）及多巴胺等物質皆參與其中。本題因官方考量考點爭議，判定為一律給分；然而在官方答案公布前，CGRP 是目前公認偏頭痛治療（如 CGRP 單株抗體）的核心標靶，而乙醯膽鹼（acetylcholine）通常與偏頭痛病理的直接關聯性最低。",
      "flashcard_front": "偏頭痛機轉 / 三叉神經血管系統 / CGRP / 血清素與多巴胺 / 乙醯膽鹼關聯",
      "flashcard_back": "降鈣素基因相關胜肽（CGRP）與血清素在偏頭痛機制中扮演關鍵角色；乙醯膽鹼與偏頭痛發作的直接關聯最小。",
      "flashcard_summary": "偏頭痛神經傳導物質 -> 降鈣素基因相關胜肽（CGRP）與血清素在偏頭痛機制中扮演關鍵角色；乙醯膽鹼與偏頭痛發作的直接關聯最小。"
    },
    {
      "question_id": "112-2_medicine-4_049",
      "question_number": 49,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "區分誘發癲癇發作的急性因素與良性熱痙攣史。",
      "explanation": "癲癇或癲癇發作的急性誘發因素包括陳舊性中風患者的全身性感染（如敗血症導致代謝混亂）、抗癲癇藥物自行停藥，以及糖尿病酮酸中毒（DKA）等嚴重代謝性異常。然而，患者在幼兒時期（3歲時）曾有過單純型熱痙攣（simple febrile seizure）且後續發育正常，並不會成為其青少年期癲癇發作的急性誘發因子。",
      "flashcard_front": "癲癇誘發因素 / 單純型熱痙攣病史 / 急性停藥 / 中風併發感染 / DKA 代謝異常",
      "flashcard_back": "幼時單純型熱痙攣無後遺症，不會增加日後癲癇發作機率；而停藥、敗血症與 DKA 則為常見急性誘發因子。",
      "flashcard_summary": "癲癇誘發因素辨識 -> 幼時單純型熱痙攣無後遺症，不會增加日後癲癇發作機率；而停藥、敗血症與 DKA 則為常見急性誘發因子。"
    },
    {
      "question_id": "112-2_medicine-4_050",
      "question_number": 50,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握巴金森氏病的藥物治療與手術原則。",
      "explanation": "左多巴（levodopa）雖然是治療巴金森氏病的黃金藥物，但長期、大劑量使用容易提早引發運動併發症（如藥效波動與異動症），因此臨床上應避免「越早使用大劑量」的做法。多巴胺促效劑常作為年輕患者的一線選擇以延緩左多巴的使用；而口服藥物控制不佳者，則可考慮深部腦刺激術（如視丘下核刺激術）。",
      "flashcard_front": "巴金森氏病治療 / 左多巴劑量與副作用 / 多巴胺促效劑適用年齡 / 視丘下核刺激術 (DBS)",
      "flashcard_back": "左多巴不宜過早使用大劑量，以防提早產生異動症等運動併發症；年輕患者可先用多巴胺促效劑。",
      "flashcard_summary": "巴金森氏病Levodopa用藥 -> 左多巴不宜過早使用大劑量，以防提早產生異動症等運動併發症；年輕患者可先用多巴胺促效劑。"
    },
    {
      "question_id": "112-2_medicine-4_051",
      "question_number": 51,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握普里昂疾病（庫賈氏症）的致病機轉與診斷。",
      "explanation": "普里昂疾病（prion disease，如庫賈氏症）是由於正常普里昂蛋白（PrPC）發生三維結構改變，錯誤摺疊成具感染性的異常普里昂蛋白（PrPSc）所致，其致病「並非由病毒或細菌感染引起」，因此 A 選項敘述錯誤。散發性庫賈氏症占最多數，臨床以快速退化性失智、肌陣攣、視覺障礙等為特徵，可藉由腦波、MRI 及腦脊髓液 14-3-3 蛋白協助診斷。",
      "flashcard_front": "普里昂疾病 (prion) / 庫賈氏症 (CJD) / 蛋白質錯誤摺疊 / 病毒感染謬誤 / 14-3-3 蛋白",
      "flashcard_back": "普里昂疾病是因蛋白質錯誤摺疊引起的退化性疾病，不含核酸，與病毒或細菌等傳染性病原體無關。",
      "flashcard_summary": "普里昂疾病致病機轉 -> 普里昂疾病是因蛋白質錯誤摺疊引起的退化性疾病，不含核酸，與病毒或細菌等傳染性病原體無關。"
    },
    {
      "question_id": "112-2_medicine-4_052",
      "question_number": 52,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "辨識亨丁頓氏病的臨床表徵與遺傳特性。",
      "explanation": "40歲患者表現出漸進式的不自主動作（舞動症/擠眉弄眼/扭腰）、伴隨早期記憶力衰退及認知退化，且其父親有類似症狀（48歲發病）及自殺史。此種體染色體顯性遺傳、發病於中年、合並不自主運動與精神/認知症狀的表現，是亨丁頓氏病（Huntington disease）的典型特徵。該病是由於第四對染色體上的 CAG 重複序列異常擴增所致。",
      "flashcard_front": "中年發病不自主動作 / 記憶力衰退 / 顯性遺傳家族史 / 父親自殺史 / 亨丁頓氏病",
      "flashcard_back": "中年出現舞蹈症不自主動作、認知退化，且具體染色體顯性遺傳及精神症狀家族史，診斷首選亨丁頓氏病。",
      "flashcard_summary": "亨丁頓氏病臨床特徵 -> 中年出現舞蹈症不自主動作、認知退化，且具體染色體顯性遺傳及精神症狀家族史，診斷首選亨丁頓氏病。"
    },
    {
      "question_id": "112-2_medicine-4_053",
      "question_number": 53,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握運動神經元疾病與其他肌無力疾病的無力特徵。",
      "explanation": "運動神經元疾病（MND，如肌萎縮性側索硬化症 ALS）的臨床特徵為「進行性、持續性且不可逆」的肌肉無力與萎縮，通常不會出現波動性或間歇性的變化。相反地，重症肌無力（肌無力症候群）典型表現為每日症狀波動與疲勞性；甲狀腺亢進引發的低血鉀性肌肉無力及週期性麻痺則表現為間歇性急性無力發作。",
      "flashcard_front": "進行性無力 / 波動性或間歇性無力 / 運動神經元疾病 (MND) / 重症肌無力 / 週期性麻痺",
      "flashcard_back": "運動神經元疾病（MND）無力呈持續進行性加重；而重症肌無力及週期性麻痺則呈波動性或間歇性無力。",
      "flashcard_summary": "運動神經元疾病無力特徵 -> 運動神經元疾病（MND）無力呈持續進行性加重；而重症肌無力及週期性麻痺則呈波動性或間歇性無力。"
    },
    {
      "question_id": "112-2_medicine-4_054",
      "question_number": 54,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握多發性肌炎的受犯肌肉部位與臨床特徵。",
      "explanation": "多發性肌炎（polymyositis）是一種自體免疫性發炎性肌病，主要侵犯「四肢近端肌肉」（如肩帶、骨盆帶肌群），導致梳頭或登梯困難，治療以類固醇為主，且少數患者可能伴隨惡性腫瘤。然而，多發性肌炎「極少侵犯動眼肌」，因此臨床上通常不會出現複視（diplopia）症狀；若病人有波動性複視，應考慮重症肌無力等診斷。",
      "flashcard_front": "多發性肌炎 / 近端肌肉無力 / 類固醇治療 / 癌症風險 / 複視與動眼肌",
      "flashcard_back": "多發性肌炎主要影響近端肢體骨骼肌，極少侵犯眼外肌，故臨床上通常「不出現複視或眼瞼下垂」。",
      "flashcard_summary": "多發性肌炎臨床表現 -> 多發性肌炎主要影響近端肢體骨骼肌，極少侵犯眼外肌，故臨床上通常「不出現複視或眼瞼下垂」。"
    },
    {
      "question_id": "112-2_medicine-4_055",
      "question_number": 55,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握急性脊髓損傷後脊髓休克的診斷特徵。",
      "explanation": "18歲男性跳水撞擊頭部，神經學檢查發現肛門反射與球海綿體肌反射完全消失，同時伴有四肢運動及感覺功能喪失。這種在急性脊髓外傷後，損傷水平以下所有脊髓反射、運動及感覺功能「暫時性完全喪失」的狀態，是「脊髓休克（spinal shock）」的典型表現，此時無法準確評估為部分或完全性永久損傷。",
      "flashcard_front": "頸部外傷 / 肛門與球海綿體反射消失 / 四肢感覺運動喪失 / 脊髓休克 / 急性期反射",
      "flashcard_back": "脊髓急性損傷後，損傷平面以下運動、感覺與脊髓反射（肛門/球海綿體）短暫完全消失，診斷為脊髓休克。",
      "flashcard_summary": "脊髓休克診斷 -> 脊髓急性損傷後，損傷平面以下運動、感覺與脊髓反射（肛門/球海綿體）短暫完全消失，診斷為脊髓休克。"
    },
    {
      "question_id": "112-2_medicine-4_056",
      "question_number": 56,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握多發性硬化症的流行病學與常見症狀。",
      "explanation": "多發性硬化症（MS）是中樞神經系統白質的去髓鞘病變，視神經炎常為初始症狀，且病患常伴隨疲倦與沮喪。在流行病學上，此病的發生率與緯度呈正相關，即「緯度越高、天氣越冷、日照越少（維生素D不足）的地區，發生率越高」，因此「緯度越高發生率越低」的敘述錯誤。",
      "flashcard_front": "多發性硬化症 (MS) / 去髓鞘病變 / 緯度與盛行率 / 初始症狀 (視神經炎) / 維生素D關聯",
      "flashcard_back": "多發性硬化症的發生率與緯度呈正相關，緯度越高且天氣冷、日照少的地區，其盛行率及發生率越高。",
      "flashcard_summary": "多發性硬化症流行病學 -> 多發性硬化症的發生率與緯度呈正相關，緯度越高且天氣冷、日照少的地區，其盛行率及發生率越高。"
    },
    {
      "question_id": "112-2_medicine-4_057",
      "question_number": 57,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "理解唐氏症與早期阿茲海默氏病病理變化的遺傳機轉。",
      "explanation": "唐氏症（三體染色體 21）患者在40歲後幾乎都會出現阿茲海默氏病的澱粉樣斑塊等神經病理變化。這是因為澱粉樣前驅蛋白（APP）基因就位於第21號染色體上；三體染色體導致 APP 基因過度表現，產生過量的 beta-amyloid，從而加速了阿茲海默氏病的病程。APOE、PSEN1 及 PSEN2 則與其他遺傳型或散發型阿茲海默症相關，但非此現象的主因。",
      "flashcard_front": "唐氏症 / 40歲阿茲海默病理 / 第21號染色體 / APP 基因過度表現 / 澱粉樣斑塊",
      "flashcard_back": "唐氏症（三體21）因 APP 基因位於第 21 號染色體，多一個拷貝導致 APP 過度表現而提早出現阿茲海默病理。",
      "flashcard_summary": "唐氏症與阿茲海默症 -> 唐氏症（三體21）因 APP 基因位於第 21 號染色體，多一個拷貝導致 APP 過度表現而提早出現阿茲海默病理。"
    },
    {
      "question_id": "112-2_medicine-4_058",
      "question_number": 58,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握急性化膿性腦膜炎的致病菌、診斷與經驗性治療原則。",
      "explanation": "急性化膿性腦膜炎的經驗性治療中，在培養結果出來前，為覆蓋抗藥性肺炎鏈球菌，必須包含第三代頭孢菌素類（如 ceftriaxone）並常合併 vancomycin。臨床上，只有約44%的患者會同時出現高燒、頸部僵硬與意識改變的三聯症（非80%以上）。成人非 B 群鏈球菌好發人群；腦壓升高引起的庫欣氏三聯症（Cushing's triad）表現為心跳變慢（非變快）、血壓上升與呼吸不規則。",
      "flashcard_front": "急性化膿性腦膜炎 / 經驗性抗生素 (第三代頭孢菌素) / 臨床三聯症比例 / 腦壓增高庫欣三聯症 / 心跳變化",
      "flashcard_back": "化膿性腦膜炎經驗治療需用三代頭孢菌素防抗藥性肺炎鏈球菌；腦壓高的庫欣氏反射會導致心跳「變慢」非變快。",
      "flashcard_summary": "腦膜炎治療與腦壓變化 -> 化膿性腦膜炎經驗治療需用三代頭孢菌素防抗藥性肺炎鏈球菌；腦壓高的庫欣氏反射會導致心跳「變慢」非變快。"
    },
    {
      "question_id": "112-2_medicine-4_059",
      "question_number": 59,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "區分精神醫學中不同類型的妄想定義。",
      "explanation": "妄想是與現實不符且無法被客觀證據說服的堅定信念。病人堅信自己是神仙下凡、能拯救世人，屬於典型的誇大妄想（delusion of grandeur）。而堅信有人要加害自己屬於被害妄想（而非虛無妄想）；堅信他人愛上自己屬於情愛妄想（而非嫉妒妄想）；堅信周遭無關事物皆與自己有關屬於關係妄想（而非控制妄想）。",
      "flashcard_front": "妄想分類 / 拯救世人與神仙下凡 / 誇大妄想 / 被害妄想 / 關係與控制妄想",
      "flashcard_back": "堅信自己擁有非凡超能力、神聖身份或能拯救世人，定義為誇大妄想（delusion of grandeur）。",
      "flashcard_summary": "誇大妄想定義 -> 堅信自己擁有非凡超能力、神聖身份或能拯救世人，定義為誇大妄想（delusion of grandeur）。"
    },
    {
      "question_id": "112-2_medicine-4_060",
      "question_number": 60,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握物質或藥物引發精神病症的臨床特徵與鑑別。",
      "explanation": "物質或藥物引發之精神病症常以被害妄想及幻覺（如使用古柯鹼易有蟻爬感等觸幻覺）為特徵，顳葉癲癇則常伴隨嗅幻覺。由於患者此時處於精神病狀態（psychosis），其「現實感（reality testing）會受損（即現實感差）」，而非現實感佳。因此 C 選項敘述最不適當。",
      "flashcard_front": "物質引發精神病症 / 古柯鹼觸幻覺 / 顳葉癲癇嗅幻覺 / 現實感評估 / 被害妄想",
      "flashcard_back": "物質或藥物引發之精神病症中，患者的現實感（reality testing）受損而呈現混亂，並非現實感佳。",
      "flashcard_summary": "物質引發精神病現實感 -> 物質或藥物引發之精神病症中，患者的現實感（reality testing）受損而呈現混亂，並非現實感佳。"
    }
  ]
}

# Define batch 5
batch_5 = {
  "dataset_id": "112-2_medicine-4",
  "batch_id": "112-2_medicine-4_batch-005",
  "items": [
    {
      "question_id": "112-2_medicine-4_061",
      "question_number": 61,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握思覺失調症的症狀途徑與自殺、認知功能特徵。",
      "explanation": "思覺失調症患者約有 5-6% 死於自殺，且其認知功能退化比正性症狀更能預測長期社會功能。在多巴胺假說中，幻覺、妄想等正性症狀與中腦邊緣途徑（mesolimbic pathway）的多巴胺過度活躍有關；而情感淡漠、社交退縮等「負性症狀（negative symptoms）及認知缺陷」則主要與「中腦皮質途徑（mesocortical pathway）」的多巴胺功能低下有關。",
      "flashcard_front": "思覺失調症 / 正性與負性症狀途徑 / 中腦邊緣與中腦皮質 / 自殺率 / 社會功能預測",
      "flashcard_back": "幻覺等正性症狀與中腦邊緣途徑有關；社交退縮等負性症狀及認知退化則與中腦皮質途徑異常有關。",
      "flashcard_summary": "思覺失調症多巴胺途徑 -> 幻覺等正性症狀與中腦邊緣途徑有關；社交退縮等負性症狀及認知退化則與中腦皮質途徑異常有關。"
    },
    {
      "question_id": "112-2_medicine-4_062",
      "question_number": 62,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握情緒穩定劑的療效、毒性及孕婦使用風險。",
      "explanation": "鋰鹽（lithium）能有效降低雙相情緒障礙症患者的自殺風險，服用時需注意水分攝取以穩定血藥濃度，中毒時會出現粗大震顫、腹瀉及口齒不清。然而，在懷孕期間，相較於抗精神病藥物，傳統的情緒穩定劑（如鋰鹽有 Ebstein 畸形風險、癲通及帝拔癲有神經管缺損風險）對「胎兒造成的畸形危險是顯著較高」的。",
      "flashcard_front": "情緒穩定劑 / 鋰鹽自殺預防 / 孕婦畸胎風險 / 鋰鹽中毒症狀 / 抗精神病藥比較",
      "flashcard_back": "傳統情緒穩定劑（如鋰鹽、帝拔癲）的致畸胎風險顯著高於非典型抗精神病藥物，孕婦使用時須極為審慎。",
      "flashcard_summary": "情緒穩定劑畸胎風險 -> 傳統情緒穩定劑（如鋰鹽、帝拔癲）的致畸胎風險顯著高於非典型抗精神病藥物，孕婦使用時須極為審慎。"
    },
    {
      "question_id": "112-2_medicine-4_063",
      "question_number": 63,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握強迫症的藥物與心理治療原則。",
      "explanation": "強迫症（OCD）的首選藥物是選擇性血清素回收抑制劑（SSRIs，通常需要比憂鬱症更高的劑量），而鋰鹽或苯二氮平（BZD）皆非強迫症的首選或有效預防藥物。心理治療中，精神分析治療對強迫症的效果有限，目前實證醫學證實「認知行為治療（CBT，特別是暴露與反應抑制療法 ERP）合併藥物治療」具有最佳的臨床療效。",
      "flashcard_front": "強迫症 (OCD) 治療 / 首選藥物 (SSRIs) / 暴露與反應抑制 (ERP) / 精神分析療效 / BZD與鋰鹽定位",
      "flashcard_back": "強迫症的首選藥物為 SSRIs，且臨床上以「行為治療（ERP）合併藥物治療」能達到最理想的療效。",
      "flashcard_summary": "強迫症治療原則 -> 強迫症的首選藥物為 SSRIs，且臨床上以「行為治療（ERP）合併藥物治療」能達到最理想的療效。"
    },
    {
      "question_id": "112-2_medicine-4_064",
      "question_number": 64,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "區分第一型與第二型雙相情緒障礙症的流行病學與自殺特徵。",
      "explanation": "重鬱症在女性盛行率為男性的兩倍，而第一型雙相情緒障礙症（Bipolar I）盛行率無明顯性別差異且合併物質濫用比例高。第二型雙相情緒障礙症（Bipolar II）的患者主要表現為輕躁狂與重鬱發作，由於其重鬱期時間長且反覆發作，其「自殺死亡率及企圖心與第一型患者相當甚至更高」，且初發病年齡並不比第一型晚，因此 D 選項敘述錯誤。",
      "flashcard_front": "情緒障礙症 / 第一型與第二型雙相障礙 / 自殺死亡率比較 / 性別盛行率 / 初發病年齡",
      "flashcard_back": "第二型雙相情緒障礙症患者的自殺死亡率與第一型患者相當或更高，並非較低；且其重鬱症狀通常更頻繁。",
      "flashcard_summary": "雙相障礙自殺風險 -> 第二型雙相情緒障礙症患者的自殺死亡率與第一型患者相當或更高，並非較低；且其重鬱症狀通常更頻繁。"
    },
    {
      "question_id": "112-2_medicine-4_065",
      "question_number": 65,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握創傷後壓力症候群的診斷與腦部結構改變。",
      "explanation": "患者經歷嚴重車禍後出現心悸、惡夢、逃避及淡漠等症狀且持續8個月，已超出適應障礙症的時間範圍（通常在壓力源消失後6個月內緩解），最可能的診斷為創傷後壓力症候群（PTSD）。神經科學研究指出，PTSD 患兒或成人的大腦中，與情緒過度活化相關的「杏仁核（amygdala）」在結構與功能上常會出現顯著的改變（如過度活躍），而非頂葉鈣化或基底核受損。",
      "flashcard_front": "車禍倖存 / 惡夢與逃避持續8個月 / 創傷後壓力症候群 (PTSD) / 杏仁核 (amygdala) 改變 / 適應障礙症鑑別",
      "flashcard_back": "車禍後逃避與惡夢持續 8 個月符合 PTSD 診斷；其神經病理主要與大腦「杏仁核」結構與功能的改變相關。",
      "flashcard_summary": "PTSD與杏仁核 -> 車禍後逃避與惡夢持續 8 個月符合 PTSD 診斷；其神經病理主要與大腦「杏仁核」結構與功能的改變相關。"
    },
    {
      "question_id": "112-2_medicine-4_066",
      "question_number": 66,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握抗精神病藥物與抗憂鬱劑對性功能的影響。",
      "explanation": "許多抗憂鬱劑（SNRI/SSRI）易導致低性慾及高潮障礙，此時可合併使用 cyproheptadine 或 amantadine 予以改善；鋰鹽亦可引起勃起功能障礙。而 risperidone（理思必妥）會因阻斷多巴胺 D2 受體而顯著升高泌乳素，導致高泌乳素血症進而降低性慾；bupropion 雖較不影響性功能，但 risperidone 不具備提高性慾的作用。",
      "flashcard_front": "藥物與性功能 / SSRI副作用 / 改善藥物 (cyproheptadine) / 鋰鹽勃起障礙 / risperidone 泌乳素",
      "flashcard_back": "risperidone 因會引致高血乳素血症，易降低（而非提高）性慾；而 bupropion 對性功能副作用最少。",
      "flashcard_summary": "抗精神病藥與性功能 -> risperidone 因會引致高血乳素血症，易降低（而非提高）性慾；而 bupropion 對性功能副作用最少。"
    },
    {
      "question_id": "112-2_medicine-4_067",
      "question_number": 67,
      "correct_answer": "B",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握失智症的流行病學、病程與精神行為症狀（BPSD）盛行率。",
      "explanation": "失智症是一種進行性且不可逆的智能受損，盛行率隨年齡遞增，且老化、家族史及女性為已知危險因子；憂鬱症或甲狀腺低下可呈假性失智表現。然而，在失智症病程中，高達「70%至80%（甚至更多）」的患者在不同階段會出現妄想、幻覺或焦慮等精神行為症狀（BPSD），「大約三分之一」的說法顯著低估了其臨床盛行率。",
      "flashcard_front": "失智症 (Dementia) / 假性失智 / BPSD (精神行為症狀) / 妄想與幻覺盛行率 / 女性危險因子",
      "flashcard_back": "失智症病程中，出現精神行為症狀（如妄想、幻覺）的患者比例高達 70-80%，而非僅有三分之一。",
      "flashcard_summary": "失智症精神症狀盛行率 -> 失智症病程中，出現精神行為症狀（如妄想、幻覺）的患者比例高達 70-80%，而非僅有三分之一。"
    },
    {
      "question_id": "112-2_medicine-4_068",
      "question_number": 68,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握海洛因中毒與戒斷的症狀及藥物治療。",
      "explanation": "海洛因（嗎啡類）急性中毒時，應給予阿片受體拮抗劑 naloxone 進行緊急搶救。嗎啡類物質即使在急性戒斷期結束後，仍可殘存失眠、焦慮等遷延性戒斷症狀達數個月之久。意識混亂、呼吸淺與瞳孔縮小是「海洛因急性中毒」的表徵，而非戒斷症狀（戒斷通常是瞳孔放大、流淚、發冷等）；methadone 和 buprenorphine 用於長期替代維持治療，能有效預防復吸，並非不利於戒除。",
      "flashcard_front": "海洛因中毒 / 針尖樣瞳孔與呼吸抑制 / naloxone / 遷延性戒斷症狀 / 美沙冬 (methadone) 替代治療",
      "flashcard_back": "針尖樣瞳孔及呼吸淺為海洛因「中毒」症狀而非戒斷；戒斷期後長期使用 methadone 能預防復發，有利戒除。",
      "flashcard_summary": "海洛因中毒與戒斷處置 -> 針尖樣瞳孔及呼吸淺為海洛因「中毒」症狀而非戒斷；戒斷期後長期使用 methadone 能預防復發，有利戒除。"
    },
    {
      "question_id": "112-2_medicine-4_069",
      "question_number": 69,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握 K 他命的藥理機轉與濫用臨床表現。",
      "explanation": "K他命（ketamine）是解離性麻醉劑，主要為 NMDA 受體拮抗劑，使用後會產生幻覺與身體解離狀態（dissociative state），其藥理機轉不同於作用在多巴胺的安非他命。K他命亦可透過鼻吸入濫用（非僅注射或口服），且長期或大量使用被證實會導致類似思覺失調症之精神病態與泌尿系統損傷（如出血性膀胱炎）。",
      "flashcard_front": "K他命 (ketamine) / NMDA受體拮抗劑 / 解離狀態與幻覺 / 鼻吸入濫用 / 精神病態",
      "flashcard_back": "K他命為 NMDA 受體拮抗劑，吸食後常產生解離與幻覺，且長期濫用可能導致類似思覺失調的精神症狀。",
      "flashcard_summary": "K他命濫用特徵 -> K他命為 NMDA 受體拮抗劑，吸食後常產生解離與幻覺，且長期濫用可能導致類似思覺失調的精神症狀。"
    },
    {
      "question_id": "112-2_medicine-4_070",
      "question_number": 70,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握 Wernicke 腦病的診斷三聯症與急診處置順序。",
      "explanation": "患者有長期酗酒與營養不良史，突發步態不穩（ataxia）、意識混淆（confusion）及眼球震顫（ophthalmoplegia），為 Wernicke 腦病的典型三聯症。此病是由於維生素 B1（thiamine）缺乏所致，立即處置應是給予靜脈或肌肉注射 thiamine。必須特別注意的是，若未先給予 thiamine 就「直接補充高濃度葡萄糖液」，會加速耗盡體內殘存的維生素 B1，從而誘發或加重病情。",
      "flashcard_front": "長期酗酒 / 步態不穩、意識混淆、眼球震顫 / 預防 Wernicke 腦病 / thiamine (B1) / 葡萄糖注射禁忌",
      "flashcard_back": "酗酒者出現 Wernicke 三聯症，必須立即注射 thiamine；且切忌在注射 thiamine 前先輸注高濃度葡萄糖。",
      "flashcard_summary": "酒精性Wernicke腦病治療 -> 酗酒者出現 Wernicke 三聯症，必須立即注射 thiamine；且切忌在注射 thiamine 前先輸注高濃度葡萄糖。"
    },
    {
      "question_id": "112-2_medicine-4_071",
      "question_number": 71,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握自閉症類群障礙症的語言發育與臨床特徵。",
      "explanation": "自閉症類群障礙症（ASD）在 DSM-5 中，其核心診斷準則已不包含獨立的「語言發展遲緩」（改為社交溝通缺陷及侷限重複行為）。以「你」代「我」是代名詞反轉而非仿說；約僅有 25-30% 左右的患者終生無有用口語（非2/3）。有些年幼的患者具有超強閱讀字詞的能力，但卻對所讀文字的實質社會意義缺乏理解（稱為過度識字 hyperlexia），此為常見的臨床現象。",
      "flashcard_front": "自閉症類群障礙 (ASD) / DSM-5核心準則 / 代名詞反轉與仿說 / 過度識字 (hyperlexia) / 無口語比例",
      "flashcard_back": "語言遲緩非 DSM-5 自閉症核心準則；有些患兒在幼年可能讀很多字卻無法理解含意（過度識字）。",
      "flashcard_summary": "自閉症語言特徵 -> 語言遲緩非 DSM-5 自閉症核心準則；有些患兒在幼年可能讀很多字卻無法理解含意（過度識字）。"
    },
    {
      "question_id": "112-2_medicine-4_072",
      "question_number": 72,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "精神科",
      "category_confidence": "high",
      "key_point": "掌握注意力不足/過動症的神經病因學特徵。",
      "explanation": "注意力不足/過動症（ADHD）主要是一種高度受基因遺傳影響的發育障礙，其遺傳率高達 70% 至 80%（非15%），且診斷以臨床評估為主，結構性腦部造影通常不呈現肉眼可見的粗糙異常。在神經學研究中，前額葉皮質（prefrontal cortex）及基底核環路主要負責執行功能、注意力的維持與衝動的抑制，為 ADHD 最常被探討與證實功能異常的腦區。",
      "flashcard_front": "ADHD 病因 / 遺傳率高達75% / 前額葉皮質 (PFC) / 腦造影診斷價值 / 注意力與衝動控制",
      "flashcard_back": "ADHD 的遺傳率極高且腦結構造影多無肉眼異常；其病理機制主要與前額葉皮質的執行與衝動控制功能異常有關。",
      "flashcard_summary": "ADHD神經病因 -> ADHD 的遺傳率極高且腦結構造影多無肉眼異常；其病理機制主要與前額葉皮質的執行與衝動控制功能異常有關。"
    },
    {
      "question_id": "112-2_medicine-4_073",
      "question_number": 73,
      "correct_answer": "A",
      "category_group": "醫學（四）",
      "category": "醫學倫理與醫療決策",
      "category_confidence": "high",
      "key_point": "掌握精神醫療中約束與隔離的合法醫囑規範。",
      "explanation": "在精神醫療實務中，對病人進行身體約束或隔離是限制人身自由的重大醫療處置，必須有明確的書面醫囑，明訂約束方式與時間，且定期記錄病人狀況，若需延展也必須由醫師再次親自評估。即使在緊急情況下，通常也不得僅以口頭醫囑逕行之（或必須在極短時間內親自評估並補開正式醫囑，不得作為常規授權），以維護病人的人權與醫療安全。",
      "flashcard_front": "精神醫療 / 約束與隔離規範 / 口頭醫囑限制 / 醫囑明確時間 / 定期評估記錄",
      "flashcard_back": "身體約束與隔離必須由醫師親自評估並開立書面醫囑，在情況緊急時，亦不可僅憑口頭醫囑進行而無後續即時評估。",
      "flashcard_summary": "約束與隔離醫囑規範 -> 身體約束與隔離必須由醫師親自評估並開立書面醫囑，在情況緊急時，亦不可僅憑口頭醫囑進行而無後續即時評估。"
    },
    {
      "question_id": "112-2_medicine-4_074",
      "question_number": 74,
      "correct_answer": "D",
      "category_group": "醫學（四）",
      "category": "小兒科",
      "category_confidence": "high",
      "key_point": "掌握股骨頭骨骺滑脫的臨床與治療原則。",
      "explanation": "青少年出現髖關節或膝關節疼痛、跛行，X光片顯示股骨頭沿生長板移位，最可能的診斷為股骨頭骨骺滑脫（Slipped Capital Femoral Epiphysis, SCFE）。SCFE 是一種小兒骨科急症，一旦診斷，必須儘快進行手術以螺釘進行原位固定（in situ pinning），以防進一步滑脫並降低股骨頭缺血性壞死（AVN）的風險，因此「保守治療為主」的敘述錯誤。",
      "flashcard_front": "青少年髖關節痛 / 走路跛行 / 股骨頭骨骺滑脫 (SCFE) / 生長板病變 / 手術固定 vs 保守治療",
      "flashcard_back": "SCFE 好發於肥胖青少年，為防止股骨頭缺血性壞死，一旦確診應「儘快安排手術螺釘固定」，不建議保守治療。",
      "flashcard_summary": "股骨頭骨骺滑脫治療 -> SCFE 好發於肥胖青少年，為防止股骨頭缺血性壞死，一旦確診應「儘快安排手術螺釘固定」，不建議保守治療。"
    },
    {
      "question_id": "112-2_medicine-4_075",
      "question_number": 75,
      "correct_answer": "C",
      "category_group": "醫學（四）",
      "category": "神經科",
      "category_confidence": "high",
      "key_point": "掌握急性缺血性腦中風的影像學檢查與血栓溶解治療指引。",
      "explanation": "急性腦中風病人在急診首選行頭部電腦斷層（CT）檢查，若看到出血（如腦出血、硬腦膜下出血）則為血栓溶解治療（rt-PA）的絕對禁忌症。然而，在缺血性中風的超急性期（發病數小時內），頭部電腦斷層「通常是完全正常的」；此時正常（排除出血）正是可以接受血栓溶解治療的前置必要條件，因此「電腦斷層正常就不需治療」的說法錯誤。",
      "flashcard_front": "急性缺血性中風 / 電腦斷層正常 / 血栓溶解劑 (rt-PA) 指引 / 排除出血 / 早期影像特徵",
      "flashcard_back": "超急性期缺血性中風 CT 常呈現正常；CT 正常（排除出血）為給予 rt-PA 治療之指引，而非不需治療。",
      "flashcard_summary": "中風CT與溶栓指引 -> 超急性期缺血性中風 CT 常呈現正常；CT 正常（排除出血）為給予 rt-PA 治療之指引，而非不需治療。"
    }
  ]
}

# Write files
os.makedirs("reports/gemini_outputs", exist_ok=True)

for i, batch in enumerate([batch_1, batch_2, batch_3, batch_4, batch_5], start=1):
    filename = f"reports/gemini_outputs/112-2_medicine-4_batch-00{i}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(batch, f, indent=2, ensure_ascii=False)
    print(f"Wrote {filename}")

# Validation block
sys.path.append('.')
from validate_all import validate_file

all_ok = True
for i in range(1, 6):
    b = f"112-2_medicine-4_batch-00{i}"
    p_path = f"reports/gemini_prompts/{b}.md"
    o_path = f"reports/gemini_outputs/{b}.json"
    
    res = validate_file(p_path, o_path)
    print(f"Validation for {b}: {res}")
    if res != "OK":
        all_ok = False

if all_ok:
    print("All 5 batches are VALID and correct!")
    sys.exit(0)
else:
    print("Some validation checks FAILED!")
    sys.exit(1)
