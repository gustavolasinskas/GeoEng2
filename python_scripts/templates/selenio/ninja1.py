#!/usr/bin/env Python3

from selenium import webdriver
import os

class RunFireFox():

    def in_the_hole(self):

        base_url = 'https://letskodeit.teachable.com/p/practice'

        driver = webdriver.Firefox()
        driver.get(base_url)
        element_by_id = driver.find_element_by_id('name')
        if element_by_id is not None:
            print (element_by_id)
            print ('We did it!')

        element_by_name = driver.find_element_by_name('show-hide')
        if element_by_name is not None:
            print (element_by_name)
            print ('Nice done again!')

        exit_status= os.system('echo $?')
        print('Process finished with exit code ' + str(exit_status))



fire = RunFireFox()
fire.in_the_hole()
