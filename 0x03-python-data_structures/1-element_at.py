#!/usr/bin/python3
def element_at(my_list, idx):
    """function that returns element based on index"""
    if idx < 0:
        return None
    elif idx > len(my_list)-1:
        return None
    else:
        return my_list[idx]
