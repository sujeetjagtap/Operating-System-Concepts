# Operating Systems – CA-3
## OS Design & Debugging Challenge
### Continuous Assessment: 10 Marks

---

## 1. Overview

The **OS Design & Debugging Challenge** is the third Continuous Assessment (CA) component of the Operating Systems course.

CA-1 developed **systems thinking** through scenario-based reasoning.

CA-2 developed **experimental thinking** through measurement and performance investigation.

CA-3 now moves students into **engineering intervention**:

> **Understand → Diagnose → Design → Implement → Debug → Validate → Defend**

Students are given a partially completed, inefficient, incorrect, unsafe, or intentionally defective operating-system-related implementation or design. They must identify the underlying problem, reason about its cause, propose alternatives, implement an appropriate solution, test it, and defend their design.

The assessment is deliberately designed to test whether students can **understand why a system fails**, rather than merely repair code through trial and error.

---

# 2. Purpose of the Challenge

Real operating-system engineering involves dealing with:

- Race conditions
- Deadlocks
- Starvation
- Scheduling inefficiencies
- Memory fragmentation
- Excessive page faults
- Incorrect resource allocation
- I/O bottlenecks
- Process-management errors
- Synchronization failures
- File-system inconsistencies
- Resource exhaustion
- Incorrect system-call usage

Students therefore need to develop the ability to move from:

> **“The program does not work.”**

to:

> **“The system exhibits this specific failure because this OS mechanism violates this condition; here are the possible remedies, this is the one I selected, and these tests demonstrate that the problem has been resolved.”**

---

# 3. Learning Intent

After completing CA-3, students should be able to:

1. Diagnose defects in OS-related algorithms and programs.
2. Distinguish symptoms from root causes.
3. Trace execution and resource interactions.
4. Identify race conditions, deadlocks, starvation and resource-management errors.
5. Design corrective mechanisms.
6. Implement and test the selected solution.
7. Construct meaningful test cases, including edge cases.
8. Compare alternative corrective approaches.
9. Validate that a fix does not introduce another problem.
10. Explain trade-offs associated with the selected design.
11. Use AI as a debugging assistant while independently verifying all suggestions.
12. Communicate technical reasoning clearly.
13. Progress from high-level OS algorithms toward low-level systems implementation.

---

# 4. Assessment Structure

| Component | Marks |
|---|---:|
| Problem diagnosis and root-cause identification | 2 |
| System/algorithm modelling and reasoning | 2 |
| Solution design and alternative analysis | 2 |
| Implementation and validation | 2 |
| Technical defence, trade-offs and communication | 2 |
| **Total** | **10** |

---

# 5. The Student Debugging Framework

Every CA-3 challenge should follow the following seven-stage process.

## Stage 1 – Observe the Failure

Students should first identify what the system is actually doing.

Examples:

- Incorrect output
- Infinite waiting
- Program freeze
- Unexpected termination
- Excessive CPU consumption
- Excessive memory usage
- Incorrect scheduling results
- Incorrect resource allocation
- Data inconsistency
- Starvation

Students must not immediately modify the code.

---

# 6. Stage 2 – Identify the OS Concept

Students should determine which OS mechanism is involved.

Possible areas include:

- Process management
- CPU scheduling
- Threads
- Synchronization
- Deadlocks
- Memory management
- Virtual memory
- File systems
- Disk scheduling
- I/O
- IPC
- Linux process behaviour
- System calls

The student must explain:

> **Why is this an OS problem rather than simply a programming syntax error?**

---

# 7. Stage 3 – Model the Failure

Students should create an appropriate model.

Examples:

### Concurrency

```text
Thread A → Shared Resource ← Thread B
```

### Deadlock

```text
P1 → R2
↑    ↓
R1 ← P2
```

### Scheduling

```text
Ready Queue → Scheduler → CPU
```

### Memory

```text
Process
   ↓
Logical Address
   ↓
Page Table
   ↓
Physical Frame
```

### File/I/O

