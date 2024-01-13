#!/usr/bin/python3
from base import Base

"""Rectangle module"""


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self._width(width)
        self._height(height)
        self._x(x)
        self._y(y)

    def _width(self, width):
        """width setter"""

        self.__width = width

    def width(self):
        """width getter"""

        return self.__width

    def _height(self, height):
        """height setter"""

        self.__height = height

    def height(self):
        """height getter"""

        return self.__height

    def _x(self, x):
        """x setter"""

        self.__x = x

    def x(self):
        """x getter"""

        return self.__x

    def _y(self, y):
        """y setter"""

        self.__y = y

    def y(self):
        """y getter"""

        return self.__y


# Tests
# r1 = Rectangle(10, 2)
# print(r1.id)
# print(r1.width())

# r2 = Rectangle(2, 10)
# print(r2.id)

# r3 = Rectangle(10, 2, 0, 0, 12)
# print(r3.id)

# print(issubclass(Rectangle, Base))
