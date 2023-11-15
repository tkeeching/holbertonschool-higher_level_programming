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
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
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

    def area(self):
        """Returns the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""

        if (self.__width == 0 or self.height == 0):
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)


# Tests
# my_rectangle = Rectangle(2, 4)
# print("Area: {} - Perimeter: {}"
#       .format(my_rectangle.area(), my_rectangle.perimeter()))

# print("--")

# my_rectangle.width = 10
# my_rectangle.height = 3
# print("Area: {} - Perimeter: {}"
#       .format(my_rectangle.area(), my_rectangle.perimeter()))

# print("--")

# my_rectangle.width = 1
# my_rectangle.height = 0
# print("Area: {} - Perimeter: {}"
#       .format(my_rectangle.area(), my_rectangle.perimeter()))
