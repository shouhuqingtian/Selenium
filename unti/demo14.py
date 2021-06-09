# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://sahitest.com/demo/framesTest.htm')
        sleep(1)

    def test01(self):
        top = self.driver.find_element_by_xpath('/html/frameset/frame[2]')
        self.driver.switch_to.frame(top)    # 切换frame
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[5]').click()
        self.driver.switch_to.default_content()    # 切换默认frame
        sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_name('top'))
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[2]').click()
        sleep(2)


if __name__ == '__main__':
    case = TestCase()
    case.test01()
    case.driver.quit()
