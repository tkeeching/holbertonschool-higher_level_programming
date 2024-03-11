#!/usr/bin/python3

import urllib.request

req = urllib.request.Request(url='https://intranet.hbtn.io/status', headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req) as response:
    html = response.read()
    print(html)
