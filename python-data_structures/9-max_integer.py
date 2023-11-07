#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None

    prev_int = my_list[0] or 0
    for i in range(len(my_list)):
        if (my_list[i] > prev_int):
            prev_int = my_list[i]
    return prev_int


# Tests
# my_list = [1, 90, 2, 13, 34, 5, -13, 3]
# my_list = [-1, -2, -3, -4]
# my_list = []
# max_value = max_integer(my_list)
# print("Max: {}".format(max_value))
