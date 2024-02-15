#!/usr/bin/python3
"""
Contains the clas "Student"
"""


class Student:
    """
    This class defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        This method initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This method retrieves a dictionary representation of a Student instance.
        """
        return self.__dict__
