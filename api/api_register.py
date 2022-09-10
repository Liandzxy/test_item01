"""
    实现注册接口对象封装
"""

# 导包
import requests


# 新建类 注册接口对象
class ApiRegister(object):

    # 新建方法 注册方法
    def api_post_register(self, url, username, password1, password2):
        # headers 定义
        headers = {"Content-Type": "application/json"}
        # data 定义
        data = {"username": username, "password1": password1, "password2": password2}
        # 调用post并返回响应对象
        return requests.post(url, headers=headers, json=data)


"""
    url,username,password1,password2 都需要从data数据读取，所以这里使用动态传参
"""
