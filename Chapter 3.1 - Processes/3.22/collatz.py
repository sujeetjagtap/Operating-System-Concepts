#!/usr/bin/env python3
"""Compute Collatz in a child and return the sequence through shared memory."""
import argparse
import multiprocessing as mp
from multiprocessing import shared_memory
import struct

MAX_SEQUENCE_LENGTH = 100

def worker(number, shm_name):
    shm = shared_memory.SharedMemory(name=shm_name)
    try:
        values = []
        while number != 1 and len(values) < MAX_SEQUENCE_LENGTH - 1:
            values.append(number)
            number = number // 2 if number % 2 == 0 else number * 3 + 1
        values.append(number)
        for i, value in enumerate(values):
            struct.pack_into("i", shm.buf, i * 4, value)
        struct.pack_into("i", shm.buf, len(values) * 4, 0)
    finally:
        shm.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int)
    number = parser.parse_args().number
    if number <= 0:
        parser.error("The starting number must be positive!")

    shm = shared_memory.SharedMemory(create=True, size=MAX_SEQUENCE_LENGTH * 4)
    try:
        p = mp.Process(target=worker, args=(number, shm.name))
        p.start()
        p.join()
        print(f"Child process terminated with status {p.exitcode}")
        values = []
        for i in range(MAX_SEQUENCE_LENGTH):
            value = struct.unpack_from("i", shm.buf, i * 4)[0]
            if value == 0:
                break
            values.append(value)
        print(" ".join(map(str, values)))
    finally:
        shm.close()
        shm.unlink()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
