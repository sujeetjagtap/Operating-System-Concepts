#!/usr/bin/env python3
"""Validate a 9x9 Sudoku solution with 27 worker threads."""
import argparse
import threading

def read_matrix(path):
    with open(path) as f:
        values = [int(x) for x in f.read().split()]
    if len(values) != 81:
        raise ValueError("Sudoku file must contain exactly 81 integers")
    if any(x < 1 or x > 9 for x in values):
        raise ValueError("Sudoku values must be in the range 1..9")
    return [values[i:i+9] for i in range(0, 81, 9)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    mat = read_matrix(args.file)
    valid = {"value": True}
    lock = threading.Lock()

    def mark_invalid():
        with lock:
            valid["value"] = False

    def check(values):
        if set(values) != set(range(1, 10)):
            mark_invalid()

    threads = []
    for i in range(9):
        threads.append(threading.Thread(target=check, args=(mat[i],)))
    for j in range(9):
        threads.append(threading.Thread(target=check, args=([mat[i][j] for i in range(9)],)))
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square = [mat[i][j] for i in range(r, r+3) for j in range(c, c+3)]
            threads.append(threading.Thread(target=check, args=(square,)))

    for t in threads: t.start()
    for t in threads: t.join()
    print("Valid solution!" if valid["value"] else "Wrong solution!")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
