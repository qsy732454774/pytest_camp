# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/11 23:03
@Author      : QSY
@Funtion    : 运行入口
"""
import os

import pytest

pytest.main(['-s','Web/test_example2.py','--alluredir','./temp','--reruns','2'])
os.system('allure generate ./temp -o ./report --clean')
