#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle  # for checker
# from rectangle import Rectangle  # for local


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __size(self, size):
        """Size setter"""

        self.width = self.validator("width", size)
        self.height = self.validator("height", size)

    def size(self):
        """Size getter"""

        return self.width

    size = property(size, __size)

    def update(self, *args, **kwargs):
        """Attributes setter"""

        if (len(args) > 0):
            attributes = ['id', 'size', 'x', 'y']

            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for attribute in kwargs:
                setattr(self, attribute, kwargs[attribute])

    def __str__(self):
        """Override string representation of the square"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Returns dictionary representation of the square"""

        result = {key.replace('_Rectangle__', '').replace('width', 'size'):
                  value for key, value in self.__dict__.items()}

        del result['height']
        return result

# Tests
# Task 10
# s1 = Square(5)
# print(s1)
# print(s1.area())
# s1.display()

# print("---")

# s2 = Square(2, 2)
# print(s2)
# print(s2.area())
# s2.display()

# print("---")

# s3 = Square(3, 1, 3)
# print(s3)
# print(s3.area())
# s3.display()


# Task 11
# s1 = Square(5)
# print(s1)
# print(s1.size)
# s1.size = 10
# print(s1)

# try:
#     s1.size = "9"
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# Task 12
# s1 = Square(5)
# print(s1)

# s1.update(10)
# print(s1)

# s1.update(1, 2)
# print(s1)

# s1.update(1, 2, 3)
# print(s1)

# s1.update(1, 2, 3, 4)
# print(s1)

# s1.update(x=12)
# print(s1)

# s1.update(size=7, y=1)
# print(s1)

# s1.update(size=7, id=89, y=1)
# print(s1)

# Task 14
# s1 = Square(10, 2, 1)
# print(s1)
# s1_dictionary = s1.to_dictionary()
# print(s1_dictionary)
# print(type(s1_dictionary))

# s2 = Square(1, 1)
# print(s2)
# s2.update(**s1_dictionary)
# print(s2)
# print(s1 == s2)

# Task 18
# s1 = Square.create(**{'size': 2})
# print(s1)
    
# Task 19
# s1 = Square(5)
# s2 = Square(7, 9, 1)
# list_squares_input = [s1, s2]

# Square.save_to_file(list_squares_input)

# list_squares_output = Square.load_from_file()

# for square in list_squares_input:
#     print("[{}] {}".format(id(square), square))

# print("---")

# for square in list_squares_output:
#     print("[{}] {}".format(id(square), square))
