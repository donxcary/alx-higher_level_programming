#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""

import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)
