#!/usr/bin/python3
""" Reading a file"""


def append_write(filename="", text=""):
    """ this function for reading file
        Args:
        filename: the file to read
    """
    with open(filename, mode='a', encoding="utf-8") as m:
        return m.write(text)
