# -*- coding: utf-8 -*-
import json
import os

os.makedirs("reports/gemini_outputs", exist_ok=True)

# ----------------------------------------------------
# 109-2_medicine-6_batch-003 (Q31-Q45)
# ----------------------------------------------------
b3_items = [
    {
        "question_id": "109-2_medicine-6_031",
        "question_number": 31,
        "correct_answer": "A",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "辨識腹腔鏡骨盆腔視診中子宮薦椎韌帶之位置與特徵。",
        "explanation": "腹腔鏡骨盆腔初步視診中，標示 * 處之構造自子宮頸後方下段往後延伸連接至薦骨，為典型的子宮薦椎韌帶（uterosacral ligament）。圓韌帶位於前方，自子宮角走向深腹股溝環；闊韌帶為覆蓋子宮與兩側的大片雙層腹膜構造；卵巢懸吊韌帶則是由骨盆壁走向卵巢上端的構造，內含卵巢動靜脈。因此正確答案為A。",
        "flashcard_front": "腹腔鏡 / 骨盆腔診視 / 子宮頸後方 / 薦骨連接韌帶",
        "flashcard_back": "子宮薦椎韌帶自子宮後下段延伸至薦骨，在腹腔鏡下為子宮頸後方兩側往後行的韌帶構造。",
        "flashcard_summary": "腹腔鏡下子宮頸後方至薦骨之韌帶 -> 子宮薦椎韌帶"
    },
    {
        "question_id": "109-2_medicine-6_032",
        "question_number": 32,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "骨盆漏斗韌帶截斷方式的安全考量。",
        "explanation": "骨盆漏斗韌帶（infundibulopelvic ligament）內含卵巢動靜脈，其管徑較粗且血流豐富。使用單極電刀進行凝結（coagulation）容易因為熱效應擴散及止血不夠確實，導致嚴重的術後出血，因此最不恰當。相較之下，以體外打結結紮、內視鏡血管夾夾閉，或使用雙極電刀進行切割與凝固，皆是臨床上較為安全且常用的阻斷與止血方式。",
        "flashcard_front": "腹腔鏡卵巢切除 / 骨盆漏斗韌帶 / 截斷方式 / 卵巢動靜脈",
        "flashcard_back": "骨盆漏斗韌帶富含血管，以單極電刀凝結止血不確實且熱傷害大，是最不恰當的截斷方式。",
        "flashcard_summary": "骨盆漏斗韌帶截斷方式 -> 單極電刀凝結最不安全，應避免使用。"
    },
    {
        "question_id": "109-2_medicine-6_033",
        "question_number": 33,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "女性不同部位毛髮生長對男性素濃度的敏感度差異。",
        "explanation": "陰毛與腋毛的生長在青春期初期即會顯著出現，其毛囊對低濃度的男性素（androgen）反應最為敏感。眉毛與睫毛屬於非男性素依賴毛髮，其生長不受男性素濃度變化的影響；腳毛與其他體毛雖然受男性素刺激，但其敏感度遠低於陰毛。因此陰毛是對男性素濃度反應最敏感的部位。",
        "flashcard_front": "女性毛髮 / 男性素 (androgen) / 最敏感部位 / 陰毛 / 腋毛",
        "flashcard_back": "陰毛與腋毛對男性素的敏感度最高，在低濃度男性素下即可開始生長。",
        "flashcard_summary": "女性毛髮對男性素最敏感部位 -> 陰毛與腋毛"
    },
    {
        "question_id": "109-2_medicine-6_034",
        "question_number": 34,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "處女膜閉鎖或陰道橫膈導致之原發性無月經的處置原則。",
        "explanation": "患者15歲有正常第二性徵發育，卻無初經且伴隨週期性腹痛，超音波可見子宮與陰道積血，高度提示處女膜閉鎖（imperforate hymen）或陰道橫膈等阻塞性構造異常。此時進行黃體素催經（progesterone challenge test）只會使子宮內膜剝落、加重陰道與子宮積血及疼痛，屬於最不適當的處置。正確處置應包括詳細內診診查以確認阻塞部位，安排靜脈腎臟攝影術（IVP）排除合併的泌尿系統畸形，並儘快進行手術切開引流。",
        "flashcard_front": "原發性無月經 / 週期性腹痛 / 子宮陰道積血 / 處置禁忌",
        "flashcard_back": "懷疑處女膜閉鎖或構造阻塞時，禁用黃體素催經，以免加重積血與症狀。",
        "flashcard_summary": "構造阻塞型原發無月經處置 -> 禁用黃體素催經，應行內診、影像檢查及手術切開。"
    },
    {
        "question_id": "109-2_medicine-6_035",
        "question_number": 35,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "停經後陰道出血（postmenopausal bleeding）之標準診斷流程。",
        "explanation": "停經後出血（postmenopausal bleeding）是子宮內膜癌的警訊，必須先進行詳細評估以排除惡性腫瘤。標準的初始步驟應是詳細詢問病史、進行內外診檢查、經陰道超音波評估內膜厚度，並建議進行子宮內膜採樣（endometrial biopsy），故B為最適當處置。在尚未排除癌症前，直接建議子宮切除、給予雌激素補充，或僅建議減重，皆是不符合醫療常規且危險的處置。",
        "flashcard_front": "停經後陰道出血 / 子宮內膜癌警訊 / 處置流程 / 內膜採樣",
        "flashcard_back": "停經後出血須先安排問診、內診、超音波及子宮內膜切片採樣以排除子宮內膜癌。",
        "flashcard_summary": "停經後陰道出血首選處置 -> 詢問病史、內診、超音波，並安排子宮內膜採樣。"
    },
    {
        "question_id": "109-2_medicine-6_036",
        "question_number": 36,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "子宮頸上皮內贅瘤第二級（CIN 2）之治療處置。",
        "explanation": "子宮頸切片若確診為高階病變（包括CIN 2和CIN 3），在40歲的非懷孕女性中，標準處置是進行子宮頸錐狀切除術（conization）或LEEP，以徹底切除病灶並做進一步病理化驗，故選D。僅進行半年抹片追蹤有漏判或惡化風險；直接進行全子宮切除屬於過度治療；施打HPV疫苗可用於預防但無法治療已發生的CIN 2病灶。",
        "flashcard_front": "CIN 2 / 40歲女性 / 子宮頸切片結果 / 下一步處置",
        "flashcard_back": "CIN 2為高階上皮病變，下一步最適當處置為子宮頸錐狀切除（conization）以切除病灶並確定診斷。",
        "flashcard_summary": "CIN 2下一步處置 -> 子宮頸錐狀切除術（conization）。"
    },
    {
        "question_id": "109-2_medicine-6_037",
        "question_number": 37,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "絨毛膜癌（choriocarcinoma）的評估指標與預後特徵。",
        "explanation": "絨毛膜癌常透過檢測 CSF 與血清中 hCG 的比值來評估腦部轉移情形。在沒有腦部轉移的患者中，CSF:serum 的 hCG 比值通常小於 1:60（多呈 1:100 或更低），當比值升高（大於 1:60）則提示有腦部轉移，因此比值為 1:100 時代表腦部轉移機會小，D選項正確。治療是依據 WHO 預後評分決定；腸道轉移屬於高危險預後極差，與肺轉移（低危）不同級；高危險群一開始應使用多重藥物化療（如 EMA-CO）。",
        "flashcard_front": "絨毛膜癌 / 腦轉移評估 / CSF與血清hCG比值 / 預後評分",
        "flashcard_back": "CSF:serum hCG比值 > 1:60提示腦轉移；比值 1:100表示腦轉移機會低。高危者需接受多重藥物化療。",
        "flashcard_summary": "絨毛膜癌CSF/血清hCG比值 -> 1:100表示腦轉移機會小，若 > 1:60 則高度懷疑腦轉移。"
    },
    {
        "question_id": "109-2_medicine-6_038",
        "question_number": 38,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "子宮內膜癌的危險因子與保護因子。",
        "explanation": "子宮內膜癌主要與無拮抗的雌激素（unopposed estrogen）長期刺激有關。懷孕與生產會使體內產生高濃度的黃體素，對子宮內膜有保護作用，因此「多產次（multiparity）」反而是子宮內膜癌的保護因子，而非危險因子，故選C。肥胖、糖尿病、高血壓、停經年齡晚以及長期單獨使用雌激素，均會增加子宮內膜癌的風險。",
        "flashcard_front": "子宮內膜癌 / 危險因子 / 保護因子 / 多產次 / 雌激素暴露",
        "flashcard_back": "子宮內膜癌危險因子包括肥胖、糖尿病、高血壓及單用雌激素；多產次為保護因子。",
        "flashcard_summary": "子宮內膜癌危險與保護因子 -> 肥胖與單用雌激素增加風險，多產次為保護因子。"
    },
    {
        "question_id": "109-2_medicine-6_039",
        "question_number": 39,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "Kleihauer–Betke test (K-B 試驗) 之臨床用途。",
        "explanation": "Kleihauer-Betke (K-B) test 是利用胎兒血紅素（HbF）對酸的抗性比微酸性或中性條件下的成人血紅素（HbA）強的原理，定量檢測母體血液中胎兒紅血球的比例。此項檢查主要用於診斷「胎兒母體間出血（fetomaternal hemorrhage）」，藉以估算胎兒出血量，並據以決定 Rh 陰性母親在產後或受傷後需要注射多少劑量的免疫球蛋白（RhoGAM），故答案為C。",
        "flashcard_front": "Kleihauer-Betke test / K-B 試驗 / 胎兒血紅素酸抗性 / 檢測疾病",
        "flashcard_back": "K-B 試驗用以診斷「胎兒母體間出血（FMH）」，透過定量母血中的胎兒紅血球來決定抗Rh抗體之追加劑量。",
        "flashcard_summary": "Kleihauer-Betke (K-B) 試驗 -> 診斷胎兒母體間出血（fetomaternal hemorrhage）。"
    },
    {
        "question_id": "109-2_medicine-6_040",
        "question_number": 40,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "剖腹產後陰道分娩（TOLAC/VBAC）的適應症與安全處置。",
        "explanation": "對於考慮嘗試剖腹產後陰道分娩（TOLAC）的孕婦，臨床上「可以」且建議使用硬脊膜外麻醉進行減痛分娩。過去擔憂減痛分娩會掩蓋子宮破裂所造成的劇烈疼痛，但目前研究證實，減痛分娩並不會延誤子宮破裂的診斷，且其引起的非特異性胎心音異常仍可作為指標，故D選項錯誤。過往有陰道生產史會提高成功率，前次剖腹若為子宮下段橫切術其子宮破裂風險極低，比傳統直切術更安全，且皆需在可進行緊急剖腹產的醫院進行。",
        "flashcard_front": "剖腹產後陰道分娩 (TOLAC) / 減痛分娩 / 子宮破裂風險 / 術式比較",
        "flashcard_back": "TOLAC「可以」使用減痛分娩，不會掩蓋子宮破裂之診斷。子宮下段橫切術破裂風險低於傳統直切。",
        "flashcard_summary": "TOLAC與減痛分娩 -> 減痛分娩不影響子宮破裂的診斷，TOLAC孕婦可安全施打。"
    },
    {
        "question_id": "109-2_medicine-6_041",
        "question_number": 41,
        "correct_answer": "A",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "唐氏症的遺傳學與臨床特徵。",
        "explanation": "唐氏症（Trisomy 21）是人類最常見的染色體異常，也是最常見的遺傳性智能障礙原因，患者通常可存活至成年，因此「非致死性三合體症」，故A敘述錯誤。常見的致死性三合體症主要為第13對染色體異常（Patau syndrome）或第18對染色體異常（Edwards syndrome）。唐氏症有約75%以上是由於母體卵子在減數分裂第一期時染色體未分離造成，且發生率與孕婦高齡有高度相關。",
        "flashcard_front": "唐氏症 (Trisomy 21) / 減數分裂第一期 / 致死性染色體異常 / 智能障礙",
        "flashcard_back": "唐氏症為「非致死性」染色體異常；愛德華氏症 (trisomy 18) 與巴陶氏症 (trisomy 13) 才是致死性三合體症。",
        "flashcard_summary": "唐氏症存活特性 -> 非致死性三合體症，患者常可存活至成年。"
    },
    {
        "question_id": "109-2_medicine-6_042",
        "question_number": 42,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "真空吸引生產（vacuum extraction）的臨床適應症與先決條件。",
        "explanation": "真空吸引術（vacuum extraction）屬於陰道助產手術，其施行的前提必須是進入「第二產程（子宮頸口已開全）」，且胎頭已降至低位（如呈現著冠）。在第二產程若發生胎心音異常減速（急迫性胎兒窘迫），以真空吸引快速協助娩出是最適當的適應症，故選D。潛伏期及第一產程因子宮頸未開全，絕對禁止使用真空吸引；且臍帶脫垂在第一產程應立即進行緊急剖腹產。",
        "flashcard_front": "真空吸引生產 / 陰道助產 / 產程階段 / 臍帶脫垂 / 胎兒窘迫",
        "flashcard_back": "真空吸引必須在「第二產程（子宮頸開全）」且胎頭低位時才能使用，通常用於解決第二產程的胎兒窘迫。",
        "flashcard_summary": "真空吸引生產適應症 -> 必須在第二產程且胎頭低位，不可在第一產程或潛伏期使用。"
    },
    {
        "question_id": "109-2_medicine-6_043",
        "question_number": 43,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "孕婦乙型鏈球菌（GBS）篩檢的常規處置流程。",
        "explanation": "根據臨床指引，除非前一胎新生兒曾確診發生過「GBS感染症」，或是本胎尿液培養出GBS，才需要在待產時直接給予預防性抗生素。若僅是前一胎篩檢菌落陽性但新生兒未受感染，本胎仍然必須於妊娠「35~37週」進行常規的生殖道與肛門 GBS 篩檢，並根據本胎篩檢結果決定待產時是否用藥，故C為最適當處置。",
        "flashcard_front": "孕婦GBS 篩檢 / 前胎GBS菌落陽性 / 常規篩檢週數 / 抗生素指引",
        "flashcard_back": "若前胎僅是篩檢陽性但寶寶未受感染，本胎仍須在35~37週接受常規生殖道篩檢。",
        "flashcard_summary": "前胎GBS篩檢陽性之本胎處置 -> 妊娠35~37週仍需重新做常規生殖道GBS篩檢。"
    },
    {
        "question_id": "109-2_medicine-6_044",
        "question_number": 44,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "雙胞胎單一胎兒死亡對存活胎兒的影響因素。",
        "explanation": "當雙胞胎中有一胎死亡時，影響另一存活胎兒罹病率與存活率的最關鍵因素為雙胞胎的「絨毛膜性（chorionicity）」。單絨毛膜雙胞胎因為胎盤間有血管吻合交通，死胎的低血壓會引流存活胎的血液，導致存活胎缺血性腦部病變或死亡；此外，胎兒死亡時的懷孕週數及死亡原因也顯著影響存活胎的預後。然而，孕婦年齡與存活胎兒的器官受損或罹病狀況並無直接因果關係，故選C。",
        "flashcard_front": "雙胞胎單一死胎 / 存活胎罹病率 / 絨毛膜性 (chorionicity) / 孕婦年齡",
        "flashcard_back": "存活胎的預後與絨毛膜性、死亡週數及死因最相關；孕婦年齡非影響存活胎病變的直接因素。",
        "flashcard_summary": "雙胞胎單一死胎預後因素 -> 最受絨毛膜性、懷孕週數影響，與孕婦年齡無直接關係。"
    },
    {
        "question_id": "109-2_medicine-6_045",
        "question_number": 45,
        "correct_answer": "A",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "重度子癇前症使用硫酸鎂（MgSO4）的臨床主要目的。",
        "explanation": "對重度子癇前症的孕婦，臨床上給予硫酸鎂的主要目的為「預防子癇症（eclampsia）的痙攣發作」，故選A。硫酸鎂雖然有輕微的血管擴張與抑制子宮收縮效果，但在重度子癇前症中，它並非用來作為主要的降血壓藥物或安胎藥。此外，硫酸鎂用於早產兒保護中樞神經的指引，通常是針對小於32週的早產孕婦，此處患者已懷孕38週足月，故主要目的仍是防範產婦抽搐。",
        "flashcard_front": "重度子癇前症 / 硫酸鎂 (MgSO4) / 給藥主要目的 / 預防痙攣",
        "flashcard_back": "重度子癇前症給予硫酸鎂的主要目的是「預防痙攣發作（防範子癇症）」，而非控制血壓。",
        "flashcard_summary": "硫酸鎂在重度子癇前症之主要作用 -> 預防子癇症之痙攣發作。"
    }
]

