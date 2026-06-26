import fs from "fs";
import path from "path";

const examPath = "public/data/exams/112-2/medicine-2.json";
const scratchDir = "scratch";
const allowed = new Set(["微生物免疫學", "寄生蟲學", "藥理學", "病理學", "公共衛生學", "其他"]);

const rows = [
  [1,"微生物免疫學","痲瘋病譜系取決於細胞免疫強弱：類結核型為Th1反應強、lepromin陽性；腫瘤型為細胞免疫差、菌量與傳染力高。","痲瘋病兩型最重要的免疫差異是什麼？","類結核型細胞免疫強、lepromin反應陽性；腫瘤型細胞免疫弱、菌量多、傳染力高，可能出現erythema nodosum leprosum。","類結核型lepromin陽性；腫瘤型傳染力高。","本題問兩型痲瘋病何者最不適當。兩型不是都對lepromin有高度反應，腫瘤型因細胞免疫不足而反應差。",["A錯。只有類結核型常有強烈lepromin反應，腫瘤型通常陰性或低反應。","B對。類結核型以細胞免疫為主，免疫球蛋白量通常正常。","C對。腫瘤型可有免疫複合體相關的結節性紅斑反應。","D對。腫瘤型菌量高，傳染力較類結核型高。"]],
  [2,"微生物免疫學","Klebsiella pneumoniae是乳糖發酵、具莢膜、黏稠菌落的革蘭陰性桿菌，常造成肝膿瘍。","MacConkey粉紅且高度黏稠、肝膿瘍要想到哪種菌？","Klebsiella pneumoniae；粉紅代表乳糖發酵，黏稠代表厚莢膜，與侵襲性肝膿瘍典型相關。","粉紅黏稠MacConkey菌落加肝膿瘍：Klebsiella pneumoniae。","題幹的MacConkey粉紅色表示乳糖發酵，高度黏性表示莢膜明顯；臨床又是肝膿瘍，最符合Klebsiella pneumoniae。",["A錯。E. coli可乳糖發酵，但典型菌落不如Klebsiella黏稠，也非此肝膿瘍線索最佳答案。","B錯。Vibrio vulnificus多與海鮮、海水傷口、敗血症相關，不是典型黏稠乳糖發酵菌落。","C錯。Vibrio cholerae以水瀉與TCBS培養特徵為主。","D對。Klebsiella pneumoniae具厚莢膜、黏稠菌落，常見於肝膿瘍。"]],
  [3,"微生物免疫學","Fluoroquinolone抗藥性常來自DNA gyrase gyrA或topoisomerase IV突變。","gyrA突變會降低哪類抗生素敏感性？","Ciprofloxacin等fluoroquinolones作用於DNA gyrase/topoisomerase IV；gyrA突變會造成抗藥性。","gyrA突變：fluoroquinolone抗藥性。","gyrase A次單元是fluoroquinolone重要作用標的；突變會降低ciprofloxacin敏感性。",["A對。Ciprofloxacin屬fluoroquinolone，作用於DNA gyrase。","B錯。Ampicillin作用於細胞壁PBP，與gyrA無直接關係。","C錯。Cephalosporin也是β-lactam，標的是細胞壁合成。","D錯。Clindamycin作用於50S核糖體。"]],
  [4,"微生物免疫學","革蘭陰性菌抗藥性常靠酵素分解、標的突變、通透性下降與外排幫浦；形成內孢子不是常見機制。","革蘭陰性菌抗藥性常見機制有哪些？","β-lactamase、標的改變、porin改變、efflux pump常見；內孢子形成主要見於Bacillus與Clostridium，不是革蘭陰性菌典型抗藥性機制。","抗藥性常見：酵素、標的、外排；內孢子不是革蘭陰性菌典型。","題目問通常與革蘭陰性菌抗藥性無關者；革蘭陰性菌一般不靠形成內孢子逃避抗生素。",["A對但非答案。β-lactamase等酵素可破壞抗生素。","B對但非答案。標的突變可使藥物無法結合。","C對但非答案。外排幫浦可降低菌體內藥物濃度。","D為答案。內孢子形成不是革蘭陰性菌通常的抗藥性機制。"]],
  [5,"微生物免疫學","Legionella需以buffered charcoal yeast extract agar培養，常加L-cysteine與鐵。","分離Legionella最適合培養基？","BCYE agar；charcoal吸附毒性物質，yeast extract、L-cysteine與鐵支持退伍軍人菌生長。","Legionella培養：BCYE agar。","退伍軍人菌需特殊營養，經典培養基是buffered charcoal yeast extract agar。",["A對。BCYE agar是Legionella標準培養基。","B錯。Caffeic acid agar常用於Cryptococcus鑑別。","C錯。Regan-Lowe agar用於Bordetella pertussis。","D錯。Cystine-tellurite agar用於Corynebacterium diphtheriae。"]],
  [6,"微生物免疫學","金黃色葡萄球菌食物中毒是預形成耐熱腸毒素造成，潛伏期短，常約1至6小時。","金黃色葡萄球菌食物中毒的時間特徵？","預形成耐熱毒素造成快速嘔吐與腹痛，平均約4小時發作，通常支持治療即可。","預形成S. aureus腸毒素：潛伏期短、約4小時。","題幹問最適當敘述；S. aureus腸毒素已在食物中形成，所以潛伏期很短。",["A錯。腸毒素具耐熱性，加熱後仍可能致病。","B錯。主要是毒素型疾病，通常不需大量抗生素。","C對。平均約4小時符合預形成毒素食物中毒。","D錯。症狀多在24小時左右緩解，不常持續4至5天。"]],
  [7,"微生物免疫學","常見性傳染菌包含Neisseria gonorrhoeae、Treponema pallidum、Chlamydia trachomatis；Listeria主要經食物傳播。","哪種菌最不可能經性行為傳染？","Listeria monocytogenes多由污染食物傳播，孕婦、新生兒、老人與免疫低下者風險高。","Listeria是食媒菌，不是典型性傳染病。","題目列出典型性病菌與非性病菌；Listeria主要與未殺菌乳製品、熟食肉品等食物相關。",["A錯。淋病雙球菌是典型性傳染病原。","B錯。梅毒螺旋體主要經性接觸傳播。","C錯。砂眼披衣菌是常見性傳染病原。","D對。Listeria主要經食物傳播，非典型性傳染菌。"]],
  [8,"微生物免疫學","有氧呼吸通常產生ATP最多；無氧呼吸可用非氧終端電子接受者，產能低於有氧呼吸。","細菌有氧與無氧呼吸何者產能較高？","有氧呼吸以氧作終端電子接受者，能量產生通常最高；細菌電子傳遞鏈位於細胞膜。","有氧呼吸ATP通常多於無氧呼吸與發酵。","題目問最不適當敘述；無氧呼吸通常不會比有氧呼吸產生更多ATP。",["A對。有氧呼吸比發酵產生更多ATP。","B對。細菌沒有粒線體，電子傳遞鏈在細胞膜。","C對。兼性厭氧菌可依環境進行有氧或無氧代謝。","D錯。無氧呼吸產能通常低於有氧呼吸。"]],
  [9,"微生物免疫學","Clostridium septicum是厭氧、產芽孢桿菌，與非外傷性肌壞死及潛在大腸癌相關。","Clostridium septicum的臨床聯想？","C. septicum與自發性氣性壞疽、非外傷性肌壞死和潛藏性大腸癌有關，為厭氧菌。","C. septicum：非外傷性肌壞死加潛在大腸癌。","題目問不是其特徵；Clostridium屬厭氧菌，說對氧氣有耐受性不恰當。",["A為答案。C. septicum是厭氧菌，不以耐氧為典型特徵。","B對。與潛藏性大腸癌有重要關聯。","C對。血液瓊脂可見擴散性生長。","D對。可造成非外傷性肌肉壞死。"]],
  [10,"微生物免疫學","RNA病毒缺乏高保真校正能力，突變率通常高於DNA病毒。","RNA病毒為何容易變異？","RNA依賴性聚合酶校正能力差，所以複製錯誤率高；但並非所有RNA病毒都只在細胞質複製。","RNA病毒突變率高於DNA病毒。","題目問最適當敘述；RNA病毒基因體複製錯誤率通常高，是抗原變異的重要原因。",["A對。RNA病毒複製錯誤率通常較高。","B錯。病毒增殖以一次產生多個子代的burst為特徵，不是單純等比級數。","C錯。無套膜腸病毒環境耐受性通常比有套膜流感病毒強。","D錯。流感病毒等RNA病毒需在細胞核內完成部分複製步驟。"]],
  [11,"微生物免疫學","病毒感染的全身類感冒症狀常由第一型干擾素與發炎細胞激素造成。","病毒感染造成類感冒全身症狀的主要因子？","干擾素可誘發發燒、倦怠、肌痛等全身症狀，也是抗病毒先天免疫重要分子。","類感冒症狀：想到干擾素。","題目問最可能引發flu-like systemic symptom的因子；干擾素最符合。",["A錯。T細胞參與清除感染，但不是典型類感冒症狀的主要可溶性因子。","B對。干擾素可造成發燒、肌痛、疲倦等症狀。","C錯。抗體以中和與清除病毒為主。","D錯。免疫複合物可造成第三型過敏，非本題主軸。"]],
  [12,"微生物免疫學","Hantavirus屬Bunyavirales，為分節負股RNA病毒，主要以鼠類排泄物傳播。","漢他病毒的主要媒介？","漢他病毒主要儲存在鼠類，人體常因吸入含病毒的鼠尿、糞、唾液氣溶膠感染。","Hantavirus：鼠類媒介，負股分節RNA。","Bunyaviridae相關病毒多為負股分節RNA；漢他病毒的關鍵傳播線索是老鼠。",["A錯。布尼亞病毒多為負股RNA，不是正股RNA。","B不選。部分布尼亞病毒在細胞質複製；核內複製不是本題最適當敘述。","C對。Hantavirus主要以老鼠為宿主與傳播來源。","D錯。漢他病毒通常不是以人傳人為主要模式。"]],
  [13,"微生物免疫學","EBV與傳染性單核球增多症、鼻咽癌、Burkitt lymphoma及口腔毛狀白斑相關；先天性聽損典型為CMV。","哪個疾病與EBV較無關？","新生兒先天性聽力受損最典型與巨細胞病毒感染有關，不是EBV典型疾病。","先天性聽損：CMV；EBV：mono、鼻咽癌、毛狀白斑。","題目問與EBV較無關者；先天性聽力受損應想到CMV。",["A錯。AIDS患者口腔毛狀白斑與EBV相關。","B對。先天性聽損較典型是CMV。","C錯。鼻咽癌與EBV關聯強。","D錯。傳染性單核球增多症典型由EBV造成。"]],
  [14,"微生物免疫學","Retrovirus反轉錄後整合成provirus，但整合位置可變，不限固定染色體位置。","反轉錄病毒provirus的整合特性？","Provirus會整合入宿主基因體，但整合位置並非固定；病毒顆粒含reverse transcriptase與兩套單股RNA。","Retrovirus整合位置可變。","題目問最不適當；provirus不是只出現在固定染色體位置。",["A錯，為答案。反轉錄病毒整合位置可變。","B對。反轉錄可利用宿主tRNA作primer。","C對。顆粒內有兩套正股單股RNA。","D對。病毒顆粒帶有reverse transcriptase。"]],
  [15,"微生物免疫學","新病毒親緣關係主要靠核酸序列比對判定。","SARS-CoV-2最初如何被認定接近蝙蝠冠狀病毒？","藉由病人檢體病毒基因序列與已知蝙蝠冠狀病毒序列高度相似，推論其親緣關係。","病毒來源與親緣：看基因序列相似度。","題目問鑑定方式；現代病毒分類與親緣推斷以核酸序列最有力。",["A錯。電子顯微鏡只能看冠狀病毒形態，不能精準判定親緣。","B對。序列高度相似是判定接近蝙蝠冠狀病毒的依據。","C錯。臨床症狀缺乏病毒分類特異性。","D錯。抗體交叉反應不是最初鑑定親緣的主要證據。"]],
  [16,"微生物免疫學","Echinocandin抑制真菌細胞壁β-1,3-glucan合成；azole、allylamine、polyene都以ergosterol路徑或膜為主。","哪類抗黴菌藥作用部位不同？","Echinocandin作用於細胞壁；triazole與allylamine抑制ergosterol合成，polyene結合ergosterol。","Echinocandin打細胞壁，其他多打ergosterol。","題目比較作用部位；只有棘白菌素主要作用在真菌細胞壁。",["A錯。Triazole抑制ergosterol合成。","B對。Echinocandin抑制β-glucan細胞壁合成。","C錯。Allylamine抑制squalene epoxidase，屬ergosterol路徑。","D錯。Polyene結合ergosterol破壞細胞膜。"]],
  [17,"微生物免疫學","Rhodotorula可產生類胡蘿蔔素，形成粉紅至紅色酵母菌落。","粉紅至紅色酵母菌落想到誰？","Rhodotorula spp.因carotenoid pigments而呈粉紅或紅色。","Rhodotorula：紅色類胡蘿蔔素。","題目問合成carotenoid pigments者；Rhodotorula是典型紅色酵母。",["A錯。Trichosporon較以關節分生孢子等特徵著名。","B對。Rhodotorula會產生粉紅至紅色色素。","C錯。Cryptococcus典型有莢膜，非紅色色素重點。","D錯。Malassezia為脂質依賴酵母，與花斑癬等相關。"]],
  [18,"微生物免疫學","周邊免疫器官包括淋巴結、脾臟、扁桃腺；胸腺是中樞免疫器官。","哪個不是周邊免疫器官？","Thymus負責T細胞成熟，是初級/中樞免疫器官，不屬周邊免疫組織。","胸腺是中樞免疫器官。","題目問人體模型介紹周邊免疫組織時的錯誤示範；指胸腺錯。",["A錯。扁桃腺屬黏膜相關周邊淋巴組織。","B錯。淋巴結是周邊免疫器官。","C錯。脾臟是周邊免疫器官。","D對。胸腺是中樞免疫器官。"]],
  [19,"微生物免疫學","Defensin是陽離子抗菌胜肽，可直接破壞微生物細胞膜。","哪個先天免疫分子直接破壞細胞膜？","Defensin可插入並破壞病原菌膜，達到快速殺菌效果。","Defensin直接破壞菌膜。","題目問直接破壞細胞膜者；defensin最符合抗菌胜肽機制。",["A錯。Cytokine主要調節免疫反應。","B錯。CRP主要作為急性期蛋白與調理素。","C錯。TLR是模式辨識受體，負責偵測病原分子。","D對。Defensin可直接破壞微生物膜。"]],
  [20,"微生物免疫學","TCR的CDR3由V(D)J接合形成，變異度最大，最直接接觸抗原胜肽。","TCR哪個CDR變異最大？","CDR3位於V(D)J接合區，接合多樣性最高，是抗原辨識差異的核心。","TCR CDR3變異最大。","題目問最大變異度；CDR3因接合多樣性而最具變異。",["A錯。CDR1有變異但不如CDR3。","B錯。CDR2也參與辨識，但變異度不是最大。","C對。CDR3變異最大。","D錯。典型抗原結合區討論CDR1至CDR3，CDR4不是標準答案。"]],
  [21,"微生物免疫學","膜上BCR的Fab可辨識抗原，但膜型BCR本身的Fc不執行分泌抗體的效應功能。","BCR與抗體功能差異的陷阱？","BCR是膜型免疫球蛋白，主要負責抗原辨識與訊號傳遞；分泌型抗體的Fc才典型執行補體、Fc受體等效應功能。","膜型BCR不等同分泌抗體的Fc效應。","題目問錯誤敘述；把BCR表面抗體的Fc直接說成可活化各種效應功能是不精確的。",["A對。TCR與BCR都有變異區與固定區，抗原結合在變異區。","B對。TCR一個結合位且只膜上；BCR可膜上或分泌成抗體。","C錯，為答案。BCR主要傳遞訊號，Fc效應是分泌抗體結合Fc受體或補體後的功能。","D對。TCR需同時辨識MHC與抗原胜肽。"]],
  [22,"微生物免疫學","Fingolimod是S1P receptor功能性拮抗劑，使淋巴球滯留於淋巴結，減少進入中樞神經。","Fingolimod治療多發性硬化症機轉？","FTY720調節S1PR1，使T淋巴球無法有效離開淋巴結，降低自體免疫攻擊。","Fingolimod：S1P receptor調節，淋巴球困在淋巴結。","題幹問FTY720免疫調節機轉；核心是S1P/S1PR1淋巴球遷移路徑。",["A錯。不是主要阻斷ADCC。","B錯。減少IL-2是calcineurin抑制劑等概念。","C錯。IL-6 receptor/JAK-STAT不是fingolimod主要標的。","D對。競爭/調節S1PR1，使淋巴球遷移受阻。"]],
  [23,"微生物免疫學","抗體中和作用由Fab結合抗原完成；Fc負責補體活化、調理、Fc受體結合與肥大細胞去顆粒等。","抗體中和作用屬Fab還是Fc功能？","Neutralization靠Fab擋住毒素或病毒與宿主結合，不是Fc部分的功能。","中和靠Fab；補體、調理、去顆粒靠Fc。","題目問不是Fc功能者；中和作用來自抗原結合部位Fab。",["A錯。Fc可活化補體。","B對。中和是Fab功能。","C錯。Fc可透過Fc受體促進調理吞噬。","D錯。IgE的Fc結合mast cell Fcε receptor可促進去顆粒。"]],
  [24,"微生物免疫學","Oral tolerance與腸道誘導調節性T細胞、TGF-β等免疫抑制環境有關。","口服耐受的免疫機轉？","腸道抗原可誘導Treg與分泌TGF-β的T細胞反應，降低對食物抗原的免疫攻擊。","Oral tolerance：Treg/TGF-β。","題目問正確敘述；口服耐受不是單靠食物被消化，而是主動免疫調節。",["A錯。消化成小分子不是oral tolerance的主要免疫機制。","B錯。食物胜肽不是主要在胸腺刪除相關T細胞。","C錯。並非所有食物都必然引發耐受。","D對。TGF-β相關調節性T細胞參與口服耐受。"]],
  [25,"微生物免疫學","衛生假說認為嬰幼兒早期微生物暴露不足，可能增加Th2偏向與第一型過敏風險。","第一型過敏與衛生假說的關聯？","過度乾淨環境使早期感染與微生物刺激不足，可能促進IgE/Th2型過敏疾病。","過度乾淨成長環境：第一型過敏風險較高。","題目問與第一型過敏最相關情況；嬰幼兒時期過度乾淨符合衛生假說。",["A對。過度乾淨環境與過敏風險上升相關。","B錯。早期細菌感染反而可能降低過敏傾向。","C錯。某些病毒感染史不如衛生假說線索直接。","D錯。第一型過敏主要與IgE，不是高濃度IgG2a。"]],
  [26,"微生物免疫學","TLR9辨識未甲基化CpG DNA；SLE抗dsDNA相關核酸免疫活化常牽涉TLR9。","anti-dsDNA相關SLE主要活化哪個TLR？","含DNA的免疫複合物可進入內體並活化TLR9，促進自體免疫發炎。","DNA對應TLR9；RNA對應TLR7/8。","題目問dsDNA自體抗體相關機轉；DNA核酸感知受體是TLR9。",["A錯。TLR1多與TLR2配對辨識細菌脂蛋白。","B錯。TLR4典型辨識LPS。","C錯。TLR7偏向辨識單股RNA。","D對。TLR9辨識DNA CpG訊號。"]],
  [27,"微生物免疫學","慢性移植排斥以血管內膜增生、纖維化、管腔狹窄與慢性缺血為特徵。","慢性排斥的典型病理？","長期免疫傷害造成小血管內皮受損、內膜增厚與硬化，植體逐漸缺血萎縮。","慢性排斥：血管硬化與缺血。","題目問最可能出現情況；慢性排斥重點是血管病變與纖維化。",["A錯。NK細胞急性進入破壞不是慢性排斥典型描述。","B對。小血管內皮損傷、浸潤、硬化與植體缺血符合慢性排斥。","C錯。血型抗體造成超急性排斥，植體黑紫腫脹。","D錯。突變植體抗原不是慢性排斥的一般機制。"]],
  [28,"微生物免疫學","CTLA-4與CD28競爭結合抗原呈現細胞上的CD80/CD86；阻斷CTLA-4可增強T細胞活化。","Anti-CTLA-4免疫治療的標的互動？","CTLA-4是T細胞抑制性檢查點，結合樹突細胞CD80/CD86後抑制共刺激；抗CTLA-4解除煞車。","CTLA-4結合CD80/CD86。","題目問anti-CTLA-4原理；關鍵是CTLA-4與APC上的B7分子CD80/CD86結合。",["A錯。CTLA-4不結合MHC。","B錯。PD-1與PD-L1/PD-L2互動，不是CTLA-4的配體。","C對。CTLA-4結合CD80/CD86。","D錯。CD11b不是CTLA-4主要配體。"]],
  [29,"寄生蟲學","Toxocara、Angiostrongylus、Loa loa可造成眼部病變；Anisakis主要侵犯胃腸道。","哪種寄生蟲最不可能造成眼病變？","海獸胃線蟲常因食入生食海魚造成胃腸道anisakiasis，不是典型眼部寄生蟲病。","Anisakis主要胃腸道，不典型眼病變。","題目問最不可能引起眼睛病變者；Anisakis以胃腸症狀為主。",["A錯。犬蛔蟲可造成眼幼蟲移行症。","B錯。廣東住血線蟲可侵犯中樞神經並可能有眼部侵犯。","C錯。Loa loa成蟲可移行通過結膜。","D對。Anisakis主要造成胃腸道病變。"]],
  [30,"寄生蟲學","鉤蟲幼蟲可造成皮膚爬行疹；東方毛線蟲主要經食入感染，造成腸道寄生。","手腳污泥後延伸紅斑搔癢最不支持哪個感染？","延伸性紅斑與搔癢符合皮膚幼蟲移行症/鉤蟲爬行疹；Trichostrongylus orientalis不是典型皮膚爬行疹。","爬行疹想到鉤蟲幼蟲，不是東方毛線蟲。","題目問最不適當敘述；東方毛線蟲感染主要是腸道線蟲病，與皮膚延伸紅斑不符。",["A對但非答案。寄生蟲可誘發過敏性搔癢。","B對但非答案。抓破皮可能續發細菌感染。","C錯，為答案。東方毛線蟲不是典型造成爬行疹的病原。","D對但非答案。鉤蟲幼蟲可造成creeping eruption。"]],
  [31,"寄生蟲學","Schistosoma haematobium寄生膀胱靜脈叢，卵有末端棘，與膀胱鱗狀細胞癌相關，治療用praziquantel。","埃及血吸蟲的重要併發症？","S. haematobium造成泌尿道血吸蟲病，慢性發炎可增加膀胱癌風險。","S. haematobium：膀胱癌、末端棘、praziquantel。","題目問正確敘述；埃及血吸蟲與非洲膀胱癌有明確關聯。",["A錯。S. haematobium卵為末端棘，不是側棘；側棘是S. mansoni。","B錯。下腸繫膜靜脈叢較符合S. mansoni。","C對。慢性感染可導致膀胱癌。","D錯。治療首選為praziquantel，不是metronidazole。"]],
  [32,"寄生蟲學","Toxoplasma感染多無症狀或類感冒；慢性可形成組織囊體，急性大量腹水不是典型表現。","弓蟲症哪個敘述錯誤？","弓蟲急性感染不以大量腹水為典型；免疫低下者可有腦炎，先天感染可有嚴重神經眼部病變。","弓蟲急性感染不典型大量腹水。","題目問錯誤敘述；大量腹水不是弓蟲急性感染典型臨床。",["A對。食入含bradyzoite的肉類可造成腸道外期感染。","B對。免疫正常者常無症狀或類感冒。","C錯，為答案。急性感染大量腹水不典型。","D對。慢性感染可於中樞形成囊體並在免疫低下時造成腦炎。"]],
  [33,"寄生蟲學","Naegleria fowleri造成原發性阿米巴腦膜腦炎，進展迅速、死亡率高，常數日內死亡。","PAM的病程特徵？","原發性阿米巴腦膜腦炎急性猛烈，若未早期治療，常在症狀後3至6天死亡。","Naegleria PAM：急速致死。","題目問最正確；PAM的關鍵是游泳淡水暴露後急性腦膜腦炎與快速死亡。",["A錯。自由生活阿米巴腦部感染不全都與游泳相關，Acanthamoeba可經其他途徑。","B錯。Naegleria組織中主要見滋養體，囊體不典型。","C對。PAM常在3至6天內死亡。","D錯。Acanthamoeba keratitis不一定都需角膜移植。"]],
  [34,"寄生蟲學","塵蟎是兒童過敏性鼻炎與氣喘的重要室內過敏原來源。","兒童過敏與氣喘主要節肢動物過敏原？","Dust mite糞便與身體成分可誘發IgE媒介過敏反應，是氣喘重要致敏原。","兒童氣喘過敏原：塵蟎。","題目問已確認可導致兒童過敏及氣喘的主要致敏原；塵蟎最典型。",["A錯。疥蟎造成疥瘡，不是兒童氣喘主要過敏原。","B對。塵蟎是重要室內過敏原。","C錯。毛囊蟎與氣喘主因關聯不如塵蟎。","D錯。恙蟎叮咬與恙蟲病相關，非主要氣喘過敏原。"]],
  [35,"微生物免疫學","美國東部蜱叮咬後發燒、白血球與血小板低下、嗜中性球內morula提示人類粒細胞型無形體/艾利希體感染。","蜱媒介且中性球內見菌體要想到什麼？","Ehrlichiosis/anaplasmosis可見白血球內morula，臨床有發燒、頭痛、白血球低下與血小板低下。","蜱叮咬加白血球內morula：Ehrlichia/Anaplasma。","題幹有美國東部、蟲咬、發燒、白血球與血小板低下、嗜中性球內菌體，最符合人艾利希體症。",["A錯。Babesiosis侵犯紅血球，可見Maltese cross。","B對。人艾利希體症可由蜱傳播並見白血球內morula。","C錯。Lyme disease典型游走性紅斑、關節炎、神經心臟表現。","D錯。Bartonellosis常與貓抓病等相關，不是此血抹片線索。"]],
  [36,"公共衛生學","兩組平均數比較的樣本數隨標準差與檢定力增加而增加，隨效應值與型一誤差容許增加而減少。","RCT樣本數何時會增加？","變異越大越難偵測差異，因此預期標準差由12增至16會增加所需樣本數。","標準差增加，樣本數增加。","題目問其他條件不變何者使樣本數增加；標準差增加會降低訊噪比，需要更多樣本。",["A錯。型一誤差由0.05放寬到0.1會降低樣本數。","B錯。效應值變大較容易偵測，樣本數下降。","C對。標準差增加會增加樣本數。","D錯。檢定力由0.9降至0.85會降低樣本數需求。"]],
  [37,"公共衛生學","粗率受人口年齡結構影響；若甲粗發生率高但年齡標準化率低，常代表甲人口較老。","粗率高但年齡標準化率低代表什麼？","甲地老年人口比例高會拉高粗發生率；校正年齡後反而低於乙地，表示危險不一定較高。","粗率受年齡結構影響。","題目比較粗發生率與年齡標準化率；差異方向提示人口老化造成粗率偏高。",["A錯。標準化後甲較低，不支持危險因子更多。","B錯。發生率不能直接推死亡分率。","C對。甲地人口老化可使粗發生率偏高。","D錯。發生率資料不能直接推盛行率。"]],
  [38,"公共衛生學","Pearson相關係數描述兩變項線性相關方向與強度，不代表因果，範圍為-1到+1。","相關係數0.8代表什麼？","0.8表示強正線性相關，但不能推出X造成Y。","相關不等於因果；r看線性相關。","題目問最恰當敘述；相關係數衡量線性相關程度。",["A錯。0.8為正相關，X大時Y傾向也大。","B錯。相關不代表因果。","C錯。相關係數最小可到-1。","D對。相關係數描述線性相關程度。"]],
  [39,"公共衛生學","嬰兒死亡率常作為國家健康水平、醫療照護與公共衛生狀況的綜合指標。","評估國家健康水平常用哪個指標？","嬰兒死亡率對環境、醫療、營養、母嬰照護敏感，因此常用於國際健康比較。","國家健康水平常用嬰兒死亡率。","題目問公共衛生常用健康水平指標；嬰兒死亡率最典型。",["A錯。流產率不是整體健康水平最常用指標。","B對。嬰兒死亡率是常用公共衛生指標。","C錯。總生育率主要反映人口生育行為。","D錯。離婚率非健康水平指標。"]],
  [40,"公共衛生學","腎臟因高血流、濃縮尿液與主動運輸而易受毒物傷害；排尿路上皮也可能受排泄毒物影響。","腎臟毒性為何常見？","腎臟過濾並濃縮外來物，腎小管與泌尿道皆可能接觸高濃度毒物。","毒物經尿排出仍可能傷害泌尿道。","題目問最不恰當；化學物經尿排出仍可能影響輸尿管、膀胱、尿道。",["A對。腎臟相對血流量大，暴露量高。","B對。鎘、汞可造成腎小管傷害。","C對。濃縮作用會提高毒物局部濃度。","D錯，為答案。尿路仍會接觸毒物並可能受害。"]],
  [41,"公共衛生學","長期砷暴露常以毛髮、指甲或尿中砷評估；血砷較反映近期暴露。","長期砷暴露用什麼生物指標較好？","血中砷半衰期較短，不適合作長期暴露指標；毛髮與指甲可反映較長期暴露。","長期砷暴露：毛髮/指甲優於血液。","題目問最不恰當；說血中砷比毛髮適合長期指標是錯的。",["A對。半導體與光電產業可有砷化物職業暴露。","B對。煉銅廠周遭可能有環境砷暴露。","C錯，為答案。長期暴露不宜用血砷優先於毛髮砷。","D對。砷暴露增加肺癌及皮膚、膀胱等癌症風險。"]],
  [42,"公共衛生學","加氯消毒有效且可有餘氯保護，但會與有機物形成三鹵甲烷等鹵化消毒副產物。","飲水加氯最大缺點？","氯與水中天然有機物反應可產生鹵化有機物，帶來潛在健康風險。","加氯缺點：鹵化消毒副產物。","題目問最主要缺點；生成鹵化有機物是飲水加氯的重要限制。",["A錯。加氯相對便宜。","B錯。加氯處理不算最費時。","C錯。餘氯反而可對管線再污染提供一定保護。","D對。會產生鹵化有機物等副產物。"]],
  [43,"公共衛生學","有機磷抑制乙醯膽鹼酯酶，使血中膽鹼酯酶活性下降並造成膽鹼性症候群。","血中膽鹼酯酶下降想到哪種暴露？","有機磷農藥會抑制AChE，檢測膽鹼酯酶活性可作為暴露與中毒指標。","有機磷：膽鹼酯酶下降。","題目問最可能危害物；有機磷是標準答案。",["A錯。四氯化碳主要肝毒性。","B錯。二甲基甲醯胺主要肝毒性與職業暴露。","C錯。鉻酸與皮膚、呼吸道及癌症風險相關。","D對。有機磷抑制膽鹼酯酶。"]],
  [44,"公共衛生學","1848年Public Health Act是英國公共衛生史的重要里程碑。","1848年公共衛生法是哪個國家？","英國在工業化與都市衛生問題背景下制定Public Health Act，推動公共衛生行政。","1848 Public Health Act：英國。","題目問歷史發展；1848年公共衛生法屬英國。",["A錯。不是日本。","B錯。不是美國。","C對。英國於1848年訂定Public Health Act。","D錯。不是德國。"]],
  [45,"公共衛生學","群體取向是降低整體族群風險分布；找出高風險個體並治療屬個體取向。","群體取向與個體取向差異？","全體減鹽、增加戶外活動、菸害廣告管制都是改變群體暴露；治療高血脂病人是高風險個體策略。","找高血脂治療是個體取向，不是群體取向。","題目問群體取向中最不恰當者；B是個體取向。",["A對。降低全民鹽攝取是群體取向。","B錯，為答案。找高血脂病人治療是個體取向。","C對。增加學童戶外活動改變群體暴露。","D對。禁止菸品廣告屬政策性群體取向。"]],
  [46,"藥理學","耐受性是反覆用藥後同劑量效果下降，需增加劑量才達到原效果。","反覆用安非他命後需加量稱為什麼？","同一劑量反應變弱、需更高劑量達相同效果，定義為tolerance。","需加量才有效：耐受性。","題目描述一再服用後對效用產生抗拒、需增加劑量，正是耐受性。",["A錯。重覆性不是成癮藥理的標準核心名詞。","B對。耐受性符合需加量的描述。","C錯。戒斷是停藥或減量後出現不適。","D錯。強化是藥物增加再次使用行為的特性。"]],
  [47,"公共衛生學","醫藥分業強調醫師診療開方、藥事人員調劑；醫師交付藥劑不等同藥師調劑權。","醫藥分業哪個說法不恰當？","醫師在急迫或偏鄉等例外可交付藥品，但不能把醫師法交付藥劑直接等同藥事法調劑。","交付藥劑不等同調劑。","題目問最不恰當；D混淆醫師交付藥劑與藥事法調劑。",["A對。急迫情形或無藥事人員地區可有例外。","B對。醫藥分業原則是醫師診療開方、不調劑。","C對。藥事人員調劑需符合優良調劑作業。","D錯，為答案。交付藥劑不應等同調劑法源。"]],
  [48,"公共衛生學","第二段預防是早期發現、早期治療，常以篩檢為代表。","呼吸道疾病第二段預防例子？","對無症狀者做胸部X光檢查屬篩檢，目的在早期發現疾病。","第二段預防：篩檢。","題目問第二段預防；無症狀者胸部X光篩檢最符合。",["A錯。均衡飲食運動屬初段預防/健康促進。","B錯。不吸菸戒菸屬初段預防。","C對。無症狀胸部X光是篩檢，屬第二段預防。","D錯。接種卡介苗屬初段預防。"]],
  [49,"公共衛生學","可接受性評估服務是否可近、可用，以及民眾是否願意接受與理解服務。","衛生服務可近性、可用性與民眾認知屬哪項準則？","可接受性涵蓋服務對象對服務的接受程度、文化適切性、可近性與可用性。","可近、可用、民眾認知：可接受性。","題目問評估準則；敘述最符合可接受性。",["A錯。合法性著重符合法規與政策授權。","B對。可接受性包含可近性、可用性與民眾認知。","C錯。重要性是問題嚴重度與優先順序。","D錯。充分性偏向資源或服務量是否足夠。"]],
  [50,"公共衛生學","人口分布、組成、數量是某一時間點的靜態描述；人口推估是對未來人口的預測。","哪個不是時間點人口描述指標？","人口推估利用模型推測未來人口變化，不是單一時間點觀察所得的靜態指標。","人口推估不是時間點觀察指標。","題目問不是此類型者；人口推估屬預測。",["A錯。人口分布可在某時間點描述。","B對。人口推估是未來預測。","C錯。人口組成可由某時間點資料描述。","D錯。人口數量是典型時間點指標。"]],
  [51,"藥理學","靜脈注射直接進入全身循環，生體可用率定義上為100%。","哪種給藥生體可用率最高？","IV給藥避開吸收與首渡代謝，bioavailability最高。","IV bioavailability = 100%。","題目問最高生體可用率；靜脈注射是基準。",["A錯。口服受吸收與首渡代謝影響。","B錯。直腸給藥部分避開首渡，但不如IV穩定。","C錯。吸入可很快，但全身生體可用率不一定最高。","D對。靜脈注射生體可用率100%。"]],
  [52,"藥理學","Ceftazidime與cefoperazone具抗Pseudomonas活性；cephalexin偏第一代，cefuroxime可涵蓋H. influenzae。","哪個cephalosporin敘述錯誤？","說cefoperazone與ceftazidime都不能治Pseudomonas是錯的，兩者皆具抗綠膿桿菌活性。","Ceftazidime/cefoperazone可抗Pseudomonas。","題目問錯誤敘述；第三代中ceftazidime、cefoperazone常被記為抗綠膿。",["A對。Cephalexin第一代，對綠膿差，偏革蘭陽性。","B對。Cefuroxime可用於H. influenzae等感染。","C錯，為答案。Ceftazidime與cefoperazone有抗Pseudomonas活性。","D對。Enterobacter易誘導AmpC抗藥，ceftriaxone需避免。"]],
  [53,"藥理學","Doxorubicin為anthracycline，主要抑制topoisomerase II並產生自由基，心毒性重要。","Doxorubicin抑制哪個topoisomerase？","Doxorubicin抑制topoisomerase II，不是topoisomerase I；心肌自由基傷害可致擴張型心肌病變。","Doxorubicin：Topo II、自由基心毒性。","題目問錯誤敘述；把doxorubicin說成抑制topoisomerase I錯，Topo I是irinotecan/topotecan。",["A對。屬抗腫瘤抗生素/anthracycline。","B錯，為答案。其主要抑制topoisomerase II。","C對。自由基造成心臟毒性。","D對。屬細胞週期非專一性藥物。"]],
  [54,"藥理學","Bleomycin是抗腫瘤抗生素，可造成DNA strand breaks，主要用於癌症治療。","哪個抗生素主要作抗癌藥？","Bleomycin可抑制DNA合成並造成斷裂，臨床用於睪丸癌、淋巴瘤等。","Bleomycin是抗癌抗生素。","題目問可抑制癌細胞週期且主要作抗癌者；bleomycin符合。",["A對。Bleomycin是抗癌藥。","B錯。Gentamicin是aminoglycoside抗菌藥。","C錯。Telithromycin是ketolide抗菌藥。","D錯。Daptomycin是抗革蘭陽性菌藥。"]],
  [55,"藥理學","Cyclophosphamide是前驅藥，需肝臟CYP450活化後形成烷化代謝物。","Cyclophosphamide為何需代謝活化？","經CYP450形成phosphoramide mustard後才能烷化DNA；副產物acrolein與出血性膀胱炎相關。","Cyclophosphamide需CYP450活化才烷化DNA。","題目問正確敘述；cyclophosphamide須經肝臟氧化活化。",["A錯。Azathioprine是6-MP前驅藥，屬免疫抑制，不是免疫增強。","B錯。CHOP的C是cyclophosphamide，不是cisplatin。","C對。需CYP450代謝後才具DNA alkylating作用。","D錯。Methotrexate抑制dihydrofolate reductase。"]],
  [56,"藥理學","Cyclosporine抑制calcineurin，降低NFAT活化與IL-2轉錄；主要毒性包括腎毒性與高血壓。","Cyclosporine主要降低哪個細胞激素？","Cyclosporine抑制T細胞IL-2產生；不是主要減少IL-1。","Cyclosporine：calcineurin-NFAT-IL-2下降。","題目問錯誤敘述；cyclosporine的核心是IL-2，不是IL-1。",["A對。抑制calcineurin活性。","B對。使NF-AT無法有效進入細胞核轉錄。","C錯，為答案。主要減少IL-2產生。","D對。腎毒性與高血壓是重要副作用。"]],
  [57,"藥理學","Abciximab阻斷血小板GPIIb/IIIa受體，抑制fibrinogen橋接造成的凝集。","Abciximab作用在哪個血小板受體？","Abciximab是抗GPIIb/IIIa單株抗體片段；題目中IIIb/IIa順序與名稱錯誤。","Abciximab抗GPIIb/IIIa。","題目問錯誤敘述；正確標的是glycoprotein IIb/IIIa，不是IIIb/IIa。",["A對。屬單株抗體相關藥物。","B錯，為答案。標的是GPIIb/IIIa，題目寫IIIb/IIa不正確。","C對。阻斷fibrinogen介導的血小板凝集。","D對。與tirofiban同屬GPIIb/IIIa抑制概念。"]],
  [58,"藥理學","Oprelvekin是重組IL-11，可促進megakaryocyte成熟、增加血小板；不會以減少嗜中性球為主要作用。","Oprelvekin用途與作用？","用於化療後血小板低下，刺激巨核細胞與骨髓造血；常見水腫、疲倦、頭痛、心律不整。","Oprelvekin增加血小板。","題目問錯誤敘述；oprelvekin目標是提高血小板，不是減少neutrophil。",["A對。促進megakaryocyte增殖與血小板上升。","B對。可影響多種造血細胞。","C錯，為答案。不是用來減少周邊嗜中性球。","D對。疲倦、頭痛、心房心律不整等可見。"]],
  [59,"藥理學","Tamoxifen是選擇性雌激素受體調節劑，用於ER陽性乳癌輔助治療。","乳癌輔助治療作用於雌激素受體的藥？","Tamoxifen在乳房組織拮抗ER訊號，可降低ER陽性乳癌復發。","Tamoxifen：SERM，ER陽性乳癌。","題目問主要標的為雌激素受體；tamoxifen最典型。",["A錯。Progesterone不是ER標的乳癌輔助治療主藥。","B錯。Ketoconazole抑制類固醇合成與抗黴菌。","C對。Tamoxifen作用於estrogen receptor。","D錯。Danazol為弱雄性素，用於子宮內膜異位等。"]],
  [60,"藥理學","Liraglutide是GLP-1 receptor agonist胜肽藥，需皮下注射。","哪個降血糖藥需注射？","Acarbose、saxagliptin、rosiglitazone可口服；liraglutide為胜肽類GLP-1 agonist，需注射。","GLP-1 agonist liraglutide需注射。","題目問必須注射者；liraglutide是胜肽，口服會被分解。",["A錯。Acarbose為口服α-glucosidase inhibitor。","B錯。Saxagliptin為口服DPP-4 inhibitor。","C對。Liraglutide需注射。","D錯。Rosiglitazone為口服TZD。"]],
  [61,"藥理學","Ketoconazole可抑制類固醇合成，在高皮質醇狀態可降低cortisol生成。","Cushing syndrome可用哪藥減輕症狀？","Ketoconazole抑制腎上腺類固醇合成酵素，可減少cortisol。","Ketoconazole可抑制cortisol合成。","題目為腎上腺腫瘤造成Cushing；能降低類固醇合成者是ketoconazole。",["A錯。Triamcinolone是糖皮質素，會加重高皮質醇效應。","B錯。Betamethasone也是糖皮質素。","C錯。Fludrocortisone偏礦物皮質素作用。","D對。Ketoconazole可抑制類固醇生成。"]],
  [62,"藥理學","Aliskiren直接抑制renin，降低angiotensin I生成，用於高血壓。","直接renin inhibitor是哪個？","Aliskiren是直接腎素抑制劑；ACEI、ARB、aldosterone antagonist作用點不同。","Aliskiren直接抑制renin。","題目問經由抑制renin作用治療高血壓者；aliskiren。",["A對。Aliskiren為direct renin inhibitor。","B錯。Captopril抑制ACE。","C錯。Eplerenone拮抗aldosterone receptor。","D錯。Losartan阻斷AT1 receptor。"]],
  [63,"藥理學","Amiodarone含碘且會抑制T4轉T3，可造成甲狀腺功能異常。","哪個抗心律不整藥影響T4轉T3？","Amiodarone可抑制周邊5'-deiodinase，使T4轉T3下降，並因含碘造成甲狀腺毒性。","Amiodarone影響甲狀腺。","題目問抑制T4轉T3者；amiodarone最典型。",["A錯。Adenosine作用於AV node A1 receptor。","B對。Amiodarone可抑制T4轉T3。","C錯。Lidocaine為class Ib鈉通道阻斷。","D錯。Dronedarone較少甲狀腺相關問題，非此經典答案。"]],
  [64,"藥理學","Tolvaptan是口服選擇性V2 receptor antagonist；conivaptan多為靜脈V1a/V2 antagonist。","口服vasopressin antagonist利尿劑？","Tolvaptan阻斷集合管V2受體，促進自由水排出，用於低血鈉等情境。","Tolvaptan：口服V2 antagonist。","題目問口服型ADH antagonist；tolvaptan。",["A錯。Conivaptan通常為靜脈給藥。","B錯。Metolazone為thiazide-like利尿劑。","C錯。Triamterene為ENaC抑制劑。","D對。Tolvaptan為口服V2 antagonist。"]],
  [65,"藥理學","Mirabegron是β3腎上腺素受體致效劑，可放鬆逼尿肌治療膀胱過度活動症。","OAB透過β3 receptor治療藥？","Mirabegron活化β3 adrenoceptor，增加膀胱儲尿容量，副作用較少抗膽鹼症狀。","Mirabegron：β3 agonist治療OAB。","題目問透過β3 adrenoceptor者；mirabegron。",["A錯。Sibutramine為減重藥，作用於單胺再吸收。","B錯。Lorcaserin為5-HT2C agonist。","C對。Mirabegron是β3 agonist。","D錯。Buspirone為5-HT1A partial agonist，治療焦慮。"]],
  [66,"藥理學","Varenicline是α4β2 nicotinic receptor部分致效劑，用於戒菸，不是muscarinic antagonist。","Varenicline作用在哪個受體？","Varenicline部分活化尼古丁型乙醯膽鹼受體，減少戒斷與吸菸獎賞。","Varenicline：α4β2 nicotinic partial agonist。","題目問錯誤敘述；把varenicline說成muscarinic antagonist是錯的。",["A錯，為答案。Varenicline不是muscarinic receptor antagonist。","B對。主要用途為戒菸。","C對。可能有精神神經副作用，如焦慮、憂鬱等需注意。","D對。戒菸效果一般優於bupropion。"]],
  [67,"藥理學","Zafirlukast是cysteinyl leukotriene receptor antagonist，用於氣喘控制。","Zafirlukast治氣喘機轉？","Zafirlukast阻斷CysLT1 receptor，降低支氣管收縮、黏液與發炎。","Zafirlukast拮抗leukotriene receptor。","題目問作用機轉；zafirlukast是白三烯受體拮抗劑。",["A錯。不是adenosine receptor拮抗。","B對。抑制/拮抗leukotriene receptor。","C錯。減少cAMP降解是PDE抑制劑如theophylline。","D錯。減少組織胺釋放不是其主要機轉。"]],
  [68,"藥理學","Alvimopan是周邊μ-opioid receptor antagonist，用於術後腸阻塞，但因心血管風險限制住院短期使用。","Alvimopan使用注意事項？","Alvimopan不易進入中樞，可拮抗腸道opioid造成的蠕動抑制；使用受REMS與心血管風險限制。","Alvimopan：周邊opioid antagonist，有心血管風險限制。","題目問正確敘述；alvimopan屬鴉片受體拮抗劑且需注意心血管毒性。",["A對。為周邊μ受體拮抗劑，曾見心血管事件疑慮。","B錯。它不易進入中樞，且住院使用限制常以短期劑量規範。","C錯。可與opioid止痛劑併用，因周邊作用不顯著影響中樞止痛。","D錯。Alvimopan為口服給藥。"]],
  [69,"藥理學","Tegaserod是5-HT4 agonist，可促進腸胃蠕動；cisapride也具5-HT4作用但因心律風險受限，本題答案為tegaserod。","哪個是5-HT4 agonist？","Tegaserod活化5-HT4受體，促進乙醯膽鹼釋放與胃腸蠕動。","Tegaserod：5-HT4 agonist。","題目問5-HT4 agonist且可用於胃食道逆流相關促蠕動概念；答案選tegaserod。",["A對。Tegaserod是5-HT4 agonist。","B錯。Cisapride也有5-HT4促動力作用，但本題標準答案不是它，且因QT延長受限。","C錯。Fluoxetine是SSRI。","D錯。Ritanserin為5-HT2 antagonist。"]],
  [70,"藥理學","Dinoprostone是PGE2，可促進子宮頸成熟與引產。","懷孕婦女引產用哪個前列腺素？","Dinoprostone用於cervical ripening與induction of labor。","Dinoprostone：PGE2引產。","題目問最適合引產藥；dinoprostone是經典PGE2製劑。",["A對。Dinoprostone用於引產與子宮頸成熟。","B錯。Alprostadil是PGE1，多用於維持動脈導管或勃起功能障礙。","C錯。Iloprost是PGI2類似物，用於肺高壓等。","D錯。Latanoprost是PGF2α類似物，用於青光眼。"]],
  [71,"藥理學","Zileuton抑制5-lipoxygenase，降低leukotriene生成，可用於輕中度氣喘控制。","Zileuton如何治療氣喘？","Zileuton抑制白三烯合成，減少支氣管收縮與發炎。","Zileuton：5-LOX inhibitor。","題目問最適合治療輕中度氣喘者；zileuton是抗白三烯藥。",["A錯。Misoprostol是PGE1類似物，保護胃黏膜等。","B錯。Ibuprofen可能誘發部分氣喘患者惡化。","C對。Zileuton可用於氣喘控制。","D錯。Indomethacin為NSAID，不是氣喘治療藥。"]],
  [72,"藥理學","Fluoxetine是SSRI，抗憂鬱作用主要與serotonin再吸收抑制相關。","Fluoxetine主要影響哪個神經傳遞物？","Fluoxetine選擇性抑制血清素再吸收，增加突觸間serotonin。","Fluoxetine：serotonin。","題目問與抗憂鬱作用最相關神經傳遞物；serotonin。",["A錯。Norepinephrine較與SNRI、TCA等相關。","B對。Fluoxetine是SSRI。","C錯。Glutamate不是fluoxetine主要機轉。","D錯。Acetylcholine不是SSRI抗憂鬱主軸。"]],
  [73,"藥理學","Phenytoin穩定不活化態鈉通道、蛋白結合高，且誘導肝微粒體酵素；不是抑制酵素。","Phenytoin對肝酵素的影響？","Phenytoin是CYP誘導劑，會增加多種藥物代謝；敘述成抑制肝酵素是錯誤。","Phenytoin誘導CYP，不是抑制。","題目問錯誤敘述；phenytoin會誘導而非抑制肝微粒體酵素。",["A對。可延長鈉通道不反應期。","B錯，為答案。Phenytoin誘導肝酵素，增加其他藥物代謝。","C對。高度與albumin結合。","D對。Fosphenytoin為水溶性前驅藥，溶解度較佳。"]],
  [74,"藥理學","Opioid長期使用對鎮痛、欣快、呼吸抑制較易耐受；縮瞳與便秘最不易耐受。","鴉片類哪個作用最不易耐受？","瞳孔縮小常持續存在，不像鎮痛或欣快感會明顯產生耐受。","Opioid不易耐受：縮瞳、便秘。","題目問最不容易產生耐受性；縮瞳是經典答案。",["A對。Miosis最不易產生耐受。","B錯。鎮痛會逐漸耐受。","C錯。止咳作用可產生耐受。","D錯。欣快感容易耐受並促成加量。"]],
  [75,"藥理學","Deferoxamine螯合三價鐵，用於急性鐵中毒。","鐵中毒治療藥？","Deferoxamine與鐵形成ferrioxamine，可由尿排出；尿液可呈酒紅色。","鐵中毒：deferoxamine。","題目問主要治療鐵中毒者；deferoxamine。",["A錯。Dimercaprol用於砷、汞、金等重金屬。","B錯。Penicillamine用於銅中毒/Wilson病等。","C錯。Melarsoprol用於非洲錐蟲病。","D對。Deferoxamine治療鐵中毒。"]],
  [76,"病理學","腦梗塞因神經組織酵素分解，數月後形成液化壞死與囊腔。","腦梗塞後囊性區域是哪種壞死？","中樞神經缺血壞死典型為液化壞死，巨噬細胞清除後留下囊性空腔。","腦梗塞：液化壞死。","題目描述大腦梗塞數月後囊性區域，最符合液化壞死。",["A對。液化壞死是腦梗塞典型結果。","B錯。凝固性壞死多見於多數實質器官梗塞。","C錯。乾酪性壞死常見於結核肉芽腫。","D錯。凋亡為單細胞程序性死亡，不形成4公分囊腔。"]],
  [77,"病理學","TGF-β是促纖維化最重要細胞激素之一，可刺激成纖維細胞與膠原沉積。","組織纖維化最相關因子？","TGF-β促進ECM生成、抑制分解，驅動修復後疤痕與纖維化。","纖維化：TGF-β。","題目問最有關分子；TGF-β是促纖維化核心。",["A對。TGF-β刺激膠原與細胞外基質沉積。","B錯。IL-1偏發炎與內皮活化。","C錯。Selectin參與白血球滾動。","D錯。Histamine造成血管擴張與通透性增加。"]],
  [78,"微生物免疫學","HSV與VZV可在感覺神經節潛伏，復發造成口唇/生殖器疱疹或帶狀疱疹；Poliovirus不以潛伏感染為主。","哪些病毒潛伏於感覺神經元？","單純疱疹病毒與水痘帶狀疱疹病毒都屬herpesvirus，可在感覺神經節建立潛伏。","感覺神經潛伏：HSV、VZV。","題目問因潛伏在感覺神經元造成主要臨床表徵者；1與3正確。",["A錯。包含2 poliovirus不對。","B錯。包含poliovirus且漏掉VZV。","C錯。包含poliovirus且漏掉HSV。","D對。僅HSV與VZV符合。"]],
  [79,"寄生蟲學","象腿症由淋巴絲蟲慢性感染造成淋巴阻塞與肢體腫大。","象腿症最可能是哪類感染？","Wuchereria bancrofti等絲蟲造成淋巴管發炎阻塞，慢性可出現elephantiasis。","象腿症：絲蟲病。","題目問象腿症最可能出現於；淋巴絲蟲病最典型。",["A錯。猩紅熱由A群鏈球菌毒素造成皮疹。","B錯。弓蟲病不造成典型象腿。","C錯。膿痂疹為皮膚細菌感染。","D對。絲蟲病可造成象腿症。"]],
  [80,"病理學","Atypical mitoses是惡性腫瘤重要形態特徵，良性細胞最不應出現。","哪個形態最支持惡性？","非典型有絲分裂代表細胞分裂調控嚴重異常，是惡性腫瘤比其他核異型表現更具特異性的特徵。","Atypical mitoses最不可能見於良性。","題目問最不可能出現在良性細胞者；非典型有絲分裂最符合。",["A對。Atypical mitoses強烈支持惡性。","B錯。高核質比可見於活躍增生或未成熟細胞，特異性較低。","C錯。Hyperchromasia可見於異型但不是最特異。","D錯。Pleomorphism可有程度差異，非最特異。"]],
  [81,"病理學","擴張型心肌病變造成收縮功能障礙，原因包括酒精、doxorubicin與TTN突變；amyloidosis多為限制型舒張障礙。","收縮功能障礙型心肌病變原因？","酒精毒性、anthracycline心毒性與titin基因突變皆可造成擴張型心肌病變。","DCM：酒精、doxorubicin、TTN。","題目問以收縮功能障礙為主要機制者；1、2、3符合，類澱粉沉積偏限制型。",["A錯。漏掉TTN突變。","B對。1酒精、2doxorubicin、3TTN皆可造成收縮障礙。","C錯。漏掉酒精。","D錯。Amyloidosis主要造成限制型心肌病變。"]],
  [82,"病理學","PTT反映內因性與共同路徑；Hemophilia A與部分vWD可延長PTT，血小板功能/數量疾病通常不延長PTT。","哪些疾病會延長PTT？","第VIII因子缺乏會延長PTT；vWD因降低第VIII因子穩定性也可延長PTT。","PTT延長：Hemophilia A、vWD。","題目問通常增加PTT者；1與3正確。",["A錯。TTP主要血小板消耗，PT/PTT通常正常。","B對。Hemophilia A與vWD可延長PTT。","C錯。Glanzmann為血小板凝集缺陷，PTT通常正常。","D錯。包含Glanzmann不恰當。"]],
  [83,"病理學","胸腺濾泡增生最常與重症肌無力相關，可見生發中心。","胸腺濾泡增生常見於哪病？","Myasthenia gravis常伴胸腺濾泡增生或胸腺瘤，與抗ACh receptor自體免疫相關。","胸腺濾泡增生：重症肌無力。","題目問最常見疾病；重症肌無力是經典連結。",["A錯。類風濕關節炎不是胸腺濾泡增生最典型關聯。","B對。重症肌無力常見胸腺異常。","C錯。Graves病是甲狀腺自體免疫病。","D錯。硬皮症非最典型。"]],
  [84,"病理學","胸腺瘤可伴多種副腫瘤自體免疫疾病，包括重症肌無力與純紅血球再生不良。","純紅血球再生不良最常併哪種腫瘤？","Thymoma與pure red cell aplasia有典型關聯。","PRCA：胸腺瘤。","題目問最常併發PRCA的腫瘤；胸腺瘤。",["A錯。畸胎瘤不是PRCA典型腫瘤。","B對。胸腺瘤可併純紅血球再生不良。","C錯。腦膜瘤無此典型關聯。","D錯。生殖細胞瘤不是典型答案。"]],
  [85,"病理學","藥物可造成G6PD溶血、大球性貧血或再生不良性貧血；小球性貧血多因缺鐵、慢性病或地中海型貧血。","哪種貧血與藥物最不相關？","Microcytic anemia常見原因是缺鐵、慢性發炎、地中海型貧血、鉛中毒等，與一般藥物使用較不直接。","藥物較少直接造成小球性貧血。","題目問與藥物最不相關；小球性貧血最符合。",["A錯。氧化性藥物可誘發G6PD缺乏溶血。","B錯。Methotrexate、trimethoprim等可造成葉酸相關大球性貧血。","C錯。Chloramphenicol等可造成再生不良性貧血。","D對。小球性貧血與藥物使用最不相關。"]],
  [86,"病理學","肺腺癌是非吸菸者、女性與年輕患者最常見的原發性肺癌類型。","不抽菸年輕女性最常見肺癌？","Adenocarcinoma常位於周邊肺，與非吸菸者肺癌最相關。","非吸菸女性肺癌：腺癌。","題目問45歲以下不抽菸女性最常見原發性肺癌；腺癌。",["A錯。鱗狀細胞癌較與吸菸、中央型病灶相關。","B對。腺癌最常見於非吸菸者與女性。","C錯。小細胞癌與吸菸高度相關。","D錯。大細胞癌不是此族群最常見。"]],
  [87,"病理學","慢性瀰漫性阻塞性肺疾病包含肺氣腫、慢性支氣管炎、支氣管擴張與氣喘；ARDS是急性瀰漫性肺泡傷害。","哪個不屬於瀰漫性阻塞性肺疾病？","ARDS主要是急性限制性/瀰漫性肺泡傷害造成低氧，不屬慢性阻塞性肺疾病。","ARDS不是COPD類阻塞性疾病。","題目問不屬於者；ARDS不是瀰漫性阻塞性肺疾病。",["A錯。肺氣腫屬阻塞性肺疾病。","B錯。慢性支氣管炎屬阻塞性肺疾病。","C錯。支氣管擴張屬阻塞性肺疾病範疇。","D對。ARDS為急性肺泡傷害，不屬阻塞性肺疾病。"]],
  [88,"病理學","氣喘是第一型過敏與Th2/IgE/嗜酸性球相關疾病，不是第二型過敏反應。","氣喘是哪型過敏？","氣喘典型為IgE媒介第一型過敏，病理可見嗜酸性球、Curschmann spirals與Charcot-Leyden crystals。","氣喘：第一型過敏，不是第二型。","題目問最不適當；說氣喘屬第二型過敏反應錯。",["A對。Th2細胞活化與IL-4、IL-5、IL-13相關。","B錯，為答案。氣喘主要屬第一型過敏。","C對。嗜酸性白血球增加常見。","D對。黏液栓可見Curschmann spirals。"]],
  [89,"病理學","急性胰臟炎常見原因包括膽道阻塞、酒精、高三酸甘油脂與高血鈣；低血鈣多是結果或嚴重度指標。","哪個不是急性胰臟炎常見原因？","低血鈣不是常見病因，反而可因脂肪壞死皂化在急性胰臟炎中出現。","急性胰臟炎原因不是低血鈣。","題目問不是常見原因；低血鈣最不符合。",["A錯。酗酒是常見原因。","B錯。胰管/膽道阻塞可誘發。","C錯。高三酸甘油脂血症是重要原因。","D對。低血鈣不是常見原因。"]],
  [90,"病理學","最常見唾液腺惡性腫瘤是黏液表皮樣癌，不是鱗狀細胞癌。","唾液腺最常見惡性腫瘤？","Mucoepidermoid carcinoma最常見，常有MAML2轉位；adenoid cystic carcinoma常見神經周圍侵犯。","唾液腺惡性：黏液表皮樣癌最常見。","題目問最不適當；把鱗狀細胞癌列為最常見唾液腺惡性腫瘤錯。",["A對。多形性腺瘤是最常見良性唾液腺腫瘤。","B錯，為答案。最常見惡性通常是黏液表皮樣癌。","C對。黏液表皮樣癌常見MAML2基因轉位。","D對。腺樣囊狀癌常有神經周圍侵犯。"]],
  [91,"病理學","Warthin tumor多見於腮腺、吸菸男性，可雙側，組織有雙層嗜酸性上皮與淋巴間質。","雙層上皮加淋巴間質的腮腺腫瘤？","Warthin tumor不是多形性腺瘤；多形性腺瘤才常見軟骨樣基質。","Warthin tumor：腮腺、吸菸、雙層上皮、淋巴間質。","題幹描述Warthin tumor；選項C的軟骨樣物質屬多形性腺瘤，因此最不適當。",["A對。Warthin tumor最常發生在腮腺。","B對。可雙側，約一部分病例雙側性。","C錯，為答案。軟骨樣基質是多形性腺瘤特徵。","D對。與抽菸高度相關。"]],
  [92,"病理學","Brunn nests是膀胱尿路上皮向固有層下陷形成的巢狀結構。","Brunn nests位於膀胱哪一層？","Brunn巢位於膀胱黏膜固有層，屬反應性/化生相關病變。","Brunn nests：固有層。","題目問最常位於何處；答案是固有層。",["A對。Brunn nests位於lamina propria。","B錯。不在內層肌肉。","C錯。不在外層肌肉。","D錯。不在外膜層。"]],
  [93,"病理學","腎血管平滑肌脂肪瘤富含異常血管，重要風險是自發性出血，與結節硬化症相關。","腎angiomyolipoma重要臨床意義？","AML為良性腫瘤，但血管成分可破裂造成後腹腔出血。","腎AML：易自發性出血。","題目問重要臨床意義；自發性出血最重要。",["A錯。AML通常良性，惡性轉變不是25%常見事件。","B對。易自發性出血。","C錯。早期腎衰竭不是典型。","D錯。散發性多為單側；結節硬化症相關較可多發雙側。"]],
  [94,"病理學","腦下垂體腺瘤良惡性不可靠靠細胞異型判定；大腺瘤可出血壞死造成pituitary apoplexy。","垂體腺瘤哪個敘述最適當？","大型垂體腺瘤可能因供血不足發生出血與壞死，造成急性頭痛與視覺症狀。","大垂體腺瘤可出血壞死。","題目問最適當；大型腫瘤內出血與壞死常見。",["A錯。垂體癌需顱脊髓或全身轉移證據，單純局部浸潤不夠。","B錯。腺瘤常破壞正常網狀纖維架構。","C錯。形態異型不可靠區分良惡性。","D對。大腺瘤常可出血與壞死。"]],
  [95,"病理學","子宮內膜異位症最常在卵巢，增加不孕，相關卵巢癌主要為子宮內膜樣癌與亮細胞癌。","Endometriosis相關卵巢癌是哪類？","與子宮內膜異位症相關的卵巢癌主要是endometrioid carcinoma與clear cell carcinoma，不是漿液性癌。","內膜異位相關癌：子宮內膜樣、亮細胞。","題目問最不適當；說主要是漿液性癌錯。",["A對。定義是子宮外有子宮內膜腺體與間質。","B對。最常見位置是卵巢。","C對。可造成沾黏與不孕風險增加。","D錯，為答案。相關癌主要是子宮內膜樣癌與亮細胞癌。"]],
  [96,"病理學","平滑肌瘤常見MED12突變，染色體改變可有但多數不具複雜異常核型，且很少惡性轉化。","子宮平滑肌瘤哪個敘述不適當？","多數leiomyoma並非具有異常且複雜的karyotype；複雜核型更需警覺惡性。","Leiomyoma常見MED12，少惡變。","題目問最不適當；大部分平滑肌瘤有複雜異常染色體核型不正確。",["A對。最常見子宮肌層腫瘤是平滑肌瘤。","B錯，為答案。多數不具異常且複雜核型。","C對。MED12突變常見。","D對。平滑肌瘤很少轉變為平滑肌肉瘤。"]],
  [97,"病理學","卵巢亮細胞癌多與子宮內膜異位症相關；良性或交界性亮細胞腫瘤少見，亮細胞癌本身較重要。","卵巢亮細胞癌哪個說法不適當？","良性或交界性卵巢亮細胞腫瘤並不比亮細胞癌常見。","卵巢亮細胞癌：良性/交界性不常見。","題目問最不適當；A與事實相反。",["A錯，為答案。良性或交界性亮細胞腫瘤不比亮細胞癌常見。","B對。治療原則與其他卵巢上皮癌相似。","C對。常見ARID1A、PIK3CA等，與子宮內膜樣癌有重疊。","D對。晚期預後不佳。"]],
  [98,"病理學","白喉、VZV與痲瘋可造成周邊神經病變；結核分枝桿菌較不典型。","哪種感染較不會引起周邊神經病變？","Mycobacterium tuberculosis主要造成肺結核、肉芽腫與全身播散，周邊神經侵犯不是典型表現。","周邊神經病變不典型：結核。","題目問較不會引起周邊神經病變者；結核分枝桿菌最不典型。",["A對。結核較不會造成典型周邊神經病變。","B錯。白喉毒素可造成神經病變。","C錯。VZV可侵犯神經造成疼痛與神經炎。","D錯。痲瘋嗜周邊神經，典型造成神經病變。"]],
  [99,"病理學","IDH1突變型高級別星狀細胞瘤相較IDH-wildtype預後較佳。","高級別astrocytoma哪個突變預後較好？","IDH突變是成人瀰漫性膠質瘤重要分子分類與預後因子，通常代表較佳存活。","IDH1突變預後較佳。","題目問相較wild-type存活較好者；IDH1。",["A錯。NF1突變不是本題最佳預後標記。","B錯。TP53常見但不如IDH1代表較佳預後。","C對。IDH1突變與較佳預後相關。","D錯。EGFR擴增/突變常見於IDH-wildtype glioblastoma，預後差。"]],
  [100,"病理學","TTF-1免疫染色常用於判斷肺腺癌或甲狀腺來源；多顆腦瘤時可協助確認肺腺癌轉移。","腦瘤切片做TTF-1的目的？","TTF-1陽性支持肺腺癌或甲狀腺來源；在多顆腦瘤情境，重點是尋找肺腺癌轉移。","TTF-1：肺腺癌轉移線索。","題目問病理醫師做TTF-1染色想了解什麼；最符合是否肺腺癌轉移。",["A錯。TTF-1不是判斷良惡性的通用染色。","B錯。分裂快慢常看Ki-67等。","C對。TTF-1可支持肺腺癌轉移。","D錯。TTF-1不是判定非上皮性腫瘤的主要染色。"]],
];

