#!/usr/bin/env python3

age = int(input("Please tell me your age: "))

print(f"You are currently {age} years old.")

for i in range(1, 4):
    next_age = age + i * 10
    print(f"Next {i * 10}, you'll be {next_age} years old.")