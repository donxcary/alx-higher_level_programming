#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


class Rectangle:
    """
    A class with Private instance attribute: width
    Private instance attribute: height
    and property setters for width and height
    with Public instance method: def area(self):
    that returns the rectangle area and
    Public instance method: def perimeter(self):
    that returns the rectangle perimeter
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        if type(width) is not int:
            message = "width must be an integer"
            raise TypeError(message)
        if width < 0:
            msg = "width must be >= 0"
            raise ValueError(msg)
        if type(height) is not int:
            message = "height must be an integer"
            raise TypeError(message)
        if height < 0:
            msg = "height must be >= 0"
            raise ValueError(msg)
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            message = "width must be an integer"
            raise TypeError(message)
        if value < 0:
            msg = "width must be >= 0"
            raise ValueError(msg)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            message = "height must be an integer"
            raise TypeError(message)
        if value < 0:
            msg = "height must be >= 0"
            raise ValueError(msg)
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        perim = 2 * (self.__width + self.__height)
        if self.__width == 0:
            perim = 0
        if self.__height == 0:
            perim = 0
        return (perim)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        a = rect_1.area()
        b = rect_2.area()
        if a >= b:
            return rect_1
        else:
            return rect_2

    def __str__(self):
        message = ""
        if self.__width == 0:
            return message
        if self.__height == 0:
            return message
        if type(self.print_symbol) is not str:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    print("{}".format(self.print_symbol), end="")
                if (i + 1) != self.__height:
                    print()
            return message
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                message = message + self.print_symbol
            if (i + 1) != self.__height:
                message = message + "\n"
        return (message)

    def __repr__(self):
        msg = "Rectangle({}, {})".format(self.__width, self.__height)
        return "%s" % (msg)

    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
