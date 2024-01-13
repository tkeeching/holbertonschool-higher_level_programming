#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry():
    """BaseGeometry class."""

    def __init__(self):
        pass

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError("{0} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{0} must be greater than 0".format(name))


"""Rectangle module"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        if self.integer_validator("width", width) is None:
            self.__width = width
        if self.integer_validator("height", height) is None:
            self.__height = height


# Tests
# r = Rectangle(3, 5)

# print(r)
# print(dir(r))

# try:
#     print("Rectangle: {} - {}".format(r.width, r.height))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r2 = Rectangle(4, True)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
