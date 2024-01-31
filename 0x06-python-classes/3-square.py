#!/usr/bin/python3
"""
Module 0-square
Defines class Square
"""

class Square:
    """
    A class that defines a square
    by its size
    """

    def __init__(self, size=0):
        """Initialize the square with an optional size"""

        # Check if size is an integer
        if type(size) != int:
            raise TypeError("size must be an integer")

        # Check if size is positive or zero
        if size < 0:
            raise ValueError("size must be >= 0")

        # Set the size attribute
        self.__size = size

    def area(self):
        """Return the current square area"""

        # Calculate the area as size squared
        area = self.__size ** 2
        return area
