#!/usr/bin/python3
"""
Defines the BaseGeometry class
"""


class BaseGeometry:
    """represent a base geometry"""

    def area(self):
        """
        Calculate the area of the geometry
        Raises:
            Exception: Indicates that the `area()` method
                    is not implemented for the geometry
        Returns:
            None
        """
        raise Exception("area() is not implemented")
