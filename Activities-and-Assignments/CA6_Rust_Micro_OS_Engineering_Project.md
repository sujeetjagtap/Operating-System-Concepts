# CA-6 – Rust Micro-OS Engineering Project
## Continuous Assessment – 15 Marks

### Course
**Operating Systems**

### Assessment Position
**CA-6 of 7 | 15 Marks**

---

## 1. Purpose

CA-6 is the **flagship engineering assessment** of the Operating Systems course.

It brings together the conceptual reasoning, experimentation, debugging, research and Linux systems experience developed through CA-1 to CA-5 and challenges students to implement selected operating-system mechanisms in **Rust**.

The central question is:

> **Can students move beyond using an operating system to designing and implementing selected operating-system mechanisms themselves?**

CA-6 should **not** require students to build a production operating system. Instead, students construct a **small educational Micro-OS** in incremental layers and demonstrate the operation of fundamental OS mechanisms.

---

## 2. Position in the CA Progression

| Assessment | Focus | Central Question |
|---|---|---|
| CA-1 – Systems Thinking | Reasoning | What is the OS problem? |
| CA-2 – Performance Investigation | Experimentation | What does the evidence show? |
| CA-3 – Design & Debugging | Engineering | How can it be improved? |
| CA-4 – Research Mini-Project | Research | What remains worth investigating? |
| CA-5 – Linux Systems Engineering | Real OS | How does a real OS behave? |
| **CA-6 – Rust Micro-OS** | **Systems Construction** | **Can I implement the mechanism?** |
| CA-7 – Viva & Demonstration | Defence | Can I explain and defend it? |

The complete progression is:

> **Think → Measure → Debug → Research → Observe → Build → Defend**

---

## 3. Educational Philosophy

> **Do not build a large operating system. Build a small operating system that makes OS mechanisms visible.**

Students should see the relationship:

**OS Concept → Design → Rust Abstraction → Hardware Interaction → Kernel Mechanism → Observable Behaviour**

The Micro-OS should prioritize:

- conceptual clarity;
- incremental development;
- safe experimentation;
- modular architecture;
- measurable behaviour;
- debugging;
- documentation;
- technical defence.

---

## 4. Recommended Project Model

A **Core + Specialization** model is recommended.

### Core – Required for Every Team

Every team should implement and demonstrate:

1. Rust kernel boot;
2. kernel console/output;
3. basic task representation;
4. task/ready queue;
5. Round Robin scheduling;
6. timer-based scheduling;
7. basic synchronization;
8. basic memory allocation;
9. kernel logging/debugging;
10. integrated execution and demonstration.

### Specialization – Choose One

| Track | Advanced Component |
|---|---|
| Scheduler | Priority / MLFQ / workload-aware scheduling |
| Memory | Paging / page-frame allocator |
| Concurrency | Advanced synchronization / lock analysis |
| System Interface | System calls / user-kernel interaction |
| Storage | Minimal block/file-system abstraction |
| Security | Isolation/protection mechanism |
| Research | Implement and evaluate a CA-4 research idea |

This provides a common minimum architecture while allowing stronger students to demonstrate innovation.

---

## 5. Learning Outcomes

After completing CA-6, students should be able to:

- explain the architecture of a minimal operating-system kernel;
- use Rust for low-level systems programming;
- understand the boot-to-kernel execution path;
- represent and manage basic tasks;
- implement a simple CPU scheduling mechanism;
- use timer/interrupt concepts for scheduling;
- implement basic kernel synchronization;
- understand and implement simple memory-allocation mechanisms;
- reason about hardware–software interaction;
- design modular kernel components;
- debug low-level systems software;
- test OS mechanisms systematically;
- collect evidence from a running Micro-OS;
- compare implementation behaviour with Linux/theoretical expectations;
- document and defend systems-engineering decisions.

---

## 6. Rust Language Policy

The **Micro-OS kernel must be implemented in Rust**.

Python may be used for:

- test generation;
- workload generation;
- serial-log analysis;
- scheduler-trace analysis;
- visualization;
- performance comparison;
- build/test automation.

Bash/Linux may be used for:

- building;
- emulation;
- flashing where applicable;
- automation;
- debugging;
- inspection.

### Recommended division

