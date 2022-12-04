#!/usr/bin/python3
"""
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        a = ""
        for j in range(0, len(matrix[i])):
            if matrix[i][j] in range(0, 1000000):
                print("{:d}".format(matrix[i][j]), end="")
                if j < len(matrix[i]) - 1:
                     print(" ", end="")
        print()

        
"""

def print_matrix_integer(matrix=[[]]):
    for each_list in matrix:
        for i in each_list:
            print("{:d}".format(i), end='')
            if i != each_list[len(each_list) - 1]:
                print(" ", end='')
        print('\n', end='')