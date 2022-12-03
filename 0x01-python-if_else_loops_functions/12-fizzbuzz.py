#!/usr/bin/python3

"""
a function that prints the numbers from 1 to 100 separated by a space.
"""
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end='')
        if i % 5 == 0:
            print("Buzz", end='')
        if i % 3 and i % 5:
            print("{:d}".format(i), end='')
        print(end=' ')
