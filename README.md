# Operating-Systems-Concepts-Practical-Exercises

## Chapter-wise experiment and project organization

The repository contains **selected practical exercises and projects**, not a
complete coding implementation of every chapter or every subsection of the
*Operating System Concepts* textbook.

The following tables use a consistent format to show the experiments and
projects that are **already available** in the original repository and are
being reimplemented in Python.

### Chapter 2 — Operating-System Structures

| Experiment / Project | Practical focus |
|---|---|
| **2.24** | File copying — copy the contents of one file to another file. |
| **2.4** | Linux `/proc` kernel module — create a `/proc` entry that reports the number of seconds since the kernel module was loaded. |

### Chapter 3 — Processes

| Experiment / Project | Practical focus |
|---|---|
| **3.19** | Process execution and timing — measure the time required to execute a command in a child process. Includes pipe-based and shared-memory communication variants. |
| **3.20** | Process ID management — allocate and release process IDs using a bitmap. |
| **3.21** | Process creation — generate the Collatz sequence in a child process. |
| **3.22** | Process creation and shared memory — generate the Collatz sequence in a child process and store the sequence in shared memory. |
| **3.26** | Inter-process communication — exchange messages between two processes using ordinary pipes. |
| **3.27** | Pipe-based file transfer — copy a file using ordinary pipes. |
| **UNIX Shell** | Shell implementation — execute commands in separate processes and support input/output redirection and pipes. |
| **Linux Kernel Module for Task Information** | Linux process information — use `/proc` to display information associated with a process ID. |
| **Linux Kernel Module for Listing Tasks** | Linux task traversal — list system tasks using linear and depth-first traversal approaches. |
| **Kernel Data Structures** | Kernel-style data structures — demonstrate use of a linked-list structure similar to the Linux kernel list implementation. |

### Chapter 4 — Threads and Concurrency

| Experiment / Project | Practical focus |
|---|---|
| **4.22** | Multithreading and statistics — compute statistical values for an array using multiple threads. |
| **4.24** | Multithreading and Monte Carlo — approximate the value of π using the Monte Carlo technique and multiple threads. |
| **Sudoku Solution Validator** | Concurrent validation — validate Sudoku rows, columns, and 3×3 regions using separate threads. |
| **Multithreaded Sorting Application** | Parallel sorting — implement merge sort using multithreading and compare single-threaded and multithreaded execution. |

### Chapter 5 — CPU Scheduling

| Experiment / Project | Practical focus |
|---|---|
| **No existing experiment** | No Chapter 5 coding directory is currently present in the original available exercise set. Recommended CPU-scheduling simulations are provided separately under `Recommended-Python-Labs/`. |

### Chapter 6 — Synchronization Tools

| Experiment / Project | Practical focus |
|---|---|
| **6.33** | Mutual exclusion and finite resources — examine synchronization requirements associated with concurrent access to a finite set of resources. |

### Coverage note

The tables above describe **the coding content currently available in this
repository**. They do not represent all concepts, subsections, exercises, or
programming projects contained in the textbook.

For topics without an existing coding directory, additional Python
laboratories and simulations are provided separately under
`Recommended-Python-Labs/`. These are **newly designed educational
simulations**, not conversions of an existing C program.

## Recommended Python Labs and Simulations — Chapters 7–21

The textbook contains many more chapters and concepts than are represented by
the existing coding directories in this repository. The following sections
provide **recommended Python laboratories and simulations** for Chapters 7–21
where no corresponding implementation is currently available in the existing
C-derived exercise set.

These are **newly designed educational labs**, not claims that the original
repository contains C implementations for these topics. They are intentionally
separated from the existing converted exercises.

The chapter names below follow the structure of *Operating System Concepts,
10th Edition*. The official textbook site lists Chapters 7–21 as
Synchronization Examples, Deadlocks, Main Memory, Virtual Memory, Mass-Storage
Structure, I/O Systems, File-System Interface, File-System Implementation,
File-System Internals, Security, Protection, Virtual Machines, Networks and
Distributed Systems, The Linux System, and Windows 10 respectively.

---

### Chapter 7 — Synchronization Examples

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **7.01 — Bounded Buffer / Producer-Consumer** | Implement the bounded-buffer problem using Python threads, locks, semaphores, and condition variables. |
| **7.02 — Readers-Writers Problem** | Simulate concurrent readers and writers accessing shared data and compare synchronization strategies. |
| **7.03 — Dining Philosophers** | Demonstrate competing threads, resource contention, deadlock, and deadlock-avoidance strategies. |
| **7.04 — Synchronization Mechanism Comparison** | Compare mutex locks, semaphores, and condition variables for selected synchronization problems. |

**Suggested outcome:** Students should be able to select an appropriate
synchronization mechanism for a concurrent problem and explain why the
mechanism is required.

---

