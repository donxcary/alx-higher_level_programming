#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def inherits_from(obj, a_class):
    """
    A function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the
    specified class ; otherwise False.
    """
    if type(obj) == a_class:
        c = False
        return c
    else:
        result = issubclass(type(obj), a_class)
        return result
