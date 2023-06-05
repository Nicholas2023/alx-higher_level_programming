#!/usr/bin/python3
"""
This module provides a function for printing full name.
It does that by combining the first and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first_name> <last_name>

    Args:
        first_name(str): First name
        last_name(str): Second name, default is ""
    Returns:
        (void): Returns nothing instead prints the first and second name
    Raises:
        TypeError: If either first or last nae is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
