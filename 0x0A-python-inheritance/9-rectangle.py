#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        A function that calculates area
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
        Prints the class
        """
        msg = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return msg
