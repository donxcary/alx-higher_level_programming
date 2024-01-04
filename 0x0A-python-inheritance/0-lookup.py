#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object
    """
    res = dir(obj)
    return(res)
