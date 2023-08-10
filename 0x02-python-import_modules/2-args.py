#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""

    from sys import argv

    c = len(argv) - 1
    if c == 1:
        print("{} argument:".format(c))
    else:
        print("{} arguments".format(c))
    for i in range(c):
        print("{}: {}".format(i+1, argv[i+1]))
        i += 1
