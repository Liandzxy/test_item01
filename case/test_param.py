# 导包
import unittest
from parameterized import parameterized


# 新建测试类
class TestParam(unittest.TestCase):
    @parameterized.expand([()])
    # 新建测试方法
    def test_param(self,username,password):
        print("用户名：",username)
        print("密码：", password)