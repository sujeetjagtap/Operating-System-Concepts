# Operating Systems Lab

## Environment Setup for Introductory Lab

This guide prepares your computer to practise all four Operating Systems
laboratory experiments using either:

-   **Windows + WSL (Windows Subsystem for Linux) + Ubuntu**
-   **macOS + Terminal**

The four experiments are:

1.  **Basics of UNIX Commands**
2.  **System Calls of UNIX**
3.  **C Programs to Simulate UNIX Commands**
4.  **Simple Shell Programs**

------------------------------------------------------------------------

# 1. What You Need

| Requirement | Windows | macOS |
|---|---|---|
| Terminal | Windows Terminal / Ubuntu terminal | Terminal |
| UNIX/Linux environment | WSL 2 + Ubuntu | macOS Terminal |
| Shell | Bash | zsh/bash |
| C compiler | GCC | Clang |
| Text editor | `vi`/`vim`, optional VS Code | `vi`/`vim`, optional VS Code |
| Manual pages | `man` | `man` |
| Calculator | `bc` | `bc` |
| Shell scripting | Bash | Bash/zsh |

You do **not** need a separate virtual machine or dual-boot installation
for these laboratory exercises.

------------------------------------------------------------------------

# 2. Option A -- Windows Using WSL

## 2.1 What is WSL?

WSL (Windows Subsystem for Linux) provides a Linux environment directly
inside Windows. For these laboratory exercises, use **WSL 2 with
Ubuntu**.

Microsoft's current installation method uses:

``` powershell
wsl --install
```

This installs the required WSL components and, by default, Ubuntu. A
restart may be required.

------------------------------------------------------------------------

## 2.2 Install WSL and Ubuntu

### Step 1 -- Open PowerShell as Administrator

1.  Open the Windows Start menu.
2.  Search for **PowerShell**.
3.  Right-click **Windows PowerShell** or **PowerShell**.
4.  Select **Run as administrator**.

### Step 2 -- Install WSL

``` powershell
wsl --install
```

Restart Windows if requested.

### Step 3 -- Complete Ubuntu setup

After restarting, Ubuntu may open automatically.

You will be asked to create:

-   A Linux username
-   A Linux password

The Linux password is used when running commands with `sudo`.

> When entering a password in a Linux terminal, characters may not
> appear on the screen. This is normal. Type the password and press
> Enter.

------------------------------------------------------------------------

## 2.3 Check the WSL Installation

Open Ubuntu from the Start menu and run:

``` bash
wsl --version
```

You can also run:

``` bash
uname -a
```

and:

``` bash
lsb_release -a
```

If `lsb_release` is not available, use:

``` bash
cat /etc/os-release
```

------------------------------------------------------------------------

## 2.4 Update Ubuntu

Inside Ubuntu:

``` bash
sudo apt update
```

Then:

``` bash
sudo apt upgrade
```

If asked for confirmation, type:

``` text
Y
```

and press Enter.

------------------------------------------------------------------------

# 3. Install the Required Linux Tools in WSL

Run:

``` bash
sudo apt install build-essential
```

This provides the tools required for compiling C programs.

Install the editors and utilities used in the labs:

``` bash
sudo apt install vim ed bc man-db
```

You may also install `emacs` if you want to practise the EMACS section:

``` bash
sudo apt install emacs
```

Verify the important tools:

``` bash
gcc --version
```

``` bash
bc --version
```

``` bash
vi --version
```

``` bash
man --version
```

Check the shell:

``` bash
echo $SHELL
```

------------------------------------------------------------------------

# 4. Create the Operating Systems Lab Workspace

Create a dedicated directory:

``` bash
mkdir -p ~/OS-Lab
```

Move into it:

``` bash
cd ~/OS-Lab
```

Create four experiment directories:

``` bash
mkdir Experiment-1
mkdir Experiment-2
mkdir Experiment-3
mkdir Experiment-4
```

Check them:

``` bash
ls
```

You should see:

``` text
Experiment-1
Experiment-2
Experiment-3
Experiment-4
```

------------------------------------------------------------------------

# 5. Recommended WSL File Location

For Linux-based laboratory work, keep your lab files inside the Linux
file system:

``` text
/home/<username>/OS-Lab
```

For example:

``` bash
cd ~/OS-Lab
```

Avoid doing regular compilation and build work from a Windows-mounted
path such as:

``` text
/mnt/c/Users/<username>/...
```

Keeping Linux projects inside the WSL Linux file system provides better
performance for Linux tools.

------------------------------------------------------------------------

# 6. Access Your WSL Files from Windows

From Ubuntu, you can open the current directory in Windows File
Explorer:

``` bash
explorer.exe .
```

You can also access the WSL file system from Windows File Explorer
through the WSL network location.

Use Windows applications for editing if desired, but perform the
compilation and execution of these experiments inside Ubuntu/WSL.

