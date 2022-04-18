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
# elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-child(2)')

# 组合匹配（id是t1的div的第一个子元素）
# elements = wd.find_elements(By.CSS_SELECTOR, '#t1 :nth-child(1)')

# 倒序匹配(匹配div的子节点的倒数第一个节点)
# elements = wd.find_elements(By.CSS_SELECTOR, 'div > :nth-last-child(1)')

# 根据在父节点中tag的序号，正序匹配（寻找所有父节点中，第一个p标签）
# elements = wd.find_elements(By.CSS_SELECTOR, 'p:nth-of-type(1)')

# 根据在父节点中tag的序号，倒序匹配（寻找所有父节点中，最后一个p标签的内容）
# elements = wd.find_elements(By.CSS_SELECTOR, 'p:nth-last-of-type(1)')

# 匹配所有p标签的奇数序号
elements = wd.find_elements(By.CSS_SELECTOR, 'p:nth-child(odd)')

for element in elements:
    print(element.text)

wd.quit()


