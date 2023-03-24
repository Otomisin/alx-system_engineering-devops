#!/usr/bin/python3
"""
Write a program that prints numbers from 0 to 99.
"""
for i in range(0, 100):
    # {:02} Pads the integers so that it has 2 zeros
    print("{:02}".format(i), end=', ')
    # or print(f"{i}", end=', ')
print("{:02}".format(i + 1))
# or print(f"{i}")
