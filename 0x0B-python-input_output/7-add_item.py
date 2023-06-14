#!/usr/bin/python3
"""
Contains a script that adds all arguments of a Python
list, and then save them to a file
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

"""Load existing items from file"""
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

"""Add new items from cmd line args"""
items.extend(sys.argv[1:])

"""Save the updated items to file"""
save_to_json_file(items, filename)
