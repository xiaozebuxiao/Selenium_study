#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID, 'kw')
element.send_keys("科技")
print(element.get_attribute('value'))

wd.quit()
