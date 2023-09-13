#!/usr/bin/python3

import json
""" function that returns the JSON representation of an object (string):  """


def to_json_string(my_obj):
    """  JSON REPRESENTATION OF STRING
    Args:
        my_obj:class
    Return:
          JSON REPRESENTATION
    """
    return json.dumps(my_obj)
