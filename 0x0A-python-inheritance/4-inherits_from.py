#!/usr/bin/python3
"""
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    Args:
        obj (object): The object to check
        a_class (type): The class to compare against
    Returns:
        bool: True if the object is an insance of a class that
                inherited from the specified class, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class)
