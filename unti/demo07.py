# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import os
from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        path = os.path.dirname(os.path.abspath(__file__))
        path_name = path + r'\forms3.html'
        self.driver.get(path_name)

    def test_select(self):  # 下拉式选择器
        e = self.driver.find_element_by_id('provise')
        select = Select(e)
        select.select_by_index(2)
        time.sleep(1)
        select.select_by_value('tj')
        time.sleep(1)
        select.select_by_visible_text('Beijing')
        time.sleep(1)
        self.driver.quit()

    def test_select_index(self):
        e = self.driver.find_element_by_id('provise')
        select = Select(e)
        # for i in range(3):
        #     select.select_by_index(i)
        #     time.sleep(1)
        # select.deselect_all()
        for i in select.options:
            print(i.text)


if __name__ == '__main__':
    case = TestCase()
    # case.test_select()
    case.test_select_index()