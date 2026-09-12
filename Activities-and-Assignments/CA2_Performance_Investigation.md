# Operating Systems – CA-2
## OS Performance Investigation
### Continuous Assessment: 10 Marks

---

## 1. Overview

The **OS Performance Investigation** is the second Continuous Assessment (CA) component of the Operating Systems course. It moves students from the analytical scenario-solving approach of CA-1 into **evidence-based experimentation and performance engineering**.

Students are not simply asked to implement operating-system algorithms. They are expected to:

> **Implement → Execute → Measure → Compare → Interpret → Conclude**

The assessment emphasizes the idea that an operating-system mechanism should be evaluated according to the workload and performance objective for which it is being considered.

The primary institutional dimensions developed are:

- **Critical Thinking**
- **Innovation & Professional Development**

with supporting development of:

- Research Experience
- Real World Exposure

---

# 2. Purpose of the Investigation

Operating-system mechanisms involve engineering trade-offs. An algorithm that performs well for one workload may perform poorly for another.

For example:

- Round Robin may improve responsiveness but increase context switching.
- SJF may reduce average waiting time but require knowledge/estimation of CPU bursts.
- LRU may outperform FIFO for some workloads but requires additional tracking.
- SSTF may reduce immediate disk-head movement but may cause starvation.
- Increasing the number of threads may improve throughput until synchronization or scheduling overhead dominates.

Therefore, students must learn to answer:

> **“What does the experimental evidence tell us?”**

rather than:

> **“Which algorithm is theoretically best?”**

---

# 3. Learning Outcomes of CA-2

After completing this CA, students should be able to:

1. Design an OS performance experiment.
2. Implement OS algorithms using an appropriate programming language.
3. Generate controlled workloads and test conditions.
4. Define relevant performance metrics.
5. Collect experimental data systematically.
6. Compare multiple OS mechanisms.
7. Visualize performance trends.
8. Identify trade-offs and performance bottlenecks.
9. Interpret unexpected experimental results.
10. Draw evidence-based engineering conclusions.
11. Use AI tools to assist experimental design while independently verifying results.
12. Communicate experimental findings through a concise technical report.

---

# 4. Assessment Structure

| Component | Marks |
|---|---:|
| Experimental design and methodology | 2 |
| Implementation and correctness | 2 |
| Data collection and measurement | 2 |
| Analysis and visualization | 2 |
| Engineering interpretation and conclusion | 2 |
| **Total** | **10** |

---

# 5. Mandatory Experimental Workflow

Every student/team must follow the following workflow.

## Step 1 – Define the Performance Question

The experiment must begin with a question that can be experimentally investigated.

Weak:

> “Study CPU scheduling.”

Strong:

> “How does Round Robin time quantum affect response time, waiting time and context-switch frequency for an interactive workload?”

The question should identify:

- OS mechanism
- Variable being investigated
- Performance measures
- Workload/environment

---

# 6. Step 2 – Formulate a Hypothesis

Students should predict the expected behaviour before running the experiment.

Example:

> “Reducing the Round Robin time quantum is expected to improve response time but increase context-switch overhead.”

The hypothesis must be testable.

---

# 7. Step 3 – Identify Variables

Students should identify:

### Independent variables

Variables intentionally changed.

Examples:

- Time quantum
- Number of processes
- Number of threads
- Page-frame count
- Page-reference pattern
- Disk-request sequence
- Buffer size

### Dependent variables

What is measured.

Examples:

- Waiting time
- Turnaround time
- Response time
- Throughput
- Page faults
- Hit ratio
- Head movement
- Execution time
- CPU utilization
- Memory utilization

### Controlled variables

Conditions that should remain constant.

Examples:

- Input workload
- Hardware
- Dataset
- Number of repetitions
- Compiler/interpreter version
- Operating environment

---

# 8. Step 4 – Implement the Experiment

## Programming Language Policy

The programming language must be explicitly stated for every experiment.

### Recommended default

**Python** is the default language for algorithmic OS simulations and performance experiments.

Python is recommended for:

- CPU scheduling simulation
- Deadlock simulation
- Memory allocation
- Page replacement
- Disk scheduling
- File-system simulation
- Performance data processing
- Visualization

