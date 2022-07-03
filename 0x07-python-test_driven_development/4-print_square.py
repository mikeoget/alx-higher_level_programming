#!/usr/bin/python3
"""This is the "print_square" module
It prints a square of a specific size using #
"""


def print_square(size):
    """Prints a square of a given size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    if size > 0:
        for i in range(size):
            print("#" * size + "\n", end="")
