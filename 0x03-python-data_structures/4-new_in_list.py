#!/usr/bin/python3

"""
Write a function that replaces an element in a list at a specific 
position without modifying the original list (like in C).
"""
def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return copied_list
    else:
        copied_list[idx] = element
        return copied_list

"""
def new_in_list(my_list, idx, element):
    newList = [None] * len(my_list)
    for i in range(0, len(my_list)):
        if i == idx:
            newList[i] = element
        else:
            newList[i] = my_list[i]
    return newList
"""

