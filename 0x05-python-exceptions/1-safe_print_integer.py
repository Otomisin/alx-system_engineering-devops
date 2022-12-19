#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)



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
