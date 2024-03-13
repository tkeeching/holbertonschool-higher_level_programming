#!/usr/bin/python3

import requests
import sys

try:
    response = requests.post(
        'https://api.github.com/users/{}'.format(sys.argv[1]),
        headers={'Authorization': 'Bearer {}'.format(sys.argv[2])})
except IndexError as error:
    print(error)
