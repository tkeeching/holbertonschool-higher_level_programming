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

    def __init__(self, size=0, position=(0, 0)):
        self.__size(size)
        self.__position(position)

    # Setter
    def __size(self, value):
        """Set the size of the square."""

        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    # Setter
    def __position(self, value):
        """Set the position of the square.
        Must be a tuple of 2 positive integers.
        """

        if (len(value) != 2
                or type(value[0]) is not int
                or type(value[0]) is not int
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    # Getter
    def size(self):
        """Returns the size of the square."""

        return self.__size

    def position(self):
        """Returns the position of the square."""

        return self.__position

    def area(self):
        """Returns the area of the square."""

        return self.__size ** 2

    def my_print(self):
        """Prints the area of the square."""

        if (self.__size == 0):
            print("")
        else:
            count_y = 0
            while (count_y < self.__position[1]):
                print("")
                count_y += 1

            for i in range(self.__size):
                count_x = 0
                for j in range(self.__size):
                    while (count_x < self.__position[0]):
                        print(" ", end="")
                        count_x += 1

                    if (j == self.__size - 1):
                        print("#")
                    else:
                        print("#", end="")

    size = property(size, __size)
    position = property(position, __position)


# Tests
# my_square_1 = Square(3)
# my_square_1.my_print()

# print("--")

# my_square_2 = Square(3, (1, 1))
# my_square_2.my_print()

# print("--")

# my_square_3 = Square(3, (3, 0))
# my_square_3.my_print()

# print("--")

# my_square_3 = Square(3, (3, 3))
# my_square_3.my_print()

# print("--")

# my_square_3 = Square(3, (-2, 0))
# my_square_3.my_print()

# print("--")

# my_square_3 = Square(3, (0, -1))
# my_square_3.my_print()

# print("--")

# my_square = Square(3, (1, 1))
# print(my_square.size)
# print(my_square.area())
# print(my_square.position)

# print("--")

# my_square = Square(3, (1, "3"))

# print("--")
