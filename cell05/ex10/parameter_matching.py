#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
    print("none")
else:
    param = argv[1]
    prompt = input("What was the parameter?: ")

    if param == prompt:
        print("Good job!")
    else:
        print("Nope, sorry...")