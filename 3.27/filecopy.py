#!/usr/bin/env python3
"""Copy a file through an ordinary pipe between parent and child processes."""
import argparse
import multiprocessing as mp
import os

BUFFER_SIZE = 25

def child(read_fd, write_fd, output_path):
    os.close(write_fd)
    with os.fdopen(read_fd, "rb") as pipe, open(output_path, "wb") as out:
        while True:
            data = pipe.read(BUFFER_SIZE)
            if not data:
                break
            out.write(data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args()

    read_fd, write_fd = os.pipe()
    p = mp.Process(target=child, args=(read_fd, write_fd, args.destination))
    p.start()
    os.close(read_fd)
    try:
        with open(args.source, "rb") as source, os.fdopen(write_fd, "wb") as pipe:
            while True:
                data = source.read(BUFFER_SIZE)
                if not data:
                    break
                pipe.write(data)
    finally:
        p.join()
    return p.exitcode

if __name__ == "__main__":
    raise SystemExit(main())
