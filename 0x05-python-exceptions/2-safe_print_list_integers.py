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
