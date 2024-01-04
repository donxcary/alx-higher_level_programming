#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """
    Function to test if max_integer works
    """
    def test_max(self):
        new_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(new_list), 4)
        new_list = []
        self.assertEqual(max_integer(new_list), None)
        new_list = [0]
        self.assertEqual(max_integer(new_list), 0)
        new_list = [1]
        self.assertEqual(max_integer(new_list), 1)
        new_list = [0, 2, 1]
        self.assertEqual(max_integer(new_list), 2)
        new_list = [-1, -1]
        self.assertEqual(max_integer(new_list), -1)
        new_list = [0, 2.4, 2, 3]
        self.assertEqual(max_integer(new_list), 3)
        new_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(new_list), 4)
        self.assertEqual(max_integer(), None)
