# Process creation, pipes and execution timing

## Theory

A parent creates a child, the child records a start timestamp and executes a command, and the parent waits for completion and calculates elapsed time. One version communicates the timestamp through a pipe; the other uses shared memory.

## Question

> Measure how long a command takes to execute in a child process, communicating the start time to the parent using a pipe and, separately, shared memory.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
