const fs = require("node:fs");
const path = require("node:path");

const root = process.cwd();

function readJson(relativePath) {
  return JSON.parse(fs.readFileSync(path.join(root, relativePath), "utf8").replace(/^\uFEFF/, ""));
}

function writeJson(relativePath, data) {
  fs.writeFileSync(path.join(root, relativePath), `${JSON.stringify(data, null, 2)}\n`, "utf8");
}

const manifest = readJson("public/data/manifest.json");
const questionIds = new Set();
for (const exam of manifest.exams) {
  const dataset = readJson(path.join("public", exam.path));
  for (const question of dataset.questions) {
    questionIds.add(question.id);
  }
}

function assertQuestionIds(ids) {
  for (const id of ids) {
    if (!questionIds.has(id)) {
      throw new Error(`Missing question id: ${id}`);
    }
  }
}

function pushUnique(array, item) {
  const index = array.findIndex((existing) => existing.id === item.id);
  if (index >= 0) {
    array[index] = item;
  } else {
    array.unshift(item);
  }
}

const instantKill = readJson("public/data/instant_kill_facts.json");
const newFacts = [
  {
    id: "108-1_medicine-4_078",
    year: "108-1",
    subject: "神經科",
    category: "急症處置 / 中風溶栓",
    reason: "血壓門檻",
    highlight_value: "185/110",
    unit: "mmHg",
    question_text: "有關腦中風之治療，下列敘述何者錯誤？",
    explanation: "急性缺血性中風若要給 rt-PA，血壓需先控制到 <185/110 mmHg；若不給溶栓，通常到 >220/120 mmHg 才需積極降壓。最大劑量 90 mg 也是常考陷阱。",
    flashcard_front: "急性缺血性中風 / rt-PA / 溶栓前血壓",
    flashcard_back: "給 rt-PA 前血壓要 <185/110 mmHg；不適合溶栓者多採 permissive hypertension，通常 >220/120 才積極降壓。",
    options: {
      A: "中風血壓多可先觀察並處理疼痛躁動",
      B: "未溶栓也在 >200/100 就緊急降壓",
      C: "3 小時內適合者可給 rt-PA",
      D: "rt-PA 最大量不超過 90 mg",
    },
  },
  {
    id: "115-1_medicine-4_077",
    year: "115-1",
    subject: "神經科",
    category: "急症處置 / 中風溶栓",
    reason: "禁忌門檻",
    highlight_value: "190/116",
    unit: "不可給",
    question_text: "針對急性腦中風病人之緊急處置，下列敘述何者錯誤？",
    explanation: "題目用 190/116 mmHg 測你是否真的記得溶栓前門檻。這個血壓仍高於 185/110，不可直接給 tPA，需先降到門檻以下並排除出血。",
    flashcard_front: "中風 tPA / 190/116 mmHg / 能不能打？",
    flashcard_back: "不能。190/116 仍超過溶栓前門檻；要先降到 <185/110 mmHg，並用影像排除出血。",
    options: {
      A: "先排除出血",
      B: "190/116 可直接 tPA",
      C: "評估 NIHSS",
      D: "處置時間窗很重要",
    },
  },
  {
    id: "115-1_medicine-4_047",
    year: "115-1",
    subject: "神經科",
    category: "急症處置 / 癲癇重積",
    reason: "時間定義",
    highlight_value: ">5",
    unit: "分鐘",
    question_text: "37 歲男性全身痙攣約 15 分鐘，有關癲癇之敘述何者錯誤？",
    explanation: "Status epilepticus 不再等 30 分鐘才診斷。抽搐持續約 5 分鐘就應視為重積並積極處置；第一線為 benzodiazepine，常見考法是 lorazepam IV 可 5 分鐘後重複。",
    flashcard_front: "Status epilepticus / 不等 30 分鐘 / 第一線",
    flashcard_back: "抽搐持續 >5 分鐘就積極處置；第一線給 BZD，如 lorazepam IV，必要時約 5 分鐘後可重複一次。",
    options: {
      A: "需超過 30 分鐘才診斷",
      B: "lorazepam IV 可重複",
      C: "可能造成神經損傷",
      D: "需先穩定 ABC",
    },
  },
  {
    id: "115-1_medicine-4_076",
    year: "115-1",
    subject: "神經科",
    category: "急症處置 / 癲癇重積",
    reason: "定義陷阱",
    highlight_value: "10",
    unit: "分鐘非唯一",
    question_text: "有關癲癇重積（status epilepticus）的描述，何者錯誤？",
    explanation: "題目提醒不要把 status epilepticus 死背成單次抽搐 10 分鐘。考點是持續抽搐或反覆發作且中間意識未恢復，都要當成急症處理。",
    flashcard_front: "Status epilepticus / 連續抽搐 vs 意識未恢復",
    flashcard_back: "不只看單次抽搐分鐘數；反覆發作且中間意識未恢復，也屬重積癲癇的考點。",
    options: {
      A: "持續抽搐",
      B: "反覆發作意識未恢復",
      C: "可能神經損傷",
      D: "只有單次抽搐 >10 分鐘才算",
    },
  },
  {
    id: "114-1_medicine-6_027",
    year: "114-1",
    subject: "耳鼻喉科",
    category: "術後併發症 / 甲狀腺手術",
    reason: "cutoff",
    highlight_value: ">50",
    unit: "% 下降",
    question_text: "甲狀腺手術後，術中副甲狀腺素下降多少以上會預期術後低血鈣？",
    explanation: "PTH 半衰期短，術中 10-20 分鐘即可觀察趨勢。相對基準值下降超過 50% 是術後低血鈣高風險，需想到鈣與維生素 D 補充。",
    flashcard_front: "甲狀腺手術 / IOPTH / 術後低血鈣",
    flashcard_back: "術中 PTH 在切除後 10-20 分鐘若比基準值下降 >50%，提示術後低血鈣高風險。",
    options: {
      A: "25%",
      B: "50%",
      C: "75%",
      D: "10%",
    },
  },
  {
    id: "112-2_medicine-5_013",
    year: "112-2",
    subject: "神經外科",
    category: "外傷 / 腦震盪",
    reason: "分級",
    highlight_value: "LOC",
    unit: "即第 3 級",
    question_text: "有關第二級腦震盪的敘述，下列何者錯誤？",
    explanation: "腦震盪分級常考「有無失去意識」。只要有任何 loss of consciousness，不論多久，都歸第 3 級；第二級是無 LOC 但症狀超過 15 分鐘。",
    flashcard_front: "腦震盪分級 / LOC / 第二級 vs 第三級",
    flashcard_back: "第二級：無 LOC、症狀 >15 分鐘；第三級：任何 LOC。",
    options: {
      A: "任何 LOC 算第三級",
      B: "第二擊症候群需避免運動",
      C: "可有失憶",
      D: "症狀可能持續 1-2 週",
    },
  },
  {
    id: "108-2_medicine-5_001",
    year: "108-2",
    subject: "外科概論",
    category: "外傷 / 死亡三相分布",
    reason: "時間",
    highlight_value: "0-15",
    unit: "分鐘",
    question_text: "外傷死亡三相分布中，死亡人數最多的時段為何？",
    explanation: "外傷死亡最多發生在即刻期，通常為傷後數秒至 15 分鐘，原因多是大血管破裂、腦幹或高位脊髓重傷。這是外科概論的秒殺時間題。",
    flashcard_front: "外傷死亡三相分布 / 第一波",
    flashcard_back: "死亡最多：傷後 0-15 分鐘；常因大血管破裂、腦幹或高位脊髓重傷。",
    options: {
      A: "0-15 minutes",
      B: "1-24 hours",
      C: "3-7 days",
      D: "7-30 days",
    },
  },
  {
    id: "112-2_medicine-5_001",
    year: "112-2",
    subject: "外科概論",
    category: "急症處置 / 大量輸血",
    reason: "比例",
    highlight_value: "1:1:1",
    unit: "RBC:FFP:PLT",
    question_text: "大量輸血流程中，各種血品使用比例何者臨床結果最好？",
    explanation: "出血性休克啟動 massive transfusion protocol 時，重點是平衡輸血，常考 RBC:FFP:Platelet 約 1:1:1（或接近 1:1:2），避免稀釋性凝血病變。",
    flashcard_front: "Massive transfusion protocol / 平衡輸血",
    flashcard_back: "大量輸血優先記 1:1:1（RBC:FFP:Platelet），目標是同時補氧合、凝血因子與血小板。",
    options: {
      A: "單補 RBC",
      B: "1:1:1",
      C: "只補晶體液",
      D: "延後給血小板",
    },
  },
];
assertQuestionIds(newFacts.map((fact) => fact.id));
for (const fact of newFacts.reverse()) {
  pushUnique(instantKill.facts, fact);
}
writeJson("public/data/instant_kill_facts.json", instantKill);

