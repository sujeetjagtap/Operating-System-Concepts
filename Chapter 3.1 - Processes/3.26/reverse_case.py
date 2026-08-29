#!/usr/bin/env python3
"""Exchange a message between two processes using two ordinary pipes."""
import multiprocessing as mp
import os

INITIAL_MESSAGE = "This iS a meSSaGe"

def child(initial_r, initial_w, final_r, final_w):
    os.close(initial_w)
    os.close(final_r)
    with os.fdopen(initial_r, "r") as source:
        message = source.read()
    altered = message.swapcase()
    with os.fdopen(final_w, "w") as dest:
        dest.write(altered)

def main():
    initial_r, initial_w = os.pipe()
    final_r, final_w = os.pipe()
    p = mp.Process(target=child, args=(initial_r, initial_w, final_r, final_w))
    p.start()
    os.close(initial_r)
    os.close(final_w)
    with os.fdopen(initial_w, "w") as pipe:
        pipe.write(INITIAL_MESSAGE)
    p.join()
    with os.fdopen(final_r, "r") as pipe:
        altered = pipe.read()
    print(f"Child terminated with status {p.exitcode}")
    print("altered message:")
    print(altered)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
