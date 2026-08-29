# Shared memory between processes

## Theory

Processes can communicate by mapping a common memory region. The child computes the Collatz sequence and stores values in shared memory; the parent waits and reads the sequence. Python uses multiprocessing.shared_memory for the same IPC concept.

## Question

> Generate the Collatz sequence in a child process, store it in shared memory and print it from the parent process.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
