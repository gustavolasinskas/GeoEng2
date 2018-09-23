#!/usr/bin/env Python3

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class AirbnbTest():

    def plantrip(self):

        baseUrl = 'https://www.airbnb.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        searchBar = driver.find_element_by_id('search-location')
        searchBar.send_keys('Bergen, Norway')

        startDate = driver.find_element_by_id('startDate')
        startDate.send_keys('01/14/2017')

        endDate = driver.find_element_by_id('endDate')
        endDate.send_keys('01/27/2017')

        print('Found dates')
        time.sleep(4)
        guests = driver.find_element_by_name('guests')
        print('Found element by Name')
        selGuests = Select(guests)
        print('Selected Checkbox')
        selGuests.select_by_visible_text('4 Guests')
        print('We did it!')

        submit = driver.find_element_by_xpath("//button[contains (@class, 'btn') and contains(@class, 'btn-large')]")
        submit.click()
        print('Submitting!')


air = AirbnbTest()
air.plantrip()
