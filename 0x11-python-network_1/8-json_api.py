#!/usr/bin/python3
"""
A module that sends a POST request to a URL with a letter as a parameter
and handles the reponse accordingly
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]

    else:
        q = ''

    _url = 'https://0.0.0.0:5000/search_user'
    data = {'q': q}

    try:
        response = requests.post(_url, data=data)
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))

        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
