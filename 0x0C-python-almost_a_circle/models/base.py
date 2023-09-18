#!/usr/bin/python3
""" the is the base classe  """


class Base:
    """ clase base  """
    __nb_objects = 0

    def __init__(self, id=None):
        """ function init
        Args:
            self:initiation of the class
            id:id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
