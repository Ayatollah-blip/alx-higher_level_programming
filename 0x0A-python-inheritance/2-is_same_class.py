#!/usr/bin/python3

""" 
function that checks if the object is exactly an instance of the specified class
"""

def is_same_class(obj, a_class):
    """ return if it-s the same else false 
     Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """

    if isinstance(obj, a_class):
        return True
    return False

