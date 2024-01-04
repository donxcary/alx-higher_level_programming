#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    b = 1
    for i in my_list:
        a = b
        for j in my_list[b:]:
            if i == j:
                del my_list[a]
                a = a - 1
            a = a + 1
        b = b + 1
    for i in my_list:
        total = total + i
    return (total)
