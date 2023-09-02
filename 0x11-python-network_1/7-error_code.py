#!/usr/bin/python3
"""
A module that sends an HTTP request to a URL and displays the body
of the response
Also prints error messages with the status code
"""

import requests
import sys

if __name__ == "__main__":
    _url = sys.argv[1]

    reponse = requests.get(_url)
    content_type = response.headers.get('content-type', '').lower()

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
