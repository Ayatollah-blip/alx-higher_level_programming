#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    c = len(argv) - 1 
    if c == 1:
        print("{} argument:".format(c))
    else:
        print("{} arguments".format(c))
    i = 1
    for arg in argv[1:]:
        print("{} : {}".format(i, arg))
        i += 1
