#!/usr/bin/env python3

import requests, os, sys

os.chdir('/Users/Alex/Desktop')



res = requests.get('http://automatetheboringstuff.com/files/rj.txt')

res.raise_for_status()

print(len(res.text))

print(res.text[100:500])

playfile = open('romeoandjuliet.txt', 'wb')
for byte_chunk in res.iter_content(100000):
    playfile.write(byte_chunk)

playfile.close()

print(sys.getdefaultencoding())
