# 自動更新流程說明

這份文件給未來維護者或其他 AI Agent 使用。目標是讓考題網站可以固定更新題目資料，AI 詳解則保持可替換、可人工審核。

## GitHub Actions

### Deploy Pages

檔案位置：

```text
.github/workflows/deploy_pages.yml
```

用途：

- 當 `main` 分支收到網站、資料、腳本或測試相關更新時，自動建置網站。
- 執行前端測試、解析器測試、題庫資料檢查。
- 建置 `dist/`。
- 發布到 GitHub Pages。

手動執行位置：

```text
GitHub repo -> Actions -> Deploy Pages -> Run workflow
```

### Update Exam Data

檔案位置：

```text
.github/workflows/update_exams.yml
```

用途：

- 每年 2 月 16 日與 10 月 16 日自動執行一次。
- 這個時間是用「近年醫師國考第一批約落在 1 到 2 月、第二批最晚可能落在 9 到 10 月」估算，並往後保留約半個月緩衝。
- 也可以在 GitHub Actions 手動執行。
- 下載考選部 PDF。
- 解析成網站使用的 JSON 題庫。
- 更新 `public/data/exams/` 與 `public/data/manifest.json`。
- 執行資料檢查、測試與網站建置。
- 預設會把更新後的題庫資料提交回 `main`。

手動執行位置：

```text
GitHub repo -> Actions -> Update Exam Data -> Run workflow
```

手動執行時要填：

```text
moex_year: 民國年，例如 115
preset: scripts/exams/moex_sources.py 裡的 preset 名稱，例如 physician-115-first
commit_changes: 是否自動提交更新，預設 true
```

## 重要資料位置

官方 PDF 來源設定：

```text
scripts/exams/moex_sources.py
```

PDF 暫存位置，不要提交到 GitHub：

```text
downloads/moex/
```

網站正式讀取的題庫：

```text
public/data/exams/
```

網站題庫目錄：

```text
public/data/manifest.json
```

資料品質報告：

```text
reports/dataset-quality.json
```

`reports/` 預設不提交到 GitHub，只作為本機或 GitHub Actions 執行時的檢查結果。

## 未來新增考試資料時

1. 到 `scripts/exams/moex_sources.py` 新增新的 preset。
2. preset 內要列出每一科的考選部代碼、年度、科目、是否有更正公告。
3. 到 GitHub Actions 手動執行 `Update Exam Data`。
4. 填入新的 `moex_year` 和 `preset`。
5. 確認 Actions 成功。
6. `Update Exam Data` 若有提交新資料，會觸發 `Deploy Pages` 自動上線。

## 給未來 AI Agent 的指令

```text
請幫我更新醫師國考題庫網站。

請先閱讀：
docs/automation.md

資料流程如下：

1. 官方考選部 PDF 來源設定在：
scripts/exams/moex_sources.py

2. PDF 暫存下載位置是：
downloads/moex/

3. 網站正式讀取的題庫 JSON 在：
public/data/exams/

4. 題庫目錄在：
public/data/manifest.json

5. 請不要把 downloads/moex/ 裡的 PDF 上傳到 GitHub。

請幫我做：

1. 新增本次考試的官方 PDF 來源 preset。
2. 下載試題、答案、必要時下載更正公告。
3. 解析成網站用 JSON。
4. 更新 public/data/exams/。
5. 更新 public/data/manifest.json。
6. 執行資料檢查與網站建置。
7. 如果只更新題目與答案，先不要產生 AI 詳解。
8. 如果要產生詳解，只修改題庫 JSON 的詳解欄位，並標記為待審核。
9. 最後請告訴我哪些檔案被修改，並提醒我到 GitHub Desktop 按 Commit + Push origin。
```

## AI 詳解原則

GitHub Actions 本身不產生詳解。未來可以接 OpenAI、Gemini、Claude 或其他 API，但詳解流程應該保持獨立。

AI 詳解只應該補題庫 JSON 的欄位，例如：

```json
{
  "key_point": "本題重點",
  "explanation": "完整詳解",
  "flashcard_summary": "閃卡摘要",
  "review_status": "ai_generated",
  "explanation_model": "模型名稱",
  "explanation_generated_at": "產生時間"
}
```

醫學詳解建議先經人工確認，再標記為 `reviewed`。
