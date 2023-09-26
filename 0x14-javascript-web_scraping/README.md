# JavaScript Web Scraping Scripts :wink:

This repository contains JavaScript scripts for various web scraping tasks. These scripts are designed to perform specific tasks related to reading files, making HTTP requests, and interacting with web APIs.

## Table of Contents

- [Getting Started](#getting-started)
- [Scripts](#scripts)
  - [0-readme.js](#0-readmejs)
  - [1-writeme.js](#1-writemejs)
  - [2-statuscode.js](#2-statuscodejs)
  - [3-starwars_title.js](#3-starwars_titlejs)
  - [4-starwars_count.js](#4-starwars_countjs)
  - [5-request_store.js](#5-request_storejs)
  - [6-completed_tasks.js](#6-completed_tasksjs)

## Getting Started

To run these scripts, you need to have Node.js installed on your system. If you don't have it installed, you can download it from the official [Node.js website](https://nodejs.org/).

Once you have Node.js installed, you can execute the scripts in your terminal.

## Scripts

### 0-readme.js

This script reads and prints the content of a file. It takes a file path as an argument and reads the file in UTF-8 encoding. If an error occurs during reading, it prints the error object.

Example usage:

```bash
$ node 0-readme.js cisfun
C is super fun!
$ node 0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
```

### 1-writeme.js

This script writes a string to a file. It takes a file path and a string as arguments and writes the content to the file in UTF-8 encoding. If an error occurs during writing, it prints the error object.

Example usage:

```bash
$ node 1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt
Python is cool
```

### 2-statuscode.js

This script displays the status code of a GET request to a given URL. It uses the `request` module to make the HTTP request.

Example usage:

```bash
$ node 2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
$ node 2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
```

### 3-starwars_title.js

This script prints the title of a Star Wars movie based on the provided movie ID. It makes a request to the Star Wars API and uses the `request` module to fetch the data.

Example usage:

```bash
$ node 3-starwars_title.js 1
A New Hope
$ node 3-starwars_title.js 5
Attack of the Clones
```

### 4-starwars_count.js

This script prints the number of movies where the character "Wedge Antilles" is present. It makes a request to the Star Wars API and filters the results based on the character ID.

Example usage:

```bash
$ node 4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
```

### 5-request_store.js

This script gets the contents of a webpage and stores it in a file. It takes a URL and a file path as arguments and saves the response in UTF-8 encoding to the specified file.

Example usage:

```bash
$ node 5-request_store.js http://loripsum.net/api loripsum
$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...
```

### 6-completed_tasks.js

This script computes the number of tasks completed by user ID. It makes a request to a JSONPlaceholder API and counts completed tasks for each user.

Example usage:

```bash
$ node 6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
```

Feel free to explore and use these scripts for your web scraping and data processing needs. Make sure to install the required dependencies, such as the `request` module, using npm if needed.