| Layer | Language |
|---|---|
| Micro-OS kernel | **Rust** |
| Build/automation | Rust tooling + Bash |
| Test harness | Python/Bash |
| Trace analysis | Python |
| Visualization | Python |
| Linux comparison experiments | Python + Linux |
| Documentation | Markdown/LaTeX/Word/etc. |

---

## 7. Recommended Development Environment

A practical educational setup should use a **virtualized/emulated environment first**, such as QEMU, rather than requiring students to boot experimental kernels directly on laboratory hardware.

Recommended components may include:

- Rust stable toolchain;
- `cargo`;
- `rustup`;
- target-specific Rust components;
- QEMU;
- Git;
- GDB or equivalent debugger where available;
- Linux development environment.

The exact target architecture and boot configuration should be standardized by faculty.

---

## 8. Architecture of the Educational Micro-OS

A recommended conceptual architecture is:

```text
+--------------------------------------------------+
|              Micro-OS Demonstration              |
+--------------------------------------------------+
|        System Interface / Optional User Layer    |
+--------------------------------------------------+
|       Task Management & CPU Scheduler            |
+--------------------------------------------------+
|     Synchronization / Kernel Data Structures     |
+--------------------------------------------------+
|          Memory Management / Allocator            |
+--------------------------------------------------+
|       Timer / Interrupt / Exception Layer         |
+--------------------------------------------------+
|          Kernel Console / Diagnostics             |
+--------------------------------------------------+
|              Hardware Abstraction                 |
+--------------------------------------------------+
|                Boot / Kernel Entry                |
+--------------------------------------------------+
|                    Hardware                      |
+--------------------------------------------------+
```

Students need not implement every layer at production complexity.

---

## 9. Development Layers

### Layer 1 – Boot

**Objective:** Boot into a minimal Rust kernel and establish a visible kernel entry point.

**Expected capability:**

- kernel starts successfully;
- kernel prints a startup message;
- kernel remains operational.

**Evidence:** boot log, source code, architecture diagram and demonstration.

### Layer 2 – Kernel Console and Diagnostics

Create a simple mechanism for kernel messages:

- information;
- warning/error;
- structured task/debug output.

Students should be able to determine what the kernel is doing.

### Layer 3 – Task Representation

Create a minimal runnable-task abstraction containing, where appropriate:

- task identifier;
- state;
- execution context;
- scheduling information;
- stack/execution resources.

Suggested states:

`READY`, `RUNNING`, `BLOCKED`, `TERMINATED`

### Layer 4 – Ready Queue

Implement a kernel data structure containing runnable tasks.

```text
Task 1 → Task 2 → Task 3 → Task 4
              ↑
          Scheduler
```

Students should understand insertion, selection, removal and ordering.

### Layer 5 – Round Robin Scheduler

Implement Round Robin scheduling.

Required evidence:

- task order;
- time-slice behaviour;
- repeated scheduling;
- scheduler trace;
- task completion.

### Layer 6 – Timer-Driven Scheduling

Connect the scheduler to a periodic timer mechanism where supported by the selected architecture.

Demonstrate the difference between cooperative switching and timer-driven/preemptive-style scheduling.

### Layer 7 – Synchronization

Implement at least one basic synchronization abstraction:

- spinlock;
- mutex-like abstraction;
- protected shared structure;
- interrupt-safe critical section.

Demonstrate shared-resource problem → synchronization → corrected execution.

### Layer 8 – Memory Management

Implement a simple memory-management mechanism such as:

- bump allocator;
- free-list allocator;
- fixed-size block allocator.

Advanced teams may implement:

- frame allocator;
- paging-related structures;
- heap allocator;
- virtual-memory extension.

### Layer 9 – Optional System Interface

Advanced teams may provide a minimal application-to-kernel interface, such as:

- console service;
- task creation;
- memory service;
- system-call abstraction.

### Layer 10 – Integrated Micro-OS

Demonstrate:

```text
Boot
 ↓
Kernel Initialization
 ↓
Create Tasks
 ↓
Ready Queue
 ↓
Timer
 ↓
Scheduler
 ↓
Task Execution
 ↓
Synchronization / Memory
 ↓
Task Completion
```

---

## 10. Core Project Requirements

Every team must demonstrate:

| Requirement | Minimum |
|---|---|
| Boot | Working Rust kernel |
| Task management | At least two controlled tasks |
| Scheduling | Round Robin |
| Timer | Scheduling trigger where supported |
| Synchronization | One working mechanism |
| Memory | One working allocator |
| Diagnostics | Kernel logs/traces |
| Validation | Repeatable test evidence |

---

## 11. Specialization Tracks

### Track A – Scheduler Engineering

Core: Round Robin.

Extensions:

- Priority Scheduling;
- Multilevel Queue;
- MLFQ;
- dynamic priority;
- workload-aware scheduling.

Evaluate response time, waiting time, fairness, throughput and overhead.

### Track B – Memory Engineering

Core: simple allocator.

Extensions:

- free-list allocator;
- page-frame allocator;
- paging abstraction;
- allocation-strategy comparison;
- memory-use statistics.

Evaluate allocation success, latency, fragmentation where applicable and utilization.

### Track C – Concurrency Engineering

Core: basic lock/synchronization.

Extensions:

- spinlock;
- mutex-like mechanism;
- reader/writer abstraction;
- lock-contention measurement;
- deadlock-prevention strategy.

Evaluate contention, throughput, correctness and scalability.

### Track D – System Interface

Core: kernel service interface.

Extensions:

- system calls;
- task creation;
- console service;
- memory service;
- controlled user/kernel interaction.

Demonstrate:

**request → kernel transition → service → return**

### Track E – Storage

Core: conceptual I/O interface.

Extensions:

- block abstraction;
- simple storage driver abstraction;
- file metadata;
- file-like interface.

Recommended only where faculty provides suitable infrastructure.

### Track F – Security and Isolation

Core: identify trust boundaries.

Extensions:

- controlled kernel interfaces;
- memory-access boundaries;
- task isolation concepts;
- privilege separation concepts.

### Track G – Research-to-Micro-OS

Preferred advanced track for strong CA-4 teams.

Question:

> **Can a mechanism investigated experimentally in CA-4 be implemented at a lower systems level?**

Examples:

| CA-4 Research | CA-6 Implementation |
|---|---|
| Round Robin quantum | Rust scheduler |
| Fairness | Fair scheduling policy |
| Lock contention | Kernel synchronization |
| Memory allocation | Rust allocator |
| Page replacement | Page-management prototype |
| Context switching | Task-switching mechanism |
| Resource management | Kernel resource abstraction |

---

## 12. Twenty Suggested Project Variants

| No. | Project | Core | Advanced Extension |
|---:|---|---|---|
| 1 | Minimal Round Robin Micro-OS | Scheduler | Dynamic quantum |
| 2 | Priority Micro-OS | Scheduler | Aging |
| 3 | Fair Scheduling Micro-OS | Scheduler | Fairness analysis |
| 4 | Workload-Aware Scheduler | Scheduler | Adaptive policy |
| 5 | Task Management Kernel | Tasks | Multiple states |
| 6 | Timer-Driven Kernel | Timer | Preemption |
| 7 | Synchronization Kernel | Lock | Contention analysis |
| 8 | Producer–Consumer Kernel | Sync | Multiple producers |
| 9 | Kernel Memory Allocator | Memory | Free-list allocator |
| 10 | Frame Allocation Kernel | Memory | Paging structures |
| 11 | Memory-Aware Scheduler | Memory + Scheduler | Adaptive policy |
| 12 | Minimal System-Call Kernel | Interface | User/kernel boundary |
| 13 | Console-Service Kernel | Interface | Structured logging |
| 14 | Task Isolation Prototype | Security | Protection extension |
| 15 | Block I/O Prototype | Storage | File abstraction |
| 16 | File Metadata Micro-OS | Storage | Directory abstraction |
| 17 | Rust Concurrency Micro-OS | Sync | Performance study |
| 18 | Research-to-Kernel Project | Selected mechanism | CA-4 extension |
| 19 | Linux-vs-Micro-OS Study | Measurement | Cross-platform analysis |
| 20 | Integrated Educational Micro-OS | All core layers | One specialization |

---

## 13. Milestone-Based Development