```text
Process → File System → Buffer → Device
```

Students should use:

- diagrams
- tables
- execution traces
- state transitions
- resource graphs
- Gantt charts
- memory maps
- page-reference traces

as appropriate.

---

# 8. Stage 4 – Determine the Root Cause

Students should distinguish:

### Symptom

> Program hangs.

### Immediate cause

> Thread A is waiting for a lock.

### Root cause

> Circular wait exists because two threads acquire shared resources in different orders.

The root-cause statement should identify the underlying OS principle that has been violated.

---

# 9. Stage 5 – Analyze Alternative Fixes

Students should consider at least two possible corrective approaches whenever feasible.

For example, for deadlock:

- Resource ordering
- Deadlock avoidance
- Timeout/retry
- Detection and recovery

For race conditions:

- Mutex
- Semaphore
- Atomic operations
- Message passing

For scheduling:

- Change scheduling algorithm
- Change priority policy
- Adjust time quantum
- Modify workload handling

Students should compare:

- Correctness
- Performance
- Complexity
- Scalability
- Fairness
- Resource consumption
- Implementation difficulty

---

# 10. Stage 6 – Implement and Validate the Fix

Students must implement the selected solution using the specified programming language.

## Programming Language Policy

### Default language: Python 3.x

Python should be used for:

- OS algorithm debugging
- Scheduling simulators
- Deadlock detection
- Memory allocation
- Page replacement
- Disk scheduling
- File-system simulations
- Concurrency demonstrations where appropriate

### Linux experiments

Use:

- Python 3.x
- Bash
- Linux utilities

where the challenge requires observation of a real operating system.

### Rust

Rust should be used for selected advanced systems-programming challenges involving:

- Threads
- Synchronization
- Memory safety
- Low-level resource management
- Systems programming

Rust challenges are especially encouraged as preparation for the later **Micro-OS Engineering Project**.

---

# 11. Stage 7 – Prove That the Fix Works

Students must not conclude:

> “The program works now.”

They must demonstrate it.

Validation should include:

- Original failing test
- Corrected test
- Boundary cases
- Stress cases
- Invalid/edge cases where appropriate
- Performance comparison where relevant

Students should demonstrate:

> **Failure → Fix → Retest → Evidence**

---

# 12. Core Debugging Principle

Students should learn the following distinction:

> **Fixing a symptom is not necessarily fixing the system.**

Example:

If a thread waits indefinitely, simply adding a timeout may hide the symptom.

Students should ask:

- Why is the thread waiting?
- Is the wait expected?
- Is there deadlock?
- Is there starvation?
- Is the scheduling policy responsible?
- Is resource ownership incorrect?

---

# 13. Challenge Bank

The following challenges may be used directly or adapted for individual students/teams.

---

# CATEGORY A – PROCESS MANAGEMENT

## Challenge A1 – Incorrect Process-State Transition

A process simulator occasionally moves a terminated process back into the ready queue.

### Students must

1. Identify the incorrect state transition.
2. Draw the correct process-state model.
3. Trace the defective execution.
4. Correct the transition logic.
5. Test all process termination scenarios.

### Programming Language

**Python 3.x**

### Concepts

Process states, PCB, process lifecycle.

---

## Challenge A2 – Zombie Process Accumulation

A Linux program creates child processes but fails to correctly handle their termination.

### Students must

- Identify zombie processes.
- Explain why they occur.
- Trace parent-child relationships.
- Correct the program.
- Verify the process table before and after the fix.

### Programming Language

**Python 3.x + Linux**

Optional advanced implementation:

**Rust**

### Tools

Appropriate Linux process inspection tools.

---

## Challenge A3 – Runaway Child Creation

A program unexpectedly creates a large number of child processes.

### Students must

- Diagnose process creation behaviour.
- Identify the cause.
- Determine resource implications.
- Design a safe correction.
- Test process limits and termination behaviour.

### Programming Language

**Python 3.x**

Optional:

**Rust**

---

