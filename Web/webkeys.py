# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/12 23:11
@Author      : QSY
@Funtion    : 输入模块功能
"""

from selenium import webdriver
class WebKey:
    def __init__(self):
        self.driver = None

    def openBrowser(self,br='gc'):
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver = webdriver.Firefox()
        elif br == 'ie':
            self.driver = webdriver.Ie()
        else:
            print("浏览器暂不支持，请添加")

        self.driver.implicitly_wait(10)


    def geturl(self,url=None):
        self.driver.get(url)

    def click(self,locator=None):
        self.driver.find_element_by_xpath(locator).click()

    def input(self,locator=None,value=None):
        self.driver.find_element_by_xpath(locator).send_keys(value)


