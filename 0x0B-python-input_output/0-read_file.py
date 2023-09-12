#!/usr/bin/python3
""" Reading a file"""


def read_file(filename=""):
    """ this function for reading file 
        Args:
        filename: the file to read
    """
    with open(filename, mode='r', encoding="utf-8") as m:
       print(m.read(), end='')    
