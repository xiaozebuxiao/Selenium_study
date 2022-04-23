#!/usr/bin/python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# 导入Select模块
from selenium.webdriver.support.ui import Select

wd = webdriver.Chrome(service=Service(r'E:\chromedriver\chromedriver.exe'))
wd.get(r'F:\自动化学习\selenium\自学\选择框\白月黑羽：web自动化 - 选择框.html')
wd.implicitly_wait(10)

# -------------单选框-----------------

# 创建select对象
# select = Select(wd.find_element(By.ID, 'ss_single'))
# 通过select对象选中小雪老师
# select.select_by_visible_text('小雷老师')

# -----------多选框--------------

# 1、先清除原来就选中的元素
select = Select(wd.find_element(By.CSS_SELECTOR, '#ss_multi'))
select.deselect_all()
# 2、再选择想要选择的元素
select.select_by_visible_text('小雷老师')
select.select_by_visible_text('小凯老师')

wd.quit()