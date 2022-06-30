#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """Defines a rectangle
    Attributes:
        __width: width of the rectangle
        __height: height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes the rectangle
        Args:
            width (int): width of rect
            height (int): height of rect
        Returns:
            None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of __width
        Returns:
            The width of the rect
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter of __width
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter of __height
        Returns:
            The height of the rect
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter of __height
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area of the rectangle
        Returns:
            Area of rect
        """
        return (self.__width * self.height)

    def perimeter(self):
        """Calculates perimeter of rect
        Returns:
            Perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """returns a print of # in the shape of the rectange

        Returns:
            printout of # in rect format
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#"*self.__width for j in range(self.__height))
        return string
