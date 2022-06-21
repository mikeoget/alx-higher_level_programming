#!/usr/bin/python3
"""This is a class Square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square being defined
    """
    def __init__(self, size):
        """Initializes the square:

        Args:
            size (int): size of the side of the square

        Returns: None
        """
        self.__size = size
