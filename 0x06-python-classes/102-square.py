#!/usr/bin/python3
'''Class definition'''


class Square:
    '''Attribute definition'''
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, (int, float)):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be a number")

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
