#!/usr/bin/python3
"""Square module with
    - private instance attribute: size
    - public instance method: def area(self)
"""


class Square:
    """Represent a Square with private instance attribute and
    public instance method
    """

    def __init__(self, size=0):
        self.__size(size)

    # Setter
    def __size(self, value):
        """Set the size of the square."""

        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    # Getter
    def size(self):
        """Returns the size of the square."""

        return self.__size

    def area(self):
        """Returns the area of the square."""

        return self.__size ** 2

    size = property(size, __size)


# Tests
# my_square = Square(89)
# print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# my_square.size = 3
# print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# try:
#     my_square.size = "5 feet"
#     print("Area: {} for size: {}".format(my_square.area(), my_square.size))
# except Exception as e:
#     print(e)
