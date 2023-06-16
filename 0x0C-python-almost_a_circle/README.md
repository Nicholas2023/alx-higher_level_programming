# Almost a Circle :smile:

This repository contains the implementation of the `Rectangle` and `Square` clases, which are part of the "Almost a Circle" project. These classes are written in Python and inherit from the `Base` class

## Installation
To use the classes in this project, follow these steps:

1. Clone the repository

```bash
$ git clone https://github.com/your-username/alx-higher_level_programming.git
```
2. Navigate to the project directory:

```bash
$ cd alx-higher_level_programming/0x0C-python-almost_a_circle
```

3. You can now import and use the `Rectangle` and `Square` classes in your Python scripts.

## Usage

## `Rectangle` Class

The `Rectangle` class represents a rectangle shape. It inherits from the `Base` class and provides additional functiopnality specific to rectangles.

### Class Constructor

The constructor for the `Rectangle` class has the following signature:

```.py
def __init__(self, width, height, x=0, y=0, id=None):
    ...
```

* `width` (integer): The width of the rectangle
* `height` (integer): The height of the rectangle
* `x` (integer, optional): The x-coordinate of the rectangle's position. Default is 0
* `y` (integer, optional): The y-coordinate of the rectangle's position. Default is 0
* `id` (integer, optional): The unique identifier for the rectangle. If not provided, a new will be assigned automatically

### Methods:

### The `Rectangle` class provide the following methods:

* `area(self)`: Calculates and returns the area of the rectangle
* `display(self)`: Prints a visual representation of the rectangle using the `#` character
* `__str__(self)`: Returns a string representation of the rectangle in the format `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
* `update(self, *args, **kwargs)`: Updates the attributes of the rectangle using positional or keyword arguments

## `Square` Class

The `Square` class represents a square shape. It inherits from the `Rectangle` class and provides additional funtionality specific to squares

### Class Constructor

The constructor for the `Square` class has the following signature:

```.py
def __init__(self, size, x=0, y=0, id=None):
    ...
```

* `size` (integer): The size (width and height) of the square
* `x` (integer, optional): The x-coordinate of the square's position. Default is 0
* `y` (integer, optional): The y-coordinate of the square's position. Default is 0
* `id` (integer, optional): The unique identifier for the square. If not provided, a new identifier will be assigned automatically

### Methods:

The `Square` class inherits all the methods from the `Rectangle` class and provides additional functionality specific to squares

## Examples

Here are some examples demonstrating the usage of the `Rectangle` and `Square` classes:

```.py
from models.rectangle import Rectangle
from models.square import Square

# Create a rectangle and print its ID
r = Rectangle(10, 5)
print(r.id)  # Output: 1

# create a square and print its area
s = Square(7)
print(s.area())  # Output: 49

# Update the attributes of a rectangle using positional arguments
r.update(2, 4, 3, 2)
print(r)  # Output: [Rectangle] (2) 3/2 - 4/3

# Update the attributes of a square using keyword arguments
s.update(x=1, y=2)
print(s)  # Output: [Square] (2) 1/2 - 7/7
```

For more detailed examples and usage instructions, please refer to the individual class implementations

## License

This project is licensed under the ALX SE.
