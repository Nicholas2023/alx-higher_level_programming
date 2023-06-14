#!/usr/bin/python3
"""
Contains a function that crreates an object
from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    Args:
        filename (str): JSON text file
    Returns:
        (object): Convertes json data
    """
    with open(filename) as file:
        json_data = json.load(file)
        return json_data
