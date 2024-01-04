#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    if type(roman_string) != str:
        return (0)
    length = len(roman_string)
    num = 0
    for i in range(0, length):
        if roman_string[i] == 'M':
            num = num + 1000
        if roman_string[i] == 'D':
            num = num + 500
        if roman_string[i] == 'L':
            num = num + 50
        if roman_string[i] == 'V':
            num = num + 5
        if i != length - 1:
            if roman_string[i] == 'C':
                if roman_string[i+1] == 'M':
                    num = num - 100
                elif roman_string[i+1] == 'D':
                    num = num - 100
                else:
                    num = num + 100
            if roman_string[i] == 'X':
                if roman_string[i+1] == 'C':
                    num = num - 10
                elif roman_string[i+1] == 'L':
                    num = num - 10
                else:
                    num = num + 10
            if roman_string[i] == 'I':
                if roman_string[i+1] == 'X':
                    num = num - 1
                elif roman_string[i+1] == 'V':
                    num = num - 1
                else:
                    num = num + 1
        else:
            if roman_string[i] == 'C':
                num = num + 100
            if roman_string[i] == 'X':
                num = num + 10
            if roman_string[i] == 'I':
                num = num + 1
    return (num)