| Milestone | Deliverable |
|---|---|
| 1 – Boot | Running Rust kernel |
| 2 – Diagnostics | Structured kernel logging |
| 3 – Tasks | Multiple task representations |
| 4 – Scheduler | Working Round Robin scheduler |
| 5 – Timer | Timer-driven scheduling behaviour |
| 6 – Synchronization | Protected shared resource |
| 7 – Memory | Working allocator |
| 8 – Specialization | Advanced component |
| 9 – Integration | Integrated Micro-OS |
| 10 – Validation | Test evidence + report |

---

## 14. Suggested 6-Week Schedule

| Week | Activity | Output |
|---|---|---|
| 1 | Rust systems programming + architecture | Project architecture |
| 2 | Boot + diagnostics | Booting kernel |
| 3 | Tasks + scheduler | Working scheduler |
| 4 | Timer + synchronization + memory | Core mechanisms |
| 5 | Specialization + integration | Integrated Micro-OS |
| 6 | Testing + analysis + documentation | Final demonstration |

---

## 15. Testing Strategy

### Level 1 – Unit-Level Testing

Where feasible, test:

- queue;
- task state;
- allocator;
- scheduler selection;
- lock behaviour.

### Level 2 – Mechanism Testing

Test:

- scheduling;
- timer interaction;
- synchronization;
- memory allocation.

### Level 3 – Integration Testing

Test:

> Boot → initialize → create tasks → schedule → synchronize → allocate → terminate

---

## 16. Required Test Cases

- **TC1 – Minimum Configuration:** two tasks.
- **TC2 – Multiple Tasks:** 3–5 controlled tasks where feasible.
- **TC3 – Boundary Case:** smallest meaningful parameter.
- **TC4 – Stress Case:** larger but safe workload.
- **TC5 – Failure Case:** controlled invalid operation/rejected request.
- **TC6 – Repeatability:** repeat an experiment and compare behaviour.

---

## 17. Evidence Requirements

Students must provide evidence for:

- successful boot;
- task creation;
- scheduler behaviour;
- timer activity;
- synchronization;
- memory allocation;
- specialization component;
- integrated execution.

Evidence may include:

- serial/console logs;
- scheduler traces;
- timing data;
- memory statistics;
- test results;
- source-level debugging evidence;
- performance plots.

> **“It runs” is not sufficient evidence. Students must show what the OS mechanism is doing.**

---

## 18. Performance Evaluation

Where meaningful, collect:

- task-switch count;
- scheduling latency;
- response time;
- throughput;
- fairness;
- allocation time;
- memory utilization;
- synchronization wait time;
- I/O latency.

Use Python for trace parsing and visualization where appropriate.

---

## 19. Python as the Analysis Layer

```text
Rust Micro-OS
     ↓
Scheduler / Kernel Trace
     ↓
Log File
     ↓
Python Parser
     ↓
Data Analysis
     ↓
Graphs
     ↓
Engineering Conclusion
```

This maintains continuity with CA-2, CA-4 and CA-5.

---

## 20. Linux vs Micro-OS Comparison

| Concept | Linux | Student Micro-OS |
|---|---|---|
| Task/process | Mature abstraction | Simplified task |
| Scheduler | Production scheduler | Educational scheduler |
| Memory | Sophisticated VM | Simple allocator |
| Synchronization | Production primitives | Student mechanism |
| I/O | Rich subsystem | Minimal abstraction |
| Security | Extensive mechanisms | Limited educational boundary |
| Hardware support | Broad | Selected target |

The purpose is to understand how complex production abstractions emerge from simpler mechanisms.

---

## 21. Debugging Strategy

Students should follow:

> **Observe → Localize → Hypothesize → Instrument → Modify → Test → Reproduce**

Common targets:

- boot failure;
- invalid memory access;
- scheduler starvation;
- task-state corruption;
- synchronization errors;
- timer configuration errors;
- allocator failures;
- unexpected task ordering.

Maintain a short debugging log documenting important failures and their resolution.

---

## 22. Suggested Git Repository

```text
micro-os/
├── README.md
├── Cargo.toml
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── design.md
│   └── testing.md
├── src/
│   ├── main.rs
│   ├── kernel/
│   ├── task/
│   ├── scheduler/
│   ├── memory/
│   ├── sync/
│   ├── timer/
│   └── drivers/
├── tests/
├── scripts/
├── traces/
└── results/
```

