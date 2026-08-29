# The /proc filesystem and kernel modules

## Theory

The original program is a Linux kernel module that exposes elapsed time through /proc and uses jiffies. Python cannot implement a loadable kernel module or create a kernel-owned /proc entry, so seconds.py is a user-space simulation using a monotonic clock.

## Question

> Create a Linux /proc-based facility that reports the number of seconds elapsed since it was loaded.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
