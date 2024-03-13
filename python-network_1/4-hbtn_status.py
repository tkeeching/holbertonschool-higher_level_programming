#!/usr/bin/python3

import requests

response = requests.get('https://intranet.hbtn.io/status')

print('Body response:')
print('{}{} {}'.format('\t', '- type:', type(response)))
print('{}{} {}'.format('\t', '- content:', response.decode('utf8')))
