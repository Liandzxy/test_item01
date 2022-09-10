"""
    注册业务层实现
"""


# 导包 unittest ApiRegister
import unittest
from api.api_register import ApiRegister
from parameterized import parameterized
from tools.read_register_json import ReadJson

# 新建读取数据函数
def get_data():
    datas = ReadJson("register.json").read_json()
    arrs = []
    # 使用遍历
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("username"),
                     data.get("password1"),
                     data.get("password2"),
                     data.get("expect_result"),
                     data.get("status_code")))
    return arrs


# 新建测试类
class TestRegister(unittest.TestCase):

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_register(self, url, username, password1, password2, except_result, status_code):

        # # 暂存数据
        # url = "http://quick.testpub.cn/api/v1/register/"
        # username = "abcgtwam"
        # password1 = "123"
        # password2 = "123"

        # 调用登录方法
        s = ApiRegister().api_post_register(url, username, password1, password2)
        print("查看响应结果：", s.json())
        # 断言 响应信息 状态码
        self.assertEquals(except_result, str(s.json()['success']))
        self.assertEquals(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()