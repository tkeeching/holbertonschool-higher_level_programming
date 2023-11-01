#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argument_length = len(argv)
    result = 0
    for i in range(1, argument_length):
        result += int(argv[i])
    print("{0}".format(result))