#!/usr/bin/python3

import requests
import sys

try:
    response = requests.post(sys.argv[1], json={'email': sys.argv[2]})
    print(response.text)
except IndexError as error:
    print(error)
