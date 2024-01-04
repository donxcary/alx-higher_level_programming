#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if len(my_list) == 0:
        return (None)
    big = my_list[0]
    for i in range(0, length):
        if my_list[i] >= big:
            big = my_list[i]
    return (big)
