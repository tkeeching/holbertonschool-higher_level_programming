#!/usr/bin/python3

import requests
import sys
import json

try:
    response = requests.post(
        sys.argv[1], data={'q': sys.argv[2] if len(sys.argv) > 1 else ''})

    try:
        data = json.loads(response.text)

        if (len(data) == 0):
            print('No result')
        else:
            print('[{}] {}'.format(data['id'], data['name']))
    except ValueError as error:
        print('Not a valid JSON')

except IndexError as error:
    print('IndexError:', error)
