#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = list(a_dictionary)
    length = len(a)
    if value in a_dictionary is False:
        return (a_dictionary)
    for i in range(0, length):
        if a_dictionary[a[i]] == value:
            del a_dictionary[a[i]]
    return (a_dictionary)
