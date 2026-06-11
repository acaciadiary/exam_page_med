# 醫師國考 AI 備考平台

React + Vite 靜態 SPA，用於醫師國考題庫練習、閃卡複習、本機收藏與作答進度保存。詳解目前採「Gemini Pro 手動貼上」流程，不使用付費 API，也不會產生意料之外的 API 流量。

## 常用指令

```powershell
npm install
npm run dev
npm run build
npm run test
```

題庫資料放在：

- `public/data/manifest.json`
- `public/data/exams/<year>/<subject>.json`

## 題庫科目分類

前端已支援細分科目按鈕。題目 JSON 可加入：

- `category`：細分科目，例如 `心臟內科`
- `category_group`：較大分類，例如 `內科學`
- `category_source`：目前支援 `manual_range`、`auto`、`unassigned`

第一步先複製範本：

```powershell
Copy-Item scripts/exams/category_ranges.template.json scripts/exams/category_ranges.json
```

再把每科的題號區間填到 `ranges`，格式如下：

```json
{
  "start": 1,
  "end": 12,
  "category": "心臟內科",
  "category_group": "內科學"
}
```

套用到題庫：

```powershell
npm run apply:categories
npm run validate:data
npm run build
```

目前如果尚未填題號區間，網頁會顯示科目按鈕，但題目會先集中在「未分類」。

## MOEX 題庫流程

```powershell
npm run download:moex:115
npm run build:moex:115
npm run validate:data
```

## Gemini Pro 手動詳解流程

1. 匯出 prompt 批次檔：

```powershell
npm run export:gemini-prompts
```

2. 到 `reports/gemini_prompts/` 複製下一個 `.md` 檔內容，貼到你已登入 Gemini Pro 的 Chrome。
3. 把 Gemini 回傳 JSON 存到：

```txt
reports/gemini_outputs/
```

4. 匯入詳解：

```powershell
npm run import:gemini-explanations
npm run validate:explanations
```

匯入後會寫入：

- `key_point`
- `explanation`
- `flashcard_summary`
- `review_status`
- `explanation_model`
- `explanation_generated_at`

## GitHub Pages

```powershell
git init
git add .
git commit -m "feat: initialize medical exam prep app"
git branch -M main
git remote add origin https://github.com/<owner>/<repo>.git
git push -u origin main
```

GitHub repo 的 Settings -> Pages 選 GitHub Actions。`main` 分支 push 後會由 `.github/workflows/deploy_pages.yml` 建置與部署。
