# CA-4 – OS Research Mini-Project
## Continuous Assessment – 10 Marks

### Course
**Operating Systems**

### Assessment Position
**CA-4 of 7 | 10 Marks**

---

## 1. Purpose

CA-4 moves students from structured problem solving and controlled performance experiments toward **small-scale, evidence-based research in Operating Systems**.

The progression across the continuous assessments is:

| Assessment | Central Question | Student Capability |
|---|---|---|
| CA-1 – Systems Thinking Challenge | What is the OS problem? | Identify, model, reason and justify |
| CA-2 – Performance Investigation | What does experimental evidence show? | Measure, compare and interpret |
| CA-3 – Design & Debugging Challenge | Can I diagnose and improve it? | Design, implement, debug and validate |
| **CA-4 – Research Mini-Project** | **What is not yet completely answered?** | **Investigate, generate evidence and propose insight** |
| CA-5 – Linux Systems Engineering Challenge | How does the real OS behave? | Apply OS concepts on Linux |
| CA-6 – Rust Micro-OS Engineering Project | Can I implement OS mechanisms? | Build low-level OS components |
| CA-7 – Viva & Demonstration | Can I defend my engineering decisions? | Communicate and defend |

The intent is **not** to turn CA-4 into a generic software mini-project. Every project must contain a **researchable question, measurable variables, evidence, analysis and a defensible conclusion**.

---

# 2. Research Philosophy

Students should experience the basic research cycle:

**Observe → Question → Review → Hypothesize → Design → Experiment → Measure → Analyze → Conclude → Propose**

A successful CA-4 project therefore answers:

1. What OS phenomenon/problem is being investigated?
2. What does existing literature say?
3. What gap, uncertainty, comparison or limitation remains?
4. What research question is being asked?
5. What hypothesis or expectation is being tested?
6. How will evidence be collected?
7. What does the evidence show?
8. What engineering conclusion follows?

Research topics can be inspired by contemporary OS research areas such as scheduling, memory management, virtualization, resource management and systems performance. These are also active themes in university OS research. citeturn0search0turn0search2

---

# 3. Learning Outcomes for CA-4

After completing CA-4, students should be able to:

- formulate a focused OS research problem;
- discover and critically review relevant literature;
- distinguish a topic from a research problem;
- formulate research questions and hypotheses;
- select suitable experimental variables and evaluation metrics;
- design a reproducible OS experiment;
- implement a prototype/simulator using an appropriate language;
- collect, visualize and analyze evidence;
- identify limitations and threats to validity;
- communicate findings using a concise technical research report;
- use Generative AI as a research assistant while independently validating its output.

---

# 4. Recommended Research Ladder

Students should not all be expected to produce novel algorithms. Research maturity can be developed progressively.

| Level | Research Activity | Expected Output |
|---|---|---|
| **Level 1 – Reproduce** | Reproduce a known experiment or result | Verify whether a reported observation can be reproduced |
| **Level 2 – Compare** | Compare two or more mechanisms under controlled conditions | Evidence-based comparison |
| **Level 3 – Extend** | Modify workload, parameters, environment or mechanism | New experimental evidence |
| **Level 4 – Propose** | Introduce a small optimization/design idea | Prototype + comparison + justification |

**Recommended expectation for undergraduate CA-4:** Levels 1–3 for most students; Level 4 for strong teams.

---

# 5. Project Structure

Each team/student should complete the following stages.

### Stage 1 – Problem Identification
Identify a specific OS phenomenon rather than a broad topic.

**Weak:** “Study CPU scheduling.”

**Better:** “Investigate how Round Robin time quantum affects response time and context-switch overhead under mixed CPU/I/O workloads.”

### Stage 2 – Literature Discovery
Find relevant textbooks, research papers, technical documentation and credible system references.

### Stage 3 – Research Gap
Identify one of the following:

- unexplored comparison;
- different workload;
- different parameter range;
- conflicting observations;
- limitation of an existing approach;
- implementation limitation;
- opportunity for optimization;
- applicability to a new scenario.

### Stage 4 – Research Question
Frame one primary question and optionally 1–2 secondary questions.

Example:

> How does increasing the Round Robin time quantum affect response time, waiting time and context-switch overhead under CPU-intensive and I/O-intensive workloads?