The exact structure may be adapted to the selected Rust kernel architecture.

---

## 23. Technical Documentation

Final report:

1. Title
2. Abstract
3. Problem Statement
4. Objectives
5. OS Concepts
6. Architecture
7. Design Decisions
8. Rust Implementation
9. Scheduling
10. Synchronization
11. Memory Management
12. Specialization Component
13. Testing
14. Results
15. Performance Analysis
16. Limitations
17. Lessons Learned
18. Future Work
19. References
20. AI Usage Disclosure

---

## 24. Architecture Diagram Requirement

Each team submits an architecture diagram showing:

- boot;
- kernel entry;
- task management;
- scheduler;
- timer;
- synchronization;
- memory;
- optional system interface;
- specialization;
- hardware/emulator.

The diagram should show **data/control flow**, not merely named boxes.

---

## 25. AI-Assisted Rust Development

Generative AI may assist with:

- Rust syntax;
- explaining compiler errors;
- test scaffolding;
- debugging hypotheses;
- architecture brainstorming;
- documentation;
- Python trace analysis.

However:

> **Students remain responsible for every line of kernel code submitted.**

Students must understand:

- ownership;
- borrowing;
- lifetimes where relevant;
- `unsafe` Rust;
- raw pointers;
- synchronization;
- memory layout;
- interrupt/context-switch implications.

AI-generated low-level code must not be copied blindly.

---

## 26. `unsafe` Rust Policy

Every significant `unsafe` block should have:

1. a clear reason;
2. documented assumptions;
3. stated invariants;
4. limited scope;
5. validation/testing evidence.

> **Minimize `unsafe`; isolate it behind safe abstractions wherever practical.**

---

## 27. Safety and Laboratory Policy

Prefer:

- QEMU;
- dedicated virtual machines;
- faculty-approved isolated hardware.

Students must not:

- experiment with unknown kernels on shared machines;
- overwrite bootloaders/disks without authorization;
- modify other students' environments;
- access unauthorized devices;
- disable security controls;
- use kernel experiments to interfere with institutional infrastructure.

> **Experiment on controlled resources, not laboratory infrastructure.**

---

## 28. 15-Mark Assessment Structure

| Criterion | Marks |
|---|---:|
| Architecture and OS mechanism design | 2 |
| Rust implementation quality | 4 |
| Core OS functionality | 3 |
| Testing, debugging and validation | 2 |
| Performance/evidence-based evaluation | 2 |
| Innovation / specialization | 1 |
| Documentation and technical demonstration | 1 |
| **Total** | **15** |

---

## 29. Detailed Rubric

| Criterion | Excellent | Good | Developing | Needs Improvement |
|---|---|---|---|---|
| Architecture | Clear modular design with justified decisions | Sound architecture | Basic design | Poorly structured |
| Rust implementation | Correct, idiomatic and controlled low-level code | Mostly correct | Several issues | Incomplete/incorrect |
| Core functionality | All mechanisms work and integrate | Most work | Partial integration | Major failures |
| Testing/debugging | Systematic and reproducible | Adequate | Limited | Minimal |
| Performance/evidence | Quantitative, insightful analysis | Meaningful measurements | Basic evidence | Unsupported claims |
| Innovation | Strong specialization/extension | Useful extension | Limited extension | None |
| Documentation/demo | Clear and technically defensible | Good | Some gaps | Poor |

---

## 30. Performance Levels

### Outstanding
Functioning Micro-OS with clear architecture, correct core mechanisms, strong evidence, meaningful specialization and excellent defence.

### Proficient
Required mechanisms are correctly implemented and demonstrated.

### Developing
Major components are present but validation and independent engineering are limited.

### Beginning
Kernel is incomplete or mechanisms cannot be adequately demonstrated or explained.

---

## 31. Individual Contribution

For team projects, each student must identify:

- subsystem owned;
- code contributed;
- experiments performed;
- documentation contributed;
- debugging contribution.

Faculty may conduct an individual viva to verify contribution.

---

## 32. Individual Viva Questions

