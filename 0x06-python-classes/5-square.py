#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    
    Attributes:
        __size (int): size of a side of the square
        __position (tuple): position of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square

        Args:
            size (int): size of a side of the square
            position (tuple): position

        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates the square's area
        
        Returns:
            The area of the square
        """
        return int(self.__size) * int(self.__size)

    @property
    def size(self):
        """retrieves the size
        
        Returns:
            the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size
        
        Args:
            value (int): side of the square
        
        Returns:
            the size as value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """retrieves the position of the #

        Returns:
            the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position

        Args:
            value (int): the positional value
        
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
               raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints out square of a character

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(['#' for j in range(self.__size)]))
