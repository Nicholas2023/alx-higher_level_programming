#!/usr/bin/python3
"""
This module provides a function for checking if an object is an
instance of, or if the object is an instance of a class that
inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an
    instance of a class that inherited from, the  specified class.
    Args:
        obj (object): The object to check
        a_class (type): The class to compare against
    Returns:
        bool: True if the object is an instance of the specified class
            or its subclass, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
