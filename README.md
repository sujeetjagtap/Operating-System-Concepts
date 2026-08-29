# Operating-Systems-Concepts-Practical-Exercises

## Brief exercise description

### Chapter 2 - OS structures
* **2.24**
    * A simple program which copies the contents of a file to another file.

* **2.4**
    * A simple linux kernel module that creates a new entry in the `/proc` file-system that reports the number of seconds since the kernel module was loaded.

### Chapter 3 - Processes
* **3.19**
    * A program that measures the amount of time necessary to run a command from the command line. The given command is being run in a child process.
    * `time_pipe.c` - implements the communication between the two processes using a pipe.
    * `time_shared_memory.c` - implements the communication between the two processes using shared memory.

* **3.20**
    * Implements a basic API to allocate and release a process id using a bitmap.

* **3.21**
    * A program that generates the Collatz sequence of a given number in a child process.

* **3.22**
    * Same as **3.21**, but the child process saves the sequence in a shared-memory object.

* **3.26**
    * A program containing a short message exchange between two processes using ordinary pipes.

* **3.27**
    * A file-copying program using ordinary pipes.

* **UNIX Shell**
    * A program to serve as a shell interface that accepts user commands and then executes each command in a separate process.
    * It supports input and output redirections, as well as pipes as a form of inter-process communication between commands. However, a command may contain only one redirection or pipe - I plan on extending this functionality in the future.

* **Linux Kernel Module for Task Information**
    * A kernel module that uses the `/proc` file-system for displaying a task's information based on its process id.

* **Linux Kernel Module for Listing Tasks**
    * A kernel module that lists all tasks in a Linux system. This is implemented both linearly and depth first.

* **Kernel Data Structures**
    * A project which consists in using the kernel linked list structure.

### Chapter 4 - Threads & Concurrency
* **4.22**
    * A multithreaded program which computes statistical values for an array of numbers

* **4.24**
    * A multithreaded program which uses the Monte Carlo technique to approximate the value of pi.

* **Sudoku Solution Validator**
    * A program which checks whether a given sudoku solution is valid or not.
    * The validation for each separate row, column and 3x3 square is done in a separate thread.

* **Multithreaded sorting application**
    * A version of merge-sort which makes use of multithreading.
    * **Results**: you can literally see the speedup between sorting the array using 1 thread and using multiple threads. On my PC, the multithreaded version ran ~4 times faster.

## Python conversion

The Python implementations in this repository are **derived from the original C implementations** provided for the Operating Systems practical exercises.

The original C programs are used as the **reference implementations** for understanding the problem requirements, algorithmic approach, operating-system concepts, input/output behavior, and intended program functionality. Each applicable C program is reimplemented in **Python 3**, adapting the implementation to Python's programming model and standard library.

The purpose of the conversion is not merely to provide a separate Python solution, but to demonstrate how the **same Operating Systems concepts and practical problems can be implemented using Python**.

Where applicable, the Python implementation preserves:

- The original practical problem/question
- The underlying Operating Systems concept
- The major algorithm or approach used in the C implementation
- The expected input and output behavior
- The relevant process, thread, synchronization, IPC, file-system, or resource-management concepts

The original C source files are also retained in the repository for **side-by-side comparison and academic reference**.

### Important portability and kernel-module note

Some exercises in the original repository are implemented as **Linux kernel modules**. These cannot be directly translated into ordinary Python programs because Python programs execute in user space and cannot themselves serve as loadable Linux kernel modules.

For these exercises, the Python versions are therefore **user-space adaptations based on the original C/kernel-module implementation and the same Operating Systems concept**.

Depending on the exercise, the Python implementation uses appropriate user-space mechanisms such as:

- Linux `/proc` for obtaining process/task information
- Python process and threading facilities
- Python data structures to represent kernel-style structures
- Python timing facilities to reproduce observable timing behavior

These implementations preserve the **educational objective and observable functionality** of the original exercise while acknowledging the architectural difference between C kernel code and Python user-space code.

Consequently, the Python versions should be understood as:

> **C-reference-based Python implementations for regular programs, and conceptually equivalent user-space adaptations for Linux kernel-module exercises.**

### Python 3 setup and dependencies

The Python implementations are intended to run on Linux, Windows, and macOS. Use **Python 3.10 or newer** where possible. The core exercises primarily use Python's standard library, so no third-party packages are normally required.

