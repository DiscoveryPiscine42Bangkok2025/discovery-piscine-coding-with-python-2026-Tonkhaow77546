#!/usr/bin/env -S python3

first_number = int(input("Enter the first number: \n"))
second_number = int(input("Enter the second number: \n"))

result = first_number * second_number

print(f"{first_number} x {second_number} = {result}")

if result == 0:
    print("The result is positive and negative.")
elif result < 0:
    print("The result is negative")
else:
    print("The result is positive")