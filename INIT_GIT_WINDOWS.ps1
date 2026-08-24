$ErrorActionPreference = "Stop"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git was not found on PATH."
}

if (-not (Test-Path ".git")) {
    git init
}

git add .
Write-Host ""
Write-Host "Review staged files with: git status"
Write-Host "Then create the human/operator initial commit, for example:"
Write-Host 'git commit -m "YM-000: bootstrap governed research repository"'
