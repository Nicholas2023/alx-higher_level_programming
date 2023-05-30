# Python-Classes and Objects :smile:

This repository contains Python script that demonstrate the implementation of classes and objects in Python. Each script focuses on a specific task related to classes and objects.

## Tasks

## 0.My first square

Create an empty class `Square` that defines a square. The class does not have any attributes or methods.

## 1. Square with size

Define a class `square` that represents a square. The class has a private instance attribute `size`, which is instantiated with a given size value. The size attribute is private to control the type and value of the size. No type or value verification is performed in this task.

## 2. Size validation

Enhance the `Square` class to include validation for the `size` attribute. The class should raise a `TypeError` exception with the message "Size must be an integer" if the provided size is not an integer. If the size is less than 0, a `ValueError` exception should be raised with the message "size must be >= 0"

## 3. Area of a square

Add a public instance method `area` to the `Square` class. This method calculates and returns the area of the square based on its size. The `size` attribute must still be validaated according to the previous task.

## 4. Access and update private attribute

Add getter and setter methods for the private `size`, and the stter method should set the value of `size` after validating it. The validation rules are the same as in task 2.

## 5. Printing a square

Implement a public instance method `my_print` in the `Square` class that prints a square using the '#' character. The size of the square is determined by the `size` attribute. If the size is 0, an empty line should be printed.

## 6. Coordinates of a square

Extend the `Square` class to include a private instance attribute `position`, which represents the position of the square. The `position` attribute is a tuple of two positive integers. Add getter and setter methods for the `position` attribute, and validate that the `position` value is a tuple of two positive integers.

## 7. Singly linked list

Create a class `Node` theat represents a node of a singly linked list. Each node has a private instance atttribute `data` (integer) and a private instance attribute `next_node` (another Node object). Implement getter and setter methods for both attributes. Additionally, create a class `SinglyLinkedList` that represents a singly linked list. The `SinglyLinkedList` class has a private instance attribute `head` which points to the first node into the correct sorted position in the list (in increasing order).

## 8. Print Square instance

Extend the `Square` class to provide a string representation of the square object a `Square. When printing a `Square` instance, it should display the square using the '#' character, similar to the `my_print` method implemented in task 5.

## Requirements

* Python 3.6 or higher

## Usage

1. Clone the repository
```
$ git clone https://github.com/your_username/alx-higher_level_programming.git
```

2. Navigate to the appropriate task directory:
```
$ cd alx-higher_level_programming/0x06-python-classes
```

3. Run the desired Python script:
```
$ ./0-main.py
```

Replace `0-main.py` with the name of the script you want to execute.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```
Feel free to customize the README file according to your needs.
```
