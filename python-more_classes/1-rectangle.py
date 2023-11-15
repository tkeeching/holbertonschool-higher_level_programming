#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Represents and empty Rectangle"""

    def __init__(self, width=0, height=0):
        self.__width(width)
        self.__height(height)

    # Setters
    def __width(self, value):
        """Setter for the width of the rectangle"""

        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def __height(self, value):
        """Setter for the height of the rectangle"""

        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    # Getters
    def width(self):
        """Returns the width of the rectangle"""

        return self.__width

    def height(self):
        """Returns the height of the rectangle"""

        return self.__height

    # Properties
    width = property(width, __width)
    height = property(height, __height)


# Tests
# my_rectangle = Rectangle(2, 4)
# print(my_rectangle.__dict__)

# my_rectangle.width = 10
# my_rectangle.height = 3
# print(my_rectangle.__dict__)
