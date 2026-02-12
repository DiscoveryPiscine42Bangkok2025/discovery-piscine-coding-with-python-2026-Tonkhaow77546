#!/usr/bin/env python3

from sys import argv


if len(argv) < 2:
    print("none")
    exit(0)

for arg in argv[1:]:
    if not arg.endswith("ism"):
        print(f"{arg}ism")