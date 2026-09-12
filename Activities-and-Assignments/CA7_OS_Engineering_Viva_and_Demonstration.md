# CA-7 – OS Engineering Viva & Demonstration
## Continuous Assessment – 5 Marks

### Course
**Operating Systems**

### Assessment Position
**CA-7 of 7 | 5 Marks**

---

# 1. Purpose

CA-7 is the **culminating assessment** of the Operating Systems Continuous Assessment framework.

It validates whether students can independently:

- demonstrate their work;
- explain the underlying OS concepts;
- interpret evidence;
- justify engineering decisions;
- diagnose unexpected behaviour;
- respond to modifications;
- defend individual contributions;
- identify limitations and future improvements.

The central question is:

> **Can the student demonstrate, explain, justify, critique and defend the OS engineering work developed throughout the course?**

CA-7 should therefore be an **evidence-based engineering viva**, not simply a recall-based oral examination.

---

# 2. Position in the CA Progression

| CA | Focus | Student Capability |
|---|---|---|
| CA-1 | Systems Thinking | Think |
| CA-2 | Performance Investigation | Measure |
| CA-3 | Design & Debugging | Engineer |
| CA-4 | Research Mini-Project | Investigate |
| CA-5 | Linux Systems Engineering | Observe |
| CA-6 | Rust Micro-OS | Build |
| **CA-7** | **Viva & Demonstration** | **Defend** |

The complete learning journey is:

> **Think → Measure → Engineer → Investigate → Observe → Build → Defend**

---

# 3. Core Philosophy

A conventional viva often asks:

> “What is a process?”

CA-7 should instead ask:

> “Show me how your program creates or observes a process. What state does it enter? How did you verify that? What would happen if the parent terminates first?”

The preferred progression is:

> **Demonstrate → Explain → Modify → Break → Diagnose → Justify → Extend**

This allows the faculty to distinguish:

- genuine understanding;
- memorized answers;
- copied code;
- AI-generated work;
- superficial project participation;
- independent engineering capability.

---

# 4. Learning Outcomes

After CA-7, students should be able to:

- communicate OS concepts clearly;
- demonstrate working systems artifacts;
- explain implementation choices;
- reason about OS behaviour;
- interpret experimental evidence;
- diagnose failures;
- justify trade-offs;
- defend research conclusions;
- explain Linux observations;
- explain Rust Micro-OS mechanisms;
- identify limitations;
- propose technically meaningful extensions.

---

# 5. Assessment Format

### Recommended Duration

**8–12 minutes per student** for individual defence.

For team projects, the team may initially demonstrate together, followed by **individual questioning**.

### Recommended Structure

| Phase | Approx. Time | Purpose |
|---|---:|---|
| Demonstration | 2 min | Show working artifact |
| Explanation | 2 min | Explain mechanism |
| Technical questioning | 3–4 min | Test understanding |
| Challenge/diagnosis | 2 min | Test reasoning |
| Defence/future extension | 1–2 min | Test engineering judgement |

Faculty may adapt timing based on class size.

---

# 6. Adaptive Viva Model

The viva should not use exactly the same questions for every student.

Instead:

## Level 1 – Demonstrate

> “Show me that the mechanism works.”

## Level 2 – Explain

> “Explain what is happening internally.”

## Level 3 – Modify

> “Change this parameter/design choice. What do you expect?”

## Level 4 – Break

> “Suppose this component fails. What happens?”

## Level 5 – Diagnose

> “Why might this result occur?”

## Level 6 – Justify

> “Why did you select this approach instead of an alternative?”

## Level 7 – Extend

> “How would you improve this system?”

The faculty should stop escalating once sufficient evidence of the student's level is obtained.

---

# 7. Five-Mark Structure

| Component | Marks |
|---|---:|
| Technical demonstration | 1 |
| Conceptual understanding | 1 |
| Engineering reasoning and trade-offs | 1 |
| Debugging / scenario-based questioning | 1 |
| Communication, individual contribution and defence | 1 |
| **Total** | **5** |

---

# 8. Technical Demonstration – 1 Mark

The student should demonstrate at least one artifact from the CA portfolio.

