# Operating Systems Lab – Experiment 1
## Basics of UNIX Commands

---

## 1. Introduction to UNIX

### Aim

To study the basics of UNIX.

### UNIX

UNIX is a multi-user operating system. It was developed at AT&T Bell Laboratories, USA, in 1969.

Ken Thompson, along with Dennis Ritchie, developed UNIX from MULTICS (Multiplexed Information and Computing Service) OS. By 1980, UNIX had been completely rewritten using the C language.

### Linux

Linux is similar to UNIX and was created by Linus Torvalds. UNIX commands can be used in Linux. Linux is open-source software.

### Structure of a Linux System

A Linux system consists of three parts:

1. UNIX/Linux Kernel
2. Shells
3. Tools and Applications

### UNIX Kernel

The kernel is the core of the UNIX operating system. It controls system tasks, schedules processes, and performs the functions of the operating system.

### Shell

The shell is the command interpreter in a UNIX operating system. It accepts commands from the user and interprets them.

---

# 2. Basic UNIX Commands

## 2.1 `date`

**Purpose:** Display the current date and time.

### Syntax

```bash
date
```

### Date Formatting Options

| Command | Purpose |
|---|---|
| `date +%m` | Display the month |
| `date +%h` | Display the month name |
| `date +%d` | Display the day of the month |
| `date +%y` | Display the last two digits of the year |
| `date +%H` | Display the hour |
| `date +%M` | Display the minutes |
| `date +%S` | Display the seconds |

---

## 2.2 `cal`

**Purpose:** Display the calendar.

### Syntax

```bash
cal
```

### Example

```bash
cal 2 2009
```

---

## 2.3 `echo`

**Purpose:** Print a message on the screen.

### Syntax

```bash
echo "text"
```

### Example

```bash
echo "Hello World"
```

---

# 3. Directory Listing

## 3.1 `ls`

**Purpose:** List files and directories.

### Syntax

```bash
ls
```

### Options

| Command | Purpose |
|---|---|
| `ls -a` | List all files, including hidden files |
| `ls -l` | Display a long listing with file details |
| `ls -t` | Sort entries by modification time |
| `ls -u` | Use access time for sorting/listing |
| `ls -S` | Sort entries by file size |
| `ls -r` | Reverse the sorting order |
| `ls -F` | Classify entries with file-type indicators |
| `ls -h` | Display file sizes in human-readable form |

### Combining Options

```bash
ls -lh
```

### Filename Patterns

List files whose names begin with letters from `a` through `m`:

```bash
ls [a-m]*
```

List files whose names begin with `a` or `A`:

```bash
ls [aA]*
```

### Redirect Output to a File

```bash
ls > mylist
```

The output of `ls` is stored in a file named `mylist`.

---

# 4. Printing and Help Commands

## 4.1 `lp`

**Purpose:** Send a file to a printer.

### Syntax

```bash
lp filename
```

---

## 4.2 `man`

**Purpose:** Display the manual page for a UNIX command.

### Syntax

```bash
man <command>
```

### Example

```bash
man cat
```

---

# 5. User and System Information

## 5.1 `who`

**Purpose:** Display information about users currently logged into the system.

```bash
who
```

---

## 5.2 `whoami`

**Purpose:** Display the username of the current user.

```bash
whoami
```

---

## 5.3 `uptime`

**Purpose:** Display how long the computer has been running since its last reboot or power-off.

```bash
uptime
```

---

## 5.4 `uname`

**Purpose:** Display system information such as the system name and hardware information.

### Syntax

```bash
uname
```

### Example

```bash
uname -a
```

---

## 5.5 `hostname`

**Purpose:** Display the system host name.

```bash
hostname
```

---

# 6. `bc` – Command-Line Calculator

**Purpose:** Perform calculations using the command-line calculator.

### Start `bc`

```bash
bc
```

### Basic Arithmetic

```text
10/2*3
15
```

### Decimal Calculation

```text
scale=1
2.25+1
3.35
```

### Number Bases

```text
ibase=2
obase=16
```

### Square Root

```text
sqrt(196)
14
quit
```

### Loop

```text
for(i=1;i<3;i=i+1) i
1
2
3
quit
```

### Using `bc -l`

```bash
bc -l
```

Example:

```text
scale=2
s(3.14)
0
```

Type `quit` to exit `bc`.

---

# 7. File Manipulation Commands

## 7.1 `cat`

**Purpose:** Create, view, and concatenate files.

### Create a File

```bash
cat > filename
```

Enter the required text and press **Ctrl+D** to finish.

### View a File

```bash
cat filename
```

### Add Text to an Existing File

```bash
cat >> filename
```

Enter the additional text and press **Ctrl+D** to finish.

### Concatenate Files

```bash
cat file1 file2 > file3
```

### Append File Contents

```bash
cat file1 file2 >> file3
```

---

## 7.2 `grep`

**Purpose:** Search for a particular word or pattern in a file.

### Syntax

```bash
grep "pattern" filename
```

### Example

```bash
grep "anu" student
```

---

## 7.3 `rm`

**Purpose:** Delete a file from the file system.

```bash
rm filename
```

---

## 7.4 `touch`

**Purpose:** Create a blank file.

```bash
touch filename
```

### Example

```bash
touch student
```

---

## 7.5 `cp`

**Purpose:** Copy files or directories.

### Syntax

```bash
cp source_file destination_file
```

### Example

```bash
cp student stud
```

---

## 7.6 `mv`

**Purpose:** Rename or move a file or directory.

