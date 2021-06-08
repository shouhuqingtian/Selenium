# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://sahitest.com/demo/clicks.htm')

    def test_mouse(self):
        btn = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        ActionChains(self.driver).double_click(btn).perform()
        sleep(2)

        btn = self.driver.find_element_by_xpath('//input[@value="click me"]')
        ActionChains(self.driver).click(btn).perform()
        sleep(2)

        btn = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        ActionChains(self.driver).context_click(btn).perform()
        sleep(2)

    def test_keys(self):
        self.driver.get('https://www.baidu.com')
        sleep(2)
        # ActionChains(self.driver).key_down(self.driver, (Keys.COMMAND, 'r')).perform()
        kw = self.driver.find_element_by_id('kw')
        kw.send_keys(Keys.TAB)
        kw.send_keys('selenium')
        kw.send_keys(Keys.CONTROL, 'a')

        sleep(1)
        kw.send_keys(Keys.F5)
        sleep(2)

        kw.send_keys(Keys.CONTROL, 'x')
        sleep(2)

        kw.send_keys(Keys.CONTROL, 'v')
        sleep(2)

    def test_move(self):
        self.driver.get('https://www.baidu.com')
        e = self.driver.find_element_by_id("s-usersetting-top")
        ActionChains(self.driver).move_to_element(e).click(e).perform()
        sleep(2)


if __name__ == '__main__':
    case = TestCase()
    # case.test_mouse()
    # case.test_keys()
    case.test_move()
    case.driver.quit()
