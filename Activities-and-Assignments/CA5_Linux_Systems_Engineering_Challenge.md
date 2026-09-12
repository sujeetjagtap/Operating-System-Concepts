# CA-5 – Linux Systems Engineering Challenge
## Continuous Assessment – 10 Marks

### Course
**Operating Systems**

### Assessment Position
**CA-5 of 7 | 10 Marks**

---

## 1. Purpose

CA-5 transitions students from **simulation and research** into the observation and engineering of a **real operating system environment**.

The central question is:

> **Can I observe, control, instrument and engineer OS behaviour on a real Linux system?**

Linux exposes substantial operating-system behaviour through processes, `/proc`, scheduling interfaces, signals, filesystems, resource controls and other system mechanisms. The Linux kernel documentation describes `/proc` as an interface to internal kernel data structures and provides process-specific information through `/proc/<pid>`. citeturn0search0turn0search10

Python can directly interact with several OS facilities, including process scheduling information and CPU affinity on supported Unix/Linux systems. citeturn0search4

CA-5 therefore emphasizes **real-system evidence rather than algorithm simulation alone**.

---

# 2. Position in the CA Progression

| Assessment | Central Question | Student Capability |
|---|---|---|
| CA-1 – Systems Thinking | What is the OS problem? | Understand, model, reason |
| CA-2 – Performance Investigation | What does evidence show? | Measure and analyze |
| CA-3 – Design & Debugging | Can I diagnose and improve it? | Engineer and validate |
| CA-4 – Research Mini-Project | What is not completely answered? | Investigate and generate evidence |
| **CA-5 – Linux Systems Engineering** | **Can I observe and control a real OS?** | **Apply and engineer** |
| CA-6 – Rust Micro-OS | Can I implement OS mechanisms? | Build low-level systems |
| CA-7 – Viva & Demonstration | Can I defend my engineering decisions? | Communicate and defend |

The overall progression becomes:

> **Think → Measure → Debug → Research → Engineer → Build → Defend**

---

# 3. Learning Outcomes

After completing CA-5, students should be able to:

- use Linux as an OS experimentation platform;
- inspect processes, threads and system resources;
- use `/proc` and standard Linux utilities to investigate system state;
- create and control processes using Python;
- work with signals and process states;
- investigate CPU scheduling behaviour;
- use process priorities and CPU affinity appropriately;
- examine memory and I/O behaviour;
- implement basic IPC mechanisms;
- investigate synchronization on a real system;
- use Bash and Python together for systems experimentation;
- collect reproducible system-level measurements;
- distinguish simulated OS behaviour from real OS behaviour;
- use Linux tools as engineering instruments;
- connect real Linux mechanisms to future Rust Micro-OS implementations.

---

# 4. Core CA-5 Engineering Framework

Every challenge should follow:

> **Observe → Formulate → Instrument → Experiment → Control → Analyze → Engineer → Validate → Defend**

### 1. Observe
Identify actual behaviour on Linux.

### 2. Formulate
State the OS question or engineering problem.

### 3. Instrument
Select commands, APIs, scripts and measurements.

### 4. Experiment
Run controlled tests.

### 5. Control
Keep workload/environment variables consistent.

### 6. Analyze
Compare measurements and explain behaviour.

### 7. Engineer
Modify configuration, workload, program or implementation.

### 8. Validate
Demonstrate that the intervention produced the intended effect.

### 9. Defend
Explain mechanisms, observations and trade-offs.

---

# 5. Linux Toolchain

CA-5 should introduce students to a practical systems-engineering toolkit.

| Tool / Interface | Purpose |
|---|---|
| `ps` | Process inspection |
| `top` / `htop` | Dynamic resource monitoring |
| `/proc` | Kernel/process information |
| `pidstat` | Process-level performance statistics |
| `vmstat` | Memory/process/system statistics |
| `iostat` | Storage/I/O statistics where available |
| `free` | Memory information |
| `lscpu` | CPU topology |
| `taskset` | CPU affinity |
| `nice` / `renice` | Process priority |
| `kill` / signals | Process control |
| `time` | Execution timing |
| `strace` | System-call observation |
| `df` / `du` | Filesystem/storage investigation |
| `find` | File-system traversal |
| `grep`, `awk`, `sed` | Data extraction/processing |
| Bash | Automation and orchestration |
| Python | Instrumentation, automation and analysis |
| Rust | Advanced systems-level implementation |

