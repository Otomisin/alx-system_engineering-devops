#!/usr/bin/python3
"""
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line
    -Print all the letters except q and e
    -You can only use one print function with string format
    -You can only use one loop in your code
    -You are not allowed to store characters in a variable
    -You are not allowed to import any module
"""
for char in range(97, 123):
    if chr(char) == "q" or chr(char) == "e":
        pass
    else:
        print("{}".format(chr(char)), end="")
        # or print(f"{chr(char)}", end="")
