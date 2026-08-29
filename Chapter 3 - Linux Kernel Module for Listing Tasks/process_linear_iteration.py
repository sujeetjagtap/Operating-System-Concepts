#!/usr/bin/env python3
"""User-space analogue of linear process traversal using Linux /proc."""
import os

def main():
    print("linear_iteration module added!")
    pids = sorted((int(name) for name in os.listdir("/proc") if name.isdigit()))
    for pid in pids:
        try:
            with open(f"/proc/{pid}/stat") as f:
                stat = f.read()
            l = stat.find("("); r = stat.rfind(")")
            comm = stat[l+1:r]
            state = stat[r+2]
            print(f"command = [{comm}] --- pid = [{pid}] --- state = [{state}]")
        except (FileNotFoundError, PermissionError, IndexError):
            continue
    print("linear_iteration module removed!")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
