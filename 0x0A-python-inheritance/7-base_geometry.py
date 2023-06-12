#!/usr/bin/python3
"""
This module defines a BaseGeometry
"""


class BaseGeometry:
    """Defines attributes of the geometry"""
    def area(self):
        """
        Calculate the area of the geometry
        Raises:
            Exception: Indicated the area() method is not implemented
        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer
        Args:
            name(str) : The name of the value.
            value (int) : The value to validate
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0.
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
