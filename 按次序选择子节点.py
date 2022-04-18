#!/usr/bin/python
# -*-coding:utf-8 -*-
"""测试文件：test01_html"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get("https://cdn2.byhy.net/files/selenium/sample1b.html")
wd.implicitly_wait(10)

# css选择器按次序选择子节点（类型是span，是父节点的第二个子节点）
elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-child(2)')

for element in elements:
    print(element.text)

wd.quit()


