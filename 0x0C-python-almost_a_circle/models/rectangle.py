#!/usr/bin/python3
"""
models/rectangle.py
Contains a class Rectangle that inherits from Base
Attributes:
    width : Private instance attribute; width of rectangle
    height : Private instance attribute; height of rectangle
    x : Private instance attribute; x coordinate
    y : Private instance attribute; y coordinate
Methods:
    __init__(self, width, height, x=0, y=0, id=None):
    Class constructor
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle
    Attributes:
        width (int): Width of rectangle
        height (int): Height of rectangle
        x (int): X-coordinate of the rectangle's position
        y (int): Y-coordinate of the rectangle's position
        id (int) : Unique identifier for the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int, optional): X-coordinate of the rectangle's position
            y (int, optional): Y-coordinate of the rectangle's position
            id (int, optional): Unique identifier for the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        int: Width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args:
            Value (int): Width value to be assigned
        Raises:
            TypeError: If input is not an integer
            ValueError: If width is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        int: Height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle
        Args:
            value (int): Height value to be assigned
        Raises:
            TypeError: If input is not an integer
            ValueError: If height is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        int: X-coordinate of the rectangle's position
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the X-coordinate of the rectangle's position
        Args:
            value (int): X-coordinate value to be assigned
        Raises:
            TypeError: If the input is not an integer
            ValueError: If the X-coordinate is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        int: Y-coordinate of the rectangle's position
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the Y-coordinate of the rectangle's position
        Args:
            value (int): Y-coordinate value to be assigned
        Raises:
            TypeError: If the input is not an integer
            ValueError: If the Y-coordinate is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Compute and return the area value of the Rectangle instance
        Returns:
            (int) : Area of a rectangle
        """
        a = self.width * self.height
        return a

    def display(self):
        """
        Prints in stdout the Rectangle instance with '#'
        """
        if self.width == 0 or self.height == 0:
            print("")
            return
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of Rectangle
        """
        return (
            "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
            .format(self.id, self.x, self.y, self.width, self.height)
        )

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        Args:
            *args (int): No-keyword arguments to assign to the attributes
            **kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