# CATEGORY B – CPU SCHEDULING

## Challenge B1 – Incorrect Round Robin Scheduler

A provided Python scheduler produces incorrect waiting times.

### Students must

1. Reconstruct the expected execution sequence.
2. Identify the algorithmic defect.
3. Correct the implementation.
4. Validate using multiple test cases.
5. Compare results with a reference calculation.

### Programming Language

**Python 3.x**

---

## Challenge B2 – Starvation in Priority Scheduling

A priority scheduler continuously delays low-priority processes.

### Students must

- Demonstrate starvation.
- Identify the cause.
- Propose at least two solutions.
- Implement aging or another selected strategy.
- Compare waiting-time distributions before and after the fix.

### Programming Language

**Python 3.x**

---

## Challenge B3 – Excessive Context Switching

A Round Robin implementation produces an unexpectedly large number of context switches.

Students must determine whether:

- Time quantum is too small.
- Workload is inappropriate.
- Implementation is incorrect.

### Programming Language

**Python 3.x**

---

## Challenge B4 – Scheduling Policy Selection

A defective scheduling system performs poorly for an interactive workload.

Students must redesign the scheduling policy and justify the change using measured evidence.

### Programming Language

**Python 3.x**

---

# CATEGORY C – THREADS AND RACE CONDITIONS

## Challenge C1 – Incorrect Bank Account Balance

Multiple threads update a shared account.

The final balance varies between executions.

### Students must

1. Reproduce the failure.
2. Identify the race condition.
3. Locate the critical section.
4. Model concurrent execution.
5. Compare synchronization approaches.
6. Implement a correction.
7. Test repeatedly.

### Programming Language

**Python 3.x**

Advanced extension:

**Rust**

---

## Challenge C2 – Double Booking

Multiple threads attempt to reserve the same resource.

The system occasionally allocates the same resource twice.

### Students must design a correct synchronization mechanism.

### Programming Language

**Python 3.x**

Optional:

**Rust**

---

## Challenge C3 – Shared Counter Failure

Several threads increment a shared counter.

The final value is less than expected.

Students must identify why apparently simple operations are not necessarily safe under concurrency.

### Programming Language

**Python 3.x**

---

## Challenge C4 – Producer-Consumer Buffer Failure

A producer-consumer implementation experiences:

- Buffer overflow
- Buffer underflow
- Incorrect synchronization
- Indefinite waiting

Students must diagnose and repair the implementation.

### Programming Language

**Python 3.x**

Optional:

**Rust**

---

# CATEGORY D – DEADLOCK

## Challenge D1 – Two-Lock Deadlock

Two threads acquire two locks in opposite order.

Students must:

- Reproduce the deadlock.
- Construct a wait-for/resource graph.
- Identify the deadlock condition.
- Propose at least two solutions.
- Implement one.
- Demonstrate absence of deadlock under repeated tests.

### Programming Language

**Python 3.x**

Advanced:

**Rust**

---

## Challenge D2 – Dining Philosophers Failure

A provided implementation occasionally freezes.

Students must identify:

- Mutual exclusion
- Hold and wait
- No preemption
- Circular wait

and implement a solution.

### Programming Language

**Python 3.x**

---

## Challenge D3 – Banker's Algorithm Defect

A Banker's Algorithm implementation incorrectly labels an unsafe state as safe.

Students must:

1. Construct the correct safety sequence.
2. Locate the implementation defect.
3. Correct it.
4. Generate safe and unsafe test cases.

### Programming Language

**Python 3.x**

---

# CATEGORY E – MEMORY MANAGEMENT

## Challenge E1 – First Fit Implementation Error

A memory allocator incorrectly allocates a process to a block that cannot accommodate it.

Students must:

- Trace the allocation.
- Identify the defect.
- Correct the implementation.
- Test fragmentation cases.

### Programming Language

**Python 3.x**

---

## Challenge E2 – Memory Fragmentation Diagnosis

A simulation reports sufficient free memory but fails a large allocation.

