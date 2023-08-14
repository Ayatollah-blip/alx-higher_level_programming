#!/usr/bin/python3
def max_integer(my_list=[]):
    """function that returns bigger int in a list"""
    if my_list == []:
        return None
    max_ = my_list[0]
    for ls in my_list:
        if ls > max_:
            max_ = ls
    return max_