Tool availability can vary across Linux distributions; students should record the distribution and tool versions used.

---

# 6. Programming Language Policy

| Activity | Primary Language |
|---|---|
| Linux command-line investigation | **Bash/Linux** |
| Process automation | **Python 3.x + Bash** |
| `/proc` analysis | **Python 3.x** |
| Signals | **Python 3.x** |
| Scheduling/priority experiments | **Python + Linux** |
| CPU affinity | **Python + Linux** |
| Memory monitoring | **Python + Linux** |
| IPC | **Python + Linux** |
| File/I/O experiments | **Python + Bash/Linux** |
| System-call investigation | **Python/Bash + Linux tools** |
| Concurrency experiments | **Python; Rust encouraged** |
| Resource isolation | **Linux + Bash/Python** |
| Advanced systems experiments | **Rust + Linux** |
| Micro-OS preparation | **Rust** |

### Principle

**Python is the default automation and analysis language. Bash is the native Linux orchestration language. Rust is the low-level systems bridge.**

Students should not use Python merely to recreate Linux commands when the learning objective is to understand the actual Linux mechanism. The preferred approach is often:

> **Linux command/tool → inspect output → automate with Python → interpret OS behaviour**

---

# 7. Challenge Structure – 10 Marks

CA-5 should be assessed through a practical Linux engineering challenge.

| Component | Marks |
|---|---:|
| Problem understanding and OS mechanism identification | 2 |
| Linux instrumentation and tool usage | 2 |
| Implementation / engineering intervention | 2 |
| Experimental evidence and analysis | 2 |
| Validation, technical explanation and defence | 2 |
| **Total** | **10** |

---

# 8. Challenge Bank

## A. Process Engineering

### L1. Process State Investigator

**Task:** Create a Python utility that launches a controlled workload and periodically records its Linux process state.

**Language:** Python + Linux `/proc`

**Investigate:**
- PID;
- process state;
- parent PID;
- CPU usage;
- memory information;
- thread count.

**Engineering outcome:** Explain how process states change during execution.

---

### L2. Parent–Child Process Investigation

**Task:** Create parent and child processes and investigate their relationships.

**Language:** Python + Bash/Linux

**Investigate:**
- parent/child hierarchy;
- process lifetime;
- termination order;
- orphaning/zombie behaviour where safely demonstrated.

---

### L3. Process Lifecycle Controller

**Task:** Develop a Python program that launches, monitors, pauses/resumes where appropriate, and terminates controlled child processes.

**Language:** Python + Linux signals.

---

### L4. Process Resource Profiler

**Task:** Compare resource behaviour of CPU-bound, memory-intensive and I/O-oriented workloads.

**Language:** Python + Linux.

**Metrics:**
- execution time;
- CPU usage;
- memory usage;
- process state;
- I/O activity.

---

# 9. CPU Scheduling and Priority

### L5. Priority Engineering Challenge

**Task:** Create multiple CPU-bound processes and investigate the effect of process priority.

**Language:** Python + Linux.

Python's OS interface exposes scheduling-related functions on supported platforms, including scheduling parameters and CPU affinity. citeturn0search4

**Compare:**
- default priority;
- modified priority;
- workload completion;
- CPU distribution.

---

### L6. CPU Affinity Investigation

**Task:** Compare workload performance when processes can execute on multiple CPUs versus restricted CPU sets.

**Language:** Python + Linux.

Python provides `sched_setaffinity()` and `sched_getaffinity()` on supported Unix platforms. citeturn0search4

**Metrics:**
- execution time;
- CPU utilization;
- throughput;
- variability.

---

### L7. Scheduling Observation

**Task:** Use Linux monitoring tools and `/proc` information to observe concurrent CPU-bound workloads.

**Language:** Bash + Python.

**Engineering question:**

> How does observed Linux scheduling behaviour differ from a simplified textbook scheduling model?

---

# 10. Threads and Concurrency

### L8. Process vs Thread Experiment

**Task:** Execute equivalent workloads using processes and threads.

**Language:** Python; Rust extension recommended.