function buildUpdate(row, questionsByNo) {
  const [n, category, key, front, back, summary, stem, details] = row;
  if (!allowed.has(category)) throw new Error(`Invalid category ${category} at ${n}`);
  const q = questionsByNo.get(n);
  if (!q) throw new Error(`Missing question ${n}`);
  const optionLines = ["A", "B", "C", "D"].map((letter, idx) => `${letter}. ${details[idx]}`).join("\n");
  return {
    question_id: q.id,
    question_number: n,
    category,
    category_confidence: "high",
    key_point: key,
    explanation: `【題幹解析】${stem}\n【選項詳解】\n${optionLines}\n【核心考點】${key}`,
    flashcard_front: front,
    flashcard_back: back,
    flashcard_summary: summary,
  };
}

const exam = JSON.parse(fs.readFileSync(examPath, "utf8"));
const questionsByNo = new Map(exam.questions.map((q) => [q.question_number, q]));
const updates = rows.map((row) => buildUpdate(row, questionsByNo));

for (let i = 0; i < updates.length; i += 10) {
  const batch = updates.slice(i, i + 10);
  const batchIndex = String(i / 10 + 1).padStart(2, "0");
  const outPath = path.join(scratchDir, `updates_112-2_medicine-2_${batchIndex}.json`);
  fs.writeFileSync(outPath, JSON.stringify(batch, null, 2) + "\n", "utf8");
}

const updatesById = new Map(updates.map((item) => [item.question_id, item]));
const now = new Date().toISOString();
let updated = 0;
for (const question of exam.questions) {
  const upd = updatesById.get(question.id);
  if (!upd) continue;
  for (const field of ["key_point", "explanation", "flashcard_front", "flashcard_back", "flashcard_summary", "category", "category_confidence"]) {
    question[field] = upd[field];
  }
  question.review_status = "ai_generated";
  question.explanation_model = "antigravity-direct";
  question.explanation_generated_at = now;
  question.category_source = "auto";
  updated += 1;
}
exam.updated_at = now;
fs.writeFileSync(examPath, JSON.stringify(exam, null, 2) + "\n", "utf8");
console.log(`Wrote ${updates.length / 10} update batches and updated ${updated} questions.`);
