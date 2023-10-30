#!/usr/bin/python
#-*-coding=UTF-8-*-
import os
import time
import unittest
from BeautifulReport import BeautifulReport



def time_stamp():
    return time.strftime("%Y%m%d_%H%M%S",time.localtime())

current_path = os.path.abspath(__file__)
testcases_path = os.path.join(current_path,"..","..","test_cases")
suite=unittest.defaultTestLoader.discover(start_dir=testcases_path,pattern="test*")
report_path = os.path.join(current_path,"..","..","reports")
BeautifulReport(suite).report(description="测试用例执行报告",filename=f"report_{time_stamp()}",report_dir=report_path)