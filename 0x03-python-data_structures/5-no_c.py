#!/usr/bin/python3
def no_c(my_string):
    my_list = [i for i in my_string]
    new_string = ''
    """function that delete c in a string"""
    for x in my_list:
        if x != 'c' and x != 'C':
            new_string += x
    return new_string
