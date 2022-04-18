#!/usr/bin/python
# -*-coding:utf-8 -*-
"""测试文件：test01_html"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get(r'F:\自动化学习\selenium\自学\test01_html.html')
wd.implicitly_wait(10)

# “+”：兄弟节点之间，紧跟着的节点（表示和span为兄弟关系，且紧跟着span的p标签）
# elements = wd.find_elements(By.CSS_SELECTOR, 'span+p')

# “~”：兄弟节点之间，之后的所有节点（表示和span为兄弟节点，span之后所有的p标签）
elements = wd.find_elements(By.CSS_SELECTOR, 'span ~ p')

for element in elements:
    print(element.text)

wd.quit()


