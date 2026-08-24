$ErrorActionPreference = "Stop"
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
& .\.venv\Scripts\python.exe scripts\verify_and_record.py
