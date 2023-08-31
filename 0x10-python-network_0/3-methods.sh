#!/bin/bash
# Curl to display all HTTP methods the server accepts

# Send a HEAD request using curl to the URL provided as an argument($1)
# -s: Silent mode, no progress output
# -I: Fetch only the response header
# The output is then piped to grep to search for the line containing "Allow"
# The -i flag makes the search case-insensitive
# The result is then piped to cut to split the line be space and extract everything
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-
