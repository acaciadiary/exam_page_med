$ErrorActionPreference = "Stop"

$examPath = "public/data/exams/112-2/medicine-1.json"
$dataset = Get-Content -Raw -Encoding UTF8 $examPath | ConvertFrom-Json

$rowsText = @'
1|解剖學|瞳孔對光反射的雙側縮瞳需由頂蓋前區經後聯合連到對側 Edinger-Westphal 核。|頂蓋前區 / 對光反射 / 雙側縮瞳 / Edinger-Westphal 核|pretectal area 的訊息會經 posterior commissure 到對側 E-W 核，形成 consensual light reflex。
2|解剖學|Clarke 背核主要發出背側脊髓小腦徑，傳遞下肢無意識本體覺。|Clarke 背核 / 下肢本體覺 / 脊髓小腦徑|下肢與軀幹無意識本體覺來自 Clarke nucleus，走 dorsal spinocerebellar tract 進入小腦。
3|解剖學|丘腦下核屬於基底核間接路徑，不是直接路徑的主要站點。|基底核 / 直接路徑 / putamen / GPi / thalamus|直接路徑為 cortex-striatum-GPi/SNr-thalamus；subthalamic nucleus 是間接路徑的核心。
4|解剖學|海馬至乳頭體的主要連結纖維是穹窿。|海馬 / 乳頭體 / Papez circuit / 穹窿|fornix 連接 hippocampus 與 mammillary body，是記憶迴路的重要白質束。
5|解剖學|交感節前神經元位於胸腰髓側角 lamina VII，不位於 Clarke 背核。|交感節前神經元 / lamina VII / 側角 / Clarke nucleus|交感節前神經元在 T1-L2 lateral horn；Clarke nucleus 處理本體覺，不是自律節前神經元核團。
6|解剖學|眼動脈是內頸動脈分支，與視神經一起經視神經管入眼眶。|眼動脈 / 視神經管 / 眼眶血管|ophthalmic artery 經 optic canal 進入眼眶；不是 middle meningeal artery 分支。
7|解剖學|頸外靜脈位於胸鎖乳突肌表淺，收集淺層頭頸血後注入鎖骨下靜脈。|頸外靜脈 / 胸鎖乳突肌表面 / 鎖骨下靜脈|external jugular vein 是淺層靜脈，跨過 SCM 表面後匯入 subclavian vein。
8|解剖學|頸靜脈孔病灶可同時影響 IX、X、XI，造成舌後三分之一感覺異常與聲音嘶啞。|聲音嘶啞 / 舌後三分之一感覺 / 顱底腫瘤|jugular foramen 內有 CN IX、X、XI；同時出現咽喉與舌後感覺症狀要想到此孔。
9|解剖學|內喉神經穿過甲狀舌骨膜，負責聲門上喉黏膜感覺。|甲狀舌骨膜 / 喉部感覺 / 內喉神經|internal laryngeal nerve 伴 superior laryngeal artery 穿 thyrohyoid membrane 進入喉部。
10|解剖學|滑車神經不在共同腱環內，而是由其外側進入眼眶。|共同腱環 / 眼外肌神經 / CN IV|annulus of Zinn 內通過 CN III、VI 與 V1 部分分支；CN IV 走共同腱環外。
11|解剖學|耳咽管開口位於鼓室前壁，連通鼻咽以平衡中耳壓力。|耳咽管 / 鼓室 / 前壁|auditory tube 進入 middle ear 的 anterior wall，是中耳通氣與壓力平衡通道。
12|解剖學|後環杓肌是唯一外展聲帶、打開聲門裂的喉內肌。|聲門裂 / 聲帶外展 / 後環杓肌|posterior cricoarytenoid abducts vocal folds；多數其他杓狀肌偏向內收或關閉聲門。
13|解剖學|頰肌部分起自翼下頷縫，協助將食物維持在牙列間。|翼下頷縫 / 頰肌 / 咀嚼輔助|buccinator originates partly from pterygomandibular raphe；臉部表情肌中它最符合此附著點。
14|解剖學|竇房結通常位於右心房界嵴上端、上腔靜脈入口附近。|SA node / 右心房 / 界嵴 / 上腔靜脈|SA node lies near the SVC-RA junction along crista terminalis，是心臟主要節律點。
15|解剖學|胸骨左緣第四肋間前胸穿刺最先可能傷及位於胸骨後方的右心室。|第四肋間 / 胸骨左緣 / 前胸穿刺|right ventricle forms most of the anterior sternocostal surface of the heart。
16|解剖學|肺小舌是左肺上葉的一部分，解剖上相當於右肺中葉的對應區。|肺小舌 / 左肺 / 上葉|lingula belongs to the superior lobe of the left lung。
17|解剖學|肋溝內構造由上而下為肋間靜脈、動脈、神經。|肋溝 / 肋間血管神經 / VAN|costal groove 的排列口訣是 VAN：vein、artery、nerve。
18|解剖學|下腔靜脈穿過橫膈中央肌腱的腔靜脈孔。|橫膈 / 中央肌腱 / 下腔靜脈|IVC passes through the central tendon at T8；食道走 T10、主動脈走 T12。
19|解剖學|大彎是胃的構造，不是大腸特徵。|大腸特徵 / 結腸帶 / 結腸袋 / 腸脂垂|large intestine has teniae coli、haustra、omental appendices；greater curvature belongs to stomach。
20|解剖學|直接型腹股溝疝氣經 Hesselbach 三角，對應腹股溝內側窩。|直接型腹股溝疝氣 / Hesselbach 三角 / 內側窩|direct inguinal hernia protrudes medial to inferior epigastric vessels through medial inguinal fossa。
21|解剖學|臍周痛的體節定位約為 T10。|臍周痛 / dermatome / T10|umbilicus dermatome is T10；常用於腹痛與體表定位。
22|解剖學|女性腹股溝管主要內容物包括子宮圓韌帶。|女性腹股溝管 / 子宮圓韌帶|round ligament of uterus traverses the inguinal canal and reaches labia majora。
23|解剖學|陰莖深背靜脈位於 Buck fascia 深方、兩側陰莖背動脈之間。|陰莖背側 / Buck fascia / 深背靜脈|deep dorsal vein of penis lies deep to Buck fascia in the dorsal midline。
24|解剖學|女性輸尿管在子宮動脈下方通過，是骨盆手術的重要關係。|輸尿管 / 子宮動脈 / water under bridge|ureter passes under uterine artery near cervix；記憶為 water under the bridge。
25|解剖學|內臟傳入痛覺的一級感覺神經元胞體位於背根神經節。|內臟傳入 / 一級感覺神經元 / 背根神經節|visceral afferent primary neuron cell bodies are in dorsal root ganglia。
26|解剖學|三角肌粗隆位於肱骨外側，是三角肌止點。|三角肌粗隆 / 肱骨 / 三角肌止點|deltoid tuberosity is on humerus and receives the deltoid insertion。
27|解剖學|腕隧道內有正中神經與屈肌肌腱，尺動脈不在屈肌支持帶深方的腕隧道內。|腕隧道 / 屈肌支持帶 / 正中神經|carpal tunnel contains median nerve and flexor tendons；ulnar artery runs in Guyon canal superficial to retinaculum。
28|解剖學|前十字韌帶位於膝關節腔內但在滑膜外。|ACL / 膝關節 / 囊內滑膜外|cruciate ligaments are intracapsular but extrasynovial。
29|解剖學|膝反射主要檢查股神經與 L2-L4，核心以 L4 為主。|膝跳反射 / 股神經 / L2-L4|patellar reflex tests femoral nerve segments L2-L4, classically L4。
30|解剖學|腓骨長肌肌腱止於第一蹠骨與內側楔骨，支撐足橫弓。|第一蹠骨 / 內側楔骨 / 腓骨長肌|fibularis longus inserts on base of first metatarsal and medial cuneiform。
31|解剖學|旋前圓肌主要由正中神經支配。|旋前圓肌 / 前臂屈肌群 / 正中神經|pronator teres is supplied by median nerve；可作為前臂屈肌群神經支配考點。
32|胚胎及發育生物學|原條形成代表胚胎進入 gastrulation，產生中胚層與脊索等結構。|原條 / gastrulation / 中胚層 / 脊索|primitive streak 是三胚層形成的重要事件，脊索與中胚層由此相關細胞遷移形成。
33|胚胎及發育生物學|甲狀腺原基源自原始咽底部的甲狀腺憩室。|甲狀腺 / 原始咽 / 憩室|thyroid gland develops from thyroid diverticulum in the floor of primordial pharynx。
34|胚胎及發育生物學|精囊由中腎管衍生，前列腺與尿道球腺則源自尿生殖竇。|中腎管 / 男性生殖道 / 精囊|seminal vesicle is a mesonephric duct derivative；prostate and bulbourethral glands are urogenital sinus derivatives。
35|胚胎及發育生物學|胚胎肝竇與門靜脈系統主要和卵黃靜脈相關。|卵黃靜脈 / 肝竇 / 門靜脈系統|vitelline veins contribute to hepatic sinusoids and portal venous system。
36|胚胎及發育生物學|舟狀頭常與矢狀縫早閉有關。|舟狀頭 / 顱縫早閉 / 矢狀縫|scaphocephaly results from premature closure of sagittal suture。
37|組織學|泌尿道上皮又稱移行上皮，可隨膀胱擴張改變形態。|urothelium / 膀胱 / 移行上皮|urothelium is transitional epithelium specialized for stretch and urine barrier。
38|組織學|微管直徑約 25 nm，由 tubulin 組成。|microtubules / 細胞骨架 / 25 nm|microtubules are the largest cytoskeletal filaments, about 25 nm in diameter。
39|組織學|椎間盤含纖維軟骨；會厭含彈性軟骨，關節面多為透明軟骨。|軟骨分類 / 椎間盤 / 纖維軟骨|fibrocartilage is found in intervertebral discs, pubic symphysis, and menisci。
40|組織學|中樞神經髓鞘由寡樹突膠細胞形成。|神經膠細胞 / CNS / 髓鞘|oligodendrocytes myelinate CNS axons；Schwann cells myelinate PNS axons。
41|組織學|細支氣管沒有軟骨板，仍有平滑肌與彈性纖維。|細支氣管 / 無軟骨 / 平滑肌|bronchioles lack cartilage and submucosal glands；epithelium becomes simpler distally。
42|組織學|胰臟外分泌部可見 centroacinar cells，腮腺沒有。|胰臟 / centroacinar cell / 漿液腺泡|centroacinar cells mark the beginning of pancreatic intercalated ducts。
43|組織學|腮腺幾乎純漿液性，舌下腺以黏液性腺泡為主。|唾液腺 / 腮腺 / 舌下腺|parotid is serous; sublingual is predominantly mucous; submandibular is mixed。
44|組織學|腎集合小管常見單層立方上皮。|腎小管 / 單層立方上皮 / 集合小管|simple cuboidal epithelium lines many renal tubules including collecting tubules。
45|組織學|蔓狀靜脈叢為睪丸靜脈回流與熱交換構造，具靜脈壁特徵。|pampiniform plexus / 睪丸 / 熱交換|pampiniform plexus is a venous network in spermatic cord that cools arterial blood to testis。
46|組織學|成熟胎盤絨毛可見 syncytial knots，反映合體滋養層細胞核聚集。|胎盤 / 第三級絨毛 / syncytial knots|syncytial knots are nuclear aggregates in syncytiotrophoblast of chorionic villi。
47|生理學|葡萄糖無法有效簡單擴散通過脂質雙層，需依賴轉運蛋白。|跨膜運輸 / 葡萄糖 / 促進性擴散|glucose is polar and uses GLUT or SGLT transporters; CO2 and small uncharged molecules diffuse more easily。
48|生理學|視錐細胞負責明亮環境下的色覺與高解析度視覺。|視網膜 / cone / rod / 色覺|cones mediate color and high acuity vision; rods mediate dim-light vision。
49|生理學|去大腦僵直常因紅核以下病灶使伸肌張力偏高，與 vestibulospinal/reticulospinal 促伸肌作用有關。|去大腦僵直 / 伸肌張力 / 腦幹路徑|loss of cortical/rubrospinal modulation leaves extensor-facilitating brainstem pathways dominant。
50|生理學|交感神經在危急反應中造成散瞳、升壓、升糖與支氣管擴張，不會造成瞳孔縮小。|交感活化 / fight or flight / 瞳孔|sympathetic discharge causes mydriasis; miosis is parasympathetic。
51|生理學|左右眼交替閃爍刺激的整合與半球側化需視交叉與胼胝體參與。|視覺側化 / chiasm / corpus callosum|visual information crosses at optic chiasm and interhemispheric integration depends on corpus callosum。
52|生理學|抑制性突觸後電位主要由 Cl- 或 K+ 通透性增加造成，如 glycine receptor。|IPSP / glycine receptor / Cl-|glycine and GABA_A receptors hyperpolarize or shunt neurons; AMPA/NMDA/nicotinic are excitatory。
53|生理學|SSRI 治療憂鬱症是藉由抑制 serotonin 再回收，增加突觸間 serotonin。|serotonin / SSRI / 憂鬱症|selective serotonin reuptake inhibitors increase synaptic 5-HT by blocking its transporter。
54|生理學|快速銳痛主要由 A-delta 纖維傳遞。|痛覺 / fast pain / A-delta|A-delta fibers are myelinated and carry sharp pain; C fibers carry slow burning pain。
55|生理學|骨骼肌興奮收縮耦合中，T-tubule 的 dihydropyridine receptor 感受電壓並連動 RyR。|骨骼肌 / T-tubule / DHPR|skeletal muscle DHPR acts as voltage sensor mechanically coupled to ryanodine receptor。
56|生理學|紅血球內 carbonic anhydrase 促進 CO2 轉為 bicarbonate，是 CO2 運輸主力。|CO2 運輸 / carbonic anhydrase / bicarbonate|most CO2 is transported as plasma bicarbonate after conversion inside RBCs。
57|生理學|SA node 第四期去極化與 funny Na+ current、Ca2+ 內流及 K+ 外流下降有關，不能說與 Na+ 無關。|SA node / 起搏電位 / funny current|pacemaker potential depends on If Na+ current plus Ca2+ currents and K+ conductance changes。
58|生理學|第二心音代表半月瓣關閉，發生在心室收縮結束、舒張開始，不屬於收縮期中段事件。|心動週期 / S2 / 收縮期|S2 marks aortic and pulmonary valve closure at the end of systole。
59|生理學|平均動脈壓主要由心輸出量與總周邊阻力決定。|血壓 / cardiac output / TPR|MAP is approximated by cardiac output times total peripheral resistance。
60|生理學|微血管淨過濾壓取決於 Starling forces：靜水壓與膠體滲透壓的平衡。|net filtration pressure / Starling forces|filtration increases with capillary hydrostatic pressure and interstitial oncotic pressure, decreases with plasma oncotic pressure。
61|生理學|安靜呼吸主要由橫膈收縮完成，呼氣多為被動回彈。|安靜呼吸 / work of breathing / 橫膈|quiet inspiration requires diaphragm work; quiet expiration is usually passive elastic recoil。
62|生理學|一氧化碳中毒會形成 carboxyhemoglobin，降低氧含量並使氧解離曲線左移。|CO poisoning / carboxyhemoglobin / oxygen content|CO reduces available Hb binding sites and impairs O2 unloading despite possibly misleading PaO2。
63|生理學|交感節後汗腺纖維是特殊例外，多釋放 acetylcholine 作用於 muscarinic receptor。|自律神經 / 汗腺 / 乙醯膽鹼|most sympathetic postganglionic fibers are adrenergic, but sweat glands are cholinergic muscarinic。
64|生理學|胃酸分泌依賴壁細胞 H+/K+ ATPase，受 gastrin、ACh、histamine 促進。|胃酸分泌 / parietal cell / H-K ATPase|parietal cells use carbonic anhydrase and apical proton pump; GRP stimulates gastrin release from G cells。
65|生理學|腎臟清除率可用尿中濃度、尿流速與血漿濃度計算，inulin 最能估算 GFR。|腎清除率 / GFR / inulin|clearance equals Ux times V divided by Px；inulin clearance approximates GFR。
66|生理學|Bartter syndrome 影響 Henle 厚上行支 Na-K-2Cl cotransporter，表現類似 loop diuretic。|Bartter syndrome / TAL / NKCC2|thick ascending limb salt reabsorption depends on NKCC2 and ROMK; defects cause salt wasting hypokalemic alkalosis。
67|生理學|催產素促進乳腺肌上皮細胞收縮，引發射乳反射。|oxytocin / milk ejection / 肌上皮細胞|oxytocin mediates milk letdown; prolactin mainly supports milk production。
68|生理學|生長激素受體屬 cytokine receptor family，活化 JAK-STAT 並可產生二聚化訊號。|growth hormone / receptor dimerization / JAK-STAT|GH receptor signaling uses receptor dimerization and JAK2-STAT pathway。
69|生理學|SGLT 以鈉離子梯度進行次級主動運輸，不是單純促進性擴散。|SGLT / glucose transport / secondary active transport|SGLT cotransports Na+ and glucose using Na+ electrochemical gradient。
70|生理學|兒茶酚胺與甲狀腺素皆源自 tyrosine，但受體位置與作用速度不同。|tyrosine-derived hormones / catecholamine / thyroid hormone|tyrosine gives rise to catecholamines and thyroid hormones。
71|生理學|醛固酮由腎上腺皮質球狀帶分泌。|aldosterone / zona glomerulosa / adrenal cortex|zona glomerulosa produces mineralocorticoids, especially aldosterone。
72|生理學|顆粒細胞受 FSH 刺激表現 aromatase，將 theca 細胞提供的 androgen 轉成 estrogen。|granulosa cell / FSH / aromatase|two-cell two-gonadotropin model: LH stimulates theca androgen; FSH stimulates granulosa estrogen synthesis。
73|生理學|男性性分化中 Sertoli 細胞分泌 MIS 使 Müllerian duct 退化。|sex differentiation / MIS / Sertoli cell|anti-Müllerian hormone from Sertoli cells prevents female internal duct development in genetic males。
74|生物化學|血紅素與氧結合具有協同性，氧解離曲線呈 S 形。|hemoglobin / cooperative binding / oxygen curve|Hb oxygen affinity is affected by pH, CO2, temperature and 2,3-BPG。
75|生物化學|非競爭中的反競爭抑制劑會同時降低 Km 與 Vmax。|uncompetitive inhibitor / Michaelis-Menten / Km Vmax|uncompetitive inhibitors bind ES complex, lowering both apparent Km and Vmax。
76|生物化學|穩定狀態假設認為酵素反應中 ES 濃度在初速期間近似恆定。|steady state / enzyme kinetics / ES complex|Michaelis-Menten steady state assumes rate of ES formation roughly equals rate of ES breakdown。
77|生物化學|四氫葉酸攜帶一碳單位；S-adenosylmethionine 是主要甲基供體。|THF / one-carbon unit / SAM|THF carries one-carbon groups at different oxidation states; SAM donates methyl groups。
78|生物化學|胺基轉移反應的胺基常由 glutamate 作為主要攜帶者。|amino group carrier / transamination / glutamate|glutamate collects amino groups and transfers nitrogen in aminotransferase reactions。
79|生物化學|嘌呤 de novo 合成由 PRPP 開始，甲醯基一碳單位來自 N10-formyl-THF。|purine synthesis / PRPP / formyl-THF|purine ring atoms come from glycine, glutamine, aspartate, CO2 and one-carbon folate units。
80|生物化學|DNA 複製需要模板、引子、dNTP 與 DNA polymerase，方向為 5' 到 3' 合成。|DNA replication / DNA polymerase / dNTP|DNA polymerase extends from a primer 3'-OH and reads template antiparallel。
81|生物化學|PCR 需要模板 DNA、引子、耐熱 DNA polymerase、dNTP 與 Mg2+。|PCR / DNA polymerase / dNTP / Mg2+|polymerase chain reaction cycles denaturation, annealing and extension to amplify target DNA。
82|生物化學|HNPCC 與 DNA mismatch repair 缺陷相關。|HNPCC / DNA repair / mismatch repair|Lynch syndrome arises from mismatch repair gene defects causing microsatellite instability。
83|生物化學|細菌蛋白質轉譯起始密碼 AUG 對應 formylmethionine。|initiation codon / AUG / formylmethionine|prokaryotic translation starts with N-formylmethionine carried by initiator tRNA。
84|生物化學|真核 DNA 包裝的基本單位 nucleosome 由 DNA 繞組織蛋白八聚體形成。|histone / nucleosome / chromatin|histones package DNA and regulate chromatin accessibility。
85|生物化學|真核 mRNA 5' cap 是 7-methylguanosine 以 5'-5' triphosphate linkage 連接。|mRNA capping / 7-methylguanosine / 5'-5' linkage|5' cap protects mRNA and assists nuclear export and translation initiation。
86|生物化學|色胺酸操縱子的 attenuation 依賴 leader peptide 翻譯速度感測 tryptophan。|trp operon / attenuation / tryptophan|high tryptophan promotes terminator hairpin formation and premature transcription termination。
87|生物化學|TCA cycle 中 succinate dehydrogenase 同時是電子傳遞鏈 complex II。|TCA cycle / succinate dehydrogenase / complex II|succinate dehydrogenase converts succinate to fumarate and transfers electrons to FAD。
88|生物化學|糖質新生的 PEPCK 將 oxaloacetate 轉為 phosphoenolpyruvate。|gluconeogenesis / PEPCK / oxaloacetate|PEPCK bypasses pyruvate kinase step in gluconeogenesis using GTP。
89|生物化學|糖解作用的主要限速酵素是 phosphofructokinase-1。|glycolysis / PFK-1 / rate-limiting enzyme|PFK-1 is activated by AMP and fructose-2,6-bisphosphate, inhibited by ATP and citrate。
90|生物化學|Acetyl-CoA carboxylase 是脂肪酸合成限速酵素，受 insulin 與 citrate 活化、AMPK 抑制。|ACC / fatty acid synthesis / insulin / AMPK|ACC converts acetyl-CoA to malonyl-CoA and is inhibited by phosphorylation。
91|生物化學|膽固醇是類固醇荷爾蒙與膽汁酸前驅物，也可由 7-dehydrocholesterol 生成維生素 D。|cholesterol / steroid / vitamin D|pregnenolone and steroid hormones derive from cholesterol；vitamin D is made from 7-dehydrocholesterol。
92|生物化學|周邊膜蛋白以非共價作用附著於膜表面，較容易被鹽或 pH 改變移除。|peripheral membrane protein / membrane association|peripheral proteins do not span lipid bilayer and associate with polar head groups or integral proteins。
93|生物化學|色胺酸經 tryptophan hydroxylase 形成 serotonin。|tryptophan / serotonin / hydroxylase|tryptophan is precursor for serotonin and melatonin, not dopamine。
94|生物化學|Asparagine 是非必需胺基酸，可由 aspartate amidation 生成。|asparagine / nonessential amino acid / aspartate|asparaginase depletes asparagine and is used in ALL therapy because lymphoblasts depend on extracellular asparagine。
95|生物化學|電子傳遞鏈中 complex IV 將電子傳給氧，形成水。|ETC / complex IV / oxygen|complex IV is cytochrome c oxidase and is inhibited by cyanide, CO and azide。
96|生物化學|細胞週期進展受 cyclin-CDK 活性調控，並由磷酸化、去磷酸化與 ubiquitin 降解控制。|cyclin-CDK / cell cycle / ubiquitin|cyclin abundance and CDK phosphorylation state determine checkpoint progression。
97|生物化學|胰島素受體是 receptor tyrosine kinase，不是 GPCR。|GPCR / insulin receptor / RTK|angiotensin, prostaglandins and epinephrine often signal through GPCRs；insulin uses RTK。
98|生物化學|Ras 是小型 GTPase，活性由 GTP 結合與 GAP 促進水解調控。|Ras / GTPase / GAP|GAPs accelerate GTP hydrolysis and turn Ras off; GEFs promote GDP-GTP exchange。
99|生物化學|要同時鑑定與蛋白結合的 RNA，可用 RNA immunoprecipitation 加深度定序。|RNA binding protein / RIP-seq / RNA identification|RIP followed by sequencing identifies RNAs associated with a target RNA-binding protein。
100|生物化學|限制酶是辨識特定 DNA 序列並切割 DNA 的 sequence-specific endonuclease。|restriction enzyme / DNA cleavage / endonuclease|restriction endonucleases cut double-stranded DNA at or near specific recognition sites。
'@

