#!/usr/bin/python3
for i in range(0, 100):
    num = str(i).zfill(2)
    if i == 99:
        print("{0}".format(num), end="")
    else:
        print("{0}".format(num), end=", ")
