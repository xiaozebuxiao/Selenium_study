#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get('https://www.baidu.com/')
"""
1、不可链接vpn；
2、本地链接未实现相关功能(F:\自动化学习\selenium\自学\selenium其他操作\百度一下，你就知道.html)；
"""
wd.implicitly_wait(10)

# 1、创建一个ActionChains对象（翻译：动作链）
ac = ActionChains(wd)

# 2、将鼠标移动到可扩展的元素上去
ac.move_to_element(wd.find_element(By.NAME, 'tj_briicon')).perform()

pass
