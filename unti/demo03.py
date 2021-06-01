# -*- coding:utf-8 -*-
import time

from selenium import webdriver


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.baidu.com')

    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        # print(self.driver.page_source)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('六一儿童节')
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        self.driver.forward()
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_prop()
    case.test_method()
