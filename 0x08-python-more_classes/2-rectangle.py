#!/usr/bin/python3
"""
Defines a rectangle with its attributes and methods
The methods defines are area and perimeter instances
"""


class Rectangle:
    """Class Attributes"""
    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle
        Attributes:
            width(int): width measurement of the rectangle.
            height(int): height measurement of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args:
            value(int): New width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Returns the new height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the new height of the rectangle
        Args:
            value(int): The new height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of a rectangle
        """
        a = self.__width * self.__height
        return a

    def perimeter(self):
        """
        Returns the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perim = 2 * (self.__width + self.__height)
        return perim