### Stage 5 – Hypothesis
State an experimentally testable expectation.

Example:

> Increasing the time quantum will reduce context-switch overhead but may increase response time for interactive workloads.

### Stage 6 – Methodology
Specify:

- independent variables;
- dependent variables;
- control variables;
- workload;
- environment;
- repetitions;
- measurement method;
- statistical/visual analysis.

### Stage 7 – Prototype / Experiment
Implement the required simulator, benchmark or Linux experiment.

### Stage 8 – Results
Present tables, plots and observations.

### Stage 9 – Interpretation
Explain **why** the results occurred using OS concepts.

### Stage 10 – Conclusion
Answer the research question and state limitations/future work.

---

# 6. Programming Language Policy

CA-4 deliberately continues the language progression established in CA-1–CA-3.

| Research Activity | Required / Preferred Language |
|---|---|
| OS algorithm simulation | **Python 3.x** |
| Scheduling simulation | **Python 3.x** |
| Deadlock algorithms | **Python 3.x** |
| Memory/page replacement simulation | **Python 3.x** |
| Disk scheduling | **Python 3.x** |
| Data analysis/visualization | **Python 3.x** |
| Linux process/system investigation | **Python + Bash/Linux** |
| Linux performance monitoring | **Python + Bash/Linux** |
| Thread/concurrency experiment | **Python; Rust encouraged** |
| Systems-performance comparison | **Python + Rust** |
| Low-level systems experiment | **Rust preferred** |
| Kernel/OS mechanism prototype | **Rust preferred** |
| Micro-OS-related research | **Rust** |
| Research report | Any suitable tool; Python recommended for plots |

### Important principle

**Python is the default research language, not the only language.**

Python should be used where the research question concerns algorithms, modelling, simulation, experimentation or data analysis. Rust should be introduced where implementation-level systems behaviour, concurrency, memory safety or low-level OS mechanisms are central.

This creates a coherent progression:

**Python Simulation → Python/Linux Experiment → Rust Systems Experiment → Rust Micro-OS**

---

# 7. Research Topic Bank

## A. CPU Scheduling

### R1. Scheduling under Different Workloads
**Question:** How do FCFS, SJF, Priority and Round Robin behave under CPU-bound, I/O-bound and mixed workloads?

**Language:** Python 3.x

**Metrics:** waiting time, turnaround time, response time, throughput, fairness.

---

### R2. Round Robin Time Quantum Optimization
**Question:** What time quantum provides a suitable balance between responsiveness and scheduling overhead?

**Language:** Python 3.x

**Metrics:** response time, waiting time, context switches, throughput.

---

### R3. Fairness vs Throughput
**Question:** Does maximizing throughput necessarily produce fair CPU allocation?

**Language:** Python 3.x

**Metrics:** throughput, CPU utilization, waiting-time variance, fairness index.

---

### R4. Workload-Aware Scheduling
**Question:** Can workload characteristics be used to select a more suitable scheduling strategy?

**Language:** Python 3.x; Rust optional.

---

### R5. Multi-Core Scheduling
**Question:** How does processor affinity or workload distribution influence execution performance?

**Language:** Python + Linux; Rust extension recommended.

---

## B. Processes and Threads

### R6. Process vs Thread Creation

**Question:** Under what workloads is thread-based execution more efficient than process-based execution?

**Language:** Python + Linux; Rust recommended for an implementation-level comparison.

**Metrics:** creation overhead, execution time, memory footprint, scalability.

---

### R7. Thread Scalability

**Question:** How does increasing the number of concurrent threads affect application throughput?

**Language:** Python; Rust preferred for stronger systems-level investigation.

---

### R8. Context-Switch Overhead

**Question:** How does increasing process/thread concurrency affect context-switch overhead?

**Language:** Python + Linux; Rust optional.

---

## C. Synchronization and Concurrency

### R9. Synchronization Contention

**Question:** How does lock contention affect application throughput as the number of concurrent workers increases?

**Language:** Python; Rust preferred.

**Metrics:** throughput, execution time, waiting time, scalability.

---

### R10. Producer–Consumer Performance

**Question:** How do buffer size and producer/consumer ratios influence throughput?

**Language:** Python; Rust extension recommended.

---

