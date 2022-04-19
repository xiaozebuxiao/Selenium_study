#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')
wd.implicitly_wait(10)

# 切换进入内部html
wd.switch_to.frame(wd.find_element(By.TAG_NAME, 'iframe'))

elements_frame = wd.find_elements(By.CSS_SELECTOR, '.animal > span')
for element_frame in elements_frame:
    print(element_frame.text)

# 切换回外层
wd.switch_to.default_content()

# 找到页面中所有id为outerbutton的元素，点击一下
elements_default = wd.find_elements(By.ID, 'outerbutton')
for element_default in elements_default:
    i = 1
    while i <= 10:
        element_default.click()
        # 找到点击后的结果，并打印
        element_click_results = wd.find_elements(By.TAG_NAME, 'li')
        for element_click_result in element_click_results:
            print(str(i) + element_click_result.text)
            i += 1

wd.quit()
