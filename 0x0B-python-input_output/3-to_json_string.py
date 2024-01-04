#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""

import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)
    """
    return (json.dumps(my_obj, sort_keys=True))
