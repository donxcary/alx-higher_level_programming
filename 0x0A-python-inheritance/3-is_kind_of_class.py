#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited
    from, the specified class ; otherwise False
    """
    result = isinstance(obj, a_class)
    return result
