#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) <= 122 and ord(s) >= 97:
            s = chr(ord(s) - 32)
        print("{}".format(s)), end="")
    print("")
