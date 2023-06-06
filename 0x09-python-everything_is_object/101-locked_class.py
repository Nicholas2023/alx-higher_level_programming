#!/usr/bin/python3
class LockedClass:
    """
    Prevents the user from creating objects
    """
    __slots__ = ['first_name']
