#!/usr/bin/python3
"""
Module for Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Representation of a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return the string representation of a Square instance
        """
        return (
                "[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width)
        )

    @property
    def size(self):
        """
        Getter for the size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute
        """
        self.width = value
        self.height = value

    def area(self):
        """
        Return the area of the Square
        """
        return self.width * self.width

    def display(self):
        """
        Print the Square with the '#' chr
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
