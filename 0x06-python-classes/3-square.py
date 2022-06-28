#!/usr/bin/python3
"""Class square defined"""


class Square:
    """Defines a square

    Attributes:
        __size (int): sides of the square
    """
    def __init__(self, size=0):
        """Initializes the square

        Args:
            size (int): sides of the square

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            Area of square
        """
        return self.__size ** 2
