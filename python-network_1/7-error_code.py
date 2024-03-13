#!/usr/bin/python3

import requests
import sys

try:
    response = requests.get(sys.argv[1])
    print(response.text)

except IndexError as error:
    print('IndexError:', error)

except requests.HTTPError as error:
    print('Error code:', error.getcode())