### Linux systems experiments

Students may use:

- **Python**
- **Bash**
- **Rust**

depending on the experiment.

### Rust usage

Rust is encouraged for experiments involving:

- Threads
- Synchronization
- Memory behaviour
- Systems programming
- Low-level performance
- Comparison with Python
- Preparation for the Micro-OS project

### Important principle

The programming language must not become the focus of the assessment unless the experiment explicitly investigates language/runtime behaviour.

The primary assessment remains:

> **OS concept + experimental design + measurement + interpretation**

---

# 9. Step 5 – Execute Controlled Experiments

Each experiment should normally include:

- Multiple input sizes
- Multiple workload conditions
- Multiple parameter values
- At least three repetitions where runtime measurement is involved

Students should document the experimental environment.

Example:

| Parameter | Value |
|---|---|
| OS | Ubuntu Linux |
| Python | Python 3.x |
| Rust | Rust stable |
| CPU | [Student records] |
| RAM | [Student records] |
| Dataset | [Student records] |
| Repetitions | 5 |
| Date | [Student records] |

---

# 10. Step 6 – Collect Data

Students should maintain structured experimental data.

Example:

| Algorithm | Quantum | Avg Waiting | Avg Turnaround | Avg Response | Context Switches |
|---|---:|---:|---:|---:|---:|
| FCFS | – | | | | |
| SJF | – | | | | |
| RR | 5 | | | | |
| RR | 10 | | | | |
| RR | 20 | | | | |

Raw observations should be retained even if only summarized values appear in the report.

---

# 11. Step 7 – Analyze and Visualize

Students should select suitable visualizations.

Possible plots include:

- Bar charts
- Line charts
- Scatter plots
- Box plots
- Performance curves
- Workload-vs-performance graphs

Examples:

> Time Quantum → Average Response Time

> Number of Processes → Context Switches

> Number of Frames → Page Faults

> Request Queue Size → Average Disk Head Movement

The graph must be accompanied by an interpretation.

A graph without interpretation is incomplete evidence.

---

# 12. Step 8 – Interpret the Results

Students should answer:

1. What pattern is visible?
2. Was the hypothesis supported?
3. Why did the observed behaviour occur?
4. Were there unexpected results?
5. What trade-offs became visible?
6. Under what workload would the result change?

---

# 13. Step 9 – Make an Engineering Recommendation

Students should conclude with a context-specific recommendation.

Example:

> “For the tested interactive workload, a 10 ms Round Robin quantum provides a suitable balance between response time and context-switch overhead. A smaller quantum improves responsiveness marginally but introduces substantially more scheduling overhead.”

---

# 14. Experiment Bank

The following experiments can be assigned individually or in teams.

---

# EXPERIMENT 1 – CPU Scheduling Performance

## Title

**Experimental Comparison of CPU Scheduling Algorithms**

## Programming Language

**Python 3.x – Recommended**

Optional extension:

**Rust**

## Objective

Compare the performance of:

- FCFS
- SJF
- SRTF
- Priority Scheduling
- Round Robin

under different workload conditions.

## Parameters

Students may vary:

- Number of processes
- CPU burst lengths
- Arrival patterns
- Priority distribution
- Round Robin time quantum

## Metrics

Measure:

- Average waiting time
- Average turnaround time
- Average response time
- Throughput
- Number of context switches

## Tasks

1. Implement the scheduling algorithms in Python.
2. Generate at least three workload types:
   - CPU-bound
   - I/O-oriented/short-burst
   - Mixed
3. Run all algorithms against equivalent workloads.
4. Collect performance metrics.
5. Plot results.
6. Determine which algorithm performs best for each workload.
7. Explain why there is no universally optimal scheduler.

## Extension

Implement the scheduler in Rust and compare execution overhead with Python.

---

# EXPERIMENT 2 – Round Robin Time Quantum Investigation

## Programming Language

**Python 3.x – Recommended**

Optional:

**Rust**

## Question

> How does time quantum influence system responsiveness and scheduling overhead?

## Vary

For example:

- 1 ms
- 5 ms
- 10 ms
- 20 ms
- 50 ms
- 100 ms

## Measure

