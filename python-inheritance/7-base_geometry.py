#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry():
    """Empty class."""

    def __init__(self):
        pass

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError("{0} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{0} must be greater than 0".format(name))


# Tests
# bg = BaseGeometry()

# bg.integer_validator("my_int", 12)
# bg.integer_validator("width", 89)

# try:
#     bg.integer_validator("name", "John")
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     bg.integer_validator("age", 0)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     bg.integer_validator("distance", -4)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
