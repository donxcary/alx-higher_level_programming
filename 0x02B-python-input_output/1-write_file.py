#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and
    returns the number of characters written:
    """
    if len(filename) == 0:
        return 0
    with open(filename, "w", encoding="utf-8") as file_open:
        length = file_open.write(text)
        return length
