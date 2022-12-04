#!/usr/bin/python3
"""
Write a function that returns a tuple with the length of a string and its first character.
"""

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        result = (0, None)
        return result
    else:
        res = (length, sentence[0:1])
        return res
