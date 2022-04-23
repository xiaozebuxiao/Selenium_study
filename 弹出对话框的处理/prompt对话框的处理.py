#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get(r'F:\自动化学习\selenium\自学\弹出对话框的处理\file\白月黑羽：web自动化 - 弹出对话框.html')
wd.implicitly_wait(10)

wd.find_element(By.ID, 'b3').click()

# 输入内容
wd.switch_to.alert.send_keys("go语言")
# 点击”确定“按钮
wd.switch_to.alert.accept()
# 输出结果
element = wd.find_element(By.TAG_NAME, 'li')
print(element.text)

wd.quit()
