#!/usr/bin/env python3
"""A small UNIX shell supporting history (!!), one pipe, redirection and &."""
import os
import shlex
import subprocess

def execute(tokens):
    background = tokens and tokens[-1] == "&"
    if background:
        tokens = tokens[:-1]

    if "|" in tokens:
        pos = tokens.index("|")
        left, right = tokens[:pos], tokens[pos+1:]
        p1 = subprocess.Popen(left, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(right, stdin=p1.stdout)
        p1.stdout.close()
        if not background:
            p2.wait(); p1.wait()
        return

    stdin = stdout = None
    cleaned = []
    i = 0
    while i < len(tokens):
        if tokens[i] in (">", "<"):
            if i + 1 >= len(tokens):
                print("Missing filename for redirection")
                return
            if tokens[i] == ">":
                stdout = open(tokens[i+1], "w")
            else:
                stdin = open(tokens[i+1], "r")
            i += 2
        else:
            cleaned.append(tokens[i]); i += 1

    if not cleaned:
        return
    try:
        p = subprocess.Popen(cleaned, stdin=stdin, stdout=stdout)
        if not background:
            p.wait()
    finally:
        if stdin: stdin.close()
        if stdout: stdout.close()

def main():
    last_command = None
    while True:
        try:
            line = input("myshell>> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if line.strip() in ("exit", "quit"):
            break
        if line.strip() == "!!":
            if last_command is None:
                print("No previous command in history!")
                continue
            line = last_command
            print(line)
        else:
            last_command = line
        try:
            tokens = shlex.split(line)
            execute(tokens)
        except ValueError as exc:
            print(f"Parse error: {exc}")
        except FileNotFoundError as exc:
            print(f"Command not found: {exc.filename}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
