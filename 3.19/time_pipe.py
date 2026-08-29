#!/usr/bin/env python3
"""Measure command execution time using a parent/child pipe."""
import argparse
import multiprocessing as mp
import os
import subprocess
import time

def child(command, send_conn):
    start = time.time()
    send_conn.send(start)
    send_conn.close()
    result = subprocess.run(command)
    os._exit(result.returncode)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="+")
    args = parser.parse_args()

    recv, send = mp.Pipe(duplex=False)
    p = mp.Process(target=child, args=(args.command, send))
    p.start()
    send.close()
    start = recv.recv()
    p.join()
    finish = time.time()
    print(f"Child terminated with status {p.exitcode}")
    print(f"The command took {finish - start:.6f} seconds to execute")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
