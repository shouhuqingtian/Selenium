# -*- coding:utf-8 -*-
import time

from selenium import webdriver
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = path + r'\forms.html'
        self.driver.get(file_path)

    def test_login(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('liu')
        password = self.driver.find_element_by_id('pwd')
        password.send_keys('123456')
        time.sleep(1)
        self.driver.find_element_by_id('submit').click()
        self.driver.switch_to.alert.accept()
        name = username.get_attribute('value')
        word = password.get_attribute('value')
        print(name, word)
        username.clear()
        password.clear()
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_login()