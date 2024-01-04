#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    a = list(a_dictionary)
    length = len(a)
    if length == 0:
        return (None)
    big = a_dictionary[a[0]]
    for i in range(0, length):
        if a_dictionary[a[i]] > big:
            big = a_dictionary[a[i]]
    for i in range(0, length):
        if big == a_dictionary[a[i]]:
            return (a[i])
