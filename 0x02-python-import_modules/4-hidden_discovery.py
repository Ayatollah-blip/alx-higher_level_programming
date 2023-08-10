#!/usr/bin/python3

if __name__ == "__main__":
    """Print the names inside the hidden module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        print("{}".format(name))