**Measure:**
- creation overhead;
- execution time;
- memory;
- scalability.

---

### L9. Thread Contention

**Task:** Create controlled concurrent workloads competing for a synchronization primitive.

**Language:** Python; Rust preferred for advanced implementation.

**Measure:**
- throughput;
- waiting;
- scalability;
- contention.

---

### L10. Race Condition and Correction

**Task:** Construct a controlled shared-state concurrency problem, observe incorrect results, introduce synchronization and validate correctness.

**Language:** Python or Rust.

**Required evidence:**

> Incorrect execution → root cause → synchronization → corrected execution.

---

# 11. Signals and Inter-Process Communication

### L11. Signal Handling Laboratory

**Task:** Build a process that handles selected signals and records its responses.

**Language:** Python + Linux.

**Investigate:**
- signal delivery;
- handling;
- termination;
- graceful shutdown.

---

### L12. Pipe-Based IPC

**Task:** Create producer and consumer processes communicating through a pipe.

**Language:** Python + Linux/Bash.

**Investigate:**
- communication latency;
- message ordering;
- producer/consumer rate mismatch.

---

### L13. FIFO-Based IPC

**Task:** Build a named-pipe communication system.

**Language:** Python + Bash/Linux.

**Compare:** pipe vs FIFO in terms of use case, architecture and behaviour.

---

### L14. IPC Performance Challenge

**Task:** Compare selected IPC mechanisms for increasing message sizes.

**Language:** Python + Linux.

**Metrics:**
- latency;
- throughput;
- CPU overhead.

---

# 12. Synchronization and Deadlock

### L15. Producer–Consumer on Linux

**Task:** Implement producer–consumer synchronization and investigate buffer size and workload effects.

**Language:** Python; Rust recommended.

---

### L16. Lock Contention Investigation

**Task:** Increase the number of concurrent workers and measure contention.

**Language:** Python or Rust.

**Metrics:**
- throughput;
- execution time;
- scalability.

---

### L17. Deadlock Demonstration and Recovery

**Task:** Construct a small controlled deadlock scenario, detect it and demonstrate a safe recovery strategy.

**Language:** Python or Rust.

**Safety:** Use only student-created processes/resources in a controlled environment.

---

# 13. Memory Engineering

### L18. Process Memory Investigator

**Task:** Create workloads with different memory footprints and investigate their Linux memory behaviour.

**Language:** Python + `/proc`.

**Investigate:**
- virtual memory;
- resident memory;
- process memory growth;
- memory release.

---

### L19. Memory Growth Experiment

**Task:** Incrementally increase a process's memory demand and observe system behaviour.

**Language:** Python + Linux.

**Required:** Establish conservative limits and avoid exhausting the host.

---

### L20. Memory vs Workload

**Task:** Compare memory behaviour for sequential, random and bursty workloads.

**Language:** Python + Linux.

---

# 14. File Systems and I/O

### L21. File Access Performance

**Task:** Compare sequential and random file access patterns.

**Language:** Python + Linux.

**Variables:**
- file size;
- block size;
- access pattern.

---

### L22. Read vs Write Investigation

**Task:** Measure controlled file read/write behaviour under different file sizes.

**Language:** Python + Bash/Linux.

---

### L23. Filesystem Observation

**Task:** Investigate filesystem capacity, file metadata and directory structure using Linux tools and Python.

**Language:** Bash + Python.

---

### L24. System-Call Investigation

**Task:** Observe system calls made by a controlled file-processing program.

**Language:** Python + Linux tracing tools.

**Expected output:** Connect application operations to underlying system calls.

---

# 15. `/proc` Engineering Challenges

The `/proc` filesystem provides process-specific directories and interfaces to kernel/system information. citeturn0search0turn0search10

### L25. Build a `/proc` Process Explorer

Develop a Python utility that displays:

- PID;
- PPID;
- state;
- CPU-related statistics;
- memory-related information;
- thread count;
- command line where permitted.

---

### L26. Process Tree Visualizer

Build a process hierarchy from `/proc` information.

**Language:** Python.

**Extension:** Export the hierarchy as text/graph data.

---

### L27. Lightweight Linux Monitor

Build a command-line dashboard showing selected:

