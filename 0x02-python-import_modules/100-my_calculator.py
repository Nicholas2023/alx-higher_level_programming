#!/usr/bin/python3

if __name__ == "__main__":
    """Basic arithmetic"""
    from calculator_1 import add, sub, mul, div
    import sys

    num_args = len(sys.argv) - 1

    if (num_args != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
