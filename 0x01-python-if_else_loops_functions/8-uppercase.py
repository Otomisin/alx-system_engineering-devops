#!/usr/bin/python3

"""
Write a function that prints a string in uppercase followed by a new line
"""


def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) - 32)  # 32 was added to the ch because by adding/subtracting 32 you get the correspoing upper ot lower case copepoint. Read more here: https://learncodingfast.com/2-ways-to-convert-a-string-to-lowercase-in-python/
        print(f"{ch}", end="")

# or

# def uppercase(str):
#     for c in str:
#         if ord('a') <= ord(c) <= ord('z'):
#             c = chr(ord(c) - (ord('a') - ord('A')))
#         print("{:s}".format(c), end='')
#     print("")
