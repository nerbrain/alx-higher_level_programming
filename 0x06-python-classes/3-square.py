#!/usr/bin/python3
"""Defines square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing class
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of the square
        """

        return (self.__size ** 2)