- CPU;
- memory;
- process;
- load;
- I/O indicators.

**Language:** Python + `/proc`.

---

# 16. Resource Management

## L28. Resource-Limited Workload

Investigate how controlled resource limits affect application behaviour.

**Language:** Bash + Python/Linux.

**Metrics:**
- completion time;
- resource consumption;
- failure behaviour.

---

## L29. Control-Group Investigation

Investigate process grouping and resource management using Linux cgroup facilities where permitted by the laboratory environment.

**Language:** Bash + Python.

Linux cgroup v2 organizes processes and threads into hierarchical groups and exposes interfaces such as `cgroup.procs` for process membership. citeturn0search1

**Important:** Students must work only within faculty-approved/user-accessible cgroups. Do not modify host-wide resource controls.

---

## L30. Isolation Observation

Investigate how selected Linux isolation mechanisms affect what a controlled process can observe.

**Language:** Bash + Python/Linux.

Advanced work may explore namespaces. Cgroup namespaces can alter the cgroup view exposed through `/proc/<pid>/cgroup`. citeturn0search1turn0search24

---

# 17. Security-Oriented Linux Engineering

### L31. File Permission Investigation

Investigate how Linux permissions affect controlled processes accessing files.

**Language:** Bash + Python.

---

### L32. Least-Privilege Experiment

Create a controlled application that requires a specific resource and investigate how restricting permissions changes behaviour.

**Language:** Python + Bash/Linux.

---

### L33. Process Visibility

Investigate process information visibility through `/proc` under different permission configurations where safely available.

The kernel documentation describes `/proc` visibility controls such as `hidepid`; students should observe rather than alter system-wide settings unless specifically authorized. citeturn0search0

---

# 18. Integrated Engineering Challenges

## L34. Linux Performance Incident Investigation

### Scenario

A workload that previously completed in a predictable time has become slow.

Students receive:

- process information;
- CPU/memory observations;
- workload description;
- selected Linux logs/measurements.

### Task

Determine the likely bottleneck.

### Required workflow

**Observe → Hypothesize → Instrument → Measure → Diagnose → Recommend → Validate**

---

## L35. CPU Saturation Investigation

Multiple processes compete for CPU resources.

Students must determine:

- which processes dominate CPU usage;
- whether affinity changes behaviour;
- whether workload completion improves after engineering intervention.

**Language:** Python + Linux.

---

## L36. Memory Pressure Investigation

A controlled workload exhibits increasing memory consumption.

Students must:

1. identify the process;
2. measure memory growth;
3. correlate workload behaviour;
4. determine whether the issue is allocation behaviour or workload design;
5. propose a safe intervention.

---

## L37. I/O Bottleneck Investigation

A file-processing workload experiences poor performance.

Students must determine whether the dominant issue relates to:

- access pattern;
- file size;
- storage behaviour;
- application design;
- system activity.

---

## L38. Concurrency Failure Investigation

A multithreaded program occasionally produces incorrect results.

Students must:

- reproduce the failure;
- identify the shared state;
- determine the synchronization issue;
- implement a correction;
- demonstrate repeated correctness.

---

# 19. Advanced Rust + Linux Challenges

These activities provide the bridge to CA-6.

### L39. Rust Process Benchmark

Compare a selected systems workload implemented in Python and Rust.

**Language:** Python + Rust + Linux.

---

### L40. Rust Threading Investigation

Implement a controlled concurrent workload in Rust and investigate scalability.

**Language:** Rust + Linux.

---

### L41. Rust Synchronization

Implement and evaluate a synchronization mechanism in Rust.

**Language:** Rust.

---

### L42. Rust Memory Allocation Investigation

Study allocation behaviour using a controlled Rust program.

**Language:** Rust + Linux.

---

### L43. Rust Task Scheduler Prototype

Implement a user-space task scheduler in Rust inspired by OS scheduling concepts.

**Language:** Rust.

**CA-6 bridge:** Extend the conceptual design into a kernel-level scheduler.

---

# 20. Challenge Difficulty Levels

| Level | Description | Examples |
|---|---|---|
| **Level 1** | Observe | `/proc`, process states, system monitoring |
| **Level 2** | Measure | priority, affinity, memory, I/O |
| **Level 3** | Engineer | IPC, synchronization, resource control |
| **Level 4** | Diagnose | integrated Linux incident |
| **Level 5** | Extend | Rust systems experiment / Micro-OS bridge |

