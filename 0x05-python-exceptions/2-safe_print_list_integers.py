#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)




# """
# Write a function that prints the first x elements of a list and only integers
# """
# TEST CODE
# """

# # # Test 1

# # my_list = [1, 2, 3, 4, 5]
# # nb_print = safe_print_list_integers(my_list, 2)
# # print("nb_print: {:d}".format(nb_print))
