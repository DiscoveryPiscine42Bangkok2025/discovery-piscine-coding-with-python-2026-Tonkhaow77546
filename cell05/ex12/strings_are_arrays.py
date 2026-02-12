#!/usr/bin/env python3

from sys import argv


if len(argv) < 2:
    print("none")
else:
    z = ""

    for char in argv[1]:
        if char == "z":
            z += "z"

    if z:
        print(z)
    else:
        print("none")
        