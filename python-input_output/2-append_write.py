#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and
    return number of characters added
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)


# Tests
# nb_characters_added = append_write("file_append.txt",
# "This School is so cool!\n")
# print(nb_characters_added)
