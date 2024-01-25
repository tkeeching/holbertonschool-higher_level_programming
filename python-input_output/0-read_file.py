#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """Prints content of a file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

# # # Tests
# read_file("my_file_0.txt")
