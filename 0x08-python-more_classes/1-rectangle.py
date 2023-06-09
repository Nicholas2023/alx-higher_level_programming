#!/usr/bin/python3
"""
Defines a rectangle class
"""


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle

        Attributes:
            width(int): Width measurement of the rectangle, default is 0
            height(int): Height measurement of the rectangle, default is 0
        """
        '''Object definition'''
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args:
            value(int): The new width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        Args:
            value(int): The new height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
