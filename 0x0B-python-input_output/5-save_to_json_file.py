#!/usr/bin/python3
"""
Contains a functions that writes an object to a text
file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file
    using JSON representation
    Args:
        my_obj (str): String to be written to a text file
        filename (str): The text file to be written on
    Returns:
        None
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