### Chapter 8 — Deadlocks

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **8.01 — Resource-Allocation Graph** | Construct and analyze resource-allocation graphs to identify potential deadlocks. |
| **8.02 — Banker's Algorithm** | Implement the safety algorithm and resource-request algorithm for deadlock avoidance. |
| **8.03 — Deadlock Detection** | Simulate multiple processes competing for resources and detect unsafe/deadlocked states. |
| **8.04 — Deadlock Prevention by Resource Ordering** | Demonstrate how imposing a global ordering on resources prevents circular wait. |
| **8.05 — Deadlock Recovery Simulation** | Simulate termination and resource-preemption strategies for recovering from deadlock. |

---

### Chapter 9 — Main Memory

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **9.01 — Fixed Partition Allocation** | Simulate fixed-partition memory allocation and calculate internal fragmentation. |
| **9.02 — First-Fit / Best-Fit / Worst-Fit** | Compare dynamic partition allocation strategies using identical memory workloads. |
| **9.03 — Paging Simulation** | Simulate pages, frames, page tables, and logical-to-physical address translation. |
| **9.04 — Segmentation Simulation** | Model segment tables and perform logical-address validation and translation. |
| **9.05 — Fragmentation Analysis** | Compare internal and external fragmentation under different allocation strategies. |

---

### Chapter 10 — Virtual Memory

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **10.01 — FIFO Page Replacement** | Simulate FIFO page replacement and calculate page faults. |
| **10.02 — LRU Page Replacement** | Simulate Least Recently Used replacement for a given reference string. |
| **10.03 — Optimal Page Replacement** | Implement the theoretical optimal algorithm as a benchmark. |
| **10.04 — Page Replacement Comparison** | Compare FIFO, LRU, and Optimal algorithms for the same workloads. |
| **10.05 — Thrashing Simulation** | Demonstrate how insufficient frames and working-set behavior can increase page faults. |
| **10.06 — Working-Set Model** | Simulate working sets and examine locality of reference. |

---

### Chapter 11 — Mass-Storage Structure

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **11.01 — FCFS Disk Scheduling** | Calculate disk-head movement for a sequence of requests. |
| **11.02 — SSTF Disk Scheduling** | Implement Shortest Seek Time First and compare it with FCFS. |
| **11.03 — SCAN / C-SCAN** | Simulate elevator-style disk scheduling algorithms. |
| **11.04 — LOOK / C-LOOK** | Compare LOOK variants with SCAN-based scheduling. |
| **11.05 — Disk Scheduling Comparison** | Compare all major disk-scheduling strategies using identical workloads. |
| **11.06 — Disk Access-Time Simulation** | Model seek time, rotational latency, and transfer time. |

---

### Chapter 12 — I/O Systems

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **12.01 — I/O Request Scheduling** | Simulate an I/O request queue and compare service policies. |
| **12.02 — Buffering Simulation** | Demonstrate single, double, and circular buffering using producer-consumer workloads. |
| **12.03 — Caching Simulation** | Model cache hits, misses, replacement, and locality. |
| **12.04 — Spooling Simulation** | Simulate a spool queue between producers and a slow device. |
| **12.05 — I/O Performance Analysis** | Compare throughput and latency under different buffering and scheduling policies. |

---

### Chapter 13 — File-System Interface

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **13.01 — File and Directory Operations** | Implement create, open, read, write, rename, copy, and delete operations using Python file APIs. |
| **13.02 — Directory Tree Traversal** | Build and traverse a hierarchical directory structure. |
| **13.03 — File-System Navigation** | Implement path resolution, directory listing, and relative/absolute path handling. |
| **13.04 — File Metadata Explorer** | Examine permissions, timestamps, size, and other file metadata. |

---

### Chapter 14 — File-System Implementation

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **14.01 — Contiguous File Allocation** | Simulate contiguous allocation and measure fragmentation and access characteristics. |
| **14.02 — Linked File Allocation** | Simulate linked allocation and compare sequential/random access behavior. |
| **14.03 — Indexed File Allocation** | Implement an index-block model for file allocation. |
| **14.04 — File Allocation Comparison** | Compare contiguous, linked, and indexed allocation. |
| **14.05 — Free-Space Bitmap** | Implement bitmap-based free-space management. |
| **14.06 — Free-List Management** | Simulate linked free-space lists and allocation/deallocation operations. |

---

### Chapter 15 — File-System Internals

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **15.01 — File-System Cache** | Simulate cache hits/misses for different file-access patterns. |
| **15.02 — Buffer Cache Replacement** | Compare simple cache replacement policies. |
| **15.03 — Journaling Simulation** | Model a write-ahead journal and replay operations after a simulated crash. |
| **15.04 — Crash Recovery** | Demonstrate consistency recovery after incomplete file-system operations. |
| **15.05 — Inode-Style Metadata Simulation** | Model file metadata and block references using Python data structures. |

---

### Chapter 16 — Security

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **16.01 — Password Hashing and Verification** | Demonstrate salted password hashing and secure verification. |
| **16.02 — Access-Control Simulation** | Model users, resources, permissions, and authorization decisions. |
| **16.03 — Authentication Simulation** | Implement a simple authentication workflow with account and credential management. |
| **16.04 — Security Policy Evaluation** | Evaluate access requests against configurable security policies. |

