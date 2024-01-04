#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


class MyInt(int):
    """
    class MyInt that inherits from int
    """
    def __init__(self, size):
        self.size = size

    def __eq__(self, other):
        """
        Equal to operator function
        """
        if self.size == other:
            return False
        else:
            return True

    def __ne__(self, x):
        """
        Not equal to operator function
        """
        if self.size != x:
            return False
        else:
            return True
