#!/usr/bin/env Python3

from selenium import webdriver
import time

class Linking():

    def new_contacts(self):
        baseUrl = "https://www.linkedin.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        login = driver.find_element_by_id("login-email")
        password = driver.find_element_by_id("login-password")
        submit = driver.find_element_by_id("login-submit")

        login.send_keys('alex.mca@live.com')
        password.send_keys('pr1mata')
        submit.click()

        time.sleep(1)
        grow_network = driver.find_element_by_id("dropdowntest")
        time.sleep(1)
        grow_network.click()
        time.sleep(2)
        lista = []
        count = 0
        for _ in range(4):
            try:
                for _ in range(10):
                    time.sleep(1)
                    for index in range(1,5):
                        connect = "//div[@id='container']//li[%s]//button[2]/span[1]" %(str(index))
                        lista.append(str(connect))

                    for item in lista:
                        verbinden = driver.find_element_by_xpath(item)
                        verbinden.click()
                        count += 1
                        time.sleep(1)
            except:
                driver.refresh()
            finally:
                print("refreshing...")

        print(str(count) + " contacts added!")
        driver.quit()
link = Linking()
link.new_contacts()
