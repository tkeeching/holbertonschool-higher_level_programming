#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0
    try:
        for i in range(0, x):
            nb_print += 1
            if ((nb_print == len(my_list)) or nb_print == x):
                print("{0}".format(my_list[i]))
            else:
                print("{0}".format(my_list[i]), end="")
        return nb_print
    except:
        nb_print = 0
        for i in range(0, len(my_list)):
            nb_print += 1
        return nb_print


# Tests
# my_list = [1, 2, 3, 4, 5]

# nb_print = safe_print_list(my_list, 2)
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list))
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))