with open("reports/gemini_outputs/109-2_medicine-6_batch-003.json", "w", encoding="utf-8") as f:
    json.dump({
        "dataset_id": "109-2_medicine-6",
        "batch_id": "109-2_medicine-6_batch-003",
        "items": b3_items
    }, f, ensure_ascii=False, indent=2)


# ----------------------------------------------------
# 109-2_medicine-6_batch-004 (Q46-Q60)
# ----------------------------------------------------
b4_items = [
    {
        "question_id": "109-2_medicine-6_046",
        "question_number": 46,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "孕婦無症狀菌尿症（asymptomatic bacteriuria）的治療原則。",
        "explanation": "孕婦若尿液細菌培養大於 100,000 cfu/mL，即使無任何臨床症狀，亦診斷為「無症狀菌尿症」。由於懷孕生理變化易使菌尿症進展為急性腎盂腎炎（風險高達 20~40%），進而引發早產或胎兒體重過輕，因此必須立即給予口服抗生素治療，故選C。觀察不治療或延遲至待產時治療均是不正確的處置。",
        "flashcard_front": "孕婦 / 無症狀菌尿症 / 尿液細菌培養 > 100,000 cfu/mL / 處置原則",
        "flashcard_back": "孕婦無症狀菌尿症必須「立即給予抗生素治療」，以防進展為急性腎盂腎炎並增加早產風險。",
        "flashcard_summary": "孕婦無症狀菌尿症處置 -> 立即給予抗生素治療，不可觀察等待。"
    },
    {
        "question_id": "109-2_medicine-6_047",
        "question_number": 47,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "POP-Q 系統中 Point Aa 的解剖定位。",
        "explanation": "在骨盆器官脫垂評估系統（POP-Q）中，Point Aa 位於陰道前壁正中線上，距離外尿道口（hymen）向內 3 公分處。這個位置在解剖學上大致對應到「膀胱頸（bladder neck）」或尿道膀胱交界處，故答案選B。",
        "flashcard_front": "POP-Q 系統 / Point Aa / 陰道前壁 / 距離外尿道口 3 公分",
        "flashcard_back": "Point Aa 位於陰道前壁距離處女膜殘跡 3 公分處，在解剖上大致相當於膀胱頸（bladder neck）。",
        "flashcard_summary": "POP-Q Point Aa 解剖位置 -> 相當於膀胱頸（bladder neck）。"
    },
    {
        "question_id": "109-2_medicine-6_048",
        "question_number": 48,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "陰道穹窿檢查中區分膀胱膨出缺陷類型的臨床測試。",
        "explanation": "將環鉗張開置於兩側陰道側穹窿（lateral fornices）並向上支撐，是臨床上用來區分「膀胱膨出」中屬於中央缺陷或是側壁/旁側缺陷的測試。如果支撐後膨出消失，代表為側壁缺陷；若膨出依然存在，則代表為中央缺陷。此檢查與直腸膨出、尿道膨出或小腸膨出無關，故選C。",
        "flashcard_front": "陰道環鉗檢查 / lateral fornices / lateral vs central defect / 骨盆缺陷區分",
        "flashcard_back": "將環鉗置於側穹窿支撐陰道壁，主要用以區分「膀胱膨出」為側壁（旁）缺陷或中央缺陷。",
        "flashcard_summary": "穹窿環鉗檢查目的 -> 區分膀胱膨出為側壁（旁）缺陷或中央缺陷。"
    },
    {
        "question_id": "109-2_medicine-6_049",
        "question_number": 49,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "子宮頸非典型鱗狀細胞（ASC-US）的標準臨床處置指引。",
        "explanation": "對於抹片呈現非典型鱗狀細胞（ASC-US）的患者，標準處理選項包括：直接做陰道鏡檢查、進行高危險型 HPV 病毒篩檢（若陽性再做陰道鏡），或於 6 個月後追蹤抹片。立即安排子宮頸錐狀切除術（D）是針對高度病變（如確診之 CIN 2/3）的侵入性治療，對於僅是 ASC-US 的患者屬於過度診斷與治療，因此最不恰當。",
        "flashcard_front": "子宮頸抹片 / ASC-US / 處置流程 / 錐狀切除限制",
        "flashcard_back": "ASC-US之處置包括抹片追蹤、高危HPV檢測或陰道鏡；不可直接進行子宮頸錐狀切除。",
        "flashcard_summary": "子宮頸抹片ASC-US處置 -> 不可立即做錐狀切除，應以追蹤、HPV檢測或陰道鏡評估。"
    },
    {
        "question_id": "109-2_medicine-6_050",
        "question_number": 50,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "自然流產的流行病學與危險因子。",
        "explanation": "臨床上已確認，前次懷孕與下次懷孕之間的間隔時間過短會增加不良妊娠預後的風險。一般建議在流產或生產後，應給予子宮和身體足夠的時間恢復，若在產後或流產後 3~6 個月內過快再次懷孕，會顯著增加自然流產、早產及胎兒生長遲滯的風險，因此D選項敘述錯誤。臨床上約 8~20% 的懷孕以流產告終，高齡孕婦及有流產史者均為高風險群。",
        "flashcard_front": "自然流產 / 懷孕間隔 / 產後快速懷孕 / 再次流產風險",
        "flashcard_back": "產後或流產後3~6個月內快速再次懷孕，「會增加」再次流產及早產的風險。",
        "flashcard_summary": "產後快速懷孕與流產風險 -> 產後3~6個月內懷孕會增加流產風險。"
    },
    {
        "question_id": "109-2_medicine-6_051",
        "question_number": 51,
        "correct_answer": "A",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "原發性陰道癌（primary vaginal cancer）的解剖好發部位。",
        "explanation": "原發性陰道癌在女性生殖道惡性腫瘤中相當罕見，絕大多數為鱗狀上皮癌。其最常見的好發解剖部位是在陰道的「上三分之一」且偏向「後壁」，故正確答案為A。",
        "flashcard_front": "原發性陰道癌 / 好發部位 / 陰道壁分段 / 後壁",
        "flashcard_back": "原發性陰道癌最常發生於陰道「上三分之一的後壁」。",
        "flashcard_summary": "原發性陰道癌最常見位置 -> 上三分之一陰道後壁。"
    },
    {
        "question_id": "109-2_medicine-6_052",
        "question_number": 52,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "卵巢內胚層竇瘤（yolk sac tumor）的雙側發生率與手術處理原則。",
        "explanation": "卵巢內胚層竇瘤（卵黃囊瘤）是一種高度惡性的非精原細胞生殖細胞腫瘤，幾乎 100% 僅發生於單側（雙側發生率趨近於 0%）。因此，手術時若另一側卵巢外觀正常，絕對不建議對其進行常規切片或取樣，以避免造成不必要的粘連或損害其生育功能，故選B。相反地，無性胚胎瘤及上皮性漿液性癌皆有較高的雙側發生機率。",
        "flashcard_front": "卵巢內胚層竇瘤 / 卵黃囊瘤 / 單側生長 / 對側卵巢切片原則",
        "flashcard_back": "卵巢內胚層竇瘤幾乎均為單側，手術不建議對外觀正常的對側卵巢進行切片以保護生育力。",
        "flashcard_summary": "卵巢內胚層竇瘤對側切片 -> 幾乎皆為單側，不建議切片健康對側卵巢。"
    },
    {
        "question_id": "109-2_medicine-6_053",
        "question_number": 53,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "子宮內膜異位症的致病機轉與激素影響。",
        "explanation": "子宮內膜異位症是雌激素依賴型疾病，月經來潮時的出血與週期性刺激會加重病灶的生長與疼痛。長期無排卵因為缺乏週期性雌激素波動與月經流出，反而會使異位內膜萎縮、減輕其病程與症狀，故D選項稱其會加重症狀是錯誤的。巧克力囊腫與經血逆流高度相關，且患者常伴隨局部免疫清除功能缺失及雌激素過高刺激。",
        "flashcard_front": "子宮內膜異位症 / 雌激素依賴 / 長期無排卵 / 經血逆流",
        "flashcard_back": "長期無排卵會降低雌激素並減少月經，使異位的子宮內膜萎縮，從而「減輕」而非加重病程。",
        "flashcard_summary": "長期無排卵與子宮內膜異位症 -> 長期無排卵能抑制並減輕子宮內膜異位的病程。"
    },
    {
        "question_id": "109-2_medicine-6_054",
        "question_number": 54,
        "correct_answer": "A",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "子宮內膜異位症治療藥物（如 Danazol）的副作用特徵。",
        "explanation": "Danazol 是一種合成的雄性素衍生物，雖然治療子宮內膜異位症療效顯著，但具有「嚴重的雄性化副作用」，例如體重增加、水腫、青春痘、多毛症、聲音變粗及肝功能異常，因此A選項稱其「幾乎沒有副作用」是錯誤的。使用 GnRHa 會造成假性停經，副作用為熱潮紅與骨質流失；口服避孕藥與黃體素則常作為第一線低副作用的治療選擇。",
        "flashcard_front": "子宮內膜異位症藥物 / Danazol / 雄性化副作用 / GnRHa / 假性停經",
        "flashcard_back": "Danazol 具有多毛、聲音變粗及肝毒性等顯著雄性化副作用，並非無副作用。GnRHa 副作用為骨流失。",
        "flashcard_summary": "Danazol 副作用特徵 -> 具顯著雄性化副作用（多毛、痤瘡、體重增加等）。"
    },
    {
        "question_id": "109-2_medicine-6_055",
        "question_number": 55,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "Clomiphene 抗性排卵障礙的替代治療方案。",
        "explanation": "Clomiphene citrate 是常用口服排卵藥，若產生 clomiphene resistance，可考慮合併胰島素增敏劑 metformin、改用芳香環酶抑制劑 Letrozole，或直接注射促性腺激素 gonadotropins 來刺激卵泡發育。多巴胺拮抗劑（dopamine antagonist）會阻斷多巴胺對泌乳激素的抑制作用，導致高泌乳激素血症，反而會抑制排卵，因此絕對不能列入考慮。",
        "flashcard_front": "Clomiphene 抗性 / 誘發排卵 / Metformin / 多巴胺拮抗劑禁忌",
        "flashcard_back": "多巴胺拮抗劑會導致高泌乳激素血症並抑制排卵，絕不可用於排卵障礙的治療。",
        "flashcard_summary": "Clomiphene 抗性處置 -> 可用 Metformin、Letrozole 或 Gonadotropin，禁用多巴胺拮抗劑。"
    },
    {
        "question_id": "109-2_medicine-6_056",
        "question_number": 56,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "停經後促卵泡激素（FSH）與雌二醇（E2）的水平特徵。",
        "explanation": "女性停經後，由於卵巢濾泡耗竭，雌二醇（Estradiol, E2）分泌量劇烈下降，通常小於 30 pg/mL。因為缺乏雌激素對下視丘和腦下垂體的負回饋作用，促黃體素與促卵泡刺激素（FSH）會大幅代償性上升，通常定義停經的指標為 FSH 大於 40 mIU/mL，故選D。",
        "flashcard_front": "停經期激素變化 / 卵巢功能衰退 / FSH指標 / E2指標",
        "flashcard_back": "停經後缺乏雌激素負回饋，血中FSH會顯著上升（>40 mIU/mL），而E2會降至極低（<30 pg/mL）。",
        "flashcard_summary": "停經婦女激素組合 -> FSH > 40 mIU/mL，E2 < 30 pg/mL。"
    },
    {
        "question_id": "109-2_medicine-6_057",
        "question_number": 57,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "卵細胞減數分裂各階段的停滯與完成時機。",
        "explanation": "女性卵細胞的發育經歷兩次停滯。第一次減數分裂在胚胎期停滯於前期（prophase I），直到青春期排卵前夕才完成；第二次減數分裂在排卵後停滯於中期（metaphase II），必須等到「受精」發生後，精子進入卵子刺激第二極體排出，此分裂才會真正完成，故正確答案為D。",
        "flashcard_front": "卵子發育 / 第一次減數分裂完成 / 第二次減數分裂完成 / 受精",
        "flashcard_back": "第一次減數分裂在排卵前完成；第二次減數分裂停在 Metaphase II，受精後才完成並排出第二極體。",
        "flashcard_summary": "卵細胞減數分裂時機 -> 第一次在排卵前完成，第二次在受精後完成。"
    },
    {
        "question_id": "109-2_medicine-6_058",
        "question_number": 58,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "ASIA 脊髓損傷評估量表（ASIA Impairment Scale）的等級判定。",
        "explanation": "根據 ASIA 評估標準，患者若在薦髓段（S4-S5）保有感覺（第四及第五薦髓皮節有感覺）或運動功能（如外括約肌自主收縮），即定義為不完全損傷。由於患者具有肛門自主收縮，代表損傷面以下有運動功能保留；且患者四肢沒有動作，代表神經病變層面以下之關鍵肌力多數小於3分，因此符合 ASIA C 的診斷標準，故選C。若僅有薦髓感覺保留而無自主收縮，則為 ASIA B。",
        "flashcard_front": "ASIA 分類 / 脊髓損傷 / 薦髓保留 (S4-S5) / 四肢無動作 / 肛門自主收縮",
        "flashcard_back": "有肛門自主收縮代表運動功能保留，且關鍵肌力多數小於3分，應判定為 ASIA C；若僅有感覺保留則為 ASIA B。",
        "flashcard_summary": "ASIA 評估等級判定 -> 薦髓S4-S5有感覺且有肛門自主收縮，為 ASIA C。"
    },
    {
        "question_id": "109-2_medicine-6_059",
        "question_number": 59,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "多發性硬化症（MS）的臨床特徵與神經系統併發症。",
        "explanation": "多發性硬化症是中樞神經系統的多灶性去髓鞘疾病。臨床上，「認知功能缺損」在多發性硬化症患者中「相當常見」（約佔 40~70% 的患者），並非非常少見，故C選項敘述錯誤。患者最常見的膀胱問題為逼尿肌過動，腸道問題以便秘最普遍，且視神經炎常導致視覺功能缺損。",
        "flashcard_front": "多發性硬化症 / 認知功能缺損 / 逼尿肌過動 / 視神經炎",
        "flashcard_back": "認知功能缺損在多發性硬化症中「相當常見」（可達40-70%），並非罕見。逼尿肌過動為最常見尿路症狀。",
        "flashcard_summary": "多發性硬化症併發症 -> 認知功能缺損很常見，而非罕見；逼尿肌過動與便秘亦為常見症狀。"
    },
    {
        "question_id": "109-2_medicine-6_060",
        "question_number": 60,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "神經肌肉交接處疾病（如重症肌無力）的電學診斷工具。",
        "explanation": "連續電刺激神經（RNS）是診斷神經肌肉交接處疾病（如重症肌無力或 Lambert-Eaton 症候群）最常用且首選的臨床電生理篩檢方法。重症肌無力患者在低頻（3 Hz）連續電刺激下，其複合肌肉動作電位波幅會呈現遞減反應，故C選項正確。一般的神經傳導檢查與針極肌電圖主要用來評估周邊神經病變與肌肉本身病變。",
        "flashcard_front": "重症肌無力 / 神經肌肉交接處病變 / 電學篩檢 / 遞減反應",
        "flashcard_back": "篩檢神經肌肉交接處疾病首選「連續電刺激神經 (RNS)」檢查，重症肌無力患者會出現波幅遞減。",
        "flashcard_summary": "神經肌肉交接處疾病篩檢 -> 首選連續電刺激神經（RNS）檢查。"
    }
]

