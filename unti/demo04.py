# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')

    def test_webelement_prop(self):
        t = self.driver.find_element_by_id('t1')
        t1 = WebElement
        print(type(t))
        print(t.id)
        print(t.tag_name)
        print(t.size)
        print(t.rect)
        print(t.text)
        print(t.location)
        self.driver.quit()

    def test_webelement_method(self):
        t = self.driver.find_element_by_id('t1')
        t.send_keys('hello world')
        time.sleep(1)
        print(t.get_attribute('type'))
        print(t.get_attribute('name'))
        print(t.get_attribute('value'))
        print(t.value_of_css_property('font'))
        print(t.value_of_css_property('color'))
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_webelement_prop()
    case.test_webelement_method()