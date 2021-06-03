# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        path = os.path.dirname(os.path.abspath(__name__))
        file_path = path + r'\forms2.html'
        self.driver.get(file_path)

    def test_checkbox(self):
        swim = self.driver.find_element_by_name('swimming')
        read = self.driver.find_element_by_name('reading')
        if not swim.is_selected():
            swim.click()
        if not read.is_selected():
            read.click()
        time.sleep(1)
        swim.click()
        read.click()
        self.driver.quit()

    def test_radio(self):
        lst = self.driver.find_elements_by_name('gender')
        lst[1].click()


if __name__ == '__main__':
    case = TestCase()
    # case.test_checkbox()
    case.test_redio()