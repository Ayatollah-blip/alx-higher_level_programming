#!/usr/bin/python3
def multiple_returns(sentence):
    """function that return tuple of length and first char"""
    ls1 = list(sentence)
    length = len(sentence)
    if length == 0:
        new_tuple = (length, None)
    else:
        new_tuple = (length, ls1[0])
    return new_tuple
