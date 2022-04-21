#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get('F:\自动化学习\selenium\自学\窗口切换\白月黑羽测试网页3.html')
wd.implicitly_wait(10)

elements = wd.find_elements(By.TAG_NAME, 'a')

for element in elements:
    element.click()

    # 获取当前窗口的句柄并保存，方便后续返回
    first_window = wd.current_window_handle

    # 获取当前页面所有的句柄
    for handle in wd.window_handles:
        # 根据句柄，切换到对应窗口
        wd.switch_to.window(handle)
        # 判断这个窗口是不是我们想要操作的窗口
        if '必应' in wd.title:
            break

    print(wd.title)

    # 根据提前保存的原窗口的句柄，切换回原窗口
    wd.switch_to.window(first_window)
    wd.switch_to.window(first_window)

    # 点击“功能按钮”，打印结果
    element_function_button = wd.find_element(By.ID, 'outerbutton')
    element_function_button.click()
    element_result = wd.find_element(By.TAG_NAME, 'li')
    print(element_result.text)

# wd.quit()
pass
