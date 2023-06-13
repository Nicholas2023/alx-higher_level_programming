#!/usr/bin/python3
"""
This module contains a function that appends a string
at the end of a text file and returns the number of chr
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and
    returns the number of characters
    Args:
        filename (str): Name of file to be appended
        text (str): The text to be appended
    Returns:
        Number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        content = file.write(text)
        return content
