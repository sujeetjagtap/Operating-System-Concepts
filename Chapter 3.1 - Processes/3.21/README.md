# Process creation and the Collatz sequence

## Theory

The Collatz sequence repeatedly maps an even n to n/2 and an odd n to 3n+1 until 1. The original C program performs the computation in a child process and the parent waits for it.

## Question

> Create a child process that generates and prints the Collatz sequence for a supplied starting number while the parent waits for termination.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