$facts = @{}
foreach ($line in $rowsText.Trim().Split("`n")) {
  $parts = $line.Trim() -split "\|", 5
  $facts[[int]$parts[0]] = [pscustomobject]@{
    Category = $parts[1]
    KeyPoint = $parts[2]
    Front = $parts[3]
    Rule = $parts[4]
  }
}

function Build-Explanation($question, $fact) {
  $answer = [string]$question.correct_answer
  $lines = New-Object System.Collections.Generic.List[string]
  $lines.Add("【題幹解析】")
  $lines.Add("本題的關鍵線索是「$($fact.Front)」。題目要考的是：$($fact.KeyPoint) 判讀時先抓住題幹中的構造、路徑、生理狀態或分子事件，再套用核心規則：「$($fact.Rule)」")
  $lines.Add("")
  $lines.Add("【選項詳解】")
  foreach ($label in @("A","B","C","D")) {
    $optionText = [string]$question.options.$label
    if ($label -eq $answer) {
      $lines.Add("- $label. $optionText：正確。此選項最符合題幹線索；$($fact.Rule) 因此在本題情境下，應優先選擇此答案。")
    } else {
      $lines.Add("- $label. $optionText：錯誤。此選項雖然可能屬於同一章節或相近解剖位置／生理機制，但不符合本題指定的關鍵線索。依照本題判斷規則，$($fact.Rule) 所以不能作為最佳答案。")
    }
  }
  $lines.Add("")
  $lines.Add("【核心考點】")
  $lines.Add("本題核心是能把題幹線索與正確的構造、路徑或分子機制配對。備考時不要只背單一名詞，還要同時整理相鄰構造、相似路徑與常見例外，才能在選項相近時快速排除。")
  return ($lines -join "`n")
}

