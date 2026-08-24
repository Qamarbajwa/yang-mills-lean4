$ErrorActionPreference = "Stop"

Write-Host "=== Yang-Mills Mass Gap local setup ==="

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "Python was not found on PATH. Install Python 3.11+ first."
}

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt

New-Item -ItemType Directory -Force evidence\test_runs | Out-Null
New-Item -ItemType Directory -Force experiments\records | Out-Null
New-Item -ItemType Directory -Force checkpoints | Out-Null
New-Item -ItemType Directory -Force literature\primary | Out-Null
New-Item -ItemType Directory -Force literature\reviews | Out-Null
New-Item -ItemType Directory -Force proofs | Out-Null
New-Item -ItemType Directory -Force derivations | Out-Null
New-Item -ItemType Directory -Force numerical | Out-Null
New-Item -ItemType Directory -Force verification | Out-Null

Write-Host ""
Write-Host "Running initial verification..."
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
& .\.venv\Scripts\python.exe scripts\verify_and_record.py

Write-Host ""
Write-Host "Setup complete."
Write-Host "Next: initialize Git, make the initial commit, then run seal_checkpoint.py."
