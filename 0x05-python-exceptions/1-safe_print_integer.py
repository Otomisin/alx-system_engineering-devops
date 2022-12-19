#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int(value)
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True




# """
# Write a function that prints the first x elements of a list and only integers.
# """
# """
# TEST CODE
# """

# # Test 1
# value = 89
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))

# # Test 2
# value = -89
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))

# # Test 3
# value = "School"
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
