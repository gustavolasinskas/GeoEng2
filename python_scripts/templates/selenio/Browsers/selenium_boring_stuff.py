#!/usr/bin/env python3
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://automatetheboringstuff.com')

#searchElem = browser.find_element_by_css_selector('.search-field')
#searchElem.send_keys('zophie')
#searchElem.submit()
elem =  browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(17) > li:nth-child(1) > a:nth-child(1)')
elem
elem.click()

elems = browser.find_elements_by_css_selector('html')
print(len(elems))
