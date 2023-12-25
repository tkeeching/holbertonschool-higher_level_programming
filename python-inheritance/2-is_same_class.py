#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """Returns True if obj is of instance a_class, otherwise returns False."""
    if (isinstance(obj, bool) or isinstance(obj, type(None))):
        return False
    elif (isinstance(obj, a_class)):
        return True
    else:
        return False


# Tests
# a = 1
# if is_same_class(a, int):
#     print("{} is an instance of the class {}".format(a, int.__name__))
# if is_same_class(a, float):
#     print("{} is an instance of the class {}".format(a, float.__name__))
# if is_same_class(a, object):
#     print("{} is an instance of the class {}".format(a, object.__name__))
# a = True
# print(is_same_class(a, int))
# a = True
# print(is_same_class(a, object))
# a = None
# print(is_same_class(a, object))
# print(type(None))
