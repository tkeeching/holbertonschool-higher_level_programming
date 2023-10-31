#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in range(len(str)):
        char = str[i]
        if ((ord(char) >= 97) and (ord(char) <= 123)):
            result += chr(ord(char) - 32)
        else:     
            result += char
    print("{0}".format(result))
