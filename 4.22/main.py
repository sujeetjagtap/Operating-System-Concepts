#!/usr/bin/env python3
"""Compute average, minimum and maximum concurrently using three threads."""
import argparse
import threading

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="+", type=int)
    numbers = parser.parse_args().numbers

    results = {}
    def average():
        results["average"] = sum(numbers) / len(numbers)
    def minimum():
        results["minimum"] = min(numbers)
    def maximum():
        results["maximum"] = max(numbers)

    threads = [threading.Thread(target=average),
               threading.Thread(target=minimum),
               threading.Thread(target=maximum)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"Average: {results['average']:.2f}")
    print(f"Minimum: {results['minimum']}")
    print(f"Maximum: {results['maximum']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
