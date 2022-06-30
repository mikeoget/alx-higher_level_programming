#!/usr/bin/python3
"""This is the say_my_name module
It prints out the name it is given
"""


def say_my_name(first_name, last_name=""):
    """It prints out the names it's given"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
