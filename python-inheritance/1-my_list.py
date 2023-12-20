#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """Returns a list."""

    def __init__(self):
        pass

    """Returns a sorted (ascending order) list."""
    def print_sorted(self):
        print(sorted(self))


# # Tests
# my_list = MyList()
# my_list.append(1)
# my_list.append(4)
# my_list.append(2)
# my_list.append(3)
# my_list.append(5)
# print(my_list)
# my_list.print_sorted()
# print(my_list)
