@echo off
setlocal

echo Operating Systems Lab - Python setup
echo ------------------------------------

where py >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=py
) else (
    where python >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        set PYTHON_CMD=python
    ) else (
        echo Python 3 was not found.
        echo Install Python 3 and ensure it is available on PATH.
        exit /b 1
    )
)

%PYTHON_CMD% --version

if not exist ".venv\Scripts\python.exe" (
    %PYTHON_CMD% -m venv .venv
)

.venv\Scripts\python.exe -m pip install --upgrade pip
if exist "requirements.txt" (
    .venv\Scripts\python.exe -m pip install -r requirements.txt
)

echo.
echo Setup complete.
echo Activate later with:
echo   .venv\Scripts\activate.bat
echo.
echo Run an exercise with:
echo   python path\to\program.py