- Response time
- Waiting time
- Turnaround time
- Context switches
- Throughput

## Expected Investigation

Students should identify the point at which decreasing the quantum provides diminishing responsiveness benefits while increasing overhead.

---

# EXPERIMENT 3 – Scheduling Under Different Workloads

## Programming Language

**Python 3.x**

## Workloads

Create:

1. Mostly short processes
2. Mostly long processes
3. Mixed workload
4. Burst-heavy workload
5. Interactive workload

Compare scheduling algorithms.

## Key Question

> Does the ranking of scheduling algorithms change when the workload changes?

Students must explain the result.

---

# EXPERIMENT 4 – Process Creation vs Thread Creation

## Programming Language

**Python 3.x + Rust**

## Objective

Investigate the cost and behaviour of process and thread creation.

## Tasks

Students should:

1. Create equivalent workloads using processes.
2. Create equivalent workloads using threads.
3. Measure creation/execution overhead.
4. Repeat with different numbers of workers.
5. Analyze scalability.

## Metrics

- Creation time
- Completion time
- CPU utilization
- Memory consumption
- Scaling behaviour

## Important Discussion

Students should explain why:

> “More threads” does not necessarily mean “more performance.”

---

# EXPERIMENT 5 – Synchronization Contention

## Programming Language

**Python 3.x**

Optional low-level comparison:

**Rust**

## Objective

Investigate the effect of synchronization on concurrent execution.

## Compare

- No synchronization
- Mutex/lock
- Semaphore
- Alternative synchronization strategies where appropriate

## Measure

- Execution time
- Throughput
- Contention
- Correctness
- Waiting behaviour

## Required Demonstration

Students should deliberately create a race condition and then correct it.

---

# EXPERIMENT 6 – Producer-Consumer Performance

## Programming Language

**Python 3.x**

Optional:

**Rust**

## Parameters

Vary:

- Buffer size
- Producer rate
- Consumer rate
- Number of producers
- Number of consumers

## Measure

- Throughput
- Waiting time
- Buffer utilization
- Producer blocking
- Consumer blocking

## Core Question

> What buffer size provides a suitable balance between throughput and memory usage?

---

# EXPERIMENT 7 – Deadlock Detection and Avoidance

## Programming Language

**Python 3.x**

## Objective

Study how resource allocation affects deadlock.

## Tasks

1. Generate multiple process/resource configurations.
2. Implement deadlock detection.
3. Implement Banker's Algorithm.
4. Generate safe and unsafe states.
5. Compare computational behaviour.
6. Visualize resource dependencies.

## Investigation

Students should determine:

> Under what resource conditions does the system move from safe to unsafe?

---

# EXPERIMENT 8 – Memory Allocation Strategies

## Programming Language

**Python 3.x**

## Compare

- First Fit
- Best Fit
- Worst Fit

## Vary

- Number of requests
- Request sizes
- Initial memory size
- Allocation sequence

## Measure

- Internal fragmentation
- External fragmentation
- Memory utilization
- Allocation failures

## Required Conclusion

Students should identify which strategy is preferable under different workload patterns.

---

# EXPERIMENT 9 – Page Replacement Performance

## Programming Language

**Python 3.x**

## Compare

- FIFO
- LRU
- Optimal

## Vary

- Number of frames
- Page-reference string
- Locality patterns
- Random access patterns
- Sequential access patterns

## Measure

- Page faults
- Hit ratio
- Fault rate

## Key Investigation

Students should investigate **Belady's anomaly** using appropriate FIFO workloads.

---

# EXPERIMENT 10 – Working Set and Thrashing

## Programming Language

**Python 3.x**

## Objective

Investigate the relationship between:

- Number of processes
- Available frames
- Working-set size
- Page faults

## Students should

1. Simulate increasing memory pressure.
2. Measure page faults.
3. Identify the onset of thrashing.
4. Relate page-fault behaviour to system performance.

---

# EXPERIMENT 11 – Disk Scheduling Performance

## Programming Language

**Python 3.x**

## Compare

- FCFS
- SSTF
- SCAN
- C-SCAN
- LOOK
- C-LOOK

## Metrics

- Total head movement
- Average seek distance
- Request service order
- Potential starvation

