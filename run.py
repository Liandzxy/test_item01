# 导包
import time
import unittest
import HtmlTestRunner


suite = unittest.defaultTestLoader.discover("./case", pattern="test_login.py")

file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))

with open(file_path, "wb") as f:
    HtmlTestRunner(stream=f).run(suite)