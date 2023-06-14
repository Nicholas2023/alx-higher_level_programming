#!/usr/bin/python3
"""
Contains a function that returns the dictionary descrip
with simple data structures(listn dic, str, int and bolls)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dict desription for JSON
    serialization of an object
    Args:
        obj (Object): Instance of a class
    Returns:
        (dictionary) simple data structure for JSON
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Object is not serializable")

    attributes = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            attributes[attr_name] = attr_value

    return attributes
