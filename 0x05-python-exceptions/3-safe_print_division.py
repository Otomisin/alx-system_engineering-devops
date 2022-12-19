#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)


# '''
# Write a function that divides 2 integers and prints the result.
# '''
# TEST CODE
# """
# a = 12
# b = 4
# result = safe_print_division(a, b)
# print("{:d} / {:d} = {}".format(a, b, result))

# #or

# print(safe_print_division(3, 4))
