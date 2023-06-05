# MOre Classes and Objects in Python :smile:

This repository contains Python code for working with classes and objects. Each file represents a different task, and they build upon othe to demonstarte various concepts related to classes and objects in Python.

## Files :love_you_gesture:

### 0-rectangle.py:

Defines an empty class `Rectangle`.

### 1-rectangle.py:

Defines a class `Rectangle` with private instance attributes `width` and `height`, along with getters and setters for these attributes.

### 2-rectangle.py:

Extends the `Rectangle` class with public instance methods `area` and `perimeter` to calculate the area and perimeter of the rectangle.

### 3-rectangle.py

Adds a string representation for the `Rectangle` class, which prints the rectangle using `#` character
### 4-rectangle.py:

Adds an `eval` representation for the `Rectangle` class, which allows creating a new instance of the class using `eval`.

### 5-rectangle.py:

Adds a message when an instance of `rectangle` is deleted using the `del` statement.

### 6-rectangle.py:

Adds a class attribute `number_of_instances` to keep track of the number of instances of the `Rectangle class.

## Usage :eagle:

To use any of the classes defined in the above files, you can import them into your Python code and create instances of the classes. Here's an example:

```
from 0-rectangle import Rectangle

my_rectangle = Rectangle()
print(type(_rectangle))  # <class '0-rectangle.Rectangle'>
print(my_rectangle.__dic__)  # {}
```

You can also modify the attributes of the instances and access their methods:

```
from 1-rectangle import Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.area())  # 8
print(my_rectangle.perimeter()) # 12

my_rectangle,width = 10
my_rectangle.height = 3
print(str(my_rectangle) # ##
			# ##
			# ##
	print(repr(my_rectangle)) # <1-rectangle.Rectangle object at 0x7f92a75a2eb8>
```

Feel free to explore and use the different classes provided in this repository according to your requirements.

## Contributing :wink:

This repository is part of an exercise/project and contributions are not accepted.
