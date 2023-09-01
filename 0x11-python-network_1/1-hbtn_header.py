#!/usr/bin/python3
"""
A script that takes URL and displays the req id
"""

import urllib.request
import sys

if __name__ == '__main__':
    """Get the url from the cmd line args"""
    _url = sys.argv[1]

    """Use a with statement to open the URL and manage
        the connection
    """

    with urllib.request.urlopen(_url) as response:
        # Get the value of the 'X-Request-ID' header from the response
        x_request_id = response.headers.get('X-Request-Id')

        # Print the value of the x-Request:
        print(dict(response.headers).get("x_request_id"))
