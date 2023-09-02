#!/usr/bin/python3
"""
A script that takes a URL and email as input,
sends a POST request to the URL with the email as
a parameter and disply response
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    """
    Get the URL and email from the cmd line args
    """
    _url = sys.argv[1]
    email = sys.argv[2]

    """ Encode the email as a URL parameter """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    """ Create a POST request and send it to the URL """
    request = urllib.request.Request(_url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        """ Read and decode the response body as UTF-8 """
        response_body = response.read().decode("utf-8")

        """ Print the response """
        print(response_body)
