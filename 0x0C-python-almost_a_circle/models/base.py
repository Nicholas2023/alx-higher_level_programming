#!/usr/bin/python3
"""
models/base.py
Contains the implementation of the Base class,
which serve as the base for all other classes in this project
"""


class Base:
    """
    Base class for managing id attributes in all future classes.
    Attributes:
        __nb_objects (int): Private class attribute to keep
        track of the number of objects created
        id (int): Public instance attribute representing the
        unique identifier of an object.
    Methods:
        __init__(self, id=None): Class constructor method to
        initialize the Base object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class
        Args:
            id (int, optional): Identifier value for the object
            Default to None
            If provided, assigns the value of id to the id attribute
            If not provided, increments __nb_objects and assigns the
            new value to the id attribute
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
