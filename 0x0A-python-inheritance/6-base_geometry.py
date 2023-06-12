#!/usr/bin/python3
"""
Defines the BaseGeometry class
"""


class BaseGeometry:
    def area(self):
        """
        Calculate the area of the geometry
        Raises:
            Exception: Indicates that the `area()` method
                    is not implemented for the geometry
        Returns:
            None
        """
        raise Exception("Area() is not implemented")