1. What happens immediately after the kernel starts?
2. How is a task represented?
3. How does the scheduler select the next task?
4. Why did you choose Round Robin?
5. What triggers a scheduling decision?
6. What happens during a timer tick?
7. How is shared kernel data protected?
8. Why is synchronization required?
9. How does your allocator work?
10. What happens when allocation fails?
11. Where is `unsafe` used and why?
12. What invariant does your `unsafe` code rely on?
13. What happens if two tasks access the same resource?
14. How did you test the scheduler?
15. How did you establish that the scheduler is actually working?
16. How is your Micro-OS different from Linux?
17. What did CA-5 teach you that helped this project?
18. What CA-4 research question could be extended into your Micro-OS?
19. What would you implement next?
20. What is the most important limitation of your current system?

---

## 33. CO Alignment

| CA-6 Component | Primary CO | Secondary COs |
|---|---|---|
| Kernel architecture | CO1 | CO6 |
| Task management | CO2 | CO1, CO6 |
| Scheduling | CO2 | CO1, CO6 |
| Synchronization | CO3 | CO2, CO6 |
| Memory management | CO4 | CO1, CO6 |
| File/I/O extension | CO5 | CO1, CO6 |
| Rust/Linux systems engineering | CO6 | CO1–CO5 |
| Performance validation | CO2–CO5 | CO6 |

**Overall emphasis:** CO6 is strongly demonstrated through implementation, while CO2–CO5 are demonstrated through the corresponding OS mechanisms.

---

## 34. Institutional Philosophy Alignment

### Primary Dimension: Innovation & Professional Development

CA-6 directly supports:

- independent project-based learning;
- engineering design;
- modern systems programming;
- creative problem solving;
- Generative AI-assisted development;
- professional software engineering practices.

| LO | CA-6 Evidence |
|---|---|
| LO1 – Independent project work | Micro-OS development |
| LO2 – Industrial awareness | Comparison with real OS practices |
| LO3 – Design thinking | Architecture + specialization |
| LO4 – Generative AI | Responsible AI-assisted Rust development |

### Secondary Dimension: Critical Thinking

Students must:

- challenge assumptions;
- reason about kernel behaviour;
- analyze implementation trade-offs;
- diagnose failures;
- justify architecture;
- evaluate performance evidence.

### Secondary Dimension: Research Experience

Research continuity is created through:

- CA-4 research-to-Micro-OS extensions;
- performance measurement;
- literature-informed design;
- hypothesis-driven evaluation;
- future-work identification.

### Real World Exposure

CA-6 provides exposure to:

- systems programming;
- version control;
- debugging;
- modular architecture;
- low-level programming;
- performance engineering;
- software testing;
- technical documentation;
- engineering trade-offs.

---

## 35. CA-6 Institutional Philosophy Matrix

| Activity | Innovation & Professional Development | Critical Thinking | Research Experience | Real World Exposure |
|---|---:|---:|---:|---:|
| Kernel architecture | **High** | **High** | Moderate | High |
| Scheduler implementation | **High** | **High** | High | High |
| Synchronization | High | **High** | High | High |
| Memory subsystem | **High** | **High** | High | High |
| Rust programming | **High** | High | Moderate | **High** |
| Performance evaluation | High | **High** | **High** | High |
| Specialization | **High** | **High** | **High** | High |
| Technical defence | **High** | High | High | **High** |

---

## 36. PO/PSO Contribution

### PO1 – Engineering Knowledge
Applies OS, computer architecture and systems-programming knowledge.

### PO2 – Problem Analysis
Analyzes kernel-level problems and implementation failures.

### PO3 – Design/Development
**Strongest alignment:** designs and implements an integrated Micro-OS.

### PO4 – Conduct Investigations
Tests and evaluates kernel mechanisms experimentally.

### PO5 – Engineering Tool Usage
Uses Rust, Cargo, QEMU, Linux, Git and debugging tools.

### PO6 – Engineer and World
Connects kernel engineering to real computing infrastructure.

### PO7 – Ethics
Requires safe experimentation, responsible AI use and software integrity.

### PO8 – Teamwork
Supports collaborative subsystem development.

### PO9 – Communication
Requires architecture documentation, report and technical defence.

### PO10 – Project Management
Requires milestone planning, subsystem ownership and integration.

### PO11 – Lifelong Learning
Introduces modern systems-programming practices and Rust.

### PSO1
Strongly develops software/hardware-oriented systems solutions.

### PSO2
Strongly develops modern-tool and emerging-technology usage.

