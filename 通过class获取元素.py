#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 创建webdriver实例对象，指明使用的chrome驱动
wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))

# 使用webdriver的get方法打开网页
wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

# 根据class选择元素，得到一个webElement对象列表
elements = wd.find_elements(By.CLASS_NAME, value="plant")

# 遍历webElement对象列表得到webElement对象的文本
for element in elements:
    print(element.text)
