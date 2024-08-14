#!/usr/bin/python3
"""
rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix by 90 degrees clockwise.
    The rotation is done in place.
    """
    n = len(matrix)
    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row to achieve the rotation
    for i in range(n):
        matrix[i].reverse()