### R11. Mutex vs Alternative Synchronization Strategies

**Question:** Under what workload conditions does one synchronization strategy outperform another?

**Language:** Rust preferred.

---

### R12. Race Condition Investigation

**Question:** How does uncontrolled concurrent access affect correctness and reproducibility?

**Language:** Python or Rust.

**Expected output:** Demonstration of race condition + controlled synchronization + evidence of correction.

---

## D. Deadlocks

### R13. Deadlock Detection under Different Resource Patterns

**Language:** Python 3.x

**Variables:** number of processes, resource types, allocation patterns.

---

### R14. Deadlock Avoidance vs Detection

**Question:** What are the performance trade-offs between avoidance and detection strategies?

**Language:** Python 3.x

---

### R15. Safe-State Analysis

**Question:** How does resource demand variability affect the probability of reaching an unsafe state?

**Language:** Python 3.x

---

## E. Memory Management

### R16. Memory Allocation Strategy Comparison

Compare first-fit, best-fit and worst-fit.

**Language:** Python 3.x

**Metrics:** internal/external fragmentation, allocation success, search cost.

---

### R17. Page Replacement under Locality

Compare FIFO, LRU and Optimal under different locality patterns.

**Language:** Python 3.x

---

### R18. Working Set and Thrashing

**Question:** How does increasing the working-set size influence page-fault behaviour?

**Language:** Python 3.x

---

### R19. Page Replacement for AI/ML-Like Access Patterns

**Question:** How do sequential, random and bursty memory-access patterns influence replacement performance?

**Language:** Python 3.x

**Extension:** Generate synthetic matrix/tensor-style access patterns.

---

## F. File Systems and Storage

### R20. Disk Scheduling Comparison

Compare FCFS, SSTF, SCAN, C-SCAN and related strategies.

**Language:** Python 3.x

**Metrics:** seek distance, response time, fairness.

---

### R21. Storage Workload Characterization

**Question:** How do sequential and random access patterns influence storage performance?

**Language:** Python + Linux.

---

### R22. File Operation Performance

Investigate read/write performance for different file sizes and access patterns.

**Language:** Python + Linux; Rust optional.

---

## G. Linux Systems Research

### R23. CPU Affinity

**Question:** How does binding workloads to selected CPU cores influence performance?

**Language:** Python + Linux; Rust optional.

---

### R24. Process Resource Usage

Investigate CPU and memory behaviour of different workload classes.

**Language:** Python + Linux.

---

### R25. Lightweight System Monitor

Develop a research prototype that monitors CPU, memory, process and I/O behaviour.

**Language:** Python + Linux.

**Research component:** Determine which metrics best distinguish workload classes.

---

### R26. Containers vs Processes

**Question:** What performance and isolation differences can be observed between ordinary processes and containerized workloads?

**Language:** Python + Linux; Bash; optional Rust component.

---

# 8. Advanced Research Topics

These should be offered to high-performing teams.

### R27. Python vs Rust Concurrency
Measure execution behaviour under increasing concurrency.

**Language:** Python + Rust

### R28. Rust Memory Safety for Systems Programming
Investigate whether selected classes of memory errors can be prevented or eliminated through Rust's ownership and borrowing model.

**Language:** Rust

### R29. Energy-Aware Scheduling
Study the relationship between workload scheduling and energy-related performance indicators where measurement facilities are available.

**Language:** Python + Linux

### R30. OS Support for AI/ML Workloads
Investigate scheduling, memory or I/O behaviour for representative AI/ML-inspired workloads.

**Language:** Python + Linux; Rust optional.

### R31. Lightweight Virtualization
Compare selected resource and performance characteristics of isolated workloads.

**Language:** Python + Linux/Bash.

### R32. OS-Level Security and Isolation
Investigate how OS mechanisms contribute to process/resource isolation.

**Language:** Python + Linux; Rust optional.

---

# 9. Suggested Research Questions

Students may select or adapt questions such as:

1. Which scheduling policy performs best for mixed workloads?
2. What is the effect of Round Robin time quantum on fairness and responsiveness?
3. When does additional concurrency stop improving throughput?
4. How does lock contention scale with the number of threads?
5. Which page replacement policy performs best under strong locality?
6. Can a workload-aware strategy outperform a fixed strategy?
7. How does CPU affinity affect application performance?
8. What is the trade-off between fairness and throughput?
9. How does memory fragmentation change with allocation strategy?
10. Can a lightweight OS monitoring tool reliably distinguish workload types?
11. How does Rust compare with Python for selected concurrent systems workloads?
12. Which OS mechanisms are most relevant to AI/ML workload performance?

