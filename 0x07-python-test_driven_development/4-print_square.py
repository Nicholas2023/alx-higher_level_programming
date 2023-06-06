#!/usr/bin/python3
"""
This module has a function thatprints a square with
character '#'
"""


def print_square(size):
    """
    Prints a square with character '#'
    Args:
        size(int): Length of a square
    Returns:
        (str): '#' character = area of square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is < 0
        TypeError: If size is a float and < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
