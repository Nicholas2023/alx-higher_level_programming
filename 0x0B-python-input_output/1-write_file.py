#!/usr/bin/python3
"""
This module contains a function that writes into a file
and returns number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and
    and returns number of characters written
    Args:
        filename (str): File written on
        text (str): String to be written
    Returns:
        Number of characters written to text file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        content = file.write(text)
        return content