---

# 10. Variables and Experimental Design

Every project must explicitly classify:

| Variable Type | Example |
|---|---|
| Independent | Time quantum |
| Dependent | Response time |
| Control | Workload size |
| Environmental | CPU/core count |
| Repetition | 5–10 runs |
| Baseline | Default configuration |

Students should avoid changing multiple uncontrolled variables simultaneously.

### Recommended experiment structure

**Baseline → Parameter Variation → Repeated Runs → Aggregate → Compare → Explain**

---

# 11. Reproducibility Requirements

Each project must document:

- operating system;
- Python/Rust version;
- hardware configuration where relevant;
- libraries/tools;
- source-code version;
- input/workload generation method;
- experimental parameters;
- number of repetitions;
- measurement method;
- random seed where applicable.

A research result that cannot be reproduced should be treated cautiously.

---

# 12. AI-Assisted Literature Review Protocol

Generative AI may be used as a **research assistant**, but not as a replacement for scholarly verification.

### Allowed Uses

Students may use AI to:

- identify keywords;
- generate search strategies;
- explain unfamiliar terminology;
- summarize papers after obtaining the original source;
- compare concepts;
- suggest hypotheses;
- critique an experimental design;
- generate starter code;
- suggest visualization techniques;
- identify potential limitations.

### Verification Rule

Students must independently verify:

**Paper → Claim → Evidence → Interpretation**

AI-generated references must **not** be accepted without checking the original publication.

### Required AI Disclosure

The report should include a short statement:

> “Generative AI was used for literature discovery, conceptual clarification, experimental brainstorming and/or code assistance. All cited sources, experimental results and technical claims were independently verified by the authors.”

If AI was not used, students should state that explicitly.

---

# 13. Literature Review Minimum Requirement

Each project should use:

- **3–5 credible references** for a basic project;
- at least **2 research papers** where available;
- relevant textbook/technical documentation;
- recent literature where the topic is contemporary.

The literature review should answer:

1. What is already known?
2. What methods have been used?
3. What metrics are commonly evaluated?
4. What limitation/gap motivates this project?
5. How is the proposed experiment different?

---

# 14. Research Proposal – Student Template

## Title
A concise research-oriented title.

## 1. Background
Brief OS context.

## 2. Problem Statement
Clearly identify the problem.

## 3. Motivation
Why is the problem worth investigating?

## 4. Literature Review
Summarize relevant sources.

## 5. Research Gap
Identify what is missing, uncertain or worth extending.

## 6. Research Question
State the primary research question.

## 7. Hypothesis
State the expected relationship.

## 8. Objectives
List 2–3 measurable objectives.

## 9. Methodology
Describe experimental design.

## 10. Tools and Language
Specify Python/Linux/Rust/etc.

## 11. Metrics
Identify measurable outcomes.

## 12. Expected Contribution
State what the experiment is expected to add.

---

# 15. Final Research Report Structure

Students submit a concise technical report containing:

1. Title
2. Abstract
3. Introduction
4. Problem Statement
5. Literature Review
6. Research Gap
7. Research Question/Hypothesis
8. Objectives
9. Methodology
10. Implementation
11. Experimental Setup
12. Results
13. Analysis and Discussion
14. Threats to Validity / Limitations
15. Conclusion
16. Future Work
17. References
18. AI Usage Disclosure

---

# 16. Suggested Experimental Evidence

Students should prioritize evidence over screenshots.

### Preferred evidence

- performance tables;
- graphs;
- statistical summaries;
- workload traces;
- timing measurements;
- scalability curves;
- fairness measures;
- memory usage;
- CPU utilization;
- page-fault counts;
- context-switch counts;
- seek distance;
- correctness/error rates.

### Screenshots

Screenshots may support the report but **must not substitute for numerical evidence**.

---

# 17. Recommended Visualizations

Depending on the project:

