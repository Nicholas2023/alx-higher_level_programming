#!/bin/bash
# Sends a request to URL and displays sizeof the response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
