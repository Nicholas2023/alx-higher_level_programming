#!/usr/bin/python3
"""Define a class-checking function"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of
    Args:
        obj (object) : The object to check
        a_class (type) : The class to compare against
    Returns:
        bool: True if the object is exactl;y an instance of
                specified class, False otherwise
    """

    return (type(obj) == a_class)
