#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base  # for checker
# from base import Base  # for local


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

    def update(self, *args, **kwargs):
        """Attributes setter"""

        if (len(args) > 0):
            attributes = ['id', 'width', 'height', 'x', 'y']

            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for attribute in kwargs:
                setattr(self, attribute, kwargs[attribute])

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
        """Validates attribute"""

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

    def display(self):
        """Prints rectangle instance with the character #"""

        if (self.__y) > 0:
            for m in range(self.__y):
                print("")
            for i in range(self.__height):
                for n in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print("")
        else:
            for i in range(self.__height):
                for n in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print("")

    def __str__(self):
        """Override string representation of the rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def to_dictionary(self):
        """Returns dictionary representation of the rectangle"""

        return {key.replace('_Rectangle__', ''): value for key, value in
                self.__dict__.items()}

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

# Task 5 Tests
# r1 = Rectangle(4, 6)
# r1.display()

# print("---")

# r1 = Rectangle(2, 2)
# r1.display()

# Task 6 Tests
# r1 = Rectangle(4, 6, 2, 1, 12)
# print(r1)

# r2 = Rectangle(5, 5, 1)
# print(r2)

# Task 7 tests
# r1 = Rectangle(2, 3, 2, 2)
# r1.display()

# print("---")

# r2 = Rectangle(3, 2, 1, 0)
# r2.display()

# print("---")

# r2 = Rectangle(10, 12, 1, 0)
# r2.display()

# print("---")

# r2 = Rectangle(10, 12, 2, 3)
# r2.display()

# Task 8 tests
# r1 = Rectangle(10, 10, 10, 10)
# print(r1)

# r1.update(89)
# print(r1)

# r1.update(89, 2)
# print(r1)

# r1.update(89, 2, 3)
# print(r1)

# r1.update(89, 2, 3, 4)
# print(r1)

# r1.update(89, 2, 3, 4, 5)
# print(r1)

# Task 9 tests
# r1 = Rectangle(10, 10, 10, 10)
# print(r1)

# r1.update(height=1)
# print(r1)

# r1.update(width=1, x=2)
# print(r1)

# r1.update(y=1, width=2, x=3, id=89)
# print(r1)

# r1.update(x=1, height=2, y=3, width=4)
# print(r1)


# Task 13
# r1 = Rectangle(10, 2, 1, 9)
# print(r1)
# r1_dictionary = r1.to_dictionary()
# print(r1_dictionary)
# print(type(r1_dictionary))

# r2 = Rectangle(1, 1)
# print(r2)
# r2.update(**r1_dictionary)
# print(r2)
# print(r1 == r2)

# Task 15
# r1 = Rectangle(10, 7, 2, 8)
# dictionary = r1.to_dictionary()
# json_dictionary = Base.to_json_string([dictionary])
# print(dictionary)
# print(type(dictionary))
# print(json_dictionary)
# print(type(json_dictionary))

# Task 16
# r1 = Rectangle(10, 7, 2, 8)
# r2 = Rectangle(2, 4)
# Rectangle.save_to_file(None)

# with open("Rectangle.json", "r") as file:
#     print(file.read())      

# Task 17
# list_input = [
#     {'id': 89, 'width': 10, 'height': 4}, 
#     {'id': 7, 'width': 1, 'height': 7}
# ]
# json_list_input = Rectangle.to_json_string(list_input)
# list_output = Rectangle.from_json_string(json_list_input)
# print("[{}] {}".format(type(list_input), list_input))
# print("[{}] {}".format(type(json_list_input), json_list_input))
# print("[{}] {}".format(type(list_output), list_output))

# Task 18
# r1 = Rectangle(3, 5, 1)
# r1_dictionary = r1.to_dictionary()
# r2 = Rectangle.create(**r1_dictionary)
# print(r1)
# print(r2)
# print(r1 is r2)
# print(r1 == r2)

# r3 = Rectangle.create(**{'width': 2, 'height': 3})
# print(r3)

# Task 19
# r1 = Rectangle(10, 7, 2, 8)
# r2 = Rectangle(2, 4)
# list_rectangles_input = [r1, r2]

# Rectangle.save_to_file(list_rectangles_input)

# list_rectangles_output = Rectangle.load_from_file()

# for rect in list_rectangles_input:
#     print("[{}] {}".format(id(rect), rect))

# print("---")

# for rect in list_rectangles_output:
#     print("[{}] {}".format(id(rect), rect))
