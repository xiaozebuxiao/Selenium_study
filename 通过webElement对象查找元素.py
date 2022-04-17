#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# 创建webdriver对象
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))

# 通过webdriver对象的get方法，获得整个网页
wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

# 通过find_element相关方法获得class名为plant的元素
elements = wd.find_elements(By.CLASS_NAME, "plant")

# 通过webelement对象获得span标签
for element in elements:
    tag = element.find_element(By.TAG_NAME, "span")
    print(tag.text)

# 关闭页面
wd.quit()