## Investigation

Students should determine which algorithm is appropriate for different request distributions.

---

# EXPERIMENT 12 – SSD vs HDD Scheduling Assumptions

## Programming Language

**Python 3.x**

## Objective

Investigate whether traditional disk-scheduling assumptions remain equally relevant for SSD-based storage.

Students should:

- Simulate HDD-style seek costs.
- Model simplified SSD access behaviour.
- Compare algorithmic decisions.
- Explain which metrics change in importance.

This is primarily a **systems reasoning experiment**, not a hardware benchmark.

---

# EXPERIMENT 13 – File-System Performance

## Programming Language

**Python 3.x**

Optional:

**Rust**

## Investigate

Compare access patterns involving:

- Many small files
- Few large files
- Sequential access
- Random access

## Measure

- Creation time
- Read/write time
- Directory traversal time
- Storage utilization

Students should explain how workload characteristics influence observed performance.

---

# EXPERIMENT 14 – Linux Process Performance Investigation

## Programming Language

**Python 3.x + Linux tools**

Optional:

**Rust**

## Tools

Students may use appropriate Linux utilities such as:

- `ps`
- `top`
- `htop`
- `time`
- `vmstat`
- `iostat`
- `pidstat`
- `strace`

subject to system availability.

## Tasks

1. Create a controlled workload.
2. Observe its process behaviour.
3. Record CPU and memory usage.
4. Identify process states.
5. Investigate system calls where appropriate.
6. Correlate observations with OS concepts.

---

# EXPERIMENT 15 – Context-Switch Investigation

## Programming Language

**Python 3.x**

Optional:

**Rust/C**

## Objective

Investigate how workload concurrency influences context-switch behaviour.

Students should vary:

- Number of processes
- Number of threads
- Workload intensity

and examine:

- Context switches
- Execution time
- CPU utilization
- Throughput

---

# EXPERIMENT 16 – CPU Affinity and Performance

## Programming Language

**Python 3.x + Linux**

Optional:

**Rust**

## Objective

Investigate whether restricting a process to selected CPU cores changes performance.

Students should compare:

- Unrestricted execution
- Single-core affinity
- Multi-core affinity

and measure suitable performance metrics.

---

# EXPERIMENT 17 – Python vs Rust Concurrency

## Programming Languages

**Python 3.x and Rust stable**

## Objective

Compare two implementation environments for a controlled concurrency workload.

Students should investigate:

- Execution time
- Memory consumption
- Thread/process behaviour
- Scaling
- Synchronization overhead

## Important Constraint

The conclusion must not simply be:

> “Rust is faster than Python.”

Students must explain **why the observed difference exists and which part is attributable to the programming language/runtime versus the OS mechanism itself**.

---

# EXPERIMENT 18 – Mini Linux System Monitor

## Programming Language

**Python 3.x**

Optional extension:

**Rust**

## Objective

Develop a lightweight system-monitoring application.

The program should display selected:

- CPU utilization
- Memory utilization
- Process information
- Process states
- Resource consumption

## Investigation

Students should use their monitor to investigate at least one controlled workload and produce an evidence-based performance report.

---

# 15. Advanced Open-Ended Investigations

Students demonstrating stronger performance may be assigned open-ended experiments.

### Investigation A – Does More Concurrency Improve Performance?

Students vary worker count and determine where performance stops improving.

### Investigation B – When Does Scheduling Overhead Become Significant?

Students investigate the relationship between time quantum and context switching.

### Investigation C – Memory Pressure Threshold

Students identify the point at which additional processes cause a sharp increase in paging activity.

### Investigation D – Synchronization Scalability

Students determine how increasing thread count affects lock contention.

### Investigation E – I/O vs CPU Bottleneck

Students construct workloads designed to be:

- CPU-bound
- I/O-bound
- Mixed

and use Linux monitoring tools to distinguish them.

---

# 16. Experimental Reproducibility

Every submission should provide enough information for another student to reproduce the experiment.

Minimum requirements:

- Source code
- Input data/workload
- Programming language and version
- Operating system
- Hardware information where relevant
- Parameters
- Number of repetitions
- Raw measurements
- Analysis method

---

# 17. Handling Experimental Noise

