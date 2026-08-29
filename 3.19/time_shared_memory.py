#!/usr/bin/env python3
"""Measure command execution time using multiprocessing shared memory."""
import argparse
import multiprocessing as mp
from multiprocessing import shared_memory
import struct
import subprocess
import time

def child(command, shm_name):
    shm = shared_memory.SharedMemory(name=shm_name)
    try:
        struct.pack_into("d", shm.buf, 0, time.time())
        result = subprocess.run(command)
        return result.returncode
    finally:
        shm.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="+")
    args = parser.parse_args()

    shm = shared_memory.SharedMemory(create=True, size=8)
    try:
        p = mp.Process(target=child, args=(args.command, shm.name))
        p.start()
        p.join()
        start = struct.unpack_from("d", shm.buf, 0)[0]
        finish = time.time()
        print(f"Child terminated with status {p.exitcode}")
        print(f"The command took {finish - start:.6f} seconds to execute")
    finally:
        shm.close()
        shm.unlink()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
