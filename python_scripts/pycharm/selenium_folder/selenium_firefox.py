#!/usr/bin/env python3

from selenium import webdriver
import os

class RunChrome():

    def in_the_hole(self):

        #driver_location = '/Users/Alex/code/python_library/chromedriver'
        #os.environ['webdriver.chrome.driver'] = driver_location

        driver = webdriver.Chrome()
        driver.get('https://www.google.com/chrome/')

chromium = RunChrome()
chromium.in_the_hole()
