#!/usr/bin/python3
import urllib.request

# Define the URL to fetch the status from
url = 'https://alx-intranet.hbtn.io/status'

# Use a with statement to open the URL and manage the connection
with urllib.request.urlopen(url) as response:
    # Read the response content into the body variable as bytes
    body = response.read()

# Print the response info
print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
