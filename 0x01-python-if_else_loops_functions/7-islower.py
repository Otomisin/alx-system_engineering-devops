#!/usr/bin/python3
"""
Write a function that checks for lowercase character.
"""


def islower(c):
    # checks for lower case characters, if there exist one, returns true if not return lower
    if ord(c) >= 97 and ord(c) <= 122:
        # A-Z = 65-90 (Character = Code point)
        # a-z = 97-122 (Character = Code point)
        # More on ord here: https://learncodingfast.com/2-ways-to-convert-a-string-to-lowercase-in-python/
        return True
    else:
        return False
# or

# def islower(c):
#     return(ord('a') <= ord(c) <= ord('z'))
