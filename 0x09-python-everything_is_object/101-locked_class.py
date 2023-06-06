#!/usr/bin/python3
"""
Defines a locked class
With only one permitted attribute
"""


class LockedClass:
    """
    Prevents the user from creating objects
    """
    __slots__ = ['first_name']