Students must understand that real systems do not always produce identical measurements.

Sources of variation may include:

- Background processes
- CPU frequency scaling
- Cache effects
- Operating-system scheduling
- Memory pressure
- Thermal behaviour
- I/O contention

Students should not simply discard unexpected measurements.

They should explain possible causes.

---

# 18. AI-Assisted Experiment Design

AI tools may be used for:

- Generating hypotheses
- Suggesting experimental parameters
- Identifying relevant performance metrics
- Reviewing experimental design
- Generating visualization ideas
- Suggesting possible explanations for unexpected results

However:

> **AI-generated numerical results must never be treated as experimental evidence.**

Students must execute the experiment themselves.

## Required AI Disclosure

Students should document:

### AI Tool

Name and version, where available.

### Purpose

What the AI was used for.

### Suggestion

Brief summary of the relevant suggestion.

### Verification

How the student independently verified it.

### Reflection

Whether the suggestion was:

- Correct
- Partially correct
- Incorrect
- Incomplete

---

# 19. Required Technical Report Structure

Every CA-2 report should contain:

## 1. Title

Concise experiment title.

## 2. Research/Performance Question

Clearly state what is being investigated.

## 3. Objective

State the intended learning/engineering objective.

## 4. OS Concept

Explain the relevant OS mechanism.

## 5. Hypothesis

State the expected result.

## 6. Experimental Environment

Include:

- Programming language
- Language version
- OS
- Hardware
- Tools

## 7. Variables

Identify:

- Independent
- Dependent
- Controlled variables

## 8. Methodology

Explain how the experiment was performed.

## 9. Implementation

Provide or reference the source code.

## 10. Test Cases/Workloads

Document inputs and configurations.

## 11. Raw Results

Provide experimental measurements.

## 12. Analysis

Compare results.

## 13. Visualization

Include relevant plots.

## 14. Discussion

Explain observed behaviour and anomalies.

## 15. Engineering Decision

State the recommended mechanism/configuration.

## 16. Limitations

Explain limitations of the experiment.

## 17. AI Disclosure

Document AI assistance and verification.

## 18. Conclusion

Provide a concise evidence-based conclusion.

---

# 20. Example of a Strong Analysis

Suppose the Round Robin experiment produces:

| Quantum | Avg Response Time | Avg Waiting Time | Context Switches |
|---:|---:|---:|---:|
| 5 ms | 12 ms | 38 ms | 420 |
| 10 ms | 15 ms | 40 ms | 240 |
| 20 ms | 18 ms | 43 ms | 130 |
| 50 ms | 31 ms | 51 ms | 60 |

A weak conclusion would be:

> “5 ms is the best because it has the lowest response time.”

A stronger conclusion is:

> “The 5 ms quantum produces the lowest response time but also generates substantially more context switches. Increasing the quantum reduces scheduling overhead at the expense of responsiveness. For the tested interactive workload, 10–20 ms provides a more balanced trade-off. The final choice would depend on the required response-time target and acceptable scheduling overhead.”

This demonstrates **engineering thinking rather than metric chasing**.

---

# 21. Assessment Rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| **Experimental Design** | No clear methodology | Basic experiment with limited control | Well-defined, controlled and reproducible experiment |
| **Implementation & Correctness** | Incorrect/missing implementation | Mostly functional | Correct, appropriate and well-tested implementation |
| **Measurement** | No meaningful data | Limited/inconsistent measurements | Systematic and reliable measurements |
| **Analysis & Visualization** | No meaningful analysis | Basic comparison | Appropriate quantitative analysis with clear visualization |
| **Engineering Interpretation** | Unsupported conclusion | Reasonable conclusion | Evidence-based conclusion with trade-offs and limitations |
| **TOTAL** | | | **10** |

---

# 22. Performance Levels

| Level | Student Behaviour |
|---|---|
| **Basic** | Correctly implements the required algorithm and reports results. |
| **Developing** | Compares alternatives using relevant metrics. |
| **Proficient** | Explains performance trends and workload dependence. |
| **Advanced** | Identifies trade-offs, anomalies and limitations. |
| **Exceptional** | Designs additional experiments, challenges assumptions and derives new engineering insights. |

