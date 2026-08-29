# PID management with a bitmap

## Theory

A bitmap records whether each PID in a fixed range is free or allocated. Allocation scans for a zero bit, marks it used and returns the PID; release marks the PID free. A lock makes the Python API safe for concurrent callers.

## Question

> Implement a PID manager with allocate_map(), allocate_pid() and release_pid() using a bitmap for PIDs 300–5000.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
