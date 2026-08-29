# Operating Systems Lab — Environment Setup

This directory contains the scripts used to prepare the Python environment for
the **Operating Systems Laboratory – Python** repository.

The repository supports:

- Debian / Ubuntu and other Debian-based Linux distributions
- Red Hat / Fedora / Rocky / AlmaLinux
- FreeBSD / OpenBSD
- Windows 10 / 11
- macOS

> **Important:** Run the setup scripts from the **repository root**, not from
> inside this `setup` directory. The scripts create `.venv` in the repository
> root and use the root-level `requirements.txt`.

## Repository Structure

```text
Operating-Systems-Lab-Python-Only/
│
├── setup/
│   ├── README.md
│   ├── setup.sh
│   ├── setup.ps1
│   └── setup.bat
│
├── requirements.txt
├── README.md
│
├── Chapter-2/
├── Chapter-3/
├── Chapter-4/
└── ...
```

---

## 1. Linux / macOS / BSD — `setup.sh`

The same shell script can be used on Linux, macOS, and BSD systems.

### Step 1 — Open a terminal

Go to the repository root:

```bash
cd /path/to/Operating-Systems-Lab-Python-Only
```

### Step 2 — Install Python 3

#### Debian / Ubuntu

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### Fedora / RHEL / Rocky / AlmaLinux

```bash
sudo dnf install python3 python3-pip
```

If your distribution requires a separate package for virtual environments,
install the appropriate Python venv package provided by the distribution.

#### FreeBSD

```bash
sudo pkg install python3 py311-pip
```

#### OpenBSD

```bash
doas pkg_add python3 py3-pip
```

#### macOS

Using Homebrew:

```bash
brew install python
```

Alternatively, install Python 3 using the official Python distribution.

Verify Python:

```bash
python3 --version
python3 -m pip --version
```

### Step 3 — Make the setup script executable

```bash
chmod +x setup/setup.sh
```

### Step 4 — Run the setup script

```bash
./setup/setup.sh
```

The script will:

1. Detect Python 3.
2. Create `.venv` in the repository root.
3. Upgrade `pip`.
4. Install packages from `requirements.txt`.

### Step 5 — Activate the environment

```bash
source .venv/bin/activate
```

Verify:

```bash
python --version
python -m pip --version
```

---

## 2. Windows PowerShell — `setup.ps1`

### Step 1 — Open PowerShell

Navigate to the repository root:

```powershell
cd C:\path\to\Operating-Systems-Lab-Python-Only
```

### Step 2 — Run the setup script

```powershell
.\setup\setup.ps1
```

### Step 3 — Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

Verify:

```powershell
python --version
python -m pip --version
```

### If PowerShell blocks script execution

If your Windows policy prevents local scripts from running, you may need:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then retry:

```powershell
.\setup\setup.ps1
```

Use your institution's IT policy if execution-policy changes are restricted.

---

## 3. Windows Command Prompt — `setup.bat`

### Step 1 — Open Command Prompt

```cmd
cd C:\path\to\Operating-Systems-Lab-Python-Only
```

### Step 2 — Run the setup script

```cmd
setup\setup.bat
```

### Step 3 — Activate the environment

```cmd
.venv\Scripts\activate.bat
```

Verify:

```cmd
python --version
python -m pip --version
```

---

## 4. Running a Laboratory Program

After activating `.venv`, run an experiment from the repository root:

```bash
python path/to/program.py
```

On Windows:

```powershell
python path\to\program.py
```

Always check the `README.md` inside the relevant experiment directory first.
It contains the theory, question, execution instructions, and any
platform-specific notes.

---

## 5. Checking the Installation

Run:

```bash
python --version
python -m pip --version
```

You can check the Python source files for syntax errors with:

```bash
python -m compileall .
```

---

## 6. Dependencies

The current laboratory implementations use Python's **standard library**.
Therefore, no third-party runtime packages are currently required.

The root-level `requirements.txt` is retained so that future exercises can
declare additional dependencies without changing the setup procedure.

---

## 7. Linux-Specific Exercises

Some exercises model Linux kernel concepts through Linux `/proc`.

For example:

```text
/proc
```

is a Linux kernel interface and is not available in the same form on Windows
or macOS.

Such exercises should be run on:

- Native Linux
- A Linux virtual machine
- WSL on Windows, where appropriate

The README in each experiment identifies Linux-specific requirements.

---

## 8. Recommended Student Workflow

1. Open a terminal in the repository root.
2. Run the appropriate setup script once.
3. Activate `.venv`.
4. Open the README of the required experiment.
5. Read the theory and practical question.
6. Run the Python implementation.
7. Test the program with the supplied and additional test cases.
8. Record the output, observations, and conclusion.
9. Deactivate the environment when finished, if desired.

### Quick Reference

| Platform | Setup | Activate |
|---|---|---|
| Debian / Ubuntu | `./setup/setup.sh` | `source .venv/bin/activate` |
| Fedora / RHEL | `./setup/setup.sh` | `source .venv/bin/activate` |
| FreeBSD | `./setup/setup.sh` | `source .venv/bin/activate` |
| OpenBSD | `./setup/setup.sh` | `source .venv/bin/activate` |
| macOS | `./setup/setup.sh` | `source .venv/bin/activate` |
| Windows PowerShell | `.\setup\setup.ps1` | `.\.venv\Scripts\Activate.ps1` |
| Windows CMD | `setup\setup.bat` | `.venv\Scripts\activate.bat` |

**Always execute the setup script from the repository root.**
