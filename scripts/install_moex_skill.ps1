$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $repoRoot "skills\moex-extract"
$target = Join-Path $env:USERPROFILE ".codex\skills\moex-extract"
$oldTarget = Join-Path $env:USERPROFILE ".codex\skills\moex-exam-platform"

if (-not (Test-Path $source)) {
  throw "Skill source not found: $source"
}

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
if (Test-Path $oldTarget) {
  Remove-Item -Path $oldTarget -Recurse -Force
}
Copy-Item -Path $source -Destination $target -Recurse -Force

Write-Host "Installed global Codex skill: $target"
