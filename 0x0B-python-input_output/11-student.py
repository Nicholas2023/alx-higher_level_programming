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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary rep of a student
        Args:
            attrs (str): Attributes to the class
        Returns:
            (dictionary): Student information
        """
        if attrs is None:
            return self.__dict__
        else:
            attributes = {}
            for attr_name in attrs:
                if attr_name in self.__dict__:
                    attributes[attr_name] = self.__dict__[attr_name]
            return attributes

    def reload_from_json(self, json):
        """
        Replaces all attibutes of the Student instance
        Args:
            json (dictionary): A dictionary key
        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
