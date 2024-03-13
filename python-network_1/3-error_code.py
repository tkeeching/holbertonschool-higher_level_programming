#!/usr/bin/python3

import urllib.request
import urllib.error
import urllib.parse
import sys

try:
    req = urllib.request.Request(
        url=sys.argv[1] if len(sys.argv) > 0 else '',
        headers={'User-Agent': 'Mozilla/5.0'})

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html)

except IndexError as error:
    print('IndexError:', error)

except urllib.error.HTTPError as error:
    print('Error code:', error)
