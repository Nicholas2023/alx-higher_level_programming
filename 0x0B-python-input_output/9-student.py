#!/usr/bin/python3
"""
Contains a class Student
"""


class Student:
    """Defining class attributes"""
    def __init__(self, first_name, last_name, age):
        """
        Initialize class attributes
        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary rep of a student
        Returns:
            (dictionary): Student information
        """
        attributes = {}
        for attr_name, attr_value in self.__dict__.items():
            attributes[attr_name] = attr_value
        return attributes
