#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Represents and empty Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width(width)
        self.__height(height)
        Rectangle.number_of_instances += 1

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

    def __del__(self):
        """Delete method"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


# Tests
# my_rectangle_1 = Rectangle(2, 4)
# my_rectangle_2 = Rectangle(2, 4)
# print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
# del my_rectangle_1
# print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
# del my_rectangle_2
# print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
