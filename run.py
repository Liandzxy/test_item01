# 导包
import time
import unittest
from HtmlTestRunner import HTMLTestRunner


suite = unittest.defaultTestLoader.discover("./case", pattern="test_login.py")

file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d_%H_%M_%S"))

with open(file_path, "w") as f:
    HTMLTestRunner(stream=f).run(suite)