------------------------------------------------------------------------

# 7. Option B -- macOS Using Terminal

macOS already provides a UNIX-like command-line environment.

Open:

**Applications → Utilities → Terminal**

or press:

``` text
Command + Space
```

and search for:

``` text
Terminal
```

------------------------------------------------------------------------

# 8. Check the macOS Terminal Environment

Open Terminal and run:

``` bash
uname -a
```

Check the shell:

``` bash
echo $SHELL
```

Check the current directory:

``` bash
pwd
```

List files:

``` bash
ls
```

------------------------------------------------------------------------

# 9. Install Apple's Command-Line Tools

To compile the C programs, install the Apple Command Line Tools.

Run:

``` bash
xcode-select --install
```

A macOS installation dialog should appear.

Complete the installation and then verify the compiler:

``` bash
clang --version
```

You can also check:

``` bash
cc --version
```

macOS normally provides `clang` rather than GCC as its system C
compiler.

For the laboratory programs, `clang` is sufficient.

------------------------------------------------------------------------

# 10. Create the Operating Systems Lab Workspace on macOS

Create the main directory:

``` bash
mkdir -p ~/OS-Lab
```

Move into it:

``` bash
cd ~/OS-Lab
```

Create the experiment directories:

``` bash
mkdir Experiment-1 Experiment-2 Experiment-3 Experiment-4
```

Check:

``` bash
ls
```

------------------------------------------------------------------------

# 11. Basic Terminal Skills to Know Before Starting

The following commands are used throughout the four experiments.

## Show the current directory

``` bash
pwd
```

## List files

``` bash
ls
```

## List all files

``` bash
ls -a
```

## Create a directory

``` bash
mkdir dirname
```

## Enter a directory

``` bash
cd dirname
```

## Move to the parent directory

``` bash
cd ..
```

## Return to your home directory

``` bash
cd ~
```

## Create a file

``` bash
touch filename
```

## Display a file

``` bash
cat filename
```

## Copy a file

``` bash
cp source destination
```

## Rename/move a file

``` bash
mv oldname newname
```

## Remove a file

``` bash
rm filename
```

## Clear the terminal

``` bash
clear
```

------------------------------------------------------------------------

# 12. Practising Experiment 1 -- Basics of UNIX Commands

Move to Experiment 1:

``` bash
cd ~/OS-Lab/Experiment-1
```

Practise the commands in the Experiment 1 manual.

## Date and Calendar

``` bash
date
```

``` bash
cal
```

``` bash
date +%m
date +%h
date +%d
date +%y
date +%H
date +%M
date +%S
```

## Display Messages

``` bash
echo "Hello World"
```

## Directory Listing

``` bash
ls
```

``` bash
ls -l
```

``` bash
ls -a
```

``` bash
ls -lh
```

## User and System Information

``` bash
who
```

``` bash
whoami
```

``` bash
uptime
```

``` bash
uname -a
```

``` bash
hostname
```

## Calculator

``` bash
bc
```

Try:

``` text
10/2*3
```

Exit using:

``` text
quit
```

You can also use:

``` bash
bc -l
```

## File Manipulation

Create a file:

``` bash
touch student
```

Add content:

``` bash
cat > student
```

Type a few lines and press:

``` text
Ctrl+D
```

View the file:

``` bash
cat student
```

Copy it:

``` bash
cp student student-copy
```

Rename it:

``` bash
mv student-copy student2
```

Search it:

``` bash
grep "word" student
```

View the beginning:

``` bash
head student
```

View the end:

``` bash
tail student
```

Count lines, words and bytes:

``` bash
wc -l student
wc -w student
wc -c student
```

------------------------------------------------------------------------

# 13. Practising Experiment 2 -- UNIX System Calls

Move to Experiment 2:

``` bash
cd ~/OS-Lab/Experiment-2
```

Create a C source file:

``` bash
vi directory.c
```

or:

``` bash
nano directory.c
```

Enter the `opendir()`, `readdir()`, and `closedir()` program from
Experiment 2.

Compile:

### Linux / WSL

``` bash
gcc directory.c -o directory
```

### macOS

``` bash
clang directory.c -o directory
```

Run:

``` bash
./directory
```

If the program expects a directory name as input, enter:

``` text
.
```

The `.` represents the current directory.

------------------------------------------------------------------------

## 13.1 Practise `fork()` and `getpid()`

Create:

``` bash
vi process.c
```

Enter the `fork()`, `getpid()`, and `exit()` program from Experiment 2.

Compile:

### Linux / WSL

``` bash
gcc process.c -o process
```

### macOS

``` bash
clang process.c -o process
```

Run:

``` bash
./process
```

Observe the parent and child process IDs.

------------------------------------------------------------------------

# 14. Practising Experiment 3 -- Simulating UNIX Commands

