#!/usr/bin/python3
from sys import argv

argument_length = len(argv)
print("{0} arguments".format(argument_length -1))

for i in range(1, argument_length):
    print("{0}: {1}".format(i, argv[i]))