# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.baidu.com')
        time.sleep(1)

    def test_sleep(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(1)

    def test_implicitly(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

    def test_wait(self):
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.title_contains('百度一下'))
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()


if __name__ == '__main__':
    case = TestCase()
    # case.test_sleep()
    # case.test_implicitly()
    case.test_wait()
    case.driver.quit()

