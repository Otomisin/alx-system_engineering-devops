#!/usr/bin/python3
"""
Write a function that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    for each_list in matrix:
        for i in each_list:
            print("{:d}".format(i), end='')
            if i != each_list[len(each_list) - 1]:
                print(" ", end='')
        print('\n', end='')
