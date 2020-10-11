# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/11 21:21
@Author      : QSY
@Funtion    : PO设计模式
"""
import time
import os

from selenium import webdriver


class Test_Comm:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login(self):
        self.driver.get("http://testingedu.com.cn:8000/index.php/Home/user/login.html")
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("13800138006")
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
        self.driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys("1234")
        self.driver.find_element_by_xpath('//a[contains(text(),"登")]').click()

    def test_Userinfo(self):
        time.sleep(1)
        self.driver.get("http://testingedu.com.cn:8000/index.php/Home/User/info.html")
        self.driver.find_element_by_xpath('//*[@id="preview"]').click()
        # 切换iframe
        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]'))
        abspath = os.getcwd()
        filepath = os.path.join(abspath, "jpg.jpg")
        # 上传图片
        self.driver.find_element_by_xpath('//*[@id="filePicker"]/div[2]/input')\
            .send_keys(filepath)
        self.driver.find_element_by_xpath('//*[@id="uploader"]/div[1]/div[3]/div[3]').click()
        # self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div[2]/form/ul[5]/li[2]/div[3]/input').click()

    def teardown_class(self):
        self.driver.quit()


