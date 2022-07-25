#!/usr/bin/python3
"""
Lookup function prints out a list of class methods and attributes
"""


def lookup(obj):
    """looks up the obj object attributes and methods"""
    return dir(obj)
