#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    for i in range(2):
        if (len(tuple_a) <= i):
            result.append(0 + tuple_b[i])
        elif (len(tuple_b) <= i):
            result.append(tuple_a[i] + 0)
        else:
            result.append(tuple_a[i] + tuple_b[i])
    return tuple(result)


# Tests
# tuple_a = (1, 89)
# tuple_b = (88, 11)
# tuple_c = (2, 4)
# new_tuple = add_tuple(tuple_a, tuple_b)
# print(new_tuple)

# print(add_tuple(tuple_a, (1, )))
# print(add_tuple(tuple_a, ()))
# print(add_tuple((), tuple_c))
