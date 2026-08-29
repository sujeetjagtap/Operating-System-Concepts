#!/usr/bin/env python3
"""Generate the Collatz sequence in a child process."""
import argparse
import multiprocessing as mp

def worker(start):
    sequence = []
    while start != 1:
        sequence.append(start)
        start = start // 2 if start % 2 == 0 else start * 3 + 1
    sequence.append(1)
    print(" ".join(map(str, sequence)), flush=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("starting_number", type=int)
    n = parser.parse_args().starting_number
    if n <= 0:
        parser.error("The starting number must be positive!")
    p = mp.Process(target=worker, args=(n,))
    p.start()
    p.join()
    print(f"Child process terminated with status {p.exitcode}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
