# -*- coding:utf-8 -*-
from selenium import webdriver
import os
import time


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://sahitest.com/demo/clicks.htm')


    def test_mouse(self):
