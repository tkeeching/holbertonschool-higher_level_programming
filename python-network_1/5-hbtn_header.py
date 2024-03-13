#!/usr/bin/python3

import requests
import sys

try:
    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
except IndexError as error:
    print(error)
