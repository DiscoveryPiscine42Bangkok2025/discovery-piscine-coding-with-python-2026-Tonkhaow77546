#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
    print("none")
    exit(0)


print(argv[1].lower())