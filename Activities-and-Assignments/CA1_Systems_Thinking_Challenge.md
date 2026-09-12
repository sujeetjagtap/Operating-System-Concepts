# Operating Systems – CA-1
## OS Systems Thinking Challenge
### Continuous Assessment: 10 Marks

---

## 1. Overview

The **OS Systems Thinking Challenge** is the first Continuous Assessment (CA) component of the Operating Systems course. It replaces a conventional written Internal Assessment with a **scenario-based, analytical and decision-oriented evaluation**.

The objective is not merely to test whether students can recall definitions, algorithms or textbook procedures. Students are expected to examine a realistic computing situation, identify the underlying operating-system problem, reason about alternative approaches, select an appropriate OS mechanism, and defend their engineering decision.

The activity is designed around the philosophy:

> **Understand → Observe → Model → Analyze → Decide → Justify**

The challenge primarily develops the institutional dimensions of:

- **Critical Thinking**
- **Research Experience**

with supporting development of:

- Innovation & Professional Development
- Real World Exposure

---

# 2. Purpose of the Challenge

Operating Systems concepts are often learned as isolated algorithms and definitions. In practice, however, an operating system is a collection of interacting mechanisms that must make engineering trade-offs involving:

- CPU utilization
- response time
- throughput
- fairness
- synchronization
- resource allocation
- memory utilization
- storage efficiency
- reliability
- security
- scalability
- energy consumption
- system responsiveness

The Systems Thinking Challenge places students in such situations.

Students must move beyond:

> “What is the definition of this OS concept?”

towards:

> “Given this situation, what is actually happening, why is it happening, what alternatives exist, which mechanism should be selected, and why?”

---

# 3. Learning Intent

After completing this CA, a student should be able to:

1. Recognize operating-system concepts embedded in unfamiliar real-world scenarios.
2. Decompose a complex system situation into relevant OS entities, resources and constraints.
3. Model processes, resources, memory, scheduling, synchronization or I/O relationships.
4. Apply appropriate OS algorithms and mechanisms.
5. Compare multiple possible solutions using measurable criteria.
6. Identify trade-offs and limitations.
7. Make a technically defensible engineering decision.
8. Support decisions with calculations, observations, experiments, documentation or reliable technical sources where appropriate.
9. Use AI as a supporting reasoning/corroboration tool without treating AI output as unquestioned truth.
10. Communicate the final decision clearly through technical reasoning.

---

# 4. Assessment Structure

| Component | Marks |
|---|---:|
| Problem identification and OS concept recognition | 2 |
| Problem modelling | 2 |
| Analysis of alternatives | 2 |
| Selection of appropriate mechanism | 2 |
| Engineering justification and communication | 2 |
| **Total** | **10** |

The five stages are mandatory for every challenge.

---

# 5. The Student Thinking Framework

For every assigned scenario, students should follow the following five-stage process.

## Stage 1 – Identify the OS Concept Involved

Students should first determine:

- What is the actual problem?
- Which OS subsystem is involved?
- Which OS concepts are relevant?
- What symptoms indicate the problem?
- Which concepts are irrelevant distractions?

Possible areas include:

- Process management
- CPU scheduling
- Threads
- Inter-process communication
- Synchronization
- Deadlocks
- Memory management
- Virtual memory
- File systems
- Disk scheduling
- I/O management
- System calls
- Protection and security
- Resource allocation
- Linux process/resource management

### Expected student output

A short statement such as:

> “The primary OS issue is CPU scheduling under an interactive workload. The key performance criteria are response time, turnaround time, fairness and throughput.”

Students should not merely write the name of an algorithm. They must explain **why the scenario represents that OS problem**.

---

# 6. Stage 2 – Model the Problem

Students should convert the scenario into an appropriate technical model.

Depending on the problem, modelling may involve:

### Process/Scheduling Problems

- Process table
- Arrival time
- Burst time
- Priority
- Gantt chart
- Process-state diagram

### Synchronization Problems

- Threads/processes
- Shared resources
- Critical sections
- Resource dependencies
- Lock ownership

