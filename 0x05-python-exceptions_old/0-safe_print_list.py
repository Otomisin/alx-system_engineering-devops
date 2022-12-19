#!/usr/bin/python3

"""
Write a function that prints x elements of a list.
"""
def safe_print_list(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            count += 1
        except:
            break
        else:
            count += 1

    print()
    return (count)

# """
# Test code
# """

# my_list = [1, 2, 3, 4, 5]


# nb_print = safe_print_list(my_list, 2)
# print("The number of elements are: {:d}\n".format(nb_print))

# my_list3 = [1, 2, 3, 4, 5, 8, 23, 3]
# nb_print = safe_print_list(my_list3, len(my_list3))
# print("nb_print: {:d}\n".format(nb_print))

# my_list2 = [1, 2, 3, 4, 5, 8]
# nb_print = safe_print_list(my_list2, len(my_list2) + 2)
# print("nb_print: {:d}\n".format(nb_print))
