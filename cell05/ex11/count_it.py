#!/usr/bin/env python3

from sys import argv

if len(argv) < 2:
    print("none")
else:
    print(f"parameters: {len(argv) - 1}")

    for arg in argv[1:]:
        print(f"{arg}: {len(arg)}")