#!/usr/bin/env python3

array = [10, 5, 7, -2, 3, 8]
new_array = []

for i in array:
    if i > 5:
        i = i + 2
        new_array.append(i)

print(array)
print(new_array)