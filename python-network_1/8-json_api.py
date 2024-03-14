#!/usr/bin/python3
"""Takes in a letter and sends a POST request"""


import requests
import sys

try:
    response = requests.post(
        'http://0.0.0.0:5000/search_user',
        data={'q': '' if len(sys.argv) == 1 else sys.argv[1]})

    json = response.json()
    if (len(json) == 0):
        print('No result')
    else:
        print('[{}] {}'.format(json['id'], json['name']))

except IndexError as error:
    print('IndexError:', error)

except ValueError as error:
    print('Not a valid JSON')
