#!/usr/bin/python3
"""is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is of instance a_class or
    if the object is an instance of a class that inherited
    from, otherwise returns False.
    """
    if (type(obj) is bool or type(obj) is None):
        return False
    elif (isinstance(obj, a_class)):
        return True
    else:
        return False


# Tests
# a = 1
# if is_kind_of_class(a, int):
#     print("{} comes from {}".format(a, int.__name__))
# if is_kind_of_class(a, float):
#     print("{} comes from {}".format(a, float.__name__))
# if is_kind_of_class(a, object):
#     print("{} comes from {}".format(a, object.__name__))