Students must determine whether the problem is:

- External fragmentation
- Internal fragmentation
- Allocation strategy
- Incorrect bookkeeping

### Programming Language

**Python 3.x**

---

## Challenge E3 – Memory Leak Investigation

A Linux/Python application gradually consumes memory.

Students must investigate whether the apparent memory growth is due to:

- Retained objects
- Caching
- Workload growth
- Process behaviour

and propose a corrective approach.

### Programming Language

**Python 3.x + Linux**

---

# CATEGORY F – VIRTUAL MEMORY

## Challenge F1 – Incorrect LRU Implementation

A page-replacement simulator produces fewer/more page faults than expected.

Students must:

- Trace page references.
- Identify the replacement error.
- Correct the algorithm.
- Validate with known cases.

### Programming Language

**Python 3.x**

---

## Challenge F2 – Detecting Belady's Anomaly

A FIFO implementation unexpectedly produces more page faults when additional frames are provided.

Students must determine whether:

- The result represents Belady's anomaly.
- The implementation is defective.

### Programming Language

**Python 3.x**

---

## Challenge F3 – Thrashing Diagnosis

A simulated multi-programming system experiences rapidly increasing page faults.

Students must:

- Identify the symptom.
- Determine the root cause.
- Analyze working-set behaviour.
- Propose corrective mechanisms.

### Programming Language

**Python 3.x**

---

# CATEGORY G – FILE SYSTEMS

## Challenge G1 – File Allocation Error

A file-system simulator incorrectly maps file blocks.

Students must identify and correct the allocation logic.

### Programming Language

**Python 3.x**

---

## Challenge G2 – File-System Consistency Failure

A simulated system crashes during file updates and leaves inconsistent metadata.

Students must design a recovery mechanism.

### Programming Language

**Python 3.x**

---

## Challenge G3 – Directory Search Bottleneck

A simulated file system becomes slow as the number of files increases.

Students must diagnose the design limitation and propose alternatives.

### Programming Language

**Python 3.x**

---

# CATEGORY H – DISK SCHEDULING

## Challenge H1 – Incorrect SSTF Scheduler

A provided implementation does not always select the nearest request.

Students must:

- Trace the request sequence.
- Identify the error.
- Correct the implementation.
- Calculate total head movement.

### Programming Language

**Python 3.x**

---

## Challenge H2 – Starvation in SSTF

A workload causes some disk requests to wait excessively.

Students must demonstrate starvation and compare SSTF with SCAN/LOOK-based approaches.

### Programming Language

**Python 3.x**

---

# CATEGORY I – I/O AND LINUX

## Challenge I1 – High I/O Wait

A Linux workload exhibits:

- Low CPU utilization
- High I/O wait
- Long request queues

Students must investigate the root cause using appropriate Linux tools.

### Programming Language

**Python 3.x + Linux tools**

---

## Challenge I2 – Slow File Processing

A Python program processes thousands of files inefficiently.

Students must determine whether the bottleneck is:

- File access
- Directory traversal
- CPU processing
- Synchronization
- Excessive system calls

### Programming Language

**Python 3.x**

---

## Challenge I3 – System Call Investigation

A program unexpectedly makes a large number of system calls.

Students must investigate the behaviour and propose an optimization.

### Programming Language

**Python 3.x + Linux**

---

# CATEGORY J – LINUX SYSTEM DEBUGGING

## Challenge J1 – CPU-Hungry Process

A Linux program consumes excessive CPU.

Students must:

1. Identify the process.
2. Determine whether it is CPU-bound.
3. Investigate its behaviour.
4. Diagnose the cause.
5. Modify the implementation.
6. Validate the improvement.

### Programming Language

**Python 3.x + Linux**

---

## Challenge J2 – Process Resource Exhaustion

A program gradually consumes system resources until execution becomes unstable.

Students must investigate process/resource limits and design mitigation.

### Programming Language

**Python 3.x + Linux**

---