const glossary = readJson("public/data/medical_glossary.json");
const newTerms = [
  {
    id: "aminoglycosides",
    name: "胺基醣苷類抗生素 (Aminoglycosides)",
    aliases: ["胺基糖苷", "Aminoglycosides", "Gentamicin", "Amikacin", "Kanamycin"],
    category: "藥理學 / 抗生素 / 藥物副作用",
    explanation: "一群主要結合細菌 30S ribosome 的殺菌型抗生素。國考最愛問的不是藥名表，而是它進入細菌需要氧氣依賴的主動運輸，所以厭氧菌天然不敏感。",
    exam_focus: "**看到厭氧菌 + aminoglycoside，要想到無效或天然抗性。** 另一個高頻陷阱是毒性與禁忌：耳毒性、腎毒性、可惡化重症肌無力；與 beta-lactam 併用可因細胞壁破壞而產生協同效果。",
    frequency: 6,
    related_questions: [
      {
        question_id: "115-1_medicine-2_001",
        note: "直接考胺基醣苷進入細菌需氧氣依賴運輸，厭氧菌天然耐藥。"
      },
      {
        question_id: "108-1_medicine-2_003",
        note: "抗藥性敘述題，陷阱是把厭氧菌說成對 aminoglycosides 有感受性。"
      },
      {
        question_id: "109-1_medicine-4_044",
        note: "重症肌無力治療題，aminoglycoside 會加重神經肌肉接合傳遞障礙。"
      }
    ],
    stage: "一階"
  },
  {
    id: "sulfonamides",
    name: "磺胺類藥物 (Sulfonamides)",
    aliases: ["磺胺", "Sulfonamides", "Sulfa drug", "Sulfamethoxazole"],
    category: "藥理學 / 抗生素 / 葉酸代謝",
    explanation: "磺胺類是 PABA 類似物，抑制細菌二氫葉酸合成酶，讓細菌不能自行合成葉酸。人體細胞直接攝取外源性葉酸，所以有選擇性毒性。",
    exam_focus: "**選擇性毒性不是因為人類核糖體不同，而是人類不自行合成葉酸。** 常見陷阱：G6PD 缺乏、新生兒或孕晚期使用可造成溶血與核黃疸；trimethoprim 則是抑制 bacterial DHFR，標的不同。",
    frequency: 6,
    related_questions: [
      {
        question_id: "115-1_medicine-2_002",
        note: "直接考磺胺類為何對哺乳類細胞毒性低：人體不自行合成葉酸。"
      },
      {
        question_id: "110-2_medicine-2_003",
        note: "同樣考選擇性毒性，干擾選項包含胜肽聚醣與核糖體。"
      },
      {
        question_id: "108-2_medicine-2_089",
        note: "孕婦抗生素禁忌題，磺胺類可在 G6PD 缺乏新生兒引發溶血與核黃疸。"
      }
    ],
    stage: "一階"
  },
  {
    id: "clostridioides_difficile_colitis",
    name: "困難梭狀芽孢桿菌感染 / 偽膜性腸炎 (C. difficile colitis)",
    aliases: ["C. difficile", "Clostridioides difficile", "Clostridium difficile", "偽膜性腸炎", "CDI"],
    category: "微生物免疫學 / 腸胃感染 / 院內感染",
    explanation: "抗生素破壞腸道菌相後，C. difficile 過度增殖並產生毒素 A/B，造成水瀉、腹痛，嚴重可見偽膜性腸炎。",
    exam_focus: "**診斷靠糞便毒素或 PCR，不是常規細菌培養。** 治療先停掉誘發抗生素，第一線常考口服 vancomycin 或 fidaxomicin；照護後酒精乾洗手不可靠，孢子污染時要肥皂清水洗手。",
    frequency: 8,
    related_questions: [
      {
        question_id: "112-2_medicine-5_003",
        note: "CDI 治療原則：停誘發抗生素，給口服 vancomycin/fidaxomicin，不加廣效抗陰性菌。"
      },
      {
        question_id: "110-1_medicine-2_090",
        note: "偽膜性腸炎診斷陷阱：主要靠毒素檢測，不靠細菌培養。"
      },
      {
        question_id: "111-1_medicine-3_059",
        note: "手部衛生題：照護 C. difficile 後不適合只用酒精乾洗手。"
      }
    ],
    stage: "二階"
  },
];
for (const term of newTerms) {
  assertQuestionIds((term.related_questions || []).map((q) => q.question_id));
  pushUnique(glossary.terms, term);
}
writeJson("public/data/medical_glossary.json", glossary);

