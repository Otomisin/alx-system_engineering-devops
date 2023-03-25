#!/usr/bin/python3
"""
Write a function that removes all characters c and C from a string.
"""
def no_c(my_string):
    new_s = my_string.translate({ord('c'): None})
    new_s = new_s.translate({ord('C'): None})
    return new_s
