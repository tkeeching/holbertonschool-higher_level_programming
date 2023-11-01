#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argument_length = len(argv) - 1
    if (argument_length == 0):
        print("{0} arguments.".format(argument_length))
    elif (argument_length == 1):
        print("{0} argument:".format(argument_length))
    else:
        print("{0} arguments:".format(argument_length))

    for i in range(1, argument_length + 1):
        print("{0}: {1}".format(i, argv[i]))
