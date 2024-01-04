#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a = list(a_dictionary)
    length = len(a)
    c = 0
    for i in range(0, length):
        if a[i] == key:
            a_dictionary[a[i]] = value
        else:
            c = c + 1
    if c == length:
        a_dictionary[key] = value
    return (a_dictionary)
