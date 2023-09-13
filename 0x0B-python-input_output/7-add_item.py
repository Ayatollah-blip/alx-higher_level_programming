#!/usr/bin/python3
""" function that returns the JSON representation of an object (string):  """
import os
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

if __name__ == '__main__':
    """  mqin func
    """
    if not os.path.isfile(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('[]')

    arg = load_from_json_file("add_item.json")
    for a in sys.argv[1:]:
        arg.append(a)
    save_to_json_file(arg, "add_item.json")
