#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    t_a = tuple_a
    t_b = tuple_b
    for i in range(2):
        if (type(t_a) is int):
            t_a = tuple([tuple_a])
        if (type(t_b) is int):
            t_b = tuple([tuple_b])
        if ((len(t_a) <= i) and (len(t_b) <= i)):
            result.append(0 + 0)
        elif (len(t_a) <= i):
            result.append(0 + t_b[i])
        elif (len(t_b) <= i):
            result.append(t_a[i] + 0)
        else:
            result.append(t_a[i] + t_b[i])
    return tuple(result)


# Tests
# tuple_a = (1, 89)
# tuple_b = (88, 11)
# tuple_c = (2, 4)
# tuple_d = (1)
# tuple_e = (1)
# new_tuple = add_tuple(tuple_a, tuple_b)
# print(new_tuple)

# print(add_tuple(tuple_a, (1, )))
# print(add_tuple(tuple_a, ()))
# print(add_tuple((), tuple_c))
# print(add_tuple(tuple_d, tuple_e))
# print(add_tuple((), ()))
