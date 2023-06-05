#!/usr/bin/python3
"""
matrix_divided.py

This module provides a function to divide all elements of a matrix by a given number.

The function takes a matrix represented as a list of lists of integers or floats and a divisor as inputs.

It divides each element of the matrix by the divisor, rounding the result to 2 decimal places.

The function returns a new matrix with the updated values.

Usage:
    matrix_divided(matrix, div)

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    result = matrix_divided(matrix, 3)
    # Output: [[0.33, 0.67, 1.0], [1.38, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number

    Args:
        matrix(list): Represents a list of lists of integers and floats
        div(float or int): The matrix elements divisor
    Returns:
        list: A new matrix with the containing results of the operation
    Raises:
        TypeError: If matrix's elements or `div` is not a float or int
        TypeError: If each row of the matrix does not have same size
        ZeroDivisionError: If `div` is zero
    """
    msg = (
        'matrix must be a matrix (list of lists) of integers/floats',
        'Each row of the matrix must have the same size',
        'div must be a number',
	'division by zero'
    )
    size = [0, 0]
    new_matrix = []

    '''Validate matrix input'''
    if not isinstance(matrix, list):
        raise TypeError(msg[0])
    size[0] = len(matrix)
    if size[0] == 0:
        raise TypeError(msg[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg[0])
        elif len(row) == 0:
            raise TypeError(msg[0])
        else:
            if size[1] == 0:
                size[1] = len(row)
            elif len(row) != size[1]:
                raise TypeError(msg[1])
            for i in row:
                if not isinstance(i, (int, float)):
                    raise TypeError(msg[0])

    '''Validate div input'''
    if not isinstance(div, (int, float)):
        raise TypeError(msg[2])
    elif div == 0:
        raise ZeroDivisionError(msg[3])
    else:
        for row in matrix:
            new_matrix_row = list(map(lambda x: round(x / div, 2), row))
            new_matrix.append(new_matrix_row)
        return new_matrix
