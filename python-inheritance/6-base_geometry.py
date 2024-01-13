#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry():
    """Empty class."""

    def __init__(self):
        pass

    def area(self):
        raise Exception('area() is not implemented')


# Tests
# bg = BaseGeometry()

# try:
#     print(bg.area())
# except Exception as e:
    # print("[{}] {}".format(e.__class__.__name__, e))