Move to Experiment 3:

``` bash
cd ~/OS-Lab/Experiment-3
```

The experiment contains C programs corresponding to:

-   `cp`
-   `ls`
-   `grep`

## 14.1 Compile a C Program

### Linux / WSL

``` bash
gcc program.c -o program
```

### macOS

``` bash
clang program.c -o program
```

Run:

``` bash
./program
```

------------------------------------------------------------------------

## 14.2 Simulating `ls`

Compile the corresponding `ls` simulation program:

``` bash
gcc ls_sim.c -o ls_sim
```

or on macOS:

``` bash
clang ls_sim.c -o ls_sim
```

Run it by supplying a directory:

``` bash
./ls_sim .
```

The `.` means the current directory.

You can also try:

``` bash
./ls_sim ..
```

------------------------------------------------------------------------

## 14.3 Simulating `grep`

The program from the lab accepts:

``` text
filename
word
```

Compile:

``` bash
gcc grep_sim.c -o grep_sim
```

or:

``` bash
clang grep_sim.c -o grep_sim
```

Run:

``` bash
./grep_sim student "anu"
```

The general form is:

``` bash
./grep_sim <filename> <word>
```

------------------------------------------------------------------------

# 15. Practising Experiment 4 -- Shell Programming

Move to Experiment 4:

``` bash
cd ~/OS-Lab/Experiment-4
```

Shell programs do not need to be compiled with GCC or Clang.

Create a shell script:

``` bash
vi even_odd.sh
```

Enter the even/odd shell program from Experiment 4.

------------------------------------------------------------------------

# 16. Running a Shell Script

There are two common methods.

## Method 1 -- Run using Bash

``` bash
bash even_odd.sh
```

This method does not require executable permission.

## Method 2 -- Make the script executable

``` bash
chmod +x even_odd.sh
```

Then run:

``` bash
./even_odd.sh
```

------------------------------------------------------------------------

# 17. Recommended Shell Script Format

A shell script can begin with:

``` bash
#!/bin/bash
```

Example:

``` bash
#!/bin/bash

echo "Enter the Number"
read n

r=`expr $n % 2`

if [ $r -eq 0 ]
then
    echo "$n is Even number"
else
    echo "$n is Odd number"
fi
```

Save the file as:

``` text
even_odd.sh
```

Run:

``` bash
bash even_odd.sh
```

------------------------------------------------------------------------

# 18. Practise All Four Shell Programs

## Program 1 -- Even or Odd

``` bash
bash even_odd.sh
```

## Program 2 -- Leap Year

Create:

``` text
leap_year.sh
```

Run:

``` bash
bash leap_year.sh
```

## Program 3 -- Factorial

Create:

``` text
factorial.sh
```

Run:

``` bash
bash factorial.sh
```

## Program 4 -- Swap Two Integers

Create:

``` text
swap.sh
```

Run:

``` bash
bash swap.sh
```

------------------------------------------------------------------------

# 19. Using `vi` During the Lab

The experiments introduce UNIX editors, including `vi`.

Start `vi`:

``` bash
vi test.txt
```

Press:

``` text
i
```

to enter insert mode.

Type some text.

Press:

``` text
Esc
```

to return to command mode.

Save and exit:

``` text
:wq
```

Exit without saving:

``` text
:q!
```

------------------------------------------------------------------------

# 20. EMACS Practice

EMACS is not necessarily installed by default.

### Ubuntu / WSL

Install it with:

``` bash
sudo apt install emacs
```

Start:

``` bash
emacs
```

If you only need the command references from the lab, EMACS installation
is optional.

------------------------------------------------------------------------

# 21. Important Difference Between WSL and macOS

Most commands used in Experiments 1--4 are UNIX/Linux commands and
behave similarly in WSL and macOS.

| Activity | WSL / Ubuntu | macOS |
|---|---|---|
| Shell | Bash | zsh by default |
| C compiler | `gcc` | `clang` |
| `ls` | Yes | Yes |
| `grep` | Yes | Yes |
| `cat` | Yes | Yes |
| `cp` | Yes | Yes |
| `mv` | Yes | Yes |
| `rm` | Yes | Yes |
| `cut` | Yes | Yes |
| `head` | Yes | Yes |
| `tail` | Yes | Yes |
| `wc` | Yes | Yes |
| `bc` | Yes | Yes |
| `vi` | Usually available | Available |
| `man` | Available after packages are installed | Available |
| `fork()` | Yes | Yes |
| `opendir()` / `readdir()` | Yes | Yes |
| Bash scripts | Yes | Yes |

------------------------------------------------------------------------

# 22. Compiling C Programs -- Quick Reference

## Windows + WSL

``` bash
gcc source.c -o program
./program
```

Example:

``` bash
gcc process.c -o process
./process
```

## macOS

``` bash
clang source.c -o program
./program
```

