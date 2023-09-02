#!/usr/bin/python3
"""
A module that takes URL and an email address as input,
sends a POST request to the spcified URL with the email
as a parameter, and displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    """
    Get the URL and email address from command line arguments
    """
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
