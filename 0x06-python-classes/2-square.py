#!/usr/bin/python3
"""A square class is defined"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of side of square
    """
    def __init__(self, size=0):
        """Instantiates a square

        Args:
            size (int): size of side of square

        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
