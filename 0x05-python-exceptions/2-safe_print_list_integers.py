#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    b = 0
    for i in my_list:
        a = a + 1
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            b = b + 1
        except (ValueError, TypeError):
            continue
    print()
    return (b)
