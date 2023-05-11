#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    n_arg = len(args)

    print("{} {}:".format(n_arg, "argument" if n_arg == 1 else "arguments"))
    for i, arg in enumerate(args):
        print("{}: {}".format((i+1), arg))
