#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
wd.implicitly_wait(10)

# css选择器选择子元素：元素3 是 元素2 是 元素1 的直接子元素：元素3 > 元素2 > 元素1
# elements = wd.find_elements(By.CSS_SELECTOR, '.plant > span')

# css选择器选择后代元素：元素3 是 元素2 是 元素1 的后代元素：元素3  元素2  元素1
# elements = wd.find_elements(By.CSS_SELECTOR, 'body .animal span')

# 两者也可混合使用
elements = wd.find_elements(By.CSS_SELECTOR, 'body > #bottom .footer1 >.data')

for element in elements:
    print(element.text)

wd.quit()

