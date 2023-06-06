#!/usr/bin/python3
"""
Defines a class Rectangle with its attributes and methods
Attributes defined in this task include width and height
Methods include area, perimeter,getters,setters print and str
"""


class Rectangle:
    """
        Defines a class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize the attributes of a Rectangle
        Attributes:
            width(int): width of rectangle, default is 0
            height(int): height of rectangle, default is 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            Returns width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the new width of a rectangle
        Args:
            value(int): The new width of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Returns the height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Returns the height of a rectangle
        Args:
            value(int): The new height of a rectangle
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
            perim = 2 * (self.__width * self.__height)
        return perim

    def __str__(self):
        """
            Returns the string representation of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        rect_str = ""
        for _ in range(self.__height):
            rect_str += "#" * self.__width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        """
            Return strin representatio
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
            Print a message when an instance is deleted
        """
        print("Bye rectangle...")