# CATEGORY K – RUST SYSTEMS DEBUGGING

These challenges are intended for advanced students or as preparation for the Micro-OS project.

## Challenge K1 – Rust Data Race Prevention

A Rust concurrent program uses shared state incorrectly.

Students must determine how Rust's ownership and synchronization model affects the design.

### Programming Language

**Rust**

### Concepts

- Ownership
- Borrowing
- `Arc`
- `Mutex`
- Threads
- Safe concurrency

---

## Challenge K2 – Rust Memory Management Design

Students are given a simplified memory allocator and must identify allocation/deallocation errors.

### Programming Language

**Rust**

### Objective

Connect:

> OS memory management → low-level systems programming → Rust memory safety

---

## Challenge K3 – Rust Task Scheduler

Students are provided a simplified task scheduler.

They must correct:

- Task-state transitions
- Queue handling
- Scheduling decisions

### Programming Language

**Rust**

This directly prepares students for the later Micro-OS scheduler.

---

# 14. Advanced Integrated Challenges

## Integrated Challenge I1 – Server Freeze

A server intermittently becomes unresponsive.

Evidence:

- CPU utilization: 40%
- Memory utilization: 80%
- Several blocked processes
- High I/O wait
- One process holds a lock for a long time

Students must determine whether the primary issue is:

- CPU scheduling
- Synchronization
- Memory pressure
- I/O
- Deadlock
- Combination of mechanisms

They must formulate a diagnosis rather than assuming the first plausible explanation.

### Programming Language

**Python 3.x + Linux**

---

## Integrated Challenge I2 – Online Banking Failure

Multiple requests simultaneously modify account data.

Observed symptoms:

- Incorrect balances
- Occasional duplicate transactions
- Increased response time

Students must investigate:

- Concurrency
- Synchronization
- Scheduling
- I/O

### Programming Language

**Python 3.x**

Advanced:

**Rust**

---

## Integrated Challenge I3 – Memory and Scheduling Interaction

A system runs many applications simultaneously.

Observed:

- High page faults
- Reduced CPU utilization
- Long process waiting times

Students must determine how memory pressure affects apparent scheduling performance.

### Programming Language

**Python 3.x**

---

# 15. Design Challenges – Students Create the Solution

Not every CA-3 challenge should provide defective code.

Some challenges should provide only a requirement.

Example:

> Design a synchronization mechanism for a shared booking service that prevents double allocation while maintaining reasonable concurrency.

Students must:

1. Define correctness requirements.
2. Identify shared resources.
3. Propose multiple designs.
4. Select one.
5. Implement it.
6. Test it.
7. Defend the decision.

### Programming Language

**Python 3.x**

Advanced option:

**Rust**

---

# 16. Fault Injection Challenges

Faculty can deliberately introduce one or more faults into a correct implementation.

Examples:

- Remove a lock.
- Reverse lock acquisition order.
- Change a scheduling comparison.
- Introduce an off-by-one page-table error.
- Modify a page replacement condition.
- Alter memory allocation bookkeeping.
- Introduce an incorrect process-state transition.
- Remove a `wait`.
- Change resource-release ordering.

Students receive:

> **A working system + one hidden defect**

and must locate it.

This approach is particularly effective because students cannot simply memorize the expected answer.

---

# 17. Debugging Without Source Code

An advanced version can provide only:

- Symptoms
- Logs
- Execution traces
- Performance measurements
- Process states
- Resource graphs

Students must infer the likely defect before receiving the implementation.

This develops **diagnostic reasoning**.

---

# 18. Required Student Response Format

Every submission should contain:

## 1. Problem Statement

Describe the observed failure.

## 2. OS Concept

Identify the relevant OS mechanism.

## 3. Failure Reproduction

Show how the failure can be reproduced.

## 4. System Model

Provide the relevant diagram/trace/model.

## 5. Root Cause

Explain the underlying reason for the failure.

## 6. Alternative Solutions

Present at least two approaches where feasible.

## 7. Selected Design

