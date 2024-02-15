#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""

import json

def load_from_json_file(filename):
    """Open the file in read mode"""
    with open(filename, "r") as f:
        """Load the JSON data as a Python object"""
        obj = json.load(f)
        # Return the object
        return obj

