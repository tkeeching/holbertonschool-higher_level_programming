#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print("{0}: {1}".format(i, a_dictionary[i]))


# Tests
# a_dictionary = { 'language': "C", 'Number': 89,
#     'track': "Low level", 'ids': [1, 2, 3] }
# print_sorted_dictionary(a_dictionary)
