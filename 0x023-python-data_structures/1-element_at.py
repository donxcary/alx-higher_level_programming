#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    length = len(my_list)
    if idx not in range(0, length):
        return None
    return (my_list[idx])
