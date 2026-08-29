$ErrorActionPreference = "Stop"

Write-Host "Operating Systems Lab - Python setup"
Write-Host "------------------------------------"

$pythonCommand = $null

try {
    $null = Get-Command py -ErrorAction Stop
    $pythonCommand = "py"
} catch {
    try {
        $null = Get-Command python -ErrorAction Stop
        $pythonCommand = "python"
    } catch {
        Write-Host "Python 3 was not found."
        Write-Host "Install Python 3 and ensure it is available on PATH."
        exit 1
    }
}

& $pythonCommand --version

if (Test-Path ".venv") {
    Write-Host "Existing .venv found; reusing it."
} else {
    & $pythonCommand -m venv .venv
}

$venvPython = Join-Path (Get-Location) ".venv\Scripts\python.exe"

& $venvPython -m pip install --upgrade pip
if (Test-Path "requirements.txt") {
    & $venvPython -m pip install -r requirements.txt
}

Write-Host ""
Write-Host "Setup complete."
Write-Host "Activate later with:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host ""
Write-Host "Run an exercise with:"
Write-Host "  python path\to\program.py"
