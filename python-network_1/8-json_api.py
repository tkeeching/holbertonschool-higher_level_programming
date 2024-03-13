#!/usr/bin/python3

import requests
import sys

try:
    response = requests.post(
        'http://0.0.0.0:5000/search_user',
        data={'q': sys.argv[1] if len(sys.argv) > 0 else ''})

    try:
        json = response.text
        if (len(json) == 0):
            print('No result')
        else:
            print('json:', json)
            print('[{}] {}'.format(json['id'], json['name']))
    except ValueError as error:
        print('Not a valid JSON')

except IndexError as error:
    print('IndexError:', error)
