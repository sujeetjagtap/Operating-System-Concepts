#!/usr/bin/env python3
"""User-space analogue of the kernel linked-list Collatz module."""
import argparse
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: "Node | None" = None

def build_collatz(start):
    head = tail = None
    number = start
    while number > 1:
        node = Node(number)
        if head is None: head = node
        else: tail.next = node
        tail = node
        number = number // 2 if number % 2 == 0 else number * 3 + 1
    node = Node(1)
    if head is None: head = node
    else: tail.next = node
    return head

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start", nargs="?", type=int, default=25)
    start = parser.parse_args().start
    if start <= 0:
        print("Error: the starting number must be an integer greater than 0!")
        return 0
    print("collatz module loaded!")
    node = build_collatz(start)
    while node:
        print(node.value)
        node = node.next
    print("collatz module removed!")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
