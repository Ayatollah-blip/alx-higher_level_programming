#!/usr/bin/python3
"""contains the BaseGeometry class"""


class BaseGeometry():
    """a subclass of BaseGeometry"""

    def area(self):
        """ not implemented yet """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method integr validator

        Args:
             name (string):name to check value
             value (int):validate the value if integer
        Raises:
             TypeError: If value is not an integer.
             ValueError: If value is <= 0.
	"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
