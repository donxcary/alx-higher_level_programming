#!/usr/bin/python3
"""
Module defines a function which adds attributes to obj
"""


def add_attribute(attr, obj, value):
    """
    function that adds a new attribute to an object
    """
    if not hasattr("__dict__", obj):
        raise TypeError("can't add new attribute")
    setattr(attr, attr, value)
