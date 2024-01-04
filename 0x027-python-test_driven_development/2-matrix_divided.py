#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def matrix_divided(matrix, div):
    """
    A simple function that divides all elements of a matrix

    Args:
        @matrix: a list of lists of integers or floats
        @div: the divisor

    Returns:
        a new matrix

    Raises:
        TypeError: Raises an exception
        ZeroDivisionError: Raises an exception
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    msg = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(message)
    else:
        for i in matrix:
            if type(i) is not list:
                raise TypeError(message)
            for j in i:
                if type(j) not in [int, float]:
                    raise TypeError(message)
    length = []
    for i in matrix:
        a = len(i)
        length.append(a)
    for a in length:
        for j in length:
            if a != j:
                raise TypeError(msg)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    b = 0
    for i in matrix:
        new_matrix.append([])
        for j in i:
            a = round(j/div, 2)
            new_matrix[b].append(a)
        b = b + 1
    return (new_matrix)
