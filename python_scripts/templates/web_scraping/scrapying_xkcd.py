#!/usr/bin/env Python3

import bs4, requests
import urllib.request

url = 'http://xkcd.com/1/'

resp = requests.get(url)

resp.status_code
resp.raise_for_status()

soup = bs4.BeautifulSoup(resp.text, 'html.parser')
image = soup.select('#comic > img')
print(image['src'])