### PSO3
Provides infrastructure-level understanding relevant to AI/ML systems, especially scheduling, memory and resource management.

---

## 37. Direct CA-1 to CA-6 Traceability

| CA | Student Experience | CA-6 Application |
|---|---|---|
| CA-1 | Systems reasoning | Architecture decisions |
| CA-2 | Performance experiments | Scheduler/memory evaluation |
| CA-3 | Debugging | Kernel debugging |
| CA-4 | Research | Research-to-Micro-OS track |
| CA-5 | Linux systems | Real OS comparison |
| **CA-6** | **Micro-OS** | **Integrated systems implementation** |

---

## 38. CA-4 → CA-5 → CA-6 Example: CPU Scheduling

### CA-4
Investigate:

> Does maximizing throughput reduce fairness?

### CA-5
Observe Linux CPU allocation and investigate priorities, affinity and workload behaviour.

### CA-6
Implement:

> A Round Robin or fairness-oriented scheduler in Rust.

### Final comparison

Discuss:

**Simulation → Linux → Micro-OS**

This demonstrates the difference between:

- theoretical model;
- production OS;
- educational implementation.

---

## 39. CA-4 → CA-5 → CA-6 Example: Memory

### CA-4
Investigate:

> How do different allocation strategies affect fragmentation?

### CA-5
Observe real Linux process memory behaviour.

### CA-6
Implement:

> A simple Rust kernel allocator.

### Advanced
Compare allocation success, latency, fragmentation and implementation complexity.

---

## 40. CA-4 → CA-5 → CA-6 Example: Synchronization

### CA-4
Research:

> How does lock contention affect scalability?

### CA-5
Observe concurrency and contention on Linux.

### CA-6
Implement:

> A kernel-level synchronization abstraction in Rust.

### Advanced
Measure lock acquisition, contention, throughput and fairness.

---

## 41. Expected Student Mindset

CA-6 should move students from:

> “I wrote code that works.”

to:

> “I designed a mechanism, implemented it, tested it, measured its behaviour, understood its limitations and can defend the engineering decisions behind it.”

---

## 42. Final Submission Package

Each team submits:

1. Rust Micro-OS source repository;
2. architecture document;
3. design document;
4. test plan;
5. test results;
6. performance data where applicable;
7. Python analysis scripts where applicable;
8. debugging log;
9. final technical report;
10. demonstration;
11. individual contribution statement;
12. AI usage disclosure.

---

## 43. Final Student Checklist

- [ ] Kernel boots successfully.
- [ ] Kernel diagnostics work.
- [ ] Tasks are represented correctly.
- [ ] Ready queue works.
- [ ] Round Robin scheduling works.
- [ ] Timer mechanism is integrated where applicable.
- [ ] Synchronization mechanism works.
- [ ] Memory allocator works.
- [ ] Specialization is implemented.
- [ ] Components are integrated.
- [ ] Test cases are documented.
- [ ] Results are reproducible.
- [ ] Performance evidence is included where meaningful.
- [ ] Important failures and debugging decisions are documented.
- [ ] `unsafe` Rust is justified.
- [ ] Source code is version-controlled.
- [ ] Report is complete.
- [ ] AI use is disclosed.
- [ ] Every team member can explain the complete system.

---

## 44. Overall Educational Significance

CA-6 is the **culminating systems-engineering experience** of the Operating Systems course.

The student journey is intentionally progressive:

> **Understand OS mechanisms**  
> ↓  
> **Simulate them in Python**  
> ↓  
> **Measure their behaviour**  
> ↓  
> **Debug and redesign them**  
> ↓  
> **Investigate them as research problems**  
> ↓  
> **Observe them on Linux**  
> ↓  
> **Implement simplified mechanisms in Rust**  
> ↓  
> **Integrate them into a Micro-OS**  
> ↓  
> **Defend the engineering decisions**

The Micro-OS is therefore not an isolated programming assignment. It is the **engineering culmination of the entire CA framework**.

---

## 45. One-Line CA-6 Definition

> **CA-6 requires students to design and implement a minimal educational Micro-OS in Rust, integrating fundamental OS mechanisms such as task management, scheduling, timer-driven execution, synchronization and memory management, and to validate and defend the resulting system through controlled evidence.**
