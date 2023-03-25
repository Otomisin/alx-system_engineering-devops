#!/usr/bin/python3
"""
This program will assign a random signed number to the variable number each time it is executed
"""
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10  # or use int(str(number)[-1]) to get the last digit
if number < 0:
    digit = -digit
print("Last digit of {} is {} and is ".format(number, digit), end="")
# or use print(f"Last digit of {number} is {digit} ", end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
