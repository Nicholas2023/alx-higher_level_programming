#!/usr/bin/python3
"""
A script that finds a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    A peak is an element that is not smaller than its neighbour
    Args:
        list_of_integers (list): List of integers to search for a peak
    Returns:
        (int) or (None): The peak element if found, None if the list is empty
    """

    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
