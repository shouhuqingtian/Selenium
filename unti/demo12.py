# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.baidu.com')
        sleep(1)

    def test01(self):
        self.driver.execute_script('alert("Hello World!")')
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test02(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)

    def test03(self):
        self.driver.get('https://www.sogou.com')
        # js = 'var q = document.getElementById("kw"); q.style.border="2px solid red"'
        # js = "var q=document.getElementById(\'kw\'); q.style.border=\'3px solid green\';"
        # self.driver.execute_script(js)
        js = 'var q=document.getElementById("query");q.style.border="2px solid red"'
        self.driver.execute_script(js)
        sleep(2)

    def test04(self):   # 滚动条
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(2)


if __name__ == '__main__':
    case = TestCase()
    # case.test01()
    # case.test02()
    # case.test03()
    case.test04()
    case.driver.quit()