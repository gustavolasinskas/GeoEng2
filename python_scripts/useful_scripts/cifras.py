#!/usr/bin/env Python3

from selenium import webdriver
import sys

baseUrl = "https://www.cifraclub.com.br/the-beatles/"

sound = " ".join(sys.argv[1:])


driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(0.5)
driver.get(baseUrl)


searchBar = driver.find_element_by_css_selector(".busca-inp")
searchBar.send_keys(str(sound))
