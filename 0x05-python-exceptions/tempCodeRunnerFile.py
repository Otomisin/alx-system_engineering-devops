#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)

# """
# Write a function that prints x elements of a list.
# Test code
# """

my_list = [1, 2, 3, 4, 5]


nb_print = safe_print_list(my_list, 2)
print("The number of elements are: {:d}\n".format(nb_print))