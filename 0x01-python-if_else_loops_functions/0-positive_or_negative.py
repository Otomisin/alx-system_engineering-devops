#!/usr/bin/python3
"""
This program will assign a random signed number to the variable number each time it is executed. 
"""
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
