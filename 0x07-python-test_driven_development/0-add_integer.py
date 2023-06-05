#!/usr/bin/python3
"""This is a package-level docstring for the add_integer module.
The add_integer takes two args a and b. b is set to 98 by default
It returns the sum of two integers after casting them to int
If a or b is not an integer or float, a TypeError excp is raised
"""


def add_integer(a, b=98):
    """
        Adds two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
