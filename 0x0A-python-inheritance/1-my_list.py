#!/usr/bin/python3
"""
    This module defines the MyList class, which is a subclass of list
"""


class MyList(list):
    """
        A subclass of list that provides additional functionality
        for printing the list in sorted order
    """
    def __init__(self):
        """Initializes the object/instance"""
        super().__init__()

    def print_sorted(self):
        """
            Prints the list in sorted order
        """
        sorted_list = sorted(self)
        print(sorted_list)