const guidelines = readJson("public/data/clinical_guidelines.json");
const newGuideline = {
  id: "cdi_management",
  title: "困難梭狀芽孢桿菌感染處置 (CDI)",
  aliases: ["C. difficile", "CDI", "偽膜性腸炎", "抗生素相關腹瀉"],
  category: "感染科 / 腸胃感染 / 院內感染",
  scenario: "近期使用廣效抗生素或住院後出現水瀉、腹痛、發燒，或大腸鏡見黃白色偽膜。",
  first_line_action: "先評估嚴重度並停用誘發抗生素；針對 CDI 給口服 vancomycin 或 fidaxomicin，同步補液與矯正電解質。",
  dosage_info: "國考重點放在「口服」vancomycin/fidaxomicin 與停誘發抗生素；嚴重脫水需補液，懷疑 fulminant colitis 要及早外科評估。",
  common_traps: "不要用廣效抗革蘭陰性菌來治 CDI，會更破壞菌相；診斷不是靠常規細菌培養；照護後不能只依賴酒精乾洗手，孢子污染需肥皂清水。",
  frequency: 6,
  related_questions: [
    {
      question_id: "112-2_medicine-5_003",
      note: "治療原則題：停誘發抗生素，口服 vancomycin/fidaxomicin。"
    },
    {
      question_id: "110-1_medicine-2_090",
      note: "診斷陷阱題：毒素檢測優先，不靠培養。"
    },
    {
      question_id: "111-1_medicine-3_059",
      note: "感染管制題：C. difficile 照護後手部衛生不可只用酒精乾洗手。"
    }
  ],
  stage: "二階"
};
assertQuestionIds(newGuideline.related_questions.map((q) => q.question_id));
pushUnique(guidelines.guidelines, newGuideline);
writeJson("public/data/clinical_guidelines.json", guidelines);

