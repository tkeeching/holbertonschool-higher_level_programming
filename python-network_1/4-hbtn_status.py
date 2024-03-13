#!/usr/bin/python3

import requests

response = requests.get('https://intranet.hbtn.io/status')

print('Body response:')
print('{}{} {}'.format('\t', '- type:', type(response.text)))
print('{}{} {}'.format('\t', '- content:', response.text))
