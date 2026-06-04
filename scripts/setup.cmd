@echo off
REM MagicSquare_XX — .venv 생성 및 dev 설치 (PowerShell 실행 정책 불필요)
setlocal
cd /d "%~dp0\.."

if not exist ".venv\Scripts\python.exe" (
    echo Creating .venv ...
    python -m venv .venv
    if errorlevel 1 exit /b 1
)

echo Upgrading pip ...
.venv\Scripts\python.exe -m pip install -U pip
if errorlevel 1 exit /b 1

echo Installing project ^(editable^) with dev extras ...
.venv\Scripts\python.exe -m pip install -e ".[dev]"
if errorlevel 1 exit /b 1

echo.
echo Done. Run tests without Activate.ps1:
echo   .venv\Scripts\python.exe -m pytest tests/entity/test_d_loc_01.py -v
echo.
echo Optional CMD activate: .venv\Scripts\activate.bat
