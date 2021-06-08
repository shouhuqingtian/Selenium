# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep, strftime, localtime, time
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.baidu.com')
        sleep(1)

    def test01(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        st = strftime('%Y-%m-%d-%H-%M-%S', localtime(time()))
        file_name = st + '.png'
        self.driver.save_screenshot(file_name)

    def test03(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        st = strftime('%Y-%m-%d-%H-%M-%S', localtime(time()))
        file_name = st + '.png'
        path = os.path.abspath('screenshot')
        file_path = path + '/' + file_name
        print(file_path)
        self.driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    case = TestCase()
    # case.test01()
    case.test03()
    case.driver.quit()