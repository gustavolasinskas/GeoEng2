#!/usr/bin/env Python3

from selenium import webdriver

class RunFireFox():

    def in_the_hole(self):
        driver = webdriver.Firefox()
        driver.get('https://www.mozilla.org/en-US/firefox/new/?gclid=CIeV0KznntACFUmBkQod1xsDMQ&v=a')

fire = RunFireFox()
fire.in_the_hole()
