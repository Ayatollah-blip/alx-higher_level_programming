#!/usr/bin/python3
""" function that returns the JSON representation of an object (string):  """
import json


def load_from_json_file(filename):
    """  JSON REPRESENTATION OF STRING
    Args:
        my_obj:python obj
    Returns:
          JSON REPRESENTATION
    """
    with open(filename, 'r') as f:
        json.load(f)
