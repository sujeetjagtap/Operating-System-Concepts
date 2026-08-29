# Process lists and process trees

## Theory

Linux maintains process/task relationships. Linear traversal visits tasks in PID order, while depth-first traversal recursively visits a process followed by its descendants. The Python versions inspect Linux /proc to provide a user-space analogue.

## Question

> Implement task traversal in two ways: linear iteration over active processes and depth-first traversal of the process tree.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
