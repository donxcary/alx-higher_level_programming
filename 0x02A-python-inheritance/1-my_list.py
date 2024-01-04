#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def __init__(self, iterable=[]):
        self.new_list = super().__init__(item for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, item)

    def __getitem__(self, index):
        return super().__getitem__(index)

    def append(self, item):
        super().append((item))

    def print_sorted(self):
        """
        Function that prints the list, but sorted (ascending sort)
        """
        new_list = self
        print(sorted(new_list))
