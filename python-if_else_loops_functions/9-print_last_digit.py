#!/usr/bin/python3
def print_last_digit(number):
    d = number % 10 if number > 0 else abs(number) % 10 * -1
    print("{0}".format(d))
