#!/usr/bin/python3
""" function that returns the JSON representation of an object (string):  """
import json


def to_json_string(my_obj):
    """  JSON REPRESENTATION OF STRING
    Args:
        my_obj:python obj
    Returns:
          JSON REPRESENTATION
    """
    return json.dumps(my_obj)
