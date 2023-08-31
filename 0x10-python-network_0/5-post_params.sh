#!/bin/bash
# Curl sends a POST request to the URL, and response body is displayed
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