Explain the chosen solution.

## 8. Implementation

Provide corrected or newly designed implementation.

## 9. Validation

Provide test cases and results.

## 10. Performance/Trade-off Analysis

Explain whether the fix introduces:

- Additional overhead
- Reduced concurrency
- Increased memory use
- Complexity
- Other limitations

## 11. AI Disclosure

Explain any AI assistance and independently verify suggestions.

## 12. Final Defence

Summarize why the solution is correct.

---

# 19. Test-Case Design Requirements

Students must not test only the original failing case.

Tests should include, where relevant:

### Normal case

Expected operating condition.

### Boundary case

Minimum/maximum values.

### Stress case

Large workload or high concurrency.

### Adversarial case

Input designed to expose weaknesses.

### Recovery case

System behaviour after failure.

Example for a scheduler:

- One process
- Multiple processes
- Equal burst times
- Different arrival times
- Very large burst
- Very small time quantum
- Same priority
- Extreme priority difference

---

# 20. Regression Testing

A successful fix must not break previously working functionality.

Students should compare:

> **Before Fix → After Fix**

for:

- Correctness
- Performance
- Resource consumption
- Edge cases

This introduces the professional concept of **regression testing**.

---

# 21. AI-Assisted Debugging Policy

AI may be used as a debugging assistant.

Students may ask AI to:

- Explain an error.
- Suggest possible root causes.
- Generate hypotheses.
- Review synchronization logic.
- Suggest test cases.
- Critique a proposed design.
- Explain unfamiliar Linux behaviour.

However:

> **Students must independently verify every AI-generated diagnosis and solution.**

### Required AI record

| Item | Student Response |
|---|---|
| AI tool | |
| Prompt/purpose | |
| Important suggestion | |
| Student verification | |
| Final assessment | Correct / Partial / Incorrect |

Students should identify cases where AI:

- Misdiagnosed the problem.
- Proposed an unsafe solution.
- Ignored an OS constraint.
- Suggested code that works superficially but violates the intended design.

---

# 22. Assessment Rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| **Problem Diagnosis** | Incorrect/no diagnosis | Identifies symptom but weak root cause | Correctly identifies root cause using OS reasoning |
| **Modelling & Reasoning** | Missing/incorrect model | Partially appropriate | Clear and technically appropriate model |
| **Solution Design** | No viable solution | One reasonable solution | Multiple alternatives compared and justified |
| **Implementation & Validation** | Incorrect/not validated | Basic implementation/testing | Correct implementation with comprehensive validation |
| **Technical Defence** | Unsupported explanation | Basic explanation | Strong evidence-based defence with trade-offs |
| **TOTAL** | | | **10** |

---

# 23. Performance Levels

| Level | Student Behaviour |
|---|---|
| **Basic** | Locates and corrects an obvious defect. |
| **Developing** | Explains why the defect occurs and validates the correction. |
| **Proficient** | Compares alternative solutions and evaluates trade-offs. |
| **Advanced** | Identifies hidden interactions and edge cases. |
| **Exceptional** | Redesigns the mechanism, validates experimentally and identifies limitations/future improvements. |

---

# 24. Faculty Challenge Design Principles

A good CA-3 challenge should contain:

1. A reproducible failure.
2. A meaningful OS concept.
3. A non-trivial root cause.
4. At least one plausible alternative solution.
5. A measurable way to validate the solution.
6. An opportunity to discuss trade-offs.
7. Scope appropriate to a 10-mark assessment.

Avoid challenges where:

- The error is merely syntax.
- The correction is obvious.
- Students only change one line without understanding it.
- There is no meaningful validation.
- AI can trivially identify the answer without experimentation.

---

# 25. Recommended Difficulty Distribution

| Difficulty | Weight | Nature |
|---|---:|---|
| **Level 1 – Diagnose** | 20% | Identify known OS defect |
| **Level 2 – Debug** | 30% | Diagnose + repair |
| **Level 3 – Design** | 30% | Compare and implement alternatives |
| **Level 4 – Redesign** | 20% | Open-ended system improvement |

