#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0
    for i in range(len(my_list)):
        if (new_list.count(my_list[i])):
            new_list.remove(my_list[i])
            new_list.append(my_list[i])
        else:
            new_list.append(my_list[i])

    for j in range(len(new_list)):
        result += new_list[j]

    return result


# Tests
# my_list = [1, 2, 3, 1, 4, 2, 5]
# result = uniq_add(my_list)
# print("Result: {:d}".format(result))
# print(result)
