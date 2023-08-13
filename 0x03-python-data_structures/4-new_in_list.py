#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """function that returns element based on index"""
    new_list = []
    for memb in my_list:
        new_list.append(memb)
    if idx < 0:
        return new_list
    elif idx > len(new_list)-1:
        return new_list
    else:
        new_list[idx] = element
        return new_list
