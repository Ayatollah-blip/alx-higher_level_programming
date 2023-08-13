#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """function that prints all the elements in a list in reverse"""
    if len(my_list) > 1:
        for member in my_list[::-1]:
            print("{:d}".format(member))
