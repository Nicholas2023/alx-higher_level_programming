#!/bin/bash
# Curl to display all HTTP methods the server accepts
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-
