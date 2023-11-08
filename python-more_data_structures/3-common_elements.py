#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for i in set_1:
        for j in set_2:
            if (i == j):
                new_list.append(i)
    return new_list


# Tests
# set_1 = { "Python", "C", "Javascript" }
# set_2 = { "Bash", "C", "Ruby", "Perl" }
# c_set = common_elements(set_1, set_2)
# print(sorted(list(c_set)))
