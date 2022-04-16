#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 引用Chrome的类，创建webdriver的对象。如同控制浏览器的遥控器(Chrome中首字母必须大写)
wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))

# 使用WebDriver对象的get方法打开指定的网站
wd.get("https://www.byhy.net/_files/stock1.html")

# 根据id选择元素，返回改元素对应的WebElement对象
element = wd.find_element(by=By.ID, value="kw")
element.send_keys("四川")

element = wd.find_element(by=By.ID, value="go")
element.click()

# 通过WebElement对象，针对页面元素进行操作
# element.send_keys("眉州东坡\n")  # 模拟输入，\n是回车的意思

# # 关闭缺省是日志
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# wd = webdriver.Chrome(executable_path='<path-to-chrome>', options=options)  # 这里指定 options 参数

wd.quit()
