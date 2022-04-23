#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get(r'F:\自动化学习\selenium\自学\选择框\白月黑羽：web自动化 - 选择框.html')
wd.implicitly_wait(10)

# ----------------checkbox（勾选框）解决方案--------------------

# 1、找到默认选中的所有元素,点击一下，使其达到未选中状态
element_checked_tags = wd.find_elements(By.CSS_SELECTOR, '#s_checkbox input[checked="checked"]')
for element_checked_tag in element_checked_tags:
    element_checked_tag.click()

# 2、选择想要选择的元素
element_expectation = wd.find_element(By.CSS_SELECTOR, '#s_checkbox > input[value="小江老师"]')
element_expectation.click()
print("现在选择的元素是：" + element_expectation.get_attribute('value'))

wd.quit()

