#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

print("{} {}:".format(num_args, "argument" if num_args == 1 else "arguments"))
for i, arg in enumerate(args):
    print("{}: {}".format((i+1), arg))
