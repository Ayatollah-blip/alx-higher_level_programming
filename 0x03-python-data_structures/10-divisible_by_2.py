#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """function that returns a list of bool if divisible by 2 """
    new_list = []
    for mst in my_list:
        if mst % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
