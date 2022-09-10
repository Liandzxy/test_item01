"""
    登录业务层实现
"""

# 导包
import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_login_json import ReadJson


def get_data():
    datas = ReadJson("login.json").read_json()
    arrs = []
    # 使用遍历
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("username"),
                     data.get("password"),
                     data.get("expect_result"),
                     data.get("status_code")))
    return arrs

# 新建测试类
class TestLogin(unittest.TestCase):

    @parameterized.expand(get_data())
    # 新建测试方法
    def test_login(self, url, username, password, expect_result, status_code):
        # # 暂存数据
        # url = "http://quick.testpub.cn/api/v1/login/"
        # username = "admin"
        # password = "admin123456"

        # 调用登录方法
        s = ApiLogin().api_post_login(url, username, password)
        print("查看响应结果：", s.json())
        # 断言
        self.assertEquals(expect_result, str(s.json()["success"]))
        self.assertEquals(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()