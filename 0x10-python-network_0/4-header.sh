#!/bin/bash
# Send a Get request to a given URL with a header variable

# Use curl to send a GET request with the following options:
# -s: Silent mode, no progress output
# -H "X-School-User-Id: 98": Add a custom header with the specified values
curl -sH "X-School-User-Id: 98" "$1"
