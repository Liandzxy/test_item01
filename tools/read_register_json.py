# 导包
import json


class ReadJson(object):
    def __init__(self, filename):
        self.filepath = "./data/" + filename

    def read_json(self):
        # 打开json文件获取内容
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载数据
            return json.load(f)


if __name__ == '__main__':
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
    print(arrs)
