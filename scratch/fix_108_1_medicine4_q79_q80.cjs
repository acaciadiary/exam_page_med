const fs = require("fs");
const path = require("path");

const files = [
  path.join("public", "data", "exams", "108-1", "medicine-4.json"),
  path.join("dist", "data", "exams", "108-1", "medicine-4.json"),
];

const now = new Date().toISOString();

const q79 = {
  id: "108-1_medicine-4_079",
  question_number: 79,
  question_text:
    "「耶和華見證人」（Jehovah's Witnesses）教派信徒在醫療上堅持不接受輸血。近來基於尊重病人自主的倫理原則，法律與倫理逐漸接受耶和華見證人拒絕輸血的意願，應該予以尊重；下列那一種情形，醫師應該尊重一個表明為耶和華見證人的信徒拒絕輸血的意願？",
  options: {
    A:
      "成年且有行為能力的病人情況緊急，如果不輸血的話，病人就會死亡；但有清楚的文書證據，證明病人的確有拒絕輸血的意願",
    B: "病人是懷孕36週的婦女拒絕輸血",
    C: "病人是15歲的未成年人拒絕輸血",
    D: "父母都是耶和華見證人信徒，為其8歲病童拒絕輸血",
  },
  correct_answer: "A",
  correct_answers: ["A"],
  answer_status: "standard",
  answer_source: "official_correction",
  category_group: "醫學（四）",
  category: "醫學倫理與醫療決策",
  category_confidence: "high",
  category_source: "auto",
  key_point: "具行為能力成年病人若有清楚拒絕輸血意願，醫師應尊重其自主決定，即使情況危及生命。",
  flashcard_front: "耶和華見證人 / 拒絕輸血 / 成年有行為能力 / 清楚文書意願",
  flashcard_back:
    "成年且有決定能力者的明確醫療拒絕意願具有高度自主性；未成年人、兒童或涉及胎兒利益時，醫師需更謹慎評估最大利益與法律責任。",
  flashcard_summary:
    "成年有行為能力 / 清楚拒絕輸血意願 -> 尊重病人自主，即使不輸血可能危及生命",
  explanation:
    "【題幹解析】\n本題考醫學倫理中的病人自主、宗教信念與拒絕治療。耶和華見證人常因宗教信念拒絕輸血；若病人是成年且有行為能力，並且有明確、可確認的拒絕輸血意願，醫師原則上應尊重其自主決定。相對地，未成年人或兒童的醫療決策需以兒童最佳利益為核心，父母或法定代理人不能任意拒絕可救命治療；孕婦個案則還涉及胎兒利益與母體自主的衝突，需要更謹慎處理。\n\n【選項詳解】\n- A. 正確。成年且有行為能力的病人，即使目前情況緊急，只要有清楚文書證據能證明其拒絕輸血意願，醫師應尊重其自主決定；這是本題最典型、最沒有代理決策爭議的情境。\n- B. 錯誤。懷孕36週婦女拒絕輸血牽涉母體自主與胎兒利益，倫理與法律評估較複雜，不能作為本題最單純應尊重拒絕輸血的答案。\n- C. 錯誤。15歲未成年人雖可參與醫療決策，但通常尚非完整法律上的成年自主決策者；若拒絕救命輸血，醫療團隊需評估最佳利益、監護人意見與法律程序。\n- D. 錯誤。父母不得單以宗教信念替8歲病童拒絕必要救命治療；兒童醫療決策以兒童最佳利益為優先，必要時可尋求倫理委員會或司法協助。\n\n【核心考點】\n拒絕輸血題要先判斷病人是否為成年、有決定能力、意願是否清楚可確認；只有在自主條件充分時，醫師才應直接尊重拒絕治療意願。",
  review_status: "ai_generated",
  explanation_model: "antigravity-direct",
  explanation_generated_at: now,
};