---

# 26. Recommended Individual/Team Model

CA-3 can use a hybrid model.

### Individual

Each student diagnoses a small defect independently.

### Team

Teams solve larger design challenges.

### Challenge Rotation

Students can rotate through:

1. Scheduling
2. Synchronization
3. Deadlock
4. Memory
5. Linux

This ensures exposure to multiple OS subsystems.

---

# 27. Connection with CA-1 and CA-2

CA-3 intentionally completes the first three stages of the OS learning progression.

| CA | Core Question | Student Action |
|---|---|---|
| **CA-1 – Systems Thinking** | What is happening and what should the OS do? | **Analyze & Decide** |
| **CA-2 – Performance Investigation** | What does the evidence tell us? | **Measure & Compare** |
| **CA-3 – Design & Debugging** | Can we design/fix the mechanism? | **Implement & Validate** |

The progression becomes:

> **Reason → Measure → Build/Fix**

---

# 28. Connection with the Rust Micro-OS

CA-3 should deliberately introduce the types of defects students will eventually encounter while implementing a Micro-OS.

| CA-3 Challenge | Micro-OS Connection |
|---|---|
| Process-state bug | Kernel task state |
| Scheduler bug | Kernel scheduler |
| Race condition | Kernel synchronization |
| Deadlock | Kernel resource management |
| Memory allocation bug | Kernel allocator |
| Page-table bug | Virtual memory |
| I/O bug | Device/console subsystem |
| System-call error | Kernel/user interface |
| Rust concurrency | Safe kernel concurrency |
| Resource leak | Kernel resource lifecycle |

This allows students to encounter the engineering principle:

> **A small systems-level defect can produce a large system-level failure.**

---

# 29. Suggested Rust Bridge Challenge

Before the full Micro-OS project, one advanced CA-3 challenge can be:

## “Repair the Rust Task Scheduler”

Students receive a simplified Rust task scheduler with one or more defects.

They must:

1. Understand the task-state model.
2. Identify the scheduling defect.
3. Trace task transitions.
4. Repair the scheduler.
5. Add test cases.
6. Measure scheduling behaviour.
7. Explain how the implementation would change inside a real kernel.

### Programming Language

**Rust**

This becomes the ideal bridge between:

> **Python OS simulation → Linux systems programming → Rust systems programming → Micro-OS**

---

# 30. Final Student Checklist

Before submission:

- [ ] I reproduced the failure.
- [ ] I identified the relevant OS concept.
- [ ] I distinguished symptom from root cause.
- [ ] I created an appropriate system model.
- [ ] I analyzed alternative solutions.
- [ ] I selected and justified a solution.
- [ ] I implemented the correction/design.
- [ ] I tested the original failure.
- [ ] I tested normal and edge cases.
- [ ] I performed regression testing.
- [ ] I considered performance and trade-offs.
- [ ] I documented the programming language and version.
- [ ] I documented the Linux environment where applicable.
- [ ] I disclosed AI assistance.
- [ ] I independently verified AI-generated suggestions.
- [ ] I can explain every important design decision.

---

# 31. Core Philosophy of CA-3

The central philosophy of the OS Design & Debugging Challenge is:

> **Do not merely fix the code. Understand the system failure, identify its root cause, compare possible solutions, implement the most appropriate mechanism, and prove that your solution works.**

Students should gradually develop the habit of asking:

> **What failed?**

↓

> **Why did it fail?**

↓

> **Which OS principle explains the failure?**

↓

> **What are my possible designs?**

↓

> **Which design is appropriate under these constraints?**

↓

> **Can I implement it correctly?**

↓

> **Can I prove that it works?**

↓

> **What trade-offs did my solution introduce?**

The intended outcome is the development of students who can **diagnose, design, implement and defend operating-system mechanisms**, preparing them for increasingly complex systems engineering tasks and ultimately for the **Rust Micro-OS Engineering Project**.