---

# 23. Recommended CA-2 Assignment Model

Rather than giving every student exactly the same experiment, use a **common experimental framework with different investigation questions**.

For example, all students study CPU scheduling but receive different questions:

| Student/Team | Investigation |
|---|---|
| Team A | Effect of time quantum |
| Team B | Effect of workload type |
| Team C | Effect of process count |
| Team D | Response time vs context switching |
| Team E | Fairness vs throughput |
| Team F | Python implementation vs Rust implementation |

This makes plagiarism/copying less useful while maintaining common assessment criteria.

---

# 24. Recommended Language Progression

CA-2 should deliberately establish the language progression toward the Micro-OS project.

| Stage | Programming Language | Purpose |
|---|---|---|
| Algorithm simulation | **Python** | Focus on OS logic and experimentation |
| Data analysis | **Python** | Metrics, statistics and visualization |
| Linux interaction | **Python + Bash** | Observe real OS behaviour |
| Systems programming | **Python / Rust** | Compare abstraction levels |
| Low-level experiments | **Rust** | Introduce systems-level thinking |
| Future Micro-OS | **Rust** | Kernel-level implementation |

The important pedagogical principle is:

> **Students first understand the OS mechanism independently of language complexity, then progressively move toward systems-level implementation.**

---

# 25. Connection with CA-1

CA-1 asked students:

> **“Given this situation, what should the OS do?”**

CA-2 now asks:

> **“Can you experimentally demonstrate whether your reasoning is correct?”**

| CA-1 | CA-2 |
|---|---|
| Scenario | Experiment |
| Identify | Measure |
| Model | Implement |
| Analyze | Compare |
| Decide | Validate |
| Justify | Evidence-based conclusion |

This creates a deliberate progression from **systems thinking to experimental engineering**.

---

# 26. Connection with the Rust Micro-OS Project

CA-2 should also prepare students for the later Micro-OS project.

For example:

| CA-2 Experiment | Future Micro-OS Connection |
|---|---|
| CPU scheduling | Kernel scheduler |
| Thread performance | Kernel tasks |
| Synchronization | Kernel locks |
| Memory allocation | Kernel allocator |
| Page replacement | Virtual memory |
| Context switching | Task switching |
| I/O performance | Device/console handling |
| System monitoring | Kernel/system information |
| Python vs Rust | Motivation for Rust systems programming |

Thus, CA-2 is not an isolated performance laboratory. It becomes the **experimental foundation for CA-6: Rust Micro-OS Engineering Project**.

---

# 27. Student Submission Checklist

Before submission, students should confirm:

- [ ] Performance question is clearly stated.
- [ ] Hypothesis is testable.
- [ ] OS concept is explained.
- [ ] Programming language and version are documented.
- [ ] Operating environment is documented.
- [ ] Independent/dependent/controlled variables are identified.
- [ ] Workloads/test cases are documented.
- [ ] Experiment is reproducible.
- [ ] Raw measurements are retained.
- [ ] Appropriate metrics are calculated.
- [ ] Results are visualized where appropriate.
- [ ] Unexpected observations are discussed.
- [ ] Alternatives/trade-offs are considered.
- [ ] Engineering recommendation is evidence-based.
- [ ] Limitations are stated.
- [ ] AI usage is disclosed and verified.

---

# 28. Faculty Guidelines

Faculty should avoid designing experiments where:

- The answer is already obvious.
- Students only reproduce textbook calculations.
- There is no measurable output.
- Only one input case is tested.
- Students are rewarded for obtaining a predetermined result.
- AI can generate the entire submission without experimentation.

Instead, experiments should contain:

> **A variable → A measurable outcome → A comparison → An interpretation → A decision**

---

# 29. Core Philosophy of CA-2

The central learning philosophy is:

> **Do not tell me which OS mechanism is better. Show me the evidence under a defined workload, explain why the evidence looks the way it does, identify the trade-offs, and tell me when your conclusion would change.**

By completing CA-2, students should begin thinking like **OS performance engineers**, rather than merely programmers who implement OS algorithms.

The progression should therefore be:

> **Question → Hypothesis → Experiment → Measurement → Evidence → Interpretation → Engineering Decision**