Possible artifacts:

- CA-1 reasoning response;
- CA-2 performance experiment;
- CA-3 debugging challenge;
- CA-4 research experiment;
- CA-5 Linux engineering task;
- CA-6 Rust Micro-OS.

### Full-mark evidence

Student demonstrates the artifact and explains what is being observed.

### Partial evidence

Artifact runs but student cannot explain the underlying mechanism.

---

# 9. Conceptual Understanding – 1 Mark

Faculty evaluates whether the student can connect implementation to OS theory.

Examples:

- process → PCB/state;
- scheduling → ready queue;
- synchronization → critical section;
- deadlock → resource allocation;
- memory → virtual/physical abstraction;
- file system → metadata/storage;
- Linux → kernel interface;
- Rust → systems-level implementation.

---

# 10. Engineering Reasoning – 1 Mark

The student should justify decisions such as:

- Why Round Robin?
- Why this time quantum?
- Why this synchronization mechanism?
- Why this memory allocator?
- Why Python rather than Rust for this experiment?
- Why Rust rather than Python for the Micro-OS?
- Why use Linux `/proc`?
- Why use QEMU?
- Why this experimental workload?

Full marks require **reasoned trade-offs**, not simply:

> “Because the teacher told us.”

---

# 11. Debugging / Scenario-Based Questioning – 1 Mark

Faculty introduces a controlled hypothetical or actual modification.

Examples:

> “Your scheduler is starving Task 3. What would you inspect?”

> “The allocator fails after repeated allocations. What could be happening?”

> “Two tasks produce inconsistent results. Where would you look?”

> “Your Linux process consumes unexpectedly high CPU. How would you investigate?”

> “The Micro-OS boots but never schedules the second task. What are your debugging steps?”

The student should reason rather than guess.

---

# 12. Communication and Defence – 1 Mark

Evaluate:

- clarity;
- confidence;
- technical vocabulary;
- logical explanation;
- individual contribution;
- ability to answer follow-up questions;
- ability to acknowledge limitations.

A student should receive credit for saying:

> “I do not know the exact cause, but I would investigate it in this order…”

rather than inventing an answer.

---

# 13. CO-Based Viva Question Bank

## CO1 – OS Fundamentals

### Basic

1. What is the role of an operating system?
2. What are the major OS services?
3. Why does an OS need resource management?
4. What is the difference between kernel and user space?
5. What is a system call?

### Application

6. Which OS service does your project use?
7. Which resource is most important in your experiment?
8. What abstraction does the OS provide for that resource?

### Advanced

9. What would happen if the OS did not provide this abstraction?
10. Which OS design decision has the greatest effect on your project?

---

# 14. CO2 – Processes, Threads and Scheduling

### Basic

1. What is a process?
2. What is a thread?
3. What is a context switch?
4. What is the ready queue?
5. Explain Round Robin.

### Application

6. How did your workload affect scheduling?
7. Why does time quantum matter?
8. What did Linux show in your scheduling experiment?

### Advanced

9. How would you detect starvation?
10. How would you balance fairness and throughput?
11. What happens when the number of runnable tasks increases?
12. How would you modify your Micro-OS scheduler for priority scheduling?

---

# 15. CO3 – Synchronization and Deadlocks

### Basic

1. What is a critical section?
2. What is a race condition?
3. What is mutual exclusion?
4. What is a deadlock?
5. What are the necessary conditions for deadlock?

### Application

6. Where is synchronization used in your project?
7. What happens without the lock?
8. How did you verify correctness?

### Advanced

9. How could your synchronization mechanism cause starvation?
10. What is the difference between deadlock prevention and avoidance?
11. How would you diagnose a concurrency bug that occurs only occasionally?
12. What would happen if two kernel tasks acquired locks in different orders?

---

# 16. CO4 – Memory Management

### Basic

1. What is virtual memory?
2. What is paging?
3. What is a page fault?
4. What is fragmentation?
5. What is an allocator?

### Application

6. How does your allocator work?
7. Why did you select your allocation strategy?
8. What happens when memory is exhausted?

### Advanced

