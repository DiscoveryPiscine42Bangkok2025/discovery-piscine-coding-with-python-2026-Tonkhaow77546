#!/usr/bin/env python3

from sys import argv

if len(argv) < 3:
    print("none")
    exit(0)

word = argv[1]
sentence = argv[2]

print(sentence.count(word))