Example:

``` bash
clang process.c -o process
./process
```

------------------------------------------------------------------------

# 23. Handling Compilation Errors

If the compiler reports an error, first check:

### 1. Is the source file present?

``` bash
ls
```

### 2. Did you type the filename correctly?

``` bash
ls *.c
```

### 3. Is the compiler available?

Linux / WSL:

``` bash
gcc --version
```

macOS:

``` bash
clang --version
```

### 4. Did you compile before running?

``` bash
gcc program.c -o program
```

or:

``` bash
clang program.c -o program
```

### 5. Does the executable exist?

``` bash
ls -l
```

Then run:

``` bash
./program
```

------------------------------------------------------------------------

# 24. Understanding `./`

When you type:

``` bash
./program
```

`./` means:

> Run the program named `program` from the current directory.

For example:

``` bash
./process
```

runs the executable `process` located in the current directory.

------------------------------------------------------------------------

# 25. Common Mistakes to Avoid

## Mistake 1 -- Typing the `$` prompt

If a manual shows:

``` text
$ ls -l
```

type only:

``` bash
ls -l
```

Do not type `$`.

## Mistake 2 -- Forgetting spaces

Correct:

``` bash
ls -l
```

Not:

``` bash
ls-l
```

Correct:

``` bash
cat file1 file2 > file3
```

## Mistake 3 -- Running a C source file directly

Do not use:

``` bash
./program.c
```

Compile first:

``` bash
gcc program.c -o program
```

Then:

``` bash
./program
```

On macOS:

``` bash
clang program.c -o program
./program
```

## Mistake 4 -- Forgetting executable permission for scripts

If using:

``` bash
./script.sh
```

make it executable:

``` bash
chmod +x script.sh
```

Alternatively:

``` bash
bash script.sh
```

## Mistake 5 -- Working in the wrong directory

Check:

``` bash
pwd
```

Then:

``` bash
ls
```

------------------------------------------------------------------------

# 26. Recommended Lab Folder Structure

Maintain the following structure:

``` text
OS-Lab/
├── Experiment-1/
│   ├── practice/
│   └── notes/
│
├── Experiment-2/
│   ├── directory.c
│   ├── process.c
│   └── practice/
│
├── Experiment-3/
│   ├── cp_sim.c
│   ├── ls_sim.c
│   ├── grep_sim.c
│   └── practice/
│
└── Experiment-4/
    ├── even_odd.sh
    ├── leap_year.sh
    ├── factorial.sh
    ├── swap.sh
    └── practice/
```

You may use different filenames, but keep each experiment in its own
directory.

------------------------------------------------------------------------

# 27. Final Verification Checklist

## Windows + WSL

``` bash
uname -a
```

``` bash
gcc --version
```

``` bash
bc --version
```

``` bash
vi --version
```

``` bash
man ls
```

``` bash
echo $SHELL
```

## macOS

``` bash
uname -a
```

``` bash
clang --version
```

``` bash
bc --version
```

``` bash
vi --version
```

``` bash
man ls
```

``` bash
echo $SHELL
```

If these commands work, the main environment required for the four
experiments is ready.

------------------------------------------------------------------------

# 28. First Practice Session

After completing the setup, practise the following sequence:

``` bash
mkdir -p ~/OS-Lab/Practice
cd ~/OS-Lab/Practice

date
ls
pwd
whoami
uname -a

touch student.txt
cat > student.txt
```

Enter three lines of text and press:

``` text
Ctrl+D
```

Then run:

``` bash
cat student.txt
wc -l student.txt
wc -w student.txt
head student.txt
tail student.txt
grep "your-word" student.txt
cp student.txt student-copy.txt
mv student-copy.txt student-renamed.txt
ls -l
rm student-renamed.txt
```

Finally:

``` bash
cd ..
ls
```

You are now ready to begin Experiments 1--4.

------------------------------------------------------------------------

# 29. Lab Practice Workflow

For every experiment, follow this workflow:

``` text
Read the objective
       ↓
Read the algorithm
       ↓
Create the source/script file
       ↓
Type the program
       ↓
Compile (C programs)
       ↓
Run the program
       ↓
Test with different inputs
       ↓
Observe the output
       ↓
Record the result
```

For C programs:

``` text
source.c
   ↓
gcc / clang
   ↓
executable
   ↓
./executable
```

For shell programs:

``` text
script.sh
   ↓
bash script.sh
       OR
chmod +x script.sh
   ↓
./script.sh
```

------------------------------------------------------------------------

# 30. Useful Official Documentation

For Windows WSL installation and configuration, refer to Microsoft's
**Windows Subsystem for Linux documentation**.

For macOS command-line development tools, refer to Apple's **Command
Line Tools documentation**.

Use the official documentation if your Windows or macOS version presents
installation options different from those shown in this guide.