### Debian / Ubuntu / Debian-based Linux

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
python3 -m pip --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run an exercise with `python path/to/program.py`. If `requirements.txt` contains no external dependencies, the install command completes without adding packages. Finish with `deactivate`.

### Red Hat / Fedora / Rocky / AlmaLinux

```bash
sudo dnf install python3 python3-pip
python3 --version
python3 -m pip --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If your specific RHEL-family release packages virtual-environment support separately, install the distribution-provided package as indicated by that release. Avoid `sudo pip install`; use the virtual environment.

### BSD

#### FreeBSD

```bash
sudo pkg install python3 py311-pip
python3 --version
python3 -m pip --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

#### OpenBSD

```bash
doas pkg_add python3 py3-pip
python3 --version
python3 -m pip --version
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Other BSD variants use their own package managers; install Python 3, pip, and venv support using the native package system before following the common virtual-environment steps.

### Windows 10 / 11

Install Python 3 from the official Python distribution or your institution's approved software source. Enable **Add Python to PATH** during installation when offered.

PowerShell:

```powershell
py --version
py -m pip --version
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell execution policy prevents activation, run the environment's interpreter directly:

```powershell
.venv\Scripts\python.exe path\to\program.py
```

Command Prompt activation:

```cmd
.venv\Scripts\activate.bat
```

### macOS

Using Homebrew:

```bash
brew install python
python3 --version
python3 -m pip --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

You may also install Python 3 using the official Python installer. After installation, use `python3` to create the environment if that is the command provided by your system.

### Verify the setup

From the repository root, after activating the virtual environment:

```bash
python --version
python -m pip --version
python -m compileall .
```

`compileall` checks Python syntax without executing the programs.

### Platform-specific OS exercises

Some original exercises model Linux kernel facilities. Ordinary Python runs in user space and cannot itself be a loadable Linux kernel module. The converted repository therefore uses documented **user-space analogues**, such as Linux `/proc`, elapsed-time APIs, and Python data structures. Exercises that explicitly depend on `/proc` should be run on Linux. Windows and macOS do not provide the same Linux `/proc` interface.

### Recommended student workflow

1. Open a terminal in the repository root.
2. Create/activate `.venv`.
3. Read the experiment's `README.md`.
4. Run the supplied Python program and sample test cases.
5. Try additional inputs and record observations/results.
6. Use the lab record template for submission.
7. Deactivate the virtual environment when finished.

### Troubleshooting

- If `python` is unavailable on Windows, try `py`.
- If `pip` is unavailable, use `python -m pip` (or `python3 -m pip`).
- If package installation gives permission errors, use a virtual environment rather than system-wide pip installation.
- If a `/proc` exercise fails, confirm that you are running Linux and that `/proc` is mounted: `ls /proc`.
- If dependencies are unnecessary for a particular exercise, Python's standard library is sufficient.


## One-command setup

The repository includes platform-specific setup scripts in the `setup/`
directory. These scripts create the `.venv` virtual environment in the
**repository root**, upgrade `pip`, and install packages from `requirements.txt`.

> **Important:** Run these commands from the repository root, not from inside
> the `setup/` directory.

### Linux / macOS / BSD

```bash
chmod +x setup/setup.sh
./setup/setup.sh
```

Activate the environment:

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.\setup\setup.ps1
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
setup\setup.bat
```

Activate:

```cmd
.venv\Scripts\activate.bat
```

### Manual alternative

If you prefer not to use the setup scripts, follow the detailed platform-specific
instructions above and create the environment manually with:

```bash
python3 -m venv .venv
```

or, on Windows:

```powershell
py -m venv .venv
```

### Dependency policy

The current laboratory programs rely on the **Python standard library**, so
`requirements.txt` is intentionally empty of third-party runtime packages.
If a future exercise introduces a third-party dependency, add it to
`requirements.txt`; the setup scripts will install it automatically.

See [`setup/README.md`](setup/README.md) for the complete setup instructions.

## Running the programs

Use Python 3. Most examples can be run directly with `python3 <program>.py`; each directory now contains a README with the theory, question, and a usage example where applicable. Linux-specific `/proc` exercises should be run on Linux.


## Setup scripts

Platform-specific environment setup scripts are provided in the `setup/`
directory. See [`setup/README.md`](setup/README.md) for detailed instructions.

From the repository root:

- Linux / macOS / BSD: `./setup/setup.sh`
- Windows PowerShell: `.\setup\setup.ps1`
- Windows CMD: `setup\setup.bat`
