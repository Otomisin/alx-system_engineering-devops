#!/usr/bin/python3
"""
Write a function that replaces an element in a list at a specific
position without modifying the original list (like in C).
"""
# pylint: disable = invalid-name
def new_in_list(my_list, idx, element):
    newList = [None] * len(my_list)
    for i in range(0, len(my_list)):
        if i == idx:
            newList[i] = element
        else:
            newList[i] = my_list[i]
    return newList
