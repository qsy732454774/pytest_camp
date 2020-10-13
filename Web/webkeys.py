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

    def openBrowser(self, br='gc'):
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver = webdriver.Firefox()
        elif br == 'ie':
            self.driver = webdriver.Ie()
        else:
            print("浏览器暂不支持，请添加")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def geturl(self, url=None):
        self.driver.get(url)

    def click(self, locator=None):
        ele = self.__find_ele(locator)
        ele.click()

    def input(self, locator=None, value=None):
        ele = self.__find_ele(locator)
        ele.send_keys(str(value))

    def __find_ele(self, locator=''):
        ele = None
        self.ele = None
        if locator.startswith('xpath='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=') + 1:]
            )
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_id(
                locator[locator.find('=') + 1:]
            )
        elif locator.startswith('name='):
            ele = self.driver.find_element_by_name(
                locator[locator.find('=') + 1:]
            )
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_id(
                locator[locator.find('=') + 1:]
            )
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_id(
                locator[locator.find('=') + 1:]
            )
        else:
            ele = self.driver.find_element_by_xpath(locator)

        self.ele = ele
        return ele

    def intoifrem(self,locator=None):
        ele = self.__find_ele(locator)
        self.driver.switch_to.frame(ele)

    def quit(self):
        self.driver.quit()
