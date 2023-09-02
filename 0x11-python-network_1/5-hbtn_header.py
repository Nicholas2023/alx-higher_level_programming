#!/usr/bin/python3
"""
A script that takes a URl as input,
Sends a request to the URL using requests library
Displays the value of the 'X-Request-Id' var from response header
"""

import requests
import sys

if __name__ == "__main__":
    """ Get the URl from the command line argument """
    _url = sys.argv[1]

    """ Send a GET request to the URL """
    response = requests.get(_url)

    """
    Get the value of the 'X-Request-Id' header from the response
    """
    x_request_id = response.headers.get('X-Request-Id')

    """ Print the value of the 'X-Request-Id' headers """
    print(x_request_id)
