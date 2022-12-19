#!/usr/bin/python3
"""
Write a function that prints an integer.
"""
def safe_print_integer_err(value):
     try: 
          val = x
          print (x)
     except: 
          print("Try another value")
     return value


"""
TEST CODE
"""

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))