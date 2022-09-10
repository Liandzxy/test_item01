"""
    实现登录接口对象封装
"""
# 导包
import requests


# 新建类 登录接口对象
class ApiLogin(object):

    # 新建方法 登录方法
    def api_post_login(self, url, username, password):
        headers = {"Content-Type": "application/json"}
        data = {"username": username, "password": password}
        return requests.post(url, headers=headers, json=data)
