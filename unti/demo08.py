# -*- coding:utf-8 -*-
from selenium import webdriver
import os
import time


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        path = os.path.dirname(os.path.abspath(__file__))
        path_name = path + r'\test_alert.html'
        self.driver.get(path_name)