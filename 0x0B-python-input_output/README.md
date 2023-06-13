# Python Input/Output Tasks :wink:

This repository contains Python scripts that demonstrate various inpu/output operations, including reading from and writing to files, working with JSON data, and serializing objects.

## Task List

### 1. Read file
* Filename: `0-read_file.py`
* Description: Reads a text file (UTF8) and prints its content to stdout.
* Usage:
```.py
read_file("filename.txt")
```

### 2. Write to a file
* Filename: `1-write_file.py`
* Description: Writes a string to a text file (UTF8) and returns the number of characters written.
* Usage:
```.py
nb_characters = write_file("filename.txt", "text")
```

### 3. Append to a file
* Filename: `2-append_write.py`
* Description: Appends a string to the end of a text file (UTF8) and returns the number of characters added.
* Usage:
```.py
nb_characters_added = append_write("filename.txt", "text")
```

### 4. To JSON string
* Filename: `3-to_json_string.py`
* Description: Returns the JSON representation of an object (string).
* Usage:
```.py
json_string = to_json_string(obj)
```

### 5. From JSON string to object
* Filename: `4-from_json_string.py`
* Description: Returns an object (Python data structure) represented by a JSON string.
* Usage:
```.py
obj = from_json_string(json_string)
```

### 6. Save Object to a file
* Filename: `5-save_to_json_file.py`
* Description: Writes an object to a text file using JSON representation.
* Usage:
```.py
save_to_json_file(obj, "filename.json")
```

### 7. Create object from a JSON file
* Filename: `6-load_from_json_file.py`
* Description: Adds command-line arguments to a Python list and saves them to a file in JSON format.
* Usage:
```.py
obj = load_from_json_file("filename.json")
```

### 8. Load, add, save
* Filename: `7-add_item.py`
* Description: Adds command-line arguments to a Python list and saves them to a file in JSON format.
* Usage:
```bash
./7-add_item.py arg1 arg2 ...
```

### 9. Class to JSON
* Filename: `8-class_to_json.py`
* Description: Returns a dictionary description with a simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object.
* Usage:
```.py
json_dict = class_to_json(obj)
```

## Repository Structure
* `0x0B-python-input_output/`:
Directory containing all the Python scripts for the tasks.

* `README.md`:
This file, providing an overview of the repository and its contents.

## Usage
To use any of the provided scripts, simply run them using the Python interpreter:

```bash
python3 script.py
```
Replace `script.py` with the name of the specific script you want to execute

## Requirements

* Python 3.x

No additional modules or libraries are required for running the scripts.

## Author

This repository is maintained by `Nicholas Otieno Odhiambo`