### Deadlock Problems

- Resource Allocation Graph
- Wait-for graph
- Available/allocated/request matrices
- Safe/unsafe state representation

### Memory Problems

- Logical/physical address representation
- Memory partitions
- Page tables
- Page-reference strings
- Allocation maps

### File/I/O Problems

- File/directory structure
- Disk request queue
- Cylinder/request sequence
- I/O path
- Device/resource relationships

### Expected student output

A diagram, table, mathematical representation, trace, graph, or other appropriate model accompanied by a brief explanation.

---

# 7. Stage 3 – Analyze Alternatives

Students must consider **at least two plausible alternatives** wherever the scenario permits.

For each alternative, students should identify:

- How the mechanism works.
- Why it could solve the problem.
- Advantages.
- Disadvantages.
- Computational/resource implications.
- Situations where it is appropriate.
- Situations where it may fail or become inefficient.

Students should use appropriate performance measures.

Examples:

| OS Area | Possible Measures |
|---|---|
| CPU Scheduling | Waiting time, turnaround time, response time, throughput |
| Synchronization | Waiting time, contention, fairness, starvation |
| Memory | Page faults, hit ratio, utilization, fragmentation |
| Disk Scheduling | Head movement, response time, throughput |
| I/O | Latency, throughput, queue length |
| Processes/Threads | Creation overhead, context-switch overhead, scalability |
| File Systems | Access time, reliability, space utilization |
| Resource Allocation | Utilization, safety, deadlock risk |

The purpose is not to identify an algorithm that is universally “best”.

The purpose is to determine:

> **Best under the given constraints.**

---

# 8. Stage 4 – Select an Appropriate Mechanism

Students must make an explicit engineering decision.

The answer should include:

### Selected mechanism

For example:

> “Round Robin scheduling with a time quantum of 20 ms is selected.”

### Selection criteria

For example:

- Interactive response time
- Fairness
- Number of concurrent users
- CPU burst characteristics

### Constraints

For example:

- Limited CPU cores
- Large number of short-running tasks
- Interactive workload

### Expected outcome

For example:

> “The selected approach should improve response time and provide fair CPU access, although excessive context switching may occur if the quantum is too small.”

A statement such as **“Round Robin is best” without reasoning receives little credit.**

---

# 9. Stage 5 – Justify the Decision

This is the most important stage.

Students must defend their decision using evidence.

Evidence may include:

- Calculations
- Diagrams
- Traces
- Small programs
- Linux experiments
- Simulations
- Measurements
- Textbook principles
- Research papers
- Official technical documentation
- Verified AI-assisted analysis

Students should explicitly state:

1. Why the selected mechanism fits the scenario.
2. Why the rejected alternatives are less suitable.
3. What trade-offs are involved.
4. What assumptions were made.
5. What limitations remain.
6. Under what changed conditions they would choose another solution.

---

# 10. Recommended Student Response Template

Every submission should follow this structure.

## A. Scenario Understanding

Briefly restate the problem in your own words.

## B. OS Concept Identification

Identify the OS concept/subsystem involved and explain why.

## C. System Model

Represent the problem using an appropriate:

- diagram
- table
- graph
- trace
- mathematical model
- process/resource representation

## D. Constraints and Assumptions

Identify:

- System constraints
- Workload characteristics
- Resource limitations
- Performance requirements
- Assumptions

## E. Alternative Solutions

Analyze at least two suitable mechanisms.

## F. Comparative Analysis

Use appropriate calculations, experiments or evidence.

## G. Selected Solution

State the chosen mechanism.

## H. Engineering Justification

Explain why the selected solution is appropriate.

## I. Trade-offs and Limitations

Discuss what is sacrificed or potentially problematic.

## J. AI Corroboration

If AI tools were used:

- State what AI was used for.
- Record the important suggestion/output.
- Verify it using course concepts, experiments or reliable sources.
- Identify any incorrect or incomplete AI-generated claims.

## K. Final Engineering Decision

Conclude in 3–5 technically meaningful sentences.

---

# 11. Scenario-Based Challenge Bank

The following challenge bank can be used throughout the course. Faculty may assign one scenario to an individual student or team, or modify the parameters to create unique versions.

---

## CATEGORY A – OS Architecture and Resource Management

### Challenge A1 – The Overloaded Computer Lab

A computer laboratory has 60 machines. Students report that systems become extremely slow when browsers, IDEs, database tools and virtual machines are opened simultaneously.

### Students should investigate

- CPU utilization
- Memory utilization
- Process count
- Context switching
- Paging
- I/O activity
- Resource contention

### Core questions

1. Which OS resources are likely becoming bottlenecks?
2. How would you model the resource usage?
3. Which measurements should be collected?
4. How can CPU and memory bottlenecks be distinguished?
5. What OS-level mechanisms could improve responsiveness?

### Relevant concepts

Process management, CPU scheduling, memory management, virtual memory, I/O.

---

### Challenge A2 – Server with Uneven Resource Usage

A web server has 16 CPU cores, but monitoring shows that several cores are heavily loaded while others remain underutilized.

### Students should determine

- Whether scheduling/load distribution is responsible.
- Whether process/thread affinity is relevant.
- Whether workload characteristics explain the imbalance.
- Which OS mechanisms could improve utilization.

---

## CATEGORY B – PROCESS MANAGEMENT AND CPU SCHEDULING

### Challenge B1 – Interactive University Portal

A university portal serves:

- Login requests
- Database queries
- File uploads
- Background report generation

Students complain that the website becomes unresponsive while large reports are generated.

### Students should

1. Identify the scheduling problem.
2. Model the workload.
3. Compare FCFS, SJF/SRTF, Priority and Round Robin.
4. Calculate appropriate performance measures.
5. Recommend a scheduling strategy.

### Extension

Students should explain how the decision changes when the number of CPU cores increases.

---

### Challenge B2 – Gaming/Interactive Application

A system simultaneously runs:

- Game rendering
- Audio processing
- Network communication
- Background updates

The game occasionally becomes unresponsive.

Students must determine:

- Which processes/tasks require priority.
- Whether preemptive scheduling is appropriate.
- What fairness means in this environment.
- How scheduling decisions affect response time.

---

### Challenge B3 – Batch Processing Centre

A data centre executes 100 jobs overnight. Each job has a different CPU burst time.

The objective is to maximize throughput while minimizing average turnaround time.

Students must compare scheduling algorithms and recommend an approach.

---

### Challenge B4 – Starvation in a Priority Scheduler

A system uses priority scheduling. High-priority tasks continually arrive, and a low-priority process has remained in the ready queue for a long time.

Students must:

- Identify starvation.
- Model the scheduling behaviour.
- Compare starvation-prevention mechanisms.
- Evaluate aging.
- Recommend a solution.

---

## CATEGORY C – THREADS AND CONCURRENCY

### Challenge C1 – Multithreaded Banking Application

Multiple threads simultaneously update customer account balances.

Occasionally, the final balance is incorrect.

Students must:

- Identify the race condition.
- Locate the critical section.
- Model concurrent execution.
- Compare mutexes, semaphores and other appropriate mechanisms.
- Select a synchronization strategy.

---

### Challenge C2 – Ticket Booking System

Thousands of users attempt to book the last available seat simultaneously.

The system occasionally sells the same seat twice.

Students must determine:

- Shared resource.
- Critical section.
- Race condition.
- Required synchronization.
- Correctness requirements.
- Performance implications.

---

### Challenge C3 – Producer-Consumer System

A data acquisition system produces data faster than a processing thread can consume it.

Students must determine:

- Appropriate buffer structure.
- Synchronization mechanism.
- Conditions for blocking.
- Risk of buffer overflow.
- Suitable producer-consumer solution.

---

### Challenge C4 – Readers-Writers Database

A database receives many read requests and occasional write requests.

Students must determine whether:

- Reader preference
- Writer preference
- Fair scheduling

is most appropriate.

They must explicitly discuss starvation.

---

## CATEGORY D – DEADLOCK

### Challenge D1 – Four-Resource Deadlock

Four processes require combinations of:

- Printer
- Scanner
- Database lock
- Network resource

The system occasionally freezes.

Students must:

1. Model resource allocation.
2. Construct a Resource Allocation Graph.
3. Determine whether deadlock exists.
4. Identify the necessary conditions.
5. Compare prevention, avoidance and detection/recovery.
6. Recommend a strategy.

---

### Challenge D2 – Dining Philosophers in a Modern System

A simulation of five concurrent tasks repeatedly enters a shared resource.

The system occasionally reaches a state where no task can proceed.

Students must:

- Explain the deadlock.
- Model the dependencies.
- Propose at least two solutions.
- Compare correctness and efficiency.

---

### Challenge D3 – Deadlock vs Starvation

A system administrator reports that a process has been waiting for several minutes.

Students must determine whether the problem represents:

- Deadlock
- Starvation
- Indefinite postponement
- Scheduling delay

Students must provide evidence for the conclusion.

---

## CATEGORY E – MEMORY MANAGEMENT

### Challenge E1 – Fragmented Memory

A system has sufficient total free memory, but a large application cannot obtain a contiguous block.

Students must investigate:

- External fragmentation
- Internal fragmentation
- Allocation strategies
- Compaction

and recommend an approach.

---

### Challenge E2 – Memory Allocation Strategy

A system receives memory requests of different sizes.

Students must compare:

- First Fit
- Best Fit
- Worst Fit

using the same request sequence.

They should calculate:

- Allocation efficiency
- Fragmentation
- Remaining free space

and recommend a strategy.

---

### Challenge E3 – Unexpected Memory Consumption

A program's memory usage continuously increases even though its workload remains constant.

Students must determine whether the problem may be related to:

- Memory leak
- Fragmentation
- Excessive process creation
- Caching
- Virtual memory behaviour

Students must propose an investigation plan.

---

## CATEGORY F – VIRTUAL MEMORY

### Challenge F1 – High Page Fault Rate

A computer has 16 GB RAM, but a large application experiences a very high page-fault rate.

Students must investigate:

- Locality
- Working set
- Page replacement
- Thrashing
- Memory pressure

and recommend corrective action.

---

### Challenge F2 – Page Replacement Decision

Given a page-reference string, students must compare:

- FIFO
- LRU
- Optimal

Students should determine:

- Number of page faults
- Hit ratio
- Relative behaviour

Then explain why the theoretically optimal algorithm is not normally directly implementable.

---

### Challenge F3 – Thrashing in a Multi-Programmed System

A system runs many applications simultaneously. CPU utilization decreases while disk activity increases.

Students must determine whether the system is experiencing thrashing and recommend mechanisms to control it.

---

## CATEGORY G – FILE SYSTEMS

### Challenge G1 – University File Server

A university stores:

- Student documents
- Faculty research data
- Examination material
- Administrative records

Students must recommend file-system design considerations involving:

- Organization
- Access control
- Reliability
- Backup
- Security
- Performance

---

### Challenge G2 – File System Failure

A system crashes while files are being written.

After reboot, some files are inconsistent.

Students must investigate:

- Atomicity
- Journaling
- File-system consistency
- Recovery
- Reliability mechanisms

---

### Challenge G3 – Millions of Small Files

A server stores millions of small files.

Directory access has become slow.

Students must investigate how file-system organization and metadata management influence performance.

---

## CATEGORY H – DISK SCHEDULING AND STORAGE

### Challenge H1 – Hospital Storage Server

A hospital server receives disk requests from:

- Patient records
- Imaging systems
- Database services
- Backup processes

Students must compare:

- FCFS
- SSTF
- SCAN
- C-SCAN
- LOOK/C-LOOK

and recommend an appropriate strategy.

---

### Challenge H2 – CCTV Storage System

A surveillance system continuously writes video data to storage while users occasionally request historical recordings.

Students must reason about:

