# Mutual exclusion and finite resources

## Theory

A finite resource pool is shared by multiple consumers. A mutex protects the check-and-update operation so two threads cannot allocate the same resources simultaneously. A requester waits until enough resources are available, then returns them.

## Question

> Implement a thread-safe finite resource manager with five resources that allocates resources to concurrent requests and returns them after use.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
