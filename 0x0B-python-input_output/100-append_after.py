#!/usr/bin/python3
"""
Contains the "append after" function
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] = line + new_string + '\n'
        file.seek(0)
        file.writelines(lines)
