#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argument_length = len(argv)
    if (argument_length - 1 == 1):
        print("{0} argument".format(argument_length -1))
    else:
        print("{0} arguments".format(argument_length -1))

    for i in range(1, argument_length):
        print("{0}: {1}".format(i, argv[i]))
