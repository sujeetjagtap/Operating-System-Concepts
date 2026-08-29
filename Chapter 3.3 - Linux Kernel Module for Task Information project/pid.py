#!/usr/bin/env python3
"""User-space replacement for the /proc/pid kernel module.

Usage:
    python pid.py PID
"""
import argparse
import os

def get_task_info(pid):
    try:
        with open(f"/proc/{pid}/stat") as f:
            stat = f.read()
        l, r = stat.find("("), stat.rfind(")")
        command = stat[l+1:r]
        state = stat[r+2]
        return command, pid, state
    except (FileNotFoundError, PermissionError, ValueError):
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pid", type=int)
    args = parser.parse_args()
    data = get_task_info(args.pid)
    if data is None:
        print("The given pid is not valid")
        return 1
    command, pid, state = data
    print(f"command = [{command}] -- pid = [{pid}] -- state = [{state}]")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
