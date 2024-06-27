#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """pascal_triangle"""
    result = []
    prev_row = []
    if n > 0:
        for i in range(n):
            row = []
            elems = i + 1
            for j in range(elems):
                if (j == 0 or j == i):
                    row.append(1)
                elif j < len(prev_row):
                    row.append(prev_row[j - 1] + prev_row[j])
                elif j == len(prev_row):
                    row.append(prev_row[0])
            prev_row = row
            result.append(row)
    return result
