#!/bin/bash
# Sends a DELETE request to the URL provided as an arg ($1)
curl -s "$1" -X DELETE
