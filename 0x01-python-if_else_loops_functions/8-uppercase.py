#!/usr/bin/python3
def uppercase(str):
    for string in str:
        if ord(string) <= 122 and ord(string) >= 97:
            string = chr(ord(string))-32
        print("{}".format(string)), end="")
    print("")