with open("reports/gemini_outputs/109-2_medicine-6_batch-004.json", "w", encoding="utf-8") as f:
    json.dump({
        "dataset_id": "109-2_medicine-6",
        "batch_id": "109-2_medicine-6_batch-004",
        "items": b4_items
    }, f, ensure_ascii=False, indent=2)


# ----------------------------------------------------
# 109-2_medicine-6_batch-005 (Q61-Q75)
# ----------------------------------------------------
b5_items = [
    {
        "question_id": "109-2_medicine-6_061",
        "question_number": 61,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "脊髓損傷病人神經性膀胱所致的最常見泌尿系統併發症。",
        "explanation": "脊髓損傷患者因控制排尿的神經受損，常引起神經性膀胱，導致尿液滯留或排尿不完全。長期留置導尿管、間歇性導尿或殘尿過多，均極易引發「泌尿道感染」，這是脊髓損傷病人泌尿系統最常見的併發症，故選B。雖然腎衰竭、泌尿道結石也是後期的嚴重併發症，但其盛行率均遠低於感染。",
        "flashcard_front": "脊髓損傷 / 神經性膀胱 / 泌尿道併發症 / 留置導尿管",
        "flashcard_back": "脊髓損傷病人最常見的泌尿系統併發症是「泌尿道感染 (UTI)」，與尿滯留及間歇導尿高度相關。",
        "flashcard_summary": "脊髓損傷泌尿系統併發症 -> 最常見為泌尿道感染（UTI）。"
    },
    {
        "question_id": "109-2_medicine-6_062",
        "question_number": 62,
        "correct_answer": "A",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "鈕扣孔變形（Boutonniere deformity）的解剖學病理機制與關節狀態。",
        "explanation": "鈕扣孔變形主要是由於手指伸肌肌腱的「中央腱斷裂」，導致側腱滑向掌側，進而將近端指間關節（PIP）向掌側拉扯。因此，典型變形表現為近端指間關節呈現「屈曲」、遠端指間關節呈現「過度伸直」，故A正確、B與C錯誤。此機轉與側腱的掌側位移密切相關，並非與側腱無關。",
        "flashcard_front": "鈕扣孔變形 / Boutonniere deformity / 中央腱斷裂 / PIP與DIP狀態",
        "flashcard_back": "中央腱斷裂導致側腱向掌側滑移，造成近端指間關節（PIP）屈曲，遠端指間關節（DIP）過度伸直。",
        "flashcard_summary": "鈕扣孔變形機制與狀態 -> 中央腱斷裂引起近端指間關節（PIP）屈曲、遠端指間關節（DIP）過度伸直。"
    },
    {
        "question_id": "109-2_medicine-6_063",
        "question_number": 63,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "頸部裝具（cervical orthosis）限制運動範圍的效能比較。",
        "explanation": "在各類頸部裝具中，胸枕下頷固定架（SOMI brace）是一種半剛性的頸胸裝具。其具有胸前金屬板、枕部支撐架以及下頷支撐架，能對頸部的前屈、後仰、側彎及轉動提供最佳的限制效果，特別是對於中高頸椎（C1-C5）的轉動限制極佳，故選D。海綿頸圈幾乎無限制效果，費城頸圈與一般硬頸圈對側彎與轉動的限制效果明顯不及 SOMI。",
        "flashcard_front": "頸部裝具 / 側彎與轉動限制 / SOMI brace / 頸椎穩定",
        "flashcard_back": "SOMI裝具提供胸、枕、下頷的剛性固定，對頸椎側彎和旋轉的限制效果在所有頸圈中最好。",
        "flashcard_summary": "限制頸部側彎與旋轉最佳裝具 -> 胸枕下頷固定架（SOMI brace）。"
    },
    {
        "question_id": "109-2_medicine-6_064",
        "question_number": 64,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "頸椎間盤突出及疼痛最好發的脊髓節段。",
        "explanation": "頸椎間盤突出與退化性關節炎最好發於活動度最大且承受重力較大的下頸椎。臨床統計上，頸椎間盤病變（discogenic pain）伴隨神經根壓迫引起放射性上肢疼痛，最好發於「第五、六頸椎間（C5-C6）」，次好發於「第六、七頸椎間（C6-C7）」，故C為最適當答案。",
        "flashcard_front": "頸椎間盤突出 / 退化性病變 / 上肢放射痛 / 最好發節段",
        "flashcard_back": "頸椎間盤突出與神經根壓迫最好發於 C5-C6 節段，其次為 C6-C7。",
        "flashcard_summary": "頸椎間盤疼痛最好發位置 -> 第五、六頸椎間（C5-C6）。"
    },
    {
        "question_id": "109-2_medicine-6_065",
        "question_number": 65,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "肺部復健運動訓練的適應症與禁忌症。",
        "explanation": "肺部復健的主要對象是慢性阻礙性肺病（COPD）等慢性肺部疾病患者，這些患者在運動時常會出現活動性呼吸窘迫。肺部復健的目的正是透過運動訓練來改善其心肺耐力、降低運動引起的呼吸困難，因此「活動性呼吸窘迫」並非絕對禁忌症，反而是復健的重要適應症，故D敘述錯誤。有氧運動、心肺運動測試及排除其他高危運動疾病均為正確的處置原則。",
        "flashcard_front": "肺部復健 / 運動處方 / Exertional dyspnea / 禁忌症誤區",
        "flashcard_back": "活動性呼吸窘迫（exertional dyspnea）是肺部復健的「主要適應症」而非絕對禁忌症。",
        "flashcard_summary": "活動性呼吸窘迫與肺部復健 -> 活動性呼吸窘迫非禁忌症，而是肺部復健的訓練重點。"
    },
    {
        "question_id": "109-2_medicine-6_066",
        "question_number": 66,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "過度訓練症候群（overtraining syndrome）的診斷定義與時程。",
        "explanation": "過度訓練症候群是指長期高強度訓練後，因恢復不足導致的生理與精神疲勞狀態。其診斷的核心在於運動表現持續下滑且症狀「無法在數天或數週的休息後恢復」，通常時程長達數週甚至數個月，因此B選項將診斷定義寫為「休息 24 小時後仍存在」是錯誤的。其典型表現為表現下滑與睡眠變差，治療需長期休息，預防是最佳策略。",
        "flashcard_front": "過度訓練症候群 / 表現下滑與失眠 / 診斷時程定義 / 休息恢復時間",
        "flashcard_back": "過度訓練症候群的疲勞與表現下滑無法在「數週或數月」的休息後恢復；短於此時間的疲勞通常僅屬過度蓄積（overreaching）。",
        "flashcard_summary": "過度訓練症候群診斷定義 -> 症狀與運動表現下滑需持續數週至數月且無法通過短暫休息恢復，非僅限24小時。"
    },
    {
        "question_id": "109-2_medicine-6_067",
        "question_number": 67,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "不同類型腦性麻痺（cerebral palsy）的病因學與臨床合併症特徵。",
        "explanation": "腦性麻痺的亞型有不同的好發合併症。雙邊癱瘓型腦性麻痺主要與早產引發的腦室周圍白質軟化症（PVL）有關，患者以下肢痙攣為主，通常智力與聽力多為正常或僅輕微受損，因此「不容易」合併嚴重的聽力異常，故D敘述錯誤。半邊癱瘓型因大腦皮質受損易合併癲癇；四肢癱瘓型因廣泛性腦部受損易有智力障礙；運動困難型多與核黃疸（膽紅素腦病）有關，常有新生兒黃疸史。",
        "flashcard_front": "腦性麻痺亞型 / PVL / 雙邊癱瘓型 / 聽力異常 / 癲癇與黃疸",
        "flashcard_back": "雙邊癱瘓型腦性麻痺常與早產PVL相關，聽力多屬正常；聽力異常常出現在膽紅素腦病變（運動困難型）中。",
        "flashcard_summary": "雙邊癱瘓型腦性麻痺與聽力 -> 雙邊癱瘓型聽力多正常，聽力喪失非其典型合併症。"
    },
    {
        "question_id": "109-2_medicine-6_068",
        "question_number": 68,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "罕見疾病與發展遲緩兒童的復健核心目標。",
        "explanation": "罕見疾病兒童通常存在基因缺陷或漸進性、不可逆的系統性病變，以目前的醫學水準，復健治療的目標「並非使生理功能完全恢復正常」，而是著重於功能性的代償與維持，故選B。復健的主要目的在於提升患者的日常生活功能、藉由擺位與輔具預防及限制肢體變形與關節攣縮，並最終協助病童重返家庭與社會活動。",
        "flashcard_front": "罕見疾病 / 兒童復健 / 復健目標 / 生理功能完全康復誤區",
        "flashcard_back": "罕見疾病多為不可逆病變，復健目標是功能代償、防範變形與社會參與，而非「生理功能回復正常」。",
        "flashcard_summary": "罕見疾病兒童復健目標 -> 重在提升生活功能與預防肢體變形，而非生理功能完全回復正常。"
    },
    {
        "question_id": "109-2_medicine-6_069",
        "question_number": 69,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "不同臨床失語症（aphasia）類型的特徵鑑別。",
        "explanation": "患者中風後表現為表達不流暢且覆誦能力差（poor repetition），但聽覺理解能力尚佳，這是典型的「布洛卡氏失語症（Broca's aphasia）」，故答案為C。渥尼克氏失語症表達流暢但理解力與覆誦均差；經皮質感覺型失語症流暢但理解差、覆誦佳；經皮質運動型失語症表達不流暢且理解佳，但其核心特徵是「覆誦能力良好（preserved repetition）」。",
        "flashcard_front": "失語症鑑別 / 表達不流暢 / 覆誦差 / 理解佳 / Broca aphasia",
        "flashcard_back": "表達不流暢、覆誦能力受損，但理解力良好，即為 Broca 失語症。",
        "flashcard_summary": "李先生中風失語症診斷 -> 布洛卡氏失語症（Broca's aphasia）。"
    },
    {
        "question_id": "109-2_medicine-6_070",
        "question_number": 70,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "編織/纖維肌痛症（fibromyalgia）的臨床特徵與排除診斷。",
        "explanation": "纖維肌痛症是一種以慢性廣泛性肌肉骨骼疼痛為特徵的疾病，病理上屬於中樞神經系統對疼痛刺激的調控異常，並無關節本身的發炎病變。因此，「多發性關節炎（polyarthritis）」不是纖維肌痛症的臨床表現，故選D。患者常合併中樞敏感化的多種症狀，如腸激躁症、憂鬱、疲勞以及被稱作 fibrofog 的認知障礙。",
        "flashcard_front": "纖維肌痛症 / 慢性廣泛疼痛 / Fibrofog / 關節炎排除",
        "flashcard_back": "纖維肌痛症是中樞疼痛調控異常，不伴有關節發炎，故不會出現多發性關節炎。常伴隨腸激躁及憂鬱。",
        "flashcard_summary": "纖維肌痛症之非典型表現 -> 不會出現多發性關節炎，後者提示其他發炎性關節病變。"
    },
    {
        "question_id": "109-2_medicine-6_071",
        "question_number": 71,
        "correct_answer": "C",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "巴氏量表（Barthel Index）評估項目的區分。",
        "explanation": "巴氏量表是評估日常生活活動（BADL）最常用的工具，包含進食、移位、個人衛生、如廁、洗澡、平地步行、上下樓梯、穿衣、大便控制及小便控制等10個項目。而「服藥（taking medication）」屬於工具性日常生活活動（IADL）的評估範圍，不包含在巴氏量表中，故正確答案為C。",
        "flashcard_front": "巴氏量表 / Barthel index / BADL與IADL / 評估項目排除",
        "flashcard_back": "巴氏量表評估基本日常生活功能，不包含「服藥、使用電話、處理財務」等工具性日常生活活動。",
        "flashcard_summary": "巴氏量表不包含項目 -> 服藥（taking medication）屬於 IADL 範疇。"
    },
    {
        "question_id": "109-2_medicine-6_072",
        "question_number": 72,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "肩關節前脫位之 X 光影像學表徵（Hill-Sachs 與 Bankart 骨折）。",
        "explanation": "患者外傷後肩痛，X光影像顯示典型的肩關節前脫位後遺症。X光中可見肱骨頭後外側的凹陷性骨折，即 Hill-Sachs 骨折，同時常伴隨關節盂前下方的骨折缺損，即 bony Bankart 骨折，因此B選項稱「沒有 bony Bankart 病灶」是錯誤的。這些骨性結構破壞均提示病人有習慣性肩關節不穩定的風險，且一般X光無法直接看見軟組織軟骨，故無法用來評估是否有旋轉肌斷裂。",
        "flashcard_front": "肩關節前脫位 / Hill-Sachs lesion / Bankart lesion / X光診斷",
        "flashcard_back": "前脫位常同時造成肱骨頭後外側凹陷（Hill-Sachs）與關節盂前下方骨折（bony Bankart），兩者均提示肩關節不穩定。",
        "flashcard_summary": "肩關節前脫位 X 光表徵 -> 可見 Hill-Sachs 與 bony Bankart 骨折，代表有關節不穩定問題。"
    },
    {
        "question_id": "109-2_medicine-6_073",
        "question_number": 73,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "復健科",
        "category_confidence": "high",
        "key_point": "外上髁炎（網球肘）的臨床定位與超音波表徵。",
        "explanation": "肘關節橈側（外側）疼痛最常見的病因為外上髁炎，即「網球肘（tennis elbow）」，其病理主要為伸腕肌群（特別是伸腕短肌 ECRB）的起點處發生慢性發炎或微小撕裂。超音波影像顯示在外上髁肌腱附著處有低回音腫脹及彩色杜卜勒血流訊號增加，高度支持網球肘的診斷，故正確答案為B。高爾夫球肘發生在內側（尺側）；韌帶或肌肉斷裂在影像上有不同的連續性中斷特徵。",
        "flashcard_front": "肘關節外側痛 / 橈側疼痛 / 伸肌起點 / 超音波血流增強",
        "flashcard_back": "肘關節外側（橈側）疼痛與伸肌起點慢性發炎，即為網球肘（tennis elbow）；高爾夫球肘為內側（尺側）。",
        "flashcard_summary": "肘外側痛與網球肘 -> 橈側疼痛與伸肌腱起點病變提示網球肘（tennis elbow）。"
    },
    {
        "question_id": "109-2_medicine-6_074",
        "question_number": 74,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "不孕症評估中的基礎影像學檢查。",
        "explanation": "在不孕症的初步評估中，必須確認輸卵管是否通暢以及子宮腔是否有結構異常。子宮輸卵管攝影（hysterosalpingography, HSG）是最重要、最常用且非侵入性的首選影像檢查，能有效評估輸卵管阻塞與黏連，故選B。膀胱攝影、下消化道攝影與電腦斷層對子宮與輸卵管的通暢性無診斷價值。",
        "flashcard_front": "不孕症評估 / 輸卵管通暢性 / 首選影像檢查 / 子宮腔異常",
        "flashcard_back": "子宮輸卵管攝影（HSG）是不孕症婦女評估輸卵管是否阻塞及子宮腔構造最核心的影像檢查。",
        "flashcard_summary": "不孕症首選影像檢查 -> 子宮輸卵管攝影檢查（HSG）。"
    },
    {
        "question_id": "109-2_medicine-6_075",
        "question_number": 75,
        "correct_answer": "A",
        "category_group": "醫學（六）",
        "category": "婦產科",
        "category_confidence": "high",
        "key_point": "孕期心血管與呼吸系統的生理變化。",
        "explanation": "孕期為了供應胎兒生長，母體會發生顯著生理調整。其中心輸出量會增加 30~50%（A正確）；血漿量增加大於紅血球增加，使血液容積顯著增加（D錯誤）；由於胎盤產生的孕酮等激素作用，全身血管擴張，使得周邊血管阻力下降（B錯誤）；而子宮逐漸增大壓迫，會使橫膈膜位置向上推升而非下降（C錯誤）。",
        "flashcard_front": "孕期生理變化 / 心輸出量 / 血液容積 / 周邊阻力 / 橫膈膜位置",
        "flashcard_back": "懷孕時心輸出量及血液容積均會「增加」，全身周邊血管阻力「下降」，且橫膈膜位置「上升」。",
        "flashcard_summary": "孕期主要生理變化 -> 心輸出量與血液容積增加，周邊阻力下降，橫膈膜上升。"
    }
]

