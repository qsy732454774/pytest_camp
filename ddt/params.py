# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/13 22:53
@Author      : QSY
@Funtion    : 输入模块功能
"""
import yaml

datas = None

with open('./lib/cases/cases.yaml', encoding='utf8') as f:
    datas = yaml.safe_load(f)

print(datas)