- Sequential vs random I/O
- Throughput
- Latency
- Scheduling
- Storage capacity

---

### Challenge H3 – SSD vs HDD

A system currently uses HDD storage but is being considered for migration to SSD.

Students must explain:

- Which traditional disk scheduling assumptions change.
- Why seek-time optimization is different.
- Which OS/storage decisions remain relevant.

---

## CATEGORY I – I/O MANAGEMENT

### Challenge I1 – Slow Printer Queue

An organization has multiple users submitting large print jobs.

Students must design a suitable OS-level queueing strategy.

---

### Challenge I2 – High I/O Wait

A Linux server shows:

- Low CPU utilization
- High I/O wait
- Large request queues

Students must identify the likely bottleneck and develop an investigation plan.

---

### Challenge I3 – Real-Time Sensor System

A system receives sensor data continuously and must process it with minimal delay.

Students must determine:

- Appropriate buffering.
- Interrupt vs polling considerations.
- Scheduling requirements.
- Priority considerations.
- Failure-handling mechanisms.

---

## CATEGORY J – LINUX AND SYSTEMS ENGINEERING

### Challenge J1 – Linux Process Investigation

Students receive a Linux system where an application appears to consume excessive CPU.

They must use appropriate Linux tools to:

- Identify the process.
- Examine CPU consumption.
- Inspect process state.
- Investigate threads.
- Formulate a diagnosis.

---

### Challenge J2 – Zombie Process Investigation

A Linux system accumulates zombie processes.

Students must:

- Explain the process lifecycle.
- Determine why zombies occur.
- Identify the parent-child relationship.
- Recommend corrective action.

---

### Challenge J3 – Runaway Process

A process continually creates child processes.

Students must investigate:

- Process creation
- Resource exhaustion
- Process limits
- System stability
- Appropriate mitigation

---

### Challenge J4 – Build a Mini Shell

Students are asked to design a shell supporting a selected set of commands.

They should reason about:

- Process creation
- Command execution
- Parent-child relationships
- Waiting
- Redirection
- Pipelines

This can be used as a bridge toward the later Linux Systems Engineering CA.

---

# 12. Integrated Scenario Challenges

These challenges combine multiple OS concepts and are particularly suitable for stronger students.

## Integrated Challenge I1 – E-Commerce Platform Under Load

An e-commerce server experiences:

- Slow response
- High CPU usage
- Memory pressure
- Many concurrent requests
- Increased disk activity

Students must determine whether there is one bottleneck or multiple interacting bottlenecks.

### Expected analysis

Students should examine:

- Processes
- Threads
- CPU scheduling
- Synchronization
- Memory
- Virtual memory
- I/O

The final solution should prioritize interventions rather than simply listing OS concepts.

---

## Integrated Challenge I2 – Cloud Server Resource Contention

Several applications run on a shared server.

One application consumes excessive CPU and memory, affecting all others.

Students must recommend:

- Scheduling considerations
- Resource isolation
- Memory controls
- Process limits
- Monitoring mechanisms

---

## Integrated Challenge I3 – Online Examination System

An online examination system simultaneously handles:

- Thousands of student logins
- Authentication
- Question retrieval
- Answer submission
- Autosave
- Database access
- Result processing

Students must identify OS-level concerns involving:

- Concurrency
- Scheduling
- Memory
- I/O
- Synchronization
- Reliability

---

## Integrated Challenge I4 – Autonomous Vehicle Computing Platform

A computing platform simultaneously executes:

- Sensor processing
- Navigation
- Object detection
- Logging
- Communication

Students must determine which tasks should receive higher priority and discuss the consequences of scheduling failures.

---

# 13. Open-Ended "What Would You Do?" Challenges

These are deliberately under-specified.

Students must identify the missing information before making a decision.

### Example

> A server is slow. The administrator wants to change the CPU scheduling algorithm. Would you approve the change?

Students should respond:

> “Insufficient information.”

They must then specify what should be measured before changing the scheduler.

This assesses genuine **systems thinking**.

