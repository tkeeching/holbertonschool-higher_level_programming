#!/usr/bin/python3

import urllib.request
import urllib.error

req = urllib.request.Request(
    url='https://intranet.hbtn.io/status',
    headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
        html_decoded = html.decode('utf8')

        print('Body response:')
        print('         - type: {}'.format(type(html)))

        start_index = html_decoded.find(
            '<pre style="word-wrap: break-word; white-space: pre-wrap;">')
        + len('<pre style="word-wrap: break-word; white-space: pre-wrap;">')

        end_index = html_decoded.find('</pre>', start_index)

        if start_index != -1 and end_index != -1:
            message = html_decoded[start_index:end_index]
            print('html_decoded:', html_decoded)
            print('         - content: {}'.format(message))
            print('         - utf8 content: {}'.format(message))
        else:
            print("Message not found.")
except urllib.error.HTTPError as error:
    print(error)