Recommended CA distribution:

- 20% Level 1
- 30% Level 2
- 30% Level 3
- 15% Level 4
- 5% Level 5

---

# 21. Student Task Template

## 1. Problem

What Linux/OS behaviour are you investigating?

## 2. OS Concept

Which OS concept is involved?

## 3. Research/Engineering Question

What specifically are you trying to determine or improve?

## 4. Hypothesis

What do you expect to happen?

## 5. Linux Environment

- Distribution:
- Kernel version:
- CPU:
- RAM:
- Python version:
- Rust version if applicable:

## 6. Tools

List Linux commands, Python modules, Rust libraries and other tools.

## 7. Methodology

Describe:

- workload;
- variables;
- controls;
- repetitions;
- measurements.

## 8. Implementation

Provide source code and explanation.

## 9. Evidence

Include:

- command output;
- numerical measurements;
- tables;
- graphs;
- selected screenshots.

## 10. Engineering Intervention

What did you change or optimize?

## 11. Validation

How did you demonstrate that the intervention worked?

## 12. Conclusion

What did you learn about Linux/OS behaviour?

---

# 22. Evidence Requirements

Students must provide **system evidence**, not merely source code.

Acceptable evidence includes:

- `/proc` observations;
- process statistics;
- timing results;
- CPU/memory measurements;
- I/O measurements;
- system-call traces;
- process trees;
- resource-control observations;
- repeated benchmark results;
- before/after comparisons.

### Minimum evidence rule

Every engineering challenge should contain:

> **Baseline → Intervention → Measurement → Comparison → Conclusion**

---

# 23. Reproducibility

Students should document:

- Linux distribution;
- kernel version;
- hardware;
- number of CPUs;
- memory;
- Python/Rust version;
- commands used;
- program parameters;
- workload;
- repetitions;
- measurement methodology.

Where randomness is involved, specify the random seed.

---

# 24. Safety Rules

CA-5 uses a real operating system. Therefore:

### Students must NOT

- kill unrelated user/system processes;
- modify kernel parameters without permission;
- modify system-wide cgroups without permission;
- exhaust host memory intentionally;
- create uncontrolled fork bombs;
- intentionally fill disks;
- disable security mechanisms;
- alter permissions of unrelated files;
- interfere with other students' processes;
- run destructive experiments on shared laboratory systems.

### Recommended environment

Use:

- dedicated Linux laboratory machines;
- virtual machines;
- containers where appropriate;
- student-owned isolated environments.

The principle is:

> **Experiment on controlled resources, not on the laboratory infrastructure.**

---

# 25. AI-Assisted Linux Engineering

AI may assist with:

- Linux command discovery;
- Python/Bash code generation;
- explanation of `/proc` fields;
- debugging;
- experimental design;
- visualization;
- interpretation hypotheses.

However, students must **execute and verify commands themselves**.

### Required discipline

For every AI-generated command:

**Understand → Execute safely → Observe → Verify → Document**

AI must not be treated as an authority on the state of the student's machine.

---

# 26. AI Disclosure

Students should include:

> “Generative AI was used for selected aspects of command discovery, conceptual clarification, code assistance and/or debugging. All commands were reviewed for safety, executed in a controlled Linux environment, and all reported observations and measurements were independently verified.”

---

# 27. CA-5 Assessment Rubric

| Criterion | 2 Marks | 1 Mark | 0 Marks |
|---|---|---|---|
| Problem & OS understanding | Correct mechanism and focused problem | Partial understanding | Incorrect/unclear |
| Linux instrumentation | Appropriate tools and meaningful measurements | Basic tool usage | Little/no instrumentation |
| Engineering intervention | Correct and justified implementation | Partial implementation | Incorrect/incomplete |
| Evidence & analysis | Strong quantitative evidence and interpretation | Basic evidence | Unsupported claims |
| Validation & defence | Reproducible result with strong explanation | Basic validation | Cannot justify result |

**Total: 10 Marks**

---

# 28. Performance Levels

