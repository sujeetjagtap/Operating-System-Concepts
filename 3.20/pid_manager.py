#!/usr/bin/env python3
"""PID manager using a bitmap, based on the 3.20 C exercise."""
import threading

MIN_PID = 300
MAX_PID = 5000

class PIDManager:
    def __init__(self, min_pid=MIN_PID, max_pid=MAX_PID):
        self.min_pid = min_pid
        self.max_pid = max_pid
        self.bitmap = bytearray(max_pid - min_pid + 1)
        self.lock = threading.Lock()

    def allocate_map(self):
        self.bitmap[:] = b"\x00" * len(self.bitmap)
        return 1

    def allocate_pid(self):
        with self.lock:
            for pid in range(self.min_pid, self.max_pid + 1):
                if not self.bitmap[pid - self.min_pid]:
                    self.bitmap[pid - self.min_pid] = 1
                    return pid
        return -1

    def release_pid(self, pid):
        if not self.min_pid <= pid <= self.max_pid:
            raise ValueError("PID outside managed range")
        with self.lock:
            self.bitmap[pid - self.min_pid] = 0

def main():
    manager = PIDManager()
    manager.allocate_map()
    allocated = [manager.allocate_pid() for _ in range(5)]
    print("Allocated PIDs:", allocated)
    manager.release_pid(allocated[2])
    print("After releasing one PID:", manager.allocate_pid())
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