> These exercises are intended for defensive and educational use. They do not
> involve password cracking or unauthorized access.

---

### Chapter 17 — Protection

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **17.01 — Protection Access Matrix** | Implement subjects, objects, and rights using an access matrix. |
| **17.02 — Access-Control Lists** | Derive and query ACL-style representations from an access matrix. |
| **17.03 — Capability Lists** | Implement capability-based access to resources. |
| **17.04 — Capability Revocation** | Simulate granting and revoking capabilities. |
| **17.05 — Protection-Domain Simulation** | Model domain switching and permitted operations. |

---

### Chapter 18 — Virtual Machines

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **18.01 — Toy Virtual Machine** | Build a small user-space VM with virtual registers, memory, instructions, and a fetch-decode-execute cycle. |
| **18.02 — VM Instruction Set** | Design and execute a small educational instruction set. |
| **18.03 — VM Resource Allocation** | Simulate CPU, memory, and I/O resource allocation among virtual machines. |
| **18.04 — Virtual Machine Isolation** | Demonstrate how separate virtual memory/state spaces can isolate simulated workloads. |

**Platform note:** These are intentionally **OS-independent simulations**.
They do not attempt to control KVM, Hyper-V, VMware, VirtualBox, or hardware
virtualization directly. A real hypervisor/API implementation would be
platform-dependent.

---

### Chapter 19 — Networks and Distributed Systems

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **19.01 — Lamport Logical Clocks** | Simulate logical clocks and happened-before relationships among distributed processes. |
| **19.02 — Vector Clock Simulation** | Extend logical-clock modeling using vector clocks. |
| **19.03 — Distributed Mutual Exclusion** | Simulate a message-based mutual-exclusion protocol. |
| **19.04 — Leader Election** | Simulate a simple distributed leader-election algorithm. |
| **19.05 — Reliable Message Delivery** | Simulate message loss, retransmission, ordering, and acknowledgements. |

These can initially be implemented as **user-space simulations**, avoiding
dependence on a particular network stack or operating system.

---

### Chapter 20 — The Linux System

**Existing C experiments:** Several Linux-specific projects already
appear under the Chapter 3 process material, including `/proc`-based task
information and task listing.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **20.01 — Linux `/proc` Process Monitor** | Inspect process information exposed through `/proc`. |
| **20.02 — Linux System Resource Monitor** | Read CPU, memory, process, and system statistics from Linux interfaces. |
| **20.03 — Linux Process Hierarchy Explorer** | Build a parent-child process tree from `/proc`. |
| **20.04 — Linux File Descriptor Explorer** | Inspect process file descriptors through Linux `/proc` interfaces. |
| **20.05 — Linux System Call Observation** | Design a controlled demonstration around observable system-call behavior where suitable tools are available. |

**Platform note:** These exercises are **Linux-specific** and should be run on
Linux. Python itself remains a user-space language; these programs inspect
Linux facilities rather than becoming kernel modules.

---

### Chapter 21 — Windows 10

**Existing C experiment:** None currently available.

**Recommended Python Labs:**

| Lab | Practical focus |
|---|---|
| **21.01 — Windows Process and Thread Explorer** | Explore process/thread information using Python-accessible Windows facilities. |
| **21.02 — Windows File-System Demonstration** | Examine Windows-specific file-system behavior using Python APIs. |
| **21.03 — Windows Service Observation** | Observe configured Windows services through supported user-space mechanisms. |
| **21.04 — Windows Resource Monitoring** | Build a basic process/resource monitoring demonstration using available Windows interfaces. |

**Platform note:** These exercises are intended for **Windows**. Where Python
standard-library facilities do not expose a Windows-specific mechanism, the
README for the experiment should identify the required platform API or
supported tool.

---

### Recommended-lab status

The experiments in Chapters 7–21 above are **recommended additions to the
laboratory curriculum**. They should be treated differently from the
C-reference-based programs already present in Chapters 2–6.

| Type | Meaning |
|---|---|
| **Existing / Converted** | A coding exercise already present in the original repository has been reimplemented in Python. |
| **Recommended / Simulation** | A new Python practical has been designed to make an OS concept experimentally observable. |
| **Platform-specific** | The practical depends on Linux, Windows, or another OS facility. |
| **OS-independent** | The practical is a Python simulation that can generally run across operating systems. |

This distinction is intentional. The official *Operating System Concepts,
10th Edition* structure contains Chapters 7–21 covering synchronization,
deadlocks, memory, storage, file systems, security/protection, virtualization,
distributed systems, and Linux/Windows case studies, but the presence of a
chapter in the textbook does **not** imply that this repository originally
contained source code for every topic.

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

Some existing exercises model Linux kernel facilities. Ordinary Python runs in
user space and cannot itself be a loadable Linux kernel module. The converted
repository therefore uses documented **user-space adaptations**, such as Linux
`/proc`, elapsed-time APIs, and Python data structures.

Some of the recommended labs are also platform-specific. Their individual
README files identify whether Linux, Windows, or another platform is required.

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