9. How would fragmentation affect your allocator?
10. How could paging be added to your Micro-OS?
11. How would you detect memory leaks?
12. What is the relationship between virtual and physical addresses?

---

# 17. CO5 – File Systems, Disk and I/O

### Basic

1. What is a file system?
2. What is file metadata?
3. What is disk scheduling?
4. What is I/O buffering?
5. Why is sequential I/O usually different from random I/O?

### Application

6. What did your Linux I/O experiment demonstrate?
7. Why did access pattern affect performance?
8. What Linux tool did you use and why?

### Advanced

9. How would you design a minimal file system?
10. How would you handle an I/O failure?
11. How does caching change observed performance?

---

# 18. CO6 – Linux and OS-Based Programming

### Basic

1. Why was Linux selected for CA-5?
2. What is `/proc`?
3. What does `ps` show?
4. What is CPU affinity?
5. What does `nice` do conceptually?

### Application

6. Which Linux tool gave you the most useful evidence?
7. How did Python interact with Linux?
8. What did you automate?

### Advanced

9. What is the relationship between a Python OS API and the underlying kernel?
10. How would you investigate an unknown performance problem on Linux?
11. Why is Rust appropriate for low-level OS programming?
12. What limitations does your Micro-OS have compared with Linux?

---

# 19. CA-1 Evidence-Based Questions

The student selects or is shown a CA-1 scenario.

### Questions

1. What OS concept did you identify?
2. What assumptions did you make?
3. What alternatives did you consider?
4. Why did you select your solution?
5. What evidence would change your decision?
6. How could AI help corroborate your reasoning?
7. Which AI-generated claim would you verify?

### Challenge

> “Give me a different solution and explain why you rejected it.”

---

# 20. CA-2 Performance Questions

1. What was your hypothesis?
2. What was your independent variable?
3. What was your dependent variable?
4. Which variables were controlled?
5. How many repetitions did you perform?
6. Why did you choose those metrics?
7. What was the biggest source of experimental noise?
8. Did the results support your hypothesis?
9. If not, what did you learn?
10. How would you improve the experiment?

### Challenge

> “Suppose your result changes on another machine. What could explain the difference?”

---

# 21. CA-3 Design & Debugging Questions

1. What was the original failure?
2. How did you reproduce it?
3. What was the root cause?
4. Which alternative fixes did you consider?
5. Why did you select your fix?
6. How did you validate it?
7. What regression could your fix introduce?
8. What test case was most important?

### Challenge

> “I have removed one assumption from your design. Does your solution still work?”

---

# 22. CA-4 Research Questions

1. What was your research question?
2. What was the research gap?
3. Which paper influenced your methodology?
4. What was your hypothesis?
5. What did the evidence show?
6. What result surprised you?
7. What are the threats to validity?
8. What would you investigate next?

### Challenge

> “Your experiment contradicts the literature. What would you do?”

---

# 23. CA-5 Linux Questions

1. What did you observe on Linux?
2. Which Linux interface/tool did you use?
3. What did `/proc` reveal?
4. How did you establish a baseline?
5. What engineering intervention did you perform?
6. How did you validate the intervention?
7. What would happen under a different workload?
8. Which observation could not be explained by your initial hypothesis?

### Challenge

> “Your process suddenly consumes more CPU. Give me your investigation sequence.”

---

# 24. CA-6 Micro-OS Questions

1. Show the boot process.
2. Where does kernel execution begin?
3. How is a task represented?
4. Show the ready queue.
5. Show the scheduler.
6. What causes a scheduling decision?
7. Explain your timer mechanism.
8. Show your synchronization mechanism.
9. Explain your allocator.
10. Where is `unsafe` Rust used?
11. Why is that `unsafe` code necessary?
12. What invariant makes it safe?
13. What happens when allocation fails?
14. How does a task terminate?
15. What would you implement next?

---

# 25. Demonstration Scenarios

Faculty may choose one scenario instead of asking many disconnected questions.

## Scenario A – Scheduler

> “You have three tasks. Demonstrate their scheduling order. Now change the scheduling parameter. Explain the difference.”

