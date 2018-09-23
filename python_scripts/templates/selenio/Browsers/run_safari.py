#!/usr/bin/env Python3

from selenium import webdriver

class RunSafari():

    def in_the_hole(self):
        driver = webdriver.Safari()
        driver.get('http://www.apple.com/safari/')

simba = RunSafari()
simba.in_the_hole()
