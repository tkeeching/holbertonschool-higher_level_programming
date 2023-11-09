#!/usr/bin/python3
def best_score(a_dictionary):
    biggest_int = 0
    name_with_biggest_int = ""
    if (a_dictionary is None):
      return None
    for k, v in a_dictionary.items():
        if (v > biggest_int):
            biggest_int = v
            name_with_biggest_int = k
    return name_with_biggest_int


# Tests
# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))

# best_key = best_score(None)
# print("Best score: {}".format(best_key))
