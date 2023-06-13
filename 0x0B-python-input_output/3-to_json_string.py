#!/usr/bin/python3
"""
This module contains a function that returns
a JSON representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object
    Args:
        my_obj (str): The string to be converted to JSON string
    Returns:
        (json): A representation of an object
    """
    js_str = json.dumps(my_obj)
    return js_str
