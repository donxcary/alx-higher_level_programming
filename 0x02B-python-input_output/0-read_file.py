#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """
    if len(filename) == 0:
        return
    with open(filename, "r", encoding="utf-8") as file_open:
        text = file_open.read()
        for line in text:
            print(line, end="")
