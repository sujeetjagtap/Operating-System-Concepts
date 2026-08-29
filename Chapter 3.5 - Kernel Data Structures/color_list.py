#!/usr/bin/env python3
"""User-space analogue of a Linux kernel linked list of RGB colors."""
from dataclasses import dataclass

@dataclass
class Color:
    red: int
    blue: int
    green: int

def main():
    colors = [
        Color(255, 0, 0),
        Color(0, 255, 0),
        Color(0, 0, 255),
        Color(255, 0, 165),
    ]
    print("color_list module loaded!")
    for color in colors:
        print(f"red = {color.red} -- blue = {color.blue} -- green = {color.green}")
    print("color_list module removed!")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
