#!/usr/bin/python3
def uppercase(str):
    for string in str:
        if ord(string) < 90 and ord(string) > 64:
            print("{}".format(chr(ord(string) - 25)))
        else:
	    print("{}".format(string))
    print()
