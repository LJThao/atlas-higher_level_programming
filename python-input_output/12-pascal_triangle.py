#!/usr/bin/python3
"""Function to create a
Pascal's Triangle"""


def pascal_triangle(n):
    """Function to return a list of lists of ints
    representing the Pascal's triangle of n"""

    if n <= 0:
        return []

    p_triangle = [[1]]
    while len(p_triangle) < n:
        triangle = p_triangle[-1]
        new_row = [1]

        for i in range(len(triangle) - 1):
            new_row.append(triangle[i] + triangle[i + 1])

        new_row.append(1)
        p_triangle.append(new_row)

    return (p_triangle)