const comparisons = readJson("public/data/disease_comparisons.json");
const newComparison = {
  id: "serotonin_syndrome_vs_nms",
  title: "血清素症候群 (Serotonin syndrome) vs 抗精神病藥惡性症候群 (NMS)",
  category: "精神科 / 藥物副作用 / 急症鑑別",
  exam_importance: "高頻",
  exam_focus_tips: "血清素症候群偏「快、反射亢進、clonus、腸胃症狀」；NMS 偏「慢、高燒、lead-pipe rigidity、CK 高、使用 dopamine antagonist 或停 dopamine agonist」。",
  common_traps: "兩者都可發燒、意識改變與自律神經不穩。看到 clonus 與 hyperreflexia 先想 serotonin syndrome；看到鉛管僵硬與抗精神病藥先想 NMS。",
  highlight_keywords: ["clonus", "hyperreflexia", "SSRI/MAOI", "lead-pipe rigidity", "CK 上升", "antipsychotics"],
  diseases: [
    {
      name: "血清素症候群 (Serotonin syndrome)",
      aliases: ["Serotonin syndrome", "SSRI", "MAOI", "血清素症候群"],
      features: {
        "起病速度": "通常數小時內，常在加藥、併用 SSRI/MAOI/linezolid/tramadol 後。",
        "神經肌肉": "Hyperreflexia、clonus、tremor 較典型。",
        "腸胃線索": "腹瀉、嘔吐較支持血清素過多。",
        "處置": "停 serotonergic drugs，支持療法；嚴重可考慮 cyproheptadine。"
      }
    },
    {
      name: "抗精神病藥惡性症候群 (Neuroleptic malignant syndrome)",
      aliases: ["NMS", "Neuroleptic malignant syndrome", "抗精神病藥惡性症候群"],
      features: {
        "起病速度": "通常 1-3 天以上，常見於 dopamine antagonist 或停 levodopa。",
        "神經肌肉": "Lead-pipe rigidity、反射不一定亢進，CK 明顯上升。",
        "腸胃線索": "腸胃症狀不如血清素症候群突出。",
        "處置": "停 offending drug，支持療法；可考慮 dantrolene 或 bromocriptine。"
      }
    }
  ],
  related_questions: [
    {
      question_id: "115-1_medicine-4_064",
      note: "抗精神病藥物副作用題，可延伸整理 NMS 的藥物來源與鑑別。"
    },
    {
      question_id: "113-2_medicine-4_065",
      note: "憂鬱症與 serotonergic drug 題，可延伸血清素症候群風險。"
    }
  ],
  must_know_numbers: [
    {
      value: "數小時",
      unit: "起病",
      target_disease: "血清素症候群",
      context: "用藥後很快出現 clonus、hyperreflexia、腹瀉時優先想到。"
    },
    {
      value: "1-3",
      unit: "天",
      target_disease: "NMS",
      context: "抗精神病藥後較慢出現高燒、鉛管僵硬、CK 高。"
    }
  ],
  stage: "二階"
};
assertQuestionIds(newComparison.related_questions.map((q) => q.question_id));
pushUnique(comparisons.comparison_groups, newComparison);
writeJson("public/data/disease_comparisons.json", comparisons);

console.log("Applied batch 1 must-know updates.");