- line graph – parameter vs performance;
- bar chart – algorithm comparison;
- scatter plot – workload vs performance;
- box plot – variability across repeated runs;
- heat map – parameter interaction;
- stacked chart – resource composition;
- scalability curve – workers/cores vs throughput.

Students must explain what every graph demonstrates.

---

# 18. Threats to Validity

Every report should identify at least two limitations, such as:

- hardware variation;
- operating-system background activity;
- insufficient repetitions;
- simulation assumptions;
- unrealistic workloads;
- measurement overhead;
- limited parameter range;
- small sample size;
- differences between simulated and real OS behaviour.

This encourages students to understand that **experimental evidence has limitations**.

---

# 19. CA-4 Assessment – 10 Marks

| Criterion | Marks |
|---|---:|
| Research problem, question and gap | 2 |
| Literature review and research justification | 1 |
| Experimental methodology and design | 2 |
| Prototype/implementation and correctness | 1 |
| Data collection, analysis and visualization | 2 |
| Research interpretation, limitations and conclusion | 1 |
| Technical communication and AI-use disclosure | 1 |
| **Total** | **10** |

---

# 20. Performance-Level Rubric

| Criterion | Excellent | Good | Developing | Needs Improvement |
|---|---|---|---|---|
| Problem & Gap | Specific, meaningful and evidence-backed | Clear but limited | Broad/partially defined | Topic only |
| Literature | Critical synthesis | Adequate review | Mostly descriptive | Minimal/unverified |
| Methodology | Controlled and reproducible | Mostly sound | Several uncontrolled factors | Poorly designed |
| Implementation | Correct and appropriate | Minor issues | Partial implementation | Incorrect/incomplete |
| Analysis | Evidence-based and insightful | Correct interpretation | Basic comparison | Unsupported claims |
| Conclusion | Directly answers question and recognizes limits | Mostly supported | Partially supported | Unsupported |
| Communication | Clear research-style presentation | Generally clear | Some gaps | Difficult to follow |

---

# 21. Recommended Team Model

### Individual
Suitable for simulation-heavy research topics.

### Pair
Recommended for Linux experiments and moderate implementation work.

### Team of 3
Recommended for projects involving:

- literature review;
- system implementation;
- experimental infrastructure;
- data analysis.

### Team rule

Each member must demonstrate an identifiable contribution.

---

# 22. Faculty Approval Checkpoint

Before implementation, faculty should verify:

- [ ] Topic is OS-specific.
- [ ] Research problem is narrower than the topic.
- [ ] At least one research question is measurable.
- [ ] Literature has been identified.
- [ ] Research gap is plausible.
- [ ] Variables are identified.
- [ ] Metrics are measurable.
- [ ] Required tools are available.
- [ ] Project is achievable within CA-4 scope.
- [ ] Ethical/legal issues are considered.
- [ ] Expected evidence is clearly defined.

---

# 23. Suggested 4-Week Execution Plan

| Week | Activity | Deliverable |
|---|---|---|
| Week 1 | Topic selection + literature discovery | Research proposal |
| Week 2 | Gap + methodology + prototype | Methodology checkpoint |
| Week 3 | Experiments + data collection | Raw results |
| Week 4 | Analysis + report + presentation | Final report and demonstration |

---

# 24. CA-4 → CA-5 → CA-6 Progression

CA-4 is intentionally designed as the bridge between **research thinking** and **systems engineering**.

### CA-4
Students ask:

> “What behaviour should I investigate?”

### CA-5
Students ask:

> “Can I observe this behaviour on a real Linux system?”

### CA-6
Students ask:

> “Can I implement the underlying OS mechanism myself?”

This produces the learning pathway:

**Research Question → Experimental Evidence → Linux Observation → Systems Implementation → Micro-OS**

---

# 25. Connection to Rust Micro-OS

Selected CA-4 research topics can become direct preparation for CA-6.

| CA-4 Research | CA-6 Micro-OS Extension |
|---|---|
| CPU scheduling | Implement a kernel scheduler |
| Thread scalability | Kernel task/thread management |
| Synchronization contention | Kernel mutex/spinlock |
| Memory allocation | Kernel allocator |
| Page management | Virtual/physical memory subsystem |
| Context switching | Task/context switch |
| Interrupt-related performance | Interrupt handling |
| File-system performance | Minimal file system |
| Resource isolation | Kernel-level protection |
| Rust vs Python systems performance | Rust-based kernel components |

