#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
wd.implicitly_wait(10)

# 通过其他属性选择元素：[ ]
# elements = wd.find_elements(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')
# elements = wd.find_elements(By.CSS_SELECTOR, '[href]')
# elements = wd.find_elements(By.CSS_SELECTOR, '.footer2 [href]')

# 多个筛选条件之间用“,”隔开
elements = wd.find_elements(By.CSS_SELECTOR, '.plant , .animal')

for element in elements:
    print(element.text)

wd.quit()

