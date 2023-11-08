#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = set_1.union(set_2)
    common_list = []

    for i in set_1:
        for j in set_2:
            if (i == j):
                common_list.append(i)

    for k in common_list:
        new_list.remove(k)

    return new_list


# Tests
# set_1 = { "Python", "C", "Javascript" }
# set_2 = { "Bash", "C", "Ruby", "Perl" }
# od_set = only_diff_elements(set_1, set_2)
# print(sorted(list(od_set)))