This mirrors the progressive structure used in OS implementation courses, where processes, synchronization, scheduling, memory and file systems build upon one another. citeturn0search2turn0search10

---

# 26. Research-to-Micro-OS Challenge

For advanced students, faculty may add:

> **“Identify one OS mechanism investigated in CA-4 and design a minimal Rust implementation of that mechanism suitable for integration into the CA-6 Micro-OS.”**

Possible mechanisms:

- round-robin scheduler;
- priority scheduler;
- task queue;
- spinlock;
- mutex abstraction;
- simple allocator;
- page-frame allocator;
- timer-based preemption;
- basic system-call interface.

This creates continuity rather than treating the Micro-OS as an isolated programming project.

---

# 27. CO Alignment

| CA-4 Component | Primary CO | Secondary COs |
|---|---|---|
| OS research problem | CO1 | CO2–CO5 |
| Scheduling investigation | CO2 | CO1, CO6 |
| Synchronization/deadlock research | CO3 | CO2, CO6 |
| Memory research | CO4 | CO1, CO6 |
| File/I/O research | CO5 | CO1, CO6 |
| Linux systems investigation | CO6 | CO1–CO5 |
| Rust systems research | CO6 | CO2–CO5 |

**Primary CO emphasis:** **CO2, CO3, CO4, CO5 and CO6**, with CO1 providing the conceptual foundation.

---

# 28. Institutional Philosophy Alignment

## Primary Dimension: Research Experience

CA-4 directly addresses:

- literature discovery using AI-supported tools;
- identification and justification of research problems;
- formulation of research questions;
- development of basic research proposals;
- use of appropriate research methodology;
- technical communication with research orientation.

### Research Experience Mapping

| Research LO | CA-4 Evidence |
|---|---|
| LO1 – Literature review using AI tools | AI-assisted literature discovery and verified review |
| LO2 – Define/justify research problems | Research gap and question |
| LO3 – Structure mini-project using research methods | Methodology and experiment |
| LO4 – Communicate with experts/researchers | Literature engagement and optional expert interaction |

---

## Secondary Dimension: Critical Thinking

CA-4 develops:

- structured evaluation of evidence;
- comparison of competing approaches;
- hypothesis-driven investigation;
- questioning of assumptions;
- reasoned technical conclusions;
- corroboration of AI-generated claims.

---

# 29. CA-4 CO–Philosophy Matrix

| CA-4 Activity | Research Experience | Critical Thinking | Innovation & Professional Development | Real World Exposure |
|---|---:|---:|---:|---:|
| Literature review | **High** | High | Moderate | Low |
| Research-gap identification | **High** | **High** | High | Moderate |
| Hypothesis formation | High | **High** | High | Moderate |
| Experimental design | **High** | **High** | High | Moderate |
| Prototype development | High | High | **High** | Moderate |
| Data analysis | **High** | **High** | Moderate | Moderate |
| Engineering recommendation | High | **High** | **High** | **High** |
| Research presentation | High | High | High | **High** |

---

# 30. PO/PSO Contribution

CA-4 strongly supports:

### PO1 – Engineering Knowledge
Application of OS concepts to research problems.

### PO2 – Problem Analysis
Research-gap identification, modelling and evidence-based analysis.

### PO3 – Design/Development
Design of experiments and prototypes.

### PO4 – Conduct Investigations
**Strongest alignment:** systematic experimentation, measurement and interpretation.

### PO5 – Engineering Tool Usage
Python, Linux, Rust and AI-assisted research tools.

### PO6 – Engineer and World
Investigation of practical system-performance and resource-management issues.

### PO7 – Ethics
Responsible AI usage, citation, reproducibility and research integrity.

### PO8 – Teamwork
Collaborative research and implementation.

### PO9 – Communication
Technical research report and presentation.

### PO10 – Project Management
Milestones, scope, workload and resource planning.

### PO11 – Lifelong Learning
Independent literature discovery and engagement with emerging OS technologies.

### PSO1
Design and development of OS-oriented software/system solutions.

### PSO2
Application of modern tools and Linux/Rust/Python technologies.

