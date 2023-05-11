#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sum = 0
    args = sys.argv[1:]
    for arg in args:
        sum += int(arg)
print(sum)
