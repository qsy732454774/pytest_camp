# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/11 20:58
@Author      : QSY
@Funtion    : web自动化实现
"""
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://testingedu.com.cn:8000/index.php/Home/user/login.html")
driver.find_element_by_xpath('//*[@id="username"]').send_keys("13800138006")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys("1234")
driver.find_element_by_xpath('//a[contains(text(),"登")]').click()

time.sleep(5)
driver.quit()
