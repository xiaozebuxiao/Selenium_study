#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 创建webdriver对象，指明chrome驱动
wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))

# 调用webdriver的get方法，打开网页
wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

# 根据标签名选择元素
elements = wd.find_elements(By.TAG_NAME, 'span')

for element in elements:
    print(element.text)
