# Parallel merge sort

## Theory

Merge sort divides an array into two halves, recursively sorts each half and merges the sorted results. The C program creates threads down to a fixed depth. The Python version mirrors this structure with threading and falls back to sorted() for small partitions.

## Question

> Implement a merge-sort application that uses multiple threads up to a fixed recursion depth and verifies the resulting array is sorted.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
