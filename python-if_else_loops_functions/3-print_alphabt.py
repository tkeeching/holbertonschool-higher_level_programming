#!/usr/bin/python3
for i in range(97, 123):
    alphabet = chr(i)
    if ((alphabet == 'e') or (alphabet == 'q')):
        continue
    print("{0}".format(alphabet), end="")
