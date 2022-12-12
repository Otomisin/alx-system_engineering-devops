#!/usr/bin/python3
"""prints the ASCII alphabet, in lowercase, not followed by a new line."""

for char in range(97, 123):
    print("{}".format(chr(char)), end="")
    # or use print(f"{chr(char)}", end=" ") to get the character of of the
    # Unicode and use ord() function to Convert back to unicode.
