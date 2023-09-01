# Python Network Tasks :smile:

This repository contains a collection of Python scripts that demonstrate network-related tasks using different libraries such as urllib and requests. These scripts can be useful for making HTTP requests, handling responses, and working with APIs.

## Scripts

### 0-hbtn_status.py

This script fetches the status of a specific URL using the urllib package and displays information about the response body.

### 1-hbtn_header.py

This script takes a URL as input, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response. It uses the urllib package.

### 2-post_email.py

This script takes a URL and an email as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response. It uses the urllib package.

### 3-error_code.py

This script takes a URL as input, sends a request to the URL, and displays the body of the response. It also handles HTTP errors using the `urllib` package.

### 4-hbtn_status.py

This script fetches the status of a specific URL using the `requests` package and displays information about the response body.

### 5-hbtn_header.py

This script takes a URL as input, sends a request to the URL, and displays the value of the `X-Request-Id` variable in the response header. It uses the `requests` package.

### 6-post_email.py

This script takes a URL and an email as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response. It uses the `requests` package.

### 7-error_code.py

This script takes a URL as input, sends a request to the URL, and displays the body of the response. It also handles HTTP errors using the `requests` package.

### 8-json_api.py

This script takes a letter as input, sends a POST request to a specified URL with the letter as a parameter, and displays the response. It handles JSON responses and provides appropriate messages.

### 10-my_github.py

This script takes GitHub credentials (username and personal access token) as input and uses the GitHub API to display the user's ID.

## Usage

Each script can be run from the command line with the appropriate arguments. Refer to the individual script descriptions for usage examples.

```bash
./script_name.py [arguments]
```

## Requirements

- Python 3.x
- urllib package (for scripts using urllib)
- requests package (for scripts using requests)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
