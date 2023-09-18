#!/usr/bin/python3
""" First Rectangle  """
from models.base import Base


class Rectangle(Base):
    """ A rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ The condtructor
        Args:
            width - The width of the class
            height - The height of the class
            x - the x coordinate
            y - The y coordinate
        Raises:
            TypeError: if the input is not integer
            ValueError: if width and height values are under or equal 0
            ValueError: if x and y are under 0
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ The getter of the private attribute width
        Returns:
            The width value
        """
        return self.__width

    @width.setter
    def width(self, width):
        """The setter for the private attribute __width
        Args:
            width - the width value
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """The getter of the private attribute height
        Returns:
            The height value
        """
        return self.__width

    @height.setter
    def height(self, height):
        """The setter for the private attribute __height
        Args:
            height - the height value
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ The getter of the private attribute x
        Returns:
            The x value
        """
        return self.__x

    @x.setter
    def x(self, x):
        """The setter for the private attribute __x
        Args:
            x - the x value
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """The getter of the private attribute y
        Returns:
            The y value
        """
        return self.__y

    @y.setter
    def y(self, y):
        """The setter for the private attribute __y
        Args:
            y - the y value
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be >= 0")
        self.__y = y
