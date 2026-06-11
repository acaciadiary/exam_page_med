---
name: moex-extract
description: Use when extracting, parsing, validating, updating, or deploying Taiwan MOEX exam-question datasets from official PDFs, including different ROC years, exam professions, subjects, answer corrections, React/Vite static SPA data, GitHub Pages deployment, and GitHub Actions scheduled updates. Also use when adding new MOEX source presets, parser rules, validation reports, or optional AI explanation generation with explicit cost controls.
---

# MOEX Exam Platform

Use this skill for Taiwan 考選部 (MOEX) exam-question projects: downloading official PDFs, parsing questions/answers/corrections into frontend JSON, validating datasets, building the React/Vite SPA, and deploying through GitHub Pages.

## Guardrails

- Answer in Traditional Chinese unless the user requests otherwise.
- Prefer official MOEX sources. Preserve source URLs in data or manifests.
- Do not call paid APIs by default. AI explanations are opt-in only after the user explicitly enables a provider, budget, and scope.
- Do not automate a logged-in browser session for Gemini/ChatGPT as a hidden API substitute. If the user wants Gemini via Chrome, discuss a manual or explicit export workflow first.
- Treat medical explanations as study aids, not clinical advice. Keep fields traceable and reviewable.
- Never commit raw downloaded PDFs, OCR dumps, tokens, browser profiles, `.tools/`, `downloads/`, `dist/`, `.env*`, or local caches.

## Standard Workflow

1. Inspect the repo first:
   - Read `package.json`, `vite.config.ts`, `.github/workflows/*.yml`, `scripts/exams/*`, `public/data/manifest.json`.
   - Check `git status` and avoid reverting user files.

2. Add or update MOEX sources:
   - Put official URLs and metadata in `scripts/exams/moex_sources.py`.
   - Model each source with year, subject id, title, group/stage, question URL, answer URL, and optional correction URL.
   - For new years/professions, create a new preset name instead of overwriting a working preset.

3. Download PDFs:
   - Prefer deterministic preset downloads:
     ```powershell
     python scripts/exams/download_moex.py --year <ROC_YEAR> --preset <PRESET> --out-dir downloads/moex
     ```
   - Keep downloads ignored by git.

4. Parse and build datasets:
   - Use `scripts/exams/build_moex_preset.py` to combine questions, answers, and corrections.
   - `correct_answers` should support multiple accepted answers.
   - `answer_status` should distinguish `standard`, `multiple_correct`, `all_credit`, and pending review.
   - Correction notes like `答A或C或AC者均給分`, `一律給分`, and `除未作答者不給分外，其餘均給分` must be represented.

5. Validate data quality:
   ```powershell
   python scripts/exams/validate_dataset.py "public/data/exams/**/*.json" --out reports/dataset-quality.json
   pytest tests/parser
   ```
   Validation should catch missing ids, duplicate question numbers, missing A-D options, missing answers, and option text accidentally swallowing the next question.

6. Frontend expectations:
   - React + Vite + TypeScript static SPA.
   - Read datasets from `public/data/manifest.json`.
   - Store markings/progress/mode in `localStorage`.
   - Exam mode: immediate feedback, marked sidebar, explanation panel.
   - Flashcard mode: 3D flip, separate flashcard markings.
   - Support light/dark themes and long-reading comfort.
   - Use `correct_answers` rather than assuming exactly one correct answer.

7. Test and build:
   ```powershell
   npm run test
   npm run build
   ```
   Keep Vitest include patterns scoped to project tests so browser profile files are not collected.

8. Deploy:
   - `vite.config.ts` should set GitHub Pages base from `GITHUB_REPOSITORY`.
   - Keep `public/.nojekyll`.
   - `deploy_pages.yml` should run frontend tests, parser tests, data validation, build, upload artifact, and deploy.
   - `update_exams.yml` should download, rebuild, validate, optionally generate explanations, test, build, then commit changed data.

## Optional AI Explanation Generation

Only implement or run explanation generation when the user explicitly opts in.

Required before running a paid provider:
- Provider name.
- API key or approved credential path.
- Model.
- Max questions or max estimated budget.
- Whether to overwrite existing explanations.

Safe first checks:
```powershell
python scripts/exams/generate_explanations.py "public/data/exams/**/*.json" --provider mock --limit 2 --report reports/explanation-generation.json
pytest tests/parser
npm run build
```

Generated fields should be:
- `key_point`
- `explanation`
- `flashcard_summary`
- `review_status`
- `explanation_model`
- `explanation_generated_at`

## GitHub Push/Pages Playbook

If system Git is unavailable:
- Install portable Git or GitHub CLI inside `.tools/`.
- Keep `.tools/` ignored.
- Use a clean remote URL without embedded tokens.
- Use temporary auth headers or `GH_TOKEN`; never commit tokens.

After pushing:
```powershell
gh run list --repo <owner>/<repo> --limit 5
gh run view <run-id> --log-failed
```

Verify Pages:
- Repository Actions run is success.
- Pages URL returns HTTP 200.
- HTML references `/<repo>/assets/...`.
- `public/data/manifest.json` and dataset JSONs are present in the deployed artifact.

## When Extending to New Exams

For a new profession/year:
- Add a new preset to `moex_sources.py`.
- Add fixtures for any new PDF layout edge cases.
- Run parser tests before full rebuild.
- Build to `public/data/exams/<year>/<subject>.json`.
- Update manifest through the build script, not by hand.
- Validate all datasets before commit.

Common MOEX PDF pitfalls:
- Chinese text may have dropped glyphs or replacement dots.
- Decimal numbers such as `3.9 mEq/L` must not become fake question boundaries.
- Option labels can be glued to previous text, e.g. `longusD.`.
- English A-D letters in prose must not be mistaken for answer options.
- Official correction PDFs may place answer rows before number rows.
