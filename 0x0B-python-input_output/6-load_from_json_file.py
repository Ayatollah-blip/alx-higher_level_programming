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
    with open(filename) as f:
        return json.load(f)
