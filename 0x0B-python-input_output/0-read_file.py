#!/usr/bin/python3
"""
This module has a function that reads a file
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout
    Args:
        filename (str) : The file that is to be read
    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content, end='')
