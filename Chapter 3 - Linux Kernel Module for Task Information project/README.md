# Process information through /proc

## Theory

The original module accepts a PID through a /proc entry and reports task information from the kernel's task_struct. The Python version reads /proc/PID/stat directly and prints command, PID and state.

## Question

> Create a /proc-based interface that accepts a PID and reports the corresponding task's command, PID and state.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
