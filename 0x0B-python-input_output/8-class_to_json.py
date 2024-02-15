#!/usr/bin/python3
"""
Contains the "class_to_json" function
"""

def class_to_json(obj):
    """
    This function takes an object as input and returns a dictionary representation of the object.
    The object should be an instance of a class.
    All attributes of the object are assumed to be JSON serializable: list, dictionary, string, integer, and boolean.
    """
    return obj.__dict__

