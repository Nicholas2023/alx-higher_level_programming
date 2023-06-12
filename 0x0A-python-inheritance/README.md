# 0x0A. Python - Inheritance :smile:

This repository contains Python scripts and classes for the "0x0A. Python - Inheritance" project. The project focuses on inheritance in Python and covers various concepts such as object attributes, method lookup, class hierachy and method overriding.

## Files

This repository consists of the following files:

* ### 1. `0-lookup.py` : 
A Python script that defines a function lookup(obj) to retrieve the list of available attributes and methods of an object.

* 2. `1-my_list.py` : 
A Python script that defines a class MyList that inherits from the list class. It adds a public instance method print_sorted() to print the list in ascending order.

* 3. `2-is_same_class.py` : 
A Python script that defines a function is_same_class(obj, a_class) to check if an object is an instance of a specified class.

* 4. `3-is_kind_of_class.py` : 
A Python script that defines a function is_kind_of_class(obj, a_class) to check if an object is an instance of a specified class or a class that inherits from it.

* 5. `4-inherits_from.py` : 
A Python script that defines a function inherits_from(obj, a_class) to check if an object is an instance of a class that inherits (directly or indirectly) from a specified class.

* 6. `5-base_geometry.py` : 
A Python script that defines an empty class BaseGeometry as a base class for geometric operations.

* 7. `6-base_geometry.py` : 
A Python script that extends the BaseGeometry class by adding a public instance method area() that raises an exception indicating that the method is not implemented.

* 8. `7-base_geometry.py` : 
A Python script that further extends the BaseGeometry class by adding a public instance method integer_validator(name, value) to validate an integer value.

* 9. `8-rectangle.py` : 
A Python script that defines a class Rectangle that inherits from BaseGeometry. It implements the __init__() method to initialize the private attributes width and height and adds integer validation.

* 10. `9-rectangle.py` : 
A Python script that extends the Rectangle class by implementing the area() method and customizing the print() and str() behavior.

* 11. `10-square.py` : 
A Python script that defines a class Square that inherits from Rectangle. It overrides the __init__() method to accept only the size parameter and adds integer validation.

* `11-square.py` : 
A Python script that further extends the Square class by implementing the area() method.

## Usage
Each Python script can be executed independently to test the functionality of the implemented classes and functions.

For example, to test the `MyList` class from `1-my_list.py`, run the following command:

```bash
$ ./1-main.py
```
This will output the list before and after calling the `print_sorted()` method.

## Requirements
The scripts are written in Python 3. The usage of built-in modules is prohibited, and the scripts should be run without any additional dependencies.

## Author
This project is created and maintained by `Odhiambo Nicholas Otieno`
