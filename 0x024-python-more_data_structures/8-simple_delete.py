#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a = list(a_dictionary)
    length = len(a)
    for i in range(0, length):
        if a[i] == key:
            del a_dictionary[a[i]]
    return (a_dictionary)
