#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0
    for i in range(0, x):
        nb_print += 1
        try:
            print("{0}".format(my_list[i]), end="")
        except IndexError:
            nb_print -= 1
            print("")
            return nb_print
    print("")
    return nb_print


# Tests
# my_list = [1, 2, 3, 4, 5]
# my_list = [1, 2, 3, 4]

# nb_print = safe_print_list(my_list, 2)
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list))
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, 0)
# print("nb_print: {:d}".format(nb_print))
