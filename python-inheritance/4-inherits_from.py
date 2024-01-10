#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is of instance a_class that
    inherited (directly or indirectly) from the specified
    class, otherwise returns False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class


# Tests
# a = True
# if inherits_from(a, int):
#     print("{} inherited from class {}".format(a, int.__name__))
# if inherits_from(a, bool):
#     print("{} inherited from class {}".format(a, bool.__name__))
# if inherits_from(a, object):
#     print("{} inherited from class {}".format(a, object.__name__))
