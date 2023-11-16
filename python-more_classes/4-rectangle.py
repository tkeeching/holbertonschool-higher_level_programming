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

        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Prints the rectangle with the character #"""

        result = ""
        if (self.__width == 0 or self.__height == 0):
            return result

        for i in range(self.__height):
            for j in range(self.__width):
                if (i != self.__height - 1 and j == self.__width - 1):
                    result += "#\n"
                else:
                    result += "#"
        return result

    def __repr__(self):
        """Internal representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"


# Tests
# my_rectangle = Rectangle(2, 4)
# print(str(my_rectangle))
# print("--")
# print(my_rectangle)
# print("--")
# print(repr(my_rectangle))
# print("--")
# print(hex(id(my_rectangle)))
# print("--")

# # create new instance based on representation
# new_rectangle = eval(repr(my_rectangle))
# print(str(new_rectangle))
# print("--")
# print(new_rectangle)
# print("--")
# print(repr(new_rectangle))
# print("--")
# print(hex(id(new_rectangle)))
# print("--")

# print(new_rectangle is my_rectangle)
# print(type(new_rectangle) is type(my_rectangle))
