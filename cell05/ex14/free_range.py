#!/usr/bin/env python3

from sys import argv

if len(argv) != 3:
    print("none")
    exit(0)

start = int(argv[1])
end = int(argv[2]) + 1

print(list(range(start, end)))