### Outstanding
Student independently identifies the mechanism, selects appropriate Linux tools, produces reproducible evidence and proposes a technically justified intervention.

### Proficient
Student correctly applies Linux tools and explains the observed OS behaviour.

### Developing
Student completes the experiment but relies heavily on procedural instructions.

### Beginning
Student produces limited evidence and cannot connect observations to OS mechanisms.

---

# 29. Faculty Evaluation Questions

1. What OS mechanism is responsible for the observed behaviour?
2. Why did you choose this Linux tool?
3. What does `/proc/<pid>` tell you?
4. Which measurements are reliable indicators of your hypothesis?
5. What variables did you control?
6. What could have affected your results?
7. Why did your intervention improve or worsen performance?
8. How do textbook scheduling assumptions differ from your Linux observations?
9. What happens if the workload is changed?
10. How would you reproduce the experiment?
11. What did AI suggest?
12. Which AI-generated suggestion did you reject or modify?
13. How would you implement the same mechanism at kernel level?
14. What part of this experiment could become a Rust Micro-OS component?

---

# 30. CO Alignment

| CA-5 Activity | Primary CO | Secondary COs |
|---|---|---|
| Process investigation | CO2 | CO1, CO6 |
| Scheduling/priority | CO2 | CO1, CO6 |
| Threads/concurrency | CO3 | CO2, CO6 |
| Deadlock investigation | CO3 | CO2 |
| Memory investigation | CO4 | CO1, CO6 |
| File/I/O investigation | CO5 | CO1, CO6 |
| Linux tools and `/proc` | CO6 | CO1–CO5 |
| Rust + Linux systems work | CO6 | CO2–CO5 |

**Strongest overall emphasis:** **CO2, CO3, CO4, CO5 and CO6.**

---

# 31. Institutional Philosophy Alignment

## Primary Dimension: Innovation & Professional Development

CA-5 develops the ability to:

- execute practical engineering tasks independently;
- work with real development environments;
- apply design-thinking principles to system problems;
- use modern tools;
- engineer and validate solutions.

### Innovation & Professional Development Mapping

| LO | CA-5 Evidence |
|---|---|
| LO1 – Independent project-based learning | Individual/team Linux engineering challenge |
| LO2 – Industrial observation | Optional comparison with real-world Linux systems |
| LO3 – Design thinking | Diagnose → design → intervene → validate |
| LO4 – Generative AI | Responsible AI-assisted systems engineering |

---

## Secondary Dimension: Real World Exposure

Linux is a practical systems environment used in computing infrastructure, cloud systems, servers, embedded systems and many development environments.

CA-5 emphasizes:

- professional Linux practice;
- system administration awareness;
- resource management;
- troubleshooting;
- command-line engineering;
- teamwork;
- professional responsibility.

---

# 32. CA-5 Philosophy Matrix

| Activity | Innovation & Professional Development | Real World Exposure | Critical Thinking | Research Experience |
|---|---:|---:|---:|---:|
| Linux process investigation | **High** | High | High | Moderate |
| Performance engineering | **High** | **High** | **High** | High |
| IPC/concurrency | **High** | High | High | Moderate |
| Memory/I/O investigation | High | **High** | **High** | High |
| Resource isolation | **High** | **High** | High | Moderate |
| Incident investigation | **High** | **High** | **High** | High |
| Rust/Linux systems work | **High** | High | High | High |
| Technical defence | **High** | **High** | High | Moderate |

---

# 33. PO/PSO Contribution

### PO1 – Engineering Knowledge
Applies OS theory to observable Linux behaviour.

### PO2 – Problem Analysis
Diagnoses real system behaviour using evidence.

### PO3 – Design/Development
Designs and implements interventions.

### PO4 – Conduct Investigations
Uses systematic system-level experiments.

### PO5 – Engineering Tool Usage
**Strong alignment:** Linux, Bash, Python, tracing and monitoring tools.

### PO6 – Engineer and World
Connects OS mechanisms to real computing infrastructure.

### PO7 – Ethics
Emphasizes safe experimentation, responsible AI and system integrity.

### PO8 – Teamwork
Supports collaborative Linux engineering.

### PO9 – Communication
Requires technical documentation and defence.

### PO10 – Project Management
Requires controlled experimentation and milestone planning.

