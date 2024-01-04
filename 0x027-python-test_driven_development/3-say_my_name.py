#!/usr/bin/python3
"""
Module
Refer to the documentation provided in the README.md
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints My name is <first name> <last name>

    Args:
        @first_name: first name of user
        @last_name: last name of user

    Raises:
        TypeError: Raises an exception
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