## Scenario B – Synchronization

> “Remove/disable the protection mechanism in a controlled test. Demonstrate the failure and explain the correction.”

## Scenario C – Memory

> “Perform repeated allocations. Explain what happens as available memory becomes constrained.”

## Scenario D – Linux

> “Start a workload. Use Linux tools to identify its resource behaviour and recommend an intervention.”

## Scenario E – Research

> “Show one result from CA-4 and defend the conclusion.”

## Scenario F – Micro-OS

> “Trace one task from creation through scheduling to termination.”

---

# 26. “Break My System” Viva

For stronger students, faculty may use a controlled **Break–Diagnose–Repair** sequence.

### Step 1
Demonstrate the working system.

### Step 2
Faculty changes one parameter or introduces a safe fault.

### Step 3
Student predicts the effect.

### Step 4
Student identifies evidence to inspect.

### Step 5
Student explains likely root cause.

### Step 6
Student proposes a correction.

### Step 7
Student explains how the correction would be validated.

This strongly tests genuine understanding.

---

# 27. AI-Related Viva Questions

Because AI may be used throughout the course, CA-7 should explicitly evaluate responsible AI usage.

Possible questions:

1. Where did you use Generative AI?
2. What did AI help you with?
3. What did you independently verify?
4. Did AI ever give you an incorrect answer?
5. How did you detect the error?
6. Why should AI-generated Rust kernel code be treated cautiously?
7. How did you validate AI-generated Linux commands?
8. Which parts of the project are entirely your own?
9. How did AI influence your research question?
10. Can you explain this code without AI assistance?

### Important principle

> **AI assistance should improve the student's capability, not replace the student's understanding.**

---

# 28. Individual Contribution Verification

For team projects, faculty should randomly assign questions.

For example:

> “Your team implemented the scheduler. You implemented memory. Explain the scheduler.”

The student should have **working awareness of the complete architecture**, while being especially strong in their assigned subsystem.

### Suggested individual evidence

Each student should maintain:

- contribution log;
- Git commits where available;
- subsystem documentation;
- debugging entries;
- experiment contributions.

---

# 29. Viva Question Selection Matrix

Faculty can select approximately:

| Category | Questions |
|---|---:|
| Conceptual | 2 |
| Project-specific | 2 |
| Evidence/analysis | 1 |
| Scenario/debugging | 1 |
| Extension/trade-off | 1 |
| Individual contribution | 1 |

This produces a compact but meaningful viva.

---

# 30. Difficulty Progression

### Level 1 – Recall

“What is a process?”

### Level 2 – Explain

“Explain what happens when a process changes state.”

### Level 3 – Apply

“Show how your program creates a process.”

### Level 4 – Analyze

“Why did the performance change?”

### Level 5 – Evaluate

“Why is your approach better under this workload?”

### Level 6 – Design

“How would you redesign it for a different workload?”

CA-7 should emphasize **Levels 3–6**.

---

# 31. 5-Mark Rubric

| Criterion | Excellent | Good | Developing | Needs Improvement |
|---|---|---|---|---|
| Demonstration | Correct and clearly explained | Works with minor gaps | Limited demonstration | Cannot demonstrate |
| Understanding | Deep conceptual understanding | Sound understanding | Partial | Memorized/unclear |
| Engineering reasoning | Strong trade-off analysis | Reasonable justification | Basic justification | No justification |
| Debugging/scenario | Systematic diagnosis | Mostly correct | Trial-and-error | Cannot reason |
| Communication/defence | Clear, independent and technically confident | Generally clear | Some dependence | Unable to defend |

---

# 32. Performance-Level Interpretation

### 5 Marks – Outstanding

Student independently demonstrates, explains, diagnoses and defends technical decisions.

### 4 Marks – Proficient

Student demonstrates strong understanding with minor gaps.

### 3 Marks – Competent

Student understands the major concepts but struggles with deeper reasoning.

### 2 Marks – Developing

Student can describe the project but cannot reliably defend design decisions.

### 1 Mark – Beginning

Student demonstrates limited understanding or relies heavily on memorized/project-generated responses.

### 0 Marks

