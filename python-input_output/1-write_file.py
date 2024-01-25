#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """Return number of character written into a file"""

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)


# Tests
# nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
# print(nb_characters)
