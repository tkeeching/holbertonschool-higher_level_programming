#!/usr/bin/python3

import requests
import sys

try:
    response = requests.get(sys.argv[1])

    if (response.status_code >= 400):
        print('Error code:', response.status_code)
    else:
        print(response.text)

except IndexError as error:
    print('IndexError:', error)
