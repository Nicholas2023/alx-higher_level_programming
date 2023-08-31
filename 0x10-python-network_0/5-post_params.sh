#!/bin/bash
# Curl sends a POST request to the URL, and response body is displayed

# Use curl to send a POST request with the following options:
# -s: Silent mode, no progress output
# -X POST: Explicitly set the request method to POST
# -d: Set requset body parameters
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
