"""
    创建项目业务层实现
"""

# 导包
import unittest
from api.api_create import ApiCreate


# 新建测试类
class TestCreate(unittest.TestCase):

    # 新建测试方法
    def test_create(self):
        # 暂存数据
        url = "http://quick.testpub.cn/api/v1/project/"
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer 90b1610b4c9b10c76ad5fd93a639dab18f201767"
                   }
        data = {"name": "55555", "describe": "5555"}
        # 调用创建方法
        s = ApiCreate().api_post_create(url, headers, data)
        print("查看响应结果：", s.json())
        self.assertEquals(200, s.status_code)

if __name__ == '__main__':
    unittest.main()