Possible missing information:

- CPU utilization
- Process characteristics
- Arrival patterns
- CPU burst distribution
- I/O wait
- Number of cores
- Context-switch frequency
- Response-time requirements

This category is particularly useful for distinguishing students who understand OS engineering from students who merely memorize algorithms.

---

# 14. AI-Assisted Reasoning – Permitted but Must Be Corroborated

AI may be used as a **reasoning assistant**, not as the final authority.

Students may use Generative AI to:

- Generate alternative hypotheses.
- Explain unfamiliar terminology.
- Suggest possible mechanisms.
- Generate test scenarios.
- Critique an initial solution.
- Identify potential edge cases.
- Help visualize system behaviour.

However, students must independently verify AI-generated information.

## Required AI Disclosure

Students should include:

### AI Tool Used
Example:

> ChatGPT / Gemini / Claude / other approved tool

### Purpose

> Used to generate possible explanations for high page-fault behaviour.

### AI Suggestion

Briefly summarize the relevant suggestion.

### Verification

Explain how the suggestion was checked using:

- OS theory
- Calculation
- Linux experiment
- Documentation
- Research source
- Instructor-provided material

### Reflection

State whether the AI output was:

- Correct
- Partially correct
- Incorrect
- Incomplete

and explain why.

The objective is:

> **AI-assisted reasoning + human verification**

rather than:

> **AI-generated answer submission**

---

# 15. Evidence-Based Decision Making

Students should be encouraged to distinguish between:

### Claim

> “Round Robin will provide better responsiveness.”

### Evidence

> “For the given workload and time quantum, the average response time was X ms compared with Y ms under FCFS.”

### Interpretation

> “The reduction occurs because newly arrived interactive processes receive CPU access without waiting for the long background process to complete.”

### Decision

> “Therefore, Round Robin is more appropriate for this workload.”

This four-step pattern should become habitual.

---

# 16. Expected Depth by Student Performance Level

| Performance Level | Expected Behaviour |
|---|---|
| **Basic** | Identifies the correct OS concept and explains the relevant theory. |
| **Developing** | Models the problem and compares alternative mechanisms. |
| **Proficient** | Uses evidence/calculations to select an appropriate solution. |
| **Advanced** | Identifies trade-offs, limitations, edge cases and changing conditions. |
| **Exceptional** | Challenges assumptions, proposes improvements, validates experimentally and develops an original engineering perspective. |

---

# 17. Assessment Rubric – 10 Marks

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| **1. OS Concept Identification** | Concept not identified/incorrect | Correct concept but weak explanation | Correct concept with clear contextual reasoning |
| **2. Problem Modelling** | No/incorrect model | Partially appropriate model | Appropriate and clearly explained model |
| **3. Alternative Analysis** | No meaningful alternatives | Alternatives listed with limited comparison | Alternatives critically compared using relevant criteria |
| **4. Mechanism Selection** | Inappropriate/no decision | Reasonable decision with weak basis | Appropriate decision supported by constraints/evidence |
| **5. Justification & Communication** | Unsupported conclusion | Basic justification | Clear evidence-based engineering justification |
| **TOTAL** | | | **10** |

---

# 18. Faculty Implementation Model

The instructor can conduct the CA in any of the following formats.

## Model A – Individual Challenge

Each student receives a different scenario.

**Recommended for:** Large classes where individual attainment needs to be measured.

## Model B – Team Challenge

Teams of 3–4 students solve one complex scenario.

**Recommended for:** Real-world exposure and collaborative problem solving.

## Model C – Challenge Carousel

Students solve multiple short scenarios during a scheduled session.

Example:

- Scenario 1 – Scheduling
- Scenario 2 – Deadlock
- Scenario 3 – Memory
- Scenario 4 – I/O

Each student must reason through all four.

## Model D – Progressive Challenge

Students receive a scenario in stages.

### Stage 1

Identify the problem.

### Stage 2

New evidence is revealed.

### Stage 3

Students revise their model.

### Stage 4

Additional constraints are introduced.

