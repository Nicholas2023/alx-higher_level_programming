#!/bin/bash
# Sends a request to the given URL and displays the response status code.
curl -sI -w '%{response_code}' "$1" -o /dev/null