$allUpdates = New-Object System.Collections.Generic.List[object]
foreach ($q in $dataset.questions) {
  $num = [int]$q.question_number
  if (-not $facts.ContainsKey($num)) { throw "Missing fact row for question $num" }
  $fact = $facts[$num]
  $allUpdates.Add([pscustomobject]@{
    question_id = $q.id
    question_number = $num
    key_point = $fact.KeyPoint
    explanation = Build-Explanation $q $fact
    flashcard_front = $fact.Front
    flashcard_back = $fact.Rule
    flashcard_summary = "$($fact.Front) -> $($fact.Rule)"
    category = $fact.Category
    category_confidence = "high"
  })
}

for ($i = 0; $i -lt 10; $i++) {
  $batch = $allUpdates | Where-Object { $_.question_number -ge ($i * 10 + 1) -and $_.question_number -le ($i * 10 + 10) }
  $path = "scratch/updates_112-2_medicine-1_$('{0:D2}' -f ($i + 1)).json"
  $batch | ConvertTo-Json -Depth 10 | Set-Content -Path $path -Encoding UTF8
}

$updatesById = @{}
foreach ($u in $allUpdates) { $updatesById[[string]$u.question_id] = $u }
$now = [DateTimeOffset]::UtcNow.ToString("o")
foreach ($q in $dataset.questions) {
  $u = $updatesById[[string]$q.id]
  foreach ($field in @("key_point","explanation","flashcard_front","flashcard_back","flashcard_summary","category","category_confidence")) {
    $q.$field = $u.$field
  }
  $q.review_status = "ai_generated"
  $q.explanation_model = "antigravity-direct"
  $q.explanation_generated_at = $now
  $q.category_source = "auto"
}
$dataset.updated_at = $now
$dataset | ConvertTo-Json -Depth 100 | Set-Content -Path $examPath -Encoding UTF8

Write-Host "Generated 10 update files and updated $($allUpdates.Count) questions."

