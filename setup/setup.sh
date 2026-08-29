#!/usr/bin/env bash
set -e

echo "Operating Systems Lab - Python setup"
echo "------------------------------------"

PYTHON_CMD=""

if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
else
    echo "Python 3 was not found."
    echo "Please install Python 3 using your operating system's package manager."
    exit 1
fi

echo "Using: $PYTHON_CMD"
"$PYTHON_CMD" --version

if ! "$PYTHON_CMD" -m venv .venv; then
    echo
    echo "Could not create the virtual environment."
    echo "On Debian/Ubuntu, install python3-venv."
    echo "On RHEL/Fedora-family systems, install the appropriate Python venv package if required."
    exit 1
fi

echo "Activating virtual environment..."
# shellcheck disable=SC1091
source .venv/bin/activate

python -m pip install --upgrade pip
if [ -f requirements.txt ]; then
    python -m pip install -r requirements.txt
fi

echo
echo "Setup complete."
echo "Activate later with:"
echo "  source .venv/bin/activate"
echo
echo "Run an exercise with:"
echo "  python path/to/program.py"
