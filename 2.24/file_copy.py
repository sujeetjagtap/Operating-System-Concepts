#!/usr/bin/env python3
"""Copy a file using low-level OS file descriptors, mirroring 2.24/file_copy.c."""
import os

def main():
    input_file = input("Give input file name:\n").strip()
    output_file = input("Give output file name:\n").strip()

    try:
        input_fd = os.open(input_file, os.O_RDONLY)
    except OSError as exc:
        print(f"Error opening the input file: {exc}")
        return 0

    try:
        output_fd = os.open(output_file, os.O_CREAT | os.O_RDWR, 0o700)
    except OSError as exc:
        os.close(input_fd)
        print(f"Error opening the output file: {exc}")
        return 0

    try:
        size = os.stat(input_file).st_size
        data = os.read(input_fd, size)
        if len(data) != size:
            print("Reading error")
            return 1
        written = os.write(output_fd, data)
        if written != len(data):
            print("Writing error")
            return 1
        print("Contents of the input file successfully copied to the output file!")
    finally:
        os.close(input_fd)
        os.close(output_fd)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
