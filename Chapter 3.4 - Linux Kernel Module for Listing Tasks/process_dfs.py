#!/usr/bin/env python3
"""User-space analogue of DFS over the Linux process tree."""
import os
from collections import defaultdict

def process_info(pid):
    try:
        with open(f"/proc/{pid}/stat") as f:
            stat = f.read()
        l, r = stat.find("("), stat.rfind(")")
        comm = stat[l+1:r]
        fields = stat[r+2:].split()
        state = fields[0]
        ppid = int(fields[1])
        return comm, ppid, state
    except (FileNotFoundError, PermissionError, ValueError, IndexError):
        return None

def main():
    children = defaultdict(list)
    info = {}
    for name in os.listdir("/proc"):
        if not name.isdigit():
            continue
        pid = int(name)
        data = process_info(pid)
        if data:
            info[pid] = data
            children[data[1]].append(pid)

    def dfs(pid):
        data = info.get(pid)
        if not data: return
        comm, ppid, _ = data
        print(f"command = [{comm}] --- pid = [{pid}] --- ppid = [{ppid}]")
        for child in sorted(children.get(pid, [])):
            dfs(child)

    print("process_dfs module loaded!")
    dfs(1)
    print("process_dfs module removed!")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
