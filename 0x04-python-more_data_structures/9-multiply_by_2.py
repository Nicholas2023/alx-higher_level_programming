#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dict = {}
    for key, val in a_dictionary.items():
        n_dict[key] = val * 2
    return n_dict