with open("reports/gemini_outputs/109-2_medicine-6_batch-005.json", "w", encoding="utf-8") as f:
    json.dump({
        "dataset_id": "109-2_medicine-6",
        "batch_id": "109-2_medicine-6_batch-005",
        "items": b5_items
    }, f, ensure_ascii=False, indent=2)


# ----------------------------------------------------
# 109-2_medicine-6_batch-006 (Q76-Q80)
# ----------------------------------------------------
b6_items = [
    {
        "question_id": "109-2_medicine-6_076",
        "question_number": 76,
        "correct_answer": "A",
        "category_group": "醫學（六）",
        "category": "眼科",
        "category_confidence": "high",
        "key_point": "視神經炎（optic neuritis）的典型臨床表現。",
        "explanation": "患者為15歲年輕女性，表現為急性單眼視力模糊、眼球轉動時疼痛、伴隨視乳突水腫，這些是「視神經炎」的典型臨床特徵，且常為多發性硬化症（MS）的早期表現，故正確答案為A。巨細胞病毒視網膜炎好發於後天免疫缺乏（AIDS）等免疫功能低下者；中心視網膜靜脈阻塞多見於有高血壓、糖尿病的老年人；葡萄膜炎一般不以轉動時疼痛和視乳突水腫為主要特徵。",
        "flashcard_front": "年輕女性 / 單眼急性視力下降 / 轉動眼球痛 / 視乳突水腫",
        "flashcard_back": "年輕女性單眼急性視力模糊且轉動時眼球疼痛，合併視乳突水腫，應高度診斷為視神經炎。",
        "flashcard_summary": "單眼視力下降與眼球轉動痛 -> 視神經炎（optic neuritis）。"
    },
    {
        "question_id": "109-2_medicine-6_077",
        "question_number": 77,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "耳鼻喉科",
        "category_confidence": "high",
        "key_point": "急性鼻竇炎的病因、治療與併發症蔓延途徑。",
        "explanation": "鼻竇與眼眶之間僅隔著一層極薄的骨板（紙樣板）。因此，急性鼻竇炎引發眼眶蜂窩性組織炎（orbital cellulitis），最常見是由於「篩竇而非蝶竇」的感染直接穿透紙樣板蔓延而來，故D選項敘述錯誤。大部分急性鼻竇炎為病毒性，使用局部類固醇噴劑有助於減輕水腫與縮短病程，且細菌性感染的首選抗生素為 amoxicillin 或 amoxicillin-clavulanate。",
        "flashcard_front": "急性鼻竇炎 / 眼眶蜂窩性組織炎 / 篩竇紙樣板 / 首選抗生素",
        "flashcard_back": "急性篩竇炎最容易穿透薄弱的紙樣板，蔓延引起眼眶蜂窩性組織炎。細菌性感染首選抗生素為 Amoxicillin。",
        "flashcard_summary": "眼眶蜂窩組織炎感染來源 -> 最常由篩竇（ethmoid sinus）蔓延而來，而非蝶竇。"
    },
    {
        "question_id": "109-2_medicine-6_078",
        "question_number": 78,
        "correct_answer": "A",
        "category_group": "醫學（六）",
        "category": "醫學倫理與醫療決策",
        "category_confidence": "high",
        "key_point": "懷孕晚期篩檢出唐氏症時的醫學倫理與法律規範。",
        "explanation": "根據我國優生保健法施行細則規定，人工流產手術之施行應於懷孕「24週以內」進行。此案中染色體檢驗報告出來時已至少懷孕25週，且24週後的胎兒出生後已具備子宮外存活的機會。因此，醫師若「立刻」為其施行墮胎手術已違反法律與優生保健規範，屬於最不恰當的作法，故選A。醫師應充分向家長說明後期引產的風險與胎兒存活可能，並照會小兒科與社工以提供客觀的疾病照護資訊與支持。",
        "flashcard_front": "唐氏症診斷 / 懷孕24週後 / 人工流產期限 / 醫療法律與倫理",
        "flashcard_back": "超過懷孕24週之胎兒已具子宮外存活能力，優生保健法不允許在此階段隨意施行人工流產。",
        "flashcard_summary": "超過24週之唐氏症墮胎要求 -> 超過24週不可立刻依法進行墮胎，應行跨科會診與支持說明。"
    },
    {
        "question_id": "109-2_medicine-6_079",
        "question_number": 79,
        "correct_answer": "D",
        "category_group": "醫學（六）",
        "category": "醫學倫理與醫療決策",
        "category_confidence": "high",
        "key_point": "編織/學術寫作中的作者定義與學術倫理（Gifting authorship 限制）。",
        "explanation": "根據國際醫學期刊編輯委員會（ICMJE）的作者署名標準，通訊作者與共同作者必須對論文有實質的學術貢獻。陳主任並無參與指導該論文，要求列為通訊作者屬於不當的學術掛名（gift authorship）。因此王醫師應秉持誠實與學術誠信原則，仍將實際指導論文寫作的楊醫師列為通訊作者，故正確答案為D。其他選項皆因政治或前途利益而違反學術倫理。",
        "flashcard_front": "學術寫作 / 通訊作者署名 / 掛名作者 (Gift authorship) / 學術倫理",
        "flashcard_back": "僅有對論文有實質貢獻者方能署名；未參與指導的陳主任要求改列為通訊作者違反學術誠信。",
        "flashcard_summary": "學術掛名要求處置 -> 拒絕無貢獻者的掛名要求，依實質貢獻將楊醫師列為通訊作者。"
    },
    {
        "question_id": "109-2_medicine-6_080",
        "question_number": 80,
        "correct_answer": "B",
        "category_group": "醫學（六）",
        "category": "醫學倫理與醫療決策",
        "category_confidence": "high",
        "key_point": "感染愛滋病之醫療從事人員的執業倫理與防護規範。",
        "explanation": "根據臨床感染管制與醫學倫理指引，感染 HIV 的醫師在體液防護得當且未進行具高血液暴露風險的侵入性操作前，並不具有傳染給病人的高風險。因此，只要做好標準防護措施，醫師「仍然可以安全從事常規醫療行為」，不需立即辭職，故B選項正確。基於隱私權保護，感染者並無義務主動向所有同事或病人揭露病情，除非涉及特定的暴露侵入性治療規範。",
        "flashcard_front": "HIV 感染醫師 / 醫療行為執行 / 標準防護 / 隱私權揭露",
        "flashcard_back": "感染HIV的醫師在做好標準防護且無血液暴露風險下，可繼續執行醫療行為，且無義務主動揭露隱私。",
        "flashcard_summary": "感染HIV醫師之執業原則 -> 做好防護下仍可執行醫療行為，不需主動向同事或病人揭露隱私。"
    }
]

with open("reports/gemini_outputs/109-2_medicine-6_batch-006.json", "w", encoding="utf-8") as f:
    json.dump({
        "dataset_id": "109-2_medicine-6",
        "batch_id": "109-2_medicine-6_batch-006",
        "items": b6_items
    }, f, ensure_ascii=False, indent=2)

print("Wrote all 109-2 medicine-6 batches successfully!")
