#!/usr/bin/python3
"""
Module 0-square
Defines class Square
"""


class Square:
    """
    A class that defines a square
    Private instance attribute: size
    property def size(self): to retrieve it
    property setter def size(self, value): to set it
    Instantiation with size and error messages
    Public instance method: def area(self): that
    returns the current square area
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        area = self.size ** 2
        return area
