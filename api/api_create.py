"""
    实现创建项目接口对象封装
"""

# 导包
import requests


# 新建创建项目接口对象
class ApiCreate(object):

    # 新建创建项目方法
    def api_post_create(self, url, headers, data):

        return requests.post(url, headers=headers, json=data)
