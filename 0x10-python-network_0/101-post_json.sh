#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument,
# using the contents of a JSON file passed as the second argument as the request body,
# and displays the body of the response.

# Usage: ./scriptname.sh <URL> <JSON_FILE>

# $1 represents the first argument passed to the script (the URL)
# $2 represents the second argument passed to the script (the JSON file)

# Send a JSON POST request using curl:
# -s: Silent mode, suppresses progress and error messages
# -L: Follow redirects if any
# -H "content-type:application/json": Set the request header to indicate JSON content type
# -d @"$2": Send the content of the JSON file as the request body
# -X POST: Specify the HTTP method as POST
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"
