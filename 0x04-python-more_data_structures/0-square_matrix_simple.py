#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    length = len(matrix)
    a = matrix[:]
    new_matrix = a
    for i in range(0, length):
        b = a[i]
        new_matrix[i] = b[:]
        length2 = len(b)
        for j in range(0, length2):
            new_matrix[i][j] = b[j] ** 2
    return(new_matrix)
