#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        """
        A function that calculates area
        """
        area = self.__size ** 2
        return area

    def __str__(self):
        """
        Prints the class
        """
        msg = "[Rectangle] {}/{}".format(self.__size, self.__size)
        return msg
