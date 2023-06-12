#!/usr/bin/python3
"""
    This module provides a function for checking if an object is
    exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the
    specified class
    Args:
        obj (object) : The object to check
        a_class (type) : The class to compare against
    Returns:
        bool: True if the object is exactl;y an instance of
                specified class, False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
