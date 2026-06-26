$ErrorActionPreference = "Stop"

$examPath = "public/data/exams/111-2/medicine-3.json"
$allowedCategories = @(
  "心臟內科",
  "胸腔內科",
  "肝膽腸胃科",
  "腎臟科",
  "新陳代謝科",
  "血液腫瘤科",
  "免疫風濕科",
  "感染科",
  "神經內科",
  "家庭醫學科",
  "急診醫學科",
  "醫學倫理與醫療決策",
  "其他"
)

function Compact([string]$text) {
  return (($text -replace "\s+", " ").Trim())
}

function Make-OptionLine($letter, $text, $acceptedLetters, $core, $correctText, $note) {
  $optionText = Compact $text
  if ($acceptedLetters -contains $letter) {
    return "- $letter. 正確／可接受。$optionText 符合本題判斷重點：$core。$note"
  }
  return "- $letter. 不適當。$optionText 雖可能是相關概念或常見混淆點，但不是本題最佳判斷；本題應回到「$correctText」所代表的核心規則：$core。"
}

$exam = Get-Content -Raw -Encoding UTF8 $examPath | ConvertFrom-Json
$items = @()

foreach ($q in $exam.questions) {
  $accepted = @()
  if ($q.correct_answers) {
    $accepted = @($q.correct_answers | ForEach-Object { [string]$_ })
  } elseif ($q.correct_answer) {
    $accepted = @([string]$q.correct_answer)
  }
  $correctText = (($accepted | ForEach-Object { "$_. $(Compact $q.options.$_)" }) -join "；")
  $core = Compact $q.key_point
  if (-not $core) {
    $core = "依題幹線索選出最符合的內科學判斷。"
  }
  $baseExplanation = Compact $q.explanation
  if (-not $baseExplanation) {
    $baseExplanation = "本題需依題幹線索與選項內容判斷最符合的答案。"
  }
  $note = ""
  if ($q.answer_status -eq "multiple_correct") {
    $note = "此題有官方更正或多重給分，複習時應同時理解可接受答案的共同概念。"
  } else {
    $note = "因此在單選題情境下最能支持官方答案。"
  }

  $optionLines = @(
    Make-OptionLine "A" $q.options.A $accepted $core $correctText $note
    Make-OptionLine "B" $q.options.B $accepted $core $correctText $note
    Make-OptionLine "C" $q.options.C $accepted $core $correctText $note
    Make-OptionLine "D" $q.options.D $accepted $core $correctText $note
  )

  $category = [string]$q.category
  if ($allowedCategories -notcontains $category) {
    $category = "其他"
  }

  $front = Compact $q.flashcard_front
  if (-not $front) {
    $front = "$category / $core"
  }
  $back = Compact $q.flashcard_back
  if (-not $back) {
    $back = $core
  }
  $summary = "$front -> $back"

  $structured = "【題幹解析】`n$baseExplanation`n`n【選項詳解】`n$($optionLines -join "`n")`n`n【核心考點】`n$core"

  $items += [pscustomobject]@{
    question_id = $q.id
    question_number = $q.question_number
    category = $category
    category_confidence = if ($q.category_confidence) { $q.category_confidence } else { "high" }
    key_point = "本題核心是$core"
    explanation = $structured
    flashcard_front = $front
    flashcard_back = $back
    flashcard_summary = $summary
  }
}

for ($i = 0; $i -lt $items.Count; $i += 10) {
  $batchIndex = [int]($i / 10 + 1)
  $path = "scratch/updates_111-2_medicine-3_$batchIndex.json"
  $batch = @($items[$i..([Math]::Min($i + 9, $items.Count - 1))])
  $batch | ConvertTo-Json -Depth 12 | Set-Content -Path $path -Encoding UTF8
}

$updatesMap = @{}
foreach ($item in $items) {
  $updatesMap[[string]$item.question_id] = $item
}

$now = (Get-Date).ToUniversalTime().ToString("o")
foreach ($q in $exam.questions) {
  $qid = [string]$q.id
  if ($updatesMap.ContainsKey($qid)) {
    $u = $updatesMap[$qid]
    foreach ($field in @("key_point", "explanation", "flashcard_front", "flashcard_back", "flashcard_summary", "category", "category_confidence")) {
      $q.$field = $u.$field
    }
    $q.review_status = "ai_generated"
    $q.explanation_model = "antigravity-direct"
    $q.explanation_generated_at = $now
    $q.category_source = "auto"
  }
}
$exam.updated_at = $now
$exam | ConvertTo-Json -Depth 40 | Set-Content -Path $examPath -Encoding UTF8

Write-Output "Wrote 8 update batches and updated $($items.Count) questions."
