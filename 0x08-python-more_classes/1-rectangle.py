#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""
    """ __init__ method   """
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height
    """ height property """
    @property
    def height(self):
        return __height
    """ height setter  """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """ height property  """
    @property
    def width(self):
        return __width
    """ height setter  """
    @width.setter
    def width(self, value):
        if  not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

          
