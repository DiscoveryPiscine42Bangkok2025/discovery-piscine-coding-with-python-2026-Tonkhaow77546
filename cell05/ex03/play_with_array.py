#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()

print(array)

for i in array:
    if i > 5:
        new_array.add(i + 2)

print(new_array)