No meaningful demonstration or evidence of individual understanding.

---

# 33. CO Alignment

| Viva Focus | CO |
|---|---|
| OS architecture/fundamentals | CO1 |
| Process/scheduling questions | CO2 |
| Synchronization/deadlock | CO3 |
| Memory management | CO4 |
| File/I/O | CO5 |
| Linux programming and Micro-OS | CO6 |

CA-7 therefore provides **integrative evidence across all six COs**.

---

# 34. Institutional Philosophy Alignment

## Primary Dimension: Critical Thinking

CA-7 strongly develops:

- reasoned arguments;
- evaluation of evidence;
- questioning assumptions;
- technical decision-making;
- diagnosis of unexpected behaviour;
- defence of alternative solutions.

### Critical Thinking Mapping

| LO | CA-7 Evidence |
|---|---|
| LO1 – Challenge existing knowledge | Defend design alternatives |
| LO2 – Systematic observation | Evidence-based demonstration |
| LO3 – Evaluate multiple sources | Research/literature defence |
| LO4 – Reasoned arguments + AI corroboration | AI verification questions |
| LO5 – Perceive objects/knowledge | System observation |
| LO6 – Raise doubts on status quo | “What would you change?” questions |

---

# 35. Secondary Dimension: Innovation & Professional Development

Students demonstrate:

- project ownership;
- professional communication;
- engineering judgement;
- independent problem solving;
- emerging-tool awareness.

---

# 36. Secondary Dimension: Research Experience

Students defend:

- research questions;
- experimental methodology;
- evidence;
- limitations;
- future work.

---

# 37. Real World Exposure

CA-7 develops professional abilities to:

- explain technical systems to others;
- defend engineering decisions;
- respond to unexpected questions;
- communicate limitations honestly;
- collaborate while demonstrating individual accountability.

---

# 38. CA-7 Philosophy Matrix

| Activity | Critical Thinking | Innovation & Professional Development | Research Experience | Real World Exposure |
|---|---:|---:|---:|---:|
| Technical demonstration | High | **High** | Moderate | **High** |
| Conceptual defence | **High** | High | Moderate | High |
| Evidence interpretation | **High** | High | **High** | High |
| Debugging challenge | **High** | **High** | High | **High** |
| Trade-off analysis | **High** | **High** | High | **High** |
| AI verification | **High** | High | **High** | High |
| Future design | **High** | **High** | **High** | High |

---

# 39. PO/PSO Contribution

### PO1 – Engineering Knowledge
Demonstrates integrated OS knowledge.

### PO2 – Problem Analysis
Explains diagnosis and analytical reasoning.

### PO3 – Design/Development
Defends engineering solutions.

### PO4 – Conduct Investigations
Interprets experimental evidence.

### PO5 – Engineering Tool Usage
Explains Linux, Python, Rust and development tools.

### PO6 – Engineer and World
Connects engineering decisions to real systems.

### PO7 – Ethics
Tests responsible AI use, research integrity and honest reporting.

### PO8 – Teamwork
Verifies individual contribution within teams.

### PO9 – Communication
**Strongest alignment:** technical oral communication and defence.

### PO10 – Project Management
Demonstrates ownership of project decisions and milestones.

### PO11 – Lifelong Learning
Tests independent understanding and future learning directions.

### PSO1
Defends software/system design solutions.

### PSO2
Demonstrates modern systems-tool usage.

### PSO3
Connects OS infrastructure to AI/ML workload and systems requirements.

---

# 40. Complete 70-Mark CA Architecture

The seven assessments now form a coherent 70-mark continuous assessment model.

| CA | Assessment | Marks | Core Capability |
|---|---|---:|---|
| CA-1 | Systems Thinking Challenge | 10 | Think |
| CA-2 | OS Performance Investigation | 10 | Measure |
| CA-3 | OS Design & Debugging Challenge | 10 | Engineer |
| CA-4 | OS Research Mini-Project | 10 | Investigate |
| CA-5 | Linux Systems Engineering Challenge | 10 | Observe |
| CA-6 | Rust Micro-OS Engineering Project | 15 | Build |
| CA-7 | OS Engineering Viva & Demonstration | 5 | Defend |
| **Total** | | **70** | |

