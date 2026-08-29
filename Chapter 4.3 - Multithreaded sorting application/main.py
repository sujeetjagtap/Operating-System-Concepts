#!/usr/bin/env python3
"""Multithreaded merge sort corresponding to the C implementation."""
import argparse
import random
import threading

MAX_DEPTH = 4
MIN_PARTITION_SIZE = 128

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

def sort_multithread(array, depth):
    if len(array) < 2:
        return array
    if depth == 0 or len(array) < MIN_PARTITION_SIZE:
        return sorted(array)

    mid = len(array) // 2
    holder = {}
    def worker():
        holder["left"] = sort_multithread(array[:mid], depth - 1)
    t = threading.Thread(target=worker)
    t.start()
    right = sort_multithread(array[mid:], depth - 1)
    t.join()
    return merge(holder["left"], right)

def sort(array):
    return sort_multithread(array, MAX_DEPTH)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args()
    if args.n < 0:
        parser.error("n must not be negative")
    array = [random.randrange(100000) for _ in range(args.n)]
    array = sort(array)
    if array != sorted(array):
        print("The array is not sorted!...:(")
        return 1
    print("The sorted array is:")
    for i, value in enumerate(array):
        print(f"{value:5d}", end="\n" if i % 10 == 9 else " ")
    print()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
