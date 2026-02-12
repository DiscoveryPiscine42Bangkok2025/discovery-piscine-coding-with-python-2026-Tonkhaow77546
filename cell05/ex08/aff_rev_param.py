#!/usr/bin/env python3

from sys import argv

if len(argv) < 4:
    print("none")
    exit(0)

for text in argv[::-1]:
    print(text)