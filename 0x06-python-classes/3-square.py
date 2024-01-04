#!/usr/bin/python3
"""
Module 0-square
Defines class Square
"""


class Square:
    """
    A class that defines a square
    Private instance attribute: size
    Instantiation with size and error messages
    Public instance method: def area(self): that
    returns the current square area
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size ** 2
        return area
