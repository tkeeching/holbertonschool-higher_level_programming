#!/usr/bin/python3

import requests
import sys

try:
    response = requests.post(
        sys.argv[1], data={'q': sys.argv[2] if len(sys.argv) > 1 else ''})

    try:
        json = response.text
        if (len(json) == 0):
            print('No result')
        else:
            print('[{}] {}'.format(json['id'], json['name']))
    except ValueError as error:
        print('Not a valid JSON')

except IndexError as error:
    print('IndexError:', error)
