#!/usr/bin/python3

import urllib.request
import urllib.error

req = urllib.request.Request(
    url='https://intranet.hbtn.io/status',
    headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
        html_decoded = html.decode('utf8')

        print('Body response:')
        print('         - type: {}'.format(type(html)))
        print('         - content: {}'.format(html))
        print('         - utf8 content: {}'.format(html_decoded))

except urllib.error.HTTPError as error:
    print(error)
