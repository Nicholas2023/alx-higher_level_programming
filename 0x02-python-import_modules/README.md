# 0x02. Python - Import Modules

This project contains Python scripts and modules to demonstrate the use of import statements and modules in Python. The tasks in this project cover the following concepts:

* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function `dir()`
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs


## Files

* `0-add.py`: A program that imports a function from the file `add_0.py` and prints the result of the addition of 1 + 2.
* `add_0.py`: A Python module that contains a function that adds two integers
* `1-calculation.py`: A program that imports functions from the file `calculator_1.py`, performs arithmetic operations on two numbers, and prints the results.
* `calculator_1.py`: A Python module that contains functions for performing arithmetics operations.
* `2-args.py`: A program that prints the number of arguments passed to it and the list of arguments.
* `3-infinite_add.py`: A program that takes any number of arguments and prints the result of their addition.
* `4-hidden_discovery.py`: A program that prints all the names defined by a compiled module `hidden_4.pyc`.
* `hidden_4.pyc`: A compiled Python module that defines variables with unusual names.


## Usage

To run any of the Python scripts in this project, navigate to the directory containing the script in your terminal and run the command `./<script_name>`.

For example, to run`0-add.py`:
```
$ ./0-add.py
1 + 2 = 3
```

To run `2-args.py` with arguments:
```
$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
```

## Credits

This project is part of the ALX Higher-Level Programming curriculum, and the Python scripts were created by ALX School staff.

