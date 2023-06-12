#!/usr/bin/python3
"""
This module inherites Geometry function
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initialize the current class"""
    def __init__(self, width, height):
        """
        Initialize a Rectangle
        Args:
            width (int): The width measurement of the rectangle
            height (int): The height  measurement of the rectangle
        Raises:
            TypeError: If measurements are not integers
            ValueError: If measurements are less than 0
        Returns:
            None
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
