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

    def test_alert(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.driver.switch_to.alert
        time.sleep(1)
        print(alert.text)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        confirm = self.driver.switch_to.alert
        time.sleep(1)
        print(confirm.text)
        # confirm.accept()
        confirm.dismiss()

    def test_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        prompt = self.driver.switch_to.alert
        time.sleep(3)
        print(prompt.text)
        prompt.accept()
        # prompt.dismiss()


if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()
    case.driver.quit()