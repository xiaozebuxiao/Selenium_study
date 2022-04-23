#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get(r'F:\自动化学习\selenium\自学\弹出对话框的处理\file\白月黑羽：web自动化 - 弹出对话框.html')
wd.implicitly_wait(10)

wd.find_element(By.ID, 'b1').click()

# 打印对话框上的文字内容
print(wd.switch_to.alert.text)

# 点击”OK“按钮，退出弹框
wd.switch_to.alert.accept()

pass
