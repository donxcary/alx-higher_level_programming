#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    if len(filename) == 0:
        return 0
    with open(filename, "a", encoding="utf-8") as file_open:
        length = file_open.write(text)
        return length
