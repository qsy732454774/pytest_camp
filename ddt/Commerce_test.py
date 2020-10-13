# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/13 22:07
@Author      : QSY
@Funtion    : 输入模块功能
"""

import time
import os

import pytest

from Web.webkeys import WebKey
from ddt.params import datas


class Test_Commerce:

    def setup_class(self):

        self.web = WebKey()
        self.web.openBrowser()

    @pytest.mark.parametrize('listcases',datas['loginPage'])
    def test_login(self, listcases):
        '''self.web.geturl("http://testingedu.com.cn:8000/index.php/Home/user/login.html")
        self.web.input('//*[@id="username"]',"13800138006")
        self.web.input('//*[@id="password"]',"123456")
        self.web.input('//*[@id="verify_code"]',"1234")
        self.web.click('//a[contains(text(),"登")]')'''

        testcases = listcases['cases']
        for cases in testcases:
            listcase = list(cases.values())
            func = getattr(self.web,listcase[0])
            values = listcases[2:]
            func(*values)

    def test_Userinfo(self):
        time.sleep(1)
        self.web.geturl("http://testingedu.com.cn:8000/index.php/Home/User/info.html")
        self.web.click('//*[@id="preview"]')
        # 切换iframe
        time.sleep(1)
        self.web.intoifrem('//*[@id="layui-layer-iframe1"]')
        """abspath = os.getcwd()
        filepath = os.path.join(abspath, "123.jpg")"""
        # 上传图片
        self.web.input('//*[@id="filePicker"]/div[2]/input',"C:\\Users\\钱思远\\PycharmProjects\\pytest_camp\\lib\\images\\123.jpg")
        self.web.click('//*[@id="uploader"]/div[1]/div[3]/div[3]')
        # self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div[2]/form/ul[5]/li[2]/div[3]/input').click()

    def teardown_class(self):
        self.web.quit()
