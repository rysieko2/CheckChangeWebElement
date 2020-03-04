#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
driver = webdriver.Firefox(executable_path="/home/krzys/Application/Tbs/geckodriver", options=options)
wait = WebDriverWait(driver,10)

#oldLocalization = "ul. Wileńska 17".decode("utf-8") 
subprocess.call(['./Application/Tbs/startMail.sh'])

driver.get("http://www.tbs-wroclaw.com.pl/mieszkania-na-wynajem/")

time.sleep(5)
oldLocalizationElement = driver.find_element_by_xpath("//strong")
oldLocalization = oldLocalizationElement.text

while 15 > time.localtime().tm_hour:
    driver.refresh()
    newLocalizationElement = driver.find_element_by_xpath("//strong")
    newLocalization = newLocalizationElement.text
    #subprocess.call(['./Application/Tbs/stopMail.sh'])
    if oldLocalization != newLocalization:
        subprocess.call(['./Application/Tbs/sendMail.sh'])
        time.sleep(5)
        oldLocalization = newLocalization
        time.sleep(60)

    #subprocess.call(['./Application/Tbs/startMail.sh'])
    #break
subprocess.call(['./Application/Tbs/stopMail.sh']) 

driver.quit()