### Syntax

```bash
mv old_file new_file
```

### Example

```bash
mv student stud
```

### Prompt Before Overwriting

```bash
mv -i student stud
```

---

# 8. `cut`

**Purpose:** Extract a specified number of characters or fields from a file.

### Syntax

```bash
cut <option> <filename>
```

### Character Extraction

```bash
cut -c 1-10 emp
```

Extract characters 1 through 10 from each line.

### Field Extraction

```bash
cut -f 3,6 emp
```

Extract fields 3 and 6.

### Field Range

```bash
cut -f 3-6 emp
```

Extract fields 3 through 6.

### Options

| Option | Purpose |
|---|---|
| `-c` | Character positions |
| `-f` | Fields |

---

# 9. `head`

**Purpose:** Display the first 10 lines of a file by default.

### Syntax

```bash
head filename
```

### Example

```bash
head student
```

### Display the First Two Lines

```bash
head -2 student
```

---

# 10. `tail`

**Purpose:** Display the last 10 lines of a file by default.

### Syntax

```bash
tail filename
```

### Example

```bash
tail student
```

### Display the Last Two Lines

```bash
tail -2 student
```

---

# 11. `chmod` – File Permissions

**Purpose:** Change the permissions of a file or directory.

### Syntax

```bash
chmod <category><operation><permission> filename
```

### Categories

| Symbol | Meaning |
|---|---|
| `u` | User/owner |
| `g` | Group |
| `o` | Others |

### Operations

| Symbol | Meaning |
|---|---|
| `+` | Assign/add permission |
| `-` | Remove permission |
| `=` | Assign the specified permission |

### Permissions

| Symbol | Meaning |
|---|---|
| `r` | Read |
| `w` | Write |
| `x` | Execute |

### Examples

Remove write and execute permission from the owner:

```bash
chmod u-wx student
```

Assign read and write permission to the owner and group:

```bash
chmod u+rw,g+rw student
```

Assign read, write, and execute permission to the group:

```bash
chmod g=rwx student
```

---

# 12. `wc`

**Purpose:** Count the number of lines, words, and characters/bytes in a file.

### Count Lines

```bash
wc -l filename
```

### Count Words

```bash
wc -w filename
```

### Count Characters/Bytes

```bash
wc -c filename
```

---

# 13. UNIX Editors

UNIX provides various editors, including:

- `vi`
- `ed`
- `ex`
- `EMACS`

---

# 14. `vi` Editor

`vi` stands for **Visual**. It is a full-screen text editor used to view and edit files.

### Modes of `vi`

1. Command mode
2. Insert mode
3. Ex mode

### Command Mode

In command mode, commands are used to navigate and manipulate the text.

### Insert Mode

In insert mode, text can be entered or edited.

### Ex Mode

Ex mode provides command-line operations for the editor.

### Cursor Movement

```text
h    Move left
j    Move down
k    Move up
l    Move right
```

---

# 15. EMACS Editor

EMACS is a text editor that provides commands for moving through, editing, deleting, and searching text.

### EMACS Notation

```text
C-    Control key
M-    Meta key
DEL   Delete/Backspace key
```

## Movement Commands

| Key | Function |
|---|---|
| `M->` | Move to the end of the file |
| `M-<` | Move to the beginning of the file |
| `C-v` | Move forward one screen |
| `M-v` | Move backward one screen |
| `C-n` | Move to the next line |
| `C-p` | Move to the previous line |
| `C-a` | Move to the beginning of the line |
| `C-e` | Move to the end of the line |
| `C-f` | Move forward one character |
| `C-b` | Move backward one character |
| `M-f` | Move forward one word |
| `M-b` | Move backward one word |

## Deletion Commands

| Key | Function |
|---|---|
| `DEL` | Delete the previous character |
| `C-d` | Delete the current character |
| `M-DEL` | Delete the previous word |
| `M-d` | Delete the next word |
| `C-x DEL` | Delete the previous sentence |
| `M-k` | Delete the rest of the current sentence |
| `C-k` | Delete the rest of the current line |
| `C-x u` | Undo the last change |

## Search and Replace in EMACS

| Key | Function |
|---|---|
| `y` | Change this occurrence of the pattern |
| `n` | Do not change this occurrence; look for another occurrence |
| `q` | Do not change further occurrences; leave the query |
| `!` | Change this occurrence and all remaining occurrences |

---

# 16. Quick Command Reference

## Basic Commands

```bash
date
cal
echo "Hello World"
ls
who
whoami
uptime
uname -a
hostname
```

## `ls` Commands

```bash
ls -a
ls -l
ls -t
ls -u
ls -S
ls -r
ls -F
ls -h
ls -lh
ls [a-m]*
ls [aA]*
ls > mylist
```

## Printing and Help

```bash
lp filename
man cat
```

## File Manipulation

```bash
cat > filename
cat filename
cat >> filename
cat file1 file2 > file3
cat file1 file2 >> file3
grep "anu" student
rm filename
touch filename
cp student stud
mv student stud
mv -i student stud
```

## Text Processing

```bash
cut -c 1-10 emp
cut -f 3,6 emp
cut -f 3-6 emp
head student
head -2 student
tail student
tail -2 student
```

## File Permissions

```bash
chmod u-wx student
chmod u+rw,g+rw student
chmod g=rwx student
```

## File Statistics

```bash
wc -l filename
wc -w filename
wc -c filename
```

## Calculator

```bash
bc
bc -l
```

---

## Result

The basics of UNIX commands and UNIX editors were studied.
