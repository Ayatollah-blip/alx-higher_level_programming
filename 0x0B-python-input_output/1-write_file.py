#!/usr/bin/python3
""" Reading a file"""


def write_file(filename="", text = ""):
    """ this function for reading file 
        Args:
        filename: the file to read
    """
    with open(filename, mode='r', encoding="utf-8") as m:
       print(m.read(), end='')    
