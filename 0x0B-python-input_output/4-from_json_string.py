#!/usr/bin/python3
""" function that returns the JSON representation of an object (string):  """
import json


def from_json_string(my_str):
    """  JSON REPRESENTATION OF STRING
    Args:
        my_obj:python obj
    Returns:
          JSON REPRESENTATION
    """
    return json.loads(my_str)
