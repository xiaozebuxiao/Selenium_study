#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 创建webdriver对象
wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))

# 方案一：隐式等待,用于处理服务器返回页面延迟的问题
wd.implicitly_wait(5)

# 通过webdriver对象的get方法获得整个页面
wd.get('https://www.byhy.net/_files/stock1.html')

# 查询带有“通讯”的股票
element_kw = wd.find_element(By.ID, "kw")
element_kw.send_keys("通讯")

element_go = wd.find_element(By.ID, "go")
element_go.click()

# -------------------------------------------------------------
# 方案二：
# import time
#
# while True:
#     try:
#         elements = wd.find_element(By.CLASS_NAME, 'result-item')
#         for element in elements:
#             print(element.text)
#     except:
#         time.sleep(1)
# -------------------------------------------------------------

# 打印查询的结果
elements = wd.find_elements(By.CLASS_NAME, 'result-item')
for element in elements:
    print(element.text)

wd.quit()

