# Pipes for file transfer

## Theory

A pipe is a unidirectional byte stream between processes. The parent reads a source file in fixed-size chunks and writes them to the pipe; the child reads the pipe and writes the destination file.

## Question

> Copy a file by sending its contents through an ordinary pipe from a parent process to a child process.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