### PO11 – Lifelong Learning
Builds practical Linux systems expertise.

### PSO1
Develops software/system solutions using CSE principles.

### PSO2
Uses Linux, Python, Bash, Rust and modern systems tools.

### PSO3
Provides infrastructure-level understanding relevant to AI/ML workloads, resource management and performance.

---

# 34. CA-5 → CA-6 Rust Micro-OS Bridge

CA-5 should explicitly prepare students for CA-6.

| Linux Experience in CA-5 | Rust Micro-OS Concept in CA-6 |
|---|---|
| Process | Kernel task |
| Thread | Kernel execution context |
| CPU scheduling | Kernel scheduler |
| Priority/affinity | Scheduling policy |
| Context switching observation | Context-switch implementation |
| Mutex/lock | Kernel synchronization |
| `/proc` memory observation | Memory subsystem |
| Memory allocation | Kernel allocator |
| File operations | File-system layer |
| Signals/interrupt concepts | Interrupt handling |
| IPC | System-call/message mechanism |
| Resource control | Kernel resource management |
| Linux boot/system view | Bootloader/kernel architecture |

---

# 35. Suggested CA-6 Preparation Challenges

At the end of CA-5, selected students should be able to answer:

### Scheduler
> “I observed scheduling on Linux. How would I implement a simplified scheduler?”

### Memory
> “I observed process memory. How would a kernel allocate memory?”

### Synchronization
> “I observed thread contention. How would a kernel protect shared data?”

### Process/Task
> “I observed process states. How would a minimal kernel represent a task?”

### I/O
> “I observed file and device interactions. How would a minimal OS abstract I/O?”

These questions become the conceptual entry points for the Rust Micro-OS.

---

# 36. Suggested 4-Week Execution Plan

| Week | Activity | Deliverable |
|---|---|---|
| Week 1 | Linux toolkit + challenge selection | Problem statement |
| Week 2 | Instrumentation + baseline experiment | Initial measurements |
| Week 3 | Engineering intervention + validation | Before/after evidence |
| Week 4 | Analysis + report + demonstration | Final submission |

---

# 37. Recommended Submission Package

1. Problem statement
2. OS mechanism explanation
3. Linux environment specification
4. Bash/Python/Rust source code
5. Experimental commands
6. Raw measurements
7. Process/system observations
8. Graphs/tables
9. Engineering intervention
10. Validation evidence
11. Limitations
12. Conclusion
13. AI-use disclosure

---

# 38. CA-5 Student Checklist

- [ ] I used a real Linux environment.
- [ ] I identified the relevant OS mechanism.
- [ ] I used appropriate Linux tools.
- [ ] I automated repetitive measurements where appropriate.
- [ ] I recorded my environment.
- [ ] I established a baseline.
- [ ] I performed an engineering intervention.
- [ ] I collected quantitative evidence.
- [ ] I validated the result.
- [ ] I explained unexpected behaviour.
- [ ] I considered experimental limitations.
- [ ] I followed laboratory safety rules.
- [ ] I disclosed AI usage.
- [ ] I can explain how the experiment relates to OS theory.
- [ ] I can explain how it could lead toward a Rust Micro-OS implementation.

---

# 39. Overall Educational Significance

CA-5 is the **real-system engineering layer** of the OS continuous-assessment framework.

CA-1 teaches students to **reason about OS problems**.

CA-2 teaches them to **measure OS behaviour**.

CA-3 teaches them to **debug and improve OS-related mechanisms**.

CA-4 teaches them to **investigate research questions**.

CA-5 now requires them to **work directly with Linux as a real operating system**.

CA-6 can then ask them to go one level deeper:

> **Can you implement selected OS mechanisms yourself?**

The resulting pathway is:

> **OS Theory → Simulation → Experiment → Research → Linux Engineering → Rust Systems Programming → Micro-OS**

This makes CA-5 much more than a Linux laboratory. It becomes the **systems-engineering bridge between high-level OS understanding and low-level OS construction**.

---

# 40. One-Line CA-5 Definition

> **CA-5 requires students to investigate and engineer real Operating Systems behaviour using Linux, Bash, Python and selected Rust systems techniques through controlled observation, instrumentation, intervention and validation.**
