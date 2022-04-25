#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get(r'F:\自动化学习\selenium\自学\xpath选择元素\白月黑羽：xpath选择.html')
wd.implicitly_wait(10)

# 使用xpath绝对路径获取p标签的“纽约”
# element = wd.find_element(By.XPATH, '/html/body/div/div/div[2]/span[1]/p[1]')
# print(element.text)


element_china = wd.find_element(By.ID, 'china')
# 通过webelement对象获取元素,必须要在webelement对象的xpath表达式前面加“.”(.//p);
element_ps = element_china.find_elements(By.XPATH, './/p')

for element_p in element_ps:
    print(element_p.text)

pass


