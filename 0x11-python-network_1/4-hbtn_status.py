#!/usr/bin/python3
"""
A script that fetches a URL using the 'requests' lib
Displays the body of the response with specific formmating
"""
import requests


if __name__ == "__main__":
    """ URL to fetch """
    _url = 'https://alx-intranet.hbtn.io/status'

    """ Send a GET request to the URL """
    response = requests.get(_url)

    """ Get the reponse content """
    content = response.text

    """ Display the formatted response body """
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
