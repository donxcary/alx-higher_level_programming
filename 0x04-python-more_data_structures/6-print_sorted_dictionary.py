#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary)
    length = len(a)
    for i in range(0, length):
        print("{:s}: {}".format(a[i], a_dictionary[a[i]]))
