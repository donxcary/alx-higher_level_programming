#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def add_attribute(clss, attr, value):
    """
    function that adds a new attribute to an object
    """
    if str(type(clss)).split(".")[0] == "<class '__main__":
        setattr(clss, attr, value)
    else:
        raise TypeError("can't add new attribute")
