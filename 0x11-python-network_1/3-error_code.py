#!/usr/bin/python3
"""
A script that takes URLas input and displays the body of the response
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    """ Get the URL from the command line argument """
    _url = sys.argv[1]

    try:
        """ Send a request to the URL and open the response """
        with urllib.request.urlopen(_url) as response:
            """ Read and decode the response body as UTF-8 """
            response_body = response.read().decode('utf-8')

            """ Print the response body """
            print(response_body)

    except urllib.error.HTTPError as e:
        """ Handle HTTP errors by printing the error code and message """
        print(f"Error code: {e.code}")
