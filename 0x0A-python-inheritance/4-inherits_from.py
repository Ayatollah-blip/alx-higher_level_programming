#!/usr/bin/python3

"""
function that checks if the object is exactly an
instance of the specified class
"""


def inherits_from(obj, a_class):
    """ return if it-s the same else false
     Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
