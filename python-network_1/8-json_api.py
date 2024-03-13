#!/usr/bin/python3

import requests
import sys

try:
    print(sys.argv)
    response = requests.post(
        'http://0.0.0.0:5000/search_user',
        data={'q': sys.argv[1] if len(sys.argv) > 1 else ''})

    try:
        json = response.json()
        if (len(json) == 0):
            print('No result')
        else:
            print('[{}] {}'.format(json['id'], json['name']))
    except ValueError as error:
        print('Not a valid JSON')

except IndexError as error:
    print('IndexError:', error)
