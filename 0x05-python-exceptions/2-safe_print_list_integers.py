#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    k = 0
    while i < x:
        try:
            int(my_list[i])
            k += 1
            print("{:d}".format(my_list[i]), end="")
        except:
            i += 0
        i += 1
    print()
    return k



# """
# Write a function that prints the first x elements of a list and only integers
# """
# TEST CODE
# """

# # # Test 1

# # my_list = [1, 2, 3, 4, 5]
# # nb_print = safe_print_list_integers(my_list, 2)
# # print("nb_print: {:d}".format(nb_print))
