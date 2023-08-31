#!/bin/bash
# Sends a request to the given URL and displays the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
