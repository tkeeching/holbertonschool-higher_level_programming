#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    output = 0
    result = []

    for i in range(0, list_length):
        try:
            output = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            output = 0
        except TypeError:
            print("wrong type")
            output = 0
        except IndexError:
            print("out of range")
            output = 0
        finally:
            result.append(output)

    return result


# Tests
# my_l_1 = [10, 8, 4]
# my_l_2 = [2, 4, 4]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)

# print("--")

# my_l_1 = [10, 8, 4, 4]
# my_l_2 = [2, 0, "H", 2, 7]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)

# print("--")

# my_l_1 = [10, 0, 4]
# my_l_2 = [2, 4, 0]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)

# print("--")

# my_l_1 = [10, 2]
# my_l_2 = [2]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)
