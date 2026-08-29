# Shells, processes, redirection and pipes

## Theory

A shell reads a command, parses arguments, starts a new process and optionally connects processes with pipes or redirects standard input/output to files. The Python implementation uses shlex and subprocess to reproduce the educational shell behavior.

## Question

> Implement a simple UNIX shell that executes commands in child processes and supports command history (!!), one pipe, input/output redirection and background execution.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
