#!/usr/bin/env python3
"""Approximate pi using Monte Carlo sampling in a worker thread."""
import argparse
import math
import random
import threading

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int)
    count = parser.parse_args().count
    if count <= 0:
        parser.error("count must be positive")

    result = {"inside": 0, "total": 0}
    def generate_points():
        inside = 0
        for _ in range(count):
            x = random.random()
            y = random.random()
            if math.hypot(x, y) <= 1:
                inside += 1
        result["inside"] = inside
        result["total"] = count

    t = threading.Thread(target=generate_points)
    t.start()
    t.join()
    print(f"{4 * result['inside'] / result['total']:.10f}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
