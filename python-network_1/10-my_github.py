#!/usr/bin/python3

import requests
import sys

try:
    response = requests.get(
        'https://api.github.com/users/{}'.format(sys.argv[1]),
        headers={'Authorization': 'Bearer {}'.format(sys.argv[2])})
    
    print(response.json()['id'])
except IndexError as error:
    print(error)

except KeyError as error:
    print('None')
