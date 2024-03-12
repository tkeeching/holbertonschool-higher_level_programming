#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

"""Takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id in the response header"""

req = urllib.request.Request(
    url=sys.argv[1],
    headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])

except urllib.error.HTTPError as error:
    print(error)
