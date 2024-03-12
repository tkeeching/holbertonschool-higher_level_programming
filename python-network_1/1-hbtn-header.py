#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

req = urllib.request.Request(
    url=sys.argv[1],
    headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])

except urllib.error.HTTPError as error:
    print(error)
