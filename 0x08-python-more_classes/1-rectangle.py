#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, widt, height):
        self.__width = widt
        self.__height = height
    @property
    def height(self):
        return __height
    @height.setter
    def height(self, heit):
        if not isinstance(heit, int):
            raise TypeError("height must be an integer")
        elif heit < 0:
            raise ValueError("height must be >= 0")
        self.__height = heit
    @property
    def width(self):
        return __width
    @width.setter
    def width(self, widt):
        if  not isinstance(widt, int):
            raise TypeError("width must be an integer")
        elif widt < 0:
            raise ValueError("width must be >= 0")
        self.__width = widt

          
