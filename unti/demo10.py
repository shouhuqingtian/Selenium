# -*- coding:utf-8 -*-
import time

from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        # path = os.path.dirname(os.path.abspath(__file__))
        # path_name = path + r"\test_wait.html"
        # self.driver.get(path_name)
        self.driver.get('https://www.baidu.com')

    def test(self):
        self.driver.find_element_by_id('btn').click()
        # 显示等待
        # time.sleep(4)
        wait = WebDriverWait(self.driver, 5)
        # wait.until(EC.title_contains(''))
        # print((EC.text_to_be_present_in_element('id', 'id2').text, 'id2'))

        # wait.until(EC.text_to_be_present_in_element('id', 'id2'), 1)
        print(WebDriverWait(self.driver, 5).until(text_to_be_present_in_element('id', 'id2'), 1))
        # print(EC.text_to_be_present_in_element('id', 'id2').text)
        # print(self.driver.find_element_by_id('id2').text)
        print('ok')


if __name__ == '__main__':
    case = TestCase()
    case.test()