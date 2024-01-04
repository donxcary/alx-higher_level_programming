#!/usr/bin/python3
"""
Module
Refer to the documentation provided in the README.md
"""


def add_integer(a, b=98):
    """
    Addition function

    Args:
        @a: first number to be added
        @b: second number to be added

    Returns:
        a + b

    Raises:
        TypeError: Raises an exception
    Usage examples:
    >>> add_integer(4.0, 2.0)
    6
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return(a + b)
