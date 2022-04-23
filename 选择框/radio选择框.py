#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get(r'F:\自动化学习\selenium\自学\选择框\白月黑羽：web自动化 - 选择框.html')
wd.implicitly_wait(10)

# 在radio框中获取当前选中的元素，并打印元素里的文字
element_pitch_on = wd.find_element(By.CSS_SELECTOR, '#s_radio input[checked="checked"]')
print("当前选中的是：" + element_pitch_on.get_attribute('value'))

# 在radio框中选择小江老师
element_xj = wd.find_element(By.CSS_SELECTOR, '#s_radio > input[value="小江老师"]')
element_xj.click()
print('现在选中的是：' + element_xj.get_attribute('value'))

wd.quit()
