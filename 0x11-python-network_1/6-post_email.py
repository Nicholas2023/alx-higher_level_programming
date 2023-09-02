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
    _url = sys.argv[1]
    email = sys.argv[2]

    """ Create a dictiopnary with the email parameter """
    data = {'email': email}

    """ Send a POST request to the URL with the email parameter """
    response = requests.post(_url, data=data)

    """ Display the response body """
    print("Your email is:", response.text)
