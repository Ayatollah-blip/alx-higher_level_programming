#!/usr/bin/python3
""" function that returns the JSON representation of an object (string):  """
import json


def save_to_json_file(my_obj, filename):
    """  JSON REPRESENTATION OF STRING
    Args:
        my_obj:python obj
    Returns:
          JSON REPRESENTATION
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
