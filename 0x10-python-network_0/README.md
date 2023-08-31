# Python Network Programming and Algorithm Complexity :smile:

This repository contains a set of Bash scripts for performing various network-related tasks using the `curl` command, as well as a Python script that implements an algorithm to find a peak in an unsorted list of integers.

## Table of Contents

- [Scripts](#scripts)
  - [0-body_size.sh](#0-body_size-sh)
  - [1-body.sh](#1-body-sh)
  - [2-delete.sh](#2-delete-sh)
  - [3-methods.sh](#3-methods-sh)
  - [4-header.sh](#4-header-sh)
  - [5-post_params.sh](#5-post_params-sh)
- [Algorithm](#algorithm)
- [Usage](#usage)

## Scripts

### 0-body_size.sh

This script takes a URL as an argument, sends a GET request using `curl`, and displays the size of the response body in bytes.

Example usage:

```bash
./0-body_size.sh 0.0.0.0:5000
```

### 1-body.sh

This script takes a URL as an argument, sends a GET request using `curl`, and displays the body of the response for a 200 status code.

Example usage:

```bash
./1-body.sh 0.0.0.0:5000/route_1
```

### 2-delete.sh

This script sends a DELETE request to the URL passed as an argument using `curl` and displays the body of the response.

Example usage:

```bash
./2-delete.sh 0.0.0.0:5000/route_3
```

### 3-methods.sh

This script takes a URL as an argument and displays all HTTP methods the server will accept using `curl`.

Example usage:

```bash
./3-methods.sh 0.0.0.0:5000/route_4
```

### 4-header.sh

This script takes a URL as an argument, sends a GET request using `curl`, and includes a custom header `X-School-User-Id` with the value `98`.

Example usage:

```bash
./4-header.sh 0.0.0.0:5000/route_5
```

### 5-post_params.sh

This script takes a URL as an argument, sends a POST request using `curl`, and includes email and subject parameters in the request body.

Example usage:

```bash
./5-post_params.sh 0.0.0.0:5000/route_6
```

## Algorithm

### 6-peak.py

This Python script defines a function `find_peak(list_of_integers)` that finds a peak in a list of unsorted integers. The algorithm has a complexity of `O(log(n))`, making it efficient for large lists.

Example usage:

```python
print(find_peak([1, 2, 4, 6, 3]))
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

2. Navigate to the appropriate directory:

```bash
cd 0x10-python-network_0
```

3. Run the desired script using the provided examples as a guide.
