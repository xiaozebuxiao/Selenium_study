#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get('https://www.byhy.net/_files/stock1.html')

elements = wd.find_elements(By.CLASS_NAME, 'result-item')

# 获取class名为result-item的元素的id
for element in elements:
    # 获取id的属性值
    id_name = element.get_attribute('id')
    print(id_name)

wd.quit()