### Stage 5

Students defend the final decision.

This is arguably the strongest model because it tests whether students can **adapt their reasoning when new evidence changes the problem**.

---

# 19. Recommended Progressive Challenge Example

## Scenario: University Cloud Server

### Round 1

> Users report slow response times.

Students identify what they need to measure.

### Round 2

The following information is provided:

- CPU utilization: 95%
- Memory utilization: 60%
- Disk utilization: 30%

Students revise their diagnosis.

### Round 3

Process information is provided:

- One background process consumes 70% CPU.
- Several interactive tasks are waiting.

Students analyze scheduling.

### Round 4

The background process is found to be CPU-bound.

Students compare scheduling alternatives.

### Round 5

The system administrator proposes increasing CPU priority for the background process.

Students must decide whether to approve or reject the proposal.

This format tests **reasoning rather than recall**.

---

# 20. Recommended Challenge Difficulty Distribution

For a class-level CA, the challenge bank can be distributed as follows:

| Difficulty | Approx. Weight | Challenge Type |
|---|---:|---|
| **Level 1 – Foundational** | 20% | Single OS concept |
| **Level 2 – Analytical** | 30% | Concept + comparison |
| **Level 3 – Engineering** | 30% | Multiple constraints + decision |
| **Level 4 – Research/Innovation** | 20% | Open-ended/investigative |

This prevents the CA from becoming either too easy or excessively research-heavy.

---

# 21. Relationship with the OS Course Outcomes

| CA Activity | Primary COs | Secondary COs |
|---|---|---|
| OS architecture/resource scenarios | **CO1** | CO4, CO5 |
| CPU scheduling challenges | **CO2** | CO1, CO6 |
| Concurrency challenges | **CO3** | CO2, CO6 |
| Deadlock challenges | **CO3** | CO2 |
| Memory challenges | **CO4** | CO1, CO6 |
| File-system challenges | **CO5** | CO1, CO6 |
| Disk/I/O challenges | **CO5** | CO2, CO4, CO6 |
| Linux investigation | **CO6** | CO2, CO3, CO4, CO5 |
| Integrated scenarios | **CO2–CO6** | CO1 |

---

# 22. Relationship with Dual-Dimension Pedagogy

| Dual Dimension | How CA-1 Develops It |
|---|---|
| **Critical Thinking** | Students challenge assumptions, identify hidden OS problems, compare alternatives, interpret evidence and defend decisions. |
| **Research Experience** | Students investigate technical evidence, formulate hypotheses, consult sources and validate claims through experiments or analysis. |
| **Innovation & Professional Development** | Students consider alternative engineering solutions and make context-dependent technical decisions. |
| **Real World Exposure** | Scenarios are derived from servers, cloud systems, banking, healthcare, e-commerce, Linux systems and other real environments. |
| **Youth Development** | Indirectly supported through responsible decision-making, collaboration and awareness of the societal consequences of computing systems. |

---

# 23. Student Submission Checklist

Before submitting, students should verify:

- [ ] I identified the actual OS problem.
- [ ] I explained the relevant OS concept.
- [ ] I created an appropriate system model.
- [ ] I identified constraints and assumptions.
- [ ] I analyzed at least two alternatives where applicable.
- [ ] I used appropriate performance measures.
- [ ] I selected one mechanism.
- [ ] I justified my decision using evidence.
- [ ] I discussed trade-offs and limitations.
- [ ] I considered what would change my decision.
- [ ] I disclosed AI usage, if applicable.
- [ ] I independently verified AI-generated claims.
- [ ] My final conclusion is technically defensible.

---

# 24. What Students Should NOT Do

The following approaches should not receive full credit:

### 1. Definition Dump

Writing several pages of textbook definitions without connecting them to the scenario.

### 2. Algorithm Listing

Listing FCFS, SJF, Round Robin, etc. without comparing their suitability.

### 3. Unsupported Decision

Writing:

> “Round Robin is the best algorithm.”

without evidence.

### 4. AI Copy-Paste

Submitting an AI-generated explanation without verification or understanding.

