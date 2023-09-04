#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width = 0, height = 0):
        """ __init__ method   """
	self.__width = width
        self.__height = height
       @property
    def height(self):
        """ height property """
       return __height 
    @height.setter
    def height(self, value):
        """ height setter  """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    @property
    def width(self):
        """ height property  """
        return __width
    @width.setter
    def width(self, value):
        """ width setter """
        if  not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

          