---

# 41. Complete Learning Journey

```text
                  OPERATING SYSTEMS
                         │
                         ▼
              CA-1: SYSTEMS THINKING
                    “What is it?”
                         │
                         ▼
             CA-2: PERFORMANCE
                 “What happens?”
                         │
                         ▼
              CA-3: ENGINEERING
                 “Why did it fail?”
                         │
                         ▼
               CA-4: RESEARCH
                “What can I learn?”
                         │
                         ▼
                CA-5: LINUX
                “Can I observe it?”
                         │
                         ▼
               CA-6: RUST MICRO-OS
                “Can I build it?”
                         │
                         ▼
               CA-7: VIVA
               “Can I defend it?”
```

---

# 42. Evidence Continuity Across All CAs

| CA | Primary Evidence |
|---|---|
| CA-1 | Reasoning/decision record |
| CA-2 | Experimental data |
| CA-3 | Before/after debugging evidence |
| CA-4 | Research report |
| CA-5 | Linux system evidence |
| CA-6 | Running Micro-OS + source |
| CA-7 | Individual technical defence |

This creates a **portfolio-based evidence trail** across the course.

---

# 43. Faculty Viva Record Sheet

### Student
____________________________

### Team
____________________________

### Selected Artifact
____________________________

### CO Focus
____________________________

### Questions

| No. | Category | Question | Performance |
|---:|---|---|---|
| 1 | Concept | | |
| 2 | Project | | |
| 3 | Evidence | | |
| 4 | Debugging | | |
| 5 | Trade-off | | |
| 6 | Individual contribution | | |
| 7 | Extension | | |

### Marks

| Component | Marks |
|---|---:|
| Demonstration | /1 |
| Conceptual understanding | /1 |
| Engineering reasoning | /1 |
| Debugging/scenario | /1 |
| Communication/defence | /1 |
| **Total** | **/5** |

---

# 44. Faculty Moderation Guidelines

To maintain fairness:

- use a common question bank;
- maintain comparable difficulty;
- ask at least one scenario-based question;
- ask individual rather than only team questions;
- evaluate reasoning rather than fluency alone;
- allow students to acknowledge uncertainty;
- avoid rewarding memorized textbook definitions alone;
- record evidence supporting unusually high/low marks.

For large classes, faculty may prepare a **question pool mapped by CO and difficulty level** and randomly select questions.

---

# 45. Recommended CA-7 Student Preparation

Students should bring/prepare:

- one representative artifact from CA-1–CA-6;
- source code where applicable;
- experimental results;
- architecture diagram;
- key design decisions;
- major debugging issue;
- one limitation;
- one future extension;
- AI-use disclosure.

The student should be able to explain the complete journey:

> **Problem → Experiment → Design → Research → Linux → Rust → Result**

---

# 46. Final Viva Challenge

For high-performing students, conclude with:

> **“If you had another four weeks, what would you improve, why would you improve it, and how would you prove that your improvement is better?”**

A strong answer should contain:

**Problem → Proposed change → Hypothesis → Metric → Experiment → Expected evidence**

This turns the final question into a miniature engineering/research proposal.

---

# 47. Overall Educational Significance

CA-7 completes the transformation of the Operating Systems course from a collection of programming exercises into a **progressive systems-engineering experience**.

Students have:

- reasoned about OS problems;
- measured OS behaviour;
- debugged and redesigned mechanisms;
- investigated research questions;
- worked with Linux;
- implemented low-level mechanisms in Rust;
- built a Micro-OS;
- and finally defended their work.

The final competency is therefore not:

> **“Can the student remember Operating Systems concepts?”**

but:

> **“Can the student understand, investigate, implement, evaluate and defend Operating Systems mechanisms?”**

That is the intended culmination of the 70-mark CA framework.

---

# 48. One-Line CA-7 Definition

> **CA-7 requires students to demonstrate, explain, diagnose, justify and defend their Operating Systems learning and engineering work through an adaptive, evidence-based individual viva and technical demonstration.**
