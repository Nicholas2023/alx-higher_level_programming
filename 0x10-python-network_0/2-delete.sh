#!/bin/bash
# Sends a DELETE request to the URL provided as an arg ($1)

# Send a DELETE request using curl with the following options:
# -s: Silent mode, no progress output
# -X DELETE: Explicitly set the request method to DELETE
curl -s "$1" -X DELETE
