# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/21 10:54
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：数据驱动实例讲解
"""


class A:

    def a(self, p1):
        """
        完成功能a
        :param p1: 所需参数
        :return: 返回结果
        """
        print("完成功能a" + str(p1))
        return 'PASS', '相关信息'

    def b(self, p1, p2):
        """
        完成功能a
        :param p1: 所需参数
        :return: 返回结果
        """
        print("完成功能b" + str(p1))
        print(p2)
        return 'PASS', '相关信息'

    def c(self, p1, p2, p3):
        """
        完成功能a
        :param p1: 所需参数
        :return: 返回结果
        """
        print("完成功能c" + str(p1))
        print(p2)
        print(p3)
        return 'PASS', '相关信息'


# 网上的数据驱动
params = [
    ['aaa'],
    ['bbb', 'bbb'],
    ['cccc', 'cccc', 'cccc']
]

obj = A()

obj.a(*params[0])
obj.b(*params[1])
obj.c(*params[2])

# 真正的数据驱动
params = [
    ['a', 'aaa'],
    ['b', 'bbb', 'bbb'],
    ['c', 'cccc', 'cccc', 'cccc'],
]

obj = A()
for p in params:
    try:

        func = getattr(obj,p[0])
        func(*p[1:])
    except Exception as e:
        print("功能暂未实现" % p)

