#!/bin/bash
# Sends a GET request to the URL and displays the response body

# Send a GET request using curl with the following options:
# -s: Silent mode, no progress output
# -f: Fail silently on HTTP errors
# -L: Follow redirects
# -X GET: Explicitly set the request method to Get
curl -sfL "$1" -X GET
