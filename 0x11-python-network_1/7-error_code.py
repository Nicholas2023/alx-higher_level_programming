#!/usr/bin/python3
"""
A module that sends an HTTP request to a URL and displays the body
of the response
Also prints error messages with the status code
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
