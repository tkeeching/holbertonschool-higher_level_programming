#!/usr/bin/python3
"""Square module with
    - private instance attribute: size
        - getter
        - setter
    - public instance method: def area(self): returns square area
    - public instance method: def my_print(self): prints the square
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

    def my_print(self):
        """Prints the area of the square."""

        if (self.__size == 0):
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    if (j == self.__size - 1):
                        print("#")
                    else:
                        print("#", end="")

    size = property(size, __size)


# Tests
# my_square = Square(3)
# my_square.my_print()

# print("--")

# my_square.size = 10
# my_square.my_print()

# print("--")

# my_square.size = 0
# my_square.my_print()

# print("--")
