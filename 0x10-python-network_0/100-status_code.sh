#!/bin/bash
# Bash script that sends a request to a URL passed as an argument and displays only the status code of the response.

# Usage: ./scriptname.sh <URL>

# $1 represents the first argument passed to the script (the URL)
# curl options:
# -s: Silent mode, suppresses progress and error messages
# -o /dev/null: Redirects the response body to /dev/null, discarding it
# -w "%{http_code}": Specifies a custom output format to display only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"
