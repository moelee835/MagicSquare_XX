# MagicSquare_XX — 로컬 가상환경(.venv) 생성 및 dev 설치
# PSSecurityException 시: .\scripts\setup.cmd 사용 (실행 정책 불필요)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$VenvPython = Join-Path $Root ".venv\Scripts\python.exe"
if (-not (Test-Path $VenvPython)) {
    Write-Host "Creating .venv ..."
    python -m venv .venv
}

Write-Host "Upgrading pip ..."
& $VenvPython -m pip install -U pip

Write-Host "Installing project (editable) with dev extras ..."
& $VenvPython -m pip install -e ".[dev]"

Write-Host ""
Write-Host "Done. Run tests (no Activate.ps1 required):"
Write-Host "  .\.venv\Scripts\python.exe -m pytest tests/entity/test_d_loc_01.py -v"
Write-Host "If PSSecurityException on Activate.ps1, use setup.cmd or activate.bat instead."
