import unittest

from .processPoolUtil import *
from .__init__ import *


class TestProcessPoolUtil(unittest.TestCase):

    def test_1(self):
        pass
        def 任务函数(参数):
            print("任务函数",参数)
            return 参数

        任务池 = 进程池(4)
        result = []
        for url in range(10):
            task = 任务池.投递任务(任务函数, (url))
            result.append(task)

        延时(2)

        for res in result:
            try:
                data = 任务池.进程池_取返回值(res)
                print(data)
            except:
                print("出错了")

        任务池.进程池_停止添加子进程()
        任务池.进程池_终止所有子进程()



    def test_2(self):
        def 任务函数(参数):
            print("任务函数",参数)
            return 参数

        x = 进程_创建(任务函数)
        x.进程_启动()
        x.进程_等待进程()
