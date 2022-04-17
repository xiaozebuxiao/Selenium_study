#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
wd.implicitly_wait(10)

# css选择器找元素
# elements = wd.find_elements(By.CSS_SELECTOR, '.animal')

# 根据tag名选择元素：直接写tag名
# elements = wd.find_elements(By.CSS_SELECTOR, "div")

# 根据属性id选择元素：#id值
# elements = wd.find_elements(By.CSS_SELECTOR, '#inner12')

# 根据属性class选择元素：.class值
elements = wd.find_elements(By.CSS_SELECTOR, '.plant')

for element in elements:
    print(element.text)

wd.quit()
