#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def print_square(size):
    """
    A simple function that prints a square with the character #

    Args:
        @size: size length of the square

    Raises:
        TypeError: Raises an exception
        ValueError: Raises an exception
    """
    message = "size must be an integer"
    if type(size) is float:
        if size < 0:
            raise TypeError(message)
    if type(size) is not int:
        raise TypeError(message)
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
