#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


class BaseGeometry:
    """
    A class with Public instance method: def area(self)
    and def integer_validator(self, name, value):
    """
    def area(self):
        """
        A public instance method that raises an Exception
        with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A public instance method that validates value
        """
        self.name = name
        if type(value) is not int:
            message = "must be an integer"
            raise TypeError("{} {}".format(self.name, message))
        if value <= 0:
            msg = "must be greater than 0"
            raise ValueError("{} {}".format(self.name, msg))
        self.value = value
