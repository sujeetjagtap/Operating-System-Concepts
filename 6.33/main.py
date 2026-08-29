#!/usr/bin/env python3
"""Thread-safe finite-resource manager using a mutex."""
import argparse
import threading
import time

MAX_RESOURCES = 5

class ResourceManager:
    def __init__(self):
        self.available = MAX_RESOURCES
        self.lock = threading.Lock()

    def decrease_count(self, count):
        while True:
            with self.lock:
                if self.available >= count:
                    self.available -= count
                    print(f"Gave {count} resources, {self.available} remaining.")
                    return
            time.sleep(0.001)

    def increase_count(self, count):
        with self.lock:
            self.available += count
            print(f"Received {count} resources, {self.available} remaining.")

    def get_resources(self, count):
        self.decrease_count(count)
        time.sleep(0.02)
        self.increase_count(count)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("requests", nargs="+", type=int)
    requests = parser.parse_args().requests
    if any(n <= 0 or n > MAX_RESOURCES for n in requests):
        parser.error(f"each request must be between 1 and {MAX_RESOURCES}")

    manager = ResourceManager()
    threads = [threading.Thread(target=manager.get_resources, args=(n,))
               for n in requests]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
