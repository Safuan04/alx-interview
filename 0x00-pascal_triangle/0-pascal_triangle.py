#!/usr/bin/python3
"""Defining a function pascal_triangle"""


def pascal_triangle(n):
    """Generates Pascal's triangle of n rows
    and returns it as a list of lists."""
    if n <= 0:
        return []

    pascal = []

    for i in range(n):
        current_row = []
        if i == 0:
            pascal.append([1])
        else:
            for j in range(i + 1):
                if j == 0 or j == i:
                    current_row.append(1)
                else:
                    value = pascal[i - 1][j] + pascal[i - 1][j - 1]
                    current_row.append(value)
            pascal.append(current_row)

    return pascal
