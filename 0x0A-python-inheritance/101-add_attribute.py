#!/usr/bin/python3
"""
Module defines a function which adds attributes to obj
"""


def add_attribute(obj, attr, value):
    """
    Check if the object has a __dict__
         attribute that stores its attribute
    """
    if not hasattr(obj, "__dict__"):
    """
    Raise a TypeError exception with the message
    """
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