### PSO3
Investigation of OS infrastructure supporting AI/ML workloads, particularly memory, scheduling and resource management.

---

# 31. Faculty Guidance – Avoiding Common Problems

### Problem 1: “My topic is too broad.”
**Correction:** Convert the topic into a measurable question.

### Problem 2: “I only implemented an algorithm.”
**Correction:** Require a comparison, hypothesis and evidence.

### Problem 3: “AI gave me the literature review.”
**Correction:** Require original-paper verification and critical synthesis.

### Problem 4: “My results are just screenshots.”
**Correction:** Require numerical measurements and visual analysis.

### Problem 5: “My project is a normal application.”
**Correction:** Require a clear OS mechanism, behaviour or systems-performance question.

### Problem 6: “The experiment gives unexpected results.”
**Correction:** Treat unexpected results as research evidence; investigate the cause instead of manipulating the data.

### Problem 7: “I could not prove my hypothesis.”
**Correction:** A well-designed negative result is still a valid research outcome.

---

# 32. Academic Integrity and Research Ethics

Students must:

- cite all external sources;
- avoid fabricated results;
- distinguish measured results from estimates;
- disclose AI assistance;
- retain raw experimental data;
- report unexpected findings;
- avoid manipulating graphs or measurements;
- clearly distinguish their own work from reused code;
- obtain faculty approval for experiments involving external systems or potentially sensitive data.

---

# 33. Recommended Submission Package

Each team submits:

1. **Research proposal**
2. **Literature matrix**
3. **Source code**
4. **Experimental configuration**
5. **Raw data**
6. **Processed data**
7. **Graphs/tables**
8. **Final research report**
9. **AI-use disclosure**
10. **Short demonstration/presentation**

---

# 34. Literature Matrix Template

| Ref. | Problem | Method | Dataset/Workload | Metrics | Key Finding | Limitation | Relevance |
|---|---|---|---|---|---|---|---|
| Paper 1 | | | | | | | |
| Paper 2 | | | | | | | |
| Paper 3 | | | | | | | |
| Paper 4 | | | | | | | |
| Paper 5 | | | | | | | |

This prevents literature review from becoming a collection of disconnected summaries.

---

# 35. Suggested Faculty Evaluation Questions

During review/viva, ask:

1. Why did you choose this problem?
2. What is the research gap?
3. Which paper most strongly influenced your methodology?
4. What is your independent variable?
5. What is your dependent variable?
6. Why did you choose these metrics?
7. Why is your workload representative?
8. What would invalidate your hypothesis?
9. Why did your results occur?
10. What alternative explanation exists?
11. What are the limitations?
12. How would you extend this work?
13. Could the experiment be reproduced by another student?
14. Where did AI assist you?
15. Which AI-generated claim did you have to correct or reject?

---

# 36. Final CA-4 Student Checklist

Before submission:

- [ ] My project has a specific OS problem.
- [ ] I have a measurable research question.
- [ ] I have reviewed relevant literature.
- [ ] I can state the research gap.
- [ ] I have a hypothesis or testable expectation.
- [ ] My variables are clearly defined.
- [ ] My experiment is reproducible.
- [ ] I used an appropriate programming language.
- [ ] I collected numerical evidence.
- [ ] I repeated important experiments.
- [ ] I included graphs/tables.
- [ ] I interpreted the results using OS concepts.
- [ ] I reported limitations.
- [ ] I answered the research question.
- [ ] I cited all sources.
- [ ] I disclosed AI usage.
- [ ] Every team member can explain the work.

---

# 37. Overall Educational Significance

CA-4 transforms the OS course from a sequence of algorithmic exercises into an **evidence-driven engineering and research experience**.

The intended progression is:

> **Understand → Question → Investigate → Experiment → Analyze → Conclude → Propose**

This is particularly valuable because contemporary OS research continues to address scheduling, memory, virtualization, resource management, safety, security and performance on increasingly heterogeneous hardware. citeturn0search0

CA-4 therefore acts as the **research bridge** between conceptual OS learning and the subsequent real-system/Linux and Rust Micro-OS engineering activities.

---

## One-Line CA-4 Definition

> **CA-4 requires students to identify a focused Operating Systems research question, investigate it through literature and reproducible experimentation, analyze evidence, and defend an evidence-based engineering conclusion.**
