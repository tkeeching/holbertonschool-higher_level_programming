#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500}
    result = 0
    prev_int = 0
    current_int = 0

    if (type(roman_string) is not str or roman_string is None):
        return result

    for i in range(len(roman_string) - 1, -1, -1):
        current_int = roman_numerals[roman_string[i]]

        if (current_int < prev_int):
            result -= current_int
        else:
            result += current_int

        prev_int = current_int

    return result


# Tests
# roman_number = "X"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "VII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "IX"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "LXXXVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "DCCVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))