### 5. One-Solution Thinking

Assuming that every OS problem has one universally optimal solution.

### 6. Ignoring Constraints

Selecting an algorithm without considering workload, hardware, latency, fairness, security or resource limitations.

---

# 25. Expected Final Student Output

A strong submission should ultimately resemble an engineering decision document:

> **Problem:** Interactive applications experience unacceptable response time because CPU resources are dominated by long-running background processes.
>
> **OS Concept:** CPU scheduling and process prioritization.
>
> **Model:** Process arrival/burst characteristics and scheduling timeline.
>
> **Alternatives:** FCFS, Priority Scheduling and Round Robin.
>
> **Analysis:** Compare response time, turnaround time, fairness and context-switch overhead.
>
> **Decision:** Select an appropriate scheduling mechanism for the stated workload.
>
> **Justification:** The selected mechanism provides the required response-time/fairness characteristics with acceptable overhead.
>
> **Trade-off:** Increased preemption may increase context-switch overhead.
>
> **Condition for Reconsideration:** If the workload becomes predominantly batch-oriented, a different scheduling policy may become more appropriate.

This is the level of reasoning expected from students completing CA-1.

---

# 26. Faculty Question Design Principles

When creating new scenarios, faculty should ensure that:

1. The scenario has a genuine OS problem.
2. More than one solution is plausible.
3. There is no trivially obvious answer.
4. Students need to make assumptions explicit.
5. At least one trade-off exists.
6. Evidence can be collected or calculated.
7. The scenario can be connected to one or more COs.
8. The scenario encourages reasoning rather than memorization.
9. Strong students have opportunities to propose better alternatives.
10. AI cannot simply provide a complete answer without student verification.

---

# 27. Suggested Faculty Question Template

For future scenario generation, use:

> **Scenario:** [Real-world system situation]
>
> **Observed Problem:** [Symptoms]
>
> **Constraints:** [Hardware/workload/performance requirements]
>
> **Available Information:** [Data provided to students]
>
> **Student Tasks:**
>
> 1. Identify the OS concept involved.
> 2. Model the problem.
> 3. Identify assumptions and constraints.
> 4. Analyze at least two alternatives.
> 5. Select an appropriate OS mechanism.
> 6. Support the decision using calculations, experiments or technical evidence.
> 7. Discuss trade-offs and limitations.
> 8. Explain how the decision would change if one major constraint changed.
> 9. Use AI, if desired, to generate/corroborate reasoning and document the verification.
> 10. Present the final engineering decision.

---

# 28. The Core Philosophy of CA-1

The Systems Thinking Challenge should establish a culture that continues through the remaining Operating Systems assessments.

Students should gradually learn that:

> **An Operating System is not a collection of algorithms to memorize.**

It is a system of interacting mechanisms in which every engineering decision involves trade-offs.

Therefore, students should repeatedly ask:

### “What is happening?”

↓

### “Why is it happening?”

↓

### “How can I model it?”

↓

### “What alternatives do I have?”

↓

### “Which solution fits this context?”

↓

### “What evidence supports my decision?”

↓

### “What happens if the conditions change?”

That mindset is the principal outcome of the **OS Systems Thinking Challenge**.

---

# 29. CA-1 at a Glance

| Item | Description |
|---|---|
| **CA Component** | OS Systems Thinking Challenge |
| **Weightage** | 10 Marks |
| **Nature** | Scenario-based / analytical / decision-oriented |
| **Mode** | Individual, team or progressive challenge |
| **Primary Dimensions** | Critical Thinking + Research Experience |
| **Supporting Dimensions** | Innovation & Professional Development + Real World Exposure |
| **Primary COs** | CO1–CO5 depending on scenario |
| **Evidence** | Models, calculations, experiments, technical sources, reasoning |
| **AI Usage** | Permitted as an assistant; mandatory verification and disclosure |
| **Core Skill** | Evidence-based OS engineering decision making |
| **Final Output** | Defensible technical decision with alternatives, trade-offs and evidence |
