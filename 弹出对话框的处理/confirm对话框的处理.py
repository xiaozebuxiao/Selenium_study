#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get(r'F:\自动化学习\selenium\自学\弹出对话框的处理\file\白月黑羽：web自动化 - 弹出对话框.html')
wd.implicitly_wait(10)

# 点击”confirm“按钮
wd.find_element(By.ID, 'b2').click()
# 打印弹框内容
print('你的操作结果是：' + wd.switch_to.alert.text)

# --------------点击”确定“按钮----------------------

# 点击”确定按钮“
# wd.switch_to.alert.accept()
# 获取操作结果
# element_li = wd.find_element(By.TAG_NAME, 'li')
# print(element_li.text)

# --------------点击”取消“按钮----------------------

# 点击”取消“按钮
wd.switch_to.alert.dismiss()
# 获取操作结果
element_li = wd.find_element(By.TAG_NAME, 'li')
print('你的操作结果是：' + element_li.text)

wd.quit()




