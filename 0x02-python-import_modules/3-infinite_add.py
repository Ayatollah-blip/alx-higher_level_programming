#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    from sys import argv
    num = 0
    if len(argv) == 1:
        print("0")
    else:
        for arg in argv[1:]:
            num += int(arg)
        print("{}".format(num))
