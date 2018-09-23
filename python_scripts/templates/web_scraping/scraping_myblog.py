#!/usr/bin/env python3

import requests, bs4

def get_article_title(url):

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#post-884 > header > h1')
    price = (elems[0].text.strip())
    print ('The title is ' + price)


url = 'https://smpressa.wordpress.com/2015/01/05/extremos/'
get_article_title(url)
