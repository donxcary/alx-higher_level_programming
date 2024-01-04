#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b = dict(a_dictionary)
    a = list(b)
    length = len(a)
    for i in range(0, length):
        b[a[i]] = b[a[i]] * 2
    return(b)