const q80 = {
  id: "108-1_medicine-4_080",
  question_number: 80,
  question_text:
    "2000公克早產兒在加護病房住院近兩個月，她因為雙側腎臟發育不全而合併慢性腎衰竭，又因為肺發育不全合併肺炎一直倚賴呼吸器治療，於3週前需開始長期腹膜透析以維持電解質及體液等平衡。很不幸地，這兩天醫師發現嬰兒發燒、透析液轉為混濁，並且流量大為減少，初步檢查診斷為黴菌性腹膜炎，除了用藥外，醫師建議手術更換腹膜透析管。這時候，不滿20歲的年輕父母親要求醫師：「她實在好可憐，不要救了，讓她走吧，請幫我們移除呼吸器，讓我們回家吧！」。下列何種做法最合適？",
  options: {
    A: "父母生她，也是法定代理人，必須由父母移除其呼吸器",
    B: "取得父母同意書後，施予緩和醫療，可由醫護人員移除呼吸器，讓她回家",
    C: "以所有可用之現代醫療盡全力搶救到最後",
    D: "不移除維生之呼吸器，但停止手術等積極治療",
  },
  correct_answer: "B",
  correct_answers: ["B"],
  answer_status: "standard",
  answer_source: "official_correction",
  category_group: "醫學（四）",
  category: "醫學倫理與醫療決策",
  category_confidence: "high",
  category_source: "auto",
  key_point: "重症新生兒若已處於長期依賴維生治療且治療負擔極高，經父母同意並以病童最佳利益為核心，可轉向緩和醫療並由醫療團隊撤除維生治療。",
  flashcard_front: "早產兒 / 長期呼吸器 / 慢性腎衰竭 / 腹膜透析感染 / 父母要求撤除維生",
  flashcard_back:
    "未成年人生命末期決策以病童最佳利益為核心；不是由父母親自移除設備，也不是一律搶救到底，而是經充分溝通與同意後由醫療團隊提供緩和醫療。",
  flashcard_summary:
    "重症早產兒 / 長期維生治療 / 父母同意 -> 以最佳利益轉向緩和醫療，醫護可撤除呼吸器",
  explanation:
    "【題幹解析】\n題幹描述2000公克早產兒長期住加護病房，已有雙側腎臟發育不全、慢性腎衰竭、肺發育不全、肺炎、長期呼吸器依賴與腹膜透析，現在又發生黴菌性腹膜炎且需更換透析管。這些線索表示病童病情極重、治療負擔高、預後不佳。父母雖未滿20歲，但仍是病童的重要代理決策者；醫療團隊應以病童最佳利益為核心，與父母充分溝通後，若符合末期或不可逆重症情境，可改以緩和醫療減輕痛苦，並由醫護人員依程序撤除維生治療。\n\n【選項詳解】\n- A. 錯誤。父母是法定代理人或主要照護決策者，但撤除呼吸器屬醫療處置，不能要求父母親自移除；應由醫療團隊在合法、合倫理、充分告知同意後執行。\n- B. 正確。取得父母同意後施予緩和醫療，並由醫護人員移除呼吸器，符合重症新生兒生命末期照護中「最佳利益、減輕痛苦、醫療團隊執行」的原則。\n- C. 錯誤。現代醫療並不要求在所有情況下無限制搶救到底；當治療只延長痛苦且預後極差時，轉向緩和醫療可能更符合病童最佳利益。\n- D. 錯誤。只停止手術等積極治療但保留呼吸器，可能仍讓病童持續承受無效或高度負擔的維生治療；若已決定以舒適照護為目標，應完整規劃緩和醫療與撤除維生治療流程。\n\n【核心考點】\n小兒生命末期倫理題要抓住「病童最佳利益、代理決策、緩和醫療、由醫療團隊執行撤除維生治療」；不應把責任推給父母，也不必一律治療到最後。",
  review_status: "ai_generated",
  explanation_model: "antigravity-direct",
  explanation_generated_at: now,
};

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, "utf8").replace(/^\uFEFF/, ""));
}

function writeJson(file, value) {
  fs.writeFileSync(file, `${JSON.stringify(value, null, 2)}\n`, "utf8");
}

for (const file of files) {
  const data = readJson(file);
  const questions = data.questions || data;
  const without = questions.filter((q) => q.question_number !== 79 && q.question_number !== 80);
  without.push(q79, q80);
  without.sort((a, b) => a.question_number - b.question_number);
  if (data.questions) {
    data.questions = without;
    data.updated_at = now;
  }
  writeJson(file, data);
  console.log(`${file}: ${without.length} questions`);
}
