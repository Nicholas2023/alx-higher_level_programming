#!/bin/bash
# Bash script that sends a PUT request to the URL 0.0.0.0:5000/catch_me,
# providing data and headers, and displays the response.

# Send a PUT request using curl:
# -s: Silent mode, suppresses progress and error messages
# -X PUT: Specify the HTTP method as PUT
# -L: Follow redirects if any
# -d "user_id=98": Send the specified data as part of the request body
# --header "origin: HolbertonSchool": Add a custom header to the request
# The URL to send the request to is the last argument
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
