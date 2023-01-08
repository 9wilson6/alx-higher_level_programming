#!/usr/bin/python3
from sys import argv

argv_length = len(argv) - 1
if __name__ == "__main__":
    if argv_length > 1:
        print("{:d} arguments:".format(argv_length))
    elif argv_length == 0:
        print("{:d} arguments.".format(argv_length))
    else:
        print("{:d} argument:".format(argv_length))
    for arg_item in argv:
        if argv.index(arg_item) == 0:
            continue
        print("{:d}: {}".format(argv.index(arg_item), arg_item))
