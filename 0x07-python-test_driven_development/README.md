# Test-Driven Development with Python :wink:

This rrepository contains Python scripts that demonstrate the concept of Test-Driven Development(TDD). Each script corresponds to a specific task and includes a set of test cases to ensure the correctness of the implented functions.


## List of Scripts :smile:

### :point_right: 1. add_integer.py: 

This script defines a function `add_integer(a, b)` that adds two integers. The function handles cases where `a` and `b` are neither integers or floats. If `a` or `b` is a float, it is cast to an integer. If either `a` or `b` is not a numeric value, a `TypeError` is raised. The function returns the sum of `a` and `b`.

### :point_right: 2. matrix_divided.py: 

This script contains a function `matrix_divided(matrix, div)` that divides all elements of a matrix by a given number. The `matrix` parameter should be a list of lists containing integers or floats. If `div` is zero, a `zeroDivisionError` is raised. The function returns a new matrix with all elements divided by `div`, round to 2 decimal places.

### 3. say_my_name.py: :point_left: 

This script defines a function `say_my_name(first_name, last_name="")` that prints a person's name. The `first_name` and `last_name` parameters must be strings. If either parameter is not a string, a `TypeErro` is raised. The function prints the message "My name is <first_name><last_name>". If `last_name` is not provided, only the first name is printed.

### 4. print_square.py: :raised_hands:

This script contains a function `print_square(size)` that prints a square using the '#' character. The `size` parameter specifies the length of each side of the square. The `size` must be a non-negative integer. If `size` is not an integer or less than zero, a `TypError` or `ValueError` is raised, respectively. The function prints the square with no spaces between the characters.

### 5. text_indentation.py: :point_left:

This script defines a function `text_indentation(text)` that adds two new lines after each occurrence of '.', '?', or ':'. The `text` parameter must be a string. If `text` is not a string, a `TypeError` is raised. The function splits the text into sentences and adds two new lines after each sentence. The resulting text is printed with no spaces at the beginning or end of each line.

### 6. max_integer.py: :writing_hand:

This script contains a function `max_integer(list=[])` that finds the maximum integer in a given list. The `list` parameter should be a list of integers. If the list is empty, the function returns `None`. If the list contains elements that are not integers, a `typeError` is raised. The function iterates over the list and returns the maximum integer.

### 7. matrix_mul.py: :+1:

This script defines a function `matrix_mul(m_a, m_b)` that performs matrix multiplication between two matrices. The `m_a` and `m_b` parameters should be lists of lists containing integers or floats. The matrices must be valid, meaning they should have the same number of columns in the first matrix as the number of rows in the second matrix. If the matrices are not valid or do not meet the requirements, appropriate exceptios are raised. The function returns a new matrix that is the result of the matrix multiplication.

## Running the Tests :unicorn:

To run the test cases for each script, execute the following command:

```
python -m unittest discover -p "*_test.py"
```

This command will discover and execute all test files that match the pattern `*_test.py`. The test cases are defined in separate test files for each script and ensure the correctness of the implemented functions.

## License :tada:

This repository is licensed under the MIT License. You can find more details in the LICENSE file.

Feel free to explore and learn about Test-Driven Development by examining the code and running the test cases. Enjoy! :thumbsup:
