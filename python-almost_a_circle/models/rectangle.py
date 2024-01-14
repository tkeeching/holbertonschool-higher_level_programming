#!/usr/bin/python3
from base import Base

"""Rectangle module"""


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width(width)
        self.__height(height)
        self.__x(x)
        self.__y(y)

    def __width(self, width):
        """width setter"""

        self.__width = self.validator("width", width)

    def width(self):
        """width getter"""

        return self.__width

    width = property(width, __width)

    def __height(self, height):
        """height setter"""

        self.__height = self.validator("height", height)

    def height(self):
        """height getter"""

        return self.__height

    height = property(height, __height)

    def __x(self, x):
        """x setter"""
        self.__x = self.validator("x", x)

    def x(self):
        """x getter"""

        return self.__x

    x = property(x, __x)

    def __y(self, y):
        """y setter"""

        self.__y = self.validator("y", y)

    def y(self):
        """y getter"""

        return self.__y

    y = property(y, __y)

    def validator(self, name, value):
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        elif ((name == "x" or name == "y") and value < 0):
            raise ValueError("{} must be >= 0".format(name))
        elif (name != "x" and name != "y" and value <= 0):
            raise ValueError("{} must be > 0".format(name))
        else:
            return value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

# Tests
# r1 = Rectangle(10, 2)
# print(r1.id)
# print(r1.width())

# r2 = Rectangle(2, 10)
# print(r2.id)

# r3 = Rectangle(10, 2, 0, 0, 12)
# print(r3.id)

# print(issubclass(Rectangle, Base))

# Task 3 Tests
# try:
#     Rectangle(10, "2")
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r = Rectangle(10, 2)
#     r.width = -10
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r = Rectangle(10, 2)
#     r.x = {}
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     Rectangle(10, 2, 3, -1)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# Task 4 Tests
# r1 = Rectangle(3, 2)
# print(r1.area())

# r2 = Rectangle(2, 10)
# print(r2.area())

# r3 = Rectangle(8, 7, 0, 0, 12)
# print(r3.area())
