#!/usr/bin/python3

if __name__ == "__main__":
    '''Handle basic arithmetics'''
    from calculator_1 import add, sub, mul, div
    import sys
    num_args = len(sys.argv) - 1

    if (num_args != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (sys.argv[2] == "+"):
        print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
    elif (sys.argv[2] == "-"):
        print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
    elif (sys.argv[2] == "*"):
        print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
    elif (sys.argv[2] == "/"):
        print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
    else:
        print("Unknown operator. Available operator: +, -, * and /")
        sys.exit(1)
