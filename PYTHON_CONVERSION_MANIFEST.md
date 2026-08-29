# Python Conversion Manifest

| Directory | Python conversion |
|---|---|
| `2.24` | `file_copy.py` |
| `2.4` | `seconds.py` (user-space analogue of kernel module) |
| `3.19` | `time_pipe.py`, `time_shared_memory.py` |
| `3.20` | `pid_manager.py` |
| `3.21` | `collatz.py` |
| `3.22` | `collatz.py` |
| `3.26` | `reverse_case.py` |
| `3.27` | `filecopy.py` |
| `4.22` | `main.py` |
| `4.24` | `main.py` |
| `6.33` | `main.py` |
| `Chapter 3 - Kernel Data Structures` | `collatz.py`, `color_list.py` (user-space analogues) |
| `Chapter 3 - Linux Kernel Module for Listing Tasks` | `process_linear_iteration.py`, `process_dfs.py` (Linux `/proc` analogues) |
| `Chapter 3 - Linux Kernel Module for Task Information project` | `pid.py` (Linux `/proc` analogue) |
| `Chapter 3 - UNIX Shell project` | `shell.py` |
| `Chapter 4 - Multithreaded sorting application` | `main.py` |
| `Chapter 4 - Sudoku Solution Validator` | `main.py` |

## Compatibility notes

- Python 3 is required; no third-party Python packages are required.
- Linux is recommended for the process `/proc` exercises.
- Kernel-module exercises cannot literally be translated into ordinary Python because Python runs in user space. Their Python versions therefore demonstrate the same OS concepts using user-space facilities.
- Python's Global Interpreter Lock (GIL) means CPU-bound `threading` code does not provide the same CPU parallelism as C/POSIX threads. The thread-based examples retain the concurrency structure for teaching purposes.
